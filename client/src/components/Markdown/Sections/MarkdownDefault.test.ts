import { createTestingPinia } from "@pinia/testing";
import { mount } from "@vue/test-utils";
import flushPromises from "flush-promises";
import { getLocalVue } from "tests/jest/helpers";

import { sanitizeHtml } from "@/directives/sanitizeHtml";

import MarkdownDefault from "./MarkdownDefault.vue";

jest.mock("@/onload/loadConfig", () => ({ getAppRoot: () => "/galaxy/" }));

describe("MarkdownDefault", () => {
    it("renders through v-sanitize-html with the markdown profile and still rewrites gx links", async () => {
        jest.mocked(sanitizeHtml).mockClear();
        const wrapper = mount(MarkdownDefault as object, {
            localVue: getLocalVue(),
            pinia: createTestingPinia({ createSpy: jest.fn }),
            propsData: { content: "See [a term](gxhelp://dataset) and <em>raw</em>" },
            stubs: { MarkdownHelpPopovers: true },
        });
        await flushPromises();

        const [html, profile] = jest.mocked(sanitizeHtml).mock.calls[0]!;
        expect(profile).toBe("markdown");
        expect(html).toContain('<a href="gxhelp://dataset">a term</a>');
        expect(html).toContain("&lt;em&gt;raw&lt;/em&gt;");
        expect(wrapper.find(".text-justify a").attributes("href")).toBe("/galaxy/help/terms/dataset");
    });
});
