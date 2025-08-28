from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_recurring_using_get_sort_column import ListRecurringUsingGETSortColumn
from ...models.list_recurring_using_get_sort_direction import ListRecurringUsingGETSortDirection
from ...models.list_recurring_using_get_status import ListRecurringUsingGETStatus
from ...models.recurring_donations_response import RecurringDonationsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    account_id: Union[Unset, str] = UNSET,
    card_expiration_from: Union[Unset, str] = UNSET,
    card_expiration_to: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    next_recurring_from: Union[Unset, str] = UNSET,
    next_recurring_to: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    setup_date_from: Union[Unset, str] = UNSET,
    setup_date_to: Union[Unset, str] = UNSET,
    sort_column: Union[Unset, ListRecurringUsingGETSortColumn] = UNSET,
    sort_direction: Union[Unset, ListRecurringUsingGETSortDirection] = UNSET,
    status: Union[Unset, ListRecurringUsingGETStatus] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["accountId"] = account_id

    params["cardExpirationFrom"] = card_expiration_from

    params["cardExpirationTo"] = card_expiration_to

    params["currentPage"] = current_page

    params["nextRecurringFrom"] = next_recurring_from

    params["nextRecurringTo"] = next_recurring_to

    params["pageSize"] = page_size

    params["setupDateFrom"] = setup_date_from

    params["setupDateTo"] = setup_date_to

    json_sort_column: Union[Unset, str] = UNSET
    if not isinstance(sort_column, Unset):
        json_sort_column = sort_column.value

    params["sortColumn"] = json_sort_column

    json_sort_direction: Union[Unset, str] = UNSET
    if not isinstance(sort_direction, Unset):
        json_sort_direction = sort_direction.value

    params["sortDirection"] = json_sort_direction

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/recurring",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, RecurringDonationsResponse]]:
    if response.status_code == 200:
        response_200 = RecurringDonationsResponse.from_dict(response.json())

        return response_200
    if response.status_code == 222:
        response_222 = RecurringDonationsResponse.from_dict(response.json())

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
) -> Response[Union[Any, RecurringDonationsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    account_id: Union[Unset, str] = UNSET,
    card_expiration_from: Union[Unset, str] = UNSET,
    card_expiration_to: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    next_recurring_from: Union[Unset, str] = UNSET,
    next_recurring_to: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    setup_date_from: Union[Unset, str] = UNSET,
    setup_date_to: Union[Unset, str] = UNSET,
    sort_column: Union[Unset, ListRecurringUsingGETSortColumn] = UNSET,
    sort_direction: Union[Unset, ListRecurringUsingGETSortDirection] = UNSET,
    status: Union[Unset, ListRecurringUsingGETStatus] = UNSET,
) -> Response[Union[Any, RecurringDonationsResponse]]:
    """Gets a list of recurring donation schedules

    Args:
        account_id (Union[Unset, str]):
        card_expiration_from (Union[Unset, str]):
        card_expiration_to (Union[Unset, str]):
        current_page (Union[Unset, int]):
        next_recurring_from (Union[Unset, str]):
        next_recurring_to (Union[Unset, str]):
        page_size (Union[Unset, int]):
        setup_date_from (Union[Unset, str]):
        setup_date_to (Union[Unset, str]):
        sort_column (Union[Unset, ListRecurringUsingGETSortColumn]):
        sort_direction (Union[Unset, ListRecurringUsingGETSortDirection]):
        status (Union[Unset, ListRecurringUsingGETStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RecurringDonationsResponse]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        card_expiration_from=card_expiration_from,
        card_expiration_to=card_expiration_to,
        current_page=current_page,
        next_recurring_from=next_recurring_from,
        next_recurring_to=next_recurring_to,
        page_size=page_size,
        setup_date_from=setup_date_from,
        setup_date_to=setup_date_to,
        sort_column=sort_column,
        sort_direction=sort_direction,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    account_id: Union[Unset, str] = UNSET,
    card_expiration_from: Union[Unset, str] = UNSET,
    card_expiration_to: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    next_recurring_from: Union[Unset, str] = UNSET,
    next_recurring_to: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    setup_date_from: Union[Unset, str] = UNSET,
    setup_date_to: Union[Unset, str] = UNSET,
    sort_column: Union[Unset, ListRecurringUsingGETSortColumn] = UNSET,
    sort_direction: Union[Unset, ListRecurringUsingGETSortDirection] = UNSET,
    status: Union[Unset, ListRecurringUsingGETStatus] = UNSET,
) -> Optional[Union[Any, RecurringDonationsResponse]]:
    """Gets a list of recurring donation schedules

    Args:
        account_id (Union[Unset, str]):
        card_expiration_from (Union[Unset, str]):
        card_expiration_to (Union[Unset, str]):
        current_page (Union[Unset, int]):
        next_recurring_from (Union[Unset, str]):
        next_recurring_to (Union[Unset, str]):
        page_size (Union[Unset, int]):
        setup_date_from (Union[Unset, str]):
        setup_date_to (Union[Unset, str]):
        sort_column (Union[Unset, ListRecurringUsingGETSortColumn]):
        sort_direction (Union[Unset, ListRecurringUsingGETSortDirection]):
        status (Union[Unset, ListRecurringUsingGETStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RecurringDonationsResponse]
    """

    return sync_detailed(
        client=client,
        account_id=account_id,
        card_expiration_from=card_expiration_from,
        card_expiration_to=card_expiration_to,
        current_page=current_page,
        next_recurring_from=next_recurring_from,
        next_recurring_to=next_recurring_to,
        page_size=page_size,
        setup_date_from=setup_date_from,
        setup_date_to=setup_date_to,
        sort_column=sort_column,
        sort_direction=sort_direction,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    account_id: Union[Unset, str] = UNSET,
    card_expiration_from: Union[Unset, str] = UNSET,
    card_expiration_to: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    next_recurring_from: Union[Unset, str] = UNSET,
    next_recurring_to: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    setup_date_from: Union[Unset, str] = UNSET,
    setup_date_to: Union[Unset, str] = UNSET,
    sort_column: Union[Unset, ListRecurringUsingGETSortColumn] = UNSET,
    sort_direction: Union[Unset, ListRecurringUsingGETSortDirection] = UNSET,
    status: Union[Unset, ListRecurringUsingGETStatus] = UNSET,
) -> Response[Union[Any, RecurringDonationsResponse]]:
    """Gets a list of recurring donation schedules

    Args:
        account_id (Union[Unset, str]):
        card_expiration_from (Union[Unset, str]):
        card_expiration_to (Union[Unset, str]):
        current_page (Union[Unset, int]):
        next_recurring_from (Union[Unset, str]):
        next_recurring_to (Union[Unset, str]):
        page_size (Union[Unset, int]):
        setup_date_from (Union[Unset, str]):
        setup_date_to (Union[Unset, str]):
        sort_column (Union[Unset, ListRecurringUsingGETSortColumn]):
        sort_direction (Union[Unset, ListRecurringUsingGETSortDirection]):
        status (Union[Unset, ListRecurringUsingGETStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RecurringDonationsResponse]]
    """

    kwargs = _get_kwargs(
        account_id=account_id,
        card_expiration_from=card_expiration_from,
        card_expiration_to=card_expiration_to,
        current_page=current_page,
        next_recurring_from=next_recurring_from,
        next_recurring_to=next_recurring_to,
        page_size=page_size,
        setup_date_from=setup_date_from,
        setup_date_to=setup_date_to,
        sort_column=sort_column,
        sort_direction=sort_direction,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    account_id: Union[Unset, str] = UNSET,
    card_expiration_from: Union[Unset, str] = UNSET,
    card_expiration_to: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    next_recurring_from: Union[Unset, str] = UNSET,
    next_recurring_to: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    setup_date_from: Union[Unset, str] = UNSET,
    setup_date_to: Union[Unset, str] = UNSET,
    sort_column: Union[Unset, ListRecurringUsingGETSortColumn] = UNSET,
    sort_direction: Union[Unset, ListRecurringUsingGETSortDirection] = UNSET,
    status: Union[Unset, ListRecurringUsingGETStatus] = UNSET,
) -> Optional[Union[Any, RecurringDonationsResponse]]:
    """Gets a list of recurring donation schedules

    Args:
        account_id (Union[Unset, str]):
        card_expiration_from (Union[Unset, str]):
        card_expiration_to (Union[Unset, str]):
        current_page (Union[Unset, int]):
        next_recurring_from (Union[Unset, str]):
        next_recurring_to (Union[Unset, str]):
        page_size (Union[Unset, int]):
        setup_date_from (Union[Unset, str]):
        setup_date_to (Union[Unset, str]):
        sort_column (Union[Unset, ListRecurringUsingGETSortColumn]):
        sort_direction (Union[Unset, ListRecurringUsingGETSortDirection]):
        status (Union[Unset, ListRecurringUsingGETStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RecurringDonationsResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            account_id=account_id,
            card_expiration_from=card_expiration_from,
            card_expiration_to=card_expiration_to,
            current_page=current_page,
            next_recurring_from=next_recurring_from,
            next_recurring_to=next_recurring_to,
            page_size=page_size,
            setup_date_from=setup_date_from,
            setup_date_to=setup_date_to,
            sort_column=sort_column,
            sort_direction=sort_direction,
            status=status,
        )
    ).parsed
