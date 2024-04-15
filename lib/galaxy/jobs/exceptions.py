from galaxy.util import unicodify

# Describe a parameter value error where there is no actual supplied
# parameter - e.g. just a specification issue.
NO_PARAMETER_VALUE = object()


class ParameterValueError(ValueError):
    def __init__(self, message_suffix, parameter_name, parameter_value=NO_PARAMETER_VALUE, is_dynamic=None):
        message = f"parameter '{parameter_name}': {message_suffix}"
        super().__init__(message)
        self.message_suffix = message_suffix
        self.parameter_name = parameter_name
        self.parameter_value = parameter_value
        self.is_dynamic = is_dynamic

    def to_dict(self):
        as_dict = {"message": unicodify(self)}
        as_dict["message_suffix"] = self.message_suffix
        as_dict["parameter_name"] = self.parameter_name
        if self.parameter_value is not NO_PARAMETER_VALUE:
            as_dict["parameter_value"] = self.parameter_value
        if self.is_dynamic is not None:
            as_dict["is_dynamic"] = self.is_dynamic
        return as_dict
