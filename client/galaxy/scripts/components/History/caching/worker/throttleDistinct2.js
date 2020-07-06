// use same store as requestWithUpdateTime?
// export const throttleDistinctDateStore = createDateStore("throttleDistinct default");

// export const throttleDistinct = (config = {}) => {
//     const { timeout = 1000, dateStore = throttleDistinctDateStore } = config;

//     return pipe(
//         filter((val) => {
//             const now = moment();
//             let ok = true;
//             if (dateStore.has(val)) {
//                 const lastRequest = dateStore.getLastDate(val);
//                 ok = now - lastRequest > timeout;
//             }
//             if (ok) {
//                 dateStore.set(val, now);
//             }
//             return ok;
//         })
//     );
// };
