from dataclasses import dataclass

from .tour_details import TourDetails

__all__ = ["GenerateTourResponse"]


@dataclass
class GenerateTourResponse:
    """
    GenerateTourResponse dataclass

    Args:
        tour (TourDetails)       :
        uploaded_hids (List[int]): List of hids for the datasets uploaded for the tour.
        use_datasets (bool)      : Indicates whether the tour should use (and wait for)
                                   datasets.
    """

    tour: TourDetails
    uploaded_hids: list[int]  # List of hids for the datasets uploaded for the tour.
    use_datasets: bool  # Indicates whether the tour should use (and wait for) datasets.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "tour": "tour",
            "uploaded_hids": "uploaded_hids",
            "use_datasets": "use_datasets",
        }
        key_transform_with_dump = {
            "tour": "tour",
            "uploaded_hids": "uploaded_hids",
            "use_datasets": "use_datasets",
        }
