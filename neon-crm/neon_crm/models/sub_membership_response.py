from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.sub_membership_response_status import SubMembershipResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.id_name_pair import IdNamePair


T = TypeVar("T", bound="SubMembershipResponse")


@_attrs_define
class SubMembershipResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        account_id (Union[Unset, str]):
        membership_level (Union[Unset, IdNamePair]):
        membership_term (Union[Unset, IdNamePair]):
        status (Union[Unset, SubMembershipResponseStatus]):
    """

    id: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    membership_level: Union[Unset, "IdNamePair"] = UNSET
    membership_term: Union[Unset, "IdNamePair"] = UNSET
    status: Union[Unset, SubMembershipResponseStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_id = self.account_id

        membership_level: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.membership_level, Unset):
            membership_level = self.membership_level.to_dict()

        membership_term: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.membership_term, Unset):
            membership_term = self.membership_term.to_dict()

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if membership_level is not UNSET:
            field_dict["membershipLevel"] = membership_level
        if membership_term is not UNSET:
            field_dict["membershipTerm"] = membership_term
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.id_name_pair import IdNamePair

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        account_id = d.pop("accountId", UNSET)

        _membership_level = d.pop("membershipLevel", UNSET)
        membership_level: Union[Unset, IdNamePair]
        if isinstance(_membership_level, Unset):
            membership_level = UNSET
        else:
            membership_level = IdNamePair.from_dict(_membership_level)

        _membership_term = d.pop("membershipTerm", UNSET)
        membership_term: Union[Unset, IdNamePair]
        if isinstance(_membership_term, Unset):
            membership_term = UNSET
        else:
            membership_term = IdNamePair.from_dict(_membership_term)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SubMembershipResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SubMembershipResponseStatus(_status)

        sub_membership_response = cls(
            id=id,
            account_id=account_id,
            membership_level=membership_level,
            membership_term=membership_term,
            status=status,
        )

        sub_membership_response.additional_properties = d
        return sub_membership_response

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
