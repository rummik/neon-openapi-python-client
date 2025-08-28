from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.membership_level import MembershipLevel
    from ..models.pagination import Pagination


T = TypeVar("T", bound="MembershipLevelsResponse")


@_attrs_define
class MembershipLevelsResponse:
    """
    Attributes:
        membership_levels (Union[Unset, list['MembershipLevel']]):
        pagination (Union[Unset, Pagination]):
    """

    membership_levels: Union[Unset, list["MembershipLevel"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        membership_levels: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.membership_levels, Unset):
            membership_levels = []
            for membership_levels_item_data in self.membership_levels:
                membership_levels_item = membership_levels_item_data.to_dict()
                membership_levels.append(membership_levels_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if membership_levels is not UNSET:
            field_dict["membershipLevels"] = membership_levels
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.membership_level import MembershipLevel
        from ..models.pagination import Pagination

        d = dict(src_dict)
        membership_levels = []
        _membership_levels = d.pop("membershipLevels", UNSET)
        for membership_levels_item_data in _membership_levels or []:
            membership_levels_item = MembershipLevel.from_dict(membership_levels_item_data)

            membership_levels.append(membership_levels_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        membership_levels_response = cls(
            membership_levels=membership_levels,
            pagination=pagination,
        )

        membership_levels_response.additional_properties = d
        return membership_levels_response

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
