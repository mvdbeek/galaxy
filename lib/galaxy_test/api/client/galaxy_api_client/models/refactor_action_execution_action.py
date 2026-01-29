from typing import TypeAlias

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

__all__ = ["RefactorActionExecutionAction"]

RefactorActionExecutionAction: TypeAlias = (
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
    | RemoveUnlabeledWorkflowOutputs
)
