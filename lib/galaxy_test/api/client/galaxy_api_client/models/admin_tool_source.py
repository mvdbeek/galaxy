from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.base_url_parameter_model import BaseUrlParameterModel
    from ..models.boolean_parameter_model import BooleanParameterModel
    from ..models.citation import Citation
    from ..models.color_parameter_model import ColorParameterModel
    from ..models.conditional_parameter_model import ConditionalParameterModel
    from ..models.container_requirement import ContainerRequirement
    from ..models.data_collection_parameter_model import DataCollectionParameterModel
    from ..models.data_column_parameter_model import DataColumnParameterModel
    from ..models.data_parameter_model import DataParameterModel
    from ..models.directory_uri_parameter_model import DirectoryUriParameterModel
    from ..models.drill_down_parameter_model import DrillDownParameterModel
    from ..models.float_parameter_model import FloatParameterModel
    from ..models.genome_build_parameter_model import GenomeBuildParameterModel
    from ..models.group_tag_parameter_model import GroupTagParameterModel
    from ..models.help_content import HelpContent
    from ..models.hidden_parameter_model import HiddenParameterModel
    from ..models.incoming_tool_output_collection import IncomingToolOutputCollection
    from ..models.incoming_tool_output_dataset import IncomingToolOutputDataset
    from ..models.integer_parameter_model import IntegerParameterModel
    from ..models.javascript_requirement import JavascriptRequirement
    from ..models.repeat_parameter_model import RepeatParameterModel
    from ..models.resource_requirement import ResourceRequirement
    from ..models.rules_parameter_model import RulesParameterModel
    from ..models.section_parameter_model import SectionParameterModel
    from ..models.select_parameter_model import SelectParameterModel
    from ..models.text_parameter_model import TextParameterModel
    from ..models.tool_output_boolean import ToolOutputBoolean
    from ..models.tool_output_float import ToolOutputFloat
    from ..models.tool_output_integer import ToolOutputInteger
    from ..models.tool_output_text import ToolOutputText
    from ..models.xref_dict import XrefDict


T = TypeVar("T", bound="AdminToolSource")


@_attrs_define
class AdminToolSource:
    """
    Attributes:
        class_ (Literal['GalaxyTool']):
        command (str):
        citations (list[Citation] | None | Unset):
        container (None | str | Unset):
        description (None | str | Unset):
        edam_operations (list[str] | None | Unset):
        edam_topics (list[str] | None | Unset):
        help_ (HelpContent | None | Unset):
        id (None | str | Unset):
        inputs (list[BaseUrlParameterModel | BooleanParameterModel | ColorParameterModel | ConditionalParameterModel |
            DataCollectionParameterModel | DataColumnParameterModel | DataParameterModel | DirectoryUriParameterModel |
            DrillDownParameterModel | FloatParameterModel | GenomeBuildParameterModel | GroupTagParameterModel |
            HiddenParameterModel | IntegerParameterModel | RepeatParameterModel | RulesParameterModel |
            SectionParameterModel | SelectParameterModel | TextParameterModel] | Unset):
        license_ (None | str | Unset):
        name (None | str | Unset):
        outputs (list[IncomingToolOutputCollection | IncomingToolOutputDataset | ToolOutputBoolean | ToolOutputFloat |
            ToolOutputInteger | ToolOutputText] | Unset):
        profile (float | None | Unset):
        requirements (list[ContainerRequirement | JavascriptRequirement | ResourceRequirement] | None | Unset):
        version (None | str | Unset):  Default: '1.0'.
        xrefs (list[XrefDict] | None | Unset):
    """

    class_: Literal["GalaxyTool"]
    command: str
    citations: list[Citation] | None | Unset = UNSET
    container: None | str | Unset = UNSET
    description: None | str | Unset = UNSET
    edam_operations: list[str] | None | Unset = UNSET
    edam_topics: list[str] | None | Unset = UNSET
    help_: HelpContent | None | Unset = UNSET
    id: None | str | Unset = UNSET
    inputs: (
        list[
            BaseUrlParameterModel
            | BooleanParameterModel
            | ColorParameterModel
            | ConditionalParameterModel
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
        | Unset
    ) = UNSET
    license_: None | str | Unset = UNSET
    name: None | str | Unset = UNSET
    outputs: (
        list[
            IncomingToolOutputCollection
            | IncomingToolOutputDataset
            | ToolOutputBoolean
            | ToolOutputFloat
            | ToolOutputInteger
            | ToolOutputText
        ]
        | Unset
    ) = UNSET
    profile: float | None | Unset = UNSET
    requirements: list[ContainerRequirement | JavascriptRequirement | ResourceRequirement] | None | Unset = UNSET
    version: None | str | Unset = "1.0"
    xrefs: list[XrefDict] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.base_url_parameter_model import BaseUrlParameterModel
        from ..models.boolean_parameter_model import BooleanParameterModel
        from ..models.color_parameter_model import ColorParameterModel
        from ..models.conditional_parameter_model import ConditionalParameterModel
        from ..models.data_collection_parameter_model import DataCollectionParameterModel
        from ..models.data_column_parameter_model import DataColumnParameterModel
        from ..models.data_parameter_model import DataParameterModel
        from ..models.directory_uri_parameter_model import DirectoryUriParameterModel
        from ..models.drill_down_parameter_model import DrillDownParameterModel
        from ..models.float_parameter_model import FloatParameterModel
        from ..models.genome_build_parameter_model import GenomeBuildParameterModel
        from ..models.group_tag_parameter_model import GroupTagParameterModel
        from ..models.help_content import HelpContent
        from ..models.hidden_parameter_model import HiddenParameterModel
        from ..models.incoming_tool_output_collection import IncomingToolOutputCollection
        from ..models.incoming_tool_output_dataset import IncomingToolOutputDataset
        from ..models.integer_parameter_model import IntegerParameterModel
        from ..models.javascript_requirement import JavascriptRequirement
        from ..models.repeat_parameter_model import RepeatParameterModel
        from ..models.resource_requirement import ResourceRequirement
        from ..models.rules_parameter_model import RulesParameterModel
        from ..models.select_parameter_model import SelectParameterModel
        from ..models.text_parameter_model import TextParameterModel
        from ..models.tool_output_float import ToolOutputFloat
        from ..models.tool_output_integer import ToolOutputInteger
        from ..models.tool_output_text import ToolOutputText

        class_ = self.class_

        command = self.command

        citations: list[dict[str, Any]] | None | Unset
        if isinstance(self.citations, Unset):
            citations = UNSET
        elif isinstance(self.citations, list):
            citations = []
            for citations_type_0_item_data in self.citations:
                citations_type_0_item = citations_type_0_item_data.to_dict()
                citations.append(citations_type_0_item)

        else:
            citations = self.citations

        container: None | str | Unset
        if isinstance(self.container, Unset):
            container = UNSET
        else:
            container = self.container

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        edam_operations: list[str] | None | Unset
        if isinstance(self.edam_operations, Unset):
            edam_operations = UNSET
        elif isinstance(self.edam_operations, list):
            edam_operations = self.edam_operations

        else:
            edam_operations = self.edam_operations

        edam_topics: list[str] | None | Unset
        if isinstance(self.edam_topics, Unset):
            edam_topics = UNSET
        elif isinstance(self.edam_topics, list):
            edam_topics = self.edam_topics

        else:
            edam_topics = self.edam_topics

        help_: dict[str, Any] | None | Unset
        if isinstance(self.help_, Unset):
            help_ = UNSET
        elif isinstance(self.help_, HelpContent):
            help_ = self.help_.to_dict()
        else:
            help_ = self.help_

        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        inputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.inputs, Unset):
            inputs = []
            for inputs_item_data in self.inputs:
                inputs_item: dict[str, Any]
                if isinstance(inputs_item_data, TextParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, IntegerParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, FloatParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, BooleanParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, HiddenParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, SelectParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, DataParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, DataCollectionParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, DataColumnParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, DirectoryUriParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, RulesParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, DrillDownParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, GroupTagParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, BaseUrlParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, GenomeBuildParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, ColorParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, ConditionalParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                elif isinstance(inputs_item_data, RepeatParameterModel):
                    inputs_item = inputs_item_data.to_dict()
                else:
                    inputs_item = inputs_item_data.to_dict()

                inputs.append(inputs_item)

        license_: None | str | Unset
        if isinstance(self.license_, Unset):
            license_ = UNSET
        else:
            license_ = self.license_

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        outputs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.outputs, Unset):
            outputs = []
            for outputs_item_data in self.outputs:
                outputs_item: dict[str, Any]
                if isinstance(outputs_item_data, IncomingToolOutputDataset):
                    outputs_item = outputs_item_data.to_dict()
                elif isinstance(outputs_item_data, IncomingToolOutputCollection):
                    outputs_item = outputs_item_data.to_dict()
                elif isinstance(outputs_item_data, ToolOutputText):
                    outputs_item = outputs_item_data.to_dict()
                elif isinstance(outputs_item_data, ToolOutputInteger):
                    outputs_item = outputs_item_data.to_dict()
                elif isinstance(outputs_item_data, ToolOutputFloat):
                    outputs_item = outputs_item_data.to_dict()
                else:
                    outputs_item = outputs_item_data.to_dict()

                outputs.append(outputs_item)

        profile: float | None | Unset
        if isinstance(self.profile, Unset):
            profile = UNSET
        else:
            profile = self.profile

        requirements: list[dict[str, Any]] | None | Unset
        if isinstance(self.requirements, Unset):
            requirements = UNSET
        elif isinstance(self.requirements, list):
            requirements = []
            for requirements_type_0_item_data in self.requirements:
                requirements_type_0_item: dict[str, Any]
                if isinstance(requirements_type_0_item_data, JavascriptRequirement):
                    requirements_type_0_item = requirements_type_0_item_data.to_dict()
                elif isinstance(requirements_type_0_item_data, ResourceRequirement):
                    requirements_type_0_item = requirements_type_0_item_data.to_dict()
                else:
                    requirements_type_0_item = requirements_type_0_item_data.to_dict()

                requirements.append(requirements_type_0_item)

        else:
            requirements = self.requirements

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        xrefs: list[dict[str, Any]] | None | Unset
        if isinstance(self.xrefs, Unset):
            xrefs = UNSET
        elif isinstance(self.xrefs, list):
            xrefs = []
            for xrefs_type_0_item_data in self.xrefs:
                xrefs_type_0_item = xrefs_type_0_item_data.to_dict()
                xrefs.append(xrefs_type_0_item)

        else:
            xrefs = self.xrefs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "class": class_,
                "command": command,
            }
        )
        if citations is not UNSET:
            field_dict["citations"] = citations
        if container is not UNSET:
            field_dict["container"] = container
        if description is not UNSET:
            field_dict["description"] = description
        if edam_operations is not UNSET:
            field_dict["edam_operations"] = edam_operations
        if edam_topics is not UNSET:
            field_dict["edam_topics"] = edam_topics
        if help_ is not UNSET:
            field_dict["help"] = help_
        if id is not UNSET:
            field_dict["id"] = id
        if inputs is not UNSET:
            field_dict["inputs"] = inputs
        if license_ is not UNSET:
            field_dict["license"] = license_
        if name is not UNSET:
            field_dict["name"] = name
        if outputs is not UNSET:
            field_dict["outputs"] = outputs
        if profile is not UNSET:
            field_dict["profile"] = profile
        if requirements is not UNSET:
            field_dict["requirements"] = requirements
        if version is not UNSET:
            field_dict["version"] = version
        if xrefs is not UNSET:
            field_dict["xrefs"] = xrefs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.base_url_parameter_model import BaseUrlParameterModel
        from ..models.boolean_parameter_model import BooleanParameterModel
        from ..models.citation import Citation
        from ..models.color_parameter_model import ColorParameterModel
        from ..models.conditional_parameter_model import ConditionalParameterModel
        from ..models.container_requirement import ContainerRequirement
        from ..models.data_collection_parameter_model import DataCollectionParameterModel
        from ..models.data_column_parameter_model import DataColumnParameterModel
        from ..models.data_parameter_model import DataParameterModel
        from ..models.directory_uri_parameter_model import DirectoryUriParameterModel
        from ..models.drill_down_parameter_model import DrillDownParameterModel
        from ..models.float_parameter_model import FloatParameterModel
        from ..models.genome_build_parameter_model import GenomeBuildParameterModel
        from ..models.group_tag_parameter_model import GroupTagParameterModel
        from ..models.help_content import HelpContent
        from ..models.hidden_parameter_model import HiddenParameterModel
        from ..models.incoming_tool_output_collection import IncomingToolOutputCollection
        from ..models.incoming_tool_output_dataset import IncomingToolOutputDataset
        from ..models.integer_parameter_model import IntegerParameterModel
        from ..models.javascript_requirement import JavascriptRequirement
        from ..models.repeat_parameter_model import RepeatParameterModel
        from ..models.resource_requirement import ResourceRequirement
        from ..models.rules_parameter_model import RulesParameterModel
        from ..models.section_parameter_model import SectionParameterModel
        from ..models.select_parameter_model import SelectParameterModel
        from ..models.text_parameter_model import TextParameterModel
        from ..models.tool_output_boolean import ToolOutputBoolean
        from ..models.tool_output_float import ToolOutputFloat
        from ..models.tool_output_integer import ToolOutputInteger
        from ..models.tool_output_text import ToolOutputText
        from ..models.xref_dict import XrefDict

        d = dict(src_dict)
        class_ = cast(Literal["GalaxyTool"], d.pop("class"))
        if class_ != "GalaxyTool":
            raise ValueError(f"class must match const 'GalaxyTool', got '{class_}'")

        command = d.pop("command")

        def _parse_citations(data: object) -> list[Citation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                citations_type_0 = []
                _citations_type_0 = data
                for citations_type_0_item_data in _citations_type_0:
                    citations_type_0_item = Citation.from_dict(citations_type_0_item_data)

                    citations_type_0.append(citations_type_0_item)

                return citations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Citation] | None | Unset, data)

        citations = _parse_citations(d.pop("citations", UNSET))

        def _parse_container(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        container = _parse_container(d.pop("container", UNSET))

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_edam_operations(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                edam_operations_type_0 = cast(list[str], data)

                return edam_operations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        edam_operations = _parse_edam_operations(d.pop("edam_operations", UNSET))

        def _parse_edam_topics(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                edam_topics_type_0 = cast(list[str], data)

                return edam_topics_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        edam_topics = _parse_edam_topics(d.pop("edam_topics", UNSET))

        def _parse_help_(data: object) -> HelpContent | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                help_type_0 = HelpContent.from_dict(data)

                return help_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(HelpContent | None | Unset, data)

        help_ = _parse_help_(d.pop("help", UNSET))

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        _inputs = d.pop("inputs", UNSET)
        inputs: (
            list[
                BaseUrlParameterModel
                | BooleanParameterModel
                | ColorParameterModel
                | ConditionalParameterModel
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
            | Unset
        ) = UNSET
        if _inputs is not UNSET:
            inputs = []
            for inputs_item_data in _inputs:

                def _parse_inputs_item(
                    data: object,
                ) -> (
                    BaseUrlParameterModel
                    | BooleanParameterModel
                    | ColorParameterModel
                    | ConditionalParameterModel
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
                        componentsschemas_galaxy_tool_parameter_model_input_type_0 = TextParameterModel.from_dict(data)

                        return componentsschemas_galaxy_tool_parameter_model_input_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_1 = IntegerParameterModel.from_dict(
                            data
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_2 = FloatParameterModel.from_dict(data)

                        return componentsschemas_galaxy_tool_parameter_model_input_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_3 = BooleanParameterModel.from_dict(
                            data
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_4 = HiddenParameterModel.from_dict(
                            data
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_5 = SelectParameterModel.from_dict(
                            data
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_6 = DataParameterModel.from_dict(data)

                        return componentsschemas_galaxy_tool_parameter_model_input_type_6
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_7 = (
                            DataCollectionParameterModel.from_dict(data)
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_7
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_8 = DataColumnParameterModel.from_dict(
                            data
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_8
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_9 = (
                            DirectoryUriParameterModel.from_dict(data)
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_9
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_10 = RulesParameterModel.from_dict(
                            data
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_10
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_11 = DrillDownParameterModel.from_dict(
                            data
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_11
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_12 = GroupTagParameterModel.from_dict(
                            data
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_12
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_13 = BaseUrlParameterModel.from_dict(
                            data
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_13
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_14 = (
                            GenomeBuildParameterModel.from_dict(data)
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_14
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_15 = ColorParameterModel.from_dict(
                            data
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_15
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_16 = (
                            ConditionalParameterModel.from_dict(data)
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_16
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        componentsschemas_galaxy_tool_parameter_model_input_type_17 = RepeatParameterModel.from_dict(
                            data
                        )

                        return componentsschemas_galaxy_tool_parameter_model_input_type_17
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_galaxy_tool_parameter_model_input_type_18 = SectionParameterModel.from_dict(data)

                    return componentsschemas_galaxy_tool_parameter_model_input_type_18

                inputs_item = _parse_inputs_item(inputs_item_data)

                inputs.append(inputs_item)

        def _parse_license_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        license_ = _parse_license_(d.pop("license", UNSET))

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        _outputs = d.pop("outputs", UNSET)
        outputs: (
            list[
                IncomingToolOutputCollection
                | IncomingToolOutputDataset
                | ToolOutputBoolean
                | ToolOutputFloat
                | ToolOutputInteger
                | ToolOutputText
            ]
            | Unset
        ) = UNSET
        if _outputs is not UNSET:
            outputs = []
            for outputs_item_data in _outputs:

                def _parse_outputs_item(
                    data: object,
                ) -> (
                    IncomingToolOutputCollection
                    | IncomingToolOutputDataset
                    | ToolOutputBoolean
                    | ToolOutputFloat
                    | ToolOutputInteger
                    | ToolOutputText
                ):
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        outputs_item_type_0 = IncomingToolOutputDataset.from_dict(data)

                        return outputs_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        outputs_item_type_1 = IncomingToolOutputCollection.from_dict(data)

                        return outputs_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        outputs_item_type_2 = ToolOutputText.from_dict(data)

                        return outputs_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        outputs_item_type_3 = ToolOutputInteger.from_dict(data)

                        return outputs_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        outputs_item_type_4 = ToolOutputFloat.from_dict(data)

                        return outputs_item_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    outputs_item_type_5 = ToolOutputBoolean.from_dict(data)

                    return outputs_item_type_5

                outputs_item = _parse_outputs_item(outputs_item_data)

                outputs.append(outputs_item)

        def _parse_profile(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        profile = _parse_profile(d.pop("profile", UNSET))

        def _parse_requirements(
            data: object,
        ) -> list[ContainerRequirement | JavascriptRequirement | ResourceRequirement] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                requirements_type_0 = []
                _requirements_type_0 = data
                for requirements_type_0_item_data in _requirements_type_0:

                    def _parse_requirements_type_0_item(
                        data: object,
                    ) -> ContainerRequirement | JavascriptRequirement | ResourceRequirement:
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            requirements_type_0_item_type_0 = JavascriptRequirement.from_dict(data)

                            return requirements_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            requirements_type_0_item_type_1 = ResourceRequirement.from_dict(data)

                            return requirements_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        requirements_type_0_item_type_2 = ContainerRequirement.from_dict(data)

                        return requirements_type_0_item_type_2

                    requirements_type_0_item = _parse_requirements_type_0_item(requirements_type_0_item_data)

                    requirements_type_0.append(requirements_type_0_item)

                return requirements_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[ContainerRequirement | JavascriptRequirement | ResourceRequirement] | None | Unset, data)

        requirements = _parse_requirements(d.pop("requirements", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        def _parse_xrefs(data: object) -> list[XrefDict] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                xrefs_type_0 = []
                _xrefs_type_0 = data
                for xrefs_type_0_item_data in _xrefs_type_0:
                    xrefs_type_0_item = XrefDict.from_dict(xrefs_type_0_item_data)

                    xrefs_type_0.append(xrefs_type_0_item)

                return xrefs_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[XrefDict] | None | Unset, data)

        xrefs = _parse_xrefs(d.pop("xrefs", UNSET))

        admin_tool_source = cls(
            class_=class_,
            command=command,
            citations=citations,
            container=container,
            description=description,
            edam_operations=edam_operations,
            edam_topics=edam_topics,
            help_=help_,
            id=id,
            inputs=inputs,
            license_=license_,
            name=name,
            outputs=outputs,
            profile=profile,
            requirements=requirements,
            version=version,
            xrefs=xrefs,
        )

        admin_tool_source.additional_properties = d
        return admin_tool_source

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
