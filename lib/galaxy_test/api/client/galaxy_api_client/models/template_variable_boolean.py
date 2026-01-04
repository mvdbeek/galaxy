from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.in_range_parameter_validator_model import InRangeParameterValidatorModel
    from ..models.length_parameter_validator_model import LengthParameterValidatorModel
    from ..models.regex_parameter_validator_model import RegexParameterValidatorModel


T = TypeVar("T", bound="TemplateVariableBoolean")


@_attrs_define
class TemplateVariableBoolean:
    """
    Attributes:
        help_ (None | str):
        name (str):
        type_ (Literal['boolean']):
        default (bool | Unset):  Default: False.
        label (None | str | Unset):
        validators (list[InRangeParameterValidatorModel | LengthParameterValidatorModel | RegexParameterValidatorModel]
            | None | Unset):
    """

    help_: None | str
    name: str
    type_: Literal["boolean"]
    default: bool | Unset = False
    label: None | str | Unset = UNSET
    validators: (
        list[InRangeParameterValidatorModel | LengthParameterValidatorModel | RegexParameterValidatorModel]
        | None
        | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.in_range_parameter_validator_model import InRangeParameterValidatorModel
        from ..models.regex_parameter_validator_model import RegexParameterValidatorModel

        help_: None | str
        help_ = self.help_

        name = self.name

        type_ = self.type_

        default = self.default

        label: None | str | Unset
        if isinstance(self.label, Unset):
            label = UNSET
        else:
            label = self.label

        validators: list[dict[str, Any]] | None | Unset
        if isinstance(self.validators, Unset):
            validators = UNSET
        elif isinstance(self.validators, list):
            validators = []
            for validators_type_0_item_data in self.validators:
                validators_type_0_item: dict[str, Any]
                if isinstance(validators_type_0_item_data, RegexParameterValidatorModel):
                    validators_type_0_item = validators_type_0_item_data.to_dict()
                elif isinstance(validators_type_0_item_data, InRangeParameterValidatorModel):
                    validators_type_0_item = validators_type_0_item_data.to_dict()
                else:
                    validators_type_0_item = validators_type_0_item_data.to_dict()

                validators.append(validators_type_0_item)

        else:
            validators = self.validators

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "help": help_,
                "name": name,
                "type": type_,
            }
        )
        if default is not UNSET:
            field_dict["default"] = default
        if label is not UNSET:
            field_dict["label"] = label
        if validators is not UNSET:
            field_dict["validators"] = validators

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.in_range_parameter_validator_model import InRangeParameterValidatorModel
        from ..models.length_parameter_validator_model import LengthParameterValidatorModel
        from ..models.regex_parameter_validator_model import RegexParameterValidatorModel

        d = dict(src_dict)

        def _parse_help_(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        help_ = _parse_help_(d.pop("help"))

        name = d.pop("name")

        type_ = cast(Literal["boolean"], d.pop("type"))
        if type_ != "boolean":
            raise ValueError(f"type must match const 'boolean', got '{type_}'")

        default = d.pop("default", UNSET)

        def _parse_label(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        label = _parse_label(d.pop("label", UNSET))

        def _parse_validators(
            data: object,
        ) -> (
            list[InRangeParameterValidatorModel | LengthParameterValidatorModel | RegexParameterValidatorModel]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                validators_type_0 = []
                _validators_type_0 = data
                for validators_type_0_item_data in _validators_type_0:

                    def _parse_validators_type_0_item(
                        data: object,
                    ) -> InRangeParameterValidatorModel | LengthParameterValidatorModel | RegexParameterValidatorModel:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            validators_type_0_item_type_0 = RegexParameterValidatorModel.from_dict(data)

                            return validators_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            validators_type_0_item_type_1 = InRangeParameterValidatorModel.from_dict(data)

                            return validators_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        validators_type_0_item_type_2 = LengthParameterValidatorModel.from_dict(data)

                        return validators_type_0_item_type_2

                    validators_type_0_item = _parse_validators_type_0_item(validators_type_0_item_data)

                    validators_type_0.append(validators_type_0_item)

                return validators_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[InRangeParameterValidatorModel | LengthParameterValidatorModel | RegexParameterValidatorModel]
                | None
                | Unset,
                data,
            )

        validators = _parse_validators(d.pop("validators", UNSET))

        template_variable_boolean = cls(
            help_=help_,
            name=name,
            type_=type_,
            default=default,
            label=label,
            validators=validators,
        )

        return template_variable_boolean
