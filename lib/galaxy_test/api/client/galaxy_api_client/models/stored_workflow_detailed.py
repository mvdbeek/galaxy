from dataclasses import dataclass
from datetime import datetime

from .annotation import Annotation
from .annotations import Annotations
from .creator import Creator
from .doi import Doi
from .email_hash import EmailHash
from .help_ import Help_
from .importable import Importable
from .inputs import Inputs
from .latest_workflow_uuid import LatestWorkflowUuid
from .license import License
from .number_of_steps import NumberOfSteps
from .readme import Readme
from .show_in_tool_panel import ShowInToolPanel
from .slug import Slug
from .source_metadata import SourceMetadata
from .stored_workflow_detailed_steps import StoredWorkflowDetailedSteps
from .tags import Tags

__all__ = ["StoredWorkflowDetailed"]


@dataclass
class StoredWorkflowDetailed:
    """
    StoredWorkflowDetailed dataclass.

    Args:
        annotation (Optional[Annotation])
                                 : The annotation of this Visualization.
        create_time (datetime)   : The time and date this item was created.
        creator_deleted (bool)   : Whether the creator of this Workflow has been deleted.
        deleted (bool)           : Whether this item is marked as deleted.
        email_hash (Optional[EmailHash])
                                 : The hash of the email of the creator of this workflow
        help_ (Optional[Help_])  : Help text shown below the tool interface.
        hidden (bool)            : TODO
        id_ (str)                :
        importable (Optional[Importable])
                                 : Indicates if the workflow is importable by the current
                                   user.
        model_class (str)        : The name of the database model class.
        name (str)               : The name of the history.
        owner (str)              : The name of the user who owns this workflow.
        published (bool)         : Whether this workflow is currently publicly available to
                                   all users.
        readme (Optional[Readme]): The detailed markdown readme of the workflow.
        slug (Optional[Slug])    : The slug of the visualization.
        source_metadata (Optional[SourceMetadata])
                                 : The source metadata of the workflow.
        tags (Tags)              : The collection of tags associated with an item.
        update_time (datetime)   : The last time and date this item was updated.
        url (str)                : The relative URL to access this item.
        version (int)            : The version of the workflow represented by an incremental
                                   number.
        annotations (Optional[Annotations])
                                 : An list of annotations to provide details or to help
                                   understand the purpose and usage of this workflow.
        creator (Optional[Creator])
                                 : Additional information about the creator (or multiple
                                   creators) of this workflow.
        doi (Optional[Doi])      : A list of Digital Object Identifiers associated with this
                                   workflow.
        inputs (Optional[Inputs]): A dictionary containing information about all the inputs
                                   of the workflow.
        latest_workflow_uuid (Optional[LatestWorkflowUuid])
                                 : TODO
        license (Optional[License])
                                 : A full URI or a a short
                                   [SPDX](https://spdx.org/licenses/) identifier for a
                                   license for this tool wrapper. The tool wrapper license
                                   can be independent of the underlying tool license. This
                                   license covers the tool yaml and associated scripts
                                   shipped with the tool.
        number_of_steps (Optional[NumberOfSteps])
                                 : The number of steps that make up this workflow.
        show_in_tool_panel (Optional[ShowInToolPanel])
                                 : Whether to display this workflow in the Tools Panel.
        steps (Optional[StoredWorkflowDetailedSteps])
                                 : A dictionary with information about all the steps of the
                                   workflow.
    """

    annotation: Annotation | None  # The annotation of this Visualization.
    create_time: datetime  # The time and date this item was created.
    creator_deleted: bool  # Whether the creator of this Workflow has been deleted.
    deleted: bool  # Whether this item is marked as deleted.
    email_hash: EmailHash | None  # The hash of the email of the creator of this workflow
    help_: Help_ | None  # Help text shown below the tool interface.
    hidden: bool  # TODO
    id_: str
    importable: Importable | None  # Indicates if the workflow is importable by the current user.
    model_class: str  # The name of the database model class.
    name: str  # The name of the history.
    owner: str  # The name of the user who owns this workflow.
    published: bool  # Whether this workflow is currently publicly available to all users.
    readme: Readme | None  # The detailed markdown readme of the workflow.
    slug: Slug | None  # The slug of the visualization.
    source_metadata: SourceMetadata | None  # The source metadata of the workflow.
    tags: Tags  # The collection of tags associated with an item.
    update_time: datetime  # The last time and date this item was updated.
    url: str  # The relative URL to access this item.
    version: int  # The version of the workflow represented by an incremental number.
    annotations: Annotations | None = (
        None  # An list of annotations to provide details or to help understand the purpose and usage of this workflow.
    )
    creator: Creator | None = None  # Additional information about the creator (or multiple creators) of this workflow.
    doi: Doi | None = None  # A list of Digital Object Identifiers associated with this workflow.
    inputs: Inputs | None = None  # A dictionary containing information about all the inputs of the workflow.
    latest_workflow_uuid: LatestWorkflowUuid | None = None  # TODO
    license: License | None = (
        None  # A full URI or a a short [SPDX](https://spdx.org/licenses/) identifier for a license for this tool wrapper. The tool wrapper license can be independent of the underlying tool license. This license covers the tool yaml and associated scripts shipped with the tool.
    )
    number_of_steps: NumberOfSteps | None = None  # The number of steps that make up this workflow.
    show_in_tool_panel: ShowInToolPanel | None = None  # Whether to display this workflow in the Tools Panel.
    steps: StoredWorkflowDetailedSteps | None = (
        None  # A dictionary with information about all the steps of the workflow.
    )
