from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.campaign_stats import CampaignStats


T = TypeVar("T", bound="SocialFundraising")


@_attrs_define
class SocialFundraising:
    """
    Attributes:
        enabled (Union[Unset, bool]): false
        fundraisers_count (Union[Unset, int]):
        create_fundraiser_url (Union[Unset, str]):
        fundraiser_list_url (Union[Unset, str]):
        fundraising_page_content (Union[Unset, str]):
        statistics (Union[Unset, CampaignStats]):
    """

    enabled: Union[Unset, bool] = UNSET
    fundraisers_count: Union[Unset, int] = UNSET
    create_fundraiser_url: Union[Unset, str] = UNSET
    fundraiser_list_url: Union[Unset, str] = UNSET
    fundraising_page_content: Union[Unset, str] = UNSET
    statistics: Union[Unset, "CampaignStats"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        fundraisers_count = self.fundraisers_count

        create_fundraiser_url = self.create_fundraiser_url

        fundraiser_list_url = self.fundraiser_list_url

        fundraising_page_content = self.fundraising_page_content

        statistics: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.statistics, Unset):
            statistics = self.statistics.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if fundraisers_count is not UNSET:
            field_dict["fundraisersCount"] = fundraisers_count
        if create_fundraiser_url is not UNSET:
            field_dict["createFundraiserUrl"] = create_fundraiser_url
        if fundraiser_list_url is not UNSET:
            field_dict["fundraiserListUrl"] = fundraiser_list_url
        if fundraising_page_content is not UNSET:
            field_dict["fundraisingPageContent"] = fundraising_page_content
        if statistics is not UNSET:
            field_dict["statistics"] = statistics

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.campaign_stats import CampaignStats

        d = dict(src_dict)
        enabled = d.pop("enabled", UNSET)

        fundraisers_count = d.pop("fundraisersCount", UNSET)

        create_fundraiser_url = d.pop("createFundraiserUrl", UNSET)

        fundraiser_list_url = d.pop("fundraiserListUrl", UNSET)

        fundraising_page_content = d.pop("fundraisingPageContent", UNSET)

        _statistics = d.pop("statistics", UNSET)
        statistics: Union[Unset, CampaignStats]
        if isinstance(_statistics, Unset):
            statistics = UNSET
        else:
            statistics = CampaignStats.from_dict(_statistics)

        social_fundraising = cls(
            enabled=enabled,
            fundraisers_count=fundraisers_count,
            create_fundraiser_url=create_fundraiser_url,
            fundraiser_list_url=fundraiser_list_url,
            fundraising_page_content=fundraising_page_content,
            statistics=statistics,
        )

        social_fundraising.additional_properties = d
        return social_fundraising

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
