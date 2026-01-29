from enum import Enum, unique

__all__ = ["RefactorRequestActionsItemActionTypeEnum"]


@unique
class RefactorRequestActionsItemActionTypeEnum(str, Enum):
    """
    Discriminator enum for RefactorRequestActionsItem union types.

    Args:
        add_input (str)          : Value for ADD_INPUT
        add_step (str)           : Value for ADD_STEP
        connect (str)            : Value for CONNECT
        disconnect (str)         : Value for DISCONNECT
        extract_input (str)      : Value for EXTRACT_INPUT
        extract_untyped_parameter (str)
                                 : Value for EXTRACT_UNTYPED_PARAMETER
        fill_defaults (str)      : Value for FILL_DEFAULTS
        fill_step_defaults (str) : Value for FILL_STEP_DEFAULTS
        update_annotation (str)  : Value for UPDATE_ANNOTATION
        update_creator (str)     : Value for UPDATE_CREATOR
        update_name (str)        : Value for UPDATE_NAME
        update_license (str)     : Value for UPDATE_LICENSE
        update_output_label (str): Value for UPDATE_OUTPUT_LABEL
        update_report (str)      : Value for UPDATE_REPORT
        update_step_label (str)  : Value for UPDATE_STEP_LABEL
        update_step_position (str): Value for UPDATE_STEP_POSITION
        upgrade_subworkflow (str): Value for UPGRADE_SUBWORKFLOW
        upgrade_tool (str)       : Value for UPGRADE_TOOL
        upgrade_all_steps (str)  : Value for UPGRADE_ALL_STEPS
        remove_unlabeled_workflow_outputs (str)
                                 : Value for REMOVE_UNLABELED_WORKFLOW_OUTPUTS
    """

    ADD_INPUT = "add_input"
    ADD_STEP = "add_step"
    CONNECT = "connect"
    DISCONNECT = "disconnect"
    EXTRACT_INPUT = "extract_input"
    EXTRACT_UNTYPED_PARAMETER = "extract_untyped_parameter"
    FILL_DEFAULTS = "fill_defaults"
    FILL_STEP_DEFAULTS = "fill_step_defaults"
    UPDATE_ANNOTATION = "update_annotation"
    UPDATE_CREATOR = "update_creator"
    UPDATE_NAME = "update_name"
    UPDATE_LICENSE = "update_license"
    UPDATE_OUTPUT_LABEL = "update_output_label"
    UPDATE_REPORT = "update_report"
    UPDATE_STEP_LABEL = "update_step_label"
    UPDATE_STEP_POSITION = "update_step_position"
    UPGRADE_SUBWORKFLOW = "upgrade_subworkflow"
    UPGRADE_TOOL = "upgrade_tool"
    UPGRADE_ALL_STEPS = "upgrade_all_steps"
    REMOVE_UNLABELED_WORKFLOW_OUTPUTS = "remove_unlabeled_workflow_outputs"
