"""Utilities for loading tools and workflows from paths for admin user requests."""

import yaml

from galaxy import exceptions


def artifact_class(trans, as_dict):
    object_id = as_dict.get("object_id", None)
    if as_dict.get("src", None) == "from_path":
        # FIXME: assert trans is not None, but probably breaks conformance tests
        # Don't merge before we haven't addressed this
        if trans and not trans.user_is_admin:
            raise exceptions.AdminRequiredException()

        workflow_path = as_dict.get("path")
        with open(workflow_path) as f:
            as_dict = yaml.safe_load(f)

    artifact_class = as_dict.get("class", None)
    target_object = None
    if artifact_class is None and "$graph" in as_dict:
        object_id = object_id or "main"
        graph = as_dict["$graph"]
        if isinstance(graph, dict):
            target_object = graph.get(object_id)
        else:
            for item in graph:
                found_id = item.get("id")
                if found_id == object_id or found_id == f"#{object_id}":
                    target_object = item
                    break

        if target_object and target_object.get("class"):
            artifact_class = target_object["class"]
            if artifact_class in ("CommandLineTool", "ExpressionTool"):
                target_object['cwlVersion'] = as_dict['cwlVersion']

    return artifact_class, as_dict, object_id, target_object


__all__ = (
    'artifact_class',
)
