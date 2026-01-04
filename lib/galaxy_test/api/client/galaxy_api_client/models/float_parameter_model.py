from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.in_range_parameter_validator_model import InRangeParameterValidatorModel


T = TypeVar("T", bound="FloatParameterModel")


@_attrs_define
class FloatParameterModel:
    """
    Attributes:
        name (str): Parameter name. Used when referencing parameter in workflows or inside command templating.
        type_ (Literal['float']):
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
        max_ (float | None | Unset):
        min_ (float | None | Unset):
        optional (bool | Unset): If `false`, parameter must have a value. Default: False.
        parameter_type (Literal['gx_float'] | Unset):  Default: 'gx_float'.
        validators (list[InRangeParameterValidatorModel] | Unset):
        value (float | None | Unset):
    """

    name: str
    type_: Literal["float"]
    argument: None | str | Unset = UNSET
    help_: None | str | Unset = UNSET
    hidden: bool | Unset = False
    is_dynamic: bool | Unset = False
    label: None | str | Unset = UNSET
    max_: float | None | Unset = UNSET
    min_: float | None | Unset = UNSET
    optional: bool | Unset = False
    parameter_type: Literal["gx_float"] | Unset = "gx_float"
    validators: list[InRangeParameterValidatorModel] | Unset = UNSET
    value: float | None | Unset = UNSET
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

        max_: float | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        min_: float | None | Unset
        if isinstance(self.min_, Unset):
            min_ = UNSET
        else:
            min_ = self.min_

        optional = self.optional

        parameter_type = self.parameter_type

        validators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.validators, Unset):
            validators = []
            for validators_item_data in self.validators:
                validators_item = validators_item_data.to_dict()
                validators.append(validators_item)

        value: float | None | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

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
        if max_ is not UNSET:
            field_dict["max"] = max_
        if min_ is not UNSET:
            field_dict["min"] = min_
        if optional is not UNSET:
            field_dict["optional"] = optional
        if parameter_type is not UNSET:
            field_dict["parameter_type"] = parameter_type
        if validators is not UNSET:
            field_dict["validators"] = validators
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.in_range_parameter_validator_model import InRangeParameterValidatorModel

        d = dict(src_dict)
        name = d.pop("name")

        type_ = cast(Literal["float"], d.pop("type"))
        if type_ != "float":
            raise ValueError(f"type must match const 'float', got '{type_}'")

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

        def _parse_max_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        def _parse_min_(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        min_ = _parse_min_(d.pop("min", UNSET))

        optional = d.pop("optional", UNSET)

        parameter_type = cast(Literal["gx_float"] | Unset, d.pop("parameter_type", UNSET))
        if parameter_type != "gx_float" and not isinstance(parameter_type, Unset):
            raise ValueError(f"parameter_type must match const 'gx_float', got '{parameter_type}'")

        _validators = d.pop("validators", UNSET)
        validators: list[InRangeParameterValidatorModel] | Unset = UNSET
        if _validators is not UNSET:
            validators = []
            for validators_item_data in _validators:
                validators_item = InRangeParameterValidatorModel.from_dict(validators_item_data)

                validators.append(validators_item)

        def _parse_value(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        float_parameter_model = cls(
            name=name,
            type_=type_,
            argument=argument,
            help_=help_,
            hidden=hidden,
            is_dynamic=is_dynamic,
            label=label,
            max_=max_,
            min_=min_,
            optional=optional,
            parameter_type=parameter_type,
            validators=validators,
            value=value,
        )

        float_parameter_model.additional_properties = d
        return float_parameter_model

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
