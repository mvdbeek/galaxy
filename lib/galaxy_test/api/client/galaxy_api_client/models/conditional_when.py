from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.base_url_parameter_model import BaseUrlParameterModel
    from ..models.boolean_parameter_model import BooleanParameterModel
    from ..models.color_parameter_model import ColorParameterModel
    from ..models.conditional_parameter_model import ConditionalParameterModel
    from ..models.cwl_boolean_parameter_model import CwlBooleanParameterModel
    from ..models.cwl_directory_parameter_model import CwlDirectoryParameterModel
    from ..models.cwl_file_parameter_model import CwlFileParameterModel
    from ..models.cwl_float_parameter_model import CwlFloatParameterModel
    from ..models.cwl_integer_parameter_model import CwlIntegerParameterModel
    from ..models.cwl_null_parameter_model import CwlNullParameterModel
    from ..models.cwl_string_parameter_model import CwlStringParameterModel
    from ..models.cwl_union_parameter_model import CwlUnionParameterModel
    from ..models.data_collection_parameter_model import DataCollectionParameterModel
    from ..models.data_column_parameter_model import DataColumnParameterModel
    from ..models.data_parameter_model import DataParameterModel
    from ..models.directory_uri_parameter_model import DirectoryUriParameterModel
    from ..models.drill_down_parameter_model import DrillDownParameterModel
    from ..models.float_parameter_model import FloatParameterModel
    from ..models.genome_build_parameter_model import GenomeBuildParameterModel
    from ..models.group_tag_parameter_model import GroupTagParameterModel
    from ..models.hidden_parameter_model import HiddenParameterModel
    from ..models.integer_parameter_model import IntegerParameterModel
    from ..models.repeat_parameter_model import RepeatParameterModel
    from ..models.rules_parameter_model import RulesParameterModel
    from ..models.section_parameter_model import SectionParameterModel
    from ..models.select_parameter_model import SelectParameterModel
    from ..models.text_parameter_model import TextParameterModel


T = TypeVar("T", bound="ConditionalWhen")


@_attrs_define
class ConditionalWhen:
    """
    Attributes:
        discriminator (bool | str):
        is_default_when (bool):
        parameters (list[BaseUrlParameterModel | BooleanParameterModel | ColorParameterModel | ConditionalParameterModel
            | CwlBooleanParameterModel | CwlDirectoryParameterModel | CwlFileParameterModel | CwlFloatParameterModel |
            CwlIntegerParameterModel | CwlNullParameterModel | CwlStringParameterModel | CwlUnionParameterModel |
            DataCollectionParameterModel | DataColumnParameterModel | DataParameterModel | DirectoryUriParameterModel |
            DrillDownParameterModel | FloatParameterModel | GenomeBuildParameterModel | GroupTagParameterModel |
            HiddenParameterModel | IntegerParameterModel | RepeatParameterModel | RulesParameterModel |
            SectionParameterModel | SelectParameterModel | TextParameterModel]):
    """

    discriminator: bool | str
    is_default_when: bool
    parameters: list[
        BaseUrlParameterModel
        | BooleanParameterModel
        | ColorParameterModel
        | ConditionalParameterModel
        | CwlBooleanParameterModel
        | CwlDirectoryParameterModel
        | CwlFileParameterModel
        | CwlFloatParameterModel
        | CwlIntegerParameterModel
        | CwlNullParameterModel
        | CwlStringParameterModel
        | CwlUnionParameterModel
        | DataCollectionParameterModel
        | DataColumnParameterModel
        | DataParameterModel
        | DirectoryUriParameterModel
        | DrillDownParameterModel
        | FloatParameterModel
        | GenomeBuildParameterModel
        | GroupTagParameterModel
        | HiddenParameterModel
        | IntegerParameterModel
        | RepeatParameterModel
        | RulesParameterModel
        | SectionParameterModel
        | SelectParameterModel
        | TextParameterModel
    ]

    def to_dict(self) -> dict[str, Any]:
        from ..models.base_url_parameter_model import BaseUrlParameterModel
        from ..models.boolean_parameter_model import BooleanParameterModel
        from ..models.color_parameter_model import ColorParameterModel
        from ..models.conditional_parameter_model import ConditionalParameterModel
        from ..models.cwl_boolean_parameter_model import CwlBooleanParameterModel
        from ..models.cwl_directory_parameter_model import CwlDirectoryParameterModel
        from ..models.cwl_file_parameter_model import CwlFileParameterModel
        from ..models.cwl_float_parameter_model import CwlFloatParameterModel
        from ..models.cwl_integer_parameter_model import CwlIntegerParameterModel
        from ..models.cwl_null_parameter_model import CwlNullParameterModel
        from ..models.cwl_string_parameter_model import CwlStringParameterModel
        from ..models.cwl_union_parameter_model import CwlUnionParameterModel
        from ..models.data_collection_parameter_model import DataCollectionParameterModel
        from ..models.data_column_parameter_model import DataColumnParameterModel
        from ..models.data_parameter_model import DataParameterModel
        from ..models.directory_uri_parameter_model import DirectoryUriParameterModel
        from ..models.drill_down_parameter_model import DrillDownParameterModel
        from ..models.float_parameter_model import FloatParameterModel
        from ..models.genome_build_parameter_model import GenomeBuildParameterModel
        from ..models.group_tag_parameter_model import GroupTagParameterModel
        from ..models.hidden_parameter_model import HiddenParameterModel
        from ..models.integer_parameter_model import IntegerParameterModel
        from ..models.repeat_parameter_model import RepeatParameterModel
        from ..models.rules_parameter_model import RulesParameterModel
        from ..models.select_parameter_model import SelectParameterModel
        from ..models.text_parameter_model import TextParameterModel

        discriminator: bool | str
        discriminator = self.discriminator

        is_default_when = self.is_default_when

        parameters = []
        for parameters_item_data in self.parameters:
            parameters_item: dict[str, Any]
            if isinstance(parameters_item_data, CwlIntegerParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, CwlFloatParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, CwlStringParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, CwlBooleanParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, CwlNullParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, CwlFileParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, CwlDirectoryParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, CwlUnionParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, TextParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, IntegerParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, FloatParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, BooleanParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, HiddenParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, SelectParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, DataParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, DataCollectionParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, DataColumnParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, DirectoryUriParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, RulesParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, DrillDownParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, GroupTagParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, BaseUrlParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, GenomeBuildParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, ColorParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, ConditionalParameterModel):
                parameters_item = parameters_item_data.to_dict()
            elif isinstance(parameters_item_data, RepeatParameterModel):
                parameters_item = parameters_item_data.to_dict()
            else:
                parameters_item = parameters_item_data.to_dict()

            parameters.append(parameters_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "discriminator": discriminator,
                "is_default_when": is_default_when,
                "parameters": parameters,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_url_parameter_model import BaseUrlParameterModel
        from ..models.boolean_parameter_model import BooleanParameterModel
        from ..models.color_parameter_model import ColorParameterModel
        from ..models.conditional_parameter_model import ConditionalParameterModel
        from ..models.cwl_boolean_parameter_model import CwlBooleanParameterModel
        from ..models.cwl_directory_parameter_model import CwlDirectoryParameterModel
        from ..models.cwl_file_parameter_model import CwlFileParameterModel
        from ..models.cwl_float_parameter_model import CwlFloatParameterModel
        from ..models.cwl_integer_parameter_model import CwlIntegerParameterModel
        from ..models.cwl_null_parameter_model import CwlNullParameterModel
        from ..models.cwl_string_parameter_model import CwlStringParameterModel
        from ..models.cwl_union_parameter_model import CwlUnionParameterModel
        from ..models.data_collection_parameter_model import DataCollectionParameterModel
        from ..models.data_column_parameter_model import DataColumnParameterModel
        from ..models.data_parameter_model import DataParameterModel
        from ..models.directory_uri_parameter_model import DirectoryUriParameterModel
        from ..models.drill_down_parameter_model import DrillDownParameterModel
        from ..models.float_parameter_model import FloatParameterModel
        from ..models.genome_build_parameter_model import GenomeBuildParameterModel
        from ..models.group_tag_parameter_model import GroupTagParameterModel
        from ..models.hidden_parameter_model import HiddenParameterModel
        from ..models.integer_parameter_model import IntegerParameterModel
        from ..models.repeat_parameter_model import RepeatParameterModel
        from ..models.rules_parameter_model import RulesParameterModel
        from ..models.section_parameter_model import SectionParameterModel
        from ..models.select_parameter_model import SelectParameterModel
        from ..models.text_parameter_model import TextParameterModel

        d = dict(src_dict)

        def _parse_discriminator(data: object) -> bool | str:
            return cast(bool | str, data)

        discriminator = _parse_discriminator(d.pop("discriminator"))

        is_default_when = d.pop("is_default_when")

        parameters = []
        _parameters = d.pop("parameters")
        for parameters_item_data in _parameters:

            def _parse_parameters_item(
                data: object,
            ) -> (
                BaseUrlParameterModel
                | BooleanParameterModel
                | ColorParameterModel
                | ConditionalParameterModel
                | CwlBooleanParameterModel
                | CwlDirectoryParameterModel
                | CwlFileParameterModel
                | CwlFloatParameterModel
                | CwlIntegerParameterModel
                | CwlNullParameterModel
                | CwlStringParameterModel
                | CwlUnionParameterModel
                | DataCollectionParameterModel
                | DataColumnParameterModel
                | DataParameterModel
                | DirectoryUriParameterModel
                | DrillDownParameterModel
                | FloatParameterModel
                | GenomeBuildParameterModel
                | GroupTagParameterModel
                | HiddenParameterModel
                | IntegerParameterModel
                | RepeatParameterModel
                | RulesParameterModel
                | SectionParameterModel
                | SelectParameterModel
                | TextParameterModel
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_0 = CwlIntegerParameterModel.from_dict(data)

                    return parameters_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_1 = CwlFloatParameterModel.from_dict(data)

                    return parameters_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_2 = CwlStringParameterModel.from_dict(data)

                    return parameters_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_3 = CwlBooleanParameterModel.from_dict(data)

                    return parameters_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_4 = CwlNullParameterModel.from_dict(data)

                    return parameters_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_5 = CwlFileParameterModel.from_dict(data)

                    return parameters_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_6 = CwlDirectoryParameterModel.from_dict(data)

                    return parameters_item_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_7 = CwlUnionParameterModel.from_dict(data)

                    return parameters_item_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_8 = TextParameterModel.from_dict(data)

                    return parameters_item_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_9 = IntegerParameterModel.from_dict(data)

                    return parameters_item_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_10 = FloatParameterModel.from_dict(data)

                    return parameters_item_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_11 = BooleanParameterModel.from_dict(data)

                    return parameters_item_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_12 = HiddenParameterModel.from_dict(data)

                    return parameters_item_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_13 = SelectParameterModel.from_dict(data)

                    return parameters_item_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_14 = DataParameterModel.from_dict(data)

                    return parameters_item_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_15 = DataCollectionParameterModel.from_dict(data)

                    return parameters_item_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_16 = DataColumnParameterModel.from_dict(data)

                    return parameters_item_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_17 = DirectoryUriParameterModel.from_dict(data)

                    return parameters_item_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_18 = RulesParameterModel.from_dict(data)

                    return parameters_item_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_19 = DrillDownParameterModel.from_dict(data)

                    return parameters_item_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_20 = GroupTagParameterModel.from_dict(data)

                    return parameters_item_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_21 = BaseUrlParameterModel.from_dict(data)

                    return parameters_item_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_22 = GenomeBuildParameterModel.from_dict(data)

                    return parameters_item_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_23 = ColorParameterModel.from_dict(data)

                    return parameters_item_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_24 = ConditionalParameterModel.from_dict(data)

                    return parameters_item_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    parameters_item_type_25 = RepeatParameterModel.from_dict(data)

                    return parameters_item_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                parameters_item_type_26 = SectionParameterModel.from_dict(data)

                return parameters_item_type_26

            parameters_item = _parse_parameters_item(parameters_item_data)

            parameters.append(parameters_item)

        conditional_when = cls(
            discriminator=discriminator,
            is_default_when=is_default_when,
            parameters=parameters,
        )

        return conditional_when
