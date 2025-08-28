from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_event_registrations_using_get1_sort_direction import GetEventRegistrationsUsingGET1SortDirection
from ...models.get_event_registrations_using_get1_sort_field import GetEventRegistrationsUsingGET1SortField
from ...models.pagination_event_registration import PaginationEventRegistration
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    registrant_account_id: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, GetEventRegistrationsUsingGET1SortDirection] = UNSET,
    sort_field: Union[Unset, GetEventRegistrationsUsingGET1SortField] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["page"] = page

    params["pageSize"] = page_size

    params["registrantAccountId"] = registrant_account_id

    json_sort_direction: Union[Unset, str] = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sortDirection"] = json_sort_direction

    json_sort_field: Union[Unset, str] = UNSET
    if not isinstance(sort_field, Unset):
        json_sort_field = sort_field.value

    params["sortField"] = json_sort_field

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/events/{id}/eventRegistrations",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PaginationEventRegistration]]:
    if response.status_code == 200:
        response_200 = PaginationEventRegistration.from_dict(response.json())

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
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    registrant_account_id: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, GetEventRegistrationsUsingGET1SortDirection] = UNSET,
    sort_field: Union[Unset, GetEventRegistrationsUsingGET1SortField] = UNSET,
) -> Response[Union[Any, PaginationEventRegistration]]:
    """Get a list of event registrations for this event

    Args:
        id (str):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        registrant_account_id (Union[Unset, str]):
        sort_direction (Union[Unset, GetEventRegistrationsUsingGET1SortDirection]):
        sort_field (Union[Unset, GetEventRegistrationsUsingGET1SortField]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginationEventRegistration]]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
        page_size=page_size,
        registrant_account_id=registrant_account_id,
        sort_direction=sort_direction,
        sort_field=sort_field,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    registrant_account_id: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, GetEventRegistrationsUsingGET1SortDirection] = UNSET,
    sort_field: Union[Unset, GetEventRegistrationsUsingGET1SortField] = UNSET,
) -> Optional[Union[Any, PaginationEventRegistration]]:
    """Get a list of event registrations for this event

    Args:
        id (str):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        registrant_account_id (Union[Unset, str]):
        sort_direction (Union[Unset, GetEventRegistrationsUsingGET1SortDirection]):
        sort_field (Union[Unset, GetEventRegistrationsUsingGET1SortField]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PaginationEventRegistration]
    """

    return sync_detailed(
        id=id,
        client=client,
        page=page,
        page_size=page_size,
        registrant_account_id=registrant_account_id,
        sort_direction=sort_direction,
        sort_field=sort_field,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    registrant_account_id: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, GetEventRegistrationsUsingGET1SortDirection] = UNSET,
    sort_field: Union[Unset, GetEventRegistrationsUsingGET1SortField] = UNSET,
) -> Response[Union[Any, PaginationEventRegistration]]:
    """Get a list of event registrations for this event

    Args:
        id (str):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        registrant_account_id (Union[Unset, str]):
        sort_direction (Union[Unset, GetEventRegistrationsUsingGET1SortDirection]):
        sort_field (Union[Unset, GetEventRegistrationsUsingGET1SortField]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PaginationEventRegistration]]
    """

    kwargs = _get_kwargs(
        id=id,
        page=page,
        page_size=page_size,
        registrant_account_id=registrant_account_id,
        sort_direction=sort_direction,
        sort_field=sort_field,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    registrant_account_id: Union[Unset, str] = UNSET,
    sort_direction: Union[Unset, GetEventRegistrationsUsingGET1SortDirection] = UNSET,
    sort_field: Union[Unset, GetEventRegistrationsUsingGET1SortField] = UNSET,
) -> Optional[Union[Any, PaginationEventRegistration]]:
    """Get a list of event registrations for this event

    Args:
        id (str):
        page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        registrant_account_id (Union[Unset, str]):
        sort_direction (Union[Unset, GetEventRegistrationsUsingGET1SortDirection]):
        sort_field (Union[Unset, GetEventRegistrationsUsingGET1SortField]):

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
            page=page,
            page_size=page_size,
            registrant_account_id=registrant_account_id,
            sort_direction=sort_direction,
            sort_field=sort_field,
        )
    ).parsed
