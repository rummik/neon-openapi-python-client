from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CampaignFundraiser")


@_attrs_define
class CampaignFundraiser:
    """
    Attributes:
        account_id (Union[Unset, str]):
        page_title (Union[Unset, str]):
        goal (Union[Unset, float]):
    """

    account_id: Union[Unset, str] = UNSET
    page_title: Union[Unset, str] = UNSET
    goal: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        page_title = self.page_title

        goal = self.goal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if page_title is not UNSET:
            field_dict["pageTitle"] = page_title
        if goal is not UNSET:
            field_dict["goal"] = goal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        page_title = d.pop("pageTitle", UNSET)

        goal = d.pop("goal", UNSET)

        campaign_fundraiser = cls(
            account_id=account_id,
            page_title=page_title,
            goal=goal,
        )

        campaign_fundraiser.additional_properties = d
        return campaign_fundraiser

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
