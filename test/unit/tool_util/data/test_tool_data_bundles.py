import csv
import json
import os
from dataclasses import dataclass

import pytest

from galaxy.tool_util.data import (
    _copy_merge,
    _process_move,
    BUNDLE_INDEX_FILE_NAME,
    BundleProcessingOptions,
    resolve_consumed_bundle_column,
)
from galaxy.tool_util.data.bundles.models import (
    convert_data_tables_xml,
    DataTableBundle,
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

    # Write stored the absolute job path relative to the extra-files dir.
    bundle_index = json.loads((tmp_path / "extra" / BUNDLE_INDEX_FILE_NAME).read_text())
    stored_path = bundle_index["data_tables"][table_name][0][path_column]
    assert stored_path == index
    assert not os.path.isabs(stored_path)

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


def _motus_column(*, with_move: bool) -> dict:
    column: dict = {"name": "path", "data_table_name": "path", "output_ref": "out1"}
    if with_move:
        column["moves"] = [
            {
                "type": "directory",
                "relativize_symlinks": False,
                "source_value": "${path}",
                "target_base": "${GALAXY_DATA_MANAGER_DATA_PATH}",
                "target_value": "motus_database/${value}/db_mOTU",
            }
        ]
        column["value_translations"] = [
            {"value": "${GALAXY_DATA_MANAGER_DATA_PATH}/motus_database/${value}/db_mOTU", "type": "template"}
        ]
    return column


def _write_consumed_bundle(tmp_path, *, with_move: bool):
    """Build a bundle HDA extra-files dir with a raw db dir and a bundle index.

    Mirrors the mOTUs data manager: a ``<move>`` relocates the raw ``db_mOTU``
    directory to ``${GALAXY_DATA_MANAGER_DATA_PATH}/motus_database/${value}/db_mOTU``
    and a value translation resolves the column to that path. ``with_move=False``
    models a plain ``path`` table (e.g. metaphlan/samestr) with no move.
    """
    extra_files_path = tmp_path / "extra"
    db_dir = extra_files_path / "db_mOTU"
    db_dir.mkdir(parents=True)
    (db_dir / "db_mOTU_versions").write_text("3.1.0")

    description = DataTableBundleProcessorDescription(
        undeclared_tables=False,
        data_tables=[
            {
                "name": "motus_db",
                "output": {"columns": [{"name": "value"}, {"name": "name"}, _motus_column(with_move=with_move)]},
            }
        ],
    )
    bundle = DataTableBundle(
        processor_description=description,
        data_tables={"motus_db": [{"value": "3.1.0", "name": "mOTUs 3.1.0", "path": "db_mOTU"}]},
        output_name="out1",
    )
    (extra_files_path / BUNDLE_INDEX_FILE_NAME).write_text(bundle.model_dump_json())
    return extra_files_path, db_dir


def test_resolve_consumed_bundle_column_applies_move(tmp_path):
    """Consuming a bundle applies the DM move so the downstream tool sees the install layout."""
    extra_files_path, db_dir = _write_consumed_bundle(tmp_path, with_move=True)
    staging_root = tmp_path / "staging"
    staging_root.mkdir()

    resolved = resolve_consumed_bundle_column(str(extra_files_path), "motus_db", "path", str(staging_root))

    expected = staging_root / "motus_database" / "3.1.0" / "db_mOTU"
    # (i) files were materialized under the staging root and (ii) the returned path points there.
    assert (expected / "db_mOTU_versions").exists()
    assert resolved == str(expected)
    # (iii) the source bundle extra-files dir is untouched (import reuses it).
    assert (db_dir / "db_mOTU_versions").exists()

    # (iv) a second call is idempotent and returns the same path.
    resolved_again = resolve_consumed_bundle_column(str(extra_files_path), "motus_db", "path", str(staging_root))
    assert resolved_again == str(expected)
    assert (expected / "db_mOTU_versions").exists()
    assert (db_dir / "db_mOTU_versions").exists()


def test_resolve_consumed_bundle_column_without_move_is_naive_join(tmp_path):
    """A move-less path table resolves to the same joined path as before (metaphlan/samestr)."""
    extra_files_path, _ = _write_consumed_bundle(tmp_path, with_move=False)
    staging_root = tmp_path / "staging"
    staging_root.mkdir()

    resolved = resolve_consumed_bundle_column(str(extra_files_path), "motus_db", "path", str(staging_root))

    assert resolved == os.path.join(str(extra_files_path), "db_mOTU")
    # Nothing is staged for a move-less column.
    assert not (staging_root / "motus_database").exists()


def _single_move_description() -> DataTableBundleProcessorDescription:
    return DataTableBundleProcessorDescription(
        undeclared_tables=False,
        data_tables=[
            {
                "name": "motus_db",
                "output": {
                    "columns": [
                        {"name": "value"},
                        {
                            "name": "path",
                            "data_table_name": "path",
                            "output_ref": "out1",
                            "moves": [
                                {
                                    "type": "directory",
                                    "relativize_symlinks": False,
                                    "source_value": "${path}",
                                    "target_base": "${GALAXY_DATA_MANAGER_DATA_PATH}",
                                    "target_value": "motus_database/${value}/db_mOTU",
                                }
                            ],
                        },
                    ]
                },
            }
        ],
    )


def test_process_move_default_transfer_is_destructive(tmp_path):
    """The default transfer still moves (empties the source), as the import path relies on."""
    source_root = tmp_path / "src"
    (source_root / "db_mOTU").mkdir(parents=True)
    (source_root / "db_mOTU" / "file").write_text("data")
    options = BundleProcessingOptions(
        what="data manager 'mock'", data_manager_path=str(tmp_path / "dm"), target_config_file=""
    )

    _process_move(
        "motus_db",
        "path",
        source_base_path=str(source_root),
        bundle_description=_single_move_description(),
        options=options,
        value="3.1.0",
        path="db_mOTU",
    )

    moved_target = tmp_path / "dm" / "motus_database" / "3.1.0" / "db_mOTU"
    assert (moved_target / "file").exists()
    # Default transfer is util.move_merge, which removes the moved source.
    assert not (source_root / "db_mOTU").exists()


def test_process_move_copy_transfer_leaves_source_intact(tmp_path):
    """A copy transfer materializes the target without emptying the source."""
    source_root = tmp_path / "src"
    (source_root / "db_mOTU").mkdir(parents=True)
    (source_root / "db_mOTU" / "file").write_text("data")
    options = BundleProcessingOptions(
        what="data manager 'mock'", data_manager_path=str(tmp_path / "dm"), target_config_file=""
    )

    _process_move(
        "motus_db",
        "path",
        source_base_path=str(source_root),
        bundle_description=_single_move_description(),
        options=options,
        transfer=_copy_merge,
        value="3.1.0",
        path="db_mOTU",
    )

    copied_target = tmp_path / "dm" / "motus_database" / "3.1.0" / "db_mOTU"
    assert (copied_target / "file").exists()
    # Copy transfer must not empty the source.
    assert (source_root / "db_mOTU" / "file").exists()


def test_copy_merge_is_idempotent_and_non_destructive(tmp_path):
    source = tmp_path / "src"
    source.mkdir()
    (source / "file").write_text("data")
    target = tmp_path / "dst"

    _copy_merge(str(source), str(target))
    _copy_merge(str(source), str(target))  # second call must not raise

    assert (target / "file").read_text() == "data"
    assert (source / "file").exists()


def _last_row(loc_file):
    with open(loc_file) as file:
        rows = csv.reader(file, delimiter="\t")
        for row in rows:
            last_row = row
        return last_row
