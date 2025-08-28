from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.membership_response_status import MembershipResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.id_name_pair import IdNamePair
    from ..models.payment_response import PaymentResponse
    from ..models.sub_membership_response import SubMembershipResponse


T = TypeVar("T", bound="MembershipResponse")


@_attrs_define
class MembershipResponse:
    """
    Attributes:
        id (Union[Unset, str]):
        sub_membership_responses (Union[Unset, list['SubMembershipResponse']]):
        account_id (Union[Unset, str]):
        payment_response (Union[Unset, PaymentResponse]):
        membership_level (Union[Unset, IdNamePair]):
        membership_term (Union[Unset, IdNamePair]):
        status (Union[Unset, MembershipResponseStatus]):
    """

    id: Union[Unset, str] = UNSET
    sub_membership_responses: Union[Unset, list["SubMembershipResponse"]] = UNSET
    account_id: Union[Unset, str] = UNSET
    payment_response: Union[Unset, "PaymentResponse"] = UNSET
    membership_level: Union[Unset, "IdNamePair"] = UNSET
    membership_term: Union[Unset, "IdNamePair"] = UNSET
    status: Union[Unset, MembershipResponseStatus] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        sub_membership_responses: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.sub_membership_responses, Unset):
            sub_membership_responses = []
            for sub_membership_responses_item_data in self.sub_membership_responses:
                sub_membership_responses_item = sub_membership_responses_item_data.to_dict()
                sub_membership_responses.append(sub_membership_responses_item)

        account_id = self.account_id

        payment_response: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment_response, Unset):
            payment_response = self.payment_response.to_dict()

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
        if sub_membership_responses is not UNSET:
            field_dict["subMembershipResponses"] = sub_membership_responses
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if payment_response is not UNSET:
            field_dict["paymentResponse"] = payment_response
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
        from ..models.payment_response import PaymentResponse
        from ..models.sub_membership_response import SubMembershipResponse

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        sub_membership_responses = []
        _sub_membership_responses = d.pop("subMembershipResponses", UNSET)
        for sub_membership_responses_item_data in _sub_membership_responses or []:
            sub_membership_responses_item = SubMembershipResponse.from_dict(sub_membership_responses_item_data)

            sub_membership_responses.append(sub_membership_responses_item)

        account_id = d.pop("accountId", UNSET)

        _payment_response = d.pop("paymentResponse", UNSET)
        payment_response: Union[Unset, PaymentResponse]
        if isinstance(_payment_response, Unset):
            payment_response = UNSET
        else:
            payment_response = PaymentResponse.from_dict(_payment_response)

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
        status: Union[Unset, MembershipResponseStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = MembershipResponseStatus(_status)

        membership_response = cls(
            id=id,
            sub_membership_responses=sub_membership_responses,
            account_id=account_id,
            payment_response=payment_response,
            membership_level=membership_level,
            membership_term=membership_term,
            status=status,
        )

        membership_response.additional_properties = d
        return membership_response

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
