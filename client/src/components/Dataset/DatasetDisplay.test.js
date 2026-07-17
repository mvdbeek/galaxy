import { createTestingPinia } from "@pinia/testing";
import { getLocalVue } from "@tests/vitest/helpers";
import { mount } from "@vue/test-utils";
import flushPromises from "flush-promises";
import { afterEach, describe, expect, it, vi } from "vitest";

import { useDatasetStore } from "@/stores/datasetStore";

import DatasetDisplay from "./DatasetDisplay.vue";

const DATASET_ID = "dataset_id";
const SECOND_DATASET_ID = "second_dataset_id";
const localVue = getLocalVue();

function deferredResponse() {
    let resolve;
    const promise = new Promise((promiseResolve) => {
        resolve = promiseResolve;
    });
    return { promise, resolve };
}

function mountDatasetDisplay() {
    const pinia = createTestingPinia({
        createSpy: vi.fn,
        stubActions: false,
    });
    const datasetStore = useDatasetStore(pinia);
    datasetStore.storedDatasets[DATASET_ID] = {
        id: DATASET_ID,
        name: "Test Dataset",
        state: "ok",
        file_ext: "txt",
        file_size: 12,
        peek: "preview",
    };
    datasetStore.storedDatasets[SECOND_DATASET_ID] = {
        id: SECOND_DATASET_ID,
        name: "Second Test Dataset",
        state: "ok",
        file_ext: "txt",
        file_size: 12,
        peek: "preview",
    };

    return mount(DatasetDisplay, {
        localVue,
        pinia,
        propsData: {
            datasetId: DATASET_ID,
            isBinary: false,
        },
        stubs: {
            FontAwesomeIcon: true,
        },
    });
}

afterEach(() => {
    vi.unstubAllGlobals();
});

describe("DatasetDisplay", () => {
    it("waits for the HEAD request before loading the preview iframe", async () => {
        const headResponse = deferredResponse();
        const fetchMock = vi.fn(() => headResponse.promise);
        vi.stubGlobal("localStorage", {
            getItem: vi.fn(() => null),
            removeItem: vi.fn(),
            setItem: vi.fn(),
        });
        vi.stubGlobal("fetch", fetchMock);

        const wrapper = mountDatasetDisplay();

        expect(fetchMock).toHaveBeenCalledWith(`/datasets/${DATASET_ID}/display/?preview=True`, {
            method: "HEAD",
            signal: expect.any(AbortSignal),
        });
        expect(wrapper.find("iframe").exists()).toBe(false);

        headResponse.resolve({ headers: new Headers() });
        await flushPromises();

        expect(wrapper.find("iframe").attributes("src")).toBe(`/datasets/${DATASET_ID}/display/?preview=True`);
    });

    it("aborts stale HEAD requests when the dataset changes", async () => {
        const firstHeadResponse = deferredResponse();
        const secondHeadResponse = deferredResponse();
        const fetchMock = vi
            .fn()
            .mockReturnValueOnce(firstHeadResponse.promise)
            .mockReturnValueOnce(secondHeadResponse.promise);
        vi.stubGlobal("localStorage", {
            getItem: vi.fn(() => null),
            removeItem: vi.fn(),
            setItem: vi.fn(),
        });
        vi.stubGlobal("fetch", fetchMock);

        const wrapper = mountDatasetDisplay();
        const firstRequestSignal = fetchMock.mock.calls[0][1].signal;

        await wrapper.setProps({ datasetId: SECOND_DATASET_ID });

        expect(firstRequestSignal.aborted).toBe(true);
        expect(fetchMock).toHaveBeenLastCalledWith(`/datasets/${SECOND_DATASET_ID}/display/?preview=True`, {
            method: "HEAD",
            signal: expect.any(AbortSignal),
        });
        expect(wrapper.find("iframe").exists()).toBe(false);

        secondHeadResponse.resolve({ headers: new Headers() });
        await flushPromises();

        expect(wrapper.find("iframe").attributes("src")).toBe(`/datasets/${SECOND_DATASET_ID}/display/?preview=True`);
    });
});
