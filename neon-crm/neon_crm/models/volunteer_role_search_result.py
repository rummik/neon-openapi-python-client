from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.volunteer_role_api import VolunteerRoleApi


T = TypeVar("T", bound="VolunteerRoleSearchResult")


@_attrs_define
class VolunteerRoleSearchResult:
    """
    Attributes:
        volunteer_role_apis (Union[Unset, list['VolunteerRoleApi']]):
        pagination (Union[Unset, Pagination]):
    """

    volunteer_role_apis: Union[Unset, list["VolunteerRoleApi"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volunteer_role_apis: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.volunteer_role_apis, Unset):
            volunteer_role_apis = []
            for volunteer_role_apis_item_data in self.volunteer_role_apis:
                volunteer_role_apis_item = volunteer_role_apis_item_data.to_dict()
                volunteer_role_apis.append(volunteer_role_apis_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if volunteer_role_apis is not UNSET:
            field_dict["volunteerRoleApis"] = volunteer_role_apis
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.volunteer_role_api import VolunteerRoleApi

        d = dict(src_dict)
        volunteer_role_apis = []
        _volunteer_role_apis = d.pop("volunteerRoleApis", UNSET)
        for volunteer_role_apis_item_data in _volunteer_role_apis or []:
            volunteer_role_apis_item = VolunteerRoleApi.from_dict(volunteer_role_apis_item_data)

            volunteer_role_apis.append(volunteer_role_apis_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        volunteer_role_search_result = cls(
            volunteer_role_apis=volunteer_role_apis,
            pagination=pagination,
        )

        volunteer_role_search_result.additional_properties = d
        return volunteer_role_search_result

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
