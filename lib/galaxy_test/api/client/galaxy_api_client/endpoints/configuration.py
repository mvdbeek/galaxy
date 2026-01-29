from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport

from ..models.anonymous_array_item_117 import AnonymousArrayItem117
from ..models.anonymous_array_item_119 import AnonymousArrayItem119
from ..models.configuration_decode_decode_id_200_response_2 import ConfigurationDecodeDecodeId200Response2
from ..models.configuration_decode_decode_id_param_run_as import ConfigurationDecodeDecodeIdParamRunAs
from ..models.configuration_dynamic_tool_confs_dynamic_tool_confs_param_run_as import (
    ConfigurationDynamicToolConfsDynamicToolConfsParamRunAs,
)
from ..models.configuration_encode_encode_id_200_response_2 import ConfigurationEncodeEncodeId200Response2
from ..models.configuration_encode_encode_id_param_run_as import ConfigurationEncodeEncodeIdParamRunAs
from ..models.configuration_index_200_response_2 import ConfigurationIndex200Response2
from ..models.configuration_index_param_keys import ConfigurationIndexParamKeys
from ..models.configuration_index_param_run_as import ConfigurationIndexParamRunAs
from ..models.configuration_index_param_view import ConfigurationIndexParamView
from ..models.configuration_tool_lineages_tool_lineages_param_run_as import (
    ConfigurationToolLineagesToolLineagesParamRunAs,
)
from ..models.configuration_toolbox_reload_toolbox_param_run_as import ConfigurationToolboxReloadToolboxParamRunAs
from ..models.configuration_version_200_response_2 import ConfigurationVersion200Response2
from ..models.configuration_whoami_200_response_2 import ConfigurationWhoami200Response2
from ..models.configuration_whoami_param_run_as import ConfigurationWhoamiParamRunAs


class ConfigurationClient:
    """Client for configuration endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def configuration_index_2_2(
        self,
        view: ConfigurationIndexParamView | None = None,
        keys: ConfigurationIndexParamKeys | None = None,
        run_as: ConfigurationIndexParamRunAs | None = None,
    ) -> ConfigurationIndex200Response2:
        """
        Return an object containing exposable configuration settings

        Return an object containing exposable configuration settings.  A more complete list is
        returned if the user is an admin. Pass in `view` and a comma-seperated list of keys to
        control which configuration settings are returned.

        Args:
            view (Optional[ConfigurationIndexParamView])
                                     : View to be passed to the serializer
            keys (Optional[ConfigurationIndexParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[ConfigurationIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationIndex200Response2: Object containing exposable configuration settings

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ConfigurationIndex200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_index_2_2(
        self,
        view: ConfigurationIndexParamView | None = None,
        keys: ConfigurationIndexParamKeys | None = None,
        run_as: ConfigurationIndexParamRunAs | None = None,
    ) -> ConfigurationIndex200Response2:
        """
        Return an object containing exposable configuration settings

        Return an object containing exposable configuration settings.  A more complete list is
        returned if the user is an admin. Pass in `view` and a comma-seperated list of keys to
        control which configuration settings are returned.

        Args:
            view (Optional[ConfigurationIndexParamView])
                                     : View to be passed to the serializer
            keys (Optional[ConfigurationIndexParamKeys])
                                     : Comma-separated list of keys to be passed to the
                                       serializer
            run-as (Optional[ConfigurationIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationIndex200Response2: Object containing exposable configuration settings

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration"

        params: dict[str, Any] = {
            **({"view": view} if view is not None else {}),
            **({"keys": keys} if keys is not None else {}),
        }

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=params, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ConfigurationIndex200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_decode_decode_id_2_2(
        self,
        encoded_id: str,
        run_as: ConfigurationDecodeDecodeIdParamRunAs | None = None,
    ) -> ConfigurationDecodeDecodeId200Response2:
        """
        Decode a given id

        Decode a given id.

        Args:
            encoded_id (str)         : Encoded id to be decoded
            run-as (Optional[ConfigurationDecodeDecodeIdParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationDecodeDecodeId200Response2: Decoded id

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/decode/{encoded_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ConfigurationDecodeDecodeId200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_decode_decode_id_2_2(
        self,
        encoded_id: str,
        run_as: ConfigurationDecodeDecodeIdParamRunAs | None = None,
    ) -> ConfigurationDecodeDecodeId200Response2:
        """
        Decode a given id

        Decode a given id.

        Args:
            encoded_id (str)         : Encoded id to be decoded
            run-as (Optional[ConfigurationDecodeDecodeIdParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationDecodeDecodeId200Response2: Decoded id

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/decode/{encoded_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ConfigurationDecodeDecodeId200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_dynamic_tool_confs_dynamic_tool_confs_2_2(
        self,
        run_as: ConfigurationDynamicToolConfsDynamicToolConfsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem117]:
        """
        Return dynamic tool configuration files

        Return dynamic tool configuration files.

        Args:
            run-as (Optional[ConfigurationDynamicToolConfsDynamicToolConfsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem117]: Dynamic tool configuration files

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/dynamic_tool_confs"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem117], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_dynamic_tool_confs_dynamic_tool_confs_2_2(
        self,
        run_as: ConfigurationDynamicToolConfsDynamicToolConfsParamRunAs | None = None,
    ) -> list[AnonymousArrayItem117]:
        """
        Return dynamic tool configuration files

        Return dynamic tool configuration files.

        Args:
            run-as (Optional[ConfigurationDynamicToolConfsDynamicToolConfsParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem117]: Dynamic tool configuration files

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/dynamic_tool_confs"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem117], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_encode_encode_id_2_2(
        self,
        decoded_id: int,
        run_as: ConfigurationEncodeEncodeIdParamRunAs | None = None,
    ) -> ConfigurationEncodeEncodeId200Response2:
        """
        Encode a given id

        Decode a given id.

        Args:
            decoded_id (int)         : Decoded id to be encoded
            run-as (Optional[ConfigurationEncodeEncodeIdParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationEncodeEncodeId200Response2: Encoded id

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/encode/{decoded_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ConfigurationEncodeEncodeId200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_encode_encode_id_2_2(
        self,
        decoded_id: int,
        run_as: ConfigurationEncodeEncodeIdParamRunAs | None = None,
    ) -> ConfigurationEncodeEncodeId200Response2:
        """
        Encode a given id

        Decode a given id.

        Args:
            decoded_id (int)         : Decoded id to be encoded
            run-as (Optional[ConfigurationEncodeEncodeIdParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationEncodeEncodeId200Response2: Encoded id

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/encode/{decoded_id}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ConfigurationEncodeEncodeId200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_tool_lineages_tool_lineages_2_2(
        self,
        run_as: ConfigurationToolLineagesToolLineagesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem119]:
        """
        Return tool lineages for tools that have them

        Return tool lineages for tools that have them.

        Args:
            run-as (Optional[ConfigurationToolLineagesToolLineagesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem119]: Tool lineages for tools that have them

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/tool_lineages"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem119], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_tool_lineages_tool_lineages_2_2(
        self,
        run_as: ConfigurationToolLineagesToolLineagesParamRunAs | None = None,
    ) -> list[AnonymousArrayItem119]:
        """
        Return tool lineages for tools that have them

        Return tool lineages for tools that have them.

        Args:
            run-as (Optional[ConfigurationToolLineagesToolLineagesParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            List[AnonymousArrayItem119]: Tool lineages for tools that have them

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/tool_lineages"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(list[AnonymousArrayItem119], response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_toolbox_reload_toolbox_2_2(
        self,
        run_as: ConfigurationToolboxReloadToolboxParamRunAs | None = None,
    ) -> Any:
        """
        Reload the Galaxy toolbox (but not individual tools)

        Reload the Galaxy toolbox (but not individual tools).

        Args:
            run-as (Optional[ConfigurationToolboxReloadToolboxParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/toolbox"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_toolbox_reload_toolbox_2_2(
        self,
        run_as: ConfigurationToolboxReloadToolboxParamRunAs | None = None,
    ) -> Any:
        """
        Reload the Galaxy toolbox (but not individual tools)

        Reload the Galaxy toolbox (but not individual tools).

        Args:
            run-as (Optional[ConfigurationToolboxReloadToolboxParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            Any: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/configuration/toolbox"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("PUT", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.json()  # Type is Any
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_version_2_2(
        self,
    ) -> ConfigurationVersion200Response2:
        """
        Return Galaxy version information: major/minor version, optional extra info

        Return Galaxy version information: major/minor version, optional extra info.

        Returns:
            ConfigurationVersion200Response2: Galaxy version information: major/minor version,
                                              optional extra info

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/version"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ConfigurationVersion200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_version_2_2(
        self,
    ) -> ConfigurationVersion200Response2:
        """
        Return Galaxy version information: major/minor version, optional extra info

        Return Galaxy version information: major/minor version, optional extra info.

        Returns:
            ConfigurationVersion200Response2: Galaxy version information: major/minor version,
                                              optional extra info

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/version"

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=None)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ConfigurationVersion200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_whoami_2_2(
        self,
        run_as: ConfigurationWhoamiParamRunAs | None = None,
    ) -> ConfigurationWhoami200Response2:
        """
        Return information about the current authenticated user

        Return information about the current authenticated user.

        Args:
            run-as (Optional[ConfigurationWhoamiParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationWhoami200Response2: Information about the current authenticated user

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/whoami"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ConfigurationWhoami200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def configuration_whoami_2_2(
        self,
        run_as: ConfigurationWhoamiParamRunAs | None = None,
    ) -> ConfigurationWhoami200Response2:
        """
        Return information about the current authenticated user

        Return information about the current authenticated user.

        Args:
            run-as (Optional[ConfigurationWhoamiParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            ConfigurationWhoami200Response2: Information about the current authenticated user

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/whoami"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(ConfigurationWhoami200Response2, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
