from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.add_input_action import AddInputAction
    from ..models.add_step_action import AddStepAction
    from ..models.connect_action import ConnectAction
    from ..models.disconnect_action import DisconnectAction
    from ..models.extract_input_action import ExtractInputAction
    from ..models.extract_untyped_parameter import ExtractUntypedParameter
    from ..models.file_defaults_action import FileDefaultsAction
    from ..models.fill_step_defaults_action import FillStepDefaultsAction
    from ..models.refactor_action_execution_message import RefactorActionExecutionMessage
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


T = TypeVar("T", bound="RefactorActionExecution")


@_attrs_define
class RefactorActionExecution:
    """
    Attributes:
        action (AddInputAction | AddStepAction | ConnectAction | DisconnectAction | ExtractInputAction |
            ExtractUntypedParameter | FileDefaultsAction | FillStepDefaultsAction | RemoveUnlabeledWorkflowOutputs |
            UpdateAnnotationAction | UpdateCreatorAction | UpdateLicenseAction | UpdateNameAction | UpdateOutputLabelAction
            | UpdateReportAction | UpdateStepLabelAction | UpdateStepPositionAction | UpgradeAllStepsAction |
            UpgradeSubworkflowAction | UpgradeToolAction):
        messages (list[RefactorActionExecutionMessage]):
    """

    action: (
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
    )
    messages: list[RefactorActionExecutionMessage]
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

        action: dict[str, Any]
        if isinstance(self.action, AddInputAction):
            action = self.action.to_dict()
        elif isinstance(self.action, AddStepAction):
            action = self.action.to_dict()
        elif isinstance(self.action, ConnectAction):
            action = self.action.to_dict()
        elif isinstance(self.action, DisconnectAction):
            action = self.action.to_dict()
        elif isinstance(self.action, ExtractInputAction):
            action = self.action.to_dict()
        elif isinstance(self.action, ExtractUntypedParameter):
            action = self.action.to_dict()
        elif isinstance(self.action, FileDefaultsAction):
            action = self.action.to_dict()
        elif isinstance(self.action, FillStepDefaultsAction):
            action = self.action.to_dict()
        elif isinstance(self.action, UpdateAnnotationAction):
            action = self.action.to_dict()
        elif isinstance(self.action, UpdateCreatorAction):
            action = self.action.to_dict()
        elif isinstance(self.action, UpdateNameAction):
            action = self.action.to_dict()
        elif isinstance(self.action, UpdateLicenseAction):
            action = self.action.to_dict()
        elif isinstance(self.action, UpdateOutputLabelAction):
            action = self.action.to_dict()
        elif isinstance(self.action, UpdateReportAction):
            action = self.action.to_dict()
        elif isinstance(self.action, UpdateStepLabelAction):
            action = self.action.to_dict()
        elif isinstance(self.action, UpdateStepPositionAction):
            action = self.action.to_dict()
        elif isinstance(self.action, UpgradeSubworkflowAction):
            action = self.action.to_dict()
        elif isinstance(self.action, UpgradeToolAction):
            action = self.action.to_dict()
        elif isinstance(self.action, UpgradeAllStepsAction):
            action = self.action.to_dict()
        else:
            action = self.action.to_dict()

        messages = []
        for messages_item_data in self.messages:
            messages_item = messages_item_data.to_dict()
            messages.append(messages_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "action": action,
                "messages": messages,
            }
        )

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
        from ..models.refactor_action_execution_message import RefactorActionExecutionMessage
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

        def _parse_action(
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
                action_type_0 = AddInputAction.from_dict(data)

                return action_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_1 = AddStepAction.from_dict(data)

                return action_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_2 = ConnectAction.from_dict(data)

                return action_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_3 = DisconnectAction.from_dict(data)

                return action_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_4 = ExtractInputAction.from_dict(data)

                return action_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_5 = ExtractUntypedParameter.from_dict(data)

                return action_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_6 = FileDefaultsAction.from_dict(data)

                return action_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_7 = FillStepDefaultsAction.from_dict(data)

                return action_type_7
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_8 = UpdateAnnotationAction.from_dict(data)

                return action_type_8
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_9 = UpdateCreatorAction.from_dict(data)

                return action_type_9
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_10 = UpdateNameAction.from_dict(data)

                return action_type_10
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_11 = UpdateLicenseAction.from_dict(data)

                return action_type_11
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_12 = UpdateOutputLabelAction.from_dict(data)

                return action_type_12
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_13 = UpdateReportAction.from_dict(data)

                return action_type_13
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_14 = UpdateStepLabelAction.from_dict(data)

                return action_type_14
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_15 = UpdateStepPositionAction.from_dict(data)

                return action_type_15
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_16 = UpgradeSubworkflowAction.from_dict(data)

                return action_type_16
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_17 = UpgradeToolAction.from_dict(data)

                return action_type_17
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                action_type_18 = UpgradeAllStepsAction.from_dict(data)

                return action_type_18
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            action_type_19 = RemoveUnlabeledWorkflowOutputs.from_dict(data)

            return action_type_19

        action = _parse_action(d.pop("action"))

        messages = []
        _messages = d.pop("messages")
        for messages_item_data in _messages:
            messages_item = RefactorActionExecutionMessage.from_dict(messages_item_data)

            messages.append(messages_item)

        refactor_action_execution = cls(
            action=action,
            messages=messages,
        )

        refactor_action_execution.additional_properties = d
        return refactor_action_execution

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
