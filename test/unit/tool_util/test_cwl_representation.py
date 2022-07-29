from galaxy.tool_util.cwl import tool_proxy
from .test_cwl import _cwl_tool_path


def test_cwl_parameter_schema_conversion():
    bwa_tool = tool_proxy(_cwl_tool_path("v1.2/tests/bwa-mem-tool.cwl"))
    cwl_tool = bwa_tool._tool
    names_to_schema = {}
    for field in cwl_tool.inputs_record_schema["fields"]:
        names_to_schema[field["name"]] = field["type"]
    x = 123
    x = 123
    x = 123


def test_cwl_parameter_schema_conversion_tmap():
    cwl_tool = tool_proxy(_cwl_tool_path("v1.2/tests/tmap-tool.cwl"))._tool
    names_to_schema = {}
    for field in cwl_tool.inputs_record_schema["fields"]:
        names_to_schema[field["name"]] = field["type"]
    x = 123
    x = 123
    x = 123
