import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.donation_item_anonymous_type import DonationItemAnonymousType
from ..models.donation_item_status import DonationItemStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acknowledgee import Acknowledgee
    from ..models.cra_info import CraInfo
    from ..models.custom_field import CustomField
    from ..models.id_name_pair import IdNamePair
    from ..models.origin import Origin
    from ..models.solicitor import Solicitor
    from ..models.tax_deducible_info import TaxDeducibleInfo
    from ..models.timestamps import Timestamps
    from ..models.tribute import Tribute


T = TypeVar("T", bound="DonationItem")


@_attrs_define
class DonationItem:
    """
    Attributes:
        donor_name (Union[Unset, str]):
        id (Union[Unset, str]):
        send_acknowledge_email (Union[Unset, bool]):
        account_id (Union[Unset, str]):
        batch_number (Union[Unset, str]):
        date (Union[Unset, datetime.datetime]):
        amount (Union[Unset, float]):
        anonymous_type (Union[Unset, DonationItemAnonymousType]):
        status (Union[Unset, DonationItemStatus]):
        cra_info (Union[Unset, CraInfo]):
        tax_deductible_info (Union[Unset, TaxDeducibleInfo]):
        origin (Union[Unset, Origin]):
        purpose (Union[Unset, IdNamePair]):
        source (Union[Unset, IdNamePair]):
        campaign (Union[Unset, IdNamePair]):
        solicitation_method (Union[Unset, IdNamePair]):
        acknowledgee (Union[Unset, Acknowledgee]):
        fund (Union[Unset, IdNamePair]):
        timestamps (Union[Unset, Timestamps]):
        tribute (Union[Unset, Tribute]):
        donation_custom_fields (Union[Unset, list['CustomField']]):
        solicitor (Union[Unset, Solicitor]):
        fundraiser_account_id (Union[Unset, str]):
    """

    donor_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    send_acknowledge_email: Union[Unset, bool] = UNSET
    account_id: Union[Unset, str] = UNSET
    batch_number: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    amount: Union[Unset, float] = UNSET
    anonymous_type: Union[Unset, DonationItemAnonymousType] = UNSET
    status: Union[Unset, DonationItemStatus] = UNSET
    cra_info: Union[Unset, "CraInfo"] = UNSET
    tax_deductible_info: Union[Unset, "TaxDeducibleInfo"] = UNSET
    origin: Union[Unset, "Origin"] = UNSET
    purpose: Union[Unset, "IdNamePair"] = UNSET
    source: Union[Unset, "IdNamePair"] = UNSET
    campaign: Union[Unset, "IdNamePair"] = UNSET
    solicitation_method: Union[Unset, "IdNamePair"] = UNSET
    acknowledgee: Union[Unset, "Acknowledgee"] = UNSET
    fund: Union[Unset, "IdNamePair"] = UNSET
    timestamps: Union[Unset, "Timestamps"] = UNSET
    tribute: Union[Unset, "Tribute"] = UNSET
    donation_custom_fields: Union[Unset, list["CustomField"]] = UNSET
    solicitor: Union[Unset, "Solicitor"] = UNSET
    fundraiser_account_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        donor_name = self.donor_name

        id = self.id

        send_acknowledge_email = self.send_acknowledge_email

        account_id = self.account_id

        batch_number = self.batch_number

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        amount = self.amount

        anonymous_type: Union[Unset, str] = UNSET
        if not isinstance(self.anonymous_type, Unset):
            anonymous_type = self.anonymous_type.value

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        cra_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cra_info, Unset):
            cra_info = self.cra_info.to_dict()

        tax_deductible_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_deductible_info, Unset):
            tax_deductible_info = self.tax_deductible_info.to_dict()

        origin: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.origin, Unset):
            origin = self.origin.to_dict()

        purpose: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.to_dict()

        source: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.source, Unset):
            source = self.source.to_dict()

        campaign: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.campaign, Unset):
            campaign = self.campaign.to_dict()

        solicitation_method: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.solicitation_method, Unset):
            solicitation_method = self.solicitation_method.to_dict()

        acknowledgee: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.acknowledgee, Unset):
            acknowledgee = self.acknowledgee.to_dict()

        fund: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fund, Unset):
            fund = self.fund.to_dict()

        timestamps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps.to_dict()

        tribute: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tribute, Unset):
            tribute = self.tribute.to_dict()

        donation_custom_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.donation_custom_fields, Unset):
            donation_custom_fields = []
            for donation_custom_fields_item_data in self.donation_custom_fields:
                donation_custom_fields_item = donation_custom_fields_item_data.to_dict()
                donation_custom_fields.append(donation_custom_fields_item)

        solicitor: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.solicitor, Unset):
            solicitor = self.solicitor.to_dict()

        fundraiser_account_id = self.fundraiser_account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if donor_name is not UNSET:
            field_dict["donorName"] = donor_name
        if id is not UNSET:
            field_dict["id"] = id
        if send_acknowledge_email is not UNSET:
            field_dict["sendAcknowledgeEmail"] = send_acknowledge_email
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if batch_number is not UNSET:
            field_dict["batchNumber"] = batch_number
        if date is not UNSET:
            field_dict["date"] = date
        if amount is not UNSET:
            field_dict["amount"] = amount
        if anonymous_type is not UNSET:
            field_dict["anonymousType"] = anonymous_type
        if status is not UNSET:
            field_dict["status"] = status
        if cra_info is not UNSET:
            field_dict["craInfo"] = cra_info
        if tax_deductible_info is not UNSET:
            field_dict["taxDeductibleInfo"] = tax_deductible_info
        if origin is not UNSET:
            field_dict["origin"] = origin
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if source is not UNSET:
            field_dict["source"] = source
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if solicitation_method is not UNSET:
            field_dict["solicitationMethod"] = solicitation_method
        if acknowledgee is not UNSET:
            field_dict["acknowledgee"] = acknowledgee
        if fund is not UNSET:
            field_dict["fund"] = fund
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps
        if tribute is not UNSET:
            field_dict["tribute"] = tribute
        if donation_custom_fields is not UNSET:
            field_dict["donationCustomFields"] = donation_custom_fields
        if solicitor is not UNSET:
            field_dict["solicitor"] = solicitor
        if fundraiser_account_id is not UNSET:
            field_dict["fundraiserAccountId"] = fundraiser_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acknowledgee import Acknowledgee
        from ..models.cra_info import CraInfo
        from ..models.custom_field import CustomField
        from ..models.id_name_pair import IdNamePair
        from ..models.origin import Origin
        from ..models.solicitor import Solicitor
        from ..models.tax_deducible_info import TaxDeducibleInfo
        from ..models.timestamps import Timestamps
        from ..models.tribute import Tribute

        d = dict(src_dict)
        donor_name = d.pop("donorName", UNSET)

        id = d.pop("id", UNSET)

        send_acknowledge_email = d.pop("sendAcknowledgeEmail", UNSET)

        account_id = d.pop("accountId", UNSET)

        batch_number = d.pop("batchNumber", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        amount = d.pop("amount", UNSET)

        _anonymous_type = d.pop("anonymousType", UNSET)
        anonymous_type: Union[Unset, DonationItemAnonymousType]
        if isinstance(_anonymous_type, Unset):
            anonymous_type = UNSET
        else:
            anonymous_type = DonationItemAnonymousType(_anonymous_type)

        _status = d.pop("status", UNSET)
        status: Union[Unset, DonationItemStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = DonationItemStatus(_status)

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

        _origin = d.pop("origin", UNSET)
        origin: Union[Unset, Origin]
        if isinstance(_origin, Unset):
            origin = UNSET
        else:
            origin = Origin.from_dict(_origin)

        _purpose = d.pop("purpose", UNSET)
        purpose: Union[Unset, IdNamePair]
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = IdNamePair.from_dict(_purpose)

        _source = d.pop("source", UNSET)
        source: Union[Unset, IdNamePair]
        if isinstance(_source, Unset):
            source = UNSET
        else:
            source = IdNamePair.from_dict(_source)

        _campaign = d.pop("campaign", UNSET)
        campaign: Union[Unset, IdNamePair]
        if isinstance(_campaign, Unset):
            campaign = UNSET
        else:
            campaign = IdNamePair.from_dict(_campaign)

        _solicitation_method = d.pop("solicitationMethod", UNSET)
        solicitation_method: Union[Unset, IdNamePair]
        if isinstance(_solicitation_method, Unset):
            solicitation_method = UNSET
        else:
            solicitation_method = IdNamePair.from_dict(_solicitation_method)

        _acknowledgee = d.pop("acknowledgee", UNSET)
        acknowledgee: Union[Unset, Acknowledgee]
        if isinstance(_acknowledgee, Unset):
            acknowledgee = UNSET
        else:
            acknowledgee = Acknowledgee.from_dict(_acknowledgee)

        _fund = d.pop("fund", UNSET)
        fund: Union[Unset, IdNamePair]
        if isinstance(_fund, Unset):
            fund = UNSET
        else:
            fund = IdNamePair.from_dict(_fund)

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: Union[Unset, Timestamps]
        if isinstance(_timestamps, Unset):
            timestamps = UNSET
        else:
            timestamps = Timestamps.from_dict(_timestamps)

        _tribute = d.pop("tribute", UNSET)
        tribute: Union[Unset, Tribute]
        if isinstance(_tribute, Unset):
            tribute = UNSET
        else:
            tribute = Tribute.from_dict(_tribute)

        donation_custom_fields = []
        _donation_custom_fields = d.pop("donationCustomFields", UNSET)
        for donation_custom_fields_item_data in _donation_custom_fields or []:
            donation_custom_fields_item = CustomField.from_dict(donation_custom_fields_item_data)

            donation_custom_fields.append(donation_custom_fields_item)

        _solicitor = d.pop("solicitor", UNSET)
        solicitor: Union[Unset, Solicitor]
        if isinstance(_solicitor, Unset):
            solicitor = UNSET
        else:
            solicitor = Solicitor.from_dict(_solicitor)

        fundraiser_account_id = d.pop("fundraiserAccountId", UNSET)

        donation_item = cls(
            donor_name=donor_name,
            id=id,
            send_acknowledge_email=send_acknowledge_email,
            account_id=account_id,
            batch_number=batch_number,
            date=date,
            amount=amount,
            anonymous_type=anonymous_type,
            status=status,
            cra_info=cra_info,
            tax_deductible_info=tax_deductible_info,
            origin=origin,
            purpose=purpose,
            source=source,
            campaign=campaign,
            solicitation_method=solicitation_method,
            acknowledgee=acknowledgee,
            fund=fund,
            timestamps=timestamps,
            tribute=tribute,
            donation_custom_fields=donation_custom_fields,
            solicitor=solicitor,
            fundraiser_account_id=fundraiser_account_id,
        )

        donation_item.additional_properties = d
        return donation_item

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
