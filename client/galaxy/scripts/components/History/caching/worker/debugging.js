import { content$, dscContent$ } from "../galaxyDb";

/**
 * Clear entire database
 */

export async function getDbInstance(db$) {
    return await db$.toPromise();
}

export async function wipeDatabase() {
    const content = await getDbInstance(content$);
    await content.erase();
    const dsc = await getDbInstance(dscContent$);
    await dsc.erase();
}
