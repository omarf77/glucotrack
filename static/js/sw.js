"use strict";

const OFFLINE_DATA_FILE = "/static/json/offline.json";
const CACHE_NAME_PREFIX = "c3offline";
const BROADCASTCHANNEL_NAME = "offline";
const CONSOLE_PREFIX = "[SW] ";
const LAZYLOAD_KEYNAME = "";
const broadcastChannel = (typeof BroadcastChannel === "undefined") ? null : new BroadcastChannel("offline");

class PromiseThrottle {
    constructor(e) {
        this._maxParallel = e;
        this._queue = [];
        this._activeCount = 0;
    }

    Add(e) {
        return new Promise((t, a) => {
            this._queue.push({ func: e, resolve: t, reject: a });
            this._MaybeStartNext();
        });
    }

    async _MaybeStartNext() {
        if (!this._queue.length || this._activeCount >= this._maxParallel) return;
        this._activeCount++;
        const e = this._queue.shift();
        try {
            const t = await e.func();
            e.resolve(t);
        } catch (t) {
            e.reject(t);
        }
        this._activeCount--;
        this._MaybeStartNext();
    }
}

const networkThrottle = new PromiseThrottle(20);

function PostBroadcastMessage(e) {
    if (broadcastChannel) {
        setTimeout(() => broadcastChannel.postMessage(e), 3000);
    }
}

function Broadcast(e) {
    PostBroadcastMessage({ type: e });
}

function BroadcastDownloadingUpdate(e) {
    PostBroadcastMessage({ type: "downloading-update", version: e });
}

function BroadcastUpdateReady(e) {
    PostBroadcastMessage({ type: "update-ready", version: e });
}

function IsUrlInLazyLoadList(e, t) {
    if (!t) return false;
    try {
        for (const a of t) {
            if (new RegExp(a).test(e)) return true;
        }
    } catch (e) {
        console.error("[SW] Error matching in lazy-load list: ", e);
    }
    return false;
}

function WriteLazyLoadListToStorage(e) {
    return (typeof localforage === "undefined") ? Promise.resolve() : localforage.setItem("", e);
}

function ReadLazyLoadListFromStorage() {
    return (typeof localforage === "undefined") ? Promise.resolve([]) : localforage.getItem("");
}

function GetCacheBaseName() {
    return "c3offline-" + self.registration.scope;
}

function GetCacheVersionName(e) {
    return GetCacheBaseName() + "-v" + e;
}

async function GetAvailableCacheNames() {
    const e = await caches.keys();
    const t = GetCacheBaseName();
    return e.filter(name => name.startsWith(t));
}

async function IsUpdatePending() {
    return (await GetAvailableCacheNames()).length >= 2;
}

async function GetMainPageUrl() {
    const e = await clients.matchAll({ includeUncontrolled: true, type: "window" });
    for (const t of e) {
        let url = t.url;
        if (url.startsWith(self.registration.scope)) {
            url = url.substring(self.registration.scope.length);
        }
        if (url && url !== "/") {
            if (url.startsWith("?")) url = "/" + url;
            return url;
        }
    }
    return "";
}

function fetchWithBypass(e, t) {
    if (typeof e === "string") {
        e = new Request(e);
    }
    return t
        ? fetch(e.url, {
            headers: e.headers,
            mode: e.mode,
            credentials: e.credentials,
            redirect: e.redirect,
            cache: "no-store"
        })
        : fetch(e);
}

async function CreateCacheFromFileList(e, t, a) {
    const n = await Promise.all(t.map(u => networkThrottle.Add(() => fetchWithBypass(u, a))));
    let success = true;

    for (const res of n) {
        if (!res.ok) {
            success = false;
            console.error(`[SW] Error fetching '${res.url}' (${res.status} ${res.statusText})`);
        }
    }

    if (!success) throw new Error("not all resources were fetched successfully");

    const cache = await caches.open(e);
    try {
        return await Promise.all(n.map((res, i) => cache.put(t[i], res)));
    } catch (t) {
        console.error("[SW] Error writing cache entries: ", t);
        caches.delete(e);
        throw t;
    }
}

async function UpdateCheck(e) {
    try {
        const t = await fetchWithBypass("/static/json/offline.json", true);
        if (!t.ok) throw new Error(`/static/json/offline.json responded with ${t.status} ${t.statusText}`);
        const a = await t.json();
        const n = a.version;
        const o = a.fileList;
        const s = a.lazyLoad;
        const r = GetCacheVersionName(n);

        if (await caches.has(r)) {
            const msg = await IsUpdatePending() ? "update-pending" : "up-to-date";
            console.log(`[SW] ${msg === "update-pending" ? "Update pending" : "Up to date"}`);
            Broadcast(msg);
            return;
        }

        const i = await GetMainPageUrl();
        o.unshift("./");
        if (i && !o.includes(i)) o.unshift(i);

        console.log(`[SW] Caching ${o.length} files for offline use`);
        e ? Broadcast("downloading") : BroadcastDownloadingUpdate(n);
        if (s) await WriteLazyLoadListToStorage(s);
        await CreateCacheFromFileList(r, o, !e);

        const ready = await IsUpdatePending();
        console.log(`[SW] All resources saved, ${ready ? "update ready" : "offline support ready"}`);
        ready ? BroadcastUpdateReady(n) : Broadcast("offline-ready");

    } catch (e) {
        console.warn("[SW] Update check failed: ", e);
    }
}

async function GetCacheNameToUse(e, t) {
    if (e.length === 1 || !t) return e[0];
    if ((await clients.matchAll()).length > 1) return e[0];
    const latest = e[e.length - 1];
    console.log("[SW] Updating to new version");
    await Promise.all(e.slice(0, -1).map(name => caches.delete(name)));
    return latest;
}

async function HandleFetch(e, t) {
    const a = await GetAvailableCacheNames();
    if (!a.length) return fetch(e.request);
    const n = await GetCacheNameToUse(a, t);
    const o = await caches.open(n);
    const s = await o.match(e.request);
    if (s) return s;

    const [fetched, lazyList] = await Promise.all([fetch(e.request), ReadLazyLoadListFromStorage()]);
    if (IsUrlInLazyLoadList(e.request.url, lazyList)) {
        try {
            await o.put(e.request, fetched.clone());
        } catch (err) {
            console.warn(`[SW] Error caching '${e.request.url}': `, err);
        }
    }

    return fetched;
}

self.addEventListener("install", e => {
    e.waitUntil(UpdateCheck(true).catch(() => null));
});

self.addEventListener("fetch", e => {
    if (new URL(e.request.url).origin !== location.origin) return;
    const t = e.request.mode === "navigate";
    const promise = HandleFetch(e, t);
    if (t) e.waitUntil(promise.then(() => UpdateCheck(false)));
    e.respondWith(promise);
});
