from dataclasses import dataclass

__all__ = ["InputReferenceByOrderIndex"]


@dataclass
class InputReferenceByOrderIndex:
    """
    InputReferenceByOrderIndex dataclass.

    Args:
        input_name (str)         : The input name as defined by the workflow module
                                   corresponding to the step being referenced. For Galaxy
                                   tool steps these inputs should be normalized using '|'
                                   (e.g. 'cond|repeat_0|input').
        order_index (int)        : The order_index of the step being referenced. The order
                                   indices of a workflow start at 0.
    """

    input_name: str  # The input name as defined by the workflow module corresponding to the step being referenced. For Galaxy tool steps these inputs should be normalized using '|' (e.g. 'cond|repeat_0|input').
    order_index: int  # The order_index of the step being referenced. The order indices of a workflow start at 0.
