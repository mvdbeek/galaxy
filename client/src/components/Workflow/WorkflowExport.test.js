import { getLocalVue } from "@tests/vitest/helpers";
import { shallowMount } from "@vue/test-utils";
import flushPromises from "flush-promises";
import { beforeEach, describe, expect, it } from "vitest";
import { nextTick } from "vue";

import { HttpResponse, useServerMock } from "@/api/client/__mocks__";

import WorkflowExport from "./WorkflowExport.vue";

const localVue = getLocalVue();
const { server, http } = useServerMock();

function getHref(item) {
    return item.attributes("href");
}

describe("Workflow Export", () => {
    let wrapper;
    beforeEach(async () => {
        server.use(
            http.untyped.get("/api/workflows/0", () => {
                return HttpResponse.json({
                    id: "0",
                    name: "workflow",
                });
            }),
            http.untyped.get("/api/workflows/1", () => {
                return HttpResponse.json({
                    id: "1",
                    owner: "owner",
                    slug: "slug",
                    importable: true,
                });
            }),
        );
        wrapper = shallowMount(WorkflowExport, {
            propsData: {
                id: "0",
            },
            localVue,
        });
        await flushPromises();
        await nextTick();
    });

    it("verify display", async () => {
        let links = wrapper.findAll("a");
        expect(getHref(links.at(0))).toBe("/api/workflows/0/download?format=json-download");
        expect(getHref(links.at(1))).toBe("/workflow/gen_image?id=0");
        await wrapper.setProps({ id: "1" });
        await flushPromises();
        links = wrapper.findAll("a");
        expect(getHref(links.at(0))).toBe("http://localhost/u/owner/w/slug/json");
        expect(getHref(links.at(1))).toBe("/api/workflows/1/download?format=json-download");
        expect(getHref(links.at(2))).toBe("/workflow/gen_image?id=1");
    });

    it("allows choosing an explicit download format and returning to the server default", async () => {
        const select = wrapper.findComponent({ name: "BFormSelect" });
        expect(select.props("options")).toEqual([
            { value: "export", text: "Server default" },
            { value: "ga", text: "Galaxy native (.ga)" },
            { value: "format2", text: "gxformat2 (.gxwf.json)" },
        ]);
        for (const style of ["format2", "ga", "export"]) {
            select.vm.$emit("input", style);
            await nextTick();
            const suffix = style === "export" ? "" : `&style=${style}`;
            expect(getHref(wrapper.find("a"))).toBe(`/api/workflows/0/download?format=json-download${suffix}`);
            expect(wrapper.text().includes("gxformat2 exports currently omit")).toBe(style === "format2");
        }
    });
});
