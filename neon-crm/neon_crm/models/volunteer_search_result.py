from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.volunteer_api import VolunteerApi


T = TypeVar("T", bound="VolunteerSearchResult")


@_attrs_define
class VolunteerSearchResult:
    """
    Attributes:
        pagination (Union[Unset, Pagination]):
        volunteer_list (Union[Unset, list['VolunteerApi']]):
    """

    pagination: Union[Unset, "Pagination"] = UNSET
    volunteer_list: Union[Unset, list["VolunteerApi"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        volunteer_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.volunteer_list, Unset):
            volunteer_list = []
            for volunteer_list_item_data in self.volunteer_list:
                volunteer_list_item = volunteer_list_item_data.to_dict()
                volunteer_list.append(volunteer_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if volunteer_list is not UNSET:
            field_dict["volunteerList"] = volunteer_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.volunteer_api import VolunteerApi

        d = dict(src_dict)
        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        volunteer_list = []
        _volunteer_list = d.pop("volunteerList", UNSET)
        for volunteer_list_item_data in _volunteer_list or []:
            volunteer_list_item = VolunteerApi.from_dict(volunteer_list_item_data)

            volunteer_list.append(volunteer_list_item)

        volunteer_search_result = cls(
            pagination=pagination,
            volunteer_list=volunteer_list,
        )

        volunteer_search_result.additional_properties = d
        return volunteer_search_result

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
