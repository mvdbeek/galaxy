import pytest

from galaxy.tool_util.data import ToolDataTableManager

LOC_ALPHA_CONTENTS = """
data1	data1name	${__HERE__}/data1/entry.txt
data2	data2name	${__HERE__}/data2/entry.txt
"""


LOC_BETA_CONTENTS_1 = """
beta1	beta1name	${__HERE__}/beta1/entry.txt
"""


LOC_BETA_CONTENTS_2 = """
beta2	beta2name	${__HERE__}/beta2/entry.txt
"""


TOOL_DATA_TABLE_CONF_XML = """<tables>
  <table name="testalpha" comment_char="#">
    <columns>value, name, path</columns>
    <file path="${__HERE__}/testalpha.loc" />
  </table>
</tables>
"""


MERGED_TOOL_DATA_TABLE_CONF_XML_1 = """<tables>
  <table name="testbeta" comment_char="#">
    <columns>value, name, path</columns>
    <file path="${__HERE__}/testbeta1.loc" />
  </table>
</tables>
"""


MERGED_TOOL_DATA_TABLE_CONF_XML_2 = """<tables>
  <table name="testbeta" comment_char="#">
    <columns>value, name, path</columns>
    <file path="${__HERE__}/testbeta2.loc" />
  </table>
</tables>
"""


# Configurations with tool_shed_repository info for testing versioned data managers (issue #20151)
VERSIONED_TOOL_DATA_TABLE_CONF_XML_1 = """<tables>
  <table name="testversioned" comment_char="#">
    <columns>value, name, path</columns>
    <file path="${__HERE__}/testversioned1.loc" />
    <tool_shed_repository>
      <tool_shed>toolshed.g2.bx.psu.edu</tool_shed>
      <repository_name>test_data_manager</repository_name>
      <repository_owner>testowner</repository_owner>
      <installed_changeset_revision>revision1</installed_changeset_revision>
    </tool_shed_repository>
  </table>
</tables>
"""


VERSIONED_TOOL_DATA_TABLE_CONF_XML_2 = """<tables>
  <table name="testversioned" comment_char="#">
    <columns>value, name, path</columns>
    <file path="${__HERE__}/testversioned2.loc" />
    <tool_shed_repository>
      <tool_shed>toolshed.g2.bx.psu.edu</tool_shed>
      <repository_name>test_data_manager</repository_name>
      <repository_owner>testowner</repository_owner>
      <installed_changeset_revision>revision2</installed_changeset_revision>
    </tool_shed_repository>
  </table>
</tables>
"""


@pytest.fixture
def tdt_manager(tmp_path) -> ToolDataTableManager:
    _write_loc_files(tmp_path)
    conf = tmp_path / "tool_data_table_conf.xml"
    conf.write_text(TOOL_DATA_TABLE_CONF_XML)
    return ToolDataTableManager(tmp_path, conf)


@pytest.fixture
def merged_tdt_manager(tmp_path) -> ToolDataTableManager:
    _write_loc_files(tmp_path)
    conf1 = tmp_path / "tool_data_table_conf_1.xml"
    conf1.write_text(MERGED_TOOL_DATA_TABLE_CONF_XML_1)
    conf2 = tmp_path / "tool_data_table_conf_2.xml"
    conf2.write_text(MERGED_TOOL_DATA_TABLE_CONF_XML_2)
    return ToolDataTableManager(tmp_path, f"{conf1},{conf2}")


@pytest.fixture
def versioned_tdt_manager(tmp_path) -> ToolDataTableManager:
    """
    Creates a ToolDataTableManager with two .loc files for the same table,
    each associated with a different tool shed repository version.
    This is used to test that data managers write to the correct versioned .loc file.
    """
    _write_loc_files(tmp_path)
    conf1 = tmp_path / "versioned_tool_data_table_conf_1.xml"
    conf1.write_text(VERSIONED_TOOL_DATA_TABLE_CONF_XML_1)
    conf2 = tmp_path / "versioned_tool_data_table_conf_2.xml"
    conf2.write_text(VERSIONED_TOOL_DATA_TABLE_CONF_XML_2)
    return ToolDataTableManager(tmp_path, f"{conf1},{conf2}")


def _write_loc_files(tmp_path):
    loc1 = tmp_path / "testalpha.loc"
    loc1.write_text(LOC_ALPHA_CONTENTS)

    loc2 = tmp_path / "testbeta1.loc"
    loc2.write_text(LOC_BETA_CONTENTS_1)

    loc3 = tmp_path / "testbeta2.loc"
    loc3.write_text(LOC_BETA_CONTENTS_2)

    # Versioned loc files for testing issue #20151
    loc_versioned1 = tmp_path / "testversioned1.loc"
    loc_versioned1.write_text("# versioned1 loc file\n")

    loc_versioned2 = tmp_path / "testversioned2.loc"
    loc_versioned2.write_text("# versioned2 loc file\n")

    data1 = tmp_path / "data1"
    data1.mkdir()
    data1_entry = data1 / "entry.txt"
    data1_entry.write_text("This is data 1.")

    data2 = tmp_path / "data2"
    data2.mkdir()
    data2_entry = data2 / "entry.txt"
    data2_entry.write_text("This is data 2.")

    data3 = tmp_path / "data3"
    data3.mkdir()
    data3_entry = data3 / "entry.txt"
    data3_entry.write_text("This is data 3.")

    beta1 = tmp_path / "beta1"
    beta1.mkdir()
    beta1_entry = beta1 / "entry.txt"
    beta1_entry.write_text("This is beta 1.")

    beta2 = tmp_path / "beta2"
    beta2.mkdir()
    beta2_entry = beta2 / "entry.txt"
    beta2_entry.write_text("This is beta 2.")
