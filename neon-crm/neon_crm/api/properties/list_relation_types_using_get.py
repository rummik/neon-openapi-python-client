from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.id_name_pair import IdNamePair
from ...models.list_relation_types_using_get_relation_type_category import ListRelationTypesUsingGETRelationTypeCategory
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    relation_type_category: Union[Unset, ListRelationTypesUsingGETRelationTypeCategory] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_relation_type_category: Union[Unset, str] = UNSET
    if not isinstance(relation_type_category, Unset):
        json_relation_type_category = relation_type_category.value

    params["relationTypeCategory"] = json_relation_type_category

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/properties/relationTypes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["IdNamePair"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = IdNamePair.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, list["IdNamePair"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    relation_type_category: Union[Unset, ListRelationTypesUsingGETRelationTypeCategory] = UNSET,
) -> Response[Union[Any, list["IdNamePair"]]]:
    """Gets relation types

    Args:
        relation_type_category (Union[Unset, ListRelationTypesUsingGETRelationTypeCategory]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['IdNamePair']]]
    """

    kwargs = _get_kwargs(
        relation_type_category=relation_type_category,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    relation_type_category: Union[Unset, ListRelationTypesUsingGETRelationTypeCategory] = UNSET,
) -> Optional[Union[Any, list["IdNamePair"]]]:
    """Gets relation types

    Args:
        relation_type_category (Union[Unset, ListRelationTypesUsingGETRelationTypeCategory]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['IdNamePair']]
    """

    return sync_detailed(
        client=client,
        relation_type_category=relation_type_category,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    relation_type_category: Union[Unset, ListRelationTypesUsingGETRelationTypeCategory] = UNSET,
) -> Response[Union[Any, list["IdNamePair"]]]:
    """Gets relation types

    Args:
        relation_type_category (Union[Unset, ListRelationTypesUsingGETRelationTypeCategory]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['IdNamePair']]]
    """

    kwargs = _get_kwargs(
        relation_type_category=relation_type_category,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    relation_type_category: Union[Unset, ListRelationTypesUsingGETRelationTypeCategory] = UNSET,
) -> Optional[Union[Any, list["IdNamePair"]]]:
    """Gets relation types

    Args:
        relation_type_category (Union[Unset, ListRelationTypesUsingGETRelationTypeCategory]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['IdNamePair']]
    """

    return (
        await asyncio_detailed(
            client=client,
            relation_type_category=relation_type_category,
        )
    ).parsed
