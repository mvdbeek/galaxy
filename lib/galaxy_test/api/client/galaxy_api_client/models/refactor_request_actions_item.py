from dataclasses import dataclass
from typing import Annotated, TypeAlias

from .add_input_action import AddInputAction
from .add_step_action import AddStepAction
from .connect_action import ConnectAction
from .disconnect_action import DisconnectAction
from .extract_input_action import ExtractInputAction
from .extract_untyped_parameter import ExtractUntypedParameter
from .file_defaults_action import FileDefaultsAction
from .fill_step_defaults_action import FillStepDefaultsAction
from .remove_unlabeled_workflow_outputs import RemoveUnlabeledWorkflowOutputs
from .update_annotation_action import UpdateAnnotationAction
from .update_creator_action import UpdateCreatorAction
from .update_license_action import UpdateLicenseAction
from .update_name_action import UpdateNameAction
from .update_output_label_action import UpdateOutputLabelAction
from .update_report_action import UpdateReportAction
from .update_step_label_action import UpdateStepLabelAction
from .update_step_position_action import UpdateStepPositionAction
from .upgrade_all_steps_action import UpgradeAllStepsAction
from .upgrade_subworkflow_action import UpgradeSubworkflowAction
from .upgrade_tool_action import UpgradeToolAction

__all__ = ["RefactorRequestActionsItem", "RefactorRequestActionsItemDiscriminator"]


@dataclass(frozen=True)
class RefactorRequestActionsItemDiscriminator:
    """Discriminator metadata for RefactorRequestActionsItem union."""

    property_name: str = "action_type"
    """The discriminator property name"""

    # Mapping stored as tuple for frozen dataclass compatibility
    _mapping_data: tuple[tuple[str, str], ...] = (
        ("add_input", "AddInputAction"),
        ("add_step", "AddStepAction"),
        ("connect", "ConnectAction"),
        ("disconnect", "DisconnectAction"),
        ("extract_input", "ExtractInputAction"),
        ("extract_untyped_parameter", "ExtractUntypedParameter"),
        ("fill_defaults", "FileDefaultsAction"),
        ("fill_step_defaults", "FillStepDefaultsAction"),
        ("remove_unlabeled_workflow_outputs", "RemoveUnlabeledWorkflowOutputs"),
        ("update_annotation", "UpdateAnnotationAction"),
        ("update_creator", "UpdateCreatorAction"),
        ("update_license", "UpdateLicenseAction"),
        ("update_name", "UpdateNameAction"),
        ("update_output_label", "UpdateOutputLabelAction"),
        ("update_report", "UpdateReportAction"),
        ("update_step_label", "UpdateStepLabelAction"),
        ("update_step_position", "UpdateStepPositionAction"),
        ("upgrade_all_steps", "UpgradeAllStepsAction"),
        ("upgrade_subworkflow", "UpgradeSubworkflowAction"),
        ("upgrade_tool", "UpgradeToolAction"),
    )

    def get_mapping(self) -> dict[str, type]:
        """Get discriminator mapping with actual type references."""
        from .add_input_action import AddInputAction
        from .add_step_action import AddStepAction
        from .connect_action import ConnectAction
        from .disconnect_action import DisconnectAction
        from .extract_input_action import ExtractInputAction
        from .extract_untyped_parameter import ExtractUntypedParameter
        from .file_defaults_action import FileDefaultsAction
        from .fill_step_defaults_action import FillStepDefaultsAction
        from .remove_unlabeled_workflow_outputs import RemoveUnlabeledWorkflowOutputs
        from .update_annotation_action import UpdateAnnotationAction
        from .update_creator_action import UpdateCreatorAction
        from .update_license_action import UpdateLicenseAction
        from .update_name_action import UpdateNameAction
        from .update_output_label_action import UpdateOutputLabelAction
        from .update_report_action import UpdateReportAction
        from .update_step_label_action import UpdateStepLabelAction
        from .update_step_position_action import UpdateStepPositionAction
        from .upgrade_all_steps_action import UpgradeAllStepsAction
        from .upgrade_subworkflow_action import UpgradeSubworkflowAction
        from .upgrade_tool_action import UpgradeToolAction

        return {
            "add_input": AddInputAction,
            "add_step": AddStepAction,
            "connect": ConnectAction,
            "disconnect": DisconnectAction,
            "extract_input": ExtractInputAction,
            "extract_untyped_parameter": ExtractUntypedParameter,
            "fill_defaults": FileDefaultsAction,
            "fill_step_defaults": FillStepDefaultsAction,
            "remove_unlabeled_workflow_outputs": RemoveUnlabeledWorkflowOutputs,
            "update_annotation": UpdateAnnotationAction,
            "update_creator": UpdateCreatorAction,
            "update_license": UpdateLicenseAction,
            "update_name": UpdateNameAction,
            "update_output_label": UpdateOutputLabelAction,
            "update_report": UpdateReportAction,
            "update_step_label": UpdateStepLabelAction,
            "update_step_position": UpdateStepPositionAction,
            "upgrade_all_steps": UpgradeAllStepsAction,
            "upgrade_subworkflow": UpgradeSubworkflowAction,
            "upgrade_tool": UpgradeToolAction,
        }


RefactorRequestActionsItem: TypeAlias = Annotated[
    AddInputAction
    | AddStepAction
    | ConnectAction
    | DisconnectAction
    | ExtractInputAction
    | ExtractUntypedParameter
    | FileDefaultsAction
    | FillStepDefaultsAction
    | UpdateAnnotationAction
    | UpdateCreatorAction
    | UpdateNameAction
    | UpdateLicenseAction
    | UpdateOutputLabelAction
    | UpdateReportAction
    | UpdateStepLabelAction
    | UpdateStepPositionAction
    | UpgradeSubworkflowAction
    | UpgradeToolAction
    | UpgradeAllStepsAction
    | RemoveUnlabeledWorkflowOutputs,
    RefactorRequestActionsItemDiscriminator(),
]
