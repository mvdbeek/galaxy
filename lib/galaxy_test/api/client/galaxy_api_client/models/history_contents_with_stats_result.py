from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.hda_custom import HDACustom
    from ..models.hda_detailed import HDADetailed
    from ..models.hda_inaccessible import HDAInaccessible
    from ..models.hda_summary import HDASummary
    from ..models.hdca_custom import HDCACustom
    from ..models.hdca_detailed import HDCADetailed
    from ..models.hdca_summary import HDCASummary
    from ..models.history_content_stats import HistoryContentStats


T = TypeVar("T", bound="HistoryContentsWithStatsResult")


@_attrs_define
class HistoryContentsWithStatsResult:
    """Includes stats with items counting

    Attributes:
        contents (list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed |
            HDCASummary]): The items matching the search query. Only the items fitting in the current page limit will be
            returned.
        stats (HistoryContentStats):
    """

    contents: list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
    stats: HistoryContentStats
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.hda_custom import HDACustom
        from ..models.hda_detailed import HDADetailed
        from ..models.hda_inaccessible import HDAInaccessible
        from ..models.hda_summary import HDASummary
        from ..models.hdca_custom import HDCACustom
        from ..models.hdca_detailed import HDCADetailed

        contents = []
        for contents_item_data in self.contents:
            contents_item: dict[str, Any]
            if isinstance(contents_item_data, HDACustom):
                contents_item = contents_item_data.to_dict()
            elif isinstance(contents_item_data, HDADetailed):
                contents_item = contents_item_data.to_dict()
            elif isinstance(contents_item_data, HDASummary):
                contents_item = contents_item_data.to_dict()
            elif isinstance(contents_item_data, HDAInaccessible):
                contents_item = contents_item_data.to_dict()
            elif isinstance(contents_item_data, HDCACustom):
                contents_item = contents_item_data.to_dict()
            elif isinstance(contents_item_data, HDCADetailed):
                contents_item = contents_item_data.to_dict()
            else:
                contents_item = contents_item_data.to_dict()

            contents.append(contents_item)

        stats = self.stats.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "contents": contents,
                "stats": stats,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.hda_custom import HDACustom
        from ..models.hda_detailed import HDADetailed
        from ..models.hda_inaccessible import HDAInaccessible
        from ..models.hda_summary import HDASummary
        from ..models.hdca_custom import HDCACustom
        from ..models.hdca_detailed import HDCADetailed
        from ..models.hdca_summary import HDCASummary
        from ..models.history_content_stats import HistoryContentStats

        d = dict(src_dict)
        contents = []
        _contents = d.pop("contents")
        for contents_item_data in _contents:

            def _parse_contents_item(
                data: object,
            ) -> HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    contents_item_type_0 = HDACustom.from_dict(data)

                    return contents_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    contents_item_type_1 = HDADetailed.from_dict(data)

                    return contents_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    contents_item_type_2 = HDASummary.from_dict(data)

                    return contents_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    contents_item_type_3 = HDAInaccessible.from_dict(data)

                    return contents_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    contents_item_type_4 = HDCACustom.from_dict(data)

                    return contents_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    contents_item_type_5 = HDCADetailed.from_dict(data)

                    return contents_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                contents_item_type_6 = HDCASummary.from_dict(data)

                return contents_item_type_6

            contents_item = _parse_contents_item(contents_item_data)

            contents.append(contents_item)

        stats = HistoryContentStats.from_dict(d.pop("stats"))

        history_contents_with_stats_result = cls(
            contents=contents,
            stats=stats,
        )

        history_contents_with_stats_result.additional_properties = d
        return history_contents_with_stats_result

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
