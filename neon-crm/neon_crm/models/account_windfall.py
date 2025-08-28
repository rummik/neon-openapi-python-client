from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AccountWindfall")


@_attrs_define
class AccountWindfall:
    """
    Attributes:
        id (Union[Unset, str]):
        windfall_id (Union[Unset, str]):
        net_worth (Union[Unset, float]):
        low_confidence_net_worth (Union[Unset, float]):
        high_confidence_net_worth (Union[Unset, float]):
        net_worth_last_calculated (Union[Unset, str]):
        recent_mover (Union[Unset, bool]):
        recently_divorced (Union[Unset, bool]):
        recent_death_in_family (Union[Unset, bool]):
        political_affiliation (Union[Unset, str]):
        political_donor (Union[Unset, bool]):
        boat_owner (Union[Unset, bool]):
        plane_owner (Union[Unset, bool]):
        small_business_owner (Union[Unset, bool]):
        philanthropic_giver (Union[Unset, bool]):
        philanthropic_cause (Union[Unset, list[str]]):
        philanthropic_focus (Union[Unset, list[str]]):
        multi_property_owner (Union[Unset, bool]):
        foundation_association (Union[Unset, bool]):
        foundation_officer (Union[Unset, bool]):
        trust_association (Union[Unset, bool]):
        nonprofit_board_member (Union[Unset, bool]):
        top_political_donor (Union[Unset, bool]):
        match_confidence (Union[Unset, float]):
        sec_money_in_motion (Union[Unset, bool]):
        liquidity_trigger (Union[Unset, bool]):
        luxury_car_owner (Union[Unset, bool]):
        imported_car_owner (Union[Unset, bool]):
        recent_mortgage (Union[Unset, bool]):
        primary_address_incorrect (Union[Unset, bool]):
    """

    id: Union[Unset, str] = UNSET
    windfall_id: Union[Unset, str] = UNSET
    net_worth: Union[Unset, float] = UNSET
    low_confidence_net_worth: Union[Unset, float] = UNSET
    high_confidence_net_worth: Union[Unset, float] = UNSET
    net_worth_last_calculated: Union[Unset, str] = UNSET
    recent_mover: Union[Unset, bool] = UNSET
    recently_divorced: Union[Unset, bool] = UNSET
    recent_death_in_family: Union[Unset, bool] = UNSET
    political_affiliation: Union[Unset, str] = UNSET
    political_donor: Union[Unset, bool] = UNSET
    boat_owner: Union[Unset, bool] = UNSET
    plane_owner: Union[Unset, bool] = UNSET
    small_business_owner: Union[Unset, bool] = UNSET
    philanthropic_giver: Union[Unset, bool] = UNSET
    philanthropic_cause: Union[Unset, list[str]] = UNSET
    philanthropic_focus: Union[Unset, list[str]] = UNSET
    multi_property_owner: Union[Unset, bool] = UNSET
    foundation_association: Union[Unset, bool] = UNSET
    foundation_officer: Union[Unset, bool] = UNSET
    trust_association: Union[Unset, bool] = UNSET
    nonprofit_board_member: Union[Unset, bool] = UNSET
    top_political_donor: Union[Unset, bool] = UNSET
    match_confidence: Union[Unset, float] = UNSET
    sec_money_in_motion: Union[Unset, bool] = UNSET
    liquidity_trigger: Union[Unset, bool] = UNSET
    luxury_car_owner: Union[Unset, bool] = UNSET
    imported_car_owner: Union[Unset, bool] = UNSET
    recent_mortgage: Union[Unset, bool] = UNSET
    primary_address_incorrect: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        windfall_id = self.windfall_id

        net_worth = self.net_worth

        low_confidence_net_worth = self.low_confidence_net_worth

        high_confidence_net_worth = self.high_confidence_net_worth

        net_worth_last_calculated = self.net_worth_last_calculated

        recent_mover = self.recent_mover

        recently_divorced = self.recently_divorced

        recent_death_in_family = self.recent_death_in_family

        political_affiliation = self.political_affiliation

        political_donor = self.political_donor

        boat_owner = self.boat_owner

        plane_owner = self.plane_owner

        small_business_owner = self.small_business_owner

        philanthropic_giver = self.philanthropic_giver

        philanthropic_cause: Union[Unset, list[str]] = UNSET
        if not isinstance(self.philanthropic_cause, Unset):
            philanthropic_cause = self.philanthropic_cause

        philanthropic_focus: Union[Unset, list[str]] = UNSET
        if not isinstance(self.philanthropic_focus, Unset):
            philanthropic_focus = self.philanthropic_focus

        multi_property_owner = self.multi_property_owner

        foundation_association = self.foundation_association

        foundation_officer = self.foundation_officer

        trust_association = self.trust_association

        nonprofit_board_member = self.nonprofit_board_member

        top_political_donor = self.top_political_donor

        match_confidence = self.match_confidence

        sec_money_in_motion = self.sec_money_in_motion

        liquidity_trigger = self.liquidity_trigger

        luxury_car_owner = self.luxury_car_owner

        imported_car_owner = self.imported_car_owner

        recent_mortgage = self.recent_mortgage

        primary_address_incorrect = self.primary_address_incorrect

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if windfall_id is not UNSET:
            field_dict["windfall_id"] = windfall_id
        if net_worth is not UNSET:
            field_dict["net_worth"] = net_worth
        if low_confidence_net_worth is not UNSET:
            field_dict["low_confidence_net_worth"] = low_confidence_net_worth
        if high_confidence_net_worth is not UNSET:
            field_dict["high_confidence_net_worth"] = high_confidence_net_worth
        if net_worth_last_calculated is not UNSET:
            field_dict["net_worth_last_calculated"] = net_worth_last_calculated
        if recent_mover is not UNSET:
            field_dict["recent_mover"] = recent_mover
        if recently_divorced is not UNSET:
            field_dict["recently_divorced"] = recently_divorced
        if recent_death_in_family is not UNSET:
            field_dict["recent_death_in_family"] = recent_death_in_family
        if political_affiliation is not UNSET:
            field_dict["political_affiliation"] = political_affiliation
        if political_donor is not UNSET:
            field_dict["political_donor"] = political_donor
        if boat_owner is not UNSET:
            field_dict["boat_owner"] = boat_owner
        if plane_owner is not UNSET:
            field_dict["plane_owner"] = plane_owner
        if small_business_owner is not UNSET:
            field_dict["small_business_owner"] = small_business_owner
        if philanthropic_giver is not UNSET:
            field_dict["philanthropic_giver"] = philanthropic_giver
        if philanthropic_cause is not UNSET:
            field_dict["philanthropic_cause"] = philanthropic_cause
        if philanthropic_focus is not UNSET:
            field_dict["philanthropic_focus"] = philanthropic_focus
        if multi_property_owner is not UNSET:
            field_dict["multi-property_owner"] = multi_property_owner
        if foundation_association is not UNSET:
            field_dict["foundation_association"] = foundation_association
        if foundation_officer is not UNSET:
            field_dict["foundation_officer"] = foundation_officer
        if trust_association is not UNSET:
            field_dict["trust_association"] = trust_association
        if nonprofit_board_member is not UNSET:
            field_dict["nonprofit_board_member"] = nonprofit_board_member
        if top_political_donor is not UNSET:
            field_dict["top_political_donor"] = top_political_donor
        if match_confidence is not UNSET:
            field_dict["match_confidence"] = match_confidence
        if sec_money_in_motion is not UNSET:
            field_dict["sec_money_in_motion"] = sec_money_in_motion
        if liquidity_trigger is not UNSET:
            field_dict["liquidity_trigger"] = liquidity_trigger
        if luxury_car_owner is not UNSET:
            field_dict["luxury_car_owner"] = luxury_car_owner
        if imported_car_owner is not UNSET:
            field_dict["imported_car_owner"] = imported_car_owner
        if recent_mortgage is not UNSET:
            field_dict["recent_mortgage"] = recent_mortgage
        if primary_address_incorrect is not UNSET:
            field_dict["primary_address_incorrect"] = primary_address_incorrect

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        windfall_id = d.pop("windfall_id", UNSET)

        net_worth = d.pop("net_worth", UNSET)

        low_confidence_net_worth = d.pop("low_confidence_net_worth", UNSET)

        high_confidence_net_worth = d.pop("high_confidence_net_worth", UNSET)

        net_worth_last_calculated = d.pop("net_worth_last_calculated", UNSET)

        recent_mover = d.pop("recent_mover", UNSET)

        recently_divorced = d.pop("recently_divorced", UNSET)

        recent_death_in_family = d.pop("recent_death_in_family", UNSET)

        political_affiliation = d.pop("political_affiliation", UNSET)

        political_donor = d.pop("political_donor", UNSET)

        boat_owner = d.pop("boat_owner", UNSET)

        plane_owner = d.pop("plane_owner", UNSET)

        small_business_owner = d.pop("small_business_owner", UNSET)

        philanthropic_giver = d.pop("philanthropic_giver", UNSET)

        philanthropic_cause = cast(list[str], d.pop("philanthropic_cause", UNSET))

        philanthropic_focus = cast(list[str], d.pop("philanthropic_focus", UNSET))

        multi_property_owner = d.pop("multi-property_owner", UNSET)

        foundation_association = d.pop("foundation_association", UNSET)

        foundation_officer = d.pop("foundation_officer", UNSET)

        trust_association = d.pop("trust_association", UNSET)

        nonprofit_board_member = d.pop("nonprofit_board_member", UNSET)

        top_political_donor = d.pop("top_political_donor", UNSET)

        match_confidence = d.pop("match_confidence", UNSET)

        sec_money_in_motion = d.pop("sec_money_in_motion", UNSET)

        liquidity_trigger = d.pop("liquidity_trigger", UNSET)

        luxury_car_owner = d.pop("luxury_car_owner", UNSET)

        imported_car_owner = d.pop("imported_car_owner", UNSET)

        recent_mortgage = d.pop("recent_mortgage", UNSET)

        primary_address_incorrect = d.pop("primary_address_incorrect", UNSET)

        account_windfall = cls(
            id=id,
            windfall_id=windfall_id,
            net_worth=net_worth,
            low_confidence_net_worth=low_confidence_net_worth,
            high_confidence_net_worth=high_confidence_net_worth,
            net_worth_last_calculated=net_worth_last_calculated,
            recent_mover=recent_mover,
            recently_divorced=recently_divorced,
            recent_death_in_family=recent_death_in_family,
            political_affiliation=political_affiliation,
            political_donor=political_donor,
            boat_owner=boat_owner,
            plane_owner=plane_owner,
            small_business_owner=small_business_owner,
            philanthropic_giver=philanthropic_giver,
            philanthropic_cause=philanthropic_cause,
            philanthropic_focus=philanthropic_focus,
            multi_property_owner=multi_property_owner,
            foundation_association=foundation_association,
            foundation_officer=foundation_officer,
            trust_association=trust_association,
            nonprofit_board_member=nonprofit_board_member,
            top_political_donor=top_political_donor,
            match_confidence=match_confidence,
            sec_money_in_motion=sec_money_in_motion,
            liquidity_trigger=liquidity_trigger,
            luxury_car_owner=luxury_car_owner,
            imported_car_owner=imported_car_owner,
            recent_mortgage=recent_mortgage,
            primary_address_incorrect=primary_address_incorrect,
        )

        account_windfall.additional_properties = d
        return account_windfall

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
