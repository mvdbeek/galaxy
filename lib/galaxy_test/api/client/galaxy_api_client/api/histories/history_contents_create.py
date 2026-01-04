from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_history_content_payload import CreateHistoryContentPayload
from ...models.hda_custom import HDACustom
from ...models.hda_detailed import HDADetailed
from ...models.hda_inaccessible import HDAInaccessible
from ...models.hda_summary import HDASummary
from ...models.hdca_custom import HDCACustom
from ...models.hdca_detailed import HDCADetailed
from ...models.hdca_summary import HDCASummary
from ...models.history_content_type import HistoryContentType
from ...models.message_exception_model import MessageExceptionModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    history_id: str,
    *,
    body: CreateHistoryContentPayload,
    type_: HistoryContentType | None | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    if not isinstance(run_as, Unset):
        headers["run-as"] = run_as

    params: dict[str, Any] = {}

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    elif isinstance(type_, HistoryContentType):
        json_type_ = type_.value
    else:
        json_type_ = type_
    params["type"] = json_type_

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
        "method": "post",
        "url": "/api/histories/{history_id}/contents".format(
            history_id=quote(str(history_id), safe=""),
        ),
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    HDACustom
    | HDADetailed
    | HDAInaccessible
    | HDASummary
    | HDCACustom
    | HDCADetailed
    | HDCASummary
    | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
    | MessageExceptionModel
    | None
):
    if response.status_code == 200:

        def _parse_response_200(
            data: object,
        ) -> (
            HDACustom
            | HDADetailed
            | HDAInaccessible
            | HDASummary
            | HDCACustom
            | HDCADetailed
            | HDCASummary
            | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
        ):
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
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_3 = HDAInaccessible.from_dict(data)

                return response_200_type_3
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_4 = HDCACustom.from_dict(data)

                return response_200_type_4
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_5 = HDCADetailed.from_dict(data)

                return response_200_type_5
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                response_200_type_6 = HDCASummary.from_dict(data)

                return response_200_type_6
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, list):
                raise TypeError()
            response_200_type_7 = []
            _response_200_type_7 = data
            for response_200_type_7_item_data in _response_200_type_7:

                def _parse_response_200_type_7_item(
                    data: object,
                ) -> HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary:
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        response_200_type_7_item_type_0 = HDACustom.from_dict(data)

                        return response_200_type_7_item_type_0
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        response_200_type_7_item_type_1 = HDADetailed.from_dict(data)

                        return response_200_type_7_item_type_1
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        response_200_type_7_item_type_2 = HDASummary.from_dict(data)

                        return response_200_type_7_item_type_2
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        response_200_type_7_item_type_3 = HDAInaccessible.from_dict(data)

                        return response_200_type_7_item_type_3
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        response_200_type_7_item_type_4 = HDCACustom.from_dict(data)

                        return response_200_type_7_item_type_4
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    try:
                        if not isinstance(data, dict):
                            raise TypeError()
                        response_200_type_7_item_type_5 = HDCADetailed.from_dict(data)

                        return response_200_type_7_item_type_5
                    except (TypeError, ValueError, AttributeError, KeyError):
                        pass
                    if not isinstance(data, dict):
                        raise TypeError()
                    response_200_type_7_item_type_6 = HDCASummary.from_dict(data)

                    return response_200_type_7_item_type_6

                response_200_type_7_item = _parse_response_200_type_7_item(response_200_type_7_item_data)

                response_200_type_7.append(response_200_type_7_item)

            return response_200_type_7

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
) -> Response[
    HDACustom
    | HDADetailed
    | HDAInaccessible
    | HDASummary
    | HDCACustom
    | HDCADetailed
    | HDCASummary
    | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
    | MessageExceptionModel
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateHistoryContentPayload,
    type_: HistoryContentType | None | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[
    HDACustom
    | HDADetailed
    | HDAInaccessible
    | HDASummary
    | HDCACustom
    | HDCADetailed
    | HDCASummary
    | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
    | MessageExceptionModel
]:
    """Create a new `HDA` or `HDCA` in the given History.

     Create a new `HDA` or `HDCA` in the given History.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType | None | Unset): The type of the target history element.
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (CreateHistoryContentPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary] | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        body=body,
        type_=type_,
        view=view,
        keys=keys,
        run_as=run_as,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    history_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateHistoryContentPayload,
    type_: HistoryContentType | None | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> (
    HDACustom
    | HDADetailed
    | HDAInaccessible
    | HDASummary
    | HDCACustom
    | HDCADetailed
    | HDCASummary
    | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
    | MessageExceptionModel
    | None
):
    """Create a new `HDA` or `HDCA` in the given History.

     Create a new `HDA` or `HDCA` in the given History.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType | None | Unset): The type of the target history element.
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (CreateHistoryContentPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary] | MessageExceptionModel
    """

    return sync_detailed(
        history_id=history_id,
        client=client,
        body=body,
        type_=type_,
        view=view,
        keys=keys,
        run_as=run_as,
    ).parsed


async def asyncio_detailed(
    history_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateHistoryContentPayload,
    type_: HistoryContentType | None | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> Response[
    HDACustom
    | HDADetailed
    | HDAInaccessible
    | HDASummary
    | HDCACustom
    | HDCADetailed
    | HDCASummary
    | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
    | MessageExceptionModel
]:
    """Create a new `HDA` or `HDCA` in the given History.

     Create a new `HDA` or `HDCA` in the given History.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType | None | Unset): The type of the target history element.
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (CreateHistoryContentPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary] | MessageExceptionModel]
    """

    kwargs = _get_kwargs(
        history_id=history_id,
        body=body,
        type_=type_,
        view=view,
        keys=keys,
        run_as=run_as,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    history_id: str,
    *,
    client: AuthenticatedClient,
    body: CreateHistoryContentPayload,
    type_: HistoryContentType | None | Unset = UNSET,
    view: None | str | Unset = UNSET,
    keys: None | str | Unset = UNSET,
    run_as: None | str | Unset = UNSET,
) -> (
    HDACustom
    | HDADetailed
    | HDAInaccessible
    | HDASummary
    | HDCACustom
    | HDCADetailed
    | HDCASummary
    | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary]
    | MessageExceptionModel
    | None
):
    """Create a new `HDA` or `HDCA` in the given History.

     Create a new `HDA` or `HDCA` in the given History.

    Args:
        history_id (str):  Example: 0123456789ABCDEF.
        type_ (HistoryContentType | None | Unset): The type of the target history element.
        view (None | str | Unset): View to be passed to the serializer
        keys (None | str | Unset): Comma-separated list of keys to be passed to the serializer
        run_as (None | str | Unset): The user ID that will be used to effectively make this API
            call. Only admins and designated users can make API calls on behalf of other users.
        body (CreateHistoryContentPayload):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary | list[HDACustom | HDADetailed | HDAInaccessible | HDASummary | HDCACustom | HDCADetailed | HDCASummary] | MessageExceptionModel
    """

    return (
        await asyncio_detailed(
            history_id=history_id,
            client=client,
            body=body,
            type_=type_,
            view=view,
            keys=keys,
            run_as=run_as,
        )
    ).parsed
