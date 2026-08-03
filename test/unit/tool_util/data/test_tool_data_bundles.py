import csv
import json
import os
from dataclasses import dataclass

import pytest

from galaxy.tool_util.data import (
    BUNDLE_INDEX_FILE_NAME,
    BundleProcessingOptions,
)
from galaxy.tool_util.data.bundles.models import (
    convert_data_tables_xml,
    DataTableBundleProcessorDescription,
    get_path_headers,
)
from galaxy.util import (
    galaxy_directory,
    parse_xml,
)
from galaxy.util.resources import (
    as_file,
    resource_path,
)

TOOLS_DIRECTORY = os.path.abspath(os.path.join(galaxy_directory(), "test/functional/tools/"))


def test_xml_parsing() -> None:
    path = os.path.join(TOOLS_DIRECTORY, "sample_data_manager_conf.xml")
    tree = parse_xml(path)
    data_managers_el = tree.getroot()
    data_manager_el = data_managers_el.find("data_manager")
    assert data_manager_el is not None
    description = convert_data_tables_xml(data_manager_el)
    assert not description.undeclared_tables
    assert len(description.data_tables) == 1
    data_table = description.data_tables[0]
    output = data_table.output
    assert output
    columns = output.columns
    assert len(columns) == 2
    column1 = columns[0]
    assert column1.name == "value"
    assert column1.output_ref is None
    column2 = columns[1]
    assert column2.name == "path"
    assert column2.output_ref == "out_file"
    moves = column2.moves
    assert len(moves) == 1
    move = moves[0]
    assert move.type == "directory"
    assert move.relativize_symlinks is True
    assert move.target_base == "${GALAXY_DATA_MANAGER_DATA_PATH}"
    assert move.target_value == "testbeta/${value}"
    assert move.source_base is None
    assert move.source_value == ""


def test_parsing_manual() -> None:
    with as_file(resource_path(__name__, "example_data_managers/manual.xml")) as path:
        tree = parse_xml(path)
    data_managers_el = tree.getroot()
    data_manager_el = data_managers_el.find("data_manager")
    assert data_manager_el is not None
    description = convert_data_tables_xml(data_manager_el)
    assert description.undeclared_tables
    assert len(description.data_tables) == 0


def test_parsing_mothur() -> None:
    with as_file(resource_path(__name__, "example_data_managers/mothur.xml")) as path:
        tree = parse_xml(path)
    data_managers_el = tree.getroot()
    data_manager_el = data_managers_el.find("data_manager")
    assert data_manager_el is not None
    description = convert_data_tables_xml(data_manager_el)
    assert not description.undeclared_tables
    assert len(description.data_tables) == 4


@dataclass
class OutputDataset:
    file_name_: str
    extra_files_path: str
    ext: str = "data_manager_json"

    def get_file_name(self, sync_cache=True, auth=None) -> str:
        return self.file_name_

    def extra_files_path_exists(self) -> bool:
        return os.path.exists(self.extra_files_path)


def prepare_typical_output_and_description(tmp_path):
    target_path = tmp_path / "newvalue.txt"
    target_path.write_text("Moo Cow")
    output = {"data_tables": {"testalpha": [{"value": "newvalue", "name": "mynewname", "path": "newvalue.txt"}]}}
    output_dataset_path = tmp_path / "output.dat"
    output_dataset_path.write_text(json.dumps(output))
    extra_files_path = tmp_path / "extra"
    extra_files_path.mkdir()
    output_dataset = OutputDataset(
        output_dataset_path,
        extra_files_path,
    )
    out_data = {"out1": output_dataset}
    data_table = {
        "name": "testalpha",
        "output": {
            "columns": [
                {
                    "name": "value",
                },
                {
                    "name": "name",
                },
                {
                    "name": "path",
                    "data_table_name": "path",
                    "output_ref": "out1",
                    "moves": [
                        {
                            "type": "directory",
                            "relativize_symlinks": True,
                            "target_value": "testalpha/${value}",
                            "target_base": "${GALAXY_DATA_MANAGER_DATA_PATH}",
                        }
                    ],
                    "value_translations": [
                        {"value": "${GALAXY_DATA_MANAGER_DATA_PATH}/testalpha/${value}/${path}", "type": "template"},
                        {"value": "abspath", "type": "function"},
                    ],
                },
            ]
        },
    }
    process_description = DataTableBundleProcessorDescription(
        **{
            "undeclared_tables": False,
            "data_tables": [data_table],
        }
    )
    return out_data, process_description


def test_typical_processing(tdt_manager, tmp_path):
    options = BundleProcessingOptions(
        what="data manager 'mock'",
        data_manager_path=str(tmp_path),
        target_config_file=str(tmp_path / "sample_data_managers_conf.xml"),
    )
    out_data, process_description = prepare_typical_output_and_description(tmp_path)
    repo_info = None
    tdt_manager.process_bundle(
        out_data,
        process_description,
        repo_info,
        options,
    )
    loc1 = tmp_path / "testalpha.loc"
    new_row = _last_row(loc1)
    assert new_row[0] == "newvalue"
    assert new_row[1] == "mynewname"
    assert new_row[2] == str(tmp_path / "testalpha" / "newvalue" / "newvalue.txt")


def test_write_bundle(tdt_manager, tmp_path):
    out_data, process_description = prepare_typical_output_and_description(tmp_path)
    tdt_manager.write_bundle(
        out_data,
        process_description,
        repo_info=None,
    )
    extra = tmp_path / "extra"
    bundle_index_json_path = extra / BUNDLE_INDEX_FILE_NAME
    assert bundle_index_json_path.exists()
    with open(bundle_index_json_path) as f:
        bundle_index = json.load(f)
    assert "processor_description" in bundle_index
    assert "data_tables" in bundle_index
    assert "output_name" in bundle_index


def test_import_bundle(tdt_manager, tmp_path):
    out_data, process_description = prepare_typical_output_and_description(tmp_path)
    tdt_manager.write_bundle(
        out_data,
        process_description,
        None,
    )

    # Writing the bundle didn't update the loc files.
    loc1 = tmp_path / "testalpha.loc"
    new_row = _last_row(loc1)
    assert new_row[0] != "newvalue"

    options = BundleProcessingOptions(
        what="data manager 'mock'",
        data_manager_path=str(tmp_path),
        target_config_file=str(tmp_path / "sample_data_managers_conf.xml"),
    )
    tdt_manager.import_bundle(
        str(tmp_path / "extra"),
        options,
    )

    # Importing the bundle does update the loc files though.
    loc1 = tmp_path / "testalpha.loc"
    new_row = _last_row(loc1)
    assert new_row[0] == "newvalue"
    assert new_row[1] == "mynewname"
    assert new_row[2] == str(tmp_path / "testalpha" / "newvalue" / "newvalue.txt")


def prepare_absolute_path_output_and_description(tmp_path, table_name="testalpha", path_column="path"):
    """Mirror a data manager recording an absolute path with a ``${column}`` move source.

    ``path_column`` defaults to the conventional ``path`` (as MetaPhlAn uses); pass
    another name (e.g. CAT's ``database_folder``) to model a data manager whose path
    column is not literally called ``path``.
    """
    index = "mpa_toy"
    extra_files_path = tmp_path / "extra"
    staged = extra_files_path / index
    staged.mkdir(parents=True)
    (staged / f"{index}.pkl").write_text("PICKLE")

    # Absolute path, as MetaPhlAn records it (points inside extra_files_path).
    recorded_path = str(staged)
    output = {"data_tables": {table_name: [{"value": index, "name": "toy", path_column: recorded_path}]}}
    output_dataset_path = tmp_path / "output.dat"
    output_dataset_path.write_text(json.dumps(output))
    output_dataset = OutputDataset(output_dataset_path, extra_files_path)
    out_data = {"out1": output_dataset}
    data_table = {
        "name": table_name,
        "output": {
            "columns": [
                {"name": "value"},
                {"name": "name"},
                {
                    "name": path_column,
                    "output_ref": "out1",
                    "moves": [
                        {
                            "type": "directory",
                            "relativize_symlinks": False,
                            "source_value": "${" + path_column + "}",
                            "target_value": "metaphlan/data/${value}",
                            "target_base": "${GALAXY_DATA_MANAGER_DATA_PATH}",
                        }
                    ],
                    "value_translations": [
                        {"value": "${GALAXY_DATA_MANAGER_DATA_PATH}/metaphlan/data/${value}", "type": "template"},
                        {"value": "abspath", "type": "function"},
                    ],
                },
            ]
        },
    }
    process_description = DataTableBundleProcessorDescription(
        **{"undeclared_tables": False, "data_tables": [data_table]}
    )
    return index, out_data, process_description


@pytest.mark.parametrize(
    ("table_name", "path_column"),
    [
        ("testalpha", "path"),  # the conventional column, à la MetaPhlAn
        ("testcat", "database_folder"),  # a differently-named path column, à la CAT
    ],
)
def test_import_bundle_with_absolute_recorded_path(tdt_manager, tmp_path, table_name, path_column):
    """Write must relativize, and import must stage, an absolute recorded path.

    Covers both the conventional ``path`` column and a differently-named one, so a
    ``path``-only assumption anywhere in the write/import wiring is caught. Renaming
    the extra-files dir before import models transport to another host, where the
    recorded absolute job dir no longer exists.
    """
    index, out_data, process_description = prepare_absolute_path_output_and_description(
        tmp_path, table_name=table_name, path_column=path_column
    )
    tdt_manager.write_bundle(out_data, process_description, None)

    # Write relativized the absolute job path and staged the move's relative layout.
    bundle_index = json.loads((tmp_path / "extra" / BUNDLE_INDEX_FILE_NAME).read_text())
    stored_path = bundle_index["data_tables"][table_name][0][path_column]
    assert stored_path == os.path.join("metaphlan", "data", index)
    assert not os.path.isabs(stored_path)
    # The files were physically moved into that layout, raw dir gone.
    assert os.path.exists(tmp_path / "extra" / stored_path / f"{index}.pkl")
    assert not (tmp_path / "extra" / index).exists()

    # Transport the bundle: the location it was written at is gone by import.
    transported = tmp_path / "imported"
    os.rename(tmp_path / "extra", transported)

    options = BundleProcessingOptions(
        what="data manager 'mock'",
        data_manager_path=str(tmp_path),
        target_config_file=str(tmp_path / "sample_data_managers_conf.xml"),
    )
    tdt_manager.import_bundle(str(transported), options)

    new_row = _last_row(tmp_path / f"{table_name}.loc")
    assert new_row[0] == index
    loc_target = new_row[-1]
    # The DB files were actually moved to where the loc entry points.
    assert os.path.exists(os.path.join(loc_target, f"{index}.pkl"))


def prepare_split_prefix_output_and_description(
    tmp_path,
    table_name="testalpha",
    path_column="path",
    store_leaf=None,
    compute_leaf=None,
    recorded_relative_path=None,
):
    """Model the object-store vs job-working-dir prefix split.

    In production ``write_bundle`` runs on the job handler, where
    ``dataset.extra_files_path`` resolves to the object-store extra-files dir,
    while the data manager baked its absolute ``path`` on the compute node under
    the transient job working dir. The directories differ in every prefix
    component, so a plain ``os.path.relpath`` escapes with ``..``. They may even
    differ in the ``dataset_<key>_files`` leaf itself: the compute side is
    uuid-keyed under outputs_to_working_directory while the store may be
    id-keyed — pass distinct ``store_leaf``/``compute_leaf`` to model that. The
    recorded absolute path deliberately does NOT exist under
    ``extra_files_path`` here, so the fix must be structural (no existence check).
    """
    index = "mpa_toy"
    compute_leaf = compute_leaf or "dataset_00000000-0000-0000-0000-000000000000_files"
    store_leaf = store_leaf or compute_leaf

    # Object-store extra-files dir: where the bundle index actually gets written.
    extra_files_path = tmp_path / "objectstore" / "000" / store_leaf
    extra_files_path.mkdir(parents=True)

    # Absolute path as recorded by the DM under the (now-irrelevant) job working dir.
    job_dir = tmp_path / "jobs" / "001" / "outputs" / compute_leaf
    recorded_path = str(job_dir / (index if recorded_relative_path is None else recorded_relative_path))

    output = {"data_tables": {table_name: [{"value": index, "name": "toy", path_column: recorded_path}]}}
    output_dataset_path = tmp_path / "output.dat"
    output_dataset_path.write_text(json.dumps(output))
    output_dataset = OutputDataset(output_dataset_path, extra_files_path)
    out_data = {"out1": output_dataset}
    data_table = {
        "name": table_name,
        "output": {
            "columns": [
                {"name": "value"},
                {"name": "name"},
                {
                    "name": path_column,
                    "output_ref": "out1",
                    "moves": [
                        {
                            "type": "directory",
                            "relativize_symlinks": False,
                            "source_value": "${" + path_column + "}",
                            "target_value": "metaphlan/data/${value}",
                            "target_base": "${GALAXY_DATA_MANAGER_DATA_PATH}",
                        }
                    ],
                    "value_translations": [
                        {"value": "${GALAXY_DATA_MANAGER_DATA_PATH}/metaphlan/data/${value}", "type": "template"},
                        {"value": "abspath", "type": "function"},
                    ],
                },
            ]
        },
    }
    process_description = DataTableBundleProcessorDescription(
        **{"undeclared_tables": False, "data_tables": [data_table]}
    )
    return index, extra_files_path, job_dir, out_data, process_description


def test_write_bundle_relativizes_split_prefix_path_from_compute_root(tdt_manager, tmp_path):
    """A data manager's compute-side path is made relative to its known job-dir root."""
    index, extra_files_path, compute_extra_files_path, out_data, process_description = (
        prepare_split_prefix_output_and_description(tmp_path)
    )
    tdt_manager.write_bundle(
        out_data,
        process_description,
        None,
        source_extra_files_paths={"out1": str(compute_extra_files_path)},
    )

    bundle_index = json.loads((extra_files_path / BUNDLE_INDEX_FILE_NAME).read_text())
    stored_path = bundle_index["data_tables"]["testalpha"][0]["path"]
    assert stored_path == index
    assert not os.path.isabs(stored_path)


def test_write_bundle_relativizes_uuid_keyed_job_path_on_id_keyed_store(tdt_manager, tmp_path):
    """A uuid-keyed compute root works even when the object store is id-keyed."""
    index, extra_files_path, compute_extra_files_path, out_data, process_description = (
        prepare_split_prefix_output_and_description(
            tmp_path,
            store_leaf="dataset_42_files",
            compute_leaf="dataset_00000000-0000-0000-0000-000000000000_files",
        )
    )
    tdt_manager.write_bundle(
        out_data,
        process_description,
        None,
        source_extra_files_paths={"out1": str(compute_extra_files_path)},
    )

    bundle_index = json.loads((extra_files_path / BUNDLE_INDEX_FILE_NAME).read_text())
    stored_path = bundle_index["data_tables"]["testalpha"][0]["path"]
    assert stored_path == index
    assert not os.path.isabs(stored_path)


def test_write_bundle_relativizes_compute_extra_files_root(tdt_manager, tmp_path):
    _, extra_files_path, compute_extra_files_path, out_data, process_description = (
        prepare_split_prefix_output_and_description(tmp_path, recorded_relative_path="")
    )
    tdt_manager.write_bundle(
        out_data,
        process_description,
        None,
        source_extra_files_paths={"out1": str(compute_extra_files_path)},
    )

    bundle_index = json.loads((extra_files_path / BUNDLE_INDEX_FILE_NAME).read_text())
    assert bundle_index["data_tables"]["testalpha"][0]["path"] == os.curdir


def test_write_bundle_preserves_nested_dataset_named_directory(tdt_manager, tmp_path):
    store_leaf = "dataset_42_files"
    relative_path = os.path.join("mpa_toy", store_leaf, "index")
    _, extra_files_path, compute_extra_files_path, out_data, process_description = (
        prepare_split_prefix_output_and_description(
            tmp_path, store_leaf=store_leaf, recorded_relative_path=relative_path
        )
    )
    tdt_manager.write_bundle(
        out_data,
        process_description,
        None,
        source_extra_files_paths={"out1": str(compute_extra_files_path)},
    )

    bundle_index = json.loads((extra_files_path / BUNDLE_INDEX_FILE_NAME).read_text())
    assert bundle_index["data_tables"]["testalpha"][0]["path"] == relative_path


def test_path_headers_from_move_and_abspath():
    """A column is a path column when it has a move or an abspath translation, whatever its name."""
    description = DataTableBundleProcessorDescription(
        undeclared_tables=False,
        data_tables=[
            {
                "name": "t",
                "output": {
                    "columns": [
                        {"name": "value"},
                        {"name": "path", "moves": [{"type": "directory", "relativize_symlinks": False}]},
                        {"name": "index_path", "value_translations": [{"type": "function", "value": "abspath"}]},
                        # An output_ref alone does not make a column a path.
                        {"name": "reference", "output_ref": "out1"},
                    ]
                },
            }
        ],
    )
    assert description.path_headers_by_data_table == {"t": {"path", "index_path"}}
    assert get_path_headers(description, "t") == {"path", "index_path"}


def test_get_path_headers_falls_back_to_convention():
    """Without a declared path column (undeclared tables, or no description) use the ``path`` convention."""
    assert get_path_headers(None, "t") == {"path"}
    description = DataTableBundleProcessorDescription(
        undeclared_tables=False,
        data_tables=[{"name": "t", "output": {"columns": [{"name": "value"}]}}],
    )
    assert get_path_headers(description, "t") == {"path"}


def test_undeclared_tables(tdt_manager, tmp_path):
    options = BundleProcessingOptions(
        what="data manager 'mock'",
        data_manager_path=str(tmp_path),
        target_config_file=str(tmp_path / "sample_data_managers_conf.xml"),
    )
    target_path = tmp_path / "newvalue.txt"
    target_path.write_text("Moo Cow")
    output = {"data_tables": {"testalpha": [{"value": "newvalue", "name": "mynewname", "path": "newvalue.txt"}]}}
    output_dataset_path = tmp_path / "output.dat"

    output_dataset_path.write_text(json.dumps(output))
    extra_files_path = tmp_path / "extra"
    output_dataset = OutputDataset(
        output_dataset_path,
        extra_files_path,
    )
    out_data = {"out1": output_dataset}
    process_description = DataTableBundleProcessorDescription(
        **{
            "undeclared_tables": True,
            "data_tables": [],
        }
    )
    repo_info = None
    tdt_manager.process_bundle(
        out_data,
        process_description,
        repo_info,
        options,
    )
    loc1 = tmp_path / "testalpha.loc"
    new_row = _last_row(loc1)
    assert new_row[0] == "newvalue"
    assert new_row[1] == "mynewname"
    assert new_row[2] == str(tmp_path / "newvalue.txt")


def prepare_motus_style_output_and_description(tmp_path):
    """Mirror mOTUs: a ``<move>`` into ``motus_database/${value}/db_mOTU`` whose base
    (``${GALAXY_DATA_MANAGER_DATA_PATH}``) is only known at import, plus a
    ``value_translation`` to that same relative layout (no ``${path}`` suffix)."""
    value = "3.1.0"
    raw_dir_name = "db_from_dm"
    extra_files_path = tmp_path / "extra"
    staged = extra_files_path / raw_dir_name
    staged.mkdir(parents=True)
    (staged / "db_mOTU_versions").write_text("VERSIONS")
    (staged / "db_mOTU_DB_CEN.fasta").write_text("FASTA")

    output = {"data_tables": {"testalpha": [{"value": value, "name": "mOTUs 3.1.0", "path": raw_dir_name}]}}
    output_dataset_path = tmp_path / "output.dat"
    output_dataset_path.write_text(json.dumps(output))
    output_dataset = OutputDataset(output_dataset_path, extra_files_path)
    out_data = {"out1": output_dataset}
    data_table = {
        "name": "testalpha",
        "output": {
            "columns": [
                {"name": "value"},
                {"name": "name"},
                {
                    "name": "path",
                    "output_ref": "out1",
                    "moves": [
                        {
                            "type": "directory",
                            "relativize_symlinks": False,
                            "source_value": "${path}",
                            "target_value": "motus_database/${value}/db_mOTU",
                            "target_base": "${GALAXY_DATA_MANAGER_DATA_PATH}",
                        }
                    ],
                    "value_translations": [
                        {
                            "value": "${GALAXY_DATA_MANAGER_DATA_PATH}/motus_database/${value}/db_mOTU",
                            "type": "template",
                        },
                        {"value": "abspath", "type": "function"},
                    ],
                },
            ]
        },
    }
    process_description = DataTableBundleProcessorDescription(
        **{"undeclared_tables": False, "data_tables": [data_table]}
    )
    return value, raw_dir_name, extra_files_path, out_data, process_description


def test_write_bundle_stages_move_layout(tdt_manager, tmp_path):
    """write_bundle physically restructures the extra_files into the move's relative
    layout, records that path, and leaves no copy of the raw dir behind."""
    value, raw_dir_name, extra_files_path, out_data, process_description = prepare_motus_style_output_and_description(
        tmp_path
    )
    tdt_manager.write_bundle(out_data, process_description, None)

    moved_dir = extra_files_path / "motus_database" / value / "db_mOTU"
    assert (moved_dir / "db_mOTU_versions").exists()
    assert (moved_dir / "db_mOTU_DB_CEN.fasta").exists()
    # The raw dir was moved, not copied.
    assert not (extra_files_path / raw_dir_name).exists()

    bundle_index = json.loads((extra_files_path / BUNDLE_INDEX_FILE_NAME).read_text())
    recorded_path = bundle_index["data_tables"]["testalpha"][0]["path"]
    assert recorded_path == os.path.join("motus_database", value, "db_mOTU")


def test_consume_join_lands_in_moved_layout(tdt_manager, tmp_path):
    """A downstream (chained) tool resolves the recorded path with a naive join and
    lands exactly on the moved db_mOTU dir with its files."""
    value, _raw, extra_files_path, out_data, process_description = prepare_motus_style_output_and_description(tmp_path)
    tdt_manager.write_bundle(out_data, process_description, None)

    bundle_index = json.loads((extra_files_path / BUNDLE_INDEX_FILE_NAME).read_text())
    recorded_path = bundle_index["data_tables"]["testalpha"][0]["path"]

    consumed = os.path.join(str(extra_files_path), recorded_path)
    assert os.path.isdir(consumed)
    assert os.path.exists(os.path.join(consumed, "db_mOTU_versions"))


def test_move_layout_round_trips_through_import(tdt_manager, tmp_path):
    """Importing the write-time-staged bundle yields the SAME final install layout
    (a single move to GALAXY_DATA_MANAGER_DATA_PATH) and the same translated .loc value."""
    value, _raw, extra_files_path, out_data, process_description = prepare_motus_style_output_and_description(tmp_path)
    tdt_manager.write_bundle(out_data, process_description, None)

    # Transport the bundle to another host: the write location is gone by import.
    transported = tmp_path / "imported"
    os.rename(extra_files_path, transported)

    install_root = tmp_path / "install"
    install_root.mkdir()
    options = BundleProcessingOptions(
        what="data manager 'mock'",
        data_manager_path=str(install_root),
        target_config_file=str(tmp_path / "sample_data_managers_conf.xml"),
    )
    tdt_manager.import_bundle(str(transported), options)

    expected_dir = install_root / "motus_database" / value / "db_mOTU"
    assert (expected_dir / "db_mOTU_versions").exists()
    assert (expected_dir / "db_mOTU_DB_CEN.fasta").exists()

    new_row = _last_row(tmp_path / "testalpha.loc")
    assert new_row[0] == value
    assert new_row[-1] == str(expected_dir)


def test_write_bundle_leaves_move_less_table_untouched(tdt_manager, tmp_path):
    """A table/column without a ``<move>`` keeps the naive relative path and layout."""
    target_path = tmp_path / "extra" / "newvalue.txt"
    target_path.parent.mkdir()
    target_path.write_text("Moo Cow")
    output = {"data_tables": {"testalpha": [{"value": "newvalue", "name": "mynewname", "path": "newvalue.txt"}]}}
    output_dataset_path = tmp_path / "output.dat"
    output_dataset_path.write_text(json.dumps(output))
    output_dataset = OutputDataset(output_dataset_path, tmp_path / "extra")
    out_data = {"out1": output_dataset}
    data_table = {
        "name": "testalpha",
        "output": {"columns": [{"name": "value"}, {"name": "name"}, {"name": "path"}]},
    }
    process_description = DataTableBundleProcessorDescription(
        **{"undeclared_tables": False, "data_tables": [data_table]}
    )
    tdt_manager.write_bundle(out_data, process_description, None)

    # Layout and recorded path unchanged: file still at its original relative location.
    assert (tmp_path / "extra" / "newvalue.txt").exists()
    bundle_index = json.loads((tmp_path / "extra" / BUNDLE_INDEX_FILE_NAME).read_text())
    assert bundle_index["data_tables"]["testalpha"][0]["path"] == "newvalue.txt"


def _last_row(loc_file):
    with open(loc_file) as file:
        rows = csv.reader(file, delimiter="\t")
        for row in rows:
            last_row = row
        return last_row
