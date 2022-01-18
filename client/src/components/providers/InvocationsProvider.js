import axios from "axios";

export function invocationsProvider(ctx, callback, extraParams) {
    const { apiUrl, filter, ...requestParams } = ctx;
    const promise = axios.get(apiUrl, { params: { ...requestParams, ...extraParams } });

    // Must return a promise that resolves to an array of items
    return promise.then((data) => {
        // Pluck the array of items off our axios response
        const items = data.data;
        callback && callback(data);
        // Must return an array of items or an empty array if an error occurred
        return items || [];
    });
}
