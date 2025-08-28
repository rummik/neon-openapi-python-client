import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.recurring_donation_recurring_period_type import RecurringDonationRecurringPeriodType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.credit_card_online_payment import CreditCardOnlinePayment
    from ..models.e_check_payment import ECheckPayment
    from ..models.id_name_pair import IdNamePair
    from ..models.timestamps import Timestamps


T = TypeVar("T", bound="RecurringDonation")


@_attrs_define
class RecurringDonation:
    """
    Attributes:
        id (Union[Unset, str]):
        recurring_period (Union[Unset, int]):
        account_id (Union[Unset, str]):
        recurring_period_type (Union[Unset, RecurringDonationRecurringPeriodType]):
        amount (Union[Unset, float]):
        next_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        purpose (Union[Unset, IdNamePair]):
        campaign (Union[Unset, IdNamePair]):
        credit_card_online (Union[Unset, CreditCardOnlinePayment]):
        ach (Union[Unset, ECheckPayment]):
        fund (Union[Unset, IdNamePair]):
        donor_covered_fee_flag (Union[Unset, bool]):
        timestamps (Union[Unset, Timestamps]):
        fundraiser_account_id (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    recurring_period: Union[Unset, int] = UNSET
    account_id: Union[Unset, str] = UNSET
    recurring_period_type: Union[Unset, RecurringDonationRecurringPeriodType] = UNSET
    amount: Union[Unset, float] = UNSET
    next_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    purpose: Union[Unset, "IdNamePair"] = UNSET
    campaign: Union[Unset, "IdNamePair"] = UNSET
    credit_card_online: Union[Unset, "CreditCardOnlinePayment"] = UNSET
    ach: Union[Unset, "ECheckPayment"] = UNSET
    fund: Union[Unset, "IdNamePair"] = UNSET
    donor_covered_fee_flag: Union[Unset, bool] = UNSET
    timestamps: Union[Unset, "Timestamps"] = UNSET
    fundraiser_account_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        recurring_period = self.recurring_period

        account_id = self.account_id

        recurring_period_type: Union[Unset, str] = UNSET
        if not isinstance(self.recurring_period_type, Unset):
            recurring_period_type = self.recurring_period_type.value

        amount = self.amount

        next_date: Union[Unset, str] = UNSET
        if not isinstance(self.next_date, Unset):
            next_date = self.next_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        purpose: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.to_dict()

        campaign: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.campaign, Unset):
            campaign = self.campaign.to_dict()

        credit_card_online: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.credit_card_online, Unset):
            credit_card_online = self.credit_card_online.to_dict()

        ach: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.ach, Unset):
            ach = self.ach.to_dict()

        fund: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fund, Unset):
            fund = self.fund.to_dict()

        donor_covered_fee_flag = self.donor_covered_fee_flag

        timestamps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps.to_dict()

        fundraiser_account_id = self.fundraiser_account_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if recurring_period is not UNSET:
            field_dict["recurringPeriod"] = recurring_period
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if recurring_period_type is not UNSET:
            field_dict["recurringPeriodType"] = recurring_period_type
        if amount is not UNSET:
            field_dict["amount"] = amount
        if next_date is not UNSET:
            field_dict["nextDate"] = next_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if credit_card_online is not UNSET:
            field_dict["creditCardOnline"] = credit_card_online
        if ach is not UNSET:
            field_dict["ach"] = ach
        if fund is not UNSET:
            field_dict["fund"] = fund
        if donor_covered_fee_flag is not UNSET:
            field_dict["donorCoveredFeeFlag"] = donor_covered_fee_flag
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps
        if fundraiser_account_id is not UNSET:
            field_dict["fundraiserAccountId"] = fundraiser_account_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.credit_card_online_payment import CreditCardOnlinePayment
        from ..models.e_check_payment import ECheckPayment
        from ..models.id_name_pair import IdNamePair
        from ..models.timestamps import Timestamps

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        recurring_period = d.pop("recurringPeriod", UNSET)

        account_id = d.pop("accountId", UNSET)

        _recurring_period_type = d.pop("recurringPeriodType", UNSET)
        recurring_period_type: Union[Unset, RecurringDonationRecurringPeriodType]
        if isinstance(_recurring_period_type, Unset):
            recurring_period_type = UNSET
        else:
            recurring_period_type = RecurringDonationRecurringPeriodType(_recurring_period_type)

        amount = d.pop("amount", UNSET)

        _next_date = d.pop("nextDate", UNSET)
        next_date: Union[Unset, datetime.datetime]
        if isinstance(_next_date, Unset):
            next_date = UNSET
        else:
            next_date = isoparse(_next_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        _purpose = d.pop("purpose", UNSET)
        purpose: Union[Unset, IdNamePair]
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = IdNamePair.from_dict(_purpose)

        _campaign = d.pop("campaign", UNSET)
        campaign: Union[Unset, IdNamePair]
        if isinstance(_campaign, Unset):
            campaign = UNSET
        else:
            campaign = IdNamePair.from_dict(_campaign)

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

        _fund = d.pop("fund", UNSET)
        fund: Union[Unset, IdNamePair]
        if isinstance(_fund, Unset):
            fund = UNSET
        else:
            fund = IdNamePair.from_dict(_fund)

        donor_covered_fee_flag = d.pop("donorCoveredFeeFlag", UNSET)

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: Union[Unset, Timestamps]
        if isinstance(_timestamps, Unset):
            timestamps = UNSET
        else:
            timestamps = Timestamps.from_dict(_timestamps)

        fundraiser_account_id = d.pop("fundraiserAccountId", UNSET)

        recurring_donation = cls(
            id=id,
            recurring_period=recurring_period,
            account_id=account_id,
            recurring_period_type=recurring_period_type,
            amount=amount,
            next_date=next_date,
            end_date=end_date,
            purpose=purpose,
            campaign=campaign,
            credit_card_online=credit_card_online,
            ach=ach,
            fund=fund,
            donor_covered_fee_flag=donor_covered_fee_flag,
            timestamps=timestamps,
            fundraiser_account_id=fundraiser_account_id,
        )

        recurring_donation.additional_properties = d
        return recurring_donation

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
