from dataclasses import dataclass

from .encoded_data_item_source_id import EncodedDataItemSourceId
from .job_output_label import JobOutputLabel

__all__ = ["JobOutput"]


@dataclass
class JobOutput:
    """
    JobOutput dataclass

    Args:
        label (JobOutputLabel)   : The output label
        value (EncodedDataItemSourceId)
                                 :
    """

    label: JobOutputLabel  # The output label
    value: EncodedDataItemSourceId

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "label": "label",
            "value": "value",
        }
        key_transform_with_dump = {
            "label": "label",
            "value": "value",
        }
