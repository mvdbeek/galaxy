import { getLocalVue } from "@tests/vitest/helpers";
import { mount } from "@vue/test-utils";
import axios from "axios";
import flushPromises from "flush-promises";
import { describe, expect, it, vi } from "vitest";

import VisualizationFrame from "./VisualizationFrame.vue";

vi.mock("axios");
vi.mock("@/onload/loadConfig", () => ({ getAppRoot: () => "/" }));

describe("VisualizationFrame", () => {
    it("names a plugin without an entry point as text", async () => {
        const name = '../version#<img src="x">';
        vi.mocked(axios.get).mockResolvedValue({ data: {} });

        const wrapper = mount(VisualizationFrame as object, {
            localVue: getLocalVue(),
            propsData: { name, config: {} },
            attachTo: document.body,
        });
        await flushPromises();

        expect(axios.get).toHaveBeenCalledWith(`/api/plugins/${encodeURIComponent(name)}`);
        const body = (wrapper.find("iframe").element as HTMLIFrameElement).contentDocument!.body;
        expect(body.textContent).toContain(`Unable to locate plugin module for: ${name}.`);
        expect(body.querySelector("img")).toBeNull();
        wrapper.destroy();
    });
});
