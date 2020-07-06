import { DatasetCollection } from "../../../model/DatasetCollection";

// test data
import rawGood from "../unit/json/DatasetCollection.json";

// error on load
import rawLoadError from "../unit/json/DatasetCollection.error.json";

// mixed bag
import rawProcessing from "../unit/json/DatasetCollection.error.json";

describe("DatasetCollection", () => {
    describe("normal result", () => {
        const dsc = new DatasetCollection(rawGood);

        it("should exist", () => {
            expect(dsc);
        });
    });

    describe("error before create", () => {
        const dsc = new DatasetCollection(rawLoadError);

        it("should exist", () => {
            expect(dsc);
        });
    });

    describe("collection processing", () => {
        const dsc = new DatasetCollection(rawProcessing);

        it("should exist", () => {
            expect(dsc);
        });
    });
});
