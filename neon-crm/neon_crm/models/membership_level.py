from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.membership_level_scope_type import MembershipLevelScopeType
from ..models.membership_level_status import MembershipLevelStatus
from ..models.membership_level_type import MembershipLevelType
from ..types import UNSET, Unset

T = TypeVar("T", bound="MembershipLevel")


@_attrs_define
class MembershipLevel:
    """
    Attributes:
        id (Union[Unset, int]):
        description (Union[Unset, str]):
        code (Union[Unset, str]):
        rank (Union[Unset, int]):
        type_ (Union[Unset, MembershipLevelType]):
        status (Union[Unset, MembershipLevelStatus]):
        force_auto_renewal (Union[Unset, bool]):
        child_member_allowed (Union[Unset, int]):
        scope_type (Union[Unset, MembershipLevelScopeType]):
    """

    id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    rank: Union[Unset, int] = UNSET
    type_: Union[Unset, MembershipLevelType] = UNSET
    status: Union[Unset, MembershipLevelStatus] = UNSET
    force_auto_renewal: Union[Unset, bool] = UNSET
    child_member_allowed: Union[Unset, int] = UNSET
    scope_type: Union[Unset, MembershipLevelScopeType] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        description = self.description

        code = self.code

        rank = self.rank

        type_: Union[Unset, str] = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        force_auto_renewal = self.force_auto_renewal

        child_member_allowed = self.child_member_allowed

        scope_type: Union[Unset, str] = UNSET
        if not isinstance(self.scope_type, Unset):
            scope_type = self.scope_type.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if code is not UNSET:
            field_dict["code"] = code
        if rank is not UNSET:
            field_dict["rank"] = rank
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if force_auto_renewal is not UNSET:
            field_dict["forceAutoRenewal"] = force_auto_renewal
        if child_member_allowed is not UNSET:
            field_dict["childMemberAllowed"] = child_member_allowed
        if scope_type is not UNSET:
            field_dict["scopeType"] = scope_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        code = d.pop("code", UNSET)

        rank = d.pop("rank", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: Union[Unset, MembershipLevelType]
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = MembershipLevelType(_type_)

        _status = d.pop("status", UNSET)
        status: Union[Unset, MembershipLevelStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MembershipLevelStatus(_status)

        force_auto_renewal = d.pop("forceAutoRenewal", UNSET)

        child_member_allowed = d.pop("childMemberAllowed", UNSET)

        _scope_type = d.pop("scopeType", UNSET)
        scope_type: Union[Unset, MembershipLevelScopeType]
        if isinstance(_scope_type, Unset):
            scope_type = UNSET
        else:
            scope_type = MembershipLevelScopeType(_scope_type)

        membership_level = cls(
            id=id,
            description=description,
            code=code,
            rank=rank,
            type_=type_,
            status=status,
            force_auto_renewal=force_auto_renewal,
            child_member_allowed=child_member_allowed,
            scope_type=scope_type,
        )

        membership_level.additional_properties = d
        return membership_level

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
