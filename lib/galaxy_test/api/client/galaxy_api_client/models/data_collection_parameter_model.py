from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.data_collection_parameter_model_value_type_0 import DataCollectionParameterModelValueType0


T = TypeVar("T", bound="DataCollectionParameterModel")


@_attrs_define
class DataCollectionParameterModel:
    """
    Attributes:
        name (str): Parameter name. Used when referencing parameter in workflows or inside command templating.
        type_ (Literal['data_collection']):
        value (DataCollectionParameterModelValueType0 | None):
        argument (None | str | Unset): If the parameter reflects just one command line argument of a certain tool, this
            tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will
            create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and
            replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is
            implicit).
        collection_type (None | str | Unset):
        extensions (list[str] | Unset):
        help_ (None | str | Unset): Short bit of text, rendered on the tool form just below the associated field to
            provide information about the field.
        hidden (bool | Unset):  Default: False.
        is_dynamic (bool | Unset):  Default: False.
        label (None | str | Unset): Will be displayed on the tool page as the label of the parameter.
        optional (bool | Unset): If `false`, parameter must have a value. Default: False.
        parameter_type (Literal['gx_data_collection'] | Unset):  Default: 'gx_data_collection'.
    """

    name: str
    type_: Literal["data_collection"]
    value: DataCollectionParameterModelValueType0 | None
    argument: None | str | Unset = UNSET
    collection_type: None | str | Unset = UNSET
    extensions: list[str] | Unset = UNSET
    help_: None | str | Unset = UNSET
    hidden: bool | Unset = False
    is_dynamic: bool | Unset = False
    label: None | str | Unset = UNSET
    optional: bool | Unset = False
    parameter_type: Literal["gx_data_collection"] | Unset = "gx_data_collection"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.data_collection_parameter_model_value_type_0 import DataCollectionParameterModelValueType0

        name = self.name

        type_ = self.type_

        value: dict[str, Any] | None
        if isinstance(self.value, DataCollectionParameterModelValueType0):
            value = self.value.to_dict()
        else:
            value = self.value

        argument: None | str | Unset
        if isinstance(self.argument, Unset):
            argument = UNSET
        else:
            argument = self.argument

        collection_type: None | str | Unset
        if isinstance(self.collection_type, Unset):
            collection_type = UNSET
        else:
            collection_type = self.collection_type

        extensions: list[str] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = self.extensions

        help_: None | str | Unset
        if isinstance(self.help_, Unset):
            help_ = UNSET
        else:
            help_ = self.help_

        hidden = self.hidden

        is_dynamic = self.is_dynamic

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        optional = self.optional

        parameter_type = self.parameter_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "type": type_,
                "value": value,
            }
        )
        if argument is not UNSET:
            field_dict["argument"] = argument
        if collection_type is not UNSET:
            field_dict["collection_type"] = collection_type
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if help_ is not UNSET:
            field_dict["help"] = help_
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if is_dynamic is not UNSET:
            field_dict["is_dynamic"] = is_dynamic
        if label is not UNSET:
            field_dict["label"] = label
        if optional is not UNSET:
            field_dict["optional"] = optional
        if parameter_type is not UNSET:
            field_dict["parameter_type"] = parameter_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.data_collection_parameter_model_value_type_0 import DataCollectionParameterModelValueType0

        d = dict(src_dict)
        name = d.pop("name")

        type_ = cast(Literal["data_collection"], d.pop("type"))
        if type_ != "data_collection":
            raise ValueError(f"type must match const 'data_collection', got '{type_}'")

        def _parse_value(data: object) -> DataCollectionParameterModelValueType0 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                value_type_0 = DataCollectionParameterModelValueType0.from_dict(data)

                return value_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DataCollectionParameterModelValueType0 | None, data)

        value = _parse_value(d.pop("value"))

        def _parse_argument(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        argument = _parse_argument(d.pop("argument", UNSET))

        def _parse_collection_type(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        collection_type = _parse_collection_type(d.pop("collection_type", UNSET))

        extensions = cast(list[str], d.pop("extensions", UNSET))

        def _parse_help_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        help_ = _parse_help_(d.pop("help", UNSET))

        hidden = d.pop("hidden", UNSET)

        is_dynamic = d.pop("is_dynamic", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        optional = d.pop("optional", UNSET)

        parameter_type = cast(Literal["gx_data_collection"] | Unset, d.pop("parameter_type", UNSET))
        if parameter_type != "gx_data_collection" and not isinstance(parameter_type, Unset):
            raise ValueError(f"parameter_type must match const 'gx_data_collection', got '{parameter_type}'")

        data_collection_parameter_model = cls(
            name=name,
            type_=type_,
            value=value,
            argument=argument,
            collection_type=collection_type,
            extensions=extensions,
            help_=help_,
            hidden=hidden,
            is_dynamic=is_dynamic,
            label=label,
            optional=optional,
            parameter_type=parameter_type,
        )

        data_collection_parameter_model.additional_properties = d
        return data_collection_parameter_model

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
