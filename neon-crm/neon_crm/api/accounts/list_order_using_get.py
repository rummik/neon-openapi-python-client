from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_order_using_get_sort_column import ListOrderUsingGETSortColumn
from ...models.list_order_using_get_sort_direction import ListOrderUsingGETSortDirection
from ...models.list_order_using_get_transaction_types_item import ListOrderUsingGETTransactionTypesItem
from ...models.order_list_response import OrderListResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    current_page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    sort_column: Union[Unset, ListOrderUsingGETSortColumn] = ListOrderUsingGETSortColumn.DATE,
    sort_direction: Union[Unset, ListOrderUsingGETSortDirection] = ListOrderUsingGETSortDirection.DESC,
    transaction_types: Union[Unset, list[ListOrderUsingGETTransactionTypesItem]] = UNSET,
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

    json_transaction_types: Union[Unset, list[str]] = UNSET
    if not isinstance(transaction_types, Unset):
        json_transaction_types = []
        for transaction_types_item_data in transaction_types:
            transaction_types_item = transaction_types_item_data.value
            json_transaction_types.append(transaction_types_item)

    params["transactionTypes"] = json_transaction_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/accounts/{id}/orders",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, OrderListResponse]]:
    if response.status_code == 200:
        response_200 = OrderListResponse.from_dict(response.json())

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
) -> Response[Union[Any, OrderListResponse]]:
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
    sort_column: Union[Unset, ListOrderUsingGETSortColumn] = ListOrderUsingGETSortColumn.DATE,
    sort_direction: Union[Unset, ListOrderUsingGETSortDirection] = ListOrderUsingGETSortDirection.DESC,
    transaction_types: Union[Unset, list[ListOrderUsingGETTransactionTypesItem]] = UNSET,
) -> Response[Union[Any, OrderListResponse]]:
    """Get an account's order history

    Args:
        id (str):
        current_page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        sort_column (Union[Unset, ListOrderUsingGETSortColumn]):  Default:
            ListOrderUsingGETSortColumn.DATE.
        sort_direction (Union[Unset, ListOrderUsingGETSortDirection]):  Default:
            ListOrderUsingGETSortDirection.DESC.
        transaction_types (Union[Unset, list[ListOrderUsingGETTransactionTypesItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OrderListResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        current_page=current_page,
        page_size=page_size,
        sort_column=sort_column,
        sort_direction=sort_direction,
        transaction_types=transaction_types,
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
    sort_column: Union[Unset, ListOrderUsingGETSortColumn] = ListOrderUsingGETSortColumn.DATE,
    sort_direction: Union[Unset, ListOrderUsingGETSortDirection] = ListOrderUsingGETSortDirection.DESC,
    transaction_types: Union[Unset, list[ListOrderUsingGETTransactionTypesItem]] = UNSET,
) -> Optional[Union[Any, OrderListResponse]]:
    """Get an account's order history

    Args:
        id (str):
        current_page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        sort_column (Union[Unset, ListOrderUsingGETSortColumn]):  Default:
            ListOrderUsingGETSortColumn.DATE.
        sort_direction (Union[Unset, ListOrderUsingGETSortDirection]):  Default:
            ListOrderUsingGETSortDirection.DESC.
        transaction_types (Union[Unset, list[ListOrderUsingGETTransactionTypesItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, OrderListResponse]
    """

    return sync_detailed(
        id=id,
        client=client,
        current_page=current_page,
        page_size=page_size,
        sort_column=sort_column,
        sort_direction=sort_direction,
        transaction_types=transaction_types,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    sort_column: Union[Unset, ListOrderUsingGETSortColumn] = ListOrderUsingGETSortColumn.DATE,
    sort_direction: Union[Unset, ListOrderUsingGETSortDirection] = ListOrderUsingGETSortDirection.DESC,
    transaction_types: Union[Unset, list[ListOrderUsingGETTransactionTypesItem]] = UNSET,
) -> Response[Union[Any, OrderListResponse]]:
    """Get an account's order history

    Args:
        id (str):
        current_page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        sort_column (Union[Unset, ListOrderUsingGETSortColumn]):  Default:
            ListOrderUsingGETSortColumn.DATE.
        sort_direction (Union[Unset, ListOrderUsingGETSortDirection]):  Default:
            ListOrderUsingGETSortDirection.DESC.
        transaction_types (Union[Unset, list[ListOrderUsingGETTransactionTypesItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OrderListResponse]]
    """

    kwargs = _get_kwargs(
        id=id,
        current_page=current_page,
        page_size=page_size,
        sort_column=sort_column,
        sort_direction=sort_direction,
        transaction_types=transaction_types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    sort_column: Union[Unset, ListOrderUsingGETSortColumn] = ListOrderUsingGETSortColumn.DATE,
    sort_direction: Union[Unset, ListOrderUsingGETSortDirection] = ListOrderUsingGETSortDirection.DESC,
    transaction_types: Union[Unset, list[ListOrderUsingGETTransactionTypesItem]] = UNSET,
) -> Optional[Union[Any, OrderListResponse]]:
    """Get an account's order history

    Args:
        id (str):
        current_page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        sort_column (Union[Unset, ListOrderUsingGETSortColumn]):  Default:
            ListOrderUsingGETSortColumn.DATE.
        sort_direction (Union[Unset, ListOrderUsingGETSortDirection]):  Default:
            ListOrderUsingGETSortDirection.DESC.
        transaction_types (Union[Unset, list[ListOrderUsingGETTransactionTypesItem]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, OrderListResponse]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            current_page=current_page,
            page_size=page_size,
            sort_column=sort_column,
            sort_direction=sort_direction,
            transaction_types=transaction_types,
        )
    ).parsed
