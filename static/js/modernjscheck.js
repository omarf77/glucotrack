"use strict";

!function () {
    let p = !0;

    const result = (new class {
        #p = "pass";
        getProp() {
            return this.#p;
        }
    }).getProp();

    "pass" !== result && (p = !1);

    p && (window["C3_ModernJSSupport_OK"] = !0);
}();
