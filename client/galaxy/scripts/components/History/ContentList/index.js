/**
 * Scrolling components for history contents and collection contents.
 */

// "vue-virtual-scroll-list" Awkward api but pretty fast.
import HistoryContentItem from "./HistoryContentItem";
import CollectionContentItem from "./CollectionContentItem";
import { ContentListFactory } from "./ContentListFactory";
export const HistoryContentList = ContentListFactory(HistoryContentItem);
export const CollectionContentList = ContentListFactory(CollectionContentItem);

// "vue-virtual-scroller", Good API but buggy and kind of slow
// export { default as HistoryContentList } from "./HistoryContentScroller";
// export { default as CollectionContentList } from "./CollectionContentScroller";

import "./styles.scss";
