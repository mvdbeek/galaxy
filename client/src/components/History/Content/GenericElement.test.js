import { createTestingPinia } from "@pinia/testing";
import { getLocalVue, suppressLucideVue2Deprecation } from "@tests/vitest/helpers";
import { mount } from "@vue/test-utils";
import { beforeEach, describe, expect, it, vi } from "vitest";
import VueRouter from "vue-router";

import { setupSelectableMock } from "@/components/ObjectStore/mockServices";

import GenericElement from "./GenericElement.vue";

vi.mock("components/History/model/queries");

setupSelectableMock();

const localVue = getLocalVue();
localVue.use(VueRouter);
const router = new VueRouter();

describe("GenericElement", () => {
    let wrapper;

    beforeEach(() => {
        suppressLucideVue2Deprecation();

        wrapper = mount(GenericElement, {
            propsData: {
                dsc: {
                    elements: [
                        {
                            element_index: 0,
                            element_identifier: "element-1",
                            element_type: "hda",
                            object: {
                                id: "item-1",
                            },
                        },
                        {
                            element_index: 1,
                            element_identifier: "element-2",
                            element_type: "hdca",
                            object: {
                                id: "item-2",
                                collection_type: "list",
                                element_count: 1,
                                elements_datatypes: ["txt"],
                                elements: [
                                    {
                                        element_index: 2,
                                        element_identifier: "element-3",
                                        element_type: "hda",
                                        object: {
                                            id: "item_3",
                                        },
                                    },
                                    {
                                        element_index: 3,
                                        element_identifier: "element-4",
                                        element_type: "hda",
                                        object: {
                                            id: "item_4",
                                        },
                                    },
                                ],
                            },
                        },
                    ],
                },
            },
            localVue,
            router,
            pinia: createTestingPinia({ createSpy: vi.fn }),
        });
    });

    it("check basics", async () => {
        const contentItems = wrapper.findAll(".content-item");
        expect(contentItems.length).toBe(2);
        expect(contentItems.at(0).attributes("data-hid")).toBe("1");
        expect(contentItems.at(1).attributes("data-hid")).toBe("2");
        await contentItems.at(1).find(".cursor-pointer").trigger("click");
        const contentExpanded = wrapper.findAll(".content-item");
        expect(contentExpanded.length).toBe(4);
        expect(contentExpanded.at(2).attributes("data-hid")).toBe("3");
        expect(contentExpanded.at(3).attributes("data-hid")).toBe("4");
    });
});

describe("GenericElement with paired collection", () => {
    let wrapper;

    beforeEach(() => {
        suppressLucideVue2Deprecation();

        wrapper = mount(GenericElement, {
            propsData: {
                dsc: {
                    elements: [
                        {
                            id: "dce-1",
                            element_index: 0,
                            element_identifier: "pair-1",
                            element_type: "dataset_collection",
                            object: {
                                id: "dc-1",
                                collection_type: "paired",
                                element_count: 2,
                                elements_datatypes: ["fastqsanger"],
                                elements: [
                                    {
                                        id: "dce-forward",
                                        element_index: 0,
                                        element_identifier: "forward",
                                        element_type: "hda",
                                        object: {
                                            id: "dataset-1",
                                            name: "forward.fastq",
                                        },
                                    },
                                    {
                                        id: "dce-reverse",
                                        element_index: 1,
                                        element_identifier: "reverse",
                                        element_type: "hda",
                                        object: {
                                            id: "dataset-2",
                                            name: "reverse.fastq",
                                        },
                                    },
                                ],
                            },
                        },
                    ],
                },
            },
            localVue,
            router,
            pinia: createTestingPinia({ createSpy: vi.fn }),
        });
    });

    it("clicking a paired collection element expands to show forward and reverse datasets", async () => {
        const contentItems = wrapper.findAll(".content-item");
        expect(contentItems.length).toBe(1);
        expect(contentItems.at(0).attributes("data-hid")).toBe("1");
        await contentItems.at(0).find(".cursor-pointer").trigger("click");
        const contentExpanded = wrapper.findAll(".content-item");
        expect(contentExpanded.length).toBe(3);
        expect(contentExpanded.at(1).attributes("data-hid")).toBe("1");
        expect(contentExpanded.at(2).attributes("data-hid")).toBe("2");
    });
});
