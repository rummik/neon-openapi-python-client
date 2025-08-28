import datetime
from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.event_search_result import EventSearchResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    archived: Union[Unset, bool] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    end_date_after: Union[Unset, datetime.datetime] = UNSET,
    end_date_before: Union[Unset, datetime.datetime] = UNSET,
    event_category: Union[Unset, int] = UNSET,
    event_id: Union[Unset, int] = UNSET,
    event_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    published_event: Union[Unset, bool] = UNSET,
    start_date_after: Union[Unset, datetime.datetime] = UNSET,
    start_date_before: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["archived"] = archived

    params["currentPage"] = current_page

    json_end_date_after: Union[Unset, str] = UNSET
    if not isinstance(end_date_after, Unset):
        json_end_date_after = end_date_after.isoformat()
    params["endDateAfter"] = json_end_date_after

    json_end_date_before: Union[Unset, str] = UNSET
    if not isinstance(end_date_before, Unset):
        json_end_date_before = end_date_before.isoformat()
    params["endDateBefore"] = json_end_date_before

    params["eventCategory"] = event_category

    params["eventId"] = event_id

    params["eventName"] = event_name

    params["pageSize"] = page_size

    params["publishedEvent"] = published_event

    json_start_date_after: Union[Unset, str] = UNSET
    if not isinstance(start_date_after, Unset):
        json_start_date_after = start_date_after.isoformat()
    params["startDateAfter"] = json_start_date_after

    json_start_date_before: Union[Unset, str] = UNSET
    if not isinstance(start_date_before, Unset):
        json_start_date_before = start_date_before.isoformat()
    params["startDateBefore"] = json_start_date_before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/events",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, EventSearchResult]]:
    if response.status_code == 200:
        response_200 = EventSearchResult.from_dict(response.json())

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
) -> Response[Union[Any, EventSearchResult]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    archived: Union[Unset, bool] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    end_date_after: Union[Unset, datetime.datetime] = UNSET,
    end_date_before: Union[Unset, datetime.datetime] = UNSET,
    event_category: Union[Unset, int] = UNSET,
    event_id: Union[Unset, int] = UNSET,
    event_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    published_event: Union[Unset, bool] = UNSET,
    start_date_after: Union[Unset, datetime.datetime] = UNSET,
    start_date_before: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[Any, EventSearchResult]]:
    """Gets a list of events

    Args:
        archived (Union[Unset, bool]):
        current_page (Union[Unset, int]):
        end_date_after (Union[Unset, datetime.datetime]):
        end_date_before (Union[Unset, datetime.datetime]):
        event_category (Union[Unset, int]):
        event_id (Union[Unset, int]):
        event_name (Union[Unset, str]):
        page_size (Union[Unset, int]):
        published_event (Union[Unset, bool]):
        start_date_after (Union[Unset, datetime.datetime]):
        start_date_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventSearchResult]]
    """

    kwargs = _get_kwargs(
        archived=archived,
        current_page=current_page,
        end_date_after=end_date_after,
        end_date_before=end_date_before,
        event_category=event_category,
        event_id=event_id,
        event_name=event_name,
        page_size=page_size,
        published_event=published_event,
        start_date_after=start_date_after,
        start_date_before=start_date_before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    archived: Union[Unset, bool] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    end_date_after: Union[Unset, datetime.datetime] = UNSET,
    end_date_before: Union[Unset, datetime.datetime] = UNSET,
    event_category: Union[Unset, int] = UNSET,
    event_id: Union[Unset, int] = UNSET,
    event_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    published_event: Union[Unset, bool] = UNSET,
    start_date_after: Union[Unset, datetime.datetime] = UNSET,
    start_date_before: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[Any, EventSearchResult]]:
    """Gets a list of events

    Args:
        archived (Union[Unset, bool]):
        current_page (Union[Unset, int]):
        end_date_after (Union[Unset, datetime.datetime]):
        end_date_before (Union[Unset, datetime.datetime]):
        event_category (Union[Unset, int]):
        event_id (Union[Unset, int]):
        event_name (Union[Unset, str]):
        page_size (Union[Unset, int]):
        published_event (Union[Unset, bool]):
        start_date_after (Union[Unset, datetime.datetime]):
        start_date_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventSearchResult]
    """

    return sync_detailed(
        client=client,
        archived=archived,
        current_page=current_page,
        end_date_after=end_date_after,
        end_date_before=end_date_before,
        event_category=event_category,
        event_id=event_id,
        event_name=event_name,
        page_size=page_size,
        published_event=published_event,
        start_date_after=start_date_after,
        start_date_before=start_date_before,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    archived: Union[Unset, bool] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    end_date_after: Union[Unset, datetime.datetime] = UNSET,
    end_date_before: Union[Unset, datetime.datetime] = UNSET,
    event_category: Union[Unset, int] = UNSET,
    event_id: Union[Unset, int] = UNSET,
    event_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    published_event: Union[Unset, bool] = UNSET,
    start_date_after: Union[Unset, datetime.datetime] = UNSET,
    start_date_before: Union[Unset, datetime.datetime] = UNSET,
) -> Response[Union[Any, EventSearchResult]]:
    """Gets a list of events

    Args:
        archived (Union[Unset, bool]):
        current_page (Union[Unset, int]):
        end_date_after (Union[Unset, datetime.datetime]):
        end_date_before (Union[Unset, datetime.datetime]):
        event_category (Union[Unset, int]):
        event_id (Union[Unset, int]):
        event_name (Union[Unset, str]):
        page_size (Union[Unset, int]):
        published_event (Union[Unset, bool]):
        start_date_after (Union[Unset, datetime.datetime]):
        start_date_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EventSearchResult]]
    """

    kwargs = _get_kwargs(
        archived=archived,
        current_page=current_page,
        end_date_after=end_date_after,
        end_date_before=end_date_before,
        event_category=event_category,
        event_id=event_id,
        event_name=event_name,
        page_size=page_size,
        published_event=published_event,
        start_date_after=start_date_after,
        start_date_before=start_date_before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    archived: Union[Unset, bool] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    end_date_after: Union[Unset, datetime.datetime] = UNSET,
    end_date_before: Union[Unset, datetime.datetime] = UNSET,
    event_category: Union[Unset, int] = UNSET,
    event_id: Union[Unset, int] = UNSET,
    event_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    published_event: Union[Unset, bool] = UNSET,
    start_date_after: Union[Unset, datetime.datetime] = UNSET,
    start_date_before: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[Union[Any, EventSearchResult]]:
    """Gets a list of events

    Args:
        archived (Union[Unset, bool]):
        current_page (Union[Unset, int]):
        end_date_after (Union[Unset, datetime.datetime]):
        end_date_before (Union[Unset, datetime.datetime]):
        event_category (Union[Unset, int]):
        event_id (Union[Unset, int]):
        event_name (Union[Unset, str]):
        page_size (Union[Unset, int]):
        published_event (Union[Unset, bool]):
        start_date_after (Union[Unset, datetime.datetime]):
        start_date_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, EventSearchResult]
    """

    return (
        await asyncio_detailed(
            client=client,
            archived=archived,
            current_page=current_page,
            end_date_after=end_date_after,
            end_date_before=end_date_before,
            event_category=event_category,
            event_id=event_id,
            event_name=event_name,
            page_size=page_size,
            published_event=published_event,
            start_date_after=start_date_after,
            start_date_before=start_date_before,
        )
    ).parsed
