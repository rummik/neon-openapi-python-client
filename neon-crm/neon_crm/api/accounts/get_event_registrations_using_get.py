from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_event_registrations_using_get_sort_column import GetEventRegistrationsUsingGETSortColumn
from ...models.get_event_registrations_using_get_sort_direction import GetEventRegistrationsUsingGETSortDirection
from ...models.pagination_event_registration import PaginationEventRegistration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    current_page: Union[Unset, int] = UNSET,
    event_id: Union[Unset, str] = UNSET,
    sort_column: Union[Unset, GetEventRegistrationsUsingGETSortColumn] = UNSET,
    sort_direction: Union[Unset, GetEventRegistrationsUsingGETSortDirection] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["currentPage"] = current_page

    params["eventId"] = event_id

    json_sort_column: Union[Unset, str] = UNSET
    if not isinstance(sort_column, Unset):
        json_sort_column = sort_column.value

    params["sortColumn"] = json_sort_column

    json_sort_direction: Union[Unset, str] = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sortDirection"] = json_sort_direction

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{id}/eventRegistrations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PaginationEventRegistration]]:
    if response.status_code == 200:
        response_200 = PaginationEventRegistration.from_dict(response.json())

        return response_200
    if response.status_code == 222:
        response_222 = PaginationEventRegistration.from_dict(response.json())

        return response_222
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
) -> Response[Union[Any, PaginationEventRegistration]]:
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
    current_page: Union[Unset, int] = UNSET,
    event_id: Union[Unset, str] = UNSET,
    sort_column: Union[Unset, GetEventRegistrationsUsingGETSortColumn] = UNSET,
    sort_direction: Union[Unset, GetEventRegistrationsUsingGETSortDirection] = UNSET,
) -> Response[Union[Any, PaginationEventRegistration]]:
    """Gets a list of event registrations for this account

    Args:
        id (str):
        current_page (Union[Unset, int]):
        event_id (Union[Unset, str]):
        sort_column (Union[Unset, GetEventRegistrationsUsingGETSortColumn]):
        sort_direction (Union[Unset, GetEventRegistrationsUsingGETSortDirection]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginationEventRegistration]]
    """

    kwargs = _get_kwargs(
        id=id,
        current_page=current_page,
        event_id=event_id,
        sort_column=sort_column,
        sort_direction=sort_direction,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    event_id: Union[Unset, str] = UNSET,
    sort_column: Union[Unset, GetEventRegistrationsUsingGETSortColumn] = UNSET,
    sort_direction: Union[Unset, GetEventRegistrationsUsingGETSortDirection] = UNSET,
) -> Optional[Union[Any, PaginationEventRegistration]]:
    """Gets a list of event registrations for this account

    Args:
        id (str):
        current_page (Union[Unset, int]):
        event_id (Union[Unset, str]):
        sort_column (Union[Unset, GetEventRegistrationsUsingGETSortColumn]):
        sort_direction (Union[Unset, GetEventRegistrationsUsingGETSortDirection]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PaginationEventRegistration]
    """

    return sync_detailed(
        id=id,
        client=client,
        current_page=current_page,
        event_id=event_id,
        sort_column=sort_column,
        sort_direction=sort_direction,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    event_id: Union[Unset, str] = UNSET,
    sort_column: Union[Unset, GetEventRegistrationsUsingGETSortColumn] = UNSET,
    sort_direction: Union[Unset, GetEventRegistrationsUsingGETSortDirection] = UNSET,
) -> Response[Union[Any, PaginationEventRegistration]]:
    """Gets a list of event registrations for this account

    Args:
        id (str):
        current_page (Union[Unset, int]):
        event_id (Union[Unset, str]):
        sort_column (Union[Unset, GetEventRegistrationsUsingGETSortColumn]):
        sort_direction (Union[Unset, GetEventRegistrationsUsingGETSortDirection]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginationEventRegistration]]
    """

    kwargs = _get_kwargs(
        id=id,
        current_page=current_page,
        event_id=event_id,
        sort_column=sort_column,
        sort_direction=sort_direction,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    event_id: Union[Unset, str] = UNSET,
    sort_column: Union[Unset, GetEventRegistrationsUsingGETSortColumn] = UNSET,
    sort_direction: Union[Unset, GetEventRegistrationsUsingGETSortDirection] = UNSET,
) -> Optional[Union[Any, PaginationEventRegistration]]:
    """Gets a list of event registrations for this account

    Args:
        id (str):
        current_page (Union[Unset, int]):
        event_id (Union[Unset, str]):
        sort_column (Union[Unset, GetEventRegistrationsUsingGETSortColumn]):
        sort_direction (Union[Unset, GetEventRegistrationsUsingGETSortDirection]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PaginationEventRegistration]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            current_page=current_page,
            event_id=event_id,
            sort_column=sort_column,
            sort_direction=sort_direction,
        )
    ).parsed
