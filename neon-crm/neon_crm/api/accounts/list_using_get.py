from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.account_search_result import AccountSearchResult
from ...models.list_using_get_user_type import ListUsingGETUserType
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    current_page: Union[Unset, int] = UNSET,
    email: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user_type: Union[Unset, ListUsingGETUserType] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["currentPage"] = current_page

    params["email"] = email

    params["firstName"] = first_name

    params["lastName"] = last_name

    params["pageSize"] = page_size

    json_user_type: Union[Unset, str] = UNSET
    if not isinstance(user_type, Unset):
        json_user_type = user_type.value

    params["userType"] = json_user_type

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/accounts",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[AccountSearchResult, Any]]:
    if response.status_code == 200:
        response_200 = AccountSearchResult.from_dict(response.json())

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
) -> Response[Union[AccountSearchResult, Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    email: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user_type: Union[Unset, ListUsingGETUserType] = UNSET,
) -> Response[Union[AccountSearchResult, Any]]:
    """Gets a list of accounts

    Args:
        current_page (Union[Unset, int]):
        email (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        page_size (Union[Unset, int]):
        user_type (Union[Unset, ListUsingGETUserType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountSearchResult, Any]]
    """

    kwargs = _get_kwargs(
        current_page=current_page,
        email=email,
        first_name=first_name,
        last_name=last_name,
        page_size=page_size,
        user_type=user_type,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    email: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user_type: Union[Unset, ListUsingGETUserType] = UNSET,
) -> Optional[Union[AccountSearchResult, Any]]:
    """Gets a list of accounts

    Args:
        current_page (Union[Unset, int]):
        email (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        page_size (Union[Unset, int]):
        user_type (Union[Unset, ListUsingGETUserType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountSearchResult, Any]
    """

    return sync_detailed(
        client=client,
        current_page=current_page,
        email=email,
        first_name=first_name,
        last_name=last_name,
        page_size=page_size,
        user_type=user_type,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    email: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user_type: Union[Unset, ListUsingGETUserType] = UNSET,
) -> Response[Union[AccountSearchResult, Any]]:
    """Gets a list of accounts

    Args:
        current_page (Union[Unset, int]):
        email (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        page_size (Union[Unset, int]):
        user_type (Union[Unset, ListUsingGETUserType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AccountSearchResult, Any]]
    """

    kwargs = _get_kwargs(
        current_page=current_page,
        email=email,
        first_name=first_name,
        last_name=last_name,
        page_size=page_size,
        user_type=user_type,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    current_page: Union[Unset, int] = UNSET,
    email: Union[Unset, str] = UNSET,
    first_name: Union[Unset, str] = UNSET,
    last_name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    user_type: Union[Unset, ListUsingGETUserType] = UNSET,
) -> Optional[Union[AccountSearchResult, Any]]:
    """Gets a list of accounts

    Args:
        current_page (Union[Unset, int]):
        email (Union[Unset, str]):
        first_name (Union[Unset, str]):
        last_name (Union[Unset, str]):
        page_size (Union[Unset, int]):
        user_type (Union[Unset, ListUsingGETUserType]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AccountSearchResult, Any]
    """

    return (
        await asyncio_detailed(
            client=client,
            current_page=current_page,
            email=email,
            first_name=first_name,
            last_name=last_name,
            page_size=page_size,
            user_type=user_type,
        )
    ).parsed
