from dataclasses import dataclass
from datetime import datetime

from .help__42 import Help42
from .stored_workflow_detailed_annotation import StoredWorkflowDetailedAnnotation
from .stored_workflow_detailed_annotations import StoredWorkflowDetailedAnnotations
from .stored_workflow_detailed_creator import StoredWorkflowDetailedCreator
from .stored_workflow_detailed_doi import StoredWorkflowDetailedDoi
from .stored_workflow_detailed_email_hash import StoredWorkflowDetailedEmailHash
from .stored_workflow_detailed_importable import StoredWorkflowDetailedImportable
from .stored_workflow_detailed_inputs import StoredWorkflowDetailedInputs
from .stored_workflow_detailed_latest_workflow_uuid import StoredWorkflowDetailedLatestWorkflowUuid
from .stored_workflow_detailed_license import StoredWorkflowDetailedLicense
from .stored_workflow_detailed_number_of_steps import StoredWorkflowDetailedNumberOfSteps
from .stored_workflow_detailed_readme import StoredWorkflowDetailedReadme
from .stored_workflow_detailed_show_in_tool_panel import StoredWorkflowDetailedShowInToolPanel
from .stored_workflow_detailed_slug import StoredWorkflowDetailedSlug
from .stored_workflow_detailed_source_metadata import StoredWorkflowDetailedSourceMetadata
from .stored_workflow_detailed_steps import StoredWorkflowDetailedSteps

__all__ = ["StoredWorkflowDetailed"]


@dataclass
class StoredWorkflowDetailed:
    """
    StoredWorkflowDetailed dataclass

    Args:
        annotation (StoredWorkflowDetailedAnnotation)
                                 : An annotation to provide details or to help understand
                                   the purpose and usage of this item.
        create_time (datetime)   : The time and date this item was created.
        creator_deleted (bool)   : Whether the creator of this Workflow has been deleted.
        deleted (bool)           : Whether this item is marked as deleted.
        email_hash (StoredWorkflowDetailedEmailHash)
                                 : The hash of the email of the creator of this workflow
        help_ (Help42 | None)    : The detailed help text for how to use the workflow and
                                   debug problems with it. (maps from 'help')
        hidden (bool)            : TODO
        id_ (str)                : Maps from 'id'
        importable (StoredWorkflowDetailedImportable)
                                 : Indicates if the workflow is importable by the current
                                   user.
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the history.
        owner (str)              : The name of the user who owns this workflow.
        published (bool)         : Whether this workflow is currently publicly available to
                                   all users.
        readme (StoredWorkflowDetailedReadme)
                                 : The detailed markdown readme of the workflow.
        slug (StoredWorkflowDetailedSlug)
                                 : The slug of the workflow.
        source_metadata (StoredWorkflowDetailedSourceMetadata)
                                 : The source metadata of the workflow.
        tags (List[str])         : The collection of tags associated with an item.
        update_time (datetime)   : The last time and date this item was updated.
        url (str)                : The relative URL to access this item.
        version (int)            : The version of the workflow represented by an incremental
                                   number.
        annotations (StoredWorkflowDetailedAnnotations | None)
                                 : An list of annotations to provide details or to help
                                   understand the purpose and usage of this workflow.
        creator (StoredWorkflowDetailedCreator | None)
                                 : Additional information about the creator (or multiple
                                   creators) of this workflow.
        doi (StoredWorkflowDetailedDoi | None)
                                 : A list of Digital Object Identifiers associated with this
                                   workflow.
        inputs (StoredWorkflowDetailedInputs | None)
                                 : A dictionary containing information about all the inputs
                                   of the workflow.
        latest_workflow_uuid (StoredWorkflowDetailedLatestWorkflowUuid | None)
                                 : TODO
        license (StoredWorkflowDetailedLicense | None)
                                 : SPDX Identifier of the license associated with this
                                   workflow.
        number_of_steps (StoredWorkflowDetailedNumberOfSteps | None)
                                 : The number of steps that make up this workflow.
        show_in_tool_panel (StoredWorkflowDetailedShowInToolPanel | None)
                                 : Whether to display this workflow in the Tools Panel.
        steps (StoredWorkflowDetailedSteps | None)
                                 : A dictionary with information about all the steps of the
                                   workflow.
    """

    annotation: StoredWorkflowDetailedAnnotation  # An annotation to provide details or to help understand the purpose and usage of this item.
    create_time: datetime  # The time and date this item was created.
    creator_deleted: bool  # Whether the creator of this Workflow has been deleted.
    deleted: bool  # Whether this item is marked as deleted.
    email_hash: StoredWorkflowDetailedEmailHash  # The hash of the email of the creator of this workflow
    help_: (
        Help42 | None
    )  # The detailed help text for how to use the workflow and debug problems with it. (maps from 'help')
    hidden: bool  # TODO
    id_: str  # Maps from 'id'
    importable: StoredWorkflowDetailedImportable  # Indicates if the workflow is importable by the current user.
    model_class: str  # The name of the database model class.
    name: str  # The name of the history.
    owner: str  # The name of the user who owns this workflow.
    published: bool  # Whether this workflow is currently publicly available to all users.
    readme: StoredWorkflowDetailedReadme  # The detailed markdown readme of the workflow.
    slug: StoredWorkflowDetailedSlug  # The slug of the workflow.
    source_metadata: StoredWorkflowDetailedSourceMetadata  # The source metadata of the workflow.
    tags: list[str]  # The collection of tags associated with an item.
    update_time: datetime  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    version: int  # The version of the workflow represented by an incremental number.
    annotations: StoredWorkflowDetailedAnnotations | None = (
        None  # An list of annotations to provide details or to help understand the purpose and usage of this workflow.
    )
    creator: StoredWorkflowDetailedCreator | None = (
        None  # Additional information about the creator (or multiple creators) of this workflow.
    )
    doi: StoredWorkflowDetailedDoi | None = None  # A list of Digital Object Identifiers associated with this workflow.
    inputs: StoredWorkflowDetailedInputs | None = (
        None  # A dictionary containing information about all the inputs of the workflow.
    )
    latest_workflow_uuid: StoredWorkflowDetailedLatestWorkflowUuid | None = None  # TODO
    license: StoredWorkflowDetailedLicense | None = (
        None  # SPDX Identifier of the license associated with this workflow.
    )
    number_of_steps: StoredWorkflowDetailedNumberOfSteps | None = (
        None  # The number of steps that make up this workflow.
    )
    show_in_tool_panel: StoredWorkflowDetailedShowInToolPanel | None = (
        None  # Whether to display this workflow in the Tools Panel.
    )
    steps: StoredWorkflowDetailedSteps | None = (
        None  # A dictionary with information about all the steps of the workflow.
    )

    class Meta:
        """Configure field name mapping for JSON conversion."""

        key_transform_with_load = {
            "annotation": "annotation",
            "annotations": "annotations",
            "create_time": "create_time",
            "creator": "creator",
            "creator_deleted": "creator_deleted",
            "deleted": "deleted",
            "doi": "doi",
            "email_hash": "email_hash",
            "help": "help_",
            "hidden": "hidden",
            "id": "id_",
            "importable": "importable",
            "inputs": "inputs",
            "latest_workflow_uuid": "latest_workflow_uuid",
            "license": "license",
            "model_class": "model_class",
            "name": "name",
            "number_of_steps": "number_of_steps",
            "owner": "owner",
            "published": "published",
            "readme": "readme",
            "show_in_tool_panel": "show_in_tool_panel",
            "slug": "slug",
            "source_metadata": "source_metadata",
            "steps": "steps",
            "tags": "tags",
            "update_time": "update_time",
            "url": "url",
            "version": "version",
        }
        key_transform_with_dump = {
            "annotation": "annotation",
            "annotations": "annotations",
            "create_time": "create_time",
            "creator": "creator",
            "creator_deleted": "creator_deleted",
            "deleted": "deleted",
            "doi": "doi",
            "email_hash": "email_hash",
            "help_": "help",
            "hidden": "hidden",
            "id_": "id",
            "importable": "importable",
            "inputs": "inputs",
            "latest_workflow_uuid": "latest_workflow_uuid",
            "license": "license",
            "model_class": "model_class",
            "name": "name",
            "number_of_steps": "number_of_steps",
            "owner": "owner",
            "published": "published",
            "readme": "readme",
            "show_in_tool_panel": "show_in_tool_panel",
            "slug": "slug",
            "source_metadata": "source_metadata",
            "steps": "steps",
            "tags": "tags",
            "update_time": "update_time",
            "url": "url",
            "version": "version",
        }
