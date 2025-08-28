from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.user_group_api import UserGroupApi


T = TypeVar("T", bound="UserGroupSearchResult")


@_attrs_define
class UserGroupSearchResult:
    """
    Attributes:
        group_list (Union[Unset, list['UserGroupApi']]):
        pagination (Union[Unset, Pagination]):
    """

    group_list: Union[Unset, list["UserGroupApi"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        group_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.group_list, Unset):
            group_list = []
            for group_list_item_data in self.group_list:
                group_list_item = group_list_item_data.to_dict()
                group_list.append(group_list_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if group_list is not UNSET:
            field_dict["groupList"] = group_list
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.user_group_api import UserGroupApi

        d = dict(src_dict)
        group_list = []
        _group_list = d.pop("groupList", UNSET)
        for group_list_item_data in _group_list or []:
            group_list_item = UserGroupApi.from_dict(group_list_item_data)

            group_list.append(group_list_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        user_group_search_result = cls(
            group_list=group_list,
            pagination=pagination,
        )

        user_group_search_result.additional_properties = d
        return user_group_search_result

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
