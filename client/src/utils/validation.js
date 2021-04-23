// type utils

export const areDefined = (...vals) => vals.every(isDefined);

export const isDefined = (val) => val !== undefined && val !== null;
