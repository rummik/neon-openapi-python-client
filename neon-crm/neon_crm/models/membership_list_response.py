from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.membership import Membership
    from ..models.pagination import Pagination


T = TypeVar("T", bound="MembershipListResponse")


@_attrs_define
class MembershipListResponse:
    """
    Attributes:
        memberships (Union[Unset, list['Membership']]):
        pagination (Union[Unset, Pagination]):
    """

    memberships: Union[Unset, list["Membership"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        memberships: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.memberships, Unset):
            memberships = []
            for memberships_item_data in self.memberships:
                memberships_item = memberships_item_data.to_dict()
                memberships.append(memberships_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if memberships is not UNSET:
            field_dict["memberships"] = memberships
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.membership import Membership
        from ..models.pagination import Pagination

        d = dict(src_dict)
        memberships = []
        _memberships = d.pop("memberships", UNSET)
        for memberships_item_data in _memberships or []:
            memberships_item = Membership.from_dict(memberships_item_data)

            memberships.append(memberships_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        membership_list_response = cls(
            memberships=memberships,
            pagination=pagination,
        )

        membership_list_response.additional_properties = d
        return membership_list_response

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
