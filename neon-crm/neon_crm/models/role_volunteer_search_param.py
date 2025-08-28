from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleVolunteerSearchParam")


@_attrs_define
class RoleVolunteerSearchParam:
    """
    Attributes:
        page_size (Union[Unset, int]):
        current_page (Union[Unset, int]):
        opportunity_ids (Union[Unset, list[str]]):
        shift_ids (Union[Unset, list[str]]):
        group_ids (Union[Unset, list[str]]):
    """

    page_size: Union[Unset, int] = UNSET
    current_page: Union[Unset, int] = UNSET
    opportunity_ids: Union[Unset, list[str]] = UNSET
    shift_ids: Union[Unset, list[str]] = UNSET
    group_ids: Union[Unset, list[str]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_size = self.page_size

        current_page = self.current_page

        opportunity_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.opportunity_ids, Unset):
            opportunity_ids = self.opportunity_ids

        shift_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.shift_ids, Unset):
            shift_ids = self.shift_ids

        group_ids: Union[Unset, list[str]] = UNSET
        if not isinstance(self.group_ids, Unset):
            group_ids = self.group_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if opportunity_ids is not UNSET:
            field_dict["opportunityIds"] = opportunity_ids
        if shift_ids is not UNSET:
            field_dict["shiftIds"] = shift_ids
        if group_ids is not UNSET:
            field_dict["groupIds"] = group_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_size = d.pop("pageSize", UNSET)

        current_page = d.pop("currentPage", UNSET)

        opportunity_ids = cast(list[str], d.pop("opportunityIds", UNSET))

        shift_ids = cast(list[str], d.pop("shiftIds", UNSET))

        group_ids = cast(list[str], d.pop("groupIds", UNSET))

        role_volunteer_search_param = cls(
            page_size=page_size,
            current_page=current_page,
            opportunity_ids=opportunity_ids,
            shift_ids=shift_ids,
            group_ids=group_ids,
        )

        role_volunteer_search_param.additional_properties = d
        return role_volunteer_search_param

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
