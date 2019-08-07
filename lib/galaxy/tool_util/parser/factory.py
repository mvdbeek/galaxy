"""Constructors for concrete tool and input source objects."""
from __future__ import absolute_import

import logging
import os
from xml.etree import ElementTree

import yaml

from galaxy.tool_util.loader import (
    load_tool_with_refereces,
    raw_xml_tree,
)
from galaxy.util.hash_util import md5_hash_file
from galaxy.util.odict import odict
from .cwl import CwlToolSource
from .interface import InputSource
from .xml import XmlInputSource, XmlToolSource
from .yaml import YamlToolSource
from ..fetcher import ToolLocationFetcher

log = logging.getLogger(__name__)


def get_tool_source(config_file=None, xml_tree=None, enable_beta_formats=True, tool_location_fetcher=None):
    """Return a ToolSource object corresponding to supplied source.

    The supplied source may be specified as a file path (using the config_file
    parameter) or as an XML object loaded with load_tool_with_refereces.
    """
    if xml_tree is not None:
        return XmlToolSource(xml_tree, source_path=config_file)
    elif config_file is None:
        raise ValueError("get_tool_source called with invalid config_file None.")

    if tool_location_fetcher is None:
        tool_location_fetcher = ToolLocationFetcher()

    config_file = tool_location_fetcher.to_tool_path(config_file)
    if enable_beta_formats:
        if config_file.endswith(".yml"):
            log.info("Loading tool from YAML - this is experimental - tool will not function in future.")
            with open(config_file, "r") as f:
                as_dict = ordered_load(f)
                return YamlToolSource(as_dict, source_path=config_file)
        elif config_file.endswith(".json") or config_file.endswith(".cwl"):
            log.info("Loading CWL tool - this is experimental - tool likely will not function in future at least in same way.")
            return CwlToolSource(config_file)

    expanded_config_file = "%s.full.xml" % config_file

    if os.path.exists(expanded_config_file):
        config_file = expanded_config_file
        tree = raw_xml_tree(expanded_config_file)
        macro_element = tree.find('macro_import_paths')
        macro_paths = []
        if macro_element:
            macro_paths = [os.path.abspath(os.path.join(os.path.dirname(config_file), e.text)) for e in macro_element.getchildren()]
    else:
        tree, macro_paths = load_tool_with_refereces(config_file)
        record_macro_in_tree(tree, macro_paths, os.path.dirname(config_file))
    if config_file != expanded_config_file:
        tree.write(expanded_config_file)
    return XmlToolSource(tree, source_path=config_file, macro_paths=macro_paths)


def record_macro_in_tree(tree, macro_paths, xml_base_dir):
    if macro_paths:
        mip = ElementTree.SubElement(tree.getroot(), 'macro_import_paths')
        for macro_path in macro_paths:
            rel_macro_path = os.path.relpath(macro_path, xml_base_dir)
            path_element = ElementTree.SubElement(mip, 'path')
            path_element.text = rel_macro_path
            hash_element = ElementTree.SubElement(mip, 'hash')
            hash_element.text = md5_hash_file(macro_path)
            update_time_element = ElementTree.SubElement(mip, 'update_time')
            update_time_element.text = os.path.getmtime(macro_path)


def ordered_load(stream):
    class OrderedLoader(yaml.Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return odict(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)

    return yaml.load(stream, OrderedLoader)


def get_tool_source_from_representation(tool_format, tool_representation):
    # TODO: make sure whatever is consuming this method uses ordered load.
    log.info("Loading dynamic tool - this is experimental - tool may not function in future.")
    if tool_format == "GalaxyTool":
        if "version" not in tool_representation:
            tool_representation["version"] = "1.0.0"  # Don't require version for embedded tools.
        return YamlToolSource(tool_representation)
    else:
        raise Exception("Unknown tool representation format [%s]." % tool_format)


def get_input_source(content):
    """Wrap an XML element in a XmlInputSource if needed.

    If the supplied content is already an InputSource object,
    it is simply returned. This allow Galaxy to uniformly
    consume using the tool input source interface.
    """
    if not isinstance(content, InputSource):
        content = XmlInputSource(content)
    return content


__all__ = ("get_tool_source", "get_input_source")
