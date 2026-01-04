from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.sample_sheet_column_definition_model_type import SampleSheetColumnDefinitionModelType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.in_range_parameter_validator_model import InRangeParameterValidatorModel
    from ..models.length_parameter_validator_model import LengthParameterValidatorModel
    from ..models.regex_parameter_validator_model import RegexParameterValidatorModel


T = TypeVar("T", bound="SampleSheetColumnDefinitionModel")


@_attrs_define
class SampleSheetColumnDefinitionModel:
    """
    Attributes:
        name (str):
        optional (bool):
        type_ (SampleSheetColumnDefinitionModelType):
        default_value (bool | float | int | None | str | Unset):
        description (None | str | Unset):
        restrictions (list[bool | float | int | None | str] | None | Unset):
        suggestions (list[bool | float | int | None | str] | None | Unset):
        validators (list[InRangeParameterValidatorModel | LengthParameterValidatorModel | RegexParameterValidatorModel]
            | None | Unset):
    """

    name: str
    optional: bool
    type_: SampleSheetColumnDefinitionModelType
    default_value: bool | float | int | None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    restrictions: list[bool | float | int | None | str] | None | Unset = UNSET
    suggestions: list[bool | float | int | None | str] | None | Unset = UNSET
    validators: (
        list[InRangeParameterValidatorModel | LengthParameterValidatorModel | RegexParameterValidatorModel]
        | None
        | Unset
    ) = UNSET

    def to_dict(self) -> dict[str, Any]:
        from ..models.in_range_parameter_validator_model import InRangeParameterValidatorModel
        from ..models.regex_parameter_validator_model import RegexParameterValidatorModel

        name = self.name

        optional = self.optional

        type_ = self.type_.value

        default_value: bool | float | int | None | str | Unset
        if isinstance(self.default_value, Unset):
            default_value = UNSET
        else:
            default_value = self.default_value

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        restrictions: list[bool | float | int | None | str] | None | Unset
        if isinstance(self.restrictions, Unset):
            restrictions = UNSET
        elif isinstance(self.restrictions, list):
            restrictions = []
            for restrictions_type_0_item_data in self.restrictions:
                restrictions_type_0_item: bool | float | int | None | str
                restrictions_type_0_item = restrictions_type_0_item_data
                restrictions.append(restrictions_type_0_item)

        else:
            restrictions = self.restrictions

        suggestions: list[bool | float | int | None | str] | None | Unset
        if isinstance(self.suggestions, Unset):
            suggestions = UNSET
        elif isinstance(self.suggestions, list):
            suggestions = []
            for suggestions_type_0_item_data in self.suggestions:
                suggestions_type_0_item: bool | float | int | None | str
                suggestions_type_0_item = suggestions_type_0_item_data
                suggestions.append(suggestions_type_0_item)

        else:
            suggestions = self.suggestions

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
                "name": name,
                "optional": optional,
                "type": type_,
            }
        )
        if default_value is not UNSET:
            field_dict["default_value"] = default_value
        if description is not UNSET:
            field_dict["description"] = description
        if restrictions is not UNSET:
            field_dict["restrictions"] = restrictions
        if suggestions is not UNSET:
            field_dict["suggestions"] = suggestions
        if validators is not UNSET:
            field_dict["validators"] = validators

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.in_range_parameter_validator_model import InRangeParameterValidatorModel
        from ..models.length_parameter_validator_model import LengthParameterValidatorModel
        from ..models.regex_parameter_validator_model import RegexParameterValidatorModel

        d = dict(src_dict)
        name = d.pop("name")

        optional = d.pop("optional")

        type_ = SampleSheetColumnDefinitionModelType(d.pop("type"))

        def _parse_default_value(data: object) -> bool | float | int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | float | int | None | str | Unset, data)

        default_value = _parse_default_value(d.pop("default_value", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_restrictions(data: object) -> list[bool | float | int | None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                restrictions_type_0 = []
                _restrictions_type_0 = data
                for restrictions_type_0_item_data in _restrictions_type_0:

                    def _parse_restrictions_type_0_item(data: object) -> bool | float | int | None | str:
                        if data is None:
                            return data
                        return cast(bool | float | int | None | str, data)

                    restrictions_type_0_item = _parse_restrictions_type_0_item(restrictions_type_0_item_data)

                    restrictions_type_0.append(restrictions_type_0_item)

                return restrictions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[bool | float | int | None | str] | None | Unset, data)

        restrictions = _parse_restrictions(d.pop("restrictions", UNSET))

        def _parse_suggestions(data: object) -> list[bool | float | int | None | str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                suggestions_type_0 = []
                _suggestions_type_0 = data
                for suggestions_type_0_item_data in _suggestions_type_0:

                    def _parse_suggestions_type_0_item(data: object) -> bool | float | int | None | str:
                        if data is None:
                            return data
                        return cast(bool | float | int | None | str, data)

                    suggestions_type_0_item = _parse_suggestions_type_0_item(suggestions_type_0_item_data)

                    suggestions_type_0.append(suggestions_type_0_item)

                return suggestions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[bool | float | int | None | str] | None | Unset, data)

        suggestions = _parse_suggestions(d.pop("suggestions", UNSET))

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

        sample_sheet_column_definition_model = cls(
            name=name,
            optional=optional,
            type_=type_,
            default_value=default_value,
            description=description,
            restrictions=restrictions,
            suggestions=suggestions,
            validators=validators,
        )

        return sample_sheet_column_definition_model
