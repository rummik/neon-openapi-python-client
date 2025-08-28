from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.time_sheet_search_param_status_list_item import TimeSheetSearchParamStatusListItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="TimeSheetSearchParam")


@_attrs_define
class TimeSheetSearchParam:
    """
    Attributes:
        page_size (Union[Unset, int]):
        current_page (Union[Unset, int]):
        ids (Union[Unset, str]):
        account_ids (Union[Unset, str]):
        project_ids (Union[Unset, str]):
        volunteer_groups (Union[Unset, str]):
        role_ids (Union[Unset, str]):
        shift_ids (Union[Unset, str]):
        status_list (Union[Unset, list[TimeSheetSearchParamStatusListItem]]):
    """

    page_size: Union[Unset, int] = UNSET
    current_page: Union[Unset, int] = UNSET
    ids: Union[Unset, str] = UNSET
    account_ids: Union[Unset, str] = UNSET
    project_ids: Union[Unset, str] = UNSET
    volunteer_groups: Union[Unset, str] = UNSET
    role_ids: Union[Unset, str] = UNSET
    shift_ids: Union[Unset, str] = UNSET
    status_list: Union[Unset, list[TimeSheetSearchParamStatusListItem]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_size = self.page_size

        current_page = self.current_page

        ids = self.ids

        account_ids = self.account_ids

        project_ids = self.project_ids

        volunteer_groups = self.volunteer_groups

        role_ids = self.role_ids

        shift_ids = self.shift_ids

        status_list: Union[Unset, list[str]] = UNSET
        if not isinstance(self.status_list, Unset):
            status_list = []
            for status_list_item_data in self.status_list:
                status_list_item = status_list_item_data.value
                status_list.append(status_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if ids is not UNSET:
            field_dict["ids"] = ids
        if account_ids is not UNSET:
            field_dict["accountIds"] = account_ids
        if project_ids is not UNSET:
            field_dict["projectIds"] = project_ids
        if volunteer_groups is not UNSET:
            field_dict["volunteerGroups"] = volunteer_groups
        if role_ids is not UNSET:
            field_dict["roleIds"] = role_ids
        if shift_ids is not UNSET:
            field_dict["shiftIds"] = shift_ids
        if status_list is not UNSET:
            field_dict["statusList"] = status_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_size = d.pop("pageSize", UNSET)

        current_page = d.pop("currentPage", UNSET)

        ids = d.pop("ids", UNSET)

        account_ids = d.pop("accountIds", UNSET)

        project_ids = d.pop("projectIds", UNSET)

        volunteer_groups = d.pop("volunteerGroups", UNSET)

        role_ids = d.pop("roleIds", UNSET)

        shift_ids = d.pop("shiftIds", UNSET)

        status_list = []
        _status_list = d.pop("statusList", UNSET)
        for status_list_item_data in _status_list or []:
            status_list_item = TimeSheetSearchParamStatusListItem(status_list_item_data)

            status_list.append(status_list_item)

        time_sheet_search_param = cls(
            page_size=page_size,
            current_page=current_page,
            ids=ids,
            account_ids=account_ids,
            project_ids=project_ids,
            volunteer_groups=volunteer_groups,
            role_ids=role_ids,
            shift_ids=shift_ids,
            status_list=status_list,
        )

        time_sheet_search_param.additional_properties = d
        return time_sheet_search_param

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
