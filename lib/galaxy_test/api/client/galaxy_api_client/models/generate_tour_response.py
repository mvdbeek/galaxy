from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.tour_details import TourDetails


T = TypeVar("T", bound="GenerateTourResponse")


@_attrs_define
class GenerateTourResponse:
    """
    Attributes:
        tour (TourDetails):
        uploaded_hids (list[int]): List of hids for the datasets uploaded for the tour.
        use_datasets (bool): Indicates whether the tour should use (and wait for) datasets.
    """

    tour: TourDetails
    uploaded_hids: list[int]
    use_datasets: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        tour = self.tour.to_dict()

        uploaded_hids = self.uploaded_hids

        use_datasets = self.use_datasets

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "tour": tour,
                "uploaded_hids": uploaded_hids,
                "use_datasets": use_datasets,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.tour_details import TourDetails

        d = dict(src_dict)
        tour = TourDetails.from_dict(d.pop("tour"))

        uploaded_hids = cast(list[int], d.pop("uploaded_hids"))

        use_datasets = d.pop("use_datasets")

        generate_tour_response = cls(
            tour=tour,
            uploaded_hids=uploaded_hids,
            use_datasets=use_datasets,
        )

        generate_tour_response.additional_properties = d
        return generate_tour_response

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
