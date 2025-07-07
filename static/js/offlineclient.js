"use strict";

{
    class s {
        constructor() {
            this._broadcastChannel = (typeof BroadcastChannel === "undefined") ? null : new BroadcastChannel("offline");
            this._queuedMessages = [];
            this._onMessageCallback = null;

            if (this._broadcastChannel) {
                this._broadcastChannel.onmessage = (s) => this._OnBroadcastChannelMessage(s);
            }
        }

        _OnBroadcastChannelMessage(s) {
            if (this._onMessageCallback) {
                this._onMessageCallback(s);
            } else {
                this._queuedMessages.push(s);
            }
        }

        SetMessageCallback(s) {
            this._onMessageCallback = s;

            for (let msg of this._queuedMessages) {
                this._onMessageCallback(msg);
            }

            this._queuedMessages.length = 0;
        }
    }

    window.OfflineClientInfo = new s();
}
