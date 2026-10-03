import { createTestingPinia } from "@pinia/testing";
import { getFakeRegisteredUser } from "@tests/test-data";
import { getLocalVue } from "@tests/vitest/helpers";
import { mount, type Wrapper } from "@vue/test-utils";
import flushPromises from "flush-promises";
import { afterEach, beforeEach, describe, expect, it, vi } from "vitest";
import type Vue from "vue";

import type { TourStep as TourStepType } from "@/api/tours";
import { useHistoryStore } from "@/stores/historyStore";
import { useTourStore } from "@/stores/tourStore";

import Tour from "./Tour.vue";
import TourStep from "./TourStep.vue";

vi.mock("app");
vi.mock("vue-router/composables", () => ({ useRouter: vi.fn() }));
vi.mock("@/composables/userLocalStorageFromHashedId", async () => {
    const { ref } = await import("vue");
    return { useUserLocalStorageFromHashId: (_key: string, initialValue: unknown) => ref(initialValue) };
});

const localVue = getLocalVue();
const steps: TourStepType[] = [
    { title: "Welcome", content: "An introduction to Galaxy." },
    { title: "Tools", content: "Find a tool to run." },
    { title: "Finished", content: "Enjoy Galaxy!" },
];

describe("Tour startup and playback", () => {
    let wrapper: Wrapper<Vue>;
    const onBefore = vi.fn<() => Promise<void>>();
    const onNext = vi.fn<() => Promise<void>>();

    beforeEach(() => {
        vi.useFakeTimers({ toFake: ["setTimeout", "clearTimeout"] });
        onBefore.mockReset().mockResolvedValue(undefined);
        onNext.mockReset().mockResolvedValue(undefined);
        mountTour();
    });

    function mountTour(historyReady = true) {
        const pinia = createTestingPinia({
            createSpy: vi.fn,
            stubActions: false,
            initialState: {
                historyStore: {
                    storedHistories: { "history-id": { id: "history-id", size: 0 } },
                    historiesLoading: false,
                },
                userStore: { currentUser: getFakeRegisteredUser() },
            },
        });
        if (historyReady) {
            useHistoryStore().setCurrentHistoryId("history-id");
        }
        useTourStore().setTour("test-tour");
        wrapper = mount(Tour as object, {
            localVue,
            pinia,
            propsData: { steps, requirements: [], tourId: "test-tour", onBefore, onNext },
            stubs: { GModal: true, FontAwesomeIcon: true },
        });
    }

    afterEach(() => {
        wrapper?.destroy();
        vi.useRealTimers();
    });

    async function advanceTime(milliseconds: number) {
        await vi.advanceTimersByTimeAsync(milliseconds);
        await flushPromises();
    }

    it("shows the first step while the history list is still loading", async () => {
        useHistoryStore().historiesLoading = true;
        await flushPromises();
        expect(useHistoryStore().historiesLoading).toBe(true);
        expect(wrapper.findComponent(TourStep).props("step")).toEqual(steps[0]);
        expect(wrapper.find(".tour-next").exists()).toBe(true);
        expect(wrapper.findComponent({ name: "GModal" }).exists()).toBe(false);
    });

    it("waits for the current history, then shows the tour without waiting for the list", async () => {
        wrapper.destroy();
        mountTour(false);
        const historyStore = useHistoryStore();
        historyStore.historiesLoading = true;
        await flushPromises();
        expect(wrapper.findComponent(TourStep).exists()).toBe(false);
        expect(wrapper.text()).toContain("Evaluating Requirements");

        historyStore.setCurrentHistoryId("history-id");
        await flushPromises();
        expect(wrapper.findComponent(TourStep).props("step")).toEqual(steps[0]);
    });

    it("still enforces tour requirements while the history list is loading", async () => {
        useHistoryStore().historiesLoading = true;
        useHistoryStore().currentHistory!.size = 1;
        await wrapper.setProps({ requirements: ["new_history"] });
        expect(wrapper.findComponent(TourStep).exists()).toBe(false);
        expect(wrapper.text()).toContain("please create a new history");
        window.dispatchEvent(new KeyboardEvent("keyup", { keyCode: 39 }));
        await flushPromises();
        expect(onNext).not.toHaveBeenCalled();
    });

    it("stays on each step until Continue is clicked by default", async () => {
        await advanceTime(60000);
        expect(useTourStore().currentTour?.step).toBe(0);
        await wrapper.find(".tour-next").trigger("click");
        await flushPromises();
        expect(useTourStore().currentTour?.step).toBe(1);
        expect(onNext).toHaveBeenCalledWith(steps[0]);
        expect(onBefore).toHaveBeenCalledWith(steps[1]);
        await advanceTime(60000);
        expect(useTourStore().currentTour?.step).toBe(1);
    });

    it("gives the current step reading time before auto-playing, and stops at the last step", async () => {
        await wrapper.find(".tour-play").trigger("click");
        expect(onNext).not.toHaveBeenCalled();
        await advanceTime(9999);
        expect(useTourStore().currentTour?.step).toBe(0);
        await advanceTime(1);
        expect(useTourStore().currentTour?.step).toBe(1);
        await advanceTime(10000);
        expect(useTourStore().currentTour?.step).toBe(2);
        await advanceTime(60000);
        expect(useTourStore().currentTour?.step).toBe(2);
        expect(onNext).toHaveBeenCalledTimes(2);
        expect(wrapper.find(".tour-end").text()).toContain("Close");
    });

    it("allows more reading time for long HTML content", async () => {
        await wrapper.setProps({
            steps: [{ content: `<p>${"word ".repeat(100)}</p>` }, ...steps.slice(1)],
        });
        await wrapper.find(".tour-play").trigger("click");
        await advanceTime(31999);
        expect(useTourStore().currentTour?.step).toBe(0);
        await advanceTime(1);
        expect(useTourStore().currentTour?.step).toBe(1);
    });

    it.each(["pointerdown", "keydown"])("pauses auto-play on %s anywhere in Galaxy", async (eventName) => {
        await wrapper.find(".tour-play").trigger("click");
        await advanceTime(1000);
        document.body.dispatchEvent(new Event(eventName, { bubbles: true }));
        await flushPromises();
        expect(wrapper.find(".tour-next").exists()).toBe(true);
        await advanceTime(60000);
        expect(useTourStore().currentTour?.step).toBe(0);
        await wrapper.find(".tour-next").trigger("click");
        await flushPromises();
        expect(useTourStore().currentTour?.step).toBe(1);
    });

    it("clears the old timer when stopping and restarting auto-play", async () => {
        await wrapper.find(".tour-play").trigger("click");
        await advanceTime(1000);
        await wrapper.find(".tour-stop").trigger("click");
        await wrapper.find(".tour-play").trigger("click");
        await advanceTime(9000);
        expect(useTourStore().currentTour?.step).toBe(0);
        await advanceTime(1000);
        expect(useTourStore().currentTour?.step).toBe(1);
        expect(onNext).toHaveBeenCalledTimes(1);
    });

    it("does not pause for clicks performed by the tour", async () => {
        onBefore.mockImplementation(async () => {
            window.dispatchEvent(new MouseEvent("click"));
        });
        await wrapper.find(".tour-play").trigger("click");
        await advanceTime(20000);
        expect(useTourStore().currentTour?.step).toBe(2);
    });

    it("waits for pre-actions before starting the next step's reading time", async () => {
        let resolveBefore!: () => void;
        onBefore.mockImplementationOnce(() => new Promise<void>((resolve) => (resolveBefore = resolve)));
        await wrapper.find(".tour-play").trigger("click");
        await advanceTime(10000);
        await advanceTime(20000);
        expect(useTourStore().currentTour?.step).toBe(0);
        expect(onNext).toHaveBeenCalledTimes(1);
        resolveBefore();
        await flushPromises();
        expect(useTourStore().currentTour?.step).toBe(1);
        await advanceTime(9999);
        expect(useTourStore().currentTour?.step).toBe(1);
        await advanceTime(1);
        expect(useTourStore().currentTour?.step).toBe(2);
    });

    it("can pause during pre-actions without restarting auto-play or advancing twice", async () => {
        let resolveBefore!: () => void;
        onBefore.mockImplementationOnce(() => new Promise<void>((resolve) => (resolveBefore = resolve)));
        await wrapper.find(".tour-play").trigger("click");
        await advanceTime(10000);
        window.dispatchEvent(new Event("pointerdown"));
        await flushPromises();
        expect(wrapper.find(".tour-next").attributes("aria-disabled")).toBe("true");
        window.dispatchEvent(new KeyboardEvent("keyup", { keyCode: 39 }));
        await flushPromises();
        expect(onNext).toHaveBeenCalledTimes(1);
        resolveBefore();
        await flushPromises();
        await advanceTime(60000);
        expect(useTourStore().currentTour?.step).toBe(1);
        expect(wrapper.find(".tour-next").attributes("aria-disabled")).toBeUndefined();
        await wrapper.find(".tour-next").trigger("click");
        await flushPromises();
        expect(useTourStore().currentTour?.step).toBe(2);
    });

    it("pauses auto-play when a step fails", async () => {
        onBefore.mockRejectedValueOnce(new Error("Missing tour target"));
        await wrapper.find(".tour-play").trigger("click");
        await advanceTime(10000);
        expect(wrapper.text()).toContain("Missing tour target");
        await advanceTime(60000);
        expect(onNext).toHaveBeenCalledTimes(1);
        expect(useTourStore().currentTour?.step).toBe(0);
    });

    it.each(["end", "unmount"])("clears pending auto-play on %s", async (action) => {
        await wrapper.find(".tour-play").trigger("click");
        if (action === "end") {
            window.dispatchEvent(new KeyboardEvent("keyup", { keyCode: 27 }));
        } else {
            wrapper.destroy();
        }
        await advanceTime(60000);
        expect(onNext).not.toHaveBeenCalled();
    });

    it("does not update a replacement tour when unmounted during pre-actions", async () => {
        let resolveBefore!: () => void;
        onBefore.mockImplementationOnce(() => new Promise<void>((resolve) => (resolveBefore = resolve)));
        await wrapper.find(".tour-play").trigger("click");
        await advanceTime(10000);
        wrapper.destroy();
        useTourStore().setTour("another-tour");
        resolveBefore();
        await flushPromises();
        await advanceTime(60000);
        expect(useTourStore().currentTour).toEqual({ id: "another-tour", step: 0 });
    });
});
