import logging

from sqlalchemy import and_

from tool_shed.util import (
    hg_util,
    metadata_util,
    repository_util,
)

log = logging.getLogger(__name__)


class ToolVersionManager:

    def __init__(self, app):
        self.app = app

    def get_tool_version(self, tool_id):
        context = self.app.install_model.context
        return context.query(self.app.install_model.ToolVersion) \
                      .filter(self.app.install_model.ToolVersion.table.c.tool_id == tool_id) \
                      .first()

    def get_tool_version_association(self, parent_tool_version, tool_version):
        """
        Return a ToolVersionAssociation if one exists that associates the two
        received tool_versions. This function is called only from Galaxy.
        """
        context = self.app.install_model.context
        return context.query(self.app.install_model.ToolVersionAssociation) \
                      .filter(and_(self.app.install_model.ToolVersionAssociation.table.c.parent_id == parent_tool_version.id,
                                   self.app.install_model.ToolVersionAssociation.table.c.tool_id == tool_version.id)) \
                      .first()

    def get_version_lineage_for_tool(self, repository_id, repository_metadata, guid):
        """
        Return the tool version lineage chain in descendant order for the received
        guid contained in the received repsitory_metadata.tool_versions.  This function
        is called only from the Tool Shed.
        """
        repository = repository_util.get_repository_by_id(self.app, repository_id)
        repo = repository.hg_repo
        # Initialize the tool lineage
        version_lineage = [guid]
        # Get all ancestor guids of the received guid.
        current_child_guid = guid
        for changeset in hg_util.reversed_upper_bounded_changelog(repo, repository_metadata.changeset_revision):
            ctx = repo[changeset]
            rm = metadata_util.get_repository_metadata_by_changeset_revision(self.app, repository_id, str(ctx))
            if rm:
                parent_guid = rm.tool_versions.get(current_child_guid, None)
                if parent_guid:
                    version_lineage.append(parent_guid)
                    current_child_guid = parent_guid
        # Get all descendant guids of the received guid.
        current_parent_guid = guid
        for changeset in hg_util.reversed_lower_upper_bounded_changelog(repo,
                                                                        repository_metadata.changeset_revision,
                                                                        repository.tip()):
            ctx = repo[changeset]
            rm = metadata_util.get_repository_metadata_by_changeset_revision(self.app, repository_id, str(ctx))
            if rm:
                tool_versions = rm.tool_versions
                for child_guid, parent_guid in tool_versions.items():
                    if parent_guid == current_parent_guid:
                        version_lineage.insert(0, child_guid)
                        current_parent_guid = child_guid
                        break
        return version_lineage
