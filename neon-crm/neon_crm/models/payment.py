import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.payment_payment_status import PaymentPaymentStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.check_payment import CheckPayment
    from ..models.credit_card_offline_payment import CreditCardOfflinePayment
    from ..models.credit_card_online_payment import CreditCardOnlinePayment
    from ..models.daf_pay_payment import DafPayPayment
    from ..models.e_check_payment import ECheckPayment
    from ..models.in_kind_payment import InKindPayment
    from ..models.wire_payment import WirePayment


T = TypeVar("T", bound="Payment")


@_attrs_define
class Payment:
    """
    Attributes:
        id (Union[Unset, str]):
        amount (Union[Unset, float]):
        payment_status (Union[Unset, PaymentPaymentStatus]):
        note (Union[Unset, str]):
        tender_type (Union[Unset, int]):
        received_date (Union[Unset, datetime.datetime]):
        credit_card_online (Union[Unset, CreditCardOnlinePayment]):
        credit_card_offline (Union[Unset, CreditCardOfflinePayment]):
        ach (Union[Unset, ECheckPayment]):
        check (Union[Unset, CheckPayment]):
        wire (Union[Unset, WirePayment]):
        in_kind (Union[Unset, InKindPayment]):
        dafpay (Union[Unset, DafPayPayment]):
    """

    id: Union[Unset, str] = UNSET
    amount: Union[Unset, float] = UNSET
    payment_status: Union[Unset, PaymentPaymentStatus] = UNSET
    note: Union[Unset, str] = UNSET
    tender_type: Union[Unset, int] = UNSET
    received_date: Union[Unset, datetime.datetime] = UNSET
    credit_card_online: Union[Unset, "CreditCardOnlinePayment"] = UNSET
    credit_card_offline: Union[Unset, "CreditCardOfflinePayment"] = UNSET
    ach: Union[Unset, "ECheckPayment"] = UNSET
    check: Union[Unset, "CheckPayment"] = UNSET
    wire: Union[Unset, "WirePayment"] = UNSET
    in_kind: Union[Unset, "InKindPayment"] = UNSET
    dafpay: Union[Unset, "DafPayPayment"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        amount = self.amount

        payment_status: Union[Unset, str] = UNSET
        if not isinstance(self.payment_status, Unset):
            payment_status = self.payment_status.value

        note = self.note

        tender_type = self.tender_type

        received_date: Union[Unset, str] = UNSET
        if not isinstance(self.received_date, Unset):
            received_date = self.received_date.isoformat()

        credit_card_online: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credit_card_online, Unset):
            credit_card_online = self.credit_card_online.to_dict()

        credit_card_offline: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credit_card_offline, Unset):
            credit_card_offline = self.credit_card_offline.to_dict()

        ach: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ach, Unset):
            ach = self.ach.to_dict()

        check: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.check, Unset):
            check = self.check.to_dict()

        wire: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.wire, Unset):
            wire = self.wire.to_dict()

        in_kind: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.in_kind, Unset):
            in_kind = self.in_kind.to_dict()

        dafpay: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dafpay, Unset):
            dafpay = self.dafpay.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if amount is not UNSET:
            field_dict["amount"] = amount
        if payment_status is not UNSET:
            field_dict["paymentStatus"] = payment_status
        if note is not UNSET:
            field_dict["note"] = note
        if tender_type is not UNSET:
            field_dict["tenderType"] = tender_type
        if received_date is not UNSET:
            field_dict["receivedDate"] = received_date
        if credit_card_online is not UNSET:
            field_dict["creditCardOnline"] = credit_card_online
        if credit_card_offline is not UNSET:
            field_dict["creditCardOffline"] = credit_card_offline
        if ach is not UNSET:
            field_dict["ach"] = ach
        if check is not UNSET:
            field_dict["check"] = check
        if wire is not UNSET:
            field_dict["wire"] = wire
        if in_kind is not UNSET:
            field_dict["inKind"] = in_kind
        if dafpay is not UNSET:
            field_dict["dafpay"] = dafpay

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_payment import CheckPayment
        from ..models.credit_card_offline_payment import CreditCardOfflinePayment
        from ..models.credit_card_online_payment import CreditCardOnlinePayment
        from ..models.daf_pay_payment import DafPayPayment
        from ..models.e_check_payment import ECheckPayment
        from ..models.in_kind_payment import InKindPayment
        from ..models.wire_payment import WirePayment

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        amount = d.pop("amount", UNSET)

        _payment_status = d.pop("paymentStatus", UNSET)
        payment_status: Union[Unset, PaymentPaymentStatus]
        if isinstance(_payment_status, Unset):
            payment_status = UNSET
        else:
            payment_status = PaymentPaymentStatus(_payment_status)

        note = d.pop("note", UNSET)

        tender_type = d.pop("tenderType", UNSET)

        _received_date = d.pop("receivedDate", UNSET)
        received_date: Union[Unset, datetime.datetime]
        if isinstance(_received_date, Unset):
            received_date = UNSET
        else:
            received_date = isoparse(_received_date)

        _credit_card_online = d.pop("creditCardOnline", UNSET)
        credit_card_online: Union[Unset, CreditCardOnlinePayment]
        if isinstance(_credit_card_online, Unset):
            credit_card_online = UNSET
        else:
            credit_card_online = CreditCardOnlinePayment.from_dict(_credit_card_online)

        _credit_card_offline = d.pop("creditCardOffline", UNSET)
        credit_card_offline: Union[Unset, CreditCardOfflinePayment]
        if isinstance(_credit_card_offline, Unset):
            credit_card_offline = UNSET
        else:
            credit_card_offline = CreditCardOfflinePayment.from_dict(_credit_card_offline)

        _ach = d.pop("ach", UNSET)
        ach: Union[Unset, ECheckPayment]
        if isinstance(_ach, Unset):
            ach = UNSET
        else:
            ach = ECheckPayment.from_dict(_ach)

        _check = d.pop("check", UNSET)
        check: Union[Unset, CheckPayment]
        if isinstance(_check, Unset):
            check = UNSET
        else:
            check = CheckPayment.from_dict(_check)

        _wire = d.pop("wire", UNSET)
        wire: Union[Unset, WirePayment]
        if isinstance(_wire, Unset):
            wire = UNSET
        else:
            wire = WirePayment.from_dict(_wire)

        _in_kind = d.pop("inKind", UNSET)
        in_kind: Union[Unset, InKindPayment]
        if isinstance(_in_kind, Unset):
            in_kind = UNSET
        else:
            in_kind = InKindPayment.from_dict(_in_kind)

        _dafpay = d.pop("dafpay", UNSET)
        dafpay: Union[Unset, DafPayPayment]
        if isinstance(_dafpay, Unset):
            dafpay = UNSET
        else:
            dafpay = DafPayPayment.from_dict(_dafpay)

        payment = cls(
            id=id,
            amount=amount,
            payment_status=payment_status,
            note=note,
            tender_type=tender_type,
            received_date=received_date,
            credit_card_online=credit_card_online,
            credit_card_offline=credit_card_offline,
            ach=ach,
            check=check,
            wire=wire,
            in_kind=in_kind,
            dafpay=dafpay,
        )

        payment.additional_properties = d
        return payment

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
