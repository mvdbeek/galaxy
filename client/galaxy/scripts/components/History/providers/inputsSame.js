import { SearchParams } from "../model/SearchParams";

// equivalence comparator for id + params
export const inputsSame = (a, b) => {
    const idSame = a[0] == b[0];
    const paramSame = SearchParams.equals(a[1], b[1]);
    return idSame && paramSame;
};