import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.pledge_anonymous_type import PledgeAnonymousType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.acknowledgee import Acknowledgee
    from ..models.custom_field import CustomField
    from ..models.id_name_pair import IdNamePair
    from ..models.pledge_daf_pay_distribution import PledgeDafPayDistribution
    from ..models.solicitor import Solicitor
    from ..models.timestamps import Timestamps
    from ..models.tribute import Tribute


T = TypeVar("T", bound="Pledge")


@_attrs_define
class Pledge:
    """
    Attributes:
        donor_name (Union[Unset, str]):
        id (Union[Unset, str]):
        matched_donation_id (Union[Unset, str]):
        account_id (Union[Unset, str]):
        date (Union[Unset, datetime.datetime]):
        amount (Union[Unset, float]):
        anonymous_type (Union[Unset, PledgeAnonymousType]):
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
        expected_date (Union[Unset, datetime.datetime]):
        dafpay (Union[Unset, PledgeDafPayDistribution]):
    """

    donor_name: Union[Unset, str] = UNSET
    id: Union[Unset, str] = UNSET
    matched_donation_id: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    date: Union[Unset, datetime.datetime] = UNSET
    amount: Union[Unset, float] = UNSET
    anonymous_type: Union[Unset, PledgeAnonymousType] = UNSET
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
    expected_date: Union[Unset, datetime.datetime] = UNSET
    dafpay: Union[Unset, "PledgeDafPayDistribution"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        donor_name = self.donor_name

        id = self.id

        matched_donation_id = self.matched_donation_id

        account_id = self.account_id

        date: Union[Unset, str] = UNSET
        if not isinstance(self.date, Unset):
            date = self.date.isoformat()

        amount = self.amount

        anonymous_type: Union[Unset, str] = UNSET
        if not isinstance(self.anonymous_type, Unset):
            anonymous_type = self.anonymous_type.value

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

        expected_date: Union[Unset, str] = UNSET
        if not isinstance(self.expected_date, Unset):
            expected_date = self.expected_date.isoformat()

        dafpay: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.dafpay, Unset):
            dafpay = self.dafpay.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if donor_name is not UNSET:
            field_dict["donorName"] = donor_name
        if id is not UNSET:
            field_dict["id"] = id
        if matched_donation_id is not UNSET:
            field_dict["matchedDonationId"] = matched_donation_id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if date is not UNSET:
            field_dict["date"] = date
        if amount is not UNSET:
            field_dict["amount"] = amount
        if anonymous_type is not UNSET:
            field_dict["anonymousType"] = anonymous_type
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
        if expected_date is not UNSET:
            field_dict["expectedDate"] = expected_date
        if dafpay is not UNSET:
            field_dict["dafpay"] = dafpay

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.acknowledgee import Acknowledgee
        from ..models.custom_field import CustomField
        from ..models.id_name_pair import IdNamePair
        from ..models.pledge_daf_pay_distribution import PledgeDafPayDistribution
        from ..models.solicitor import Solicitor
        from ..models.timestamps import Timestamps
        from ..models.tribute import Tribute

        d = dict(src_dict)
        donor_name = d.pop("donorName", UNSET)

        id = d.pop("id", UNSET)

        matched_donation_id = d.pop("matchedDonationId", UNSET)

        account_id = d.pop("accountId", UNSET)

        _date = d.pop("date", UNSET)
        date: Union[Unset, datetime.datetime]
        if isinstance(_date, Unset):
            date = UNSET
        else:
            date = isoparse(_date)

        amount = d.pop("amount", UNSET)

        _anonymous_type = d.pop("anonymousType", UNSET)
        anonymous_type: Union[Unset, PledgeAnonymousType]
        if isinstance(_anonymous_type, Unset):
            anonymous_type = UNSET
        else:
            anonymous_type = PledgeAnonymousType(_anonymous_type)

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

        _expected_date = d.pop("expectedDate", UNSET)
        expected_date: Union[Unset, datetime.datetime]
        if isinstance(_expected_date, Unset):
            expected_date = UNSET
        else:
            expected_date = isoparse(_expected_date)

        _dafpay = d.pop("dafpay", UNSET)
        dafpay: Union[Unset, PledgeDafPayDistribution]
        if isinstance(_dafpay, Unset):
            dafpay = UNSET
        else:
            dafpay = PledgeDafPayDistribution.from_dict(_dafpay)

        pledge = cls(
            donor_name=donor_name,
            id=id,
            matched_donation_id=matched_donation_id,
            account_id=account_id,
            date=date,
            amount=amount,
            anonymous_type=anonymous_type,
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
            expected_date=expected_date,
            dafpay=dafpay,
        )

        pledge.additional_properties = d
        return pledge

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
