from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_membership_using_get_sort_column import ListMembershipUsingGETSortColumn
from ...models.list_membership_using_get_sort_direction import ListMembershipUsingGETSortDirection
from ...models.membership_list_response import MembershipListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    current_page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    sort_column: Union[Unset, ListMembershipUsingGETSortColumn] = ListMembershipUsingGETSortColumn.DATE,
    sort_direction: Union[Unset, ListMembershipUsingGETSortDirection] = ListMembershipUsingGETSortDirection.DESC,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["currentPage"] = current_page

    params["pageSize"] = page_size

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
        "url": f"/accounts/{id}/memberships",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, MembershipListResponse]]:
    if response.status_code == 200:
        response_200 = MembershipListResponse.from_dict(response.json())

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
) -> Response[Union[Any, MembershipListResponse]]:
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
    page_size: Union[Unset, int] = UNSET,
    sort_column: Union[Unset, ListMembershipUsingGETSortColumn] = ListMembershipUsingGETSortColumn.DATE,
    sort_direction: Union[Unset, ListMembershipUsingGETSortDirection] = ListMembershipUsingGETSortDirection.DESC,
) -> Response[Union[Any, MembershipListResponse]]:
    """Get an account's membership history

    Args:
        id (str):
        current_page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        sort_column (Union[Unset, ListMembershipUsingGETSortColumn]):  Default:
            ListMembershipUsingGETSortColumn.DATE.
        sort_direction (Union[Unset, ListMembershipUsingGETSortDirection]):  Default:
            ListMembershipUsingGETSortDirection.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MembershipListResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        current_page=current_page,
        page_size=page_size,
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
    page_size: Union[Unset, int] = UNSET,
    sort_column: Union[Unset, ListMembershipUsingGETSortColumn] = ListMembershipUsingGETSortColumn.DATE,
    sort_direction: Union[Unset, ListMembershipUsingGETSortDirection] = ListMembershipUsingGETSortDirection.DESC,
) -> Optional[Union[Any, MembershipListResponse]]:
    """Get an account's membership history

    Args:
        id (str):
        current_page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        sort_column (Union[Unset, ListMembershipUsingGETSortColumn]):  Default:
            ListMembershipUsingGETSortColumn.DATE.
        sort_direction (Union[Unset, ListMembershipUsingGETSortDirection]):  Default:
            ListMembershipUsingGETSortDirection.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MembershipListResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        current_page=current_page,
        page_size=page_size,
        sort_column=sort_column,
        sort_direction=sort_direction,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    sort_column: Union[Unset, ListMembershipUsingGETSortColumn] = ListMembershipUsingGETSortColumn.DATE,
    sort_direction: Union[Unset, ListMembershipUsingGETSortDirection] = ListMembershipUsingGETSortDirection.DESC,
) -> Response[Union[Any, MembershipListResponse]]:
    """Get an account's membership history

    Args:
        id (str):
        current_page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        sort_column (Union[Unset, ListMembershipUsingGETSortColumn]):  Default:
            ListMembershipUsingGETSortColumn.DATE.
        sort_direction (Union[Unset, ListMembershipUsingGETSortDirection]):  Default:
            ListMembershipUsingGETSortDirection.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, MembershipListResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        current_page=current_page,
        page_size=page_size,
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
    page_size: Union[Unset, int] = UNSET,
    sort_column: Union[Unset, ListMembershipUsingGETSortColumn] = ListMembershipUsingGETSortColumn.DATE,
    sort_direction: Union[Unset, ListMembershipUsingGETSortDirection] = ListMembershipUsingGETSortDirection.DESC,
) -> Optional[Union[Any, MembershipListResponse]]:
    """Get an account's membership history

    Args:
        id (str):
        current_page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        sort_column (Union[Unset, ListMembershipUsingGETSortColumn]):  Default:
            ListMembershipUsingGETSortColumn.DATE.
        sort_direction (Union[Unset, ListMembershipUsingGETSortDirection]):  Default:
            ListMembershipUsingGETSortDirection.DESC.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, MembershipListResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            current_page=current_page,
            page_size=page_size,
            sort_column=sort_column,
            sort_direction=sort_direction,
        )
    ).parsed
