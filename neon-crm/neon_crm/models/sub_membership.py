import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.sub_membership_change_type import SubMembershipChangeType
from ..models.sub_membership_enroll_type import SubMembershipEnrollType
from ..models.sub_membership_status import SubMembershipStatus
from ..models.sub_membership_term_unit import SubMembershipTermUnit
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.cra_info import CraInfo
    from ..models.custom_field import CustomField
    from ..models.id_name_pair import IdNamePair
    from ..models.origin import Origin
    from ..models.tax_deducible_info import TaxDeducibleInfo
    from ..models.timestamps import Timestamps


T = TypeVar("T", bound="SubMembership")


@_attrs_define
class SubMembership:
    """
    Attributes:
        id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        account_id (Union[Unset, str]):
        membership_level (Union[Unset, IdNamePair]):
        membership_term (Union[Unset, IdNamePair]):
        auto_renewal (Union[Unset, bool]):
        source (Union[Unset, IdNamePair]):
        change_type (Union[Unset, SubMembershipChangeType]):
        term_unit (Union[Unset, SubMembershipTermUnit]):
        term_duration (Union[Unset, int]):
        enroll_type (Union[Unset, SubMembershipEnrollType]):
        transaction_date (Union[Unset, datetime.datetime]):
        term_start_date (Union[Unset, datetime.datetime]):
        term_end_date (Union[Unset, datetime.datetime]):
        fee (Union[Unset, float]):
        coupon_code (Union[Unset, str]):
        send_acknowledge_email (Union[Unset, bool]):
        status (Union[Unset, SubMembershipStatus]):
        complimentary (Union[Unset, int]): 1: Complimentary memberships because of donations made.<br>2: Complimentary
            memberships through the combination of past membership fees.<br>3: Complimentary memberships through the
            combination of donations made and previous membership fees.
        membership_custom_fields (Union[Unset, list['CustomField']]):
        cra_info (Union[Unset, CraInfo]):
        tax_deductible_info (Union[Unset, TaxDeducibleInfo]):
        timestamps (Union[Unset, Timestamps]):
        origin (Union[Unset, Origin]):
        send_auto_renewal_enabled_email (Union[Unset, bool]):
        is_current_employee (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    parent_id: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    membership_level: Union[Unset, "IdNamePair"] = UNSET
    membership_term: Union[Unset, "IdNamePair"] = UNSET
    auto_renewal: Union[Unset, bool] = UNSET
    source: Union[Unset, "IdNamePair"] = UNSET
    change_type: Union[Unset, SubMembershipChangeType] = UNSET
    term_unit: Union[Unset, SubMembershipTermUnit] = UNSET
    term_duration: Union[Unset, int] = UNSET
    enroll_type: Union[Unset, SubMembershipEnrollType] = UNSET
    transaction_date: Union[Unset, datetime.datetime] = UNSET
    term_start_date: Union[Unset, datetime.datetime] = UNSET
    term_end_date: Union[Unset, datetime.datetime] = UNSET
    fee: Union[Unset, float] = UNSET
    coupon_code: Union[Unset, str] = UNSET
    send_acknowledge_email: Union[Unset, bool] = UNSET
    status: Union[Unset, SubMembershipStatus] = UNSET
    complimentary: Union[Unset, int] = UNSET
    membership_custom_fields: Union[Unset, list["CustomField"]] = UNSET
    cra_info: Union[Unset, "CraInfo"] = UNSET
    tax_deductible_info: Union[Unset, "TaxDeducibleInfo"] = UNSET
    timestamps: Union[Unset, "Timestamps"] = UNSET
    origin: Union[Unset, "Origin"] = UNSET
    send_auto_renewal_enabled_email: Union[Unset, bool] = UNSET
    is_current_employee: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        parent_id = self.parent_id

        account_id = self.account_id

        membership_level: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.membership_level, Unset):
            membership_level = self.membership_level.to_dict()

        membership_term: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.membership_term, Unset):
            membership_term = self.membership_term.to_dict()

        auto_renewal = self.auto_renewal

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        change_type: Union[Unset, str] = UNSET
        if not isinstance(self.change_type, Unset):
            change_type = self.change_type.value

        term_unit: Union[Unset, str] = UNSET
        if not isinstance(self.term_unit, Unset):
            term_unit = self.term_unit.value

        term_duration = self.term_duration

        enroll_type: Union[Unset, str] = UNSET
        if not isinstance(self.enroll_type, Unset):
            enroll_type = self.enroll_type.value

        transaction_date: Union[Unset, str] = UNSET
        if not isinstance(self.transaction_date, Unset):
            transaction_date = self.transaction_date.isoformat()

        term_start_date: Union[Unset, str] = UNSET
        if not isinstance(self.term_start_date, Unset):
            term_start_date = self.term_start_date.isoformat()

        term_end_date: Union[Unset, str] = UNSET
        if not isinstance(self.term_end_date, Unset):
            term_end_date = self.term_end_date.isoformat()

        fee = self.fee

        coupon_code = self.coupon_code

        send_acknowledge_email = self.send_acknowledge_email

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        complimentary = self.complimentary

        membership_custom_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.membership_custom_fields, Unset):
            membership_custom_fields = []
            for membership_custom_fields_item_data in self.membership_custom_fields:
                membership_custom_fields_item = membership_custom_fields_item_data.to_dict()
                membership_custom_fields.append(membership_custom_fields_item)

        cra_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cra_info, Unset):
            cra_info = self.cra_info.to_dict()

        tax_deductible_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_deductible_info, Unset):
            tax_deductible_info = self.tax_deductible_info.to_dict()

        timestamps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps.to_dict()

        origin: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.to_dict()

        send_auto_renewal_enabled_email = self.send_auto_renewal_enabled_email

        is_current_employee = self.is_current_employee

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if parent_id is not UNSET:
            field_dict["parentId"] = parent_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if membership_level is not UNSET:
            field_dict["membershipLevel"] = membership_level
        if membership_term is not UNSET:
            field_dict["membershipTerm"] = membership_term
        if auto_renewal is not UNSET:
            field_dict["autoRenewal"] = auto_renewal
        if source is not UNSET:
            field_dict["source"] = source
        if change_type is not UNSET:
            field_dict["changeType"] = change_type
        if term_unit is not UNSET:
            field_dict["termUnit"] = term_unit
        if term_duration is not UNSET:
            field_dict["termDuration"] = term_duration
        if enroll_type is not UNSET:
            field_dict["enrollType"] = enroll_type
        if transaction_date is not UNSET:
            field_dict["transactionDate"] = transaction_date
        if term_start_date is not UNSET:
            field_dict["termStartDate"] = term_start_date
        if term_end_date is not UNSET:
            field_dict["termEndDate"] = term_end_date
        if fee is not UNSET:
            field_dict["fee"] = fee
        if coupon_code is not UNSET:
            field_dict["couponCode"] = coupon_code
        if send_acknowledge_email is not UNSET:
            field_dict["sendAcknowledgeEmail"] = send_acknowledge_email
        if status is not UNSET:
            field_dict["status"] = status
        if complimentary is not UNSET:
            field_dict["complimentary"] = complimentary
        if membership_custom_fields is not UNSET:
            field_dict["membershipCustomFields"] = membership_custom_fields
        if cra_info is not UNSET:
            field_dict["craInfo"] = cra_info
        if tax_deductible_info is not UNSET:
            field_dict["taxDeductibleInfo"] = tax_deductible_info
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps
        if origin is not UNSET:
            field_dict["origin"] = origin
        if send_auto_renewal_enabled_email is not UNSET:
            field_dict["sendAutoRenewalEnabledEmail"] = send_auto_renewal_enabled_email
        if is_current_employee is not UNSET:
            field_dict["isCurrentEmployee"] = is_current_employee

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.cra_info import CraInfo
        from ..models.custom_field import CustomField
        from ..models.id_name_pair import IdNamePair
        from ..models.origin import Origin
        from ..models.tax_deducible_info import TaxDeducibleInfo
        from ..models.timestamps import Timestamps

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        parent_id = d.pop("parentId", UNSET)

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

        auto_renewal = d.pop("autoRenewal", UNSET)

        _source = d.pop("source", UNSET)
        source: Union[Unset, IdNamePair]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = IdNamePair.from_dict(_source)

        _change_type = d.pop("changeType", UNSET)
        change_type: Union[Unset, SubMembershipChangeType]
        if isinstance(_change_type, Unset):
            change_type = UNSET
        else:
            change_type = SubMembershipChangeType(_change_type)

        _term_unit = d.pop("termUnit", UNSET)
        term_unit: Union[Unset, SubMembershipTermUnit]
        if isinstance(_term_unit, Unset):
            term_unit = UNSET
        else:
            term_unit = SubMembershipTermUnit(_term_unit)

        term_duration = d.pop("termDuration", UNSET)

        _enroll_type = d.pop("enrollType", UNSET)
        enroll_type: Union[Unset, SubMembershipEnrollType]
        if isinstance(_enroll_type, Unset):
            enroll_type = UNSET
        else:
            enroll_type = SubMembershipEnrollType(_enroll_type)

        _transaction_date = d.pop("transactionDate", UNSET)
        transaction_date: Union[Unset, datetime.datetime]
        if isinstance(_transaction_date, Unset):
            transaction_date = UNSET
        else:
            transaction_date = isoparse(_transaction_date)

        _term_start_date = d.pop("termStartDate", UNSET)
        term_start_date: Union[Unset, datetime.datetime]
        if isinstance(_term_start_date, Unset):
            term_start_date = UNSET
        else:
            term_start_date = isoparse(_term_start_date)

        _term_end_date = d.pop("termEndDate", UNSET)
        term_end_date: Union[Unset, datetime.datetime]
        if isinstance(_term_end_date, Unset):
            term_end_date = UNSET
        else:
            term_end_date = isoparse(_term_end_date)

        fee = d.pop("fee", UNSET)

        coupon_code = d.pop("couponCode", UNSET)

        send_acknowledge_email = d.pop("sendAcknowledgeEmail", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, SubMembershipStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = SubMembershipStatus(_status)

        complimentary = d.pop("complimentary", UNSET)

        membership_custom_fields = []
        _membership_custom_fields = d.pop("membershipCustomFields", UNSET)
        for membership_custom_fields_item_data in _membership_custom_fields or []:
            membership_custom_fields_item = CustomField.from_dict(membership_custom_fields_item_data)

            membership_custom_fields.append(membership_custom_fields_item)

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

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: Union[Unset, Timestamps]
        if isinstance(_timestamps, Unset):
            timestamps = UNSET
        else:
            timestamps = Timestamps.from_dict(_timestamps)

        _origin = d.pop("origin", UNSET)
        origin: Union[Unset, Origin]
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = Origin.from_dict(_origin)

        send_auto_renewal_enabled_email = d.pop("sendAutoRenewalEnabledEmail", UNSET)

        is_current_employee = d.pop("isCurrentEmployee", UNSET)

        sub_membership = cls(
            id=id,
            parent_id=parent_id,
            account_id=account_id,
            membership_level=membership_level,
            membership_term=membership_term,
            auto_renewal=auto_renewal,
            source=source,
            change_type=change_type,
            term_unit=term_unit,
            term_duration=term_duration,
            enroll_type=enroll_type,
            transaction_date=transaction_date,
            term_start_date=term_start_date,
            term_end_date=term_end_date,
            fee=fee,
            coupon_code=coupon_code,
            send_acknowledge_email=send_acknowledge_email,
            status=status,
            complimentary=complimentary,
            membership_custom_fields=membership_custom_fields,
            cra_info=cra_info,
            tax_deductible_info=tax_deductible_info,
            timestamps=timestamps,
            origin=origin,
            send_auto_renewal_enabled_email=send_auto_renewal_enabled_email,
            is_current_employee=is_current_employee,
        )

        sub_membership.additional_properties = d
        return sub_membership

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
