from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.model_store_format import ModelStoreFormat
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.write_invocation_store_to_payload_bco_override_algorithmic_error_type_0 import (
        WriteInvocationStoreToPayloadBcoOverrideAlgorithmicErrorType0,
    )
    from ..models.write_invocation_store_to_payload_bco_override_empirical_error_type_0 import (
        WriteInvocationStoreToPayloadBcoOverrideEmpiricalErrorType0,
    )
    from ..models.write_invocation_store_to_payload_bco_override_environment_variables_type_0 import (
        WriteInvocationStoreToPayloadBcoOverrideEnvironmentVariablesType0,
    )
    from ..models.xref_item import XrefItem


T = TypeVar("T", bound="WriteInvocationStoreToPayload")


@_attrs_define
class WriteInvocationStoreToPayload:
    """
    Attributes:
        target_uri (str): Galaxy Files URI to write mode store content to.
        bco_merge_history_metadata (bool | Unset): When reading tags/annotations to generate BCO object include history
            metadata. Default: False.
        bco_override_algorithmic_error (None | Unset | WriteInvocationStoreToPayloadBcoOverrideAlgorithmicErrorType0):
            Override algorithmic error for 'error domain' when generating BioCompute object.
        bco_override_empirical_error (None | Unset | WriteInvocationStoreToPayloadBcoOverrideEmpiricalErrorType0):
            Override empirical error for 'error domain' when generating BioCompute object.
        bco_override_environment_variables (None | Unset |
            WriteInvocationStoreToPayloadBcoOverrideEnvironmentVariablesType0): Override environment variables for
            'execution_domain' when generating BioCompute object.
        bco_override_xref (list[XrefItem] | None | Unset): Override xref for 'description domain' when generating
            BioCompute object.
        include_deleted (bool | Unset): Include file contents for deleted datasets (if include_files is True). Default:
            False.
        include_files (bool | Unset): include materialized files in export when available Default: True.
        include_hidden (bool | Unset): Include file contents for hidden datasets (if include_files is True). Default:
            False.
        model_store_format (ModelStoreFormat | Unset): Available types of model stores for export.
    """

    target_uri: str
    bco_merge_history_metadata: bool | Unset = False
    bco_override_algorithmic_error: None | Unset | WriteInvocationStoreToPayloadBcoOverrideAlgorithmicErrorType0 = UNSET
    bco_override_empirical_error: None | Unset | WriteInvocationStoreToPayloadBcoOverrideEmpiricalErrorType0 = UNSET
    bco_override_environment_variables: (
        None | Unset | WriteInvocationStoreToPayloadBcoOverrideEnvironmentVariablesType0
    ) = UNSET
    bco_override_xref: list[XrefItem] | None | Unset = UNSET
    include_deleted: bool | Unset = False
    include_files: bool | Unset = True
    include_hidden: bool | Unset = False
    model_store_format: ModelStoreFormat | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.write_invocation_store_to_payload_bco_override_algorithmic_error_type_0 import (
            WriteInvocationStoreToPayloadBcoOverrideAlgorithmicErrorType0,
        )
        from ..models.write_invocation_store_to_payload_bco_override_empirical_error_type_0 import (
            WriteInvocationStoreToPayloadBcoOverrideEmpiricalErrorType0,
        )
        from ..models.write_invocation_store_to_payload_bco_override_environment_variables_type_0 import (
            WriteInvocationStoreToPayloadBcoOverrideEnvironmentVariablesType0,
        )

        target_uri = self.target_uri

        bco_merge_history_metadata = self.bco_merge_history_metadata

        bco_override_algorithmic_error: dict[str, Any] | None | Unset
        if isinstance(self.bco_override_algorithmic_error, Unset):
            bco_override_algorithmic_error = UNSET
        elif isinstance(
            self.bco_override_algorithmic_error, WriteInvocationStoreToPayloadBcoOverrideAlgorithmicErrorType0
        ):
            bco_override_algorithmic_error = self.bco_override_algorithmic_error.to_dict()
        else:
            bco_override_algorithmic_error = self.bco_override_algorithmic_error

        bco_override_empirical_error: dict[str, Any] | None | Unset
        if isinstance(self.bco_override_empirical_error, Unset):
            bco_override_empirical_error = UNSET
        elif isinstance(self.bco_override_empirical_error, WriteInvocationStoreToPayloadBcoOverrideEmpiricalErrorType0):
            bco_override_empirical_error = self.bco_override_empirical_error.to_dict()
        else:
            bco_override_empirical_error = self.bco_override_empirical_error

        bco_override_environment_variables: dict[str, Any] | None | Unset
        if isinstance(self.bco_override_environment_variables, Unset):
            bco_override_environment_variables = UNSET
        elif isinstance(
            self.bco_override_environment_variables, WriteInvocationStoreToPayloadBcoOverrideEnvironmentVariablesType0
        ):
            bco_override_environment_variables = self.bco_override_environment_variables.to_dict()
        else:
            bco_override_environment_variables = self.bco_override_environment_variables

        bco_override_xref: list[dict[str, Any]] | None | Unset
        if isinstance(self.bco_override_xref, Unset):
            bco_override_xref = UNSET
        elif isinstance(self.bco_override_xref, list):
            bco_override_xref = []
            for bco_override_xref_type_0_item_data in self.bco_override_xref:
                bco_override_xref_type_0_item = bco_override_xref_type_0_item_data.to_dict()
                bco_override_xref.append(bco_override_xref_type_0_item)

        else:
            bco_override_xref = self.bco_override_xref

        include_deleted = self.include_deleted

        include_files = self.include_files

        include_hidden = self.include_hidden

        model_store_format: str | Unset = UNSET
        if not isinstance(self.model_store_format, Unset):
            model_store_format = self.model_store_format.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "target_uri": target_uri,
            }
        )
        if bco_merge_history_metadata is not UNSET:
            field_dict["bco_merge_history_metadata"] = bco_merge_history_metadata
        if bco_override_algorithmic_error is not UNSET:
            field_dict["bco_override_algorithmic_error"] = bco_override_algorithmic_error
        if bco_override_empirical_error is not UNSET:
            field_dict["bco_override_empirical_error"] = bco_override_empirical_error
        if bco_override_environment_variables is not UNSET:
            field_dict["bco_override_environment_variables"] = bco_override_environment_variables
        if bco_override_xref is not UNSET:
            field_dict["bco_override_xref"] = bco_override_xref
        if include_deleted is not UNSET:
            field_dict["include_deleted"] = include_deleted
        if include_files is not UNSET:
            field_dict["include_files"] = include_files
        if include_hidden is not UNSET:
            field_dict["include_hidden"] = include_hidden
        if model_store_format is not UNSET:
            field_dict["model_store_format"] = model_store_format

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.write_invocation_store_to_payload_bco_override_algorithmic_error_type_0 import (
            WriteInvocationStoreToPayloadBcoOverrideAlgorithmicErrorType0,
        )
        from ..models.write_invocation_store_to_payload_bco_override_empirical_error_type_0 import (
            WriteInvocationStoreToPayloadBcoOverrideEmpiricalErrorType0,
        )
        from ..models.write_invocation_store_to_payload_bco_override_environment_variables_type_0 import (
            WriteInvocationStoreToPayloadBcoOverrideEnvironmentVariablesType0,
        )
        from ..models.xref_item import XrefItem

        d = dict(src_dict)
        target_uri = d.pop("target_uri")

        bco_merge_history_metadata = d.pop("bco_merge_history_metadata", UNSET)

        def _parse_bco_override_algorithmic_error(
            data: object,
        ) -> None | Unset | WriteInvocationStoreToPayloadBcoOverrideAlgorithmicErrorType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bco_override_algorithmic_error_type_0 = (
                    WriteInvocationStoreToPayloadBcoOverrideAlgorithmicErrorType0.from_dict(data)
                )

                return bco_override_algorithmic_error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WriteInvocationStoreToPayloadBcoOverrideAlgorithmicErrorType0, data)

        bco_override_algorithmic_error = _parse_bco_override_algorithmic_error(
            d.pop("bco_override_algorithmic_error", UNSET)
        )

        def _parse_bco_override_empirical_error(
            data: object,
        ) -> None | Unset | WriteInvocationStoreToPayloadBcoOverrideEmpiricalErrorType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bco_override_empirical_error_type_0 = (
                    WriteInvocationStoreToPayloadBcoOverrideEmpiricalErrorType0.from_dict(data)
                )

                return bco_override_empirical_error_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WriteInvocationStoreToPayloadBcoOverrideEmpiricalErrorType0, data)

        bco_override_empirical_error = _parse_bco_override_empirical_error(d.pop("bco_override_empirical_error", UNSET))

        def _parse_bco_override_environment_variables(
            data: object,
        ) -> None | Unset | WriteInvocationStoreToPayloadBcoOverrideEnvironmentVariablesType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                bco_override_environment_variables_type_0 = (
                    WriteInvocationStoreToPayloadBcoOverrideEnvironmentVariablesType0.from_dict(data)
                )

                return bco_override_environment_variables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | WriteInvocationStoreToPayloadBcoOverrideEnvironmentVariablesType0, data)

        bco_override_environment_variables = _parse_bco_override_environment_variables(
            d.pop("bco_override_environment_variables", UNSET)
        )

        def _parse_bco_override_xref(data: object) -> list[XrefItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bco_override_xref_type_0 = []
                _bco_override_xref_type_0 = data
                for bco_override_xref_type_0_item_data in _bco_override_xref_type_0:
                    bco_override_xref_type_0_item = XrefItem.from_dict(bco_override_xref_type_0_item_data)

                    bco_override_xref_type_0.append(bco_override_xref_type_0_item)

                return bco_override_xref_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[XrefItem] | None | Unset, data)

        bco_override_xref = _parse_bco_override_xref(d.pop("bco_override_xref", UNSET))

        include_deleted = d.pop("include_deleted", UNSET)

        include_files = d.pop("include_files", UNSET)

        include_hidden = d.pop("include_hidden", UNSET)

        _model_store_format = d.pop("model_store_format", UNSET)
        model_store_format: ModelStoreFormat | Unset
        if isinstance(_model_store_format, Unset):
            model_store_format = UNSET
        else:
            model_store_format = ModelStoreFormat(_model_store_format)

        write_invocation_store_to_payload = cls(
            target_uri=target_uri,
            bco_merge_history_metadata=bco_merge_history_metadata,
            bco_override_algorithmic_error=bco_override_algorithmic_error,
            bco_override_empirical_error=bco_override_empirical_error,
            bco_override_environment_variables=bco_override_environment_variables,
            bco_override_xref=bco_override_xref,
            include_deleted=include_deleted,
            include_files=include_files,
            include_hidden=include_hidden,
            model_store_format=model_store_format,
        )

        write_invocation_store_to_payload.additional_properties = d
        return write_invocation_store_to_payload

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
