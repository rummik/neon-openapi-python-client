from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.pagination_sort_direction import PaginationSortDirection
from ..types import UNSET, Unset

T = TypeVar("T", bound="Pagination")


@_attrs_define
class Pagination:
    """
    Attributes:
        current_page (Union[Unset, int]):
        page_size (Union[Unset, int]):
        sort_column (Union[Unset, str]):
        sort_direction (Union[Unset, PaginationSortDirection]):
        total_pages (Union[Unset, int]):
        total_results (Union[Unset, int]):
    """

    current_page: Union[Unset, int] = UNSET
    page_size: Union[Unset, int] = UNSET
    sort_column: Union[Unset, str] = UNSET
    sort_direction: Union[Unset, PaginationSortDirection] = UNSET
    total_pages: Union[Unset, int] = UNSET
    total_results: Union[Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        current_page = self.current_page

        page_size = self.page_size

        sort_column = self.sort_column

        sort_direction: Union[Unset, str] = UNSET
        if not isinstance(self.sort_direction, Unset):
            sort_direction = self.sort_direction.value

        total_pages = self.total_pages

        total_results = self.total_results

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if sort_column is not UNSET:
            field_dict["sortColumn"] = sort_column
        if sort_direction is not UNSET:
            field_dict["sortDirection"] = sort_direction
        if total_pages is not UNSET:
            field_dict["totalPages"] = total_pages
        if total_results is not UNSET:
            field_dict["totalResults"] = total_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_page = d.pop("currentPage", UNSET)

        page_size = d.pop("pageSize", UNSET)

        sort_column = d.pop("sortColumn", UNSET)

        _sort_direction = d.pop("sortDirection", UNSET)
        sort_direction: Union[Unset, PaginationSortDirection]
        if isinstance(_sort_direction, Unset):
            sort_direction = UNSET
        else:
            sort_direction = PaginationSortDirection(_sort_direction)

        total_pages = d.pop("totalPages", UNSET)

        total_results = d.pop("totalResults", UNSET)

        pagination = cls(
            current_page=current_page,
            page_size=page_size,
            sort_column=sort_column,
            sort_direction=sort_direction,
            total_pages=total_pages,
            total_results=total_results,
        )

        pagination.additional_properties = d
        return pagination

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
