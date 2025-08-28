from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.custom_field_group import CustomFieldGroup
from ...models.list_using_get1_component import ListUsingGET1Component
from ...types import UNSET, Response


def _get_kwargs(
    *,
    component: ListUsingGET1Component,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_component = component.value
    params["component"] = json_component

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/customFields/groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, list["CustomFieldGroup"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = CustomFieldGroup.from_dict(response_200_item_data)

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
) -> Response[Union[Any, list["CustomFieldGroup"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    component: ListUsingGET1Component,
) -> Response[Union[Any, list["CustomFieldGroup"]]]:
    """Gets a list of custom field groups

    Args:
        component (ListUsingGET1Component):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CustomFieldGroup']]]
    """

    kwargs = _get_kwargs(
        component=component,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    component: ListUsingGET1Component,
) -> Optional[Union[Any, list["CustomFieldGroup"]]]:
    """Gets a list of custom field groups

    Args:
        component (ListUsingGET1Component):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CustomFieldGroup']]
    """

    return sync_detailed(
        client=client,
        component=component,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    component: ListUsingGET1Component,
) -> Response[Union[Any, list["CustomFieldGroup"]]]:
    """Gets a list of custom field groups

    Args:
        component (ListUsingGET1Component):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, list['CustomFieldGroup']]]
    """

    kwargs = _get_kwargs(
        component=component,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    component: ListUsingGET1Component,
) -> Optional[Union[Any, list["CustomFieldGroup"]]]:
    """Gets a list of custom field groups

    Args:
        component (ListUsingGET1Component):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, list['CustomFieldGroup']]
    """

    return (
        await asyncio_detailed(
            client=client,
            component=component,
        )
    ).parsed
