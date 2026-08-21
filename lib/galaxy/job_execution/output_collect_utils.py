"""Model-free helpers used while collecting job outputs."""

import logging
import operator
import os
import re
from tempfile import NamedTemporaryFile
from typing import (
    Any,
    NamedTuple,
    Protocol,
    TYPE_CHECKING,
)

from galaxy.objectstore import (
    ObjectStore,
    persist_extra_files,
)
from galaxy.tool_util.parser.output_collection_def import (
    DEFAULT_DATASET_COLLECTOR_DESCRIPTION,
    ToolProvidedMetadataDatasetCollection,
)
from galaxy.util import (
    in_directory,
    shrink_and_unicodify,
    unicodify,
)

if TYPE_CHECKING:
    from galaxy.model import DatasetInstance

log = logging.getLogger(__name__)

DATASET_ID_TOKEN = "DATASET_ID"


class MaxDiscoveredFilesExceededError(ValueError):
    pass


class DiscoveryContext(Protocol):
    job_working_directory: str

    def increment_discovered_file_count(self): ...


class DiscoveredFile(NamedTuple):
    path: str
    collector: Any | None
    match: "JsonCollectedDatasetMatch"

    def discovered_state(self, element: dict[str, Any], final_job_state="ok") -> "DiscoveredResultState":
        return DiscoveredResultState(element.get("info"), final_job_state)


class DiscoveredResultState(NamedTuple):
    info: str | None
    state: str


class DiscoveredDeferredFile(NamedTuple):
    collector: Any | None
    match: "JsonCollectedDatasetMatch"

    def discovered_state(self, element: dict[str, Any], final_job_state="ok") -> DiscoveredResultState:
        state = "deferred" if final_job_state == "ok" else final_job_state
        return DiscoveredResultState(element.get("info"), state)

    @property
    def path(self):
        return None


class DiscoveredFileError(NamedTuple):
    error_message: str
    collector: Any | None
    match: "JsonCollectedDatasetMatch"
    path: str | None = None

    def discovered_state(self, element: dict[str, Any], final_job_state="ok") -> DiscoveredResultState:
        return DiscoveredResultState(self.error_message, "error")


DiscoveredResult = DiscoveredFile | DiscoveredDeferredFile | DiscoveredFileError


class JsonCollectedDatasetMatch:
    def __init__(self, as_dict, collector, filename, path=None, parent_identifiers=None):
        self.as_dict = as_dict
        self.collector = collector
        self.filename = filename
        self.path = path
        self._parent_identifiers = parent_identifiers or []

    @property
    def designation(self):
        if element_identifiers := self.raw_element_identifiers:
            return ":".join(element_identifiers)
        if "designation" in self.as_dict:
            return self.as_dict.get("designation")
        if "name" in self.as_dict:
            return self.as_dict.get("name")
        return None

    @property
    def element_identifiers(self):
        return self._parent_identifiers + (self.raw_element_identifiers or [self.designation])

    @property
    def raw_element_identifiers(self):
        identifiers = []
        index = 0
        while (key := f"identifier_{index}") in self.as_dict:
            identifiers.append(self.as_dict.get(key))
            index += 1
        return identifiers

    @property
    def name(self):
        return self.as_dict.get("name")

    @property
    def dbkey(self) -> str:
        return self.as_dict.get("dbkey", self.collector and self.collector.default_dbkey or "?")

    @property
    def ext(self) -> str:
        return self.as_dict.get("ext", self.collector and self.collector.default_ext or "data")

    @property
    def visible(self) -> bool:
        try:
            return self.as_dict["visible"].lower() == "visible"
        except KeyError:
            if self.collector and self.collector.default_visible is not None:
                return self.collector.default_visible
            return True

    @property
    def link_data(self):
        return bool(self.as_dict.get("link_data_only", False))

    @property
    def tag_list(self):
        return self.as_dict.get("tags", [])

    @property
    def object_id(self):
        return self.as_dict.get("object_id")

    @property
    def sources(self):
        return self.as_dict.get("sources", [])

    @property
    def hashes(self):
        return self.as_dict.get("hashes", [])

    @property
    def created_from_basename(self):
        return self.as_dict.get("created_from_basename")

    @property
    def extra_files(self):
        return self.as_dict.get("extra_files")

    @property
    def effective_state(self):
        return self.as_dict.get("state") or "ok"

    @property
    def row(self):
        return self.as_dict.get("row") or None


class RegexCollectedDatasetMatch(JsonCollectedDatasetMatch):
    def __init__(self, re_match, collector, filename, path=None):
        super().__init__(re_match.groupdict(), collector, filename, path=path)


def discover_target_directory(dir_name, job_working_directory):
    if not dir_name:
        return job_working_directory
    directory = os.path.join(job_working_directory, dir_name)
    if not in_directory(directory, job_working_directory):
        raise Exception(
            "Problem with tool configuration, attempting to pull in datasets from outside working directory."
        )
    return directory


def discovered_file_for_element(dataset, context: DiscoveryContext, parent_identifiers=None, collector=None):
    context.increment_discovered_file_count()
    parent_identifiers = parent_identifiers or []
    target_directory = discover_target_directory(getattr(collector, "directory", None), context.job_working_directory)
    filename = dataset.get("filename")
    error_message = dataset.get("error_message")
    if error_message is not None:
        return DiscoveredFileError(
            error_message,
            collector,
            JsonCollectedDatasetMatch(dataset, collector, None, parent_identifiers=parent_identifiers),
        )
    if dataset.get("state") == "deferred":
        return DiscoveredDeferredFile(
            collector,
            JsonCollectedDatasetMatch(dataset, collector, None, parent_identifiers=parent_identifiers),
        )
    if not dataset.get("link_data_only"):
        path = os.path.join(target_directory, filename)
        if not in_directory(path, target_directory):
            raise Exception(
                "Problem with tool configuration, attempting to pull in datasets from outside working directory."
            )
    else:
        path = filename
    return DiscoveredFile(
        path,
        collector,
        JsonCollectedDatasetMatch(dataset, collector, filename, path=path, parent_identifiers=parent_identifiers),
    )


class ToolMetadataDatasetCollector:
    def __init__(self, description):
        self.discover_via = description.discover_via
        self.default_dbkey = description.default_dbkey
        self.default_ext = description.default_ext
        self.default_visible = description.default_visible
        self.directory = description.directory
        self.assign_primary_output = description.assign_primary_output


class DatasetCollector:
    def __init__(self, description):
        self.discover_via = description.discover_via
        self.sort_key = description.sort_key
        self.sort_reverse = description.sort_reverse
        self.sort_comp = description.sort_comp
        self.pattern = description.pattern
        self.default_dbkey = description.default_dbkey
        self.default_ext = description.default_ext
        self.default_visible = description.default_visible
        self.directory = description.directory
        self.assign_primary_output = description.assign_primary_output
        self.recurse = description.recurse
        self.match_relative_path = description.match_relative_path

    def _pattern_for_dataset(self, dataset_instance=None):
        token_replacement = str(dataset_instance.id) if dataset_instance else r"\d+"
        return self.pattern.replace(DATASET_ID_TOKEN, token_replacement)

    def match(self, dataset_instance, filename, path=None, parent_paths=None):
        pattern = self._pattern_for_dataset(dataset_instance)
        if self.match_relative_path and parent_paths:
            filename = os.path.join(*parent_paths, filename)
        if re_match := re.match(pattern, filename):
            return RegexCollectedDatasetMatch(re_match, self, filename, path=path)
        return None

    def sort(self, matches):
        assert self.sort_key in ["filename", "dbkey", "name", "designation"]
        assert self.sort_comp in ["lexical", "numeric"]
        key = operator.attrgetter(self.sort_key)
        if self.sort_comp == "numeric":
            lexical_key = key

            def key(value):
                return int(lexical_key(value))

        return sorted(matches, key=key, reverse=self.sort_reverse)


def dataset_collector(description):
    if description is DEFAULT_DATASET_COLLECTOR_DESCRIPTION:
        return DEFAULT_DATASET_COLLECTOR
    if description.discover_via == "pattern":
        return DatasetCollector(description)
    return ToolMetadataDatasetCollector(description)


def discover_files(output_name, tool_provided_metadata, collectors, job_working_directory, matchable):
    if collectors and collectors[0].discover_via == "tool_provided_metadata":
        assert len(collectors) == 1
        collector = collectors[0]
        target_directory = discover_target_directory(collector.directory, job_working_directory)
        for dataset in tool_provided_metadata.get_new_datasets(output_name):
            filename = dataset["filename"]
            path = os.path.join(target_directory, filename)
            yield DiscoveredFile(path, collector, JsonCollectedDatasetMatch(dataset, collector, filename, path=path))
    else:
        for match, collector in walk_over_file_collectors(collectors, job_working_directory, matchable):
            yield DiscoveredFile(match.path, collector, match)


def walk_over_file_collectors(collectors, job_working_directory, matchable):
    for collector in collectors:
        assert collector.discover_via == "pattern"
        for match in walk_over_extra_files(collector.directory, collector, job_working_directory, matchable):
            yield match, collector


def walk_over_extra_files(target_dir, collector, job_working_directory, matchable, parent_paths=None):
    parent_paths = parent_paths or []

    def walk(current_target, current_working_directory, current_parent_paths):
        directory = discover_target_directory(current_target, current_working_directory)
        if os.path.isdir(directory):
            for filename in os.listdir(directory):
                path = os.path.join(directory, filename)
                if os.path.isdir(path):
                    if collector.recurse:
                        yield from walk(filename, directory, [*current_parent_paths, filename])
                elif match := collector.match(matchable, filename, path=path, parent_paths=current_parent_paths):
                    yield match

    yield from collector.sort(walk(target_dir, job_working_directory, parent_paths))


DEFAULT_DATASET_COLLECTOR = DatasetCollector(DEFAULT_DATASET_COLLECTOR_DESCRIPTION)
DEFAULT_TOOL_PROVIDED_DATASET_COLLECTOR = ToolMetadataDatasetCollector(ToolProvidedMetadataDatasetCollection())


def read_exit_code_from(exit_code_file, id_tag):
    """Read exit code reported for a Galaxy job."""
    try:
        # This should be an 8-bit exit code, but read ahead anyway:
        exit_code_str = open(exit_code_file).read(32)
    except Exception:
        # By default, the exit code is 0, which typically indicates success.
        exit_code_str = "0"

    try:
        # Decode the exit code. If it's bogus, then just use 0.
        exit_code = int(exit_code_str)
    except ValueError:
        galaxy_id_tag = id_tag
        log.warning(f"({galaxy_id_tag}) Exit code '{exit_code_str}' invalid. Using 0.")
        exit_code = 0

    return exit_code


def default_exit_code_file(files_dir, id_tag):
    return os.path.join(files_dir, f"galaxy_{id_tag}.ec")


def collect_extra_files(
    object_store: ObjectStore,
    dataset: "DatasetInstance",
    job_working_directory: str,
    outputs_to_working_directory: bool = False,
):
    # TODO: should this use compute_environment to determine the extra files path ?
    assert dataset.dataset
    real_file_name = file_name = dataset.dataset.extra_files_path_name_from(object_store)
    if outputs_to_working_directory:
        # OutputsToWorkingDirectoryPathRewriter always rewrites extra files to uuid path,
        # so we have to collect from that path even if the real extra files path is dataset_N_files
        file_name = f"dataset_{dataset.dataset.uuid}_files"
    output_location = "outputs"
    temp_file_path = os.path.join(job_working_directory, output_location, file_name)
    if not os.path.exists(temp_file_path):
        # Fall back to working dir, remove in 23.2
        output_location = "working"
        temp_file_path = os.path.join(job_working_directory, output_location, file_name)
    if not os.path.exists(temp_file_path):
        # no outputs to working directory, but may still need to push form cache to backend
        temp_file_path = dataset.extra_files_path
    try:
        # This skips creation of directories - object store automatically creates them.
        # However, empty directories will not be created in the object store at all.
        persist_extra_files(
            object_store=object_store,
            src_extra_files_path=temp_file_path,
            primary_data=dataset,
            extra_files_path_name=real_file_name,
        )
    except Exception as e:
        log.debug("Error in collect_associated_files: %s", unicodify(e))

    # Handle composite datatypes of auto_primary_file type
    if dataset.datatype.composite_type == "auto_primary_file" and not dataset.has_data():
        try:
            with NamedTemporaryFile(mode="w") as temp_fh:
                temp_fh.write(dataset.datatype.generate_primary_file(dataset))
                temp_fh.flush()
                object_store.update_from_file(dataset.dataset, file_name=temp_fh.name, create=True)
                dataset.set_size()
        except Exception as e:
            log.warning(
                "Unable to generate primary composite file automatically for %s: %s", dataset.dataset.id, unicodify(e)
            )


def collect_shrinked_content_from_path(path):
    try:
        with open(path, "rb") as fh:
            return shrink_and_unicodify(fh.read().strip())
    except FileNotFoundError:
        return None
