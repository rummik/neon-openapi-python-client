from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.output_fields import OutputFields
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    search_key: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["searchKey"] = search_key

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/donations/search/outputFields",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, OutputFields]]:
    if response.status_code == 200:
        response_200 = OutputFields.from_dict(response.json())

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
) -> Response[Union[Any, OutputFields]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    search_key: Union[Unset, str] = UNSET,
) -> Response[Union[Any, OutputFields]]:
    """Gets a list of possible output columns for the /donations/search method

    Args:
        search_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OutputFields]]
    """

    kwargs = _get_kwargs(
        search_key=search_key,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    search_key: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, OutputFields]]:
    """Gets a list of possible output columns for the /donations/search method

    Args:
        search_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, OutputFields]
    """

    return sync_detailed(
        client=client,
        search_key=search_key,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    search_key: Union[Unset, str] = UNSET,
) -> Response[Union[Any, OutputFields]]:
    """Gets a list of possible output columns for the /donations/search method

    Args:
        search_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, OutputFields]]
    """

    kwargs = _get_kwargs(
        search_key=search_key,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    search_key: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, OutputFields]]:
    """Gets a list of possible output columns for the /donations/search method

    Args:
        search_key (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, OutputFields]
    """

    return (
        await asyncio_detailed(
            client=client,
            search_key=search_key,
        )
    ).parsed
