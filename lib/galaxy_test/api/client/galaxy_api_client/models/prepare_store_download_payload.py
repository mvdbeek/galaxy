from dataclasses import dataclass

from .model_store_format import ModelStoreFormat
from .prepare_store_download_payload_bco_override_algorithmic_error import (
    PrepareStoreDownloadPayloadBcoOverrideAlgorithmicError,
)
from .prepare_store_download_payload_bco_override_empirical_error import (
    PrepareStoreDownloadPayloadBcoOverrideEmpiricalError,
)
from .prepare_store_download_payload_bco_override_environment_variables import (
    PrepareStoreDownloadPayloadBcoOverrideEnvironmentVariables,
)
from .prepare_store_download_payload_bco_override_xref import PrepareStoreDownloadPayloadBcoOverrideXref

__all__ = ["PrepareStoreDownloadPayload"]


@dataclass
class PrepareStoreDownloadPayload:
    """
    PrepareStoreDownloadPayload dataclass

    Args:
        bco_merge_history_metadata (bool | None)
                                 : When reading tags/annotations to generate BCO object
                                   include history metadata.
        bco_override_algorithmic_error (PrepareStoreDownloadPayloadBcoOverrideAlgorithmicError | None)
                                 : Override algorithmic error for 'error domain' when
                                   generating BioCompute object.
        bco_override_empirical_error (PrepareStoreDownloadPayloadBcoOverrideEmpiricalError | None)
                                 : Override empirical error for 'error domain' when
                                   generating BioCompute object.
        bco_override_environment_variables (PrepareStoreDownloadPayloadBcoOverrideEnvironmentVariables | None)
                                 : Override environment variables for 'execution_domain'
                                   when generating BioCompute object.
        bco_override_xref (PrepareStoreDownloadPayloadBcoOverrideXref | None)
                                 : Override xref for 'description domain' when generating
                                   BioCompute object.
        include_deleted (bool | None)
                                 : Include file contents for deleted datasets (if
                                   include_files is True).
        include_files (bool | None)
                                 : include materialized files in export when available
        include_hidden (bool | None)
                                 : Include file contents for hidden datasets (if
                                   include_files is True).
        model_store_format (ModelStoreFormat | None)
                                 : Available types of model stores for export.
    """

    bco_merge_history_metadata: bool | None = (
        False  # When reading tags/annotations to generate BCO object include history metadata.
    )
    bco_override_algorithmic_error: PrepareStoreDownloadPayloadBcoOverrideAlgorithmicError | None = (
        None  # Override algorithmic error for 'error domain' when generating BioCompute object.
    )
    bco_override_empirical_error: PrepareStoreDownloadPayloadBcoOverrideEmpiricalError | None = (
        None  # Override empirical error for 'error domain' when generating BioCompute object.
    )
    bco_override_environment_variables: PrepareStoreDownloadPayloadBcoOverrideEnvironmentVariables | None = (
        None  # Override environment variables for 'execution_domain' when generating BioCompute object.
    )
    bco_override_xref: PrepareStoreDownloadPayloadBcoOverrideXref | None = (
        None  # Override xref for 'description domain' when generating BioCompute object.
    )
    include_deleted: bool | None = False  # Include file contents for deleted datasets (if include_files is True).
    include_files: bool | None = True  # include materialized files in export when available
    include_hidden: bool | None = False  # Include file contents for hidden datasets (if include_files is True).
    model_store_format: ModelStoreFormat | None = None  # Available types of model stores for export.

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "bco_merge_history_metadata": "bco_merge_history_metadata",
            "bco_override_algorithmic_error": "bco_override_algorithmic_error",
            "bco_override_empirical_error": "bco_override_empirical_error",
            "bco_override_environment_variables": "bco_override_environment_variables",
            "bco_override_xref": "bco_override_xref",
            "include_deleted": "include_deleted",
            "include_files": "include_files",
            "include_hidden": "include_hidden",
            "model_store_format": "model_store_format",
        }
        key_transform_with_dump = {
            "bco_merge_history_metadata": "bco_merge_history_metadata",
            "bco_override_algorithmic_error": "bco_override_algorithmic_error",
            "bco_override_empirical_error": "bco_override_empirical_error",
            "bco_override_environment_variables": "bco_override_environment_variables",
            "bco_override_xref": "bco_override_xref",
            "include_deleted": "include_deleted",
            "include_files": "include_files",
            "include_hidden": "include_hidden",
            "model_store_format": "model_store_format",
        }
