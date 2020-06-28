import { pipe } from "rxjs";
import { map } from "rxjs/operators";

export const mapByProp = propName =>
    pipe(
        map(items =>
            items.reduce((itemSet, item) => {
                itemSet.set(item[propName], item);
                return itemSet;
            }, new Map())
        )
    );
