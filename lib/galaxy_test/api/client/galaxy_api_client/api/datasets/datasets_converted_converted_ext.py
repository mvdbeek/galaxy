from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.hda_custom import HDACustom
from ...models.hda_detailed import HDADetailed
from ...models.hda_inaccessible import HDAInaccessible
from ...models.hda_summary import HDASummary
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    dataset_id: str,
    ext: str,
    *,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_view: None | str | Unset
    if isinstance(view, Unset):
        json_view = UNSET
    else:
        json_view = view
    params["view"] = json_view

    json_keys: None | str | Unset
    if isinstance(keys, Unset):
        json_keys = UNSET
    else:
        json_keys = keys
    params["keys"] = json_keys

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/datasets/{dataset_id}/converted/{ext}".format(
            dataset_id=quote(str(dataset_id), safe=""),
            ext=quote(str(ext), safe=""),
        ),
        "params": params,
    }

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HDACustom | HDADetailed | HDAInaccessible | HDASummary | MessageExceptionModel | None:
    if response.status_code == 200:

        def _parse_response_200(data: object) -> HDACustom | HDADetailed | HDAInaccessible | HDASummary:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_0 = HDACustom.from_dict(data)

                return response_200_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_1 = HDADetailed.from_dict(data)

                return response_200_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_2 = HDASummary.from_dict(data)

                return response_200_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_200_type_3 = HDAInaccessible.from_dict(data)

            return response_200_type_3

        response_200 = _parse_response_200(response.json())

        return response_200

    if 400 <= response.status_code <= 499:
        response_4xx = MessageExceptionModel.from_dict(response.json())

        return response_4xx

    if 500 <= response.status_code <= 599:
        response_5xx = MessageExceptionModel.from_dict(response.json())

        return response_5xx

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HDACustom | HDADetailed | HDAInaccessible | HDASummary | MessageExceptionModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    dataset_id: str,
    ext: str,
    *,
    client: AuthenticatedClient,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[HDACustom | HDADetailed | HDAInaccessible | HDASummary | MessageExceptionModel]:
    """Return information about datasets made by converting this dataset to a new format.

     Return information about datasets made by converting this dataset to a new format.

    If there is no existing converted dataset for the format in `ext`, one will be created.

    **Note**: `view` and `keys` are also available to control the serialization of the dataset.

    Args:
        dataset_id (str):  Example: 0123456789ABCDEF.
        ext (str): File extension of the new format to convert this dataset to.
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HDACustom | HDADetailed | HDAInaccessible | HDASummary | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        ext=ext,
        view=view,
        keys=keys,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    dataset_id: str,
    ext: str,
    *,
    client: AuthenticatedClient,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> HDACustom | HDADetailed | HDAInaccessible | HDASummary | MessageExceptionModel | None:
    """Return information about datasets made by converting this dataset to a new format.

     Return information about datasets made by converting this dataset to a new format.

    If there is no existing converted dataset for the format in `ext`, one will be created.

    **Note**: `view` and `keys` are also available to control the serialization of the dataset.

    Args:
        dataset_id (str):  Example: 0123456789ABCDEF.
        ext (str): File extension of the new format to convert this dataset to.
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HDACustom | HDADetailed | HDAInaccessible | HDASummary | MessageExceptionModel
    """

    return sync_detailed(
        dataset_id=dataset_id,
        ext=ext,
        client=client,
        view=view,
        keys=keys,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    dataset_id: str,
    ext: str,
    *,
    client: AuthenticatedClient,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[HDACustom | HDADetailed | HDAInaccessible | HDASummary | MessageExceptionModel]:
    """Return information about datasets made by converting this dataset to a new format.

     Return information about datasets made by converting this dataset to a new format.

    If there is no existing converted dataset for the format in `ext`, one will be created.

    **Note**: `view` and `keys` are also available to control the serialization of the dataset.

    Args:
        dataset_id (str):  Example: 0123456789ABCDEF.
        ext (str): File extension of the new format to convert this dataset to.
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HDACustom | HDADetailed | HDAInaccessible | HDASummary | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        dataset_id=dataset_id,
        ext=ext,
        view=view,
        keys=keys,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    dataset_id: str,
    ext: str,
    *,
    client: AuthenticatedClient,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> HDACustom | HDADetailed | HDAInaccessible | HDASummary | MessageExceptionModel | None:
    """Return information about datasets made by converting this dataset to a new format.

     Return information about datasets made by converting this dataset to a new format.

    If there is no existing converted dataset for the format in `ext`, one will be created.

    **Note**: `view` and `keys` are also available to control the serialization of the dataset.

    Args:
        dataset_id (str):  Example: 0123456789ABCDEF.
        ext (str): File extension of the new format to convert this dataset to.
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HDACustom | HDADetailed | HDAInaccessible | HDASummary | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            dataset_id=dataset_id,
            ext=ext,
            client=client,
            view=view,
            keys=keys,
            run_as=run_as,
        )
    ).parsed
