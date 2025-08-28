from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.list_product_using_get_status import ListProductUsingGETStatus
from ...models.product_search_response import ProductSearchResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    catalog_id: Union[Unset, str] = UNSET,
    category_id: Union[Unset, str] = UNSET,
    code: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    status: Union[Unset, ListProductUsingGETStatus] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["catalogId"] = catalog_id

    params["categoryId"] = category_id

    params["code"] = code

    params["currentPage"] = current_page

    params["keyword"] = keyword

    params["name"] = name

    params["pageSize"] = page_size

    json_status: Union[Unset, str] = UNSET
    if not isinstance(status, Unset):
        json_status = status.value

    params["status"] = json_status

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/store/products",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProductSearchResponse]]:
    if response.status_code == 200:
        response_200 = ProductSearchResponse.from_dict(response.json())

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
) -> Response[Union[Any, ProductSearchResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    catalog_id: Union[Unset, str] = UNSET,
    category_id: Union[Unset, str] = UNSET,
    code: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    status: Union[Unset, ListProductUsingGETStatus] = UNSET,
) -> Response[Union[Any, ProductSearchResponse]]:
    """Get a list of store products

    Args:
        catalog_id (Union[Unset, str]):
        category_id (Union[Unset, str]):
        code (Union[Unset, str]):
        current_page (Union[Unset, int]):
        keyword (Union[Unset, str]):
        name (Union[Unset, str]):
        page_size (Union[Unset, int]):
        status (Union[Unset, ListProductUsingGETStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProductSearchResponse]]
    """

    kwargs = _get_kwargs(
        catalog_id=catalog_id,
        category_id=category_id,
        code=code,
        current_page=current_page,
        keyword=keyword,
        name=name,
        page_size=page_size,
        status=status,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    catalog_id: Union[Unset, str] = UNSET,
    category_id: Union[Unset, str] = UNSET,
    code: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    status: Union[Unset, ListProductUsingGETStatus] = UNSET,
) -> Optional[Union[Any, ProductSearchResponse]]:
    """Get a list of store products

    Args:
        catalog_id (Union[Unset, str]):
        category_id (Union[Unset, str]):
        code (Union[Unset, str]):
        current_page (Union[Unset, int]):
        keyword (Union[Unset, str]):
        name (Union[Unset, str]):
        page_size (Union[Unset, int]):
        status (Union[Unset, ListProductUsingGETStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProductSearchResponse]
    """

    return sync_detailed(
        client=client,
        catalog_id=catalog_id,
        category_id=category_id,
        code=code,
        current_page=current_page,
        keyword=keyword,
        name=name,
        page_size=page_size,
        status=status,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    catalog_id: Union[Unset, str] = UNSET,
    category_id: Union[Unset, str] = UNSET,
    code: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    status: Union[Unset, ListProductUsingGETStatus] = UNSET,
) -> Response[Union[Any, ProductSearchResponse]]:
    """Get a list of store products

    Args:
        catalog_id (Union[Unset, str]):
        category_id (Union[Unset, str]):
        code (Union[Unset, str]):
        current_page (Union[Unset, int]):
        keyword (Union[Unset, str]):
        name (Union[Unset, str]):
        page_size (Union[Unset, int]):
        status (Union[Unset, ListProductUsingGETStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProductSearchResponse]]
    """

    kwargs = _get_kwargs(
        catalog_id=catalog_id,
        category_id=category_id,
        code=code,
        current_page=current_page,
        keyword=keyword,
        name=name,
        page_size=page_size,
        status=status,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    catalog_id: Union[Unset, str] = UNSET,
    category_id: Union[Unset, str] = UNSET,
    code: Union[Unset, str] = UNSET,
    current_page: Union[Unset, int] = UNSET,
    keyword: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    page_size: Union[Unset, int] = UNSET,
    status: Union[Unset, ListProductUsingGETStatus] = UNSET,
) -> Optional[Union[Any, ProductSearchResponse]]:
    """Get a list of store products

    Args:
        catalog_id (Union[Unset, str]):
        category_id (Union[Unset, str]):
        code (Union[Unset, str]):
        current_page (Union[Unset, int]):
        keyword (Union[Unset, str]):
        name (Union[Unset, str]):
        page_size (Union[Unset, int]):
        status (Union[Unset, ListProductUsingGETStatus]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProductSearchResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            catalog_id=catalog_id,
            category_id=category_id,
            code=code,
            current_page=current_page,
            keyword=keyword,
            name=name,
            page_size=page_size,
            status=status,
        )
    ).parsed
