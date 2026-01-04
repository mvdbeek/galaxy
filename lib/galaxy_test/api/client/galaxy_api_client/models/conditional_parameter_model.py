from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.boolean_parameter_model import BooleanParameterModel
    from ..models.conditional_when import ConditionalWhen
    from ..models.select_parameter_model import SelectParameterModel


T = TypeVar("T", bound="ConditionalParameterModel")


@_attrs_define
class ConditionalParameterModel:
    """
    Attributes:
        name (str): Parameter name. Used when referencing parameter in workflows or inside command templating.
        test_parameter (BooleanParameterModel | SelectParameterModel):
        type_ (Literal['conditional']):
        whens (list[ConditionalWhen]):
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
        parameter_type (Literal['gx_conditional'] | Unset):  Default: 'gx_conditional'.
    """

    name: str
    test_parameter: BooleanParameterModel | SelectParameterModel
    type_: Literal["conditional"]
    whens: list[ConditionalWhen]
    argument: None | str | Unset = UNSET
    help_: None | str | Unset = UNSET
    hidden: bool | Unset = False
    is_dynamic: bool | Unset = False
    label: None | str | Unset = UNSET
    optional: bool | Unset = False
    parameter_type: Literal["gx_conditional"] | Unset = "gx_conditional"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.boolean_parameter_model import BooleanParameterModel

        name = self.name

        test_parameter: dict[str, Any]
        if isinstance(self.test_parameter, BooleanParameterModel):
            test_parameter = self.test_parameter.to_dict()
        else:
            test_parameter = self.test_parameter.to_dict()

        type_ = self.type_

        whens = []
        for whens_item_data in self.whens:
            whens_item = whens_item_data.to_dict()
            whens.append(whens_item)

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
                "test_parameter": test_parameter,
                "type": type_,
                "whens": whens,
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
        from ..models.boolean_parameter_model import BooleanParameterModel
        from ..models.conditional_when import ConditionalWhen
        from ..models.select_parameter_model import SelectParameterModel

        d = dict(src_dict)
        name = d.pop("name")

        def _parse_test_parameter(data: object) -> BooleanParameterModel | SelectParameterModel:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                test_parameter_type_0 = BooleanParameterModel.from_dict(data)

                return test_parameter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            test_parameter_type_1 = SelectParameterModel.from_dict(data)

            return test_parameter_type_1

        test_parameter = _parse_test_parameter(d.pop("test_parameter"))

        type_ = cast(Literal["conditional"], d.pop("type"))
        if type_ != "conditional":
            raise ValueError(f"type must match const 'conditional', got '{type_}'")

        whens = []
        _whens = d.pop("whens")
        for whens_item_data in _whens:
            whens_item = ConditionalWhen.from_dict(whens_item_data)

            whens.append(whens_item)

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

        parameter_type = cast(Literal["gx_conditional"] | Unset, d.pop("parameter_type", UNSET))
        if parameter_type != "gx_conditional" and not isinstance(parameter_type, Unset):
            raise ValueError(f"parameter_type must match const 'gx_conditional', got '{parameter_type}'")

        conditional_parameter_model = cls(
            name=name,
            test_parameter=test_parameter,
            type_=type_,
            whens=whens,
            argument=argument,
            help_=help_,
            hidden=hidden,
            is_dynamic=is_dynamic,
            label=label,
            optional=optional,
            parameter_type=parameter_type,
        )

        conditional_parameter_model.additional_properties = d
        return conditional_parameter_model

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
