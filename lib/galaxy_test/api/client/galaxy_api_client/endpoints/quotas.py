from typing import Any, cast

from galaxy_test.api.client.galaxy_api_client.core.exceptions import HTTPError
from galaxy_test.api.client.galaxy_api_client.core.http_transport import HttpTransport
from galaxy_test.api.client.galaxy_api_client.core.utils import DataclassSerializer

from ..models.create_quota_params import CreateQuotaParams
from ..models.create_quota_result import CreateQuotaResult
from ..models.delete_quota_payload import DeleteQuotaPayload
from ..models.quota_details import QuotaDetails
from ..models.quota_summary_list import QuotaSummaryList
from ..models.quotas_create_param_run_as import QuotasCreateParamRunAs
from ..models.quotas_delete_param_run_as import QuotasDeleteParamRunAs
from ..models.quotas_deleted_index_deleted_param_run_as import QuotasDeletedIndexDeletedParamRunAs
from ..models.quotas_deleted_show_deleted_param_run_as import QuotasDeletedShowDeletedParamRunAs
from ..models.quotas_deleted_undelete_undelete_param_run_as import QuotasDeletedUndeleteUndeleteParamRunAs
from ..models.quotas_index_param_run_as import QuotasIndexParamRunAs
from ..models.quotas_purge_purge_param_run_as import QuotasPurgePurgeParamRunAs
from ..models.quotas_show_param_run_as import QuotasShowParamRunAs
from ..models.quotas_update_param_run_as import QuotasUpdateParamRunAs
from ..models.update_quota_params import UpdateQuotaParams


class QuotasClient:
    """Client for quotas endpoints. Uses HttpTransport for all HTTP and header management."""

    def __init__(self, transport: HttpTransport, base_url: str) -> None:
        self._transport = transport
        self.base_url: str = base_url

    async def quotas_index_2_2(
        self,
        run_as: QuotasIndexParamRunAs | None = None,
    ) -> QuotaSummaryList:
        """
        Displays a list with information of quotas that are currently active.

        Displays a list with information of quotas that are currently active.

        Args:
            run-as (Optional[QuotasIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            QuotaSummaryList: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(QuotaSummaryList, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_index_2_2(
        self,
        run_as: QuotasIndexParamRunAs | None = None,
    ) -> QuotaSummaryList:
        """
        Displays a list with information of quotas that are currently active.

        Displays a list with information of quotas that are currently active.

        Args:
            run-as (Optional[QuotasIndexParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            QuotaSummaryList: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(QuotaSummaryList, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_create_2_2(
        self,
        body: CreateQuotaParams,
        run_as: QuotasCreateParamRunAs | None = None,
    ) -> CreateQuotaResult:
        """
        Creates a new quota.

        Creates a new quota.

        Args:
            run-as (Optional[QuotasCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateQuotaParams) : Request body. (json)

        Returns:
            CreateQuotaResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateQuotaParams = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(CreateQuotaResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_create_2_2(
        self,
        body: CreateQuotaParams,
        run_as: QuotasCreateParamRunAs | None = None,
    ) -> CreateQuotaResult:
        """
        Creates a new quota.

        Creates a new quota.

        Args:
            run-as (Optional[QuotasCreateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (CreateQuotaParams) : Request body. (json)

        Returns:
            CreateQuotaResult: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: CreateQuotaParams = DataclassSerializer.serialize(body)

        response = await self._transport.request("POST", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(CreateQuotaResult, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_deleted_index_deleted_2_2(
        self,
        run_as: QuotasDeletedIndexDeletedParamRunAs | None = None,
    ) -> QuotaSummaryList:
        """
        Displays a list with information of quotas that have been deleted.

        Displays a list with information of quotas that have been deleted.

        Args:
            run-as (Optional[QuotasDeletedIndexDeletedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            QuotaSummaryList: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas/deleted"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(QuotaSummaryList, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_deleted_index_deleted_2_2(
        self,
        run_as: QuotasDeletedIndexDeletedParamRunAs | None = None,
    ) -> QuotaSummaryList:
        """
        Displays a list with information of quotas that have been deleted.

        Displays a list with information of quotas that have been deleted.

        Args:
            run-as (Optional[QuotasDeletedIndexDeletedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            QuotaSummaryList: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas/deleted"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(QuotaSummaryList, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_deleted_show_deleted_2_2(
        self,
        id_: str,
        run_as: QuotasDeletedShowDeletedParamRunAs | None = None,
    ) -> QuotaDetails:
        """
        Displays details on a particular quota that has been deleted.

        Displays details on a particular quota that has been deleted.

        Args:
            id (str)                 : The ID of the Quota.
            run-as (Optional[QuotasDeletedShowDeletedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            QuotaDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas/deleted/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(QuotaDetails, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_deleted_show_deleted_2_2(
        self,
        id_: str,
        run_as: QuotasDeletedShowDeletedParamRunAs | None = None,
    ) -> QuotaDetails:
        """
        Displays details on a particular quota that has been deleted.

        Displays details on a particular quota that has been deleted.

        Args:
            id (str)                 : The ID of the Quota.
            run-as (Optional[QuotasDeletedShowDeletedParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            QuotaDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas/deleted/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(QuotaDetails, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_deleted_undelete_undelete_2_2(
        self,
        id_: str,
        run_as: QuotasDeletedUndeleteUndeleteParamRunAs | None = None,
    ) -> str:
        """
        Restores a previously deleted quota.

        Restores a previously deleted quota.

        Args:
            id (str)                 : The ID of the Quota.
            run-as (Optional[QuotasDeletedUndeleteUndeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas/deleted/{id_}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_deleted_undelete_undelete_2_2(
        self,
        id_: str,
        run_as: QuotasDeletedUndeleteUndeleteParamRunAs | None = None,
    ) -> str:
        """
        Restores a previously deleted quota.

        Restores a previously deleted quota.

        Args:
            id (str)                 : The ID of the Quota.
            run-as (Optional[QuotasDeletedUndeleteUndeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas/deleted/{id_}/undelete"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_delete_2_2(
        self,
        id_: str,
        run_as: QuotasDeleteParamRunAs | None = None,
        body: DeleteQuotaPayload | None = None,
    ) -> str:
        """
        Deletes an existing quota.

        Deletes an existing quota.

        Args:
            id (str)                 : The ID of the Quota.
            run-as (Optional[QuotasDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[DeleteQuotaPayload])
                                     : Request body. (json)

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DeleteQuotaPayload | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_delete_2_2(
        self,
        id_: str,
        run_as: QuotasDeleteParamRunAs | None = None,
        body: DeleteQuotaPayload | None = None,
    ) -> str:
        """
        Deletes an existing quota.

        Deletes an existing quota.

        Args:
            id (str)                 : The ID of the Quota.
            run-as (Optional[QuotasDeleteParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (Optional[DeleteQuotaPayload])
                                     : Request body. (json)

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: DeleteQuotaPayload | None = DataclassSerializer.serialize(body)

        response = await self._transport.request("DELETE", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_show_2_2(
        self,
        id_: str,
        run_as: QuotasShowParamRunAs | None = None,
    ) -> QuotaDetails:
        """
        Displays details on a particular active quota.

        Displays details on a particular active quota.

        Args:
            id (str)                 : The ID of the Quota.
            run-as (Optional[QuotasShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            QuotaDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(QuotaDetails, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_show_2_2(
        self,
        id_: str,
        run_as: QuotasShowParamRunAs | None = None,
    ) -> QuotaDetails:
        """
        Displays details on a particular active quota.

        Displays details on a particular active quota.

        Args:
            id (str)                 : The ID of the Quota.
            run-as (Optional[QuotasShowParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            QuotaDetails: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("GET", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return cast(QuotaDetails, response.json())
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_update_2_2(
        self,
        id_: str,
        body: UpdateQuotaParams,
        run_as: QuotasUpdateParamRunAs | None = None,
    ) -> str:
        """
        Updates an existing quota.

        Updates an existing quota.

        Args:
            id (str)                 : The ID of the Quota.
            run-as (Optional[QuotasUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateQuotaParams) : Request body. (json)

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateQuotaParams = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_update_2_2(
        self,
        id_: str,
        body: UpdateQuotaParams,
        run_as: QuotasUpdateParamRunAs | None = None,
    ) -> str:
        """
        Updates an existing quota.

        Updates an existing quota.

        Args:
            id (str)                 : The ID of the Quota.
            run-as (Optional[QuotasUpdateParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.
            body (UpdateQuotaParams) : Request body. (json)

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas/{id_}"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        json_body: UpdateQuotaParams = DataclassSerializer.serialize(body)

        response = await self._transport.request("PUT", url, params=None, json=json_body, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_purge_purge_2_2(
        self,
        id_: str,
        run_as: QuotasPurgePurgeParamRunAs | None = None,
    ) -> str:
        """
        Purges a previously deleted quota.

        Args:
            id (str)                 : The ID of the Quota.
            run-as (Optional[QuotasPurgePurgeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas/{id_}/purge"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover

    async def quotas_purge_purge_2_2(
        self,
        id_: str,
        run_as: QuotasPurgePurgeParamRunAs | None = None,
    ) -> str:
        """
        Purges a previously deleted quota.

        Args:
            id (str)                 : The ID of the Quota.
            run-as (Optional[QuotasPurgePurgeParamRunAs])
                                     : The user ID that will be used to effectively make this
                                       API call. Only admins and designated users can make API
                                       calls on behalf of other users.

        Returns:
            str: Successful Response

        Raises:
            HttpError:
                HTTPError: If the server returns a non-2xx HTTP response.
        """
        url = f"{self.base_url}/api/quotas/{id_}/purge"

        headers: dict[str, Any] = {
            **({"run-as": run_as} if run_as is not None else {}),
        }

        response = await self._transport.request("POST", url, params=None, json=None, data=None, headers=headers)

        # Check response status code and handle accordingly
        match response.status_code:
            case 200:
                return response.text
            case _:
                raise HTTPError(response=response, message="Unhandled status code", status_code=response.status_code)
        # All paths above should return or raise - this should never execute
        assert False, "Unexpected code path"  # pragma: no cover
