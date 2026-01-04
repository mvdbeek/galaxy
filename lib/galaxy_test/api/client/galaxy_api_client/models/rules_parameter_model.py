from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RulesParameterModel")


@_attrs_define
class RulesParameterModel:
    """
    Attributes:
        name (str): Parameter name. Used when referencing parameter in workflows or inside command templating.
        type_ (Literal['rules']):
        argument (None | str | Unset): If the parameter reflects just one command line argument of a certain tool, this
            tag should be set to that particular argument. It is rendered in parenthesis after the help section, and it will
            create the name attribute (if not given explicitly) from the argument attribute by stripping leading dashes and
            replacing all remaining dashes by underscores (e.g. if argument="--long-parameter" then name="long_parameter" is
            implicit).
        help_ (None | str | Unset): Short bit of text, rendered on the tool form just below the associated field to
            provide information about the field.
        hidden (bool | Unset):  Default: False.
        is_dynamic (bool | Unset):  Default: False.
        label (None | str | Unset): Will be displayed on the tool page as the label of the parameter.
        optional (bool | Unset): If `false`, parameter must have a value. Default: False.
        parameter_type (Literal['gx_rules'] | Unset):  Default: 'gx_rules'.
    """

    name: str
    type_: Literal["rules"]
    argument: None | str | Unset = UNSET
    help_: None | str | Unset = UNSET
    hidden: bool | Unset = False
    is_dynamic: bool | Unset = False
    label: None | str | Unset = UNSET
    optional: bool | Unset = False
    parameter_type: Literal["gx_rules"] | Unset = "gx_rules"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        type_ = self.type_

        argument: None | str | Unset
        if isinstance(self.argument, Unset):
            argument = UNSET
        else:
            argument = self.argument

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
            }
        )
        if argument is not UNSET:
            field_dict["argument"] = argument
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
        d = dict(src_dict)
        name = d.pop("name")

        type_ = cast(Literal["rules"], d.pop("type"))
        if type_ != "rules":
            raise ValueError(f"type must match const 'rules', got '{type_}'")

        def _parse_argument(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        argument = _parse_argument(d.pop("argument", UNSET))

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

        parameter_type = cast(Literal["gx_rules"] | Unset, d.pop("parameter_type", UNSET))
        if parameter_type != "gx_rules" and not isinstance(parameter_type, Unset):
            raise ValueError(f"parameter_type must match const 'gx_rules', got '{parameter_type}'")

        rules_parameter_model = cls(
            name=name,
            type_=type_,
            argument=argument,
            help_=help_,
            hidden=hidden,
            is_dynamic=is_dynamic,
            label=label,
            optional=optional,
            parameter_type=parameter_type,
        )

        rules_parameter_model.additional_properties = d
        return rules_parameter_model

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
