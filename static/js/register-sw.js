"use strict";

window.C3_RegisterSW = async function () {
    if (navigator.serviceWorker) {
        try {
            const registration = await navigator.serviceWorker.register("/static/js/sw.js", { scope: "./" });
            console.info("Registered service worker on " + registration.scope);
        } catch (e) {
            console.warn("Failed to register service worker: ", e);
        }
    }
};
