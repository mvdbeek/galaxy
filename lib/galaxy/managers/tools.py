import logging
from typing import TYPE_CHECKING
from uuid import uuid4

from sqlalchemy import sql

from galaxy import exceptions
from galaxy import model
from galaxy.exceptions import DuplicatedIdentifierException
from galaxy.tool_util.cwl import tool_proxy
from .base import ModelManager, raise_filter_err
from .executables import artifact_class

log = logging.getLogger(__name__)

if TYPE_CHECKING:
    from galaxy.managers.base import OrmFilterParsersType


class DynamicToolManager(ModelManager):
    """ Manages dynamic tools stored in Galaxy's database.
    """
    model_class = model.DynamicTool

    def get_tool_by_uuid(self, uuid):
        dynamic_tool = self._one_or_none(
            self.query().filter(self.model_class.uuid == uuid)
        )
        return dynamic_tool

    def get_tool_by_tool_id(self, tool_id):
        dynamic_tool = self._one_or_none(
            self.query().filter(self.model_class.tool_id == tool_id)
        )
        return dynamic_tool

    def get_tool_by_id(self, object_id):
        dynamic_tool = self._one_or_none(
            self.query().filter(self.model_class.id == object_id)
        )
        return dynamic_tool

    def create_tool(self, trans, tool_payload, allow_load=True):
        src = tool_payload.get("src", "representation")
        is_path = src == "from_path"
        target_object = None

        if is_path:
            tool_format, representation, object_id, target_object = artifact_class(None, tool_payload)
        else:
            assert src == "representation"
            representation = tool_payload.get("representation")
            if not representation:
                raise exceptions.ObjectAttributeMissingException(
                    "A tool 'representation' is required."
                )

            tool_format = representation.get("class")
            if not tool_format:
                raise exceptions.ObjectAttributeMissingException(
                    "Current tool representations require 'class'."
                )

        enable_beta_formats = getattr(self.app.config, "enable_beta_tool_formats", False)
        if not enable_beta_formats:
            raise exceptions.ConfigDoesNotAllowException("Set 'enable_beta_tool_formats' in Galaxy config to create dynamic tools.")

        tool_directory = tool_payload.get("tool_directory")
        tool_path = None
        if tool_format == "GalaxyTool":
            uuid = tool_payload.get("uuid")
            if uuid is None:
                uuid = uuid4()

            tool_id = representation.get("id")
            if not tool_id:
                tool_id = str(uuid)

        elif tool_format in ("CommandLineTool", "ExpressionTool"):
            # CWL tools
            uuid = tool_payload.get("uuid") or representation.get('uuid')
            if uuid is None:
                uuid = str(uuid4())
            tool_path = tool_payload.get("path")
            if target_object is not None:
                representation = {'raw_process_reference': target_object, 'uuid': uuid, 'class': tool_format}
                proxy = tool_proxy(tool_object=target_object, tool_directory=tool_directory, uuid=uuid)
                tool_path = None
            elif is_path:
                proxy = tool_proxy(tool_path=tool_path, uuid=uuid)
            else:
                # Build a tool proxy so that we can convert to the persistable
                # hash.
                proxy = tool_proxy(
                    tool_object=representation["raw_process_reference"],
                    tool_directory=tool_directory,
                    uuid=uuid,
                )
            tool_id = proxy.galaxy_id()
        else:
            raise Exception(f"Unknown tool format [{tool_format}] encountered.")
        # TODO: enforce via DB constraint and catch appropriate
        # exception.
        dynamic_tool = self.get_tool_by_uuid(uuid)
        if dynamic_tool:
            if not allow_load:
                raise DuplicatedIdentifierException(dynamic_tool.id)
            assert dynamic_tool.uuid == uuid
        else:
            tool_version = representation.get("version")
            dynamic_tool = self.create(
                tool_format=tool_format,
                tool_id=tool_id,
                tool_version=tool_version,
                tool_path=tool_path,
                tool_directory=tool_directory,
                uuid=uuid,
                value=representation,
            )
        self.app.toolbox.load_dynamic_tool(dynamic_tool)
        return dynamic_tool

    def list_tools(self, active=True):
        return self.query().filter(self.model_class.active == active)

    def deactivate(self, dynamic_tool):
        self.update(dynamic_tool, {"active": False})
        return dynamic_tool


class ToolFilterMixin:
    orm_filter_parsers: "OrmFilterParsersType"

    def create_tool_filter(self, attr, op, val):

        def _create_tool_filter(model_class=None):
            if op == 'eq':
                cond = model.Job.table.c.tool_id == val
            elif op == 'contains':
                cond = model.Job.table.c.tool_id.contains(val, autoescape=True)
            else:
                raise_filter_err(attr, op, val, 'bad op in filter')
            if model_class is model.HistoryDatasetAssociation:
                return sql.expression.and_(
                    model.Job.table.c.id == model.JobToOutputDatasetAssociation.table.c.job_id,
                    model.HistoryDatasetAssociation.table.c.id == model.JobToOutputDatasetAssociation.table.c.dataset_id,
                    cond
                )
            elif model_class is model.HistoryDatasetCollectionAssociation:
                return sql.expression.and_(
                    model.Job.id == model.JobToOutputDatasetAssociation.job_id,
                    model.JobToOutputDatasetAssociation.dataset_id == model.DatasetCollectionElement.hda_id,
                    model.DatasetCollectionElement.dataset_collection_id == model.HistoryDatasetCollectionAssociation.collection_id,
                    cond,
                )
            else:
                return True
        return _create_tool_filter

    def _add_parsers(self):
        self.orm_filter_parsers.update({
            'tool_id': self.create_tool_filter,
        })
