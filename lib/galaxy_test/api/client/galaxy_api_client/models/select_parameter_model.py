from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.label_value import LabelValue
    from ..models.no_options_parameter_validator_model import NoOptionsParameterValidatorModel


T = TypeVar("T", bound="SelectParameterModel")


@_attrs_define
class SelectParameterModel:
    """
    Attributes:
        name (str): Parameter name. Used when referencing parameter in workflows or inside command templating.
        type_ (Literal['select']):
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
        multiple (bool | Unset):  Default: False.
        optional (bool | Unset): If `false`, parameter must have a value. Default: False.
        options (list[LabelValue] | None | Unset):
        parameter_type (Literal['gx_select'] | Unset):  Default: 'gx_select'.
        validators (list[NoOptionsParameterValidatorModel] | Unset):
    """

    name: str
    type_: Literal["select"]
    argument: None | str | Unset = UNSET
    help_: None | str | Unset = UNSET
    hidden: bool | Unset = False
    is_dynamic: bool | Unset = False
    label: None | str | Unset = UNSET
    multiple: bool | Unset = False
    optional: bool | Unset = False
    options: list[LabelValue] | None | Unset = UNSET
    parameter_type: Literal["gx_select"] | Unset = "gx_select"
    validators: list[NoOptionsParameterValidatorModel] | Unset = UNSET
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

        multiple = self.multiple

        optional = self.optional

        options: list[dict[str, Any]] | None | Unset
        if isinstance(self.options, Unset):
            options = UNSET
        elif isinstance(self.options, list):
            options = []
            for options_type_0_item_data in self.options:
                options_type_0_item = options_type_0_item_data.to_dict()
                options.append(options_type_0_item)

        else:
            options = self.options

        parameter_type = self.parameter_type

        validators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.validators, Unset):
            validators = []
            for validators_item_data in self.validators:
                validators_item = validators_item_data.to_dict()
                validators.append(validators_item)

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
        if multiple is not UNSET:
            field_dict["multiple"] = multiple
        if optional is not UNSET:
            field_dict["optional"] = optional
        if options is not UNSET:
            field_dict["options"] = options
        if parameter_type is not UNSET:
            field_dict["parameter_type"] = parameter_type
        if validators is not UNSET:
            field_dict["validators"] = validators

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.label_value import LabelValue
        from ..models.no_options_parameter_validator_model import NoOptionsParameterValidatorModel

        d = dict(src_dict)
        name = d.pop("name")

        type_ = cast(Literal["select"], d.pop("type"))
        if type_ != "select":
            raise ValueError(f"type must match const 'select', got '{type_}'")

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

        multiple = d.pop("multiple", UNSET)

        optional = d.pop("optional", UNSET)

        def _parse_options(data: object) -> list[LabelValue] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                options_type_0 = []
                _options_type_0 = data
                for options_type_0_item_data in _options_type_0:
                    options_type_0_item = LabelValue.from_dict(options_type_0_item_data)

                    options_type_0.append(options_type_0_item)

                return options_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[LabelValue] | None | Unset, data)

        options = _parse_options(d.pop("options", UNSET))

        parameter_type = cast(Literal["gx_select"] | Unset, d.pop("parameter_type", UNSET))
        if parameter_type != "gx_select" and not isinstance(parameter_type, Unset):
            raise ValueError(f"parameter_type must match const 'gx_select', got '{parameter_type}'")

        _validators = d.pop("validators", UNSET)
        validators: list[NoOptionsParameterValidatorModel] | Unset = UNSET
        if _validators is not UNSET:
            validators = []
            for validators_item_data in _validators:
                validators_item = NoOptionsParameterValidatorModel.from_dict(validators_item_data)

                validators.append(validators_item)

        select_parameter_model = cls(
            name=name,
            type_=type_,
            argument=argument,
            help_=help_,
            hidden=hidden,
            is_dynamic=is_dynamic,
            label=label,
            multiple=multiple,
            optional=optional,
            options=options,
            parameter_type=parameter_type,
            validators=validators,
        )

        select_parameter_model.additional_properties = d
        return select_parameter_model

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
