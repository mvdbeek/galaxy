import { pipe } from "rxjs";
import { map, switchMap  } from "rxjs/operators";
import { monitorDscQuery } from "../../caching";


export const dscContentObservable = (cfg = {}) => {
    return pipe(
        map(buildPouchRequest),
        switchMap(request => monitorDscQuery(request, cfg))
    );
}

const buildPouchRequest = ([contents_url, params]) => {
    // const { skip, limit, filterText } = params;
    return {
        selector: {
            // we put the contents_url in the id, should
            // come back with auto ordered and sorted results
            _id: { $regex: new RegExp(contents_url, "i")},
            // ...buildSelectorFromParams(params),
        },
        // skip,
        // limit
    };
};

export function buildSelectorFromParams(params) {
    console.log("buildSelectorFromParams", params);

    const selector = {};

    // const selector = {
    //     visible: { $eq: true },
    //     isDeleted: { $eq: false },
    // };

    // if (params.showDeleted) {
    //     delete selector.visible;
    //     selector.isDeleted = { $eq: true };
    // }

    // if (params.showHidden) {
    //     delete selector.isDeleted;
    //     selector.visible = { $eq: false };
    // }

    // if (params.showDeleted && params.showHidden) {
    //     selector.visible = { $eq: false };
    //     selector.isDeleted = { $eq: true };
    // }

    // if (params.filterText) {
    //     selector.element_identifier = { $regex: new RegExp(params.filterText, "gi") }
    // }

    return selector;
}
