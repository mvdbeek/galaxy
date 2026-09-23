import { sanitizeHtml } from "@/directives/sanitizeHtml";

// The global test setup replaces this module with a pass-through spy; these
// tests run the real profiles through DOMPurify under jsdom.
jest.unmock("@/directives/sanitizeHtml");

function parse(html: string): HTMLElement {
    const container = document.createElement("div");
    container.innerHTML = html;
    return container;
}

describe("sanitizeHtml", () => {
    test("default profile removes scripts, event handlers, styles and form controls", () => {
        const clean = parse(
            sanitizeHtml(
                '<b>ok</b><img src="x" onerror="alert(1)"><script>alert(2)</script><style>*{}</style><form><input></form>',
            ),
        );
        expect(clean.querySelector("b")?.textContent).toBe("ok");
        expect(clean.querySelector("img")?.hasAttribute("onerror")).toBe(false);
        expect(clean.querySelector("script, style, form, input")).toBeNull();
    });

    test("null and undefined become empty strings", () => {
        expect(sanitizeHtml(null)).toBe("");
        expect(sanitizeHtml(undefined)).toBe("");
    });

    test("default profile drops target, links keeps it and adds noopener noreferrer", () => {
        const html = '<a href="https://x" target="_blank">x</a>';
        expect(parse(sanitizeHtml(html)).querySelector("a")?.hasAttribute("target")).toBe(false);
        const link = parse(sanitizeHtml(html, "links")).querySelector("a");
        expect(link?.getAttribute("target")).toBe("_blank");
        expect(link?.getAttribute("rel")).toBe("noopener noreferrer");
    });

    test("same-window targets get no rel", () => {
        const link = parse(sanitizeHtml('<a href="https://x" target="_self">x</a>', "links")).querySelector("a");
        expect(link?.hasAttribute("rel")).toBe(false);
    });

    test("markdown profile keeps Galaxy URIs and drops javascript: URIs", () => {
        const clean = parse(
            sanitizeHtml('<a href="gxhelp://dataset">a</a><a href="javascript:alert(1)">b</a>', "markdown"),
        );
        const [gx, js] = Array.from(clean.querySelectorAll("a"));
        expect(gx?.getAttribute("href")).toBe("gxhelp://dataset");
        expect(js?.hasAttribute("href")).toBe(false);
    });

    test("unknown profiles are rejected", () => {
        expect(() => sanitizeHtml("x", "nope" as never)).toThrow("Unknown v-sanitize-html profile: nope");
    });
});
