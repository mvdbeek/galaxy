from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.add_input_action import AddInputAction
    from ..models.add_step_action import AddStepAction
    from ..models.connect_action import ConnectAction
    from ..models.disconnect_action import DisconnectAction
    from ..models.extract_input_action import ExtractInputAction
    from ..models.extract_untyped_parameter import ExtractUntypedParameter
    from ..models.file_defaults_action import FileDefaultsAction
    from ..models.fill_step_defaults_action import FillStepDefaultsAction
    from ..models.remove_unlabeled_workflow_outputs import RemoveUnlabeledWorkflowOutputs
    from ..models.update_annotation_action import UpdateAnnotationAction
    from ..models.update_creator_action import UpdateCreatorAction
    from ..models.update_license_action import UpdateLicenseAction
    from ..models.update_name_action import UpdateNameAction
    from ..models.update_output_label_action import UpdateOutputLabelAction
    from ..models.update_report_action import UpdateReportAction
    from ..models.update_step_label_action import UpdateStepLabelAction
    from ..models.update_step_position_action import UpdateStepPositionAction
    from ..models.upgrade_all_steps_action import UpgradeAllStepsAction
    from ..models.upgrade_subworkflow_action import UpgradeSubworkflowAction
    from ..models.upgrade_tool_action import UpgradeToolAction


T = TypeVar("T", bound="RefactorRequest")


@_attrs_define
class RefactorRequest:
    """
    Attributes:
        actions (list[AddInputAction | AddStepAction | ConnectAction | DisconnectAction | ExtractInputAction |
            ExtractUntypedParameter | FileDefaultsAction | FillStepDefaultsAction | RemoveUnlabeledWorkflowOutputs |
            UpdateAnnotationAction | UpdateCreatorAction | UpdateLicenseAction | UpdateNameAction | UpdateOutputLabelAction
            | UpdateReportAction | UpdateStepLabelAction | UpdateStepPositionAction | UpgradeAllStepsAction |
            UpgradeSubworkflowAction | UpgradeToolAction]):
        dry_run (bool | Unset):  Default: False.
        style (str | Unset):  Default: 'export'.
    """

    actions: list[
        AddInputAction
        | AddStepAction
        | ConnectAction
        | DisconnectAction
        | ExtractInputAction
        | ExtractUntypedParameter
        | FileDefaultsAction
        | FillStepDefaultsAction
        | RemoveUnlabeledWorkflowOutputs
        | UpdateAnnotationAction
        | UpdateCreatorAction
        | UpdateLicenseAction
        | UpdateNameAction
        | UpdateOutputLabelAction
        | UpdateReportAction
        | UpdateStepLabelAction
        | UpdateStepPositionAction
        | UpgradeAllStepsAction
        | UpgradeSubworkflowAction
        | UpgradeToolAction
    ]
    dry_run: bool | Unset = False
    style: str | Unset = "export"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.add_input_action import AddInputAction
        from ..models.add_step_action import AddStepAction
        from ..models.connect_action import ConnectAction
        from ..models.disconnect_action import DisconnectAction
        from ..models.extract_input_action import ExtractInputAction
        from ..models.extract_untyped_parameter import ExtractUntypedParameter
        from ..models.file_defaults_action import FileDefaultsAction
        from ..models.fill_step_defaults_action import FillStepDefaultsAction
        from ..models.update_annotation_action import UpdateAnnotationAction
        from ..models.update_creator_action import UpdateCreatorAction
        from ..models.update_license_action import UpdateLicenseAction
        from ..models.update_name_action import UpdateNameAction
        from ..models.update_output_label_action import UpdateOutputLabelAction
        from ..models.update_report_action import UpdateReportAction
        from ..models.update_step_label_action import UpdateStepLabelAction
        from ..models.update_step_position_action import UpdateStepPositionAction
        from ..models.upgrade_all_steps_action import UpgradeAllStepsAction
        from ..models.upgrade_subworkflow_action import UpgradeSubworkflowAction
        from ..models.upgrade_tool_action import UpgradeToolAction

        actions = []
        for actions_item_data in self.actions:
            actions_item: dict[str, Any]
            if isinstance(actions_item_data, AddInputAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, AddStepAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ConnectAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, DisconnectAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ExtractInputAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, ExtractUntypedParameter):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, FileDefaultsAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, FillStepDefaultsAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, UpdateAnnotationAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, UpdateCreatorAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, UpdateNameAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, UpdateLicenseAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, UpdateOutputLabelAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, UpdateReportAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, UpdateStepLabelAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, UpdateStepPositionAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, UpgradeSubworkflowAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, UpgradeToolAction):
                actions_item = actions_item_data.to_dict()
            elif isinstance(actions_item_data, UpgradeAllStepsAction):
                actions_item = actions_item_data.to_dict()
            else:
                actions_item = actions_item_data.to_dict()

            actions.append(actions_item)

        dry_run = self.dry_run

        style = self.style

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "actions": actions,
            }
        )
        if dry_run is not UNSET:
            field_dict["dry_run"] = dry_run
        if style is not UNSET:
            field_dict["style"] = style

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.add_input_action import AddInputAction
        from ..models.add_step_action import AddStepAction
        from ..models.connect_action import ConnectAction
        from ..models.disconnect_action import DisconnectAction
        from ..models.extract_input_action import ExtractInputAction
        from ..models.extract_untyped_parameter import ExtractUntypedParameter
        from ..models.file_defaults_action import FileDefaultsAction
        from ..models.fill_step_defaults_action import FillStepDefaultsAction
        from ..models.remove_unlabeled_workflow_outputs import RemoveUnlabeledWorkflowOutputs
        from ..models.update_annotation_action import UpdateAnnotationAction
        from ..models.update_creator_action import UpdateCreatorAction
        from ..models.update_license_action import UpdateLicenseAction
        from ..models.update_name_action import UpdateNameAction
        from ..models.update_output_label_action import UpdateOutputLabelAction
        from ..models.update_report_action import UpdateReportAction
        from ..models.update_step_label_action import UpdateStepLabelAction
        from ..models.update_step_position_action import UpdateStepPositionAction
        from ..models.upgrade_all_steps_action import UpgradeAllStepsAction
        from ..models.upgrade_subworkflow_action import UpgradeSubworkflowAction
        from ..models.upgrade_tool_action import UpgradeToolAction

        d = dict(src_dict)
        actions = []
        _actions = d.pop("actions")
        for actions_item_data in _actions:

            def _parse_actions_item(
                data: object,
            ) -> (
                AddInputAction
                | AddStepAction
                | ConnectAction
                | DisconnectAction
                | ExtractInputAction
                | ExtractUntypedParameter
                | FileDefaultsAction
                | FillStepDefaultsAction
                | RemoveUnlabeledWorkflowOutputs
                | UpdateAnnotationAction
                | UpdateCreatorAction
                | UpdateLicenseAction
                | UpdateNameAction
                | UpdateOutputLabelAction
                | UpdateReportAction
                | UpdateStepLabelAction
                | UpdateStepPositionAction
                | UpgradeAllStepsAction
                | UpgradeSubworkflowAction
                | UpgradeToolAction
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_0 = AddInputAction.from_dict(data)

                    return actions_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_1 = AddStepAction.from_dict(data)

                    return actions_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_2 = ConnectAction.from_dict(data)

                    return actions_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_3 = DisconnectAction.from_dict(data)

                    return actions_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_4 = ExtractInputAction.from_dict(data)

                    return actions_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_5 = ExtractUntypedParameter.from_dict(data)

                    return actions_item_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_6 = FileDefaultsAction.from_dict(data)

                    return actions_item_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_7 = FillStepDefaultsAction.from_dict(data)

                    return actions_item_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_8 = UpdateAnnotationAction.from_dict(data)

                    return actions_item_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_9 = UpdateCreatorAction.from_dict(data)

                    return actions_item_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_10 = UpdateNameAction.from_dict(data)

                    return actions_item_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_11 = UpdateLicenseAction.from_dict(data)

                    return actions_item_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_12 = UpdateOutputLabelAction.from_dict(data)

                    return actions_item_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_13 = UpdateReportAction.from_dict(data)

                    return actions_item_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_14 = UpdateStepLabelAction.from_dict(data)

                    return actions_item_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_15 = UpdateStepPositionAction.from_dict(data)

                    return actions_item_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_16 = UpgradeSubworkflowAction.from_dict(data)

                    return actions_item_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_17 = UpgradeToolAction.from_dict(data)

                    return actions_item_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    actions_item_type_18 = UpgradeAllStepsAction.from_dict(data)

                    return actions_item_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                actions_item_type_19 = RemoveUnlabeledWorkflowOutputs.from_dict(data)

                return actions_item_type_19

            actions_item = _parse_actions_item(actions_item_data)

            actions.append(actions_item)

        dry_run = d.pop("dry_run", UNSET)

        style = d.pop("style", UNSET)

        refactor_request = cls(
            actions=actions,
            dry_run=dry_run,
            style=style,
        )

        refactor_request.additional_properties = d
        return refactor_request

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
