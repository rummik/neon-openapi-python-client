from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_attendees import EventAttendees
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    current_page: Union[Unset, int] = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["currentPage"] = current_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/events/{id}/attendees",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, EventAttendees]]:
    if response.status_code == 200:
        response_200 = EventAttendees.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, EventAttendees]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = 0,
) -> Response[Union[Any, EventAttendees]]:
    """Get a list of attendees for an event

    Args:
        id (str):
        current_page (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventAttendees]]
    """

    kwargs = _get_kwargs(
        id=id,
        current_page=current_page,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = 0,
) -> Optional[Union[Any, EventAttendees]]:
    """Get a list of attendees for an event

    Args:
        id (str):
        current_page (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventAttendees]
    """

    return sync_detailed(
        id=id,
        client=client,
        current_page=current_page,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = 0,
) -> Response[Union[Any, EventAttendees]]:
    """Get a list of attendees for an event

    Args:
        id (str):
        current_page (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventAttendees]]
    """

    kwargs = _get_kwargs(
        id=id,
        current_page=current_page,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = 0,
) -> Optional[Union[Any, EventAttendees]]:
    """Get a list of attendees for an event

    Args:
        id (str):
        current_page (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventAttendees]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            current_page=current_page,
        )
    ).parsed
