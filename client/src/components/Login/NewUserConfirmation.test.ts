import { getLocalVue } from "@tests/jest/helpers";
import { mount, type Wrapper } from "@vue/test-utils";
import axios from "axios";
import MockAdapter from "axios-mock-adapter";
import flushPromises from "flush-promises";

import { getAppRoot } from "@/onload/loadConfig";

import MountTarget from "./NewUserConfirmation.vue";

const localVue = getLocalVue(true);

jest.mock("@/onload/loadConfig");
jest.mock("vue-router/composables", () => ({
    useRouter: () => ({ push: jest.fn() }),
}));

const CREATE_USER_URL = "/authnz/test_provider/create_user";
const SESSION_CSRF_TOKEN = "session_csrf_token";
// A token in the query string must never reach the confirmation request.
const ATTACKER_TOKEN = "attacker_token";

const originalLocation = window.location;
// A single mutable stand-in so the component's `location.href = ...` navigation is observable.
const mockLocation = { ...originalLocation, search: "", href: "" };
jest.spyOn(window, "location", "get").mockImplementation(() => mockLocation as Location);

function setLocationSearch(search: string) {
    mockLocation.search = search;
}

function mountConfirmation() {
    return mount(MountTarget as object, {
        propsData: { sessionCsrfToken: SESSION_CSRF_TOKEN },
        localVue,
    });
}

async function acceptTermsAndSubmit(wrapper: Wrapper<Vue>) {
    await wrapper.find("input[type='checkbox']").setChecked();
    await wrapper.find("button[name='confirm']").trigger("click");
    await flushPromises();
}

describe("NewUserConfirmation", () => {
    let wrapper: Wrapper<Vue>;
    let axiosMock: MockAdapter;

    beforeEach(() => {
        jest.mocked(getAppRoot).mockReturnValue("");
        setLocationSearch(`?provider=test_provider&provider_token=${ATTACKER_TOKEN}`);
        mockLocation.href = "";
        axiosMock = new MockAdapter(axios);
        axiosMock.onPost(CREATE_USER_URL).reply(200, { redirect_uri: "/" });
        wrapper = mountConfirmation();
    });

    afterEach(() => {
        axiosMock.restore();
        jest.clearAllMocks();
    });

    it("renders the confirmation prompt with a single terms checkbox", () => {
        expect(wrapper.find(".card-header").text()).toBe("Confirm new account creation");

        const inputs = wrapper.findAll("input");
        expect(inputs.length).toBe(1);
        expect(inputs.at(0).attributes("type")).toBe("checkbox");
    });

    it("does not submit until the terms checkbox is checked", async () => {
        await wrapper.find("button[name='confirm']").trigger("click");
        await flushPromises();

        expect(axiosMock.history.post?.length).toBe(0);
    });

    it("posts only the session CSRF token, never a token from the URL", async () => {
        await acceptTermsAndSubmit(wrapper);

        const postedData = axiosMock.history.post?.[0];
        expect(postedData).toBeDefined();
        expect(postedData?.url).toBe(CREATE_USER_URL);

        const postedFormData = postedData?.data as FormData;
        expect(postedFormData.get("session_csrf_token")).toBe(SESSION_CSRF_TOKEN);
        expect(Array.from(postedFormData.values())).toEqual([SESSION_CSRF_TOKEN]);
        expect(JSON.stringify(Array.from(postedFormData.entries()))).not.toContain(ATTACKER_TOKEN);
    });

    it("reloads the page on success so the new session takes effect", async () => {
        axiosMock.onPost(CREATE_USER_URL).reply(200, { redirect_uri: "/user/external_ids" });

        await acceptTermsAndSubmit(wrapper);

        // A router push would leave the application running against the pre-login session.
        expect(mockLocation.href).toBe("/user/external_ids");
    });

    it("does not prefix a server-generated redirect URI again", async () => {
        jest.mocked(getAppRoot).mockReturnValue("/galaxy");
        axiosMock
            .onPost("/galaxy/authnz/test_provider/create_user")
            .reply(200, { redirect_uri: "/galaxy/user/external_ids" });

        await acceptTermsAndSubmit(wrapper);

        expect(mockLocation.href).toBe("/galaxy/user/external_ids");
    });

    it("falls back to the root when the server returns no redirect_uri", async () => {
        axiosMock.onPost(CREATE_USER_URL).reply(200, {});

        await acceptTermsAndSubmit(wrapper);

        expect(mockLocation.href).toBe("/");
    });

    it("shows the server error and does not navigate when confirmation is rejected", async () => {
        axiosMock
            .onPost(CREATE_USER_URL)
            .reply(400, { err_msg: "Unable to confirm this external account. Please restart the login process." });

        await acceptTermsAndSubmit(wrapper);

        expect(wrapper.find(".alert-danger").text()).toContain("Please restart the login process.");
        expect(mockLocation.href).toBe("");
    });

    it("reports a missing provider without posting", async () => {
        setLocationSearch(`?provider_token=${ATTACKER_TOKEN}`);
        wrapper = mountConfirmation();

        await acceptTermsAndSubmit(wrapper);

        expect(wrapper.find(".alert-danger").text()).toBe("Missing provider.");
        expect(axiosMock.history.post?.length).toBe(0);
    });

    it("submits when the URL carries no provider_token at all", async () => {
        setLocationSearch("?provider=test_provider");
        wrapper = mountConfirmation();

        await acceptTermsAndSubmit(wrapper);

        expect(axiosMock.history.post?.length).toBe(1);
    });

    it("shows the registration warning message when configured", async () => {
        await wrapper.setProps({ registrationWarningMessage: "registration warning message" });

        expect(wrapper.find(".alert-info").text()).toBe("registration warning message");
    });

    it("renders the terms of use in a frame when a terms url is configured", async () => {
        await wrapper.setProps({ termsUrl: "terms_url" });

        expect(wrapper.find("iframe").attributes("src")).toBe("terms_url");
    });

    it("offers a link back to the login form", () => {
        expect(wrapper.find("a[id=login-toggle]").text()).toBe("Log in here.");
    });
});
