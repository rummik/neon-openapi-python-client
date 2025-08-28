import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cra_info import CraInfo
    from ..models.origin import Origin
    from ..models.payment import Payment
    from ..models.tax_deducible_info import TaxDeducibleInfo
    from ..models.timestamps import Timestamps


T = TypeVar("T", bound="PledgePayment")


@_attrs_define
class PledgePayment:
    """
    Attributes:
        id (Union[Unset, str]):
        pledge_id (Union[Unset, str]):
        date (Union[Unset, datetime.datetime]):
        installment_id (Union[Unset, str]):
        payment (Union[Unset, Payment]):
        timestamps (Union[Unset, Timestamps]):
        cra_info (Union[Unset, CraInfo]):
        tax_deductible_info (Union[Unset, TaxDeducibleInfo]):
        donor_covered_fee_flag (Union[Unset, bool]):
        donor_covered_fee (Union[Unset, float]):
        origin (Union[Unset, Origin]):
        send_matched_donor_email (Union[Unset, bool]):
        send_matched_donor_letter (Union[Unset, bool]):
        send_acknowledge_email (Union[Unset, bool]):
        send_acknowledge_letter (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    pledge_id: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    installment_id: Union[Unset, str] = UNSET
    payment: Union[Unset, "Payment"] = UNSET
    timestamps: Union[Unset, "Timestamps"] = UNSET
    cra_info: Union[Unset, "CraInfo"] = UNSET
    tax_deductible_info: Union[Unset, "TaxDeducibleInfo"] = UNSET
    donor_covered_fee_flag: Union[Unset, bool] = UNSET
    donor_covered_fee: Union[Unset, float] = UNSET
    origin: Union[Unset, "Origin"] = UNSET
    send_matched_donor_email: Union[Unset, bool] = UNSET
    send_matched_donor_letter: Union[Unset, bool] = UNSET
    send_acknowledge_email: Union[Unset, bool] = UNSET
    send_acknowledge_letter: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        pledge_id = self.pledge_id

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        installment_id = self.installment_id

        payment: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.payment, Unset):
            payment = self.payment.to_dict()

        timestamps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps.to_dict()

        cra_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cra_info, Unset):
            cra_info = self.cra_info.to_dict()

        tax_deductible_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_deductible_info, Unset):
            tax_deductible_info = self.tax_deductible_info.to_dict()

        donor_covered_fee_flag = self.donor_covered_fee_flag

        donor_covered_fee = self.donor_covered_fee

        origin: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.to_dict()

        send_matched_donor_email = self.send_matched_donor_email

        send_matched_donor_letter = self.send_matched_donor_letter

        send_acknowledge_email = self.send_acknowledge_email

        send_acknowledge_letter = self.send_acknowledge_letter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if pledge_id is not UNSET:
            field_dict["pledgeId"] = pledge_id
        if date is not UNSET:
            field_dict["date"] = date
        if installment_id is not UNSET:
            field_dict["installmentId"] = installment_id
        if payment is not UNSET:
            field_dict["payment"] = payment
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps
        if cra_info is not UNSET:
            field_dict["craInfo"] = cra_info
        if tax_deductible_info is not UNSET:
            field_dict["taxDeductibleInfo"] = tax_deductible_info
        if donor_covered_fee_flag is not UNSET:
            field_dict["donorCoveredFeeFlag"] = donor_covered_fee_flag
        if donor_covered_fee is not UNSET:
            field_dict["donorCoveredFee"] = donor_covered_fee
        if origin is not UNSET:
            field_dict["origin"] = origin
        if send_matched_donor_email is not UNSET:
            field_dict["sendMatchedDonorEmail"] = send_matched_donor_email
        if send_matched_donor_letter is not UNSET:
            field_dict["sendMatchedDonorLetter"] = send_matched_donor_letter
        if send_acknowledge_email is not UNSET:
            field_dict["sendAcknowledgeEmail"] = send_acknowledge_email
        if send_acknowledge_letter is not UNSET:
            field_dict["sendAcknowledgeLetter"] = send_acknowledge_letter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cra_info import CraInfo
        from ..models.origin import Origin
        from ..models.payment import Payment
        from ..models.tax_deducible_info import TaxDeducibleInfo
        from ..models.timestamps import Timestamps

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        pledge_id = d.pop("pledgeId", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        installment_id = d.pop("installmentId", UNSET)

        _payment = d.pop("payment", UNSET)
        payment: Union[Unset, Payment]
        if isinstance(_payment, Unset):
            payment = UNSET
        else:
            payment = Payment.from_dict(_payment)

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: Union[Unset, Timestamps]
        if isinstance(_timestamps, Unset):
            timestamps = UNSET
        else:
            timestamps = Timestamps.from_dict(_timestamps)

        _cra_info = d.pop("craInfo", UNSET)
        cra_info: Union[Unset, CraInfo]
        if isinstance(_cra_info, Unset):
            cra_info = UNSET
        else:
            cra_info = CraInfo.from_dict(_cra_info)

        _tax_deductible_info = d.pop("taxDeductibleInfo", UNSET)
        tax_deductible_info: Union[Unset, TaxDeducibleInfo]
        if isinstance(_tax_deductible_info, Unset):
            tax_deductible_info = UNSET
        else:
            tax_deductible_info = TaxDeducibleInfo.from_dict(_tax_deductible_info)

        donor_covered_fee_flag = d.pop("donorCoveredFeeFlag", UNSET)

        donor_covered_fee = d.pop("donorCoveredFee", UNSET)

        _origin = d.pop("origin", UNSET)
        origin: Union[Unset, Origin]
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = Origin.from_dict(_origin)

        send_matched_donor_email = d.pop("sendMatchedDonorEmail", UNSET)

        send_matched_donor_letter = d.pop("sendMatchedDonorLetter", UNSET)

        send_acknowledge_email = d.pop("sendAcknowledgeEmail", UNSET)

        send_acknowledge_letter = d.pop("sendAcknowledgeLetter", UNSET)

        pledge_payment = cls(
            id=id,
            pledge_id=pledge_id,
            date=date,
            installment_id=installment_id,
            payment=payment,
            timestamps=timestamps,
            cra_info=cra_info,
            tax_deductible_info=tax_deductible_info,
            donor_covered_fee_flag=donor_covered_fee_flag,
            donor_covered_fee=donor_covered_fee,
            origin=origin,
            send_matched_donor_email=send_matched_donor_email,
            send_matched_donor_letter=send_matched_donor_letter,
            send_acknowledge_email=send_acknowledge_email,
            send_acknowledge_letter=send_acknowledge_letter,
        )

        pledge_payment.additional_properties = d
        return pledge_payment

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
