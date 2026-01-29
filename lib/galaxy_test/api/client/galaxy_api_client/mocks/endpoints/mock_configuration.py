from typing import TYPE_CHECKING, Any

from ...models.configuration_decode_decode_id_200_response import ConfigurationDecodeDecodeId200Response
from ...models.configuration_decode_decode_id_param_run_as import ConfigurationDecodeDecodeIdParamRunAs
from ...models.configuration_dynamic_tool_confs_dynamic_tool_confs_param_run_as import (
    ConfigurationDynamicToolConfsDynamicToolConfsParamRunAs,
)
from ...models.configuration_encode_encode_id_200_response import ConfigurationEncodeEncodeId200Response
from ...models.configuration_encode_encode_id_param_run_as import ConfigurationEncodeEncodeIdParamRunAs
from ...models.configuration_index_200_response import ConfigurationIndex200Response
from ...models.configuration_index_param_keys import ConfigurationIndexParamKeys
from ...models.configuration_index_param_run_as import ConfigurationIndexParamRunAs
from ...models.configuration_index_param_view import ConfigurationIndexParamView
from ...models.configuration_tool_lineages_tool_lineages_param_run_as import (
    ConfigurationToolLineagesToolLineagesParamRunAs,
)
from ...models.configuration_toolbox_reload_toolbox_param_run_as import ConfigurationToolboxReloadToolboxParamRunAs
from ...models.configuration_version_200_response import ConfigurationVersion200Response
from ...models.configuration_whoami_200_response import ConfigurationWhoami200Response
from ...models.configuration_whoami_param_run_as import ConfigurationWhoamiParamRunAs

if TYPE_CHECKING:
    pass


class MockConfigurationClient:
    """
    Mock implementation of ConfigurationClient for testing.

    Provides default implementations that raise NotImplementedError.
    Override methods as needed in your tests.

    Example:
        class TestConfigurationClient(MockConfigurationClient):
            async def method_name(self, ...) -> ReturnType:
                return test_data
    """

    async def configuration_index(
        self,
        view: ConfigurationIndexParamView | None = None,
        keys: ConfigurationIndexParamKeys | None = None,
        run_as: ConfigurationIndexParamRunAs | None = None,
    ) -> ConfigurationIndex200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockConfigurationClient.configuration_index() not implemented. Override this method in your test subclass."
        )

    async def configuration_decode_decode_id(
        self,
        encoded_id: str,
        run_as: ConfigurationDecodeDecodeIdParamRunAs | None = None,
    ) -> ConfigurationDecodeDecodeId200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockConfigurationClient.configuration_decode_decode_id() not implemented. Override this method in your test subclass."
        )

    async def configuration_dynamic_tool_confs_dynamic_tool_confs(
        self,
        run_as: ConfigurationDynamicToolConfsDynamicToolConfsParamRunAs | None = None,
    ) -> list[Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockConfigurationClient.configuration_dynamic_tool_confs_dynamic_tool_confs() not implemented. Override this method in your test subclass."
        )

    async def configuration_encode_encode_id(
        self,
        decoded_id: int,
        run_as: ConfigurationEncodeEncodeIdParamRunAs | None = None,
    ) -> ConfigurationEncodeEncodeId200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockConfigurationClient.configuration_encode_encode_id() not implemented. Override this method in your test subclass."
        )

    async def configuration_tool_lineages_tool_lineages(
        self,
        run_as: ConfigurationToolLineagesToolLineagesParamRunAs | None = None,
    ) -> list[Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockConfigurationClient.configuration_tool_lineages_tool_lineages() not implemented. Override this method in your test subclass."
        )

    async def configuration_toolbox_reload_toolbox(
        self,
        run_as: ConfigurationToolboxReloadToolboxParamRunAs | None = None,
    ) -> dict[str, Any]:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockConfigurationClient.configuration_toolbox_reload_toolbox() not implemented. Override this method in your test subclass."
        )

    async def configuration_version(
        self,
    ) -> ConfigurationVersion200Response:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockConfigurationClient.configuration_version() not implemented. Override this method in your test subclass."
        )

    async def configuration_whoami(
        self,
        run_as: ConfigurationWhoamiParamRunAs | None = None,
    ) -> ConfigurationWhoami200Response | None:
        """
        Mock implementation that raises NotImplementedError.

        Override this method in your test subclass to provide
        the behavior needed for your test scenario.
        """
        raise NotImplementedError(
            "MockConfigurationClient.configuration_whoami() not implemented. Override this method in your test subclass."
        )
