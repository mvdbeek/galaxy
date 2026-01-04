from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define

from ..models.object_store_template_summary_type import ObjectStoreTemplateSummaryType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.badge_dict import BadgeDict
    from ..models.template_secret import TemplateSecret
    from ..models.template_variable_boolean import TemplateVariableBoolean
    from ..models.template_variable_integer import TemplateVariableInteger
    from ..models.template_variable_path_component import TemplateVariablePathComponent
    from ..models.template_variable_string import TemplateVariableString


T = TypeVar("T", bound="ObjectStoreTemplateSummary")


@_attrs_define
class ObjectStoreTemplateSummary:
    """
    Attributes:
        badges (list[BadgeDict]):
        description (None | str):
        id (str):
        name (None | str):
        type_ (ObjectStoreTemplateSummaryType):
        hidden (bool | Unset):  Default: False.
        secrets (list[TemplateSecret] | None | Unset):
        variables (list[TemplateVariableBoolean | TemplateVariableInteger | TemplateVariablePathComponent |
            TemplateVariableString] | None | Unset):
        version (int | Unset):  Default: 0.
    """

    badges: list[BadgeDict]
    description: None | str
    id: str
    name: None | str
    type_: ObjectStoreTemplateSummaryType
    hidden: bool | Unset = False
    secrets: list[TemplateSecret] | None | Unset = UNSET
    variables: (
        list[TemplateVariableBoolean | TemplateVariableInteger | TemplateVariablePathComponent | TemplateVariableString]
        | None
        | Unset
    ) = UNSET
    version: int | Unset = 0

    def to_dict(self) -> dict[str, Any]:
        from ..models.template_variable_integer import TemplateVariableInteger
        from ..models.template_variable_path_component import TemplateVariablePathComponent
        from ..models.template_variable_string import TemplateVariableString

        badges = []
        for badges_item_data in self.badges:
            badges_item = badges_item_data.to_dict()
            badges.append(badges_item)

        description: None | str
        description = self.description

        id = self.id

        name: None | str
        name = self.name

        type_ = self.type_.value

        hidden = self.hidden

        secrets: list[dict[str, Any]] | None | Unset
        if isinstance(self.secrets, Unset):
            secrets = UNSET
        elif isinstance(self.secrets, list):
            secrets = []
            for secrets_type_0_item_data in self.secrets:
                secrets_type_0_item = secrets_type_0_item_data.to_dict()
                secrets.append(secrets_type_0_item)

        else:
            secrets = self.secrets

        variables: list[dict[str, Any]] | None | Unset
        if isinstance(self.variables, Unset):
            variables = UNSET
        elif isinstance(self.variables, list):
            variables = []
            for variables_type_0_item_data in self.variables:
                variables_type_0_item: dict[str, Any]
                if isinstance(variables_type_0_item_data, TemplateVariableString):
                    variables_type_0_item = variables_type_0_item_data.to_dict()
                elif isinstance(variables_type_0_item_data, TemplateVariableInteger):
                    variables_type_0_item = variables_type_0_item_data.to_dict()
                elif isinstance(variables_type_0_item_data, TemplateVariablePathComponent):
                    variables_type_0_item = variables_type_0_item_data.to_dict()
                else:
                    variables_type_0_item = variables_type_0_item_data.to_dict()

                variables.append(variables_type_0_item)

        else:
            variables = self.variables

        version = self.version

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "badges": badges,
                "description": description,
                "id": id,
                "name": name,
                "type": type_,
            }
        )
        if hidden is not UNSET:
            field_dict["hidden"] = hidden
        if secrets is not UNSET:
            field_dict["secrets"] = secrets
        if variables is not UNSET:
            field_dict["variables"] = variables
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.badge_dict import BadgeDict
        from ..models.template_secret import TemplateSecret
        from ..models.template_variable_boolean import TemplateVariableBoolean
        from ..models.template_variable_integer import TemplateVariableInteger
        from ..models.template_variable_path_component import TemplateVariablePathComponent
        from ..models.template_variable_string import TemplateVariableString

        d = dict(src_dict)
        badges = []
        _badges = d.pop("badges")
        for badges_item_data in _badges:
            badges_item = BadgeDict.from_dict(badges_item_data)

            badges.append(badges_item)

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))

        id = d.pop("id")

        def _parse_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        name = _parse_name(d.pop("name"))

        type_ = ObjectStoreTemplateSummaryType(d.pop("type"))

        hidden = d.pop("hidden", UNSET)

        def _parse_secrets(data: object) -> list[TemplateSecret] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                secrets_type_0 = []
                _secrets_type_0 = data
                for secrets_type_0_item_data in _secrets_type_0:
                    secrets_type_0_item = TemplateSecret.from_dict(secrets_type_0_item_data)

                    secrets_type_0.append(secrets_type_0_item)

                return secrets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TemplateSecret] | None | Unset, data)

        secrets = _parse_secrets(d.pop("secrets", UNSET))

        def _parse_variables(
            data: object,
        ) -> (
            list[
                TemplateVariableBoolean
                | TemplateVariableInteger
                | TemplateVariablePathComponent
                | TemplateVariableString
            ]
            | None
            | Unset
        ):
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                variables_type_0 = []
                _variables_type_0 = data
                for variables_type_0_item_data in _variables_type_0:

                    def _parse_variables_type_0_item(
                        data: object,
                    ) -> (
                        TemplateVariableBoolean
                        | TemplateVariableInteger
                        | TemplateVariablePathComponent
                        | TemplateVariableString
                    ):
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            variables_type_0_item_type_0 = TemplateVariableString.from_dict(data)

                            return variables_type_0_item_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            variables_type_0_item_type_1 = TemplateVariableInteger.from_dict(data)

                            return variables_type_0_item_type_1
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            variables_type_0_item_type_2 = TemplateVariablePathComponent.from_dict(data)

                            return variables_type_0_item_type_2
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        if not isinstance(data, dict):
                            raise TypeError()
                        variables_type_0_item_type_3 = TemplateVariableBoolean.from_dict(data)

                        return variables_type_0_item_type_3

                    variables_type_0_item = _parse_variables_type_0_item(variables_type_0_item_data)

                    variables_type_0.append(variables_type_0_item)

                return variables_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[
                    TemplateVariableBoolean
                    | TemplateVariableInteger
                    | TemplateVariablePathComponent
                    | TemplateVariableString
                ]
                | None
                | Unset,
                data,
            )

        variables = _parse_variables(d.pop("variables", UNSET))

        version = d.pop("version", UNSET)

        object_store_template_summary = cls(
            badges=badges,
            description=description,
            id=id,
            name=name,
            type_=type_,
            hidden=hidden,
            secrets=secrets,
            variables=variables,
            version=version,
        )

        return object_store_template_summary
