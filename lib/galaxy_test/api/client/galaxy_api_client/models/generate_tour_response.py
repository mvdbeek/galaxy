from dataclasses import dataclass

from .tour_details import TourDetails
from .uploaded_hids import UploadedHids

__all__ = ["GenerateTourResponse"]


@dataclass
class GenerateTourResponse:
    """
    GenerateTourResponse dataclass.

    Args:
        tour (TourDetails)       :
        uploaded_hids (UploadedHids)
                                 : List of hids for the datasets uploaded for the tour.
        use_datasets (bool)      : Indicates whether the tour should use (and wait for)
                                   datasets.
    """

    tour: TourDetails
    uploaded_hids: UploadedHids  # List of hids for the datasets uploaded for the tour.
    use_datasets: bool  # Indicates whether the tour should use (and wait for) datasets.
