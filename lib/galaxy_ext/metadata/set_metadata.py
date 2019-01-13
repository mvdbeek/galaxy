"""
Execute an external process to set_meta() on a provided list of pickled datasets.

This was formerly scripts/set_metadata.py and expects these arguments:

    %prog datatypes_conf.xml job_metadata_file metadata_in,metadata_kwds,metadata_out,metadata_results_code,output_filename_override,metadata_override... max_metadata_value_size

Galaxy should be importable on sys.path and output_filename_override should be
set to the path of the dataset on which metadata is being set
(output_filename_override could previously be left empty and the path would be
constructed automatically).
"""
import json
import logging
import os
import sys

# insert *this* galaxy before all others on sys.path
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)))

from six.moves import cPickle

from galaxy.datatypes import sniff
from galaxy.datatypes.registry import Registry
from galaxy.metadata.parameters import MetadataCollection, MetadataTempFile
from galaxy.util import stringify_dictionary_keys, total_size

# ensure supported version
assert sys.version_info[:2] >= (2, 7), 'Python version must be at least 2.7, this is: %s' % sys.version

logging.basicConfig()
log = logging.getLogger(__name__)


def set_meta_with_tool_provided(dataset_instance, file_dict, set_meta_kwds, datatypes_registry, max_metadata_value_size):
    # This method is somewhat odd, in that we set the metadata attributes from tool,
    # then call set_meta, then set metadata attributes from tool again.
    # This is intentional due to interplay of overwrite kwd, the fact that some metadata
    # parameters may rely on the values of others, and that we are accepting the
    # values provided by the tool as Truth.
    extension = dataset_instance.extension
    if extension == "_sniff_":
        try:
            extension = sniff.handle_uploaded_dataset_file(dataset_instance.dataset.external_filename, datatypes_registry)
            # We need to both set the extension so it is available to set_meta
            # and record it in the metadata so it can be reloaded on the server
            # side and the model updated (see MetadataCollection.{from,to}_JSON_dict)
            dataset_instance.extension = extension
            # Set special metadata property that will reload this on server side.
            setattr(dataset_instance.metadata, "__extension__", extension)
        except Exception:
            # TODO: log this when metadata can log stuff...
            # https://trello.com/c/Nrwodu9d
            pass

    for metadata_name, metadata_value in file_dict.get('metadata', {}).items():
        setattr(dataset_instance.metadata, metadata_name, metadata_value)
    dataset_instance.datatype.set_meta(dataset_instance, **set_meta_kwds)
    for metadata_name, metadata_value in file_dict.get('metadata', {}).items():
        setattr(dataset_instance.metadata, metadata_name, metadata_value)

    if max_metadata_value_size:
        for k, v in list(dataset_instance.metadata.items()):
            if total_size(v) > max_metadata_value_size:
                log.info("Key %s too large for metadata, discarding" % k)
                dataset_instance.metadata.remove_key(k)


class MiniHDA(object):
    """Provides a stripped down HDA for metadata setting"""

    def __init__(self, id, file_name, extension, dataset, registry, galaxy_version=None, **kwds):
        self.id = id
        self.file_name = file_name
        self.external_filename = file_name
        self.extension = extension
        self.dataset = dataset
        self.galaxy_version = galaxy_version
        self._size = None
        self._metadata = None
        self.metadata = MetadataCollection(self)
        self.registry = registry

    @property
    def datatype(self):
        extension = self.extension
        if extension == 'auto' or extension == '_sniff_' or not extension:
            extension = 'data'
        return self.registry.get_datatype_by_extension(extension)

    @property
    def ext(self):
        return self.extension

    @property
    def extra_files_path(self):
        return self.dataset.extra_files_path

    def has_data(self):
        if self._size is None:
            self._size = os.path.getsize(self.external_filename)
        return self._size > 0

    @staticmethod
    def from_json(json_path, registry):
        with open(json_path) as json_source:
            dataset_dict = json.load(json_source)
        dataset_dict['dataset'] = MiniDataset(id=dataset_dict['dataset']['id'],
                                              external_filename=dataset_dict['file_name'],
                                              )
        dataset_dict['registry'] = registry
        mini_hda = MiniHDA(**dataset_dict)
        mini_hda.metadata.from_JSON_dict(json_dict=dataset_dict['metadata'])
        return mini_hda


class MiniDataset(object):

    def __init__(self, id, external_filename=None, external_extra_files_path=None):
        self.id = id
        self.external_filename = external_filename
        self.external_extra_files_path = external_extra_files_path
        self.state = 'OK'

    @property
    def extra_files_path(self):
        return self.external_extra_files_path


def set_metadata():
    # locate galaxy_root for loading datatypes
    galaxy_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir, os.pardir))
    MetadataTempFile.tmp_dir = tool_job_working_directory = os.path.abspath(os.getcwd())

    # This is ugly, but to transition from existing jobs without this parameter
    # to ones with, smoothly, it has to be the last optional parameter and we
    # have to sniff it.
    try:
        max_metadata_value_size = int(sys.argv[-1])
        sys.argv = sys.argv[:-1]
    except ValueError:
        max_metadata_value_size = 0
        # max_metadata_value_size is unspecified and should be 0

    # Set up datatypes registry
    datatypes_config = sys.argv.pop(1)
    if not os.path.exists(datatypes_config):
        print("Metadata setting failed because registry.xml could not be found. You may retry setting metadata.")
        sys.exit(1)
    datatypes_registry = Registry()
    datatypes_registry.load_datatypes(root_dir=galaxy_root, config=datatypes_config)

    job_metadata = sys.argv.pop(1)
    existing_job_metadata_dict = {}
    new_job_metadata_dict = {}
    if job_metadata != "None" and os.path.exists(job_metadata):
        for line in open(job_metadata, 'r'):
            try:
                line = stringify_dictionary_keys(json.loads(line))
                if line['type'] == 'dataset':
                    existing_job_metadata_dict[int(line['dataset_id'])] = line
                elif line['type'] == 'new_primary_dataset':
                    new_job_metadata_dict[line['filename']] = line
            except Exception:
                continue

    for filenames in sys.argv[1:]:
        fields = filenames.split(',')
        filename_in = fields.pop(0)
        filename_kwds = fields.pop(0)
        filename_out = fields.pop(0)
        filename_results_code = fields.pop(0)
        dataset_filename_override = fields.pop(0)
        override_metadata = fields.pop(0)
        set_meta_kwds = stringify_dictionary_keys(json.load(open(filename_kwds)))  # load kwds; need to ensure our keywords are not unicode
        try:
            try:
                # pick up serialized dataset
                dataset = MiniHDA.from_json(filename_in, registry=datatypes_registry)
            except Exception:
                # old jobs, remove this in 20.XX
                dataset = cPickle.load(open(filename_in, 'rb'))  # load DatasetInstance
            dataset.dataset.external_filename = dataset_filename_override
            files_path = os.path.abspath(os.path.join(tool_job_working_directory, "dataset_%s_files" % (dataset.dataset.id)))
            dataset.dataset.external_extra_files_path = files_path
            file_dict = existing_job_metadata_dict.get(dataset.dataset.id, {})
            if 'ext' in file_dict:
                dataset.extension = file_dict['ext']
            # Metadata FileParameter types may not be writable on a cluster node, and are therefore temporarily substituted with MetadataTempFiles
            override_metadata = json.load(open(override_metadata))
            for metadata_name, metadata_file_override in override_metadata:
                if MetadataTempFile.is_JSONified_value(metadata_file_override):
                    metadata_file_override = MetadataTempFile.from_JSON(metadata_file_override)
                setattr(dataset.metadata, metadata_name, metadata_file_override)
            set_meta_with_tool_provided(dataset, file_dict, set_meta_kwds, datatypes_registry, max_metadata_value_size)
            dataset.metadata.to_JSON_dict(filename_out)  # write out results of set_meta
            json.dump((True, 'Metadata has been set successfully'), open(filename_results_code, 'wt+'))  # setting metadata has succeeded
        except Exception as e:
            json.dump((False, str(e)), open(filename_results_code, 'wt+'))  # setting metadata has failed somehow

    for i, (filename, file_dict) in enumerate(new_job_metadata_dict.items(), start=1):
        new_dataset_filename = os.path.join(tool_job_working_directory, "working", file_dict['filename'])
        new_dataset = MiniDataset(id=-i, external_filename=new_dataset_filename)
        extra_files = file_dict.get('extra_files', None)
        if extra_files is not None:
            new_dataset._extra_files_path = os.path.join(tool_job_working_directory, "working", extra_files)
        new_dataset_instance = MiniHDA(id=-i, file_name=new_dataset_filename, dataset=new_dataset, extension=file_dict.get('ext', 'data'), registry=datatypes_registry)
        set_meta_with_tool_provided(new_dataset_instance, file_dict, set_meta_kwds, datatypes_registry, max_metadata_value_size)
        file_dict['metadata'] = json.loads(new_dataset_instance.metadata.to_JSON_dict())  # storing metadata in external form, need to turn back into dict, then later jsonify
    if existing_job_metadata_dict or new_job_metadata_dict:
        with open(job_metadata, 'wt') as job_metadata_fh:
            for value in list(existing_job_metadata_dict.values()) + list(new_job_metadata_dict.values()):
                job_metadata_fh.write("%s\n" % (json.dumps(value)))
