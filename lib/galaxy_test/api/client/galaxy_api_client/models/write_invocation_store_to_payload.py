from dataclasses import dataclass

from .bco_override_algorithmic_error import BcoOverrideAlgorithmicError
from .bco_override_empirical_error import BcoOverrideEmpiricalError
from .bco_override_environment_variables import BcoOverrideEnvironmentVariables
from .bco_override_xref import BcoOverrideXref
from .model_store_format import ModelStoreFormat

__all__ = ["WriteInvocationStoreToPayload"]


@dataclass
class WriteInvocationStoreToPayload:
    """
    WriteInvocationStoreToPayload dataclass.

    Args:
        target_uri (str)         : Galaxy Files URI to write mode store content to.
        bco_merge_history_metadata (Optional[bool])
                                 : When reading tags/annotations to generate BCO object
                                   include history metadata.
        bco_override_algorithmic_error (Optional[BcoOverrideAlgorithmicError])
                                 : Override algorithmic error for 'error domain' when
                                   generating BioCompute object.
        bco_override_empirical_error (Optional[BcoOverrideEmpiricalError])
                                 : Override empirical error for 'error domain' when
                                   generating BioCompute object.
        bco_override_environment_variables (Optional[BcoOverrideEnvironmentVariables])
                                 : Override environment variables for 'execution_domain'
                                   when generating BioCompute object.
        bco_override_xref (Optional[BcoOverrideXref])
                                 : Override xref for 'description domain' when generating
                                   BioCompute object.
        include_deleted (Optional[bool])
                                 : Include file contents for deleted datasets (if
                                   include_files is True).
        include_files (Optional[bool])
                                 : include materialized files in export when available
        include_hidden (Optional[bool])
                                 : Include file contents for hidden datasets (if
                                   include_files is True).
        model_store_format (Optional[ModelStoreFormat])
                                 :
    """

    target_uri: str  # Galaxy Files URI to write mode store content to.
    bco_merge_history_metadata: bool | None = (
        False  # When reading tags/annotations to generate BCO object include history metadata.
    )
    bco_override_algorithmic_error: BcoOverrideAlgorithmicError | None = (
        None  # Override algorithmic error for 'error domain' when generating BioCompute object.
    )
    bco_override_empirical_error: BcoOverrideEmpiricalError | None = (
        None  # Override empirical error for 'error domain' when generating BioCompute object.
    )
    bco_override_environment_variables: BcoOverrideEnvironmentVariables | None = (
        None  # Override environment variables for 'execution_domain' when generating BioCompute object.
    )
    bco_override_xref: BcoOverrideXref | None = (
        None  # Override xref for 'description domain' when generating BioCompute object.
    )
    include_deleted: bool | None = False  # Include file contents for deleted datasets (if include_files is True).
    include_files: bool | None = True  # include materialized files in export when available
    include_hidden: bool | None = False  # Include file contents for hidden datasets (if include_files is True).
    model_store_format: ModelStoreFormat | None = None
