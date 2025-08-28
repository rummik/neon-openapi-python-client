from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_card_online_payment import CreditCardOnlinePayment
    from ..models.e_check_payment import ECheckPayment


T = TypeVar("T", bound="MembershipAutoRenewal")


@_attrs_define
class MembershipAutoRenewal:
    """
    Attributes:
        membership_id (Union[Unset, str]):
        auto_renewal (Union[Unset, bool]):
        credit_card_online (Union[Unset, CreditCardOnlinePayment]):
        ach (Union[Unset, ECheckPayment]):
        donor_covered_fee_flag (Union[Unset, bool]):
        send_auto_renewal_enabled_email (Union[Unset, bool]):
    """

    membership_id: Union[Unset, str] = UNSET
    auto_renewal: Union[Unset, bool] = UNSET
    credit_card_online: Union[Unset, "CreditCardOnlinePayment"] = UNSET
    ach: Union[Unset, "ECheckPayment"] = UNSET
    donor_covered_fee_flag: Union[Unset, bool] = UNSET
    send_auto_renewal_enabled_email: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        membership_id = self.membership_id

        auto_renewal = self.auto_renewal

        credit_card_online: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credit_card_online, Unset):
            credit_card_online = self.credit_card_online.to_dict()

        ach: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ach, Unset):
            ach = self.ach.to_dict()

        donor_covered_fee_flag = self.donor_covered_fee_flag

        send_auto_renewal_enabled_email = self.send_auto_renewal_enabled_email

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if membership_id is not UNSET:
            field_dict["membershipId"] = membership_id
        if auto_renewal is not UNSET:
            field_dict["autoRenewal"] = auto_renewal
        if credit_card_online is not UNSET:
            field_dict["creditCardOnline"] = credit_card_online
        if ach is not UNSET:
            field_dict["ach"] = ach
        if donor_covered_fee_flag is not UNSET:
            field_dict["donorCoveredFeeFlag"] = donor_covered_fee_flag
        if send_auto_renewal_enabled_email is not UNSET:
            field_dict["sendAutoRenewalEnabledEmail"] = send_auto_renewal_enabled_email

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credit_card_online_payment import CreditCardOnlinePayment
        from ..models.e_check_payment import ECheckPayment

        d = dict(src_dict)
        membership_id = d.pop("membershipId", UNSET)

        auto_renewal = d.pop("autoRenewal", UNSET)

        _credit_card_online = d.pop("creditCardOnline", UNSET)
        credit_card_online: Union[Unset, CreditCardOnlinePayment]
        if isinstance(_credit_card_online, Unset):
            credit_card_online = UNSET
        else:
            credit_card_online = CreditCardOnlinePayment.from_dict(_credit_card_online)

        _ach = d.pop("ach", UNSET)
        ach: Union[Unset, ECheckPayment]
        if isinstance(_ach, Unset):
            ach = UNSET
        else:
            ach = ECheckPayment.from_dict(_ach)

        donor_covered_fee_flag = d.pop("donorCoveredFeeFlag", UNSET)

        send_auto_renewal_enabled_email = d.pop("sendAutoRenewalEnabledEmail", UNSET)

        membership_auto_renewal = cls(
            membership_id=membership_id,
            auto_renewal=auto_renewal,
            credit_card_online=credit_card_online,
            ach=ach,
            donor_covered_fee_flag=donor_covered_fee_flag,
            send_auto_renewal_enabled_email=send_auto_renewal_enabled_email,
        )

        membership_auto_renewal.additional_properties = d
        return membership_auto_renewal

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
