import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.campaign_status import CampaignStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.campaign_stats import CampaignStats
    from ..models.cra_info import CraInfo
    from ..models.id_name_pair import IdNamePair
    from ..models.social_fundraising import SocialFundraising
    from ..models.tax_deducible_info import TaxDeducibleInfo


T = TypeVar("T", bound="Campaign")


@_attrs_define
class Campaign:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        code (Union[Unset, str]):
        start_date (Union[Unset, datetime.datetime]):
        end_date (Union[Unset, datetime.datetime]):
        fund (Union[Unset, IdNamePair]):
        purpose (Union[Unset, IdNamePair]):
        parent_campaign (Union[Unset, IdNamePair]):
        page_content (Union[Unset, str]):
        status (Union[Unset, CampaignStatus]):
        goal (Union[Unset, float]):
        campaign_page_url (Union[Unset, str]):
        donation_form_url (Union[Unset, str]):
        statistics (Union[Unset, CampaignStats]):
        social_fundraising (Union[Unset, SocialFundraising]):
        cra_info (Union[Unset, CraInfo]):
        tax_deductible_info (Union[Unset, TaxDeducibleInfo]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    start_date: Union[Unset, datetime.datetime] = UNSET
    end_date: Union[Unset, datetime.datetime] = UNSET
    fund: Union[Unset, "IdNamePair"] = UNSET
    purpose: Union[Unset, "IdNamePair"] = UNSET
    parent_campaign: Union[Unset, "IdNamePair"] = UNSET
    page_content: Union[Unset, str] = UNSET
    status: Union[Unset, CampaignStatus] = UNSET
    goal: Union[Unset, float] = UNSET
    campaign_page_url: Union[Unset, str] = UNSET
    donation_form_url: Union[Unset, str] = UNSET
    statistics: Union[Unset, "CampaignStats"] = UNSET
    social_fundraising: Union[Unset, "SocialFundraising"] = UNSET
    cra_info: Union[Unset, "CraInfo"] = UNSET
    tax_deductible_info: Union[Unset, "TaxDeducibleInfo"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        code = self.code

        start_date: Union[Unset, str] = UNSET
        if not isinstance(self.start_date, Unset):
            start_date = self.start_date.isoformat()

        end_date: Union[Unset, str] = UNSET
        if not isinstance(self.end_date, Unset):
            end_date = self.end_date.isoformat()

        fund: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fund, Unset):
            fund = self.fund.to_dict()

        purpose: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.to_dict()

        parent_campaign: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.parent_campaign, Unset):
            parent_campaign = self.parent_campaign.to_dict()

        page_content = self.page_content

        status: Union[Unset, str] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        goal = self.goal

        campaign_page_url = self.campaign_page_url

        donation_form_url = self.donation_form_url

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        social_fundraising: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.social_fundraising, Unset):
            social_fundraising = self.social_fundraising.to_dict()

        cra_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.cra_info, Unset):
            cra_info = self.cra_info.to_dict()

        tax_deductible_info: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.tax_deductible_info, Unset):
            tax_deductible_info = self.tax_deductible_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if code is not UNSET:
            field_dict["code"] = code
        if start_date is not UNSET:
            field_dict["startDate"] = start_date
        if end_date is not UNSET:
            field_dict["endDate"] = end_date
        if fund is not UNSET:
            field_dict["fund"] = fund
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if parent_campaign is not UNSET:
            field_dict["parentCampaign"] = parent_campaign
        if page_content is not UNSET:
            field_dict["pageContent"] = page_content
        if status is not UNSET:
            field_dict["status"] = status
        if goal is not UNSET:
            field_dict["goal"] = goal
        if campaign_page_url is not UNSET:
            field_dict["campaignPageUrl"] = campaign_page_url
        if donation_form_url is not UNSET:
            field_dict["donationFormUrl"] = donation_form_url
        if statistics is not UNSET:
            field_dict["statistics"] = statistics
        if social_fundraising is not UNSET:
            field_dict["socialFundraising"] = social_fundraising
        if cra_info is not UNSET:
            field_dict["craInfo"] = cra_info
        if tax_deductible_info is not UNSET:
            field_dict["taxDeductibleInfo"] = tax_deductible_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.campaign_stats import CampaignStats
        from ..models.cra_info import CraInfo
        from ..models.id_name_pair import IdNamePair
        from ..models.social_fundraising import SocialFundraising
        from ..models.tax_deducible_info import TaxDeducibleInfo

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        code = d.pop("code", UNSET)

        _start_date = d.pop("startDate", UNSET)
        start_date: Union[Unset, datetime.datetime]
        if isinstance(_start_date, Unset):
            start_date = UNSET
        else:
            start_date = isoparse(_start_date)

        _end_date = d.pop("endDate", UNSET)
        end_date: Union[Unset, datetime.datetime]
        if isinstance(_end_date, Unset):
            end_date = UNSET
        else:
            end_date = isoparse(_end_date)

        _fund = d.pop("fund", UNSET)
        fund: Union[Unset, IdNamePair]
        if isinstance(_fund, Unset):
            fund = UNSET
        else:
            fund = IdNamePair.from_dict(_fund)

        _purpose = d.pop("purpose", UNSET)
        purpose: Union[Unset, IdNamePair]
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = IdNamePair.from_dict(_purpose)

        _parent_campaign = d.pop("parentCampaign", UNSET)
        parent_campaign: Union[Unset, IdNamePair]
        if isinstance(_parent_campaign, Unset):
            parent_campaign = UNSET
        else:
            parent_campaign = IdNamePair.from_dict(_parent_campaign)

        page_content = d.pop("pageContent", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, CampaignStatus]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = CampaignStatus(_status)

        goal = d.pop("goal", UNSET)

        campaign_page_url = d.pop("campaignPageUrl", UNSET)

        donation_form_url = d.pop("donationFormUrl", UNSET)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, CampaignStats]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = CampaignStats.from_dict(_statistics)

        _social_fundraising = d.pop("socialFundraising", UNSET)
        social_fundraising: Union[Unset, SocialFundraising]
        if isinstance(_social_fundraising, Unset):
            social_fundraising = UNSET
        else:
            social_fundraising = SocialFundraising.from_dict(_social_fundraising)

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

        campaign = cls(
            id=id,
            name=name,
            code=code,
            start_date=start_date,
            end_date=end_date,
            fund=fund,
            purpose=purpose,
            parent_campaign=parent_campaign,
            page_content=page_content,
            status=status,
            goal=goal,
            campaign_page_url=campaign_page_url,
            donation_form_url=donation_form_url,
            statistics=statistics,
            social_fundraising=social_fundraising,
            cra_info=cra_info,
            tax_deductible_info=tax_deductible_info,
        )

        campaign.additional_properties = d
        return campaign

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
