import axios from "axios";
import { afterEach, describe, expect, it, vi } from "vitest";

import { getRunData, WorkflowMissingToolsError } from "./services";

vi.mock("axios");
vi.mock("@/onload/loadConfig", () => ({ getAppRoot: () => "/" }));

describe("getRunData", () => {
    afterEach(() => {
        vi.mocked(axios.get).mockReset();
    });

    it("turns a missing-tools rejection into a WorkflowMissingToolsError", async () => {
        vi.mocked(axios.get).mockRejectedValue({
            response: {
                status: 400,
                data: { err_msg: "Workflow cannot be run.", missing_tool_ids: ["fastqc", "bwa"] },
            },
        });

        const error = await getRunData("abc").catch((e) => e);

        expect(error).toBeInstanceOf(WorkflowMissingToolsError);
        expect(error.message).toBe("Workflow cannot be run.");
        expect(error.missingToolIds).toEqual(["fastqc", "bwa"]);
    });

    it("rethrows other failures as plain errors", async () => {
        vi.mocked(axios.get).mockRejectedValue({
            response: { status: 403, data: { err_msg: "Workflow is not accessible." } },
        });

        const error = await getRunData("abc").catch((e) => e);

        expect(error).not.toBeInstanceOf(WorkflowMissingToolsError);
        expect(error.message).toBe("Workflow is not accessible.");
    });

    it("does not treat an empty missing_tool_ids list as missing tools", async () => {
        vi.mocked(axios.get).mockRejectedValue({
            response: { status: 400, data: { err_msg: "Bad request.", missing_tool_ids: [] } },
        });

        const error = await getRunData("abc").catch((e) => e);

        expect(error).not.toBeInstanceOf(WorkflowMissingToolsError);
        expect(error.message).toBe("Bad request.");
    });
});
