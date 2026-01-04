from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

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
    from ..models.rules_parameter_model import RulesParameterModel
    from ..models.section_parameter_model import SectionParameterModel
    from ..models.select_parameter_model import SelectParameterModel
    from ..models.text_parameter_model import TextParameterModel


T = TypeVar("T", bound="RepeatParameterModel")


@_attrs_define
class RepeatParameterModel:
    """
    Attributes:
        name (str): Parameter name. Used when referencing parameter in workflows or inside command templating.
        parameters (list[BaseUrlParameterModel | BooleanParameterModel | ColorParameterModel | ConditionalParameterModel
            | CwlBooleanParameterModel | CwlDirectoryParameterModel | CwlFileParameterModel | CwlFloatParameterModel |
            CwlIntegerParameterModel | CwlNullParameterModel | CwlStringParameterModel | CwlUnionParameterModel |
            DataCollectionParameterModel | DataColumnParameterModel | DataParameterModel | DirectoryUriParameterModel |
            DrillDownParameterModel | FloatParameterModel | GenomeBuildParameterModel | GroupTagParameterModel |
            HiddenParameterModel | IntegerParameterModel | RepeatParameterModel | RulesParameterModel |
            SectionParameterModel | SelectParameterModel | TextParameterModel]):
        type_ (Literal['repeat']):
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
        max_ (int | None | Unset):
        min_ (int | None | Unset):
        optional (bool | Unset): If `false`, parameter must have a value. Default: False.
        parameter_type (Literal['gx_repeat'] | Unset):  Default: 'gx_repeat'.
    """

    name: str
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
    type_: Literal["repeat"]
    argument: None | str | Unset = UNSET
    help_: None | str | Unset = UNSET
    hidden: bool | Unset = False
    is_dynamic: bool | Unset = False
    label: None | str | Unset = UNSET
    max_: int | None | Unset = UNSET
    min_: int | None | Unset = UNSET
    optional: bool | Unset = False
    parameter_type: Literal["gx_repeat"] | Unset = "gx_repeat"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

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
        from ..models.rules_parameter_model import RulesParameterModel
        from ..models.select_parameter_model import SelectParameterModel
        from ..models.text_parameter_model import TextParameterModel

        name = self.name

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

        max_: int | None | Unset
        if isinstance(self.max_, Unset):
            max_ = UNSET
        else:
            max_ = self.max_

        min_: int | None | Unset
        if isinstance(self.min_, Unset):
            min_ = UNSET
        else:
            min_ = self.min_

        optional = self.optional

        parameter_type = self.parameter_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "parameters": parameters,
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
        from ..models.rules_parameter_model import RulesParameterModel
        from ..models.section_parameter_model import SectionParameterModel
        from ..models.select_parameter_model import SelectParameterModel
        from ..models.text_parameter_model import TextParameterModel

        d = dict(src_dict)
        name = d.pop("name")

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

        type_ = cast(Literal["repeat"], d.pop("type"))
        if type_ != "repeat":
            raise ValueError(f"type must match const 'repeat', got '{type_}'")

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

        def _parse_max_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_ = _parse_max_(d.pop("max", UNSET))

        def _parse_min_(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        min_ = _parse_min_(d.pop("min", UNSET))

        optional = d.pop("optional", UNSET)

        parameter_type = cast(Literal["gx_repeat"] | Unset, d.pop("parameter_type", UNSET))
        if parameter_type != "gx_repeat" and not isinstance(parameter_type, Unset):
            raise ValueError(f"parameter_type must match const 'gx_repeat', got '{parameter_type}'")

        repeat_parameter_model = cls(
            name=name,
            parameters=parameters,
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
        )

        repeat_parameter_model.additional_properties = d
        return repeat_parameter_model

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
