from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.event_dates import EventDates
    from ..models.financial_settings import FinancialSettings
    from ..models.id_name_pair import IdNamePair
    from ..models.location import Location


T = TypeVar("T", bound="Event")


@_attrs_define
class Event:
    """
    Attributes:
        id (Union[Unset, str]):
        name (Union[Unset, str]):
        summary (Union[Unset, str]):
        code (Union[Unset, str]):
        maximum_attendees (Union[Unset, int]):
        category (Union[Unset, IdNamePair]):
        topic (Union[Unset, IdNamePair]):
        campaign (Union[Unset, IdNamePair]):
        publish_event (Union[Unset, bool]):
        enable_event_registration_form (Union[Unset, bool]):
        archived (Union[Unset, bool]):
        enable_wait_listing (Union[Unset, bool]):
        create_accountsfor_attendees (Union[Unset, bool]):
        event_description (Union[Unset, str]):
        event_dates (Union[Unset, EventDates]):
        financial_settings (Union[Unset, FinancialSettings]):
        location (Union[Unset, Location]):
        thumbnail_url (Union[Unset, str]):
    """

    id: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    summary: Union[Unset, str] = UNSET
    code: Union[Unset, str] = UNSET
    maximum_attendees: Union[Unset, int] = UNSET
    category: Union[Unset, "IdNamePair"] = UNSET
    topic: Union[Unset, "IdNamePair"] = UNSET
    campaign: Union[Unset, "IdNamePair"] = UNSET
    publish_event: Union[Unset, bool] = UNSET
    enable_event_registration_form: Union[Unset, bool] = UNSET
    archived: Union[Unset, bool] = UNSET
    enable_wait_listing: Union[Unset, bool] = UNSET
    create_accountsfor_attendees: Union[Unset, bool] = UNSET
    event_description: Union[Unset, str] = UNSET
    event_dates: Union[Unset, "EventDates"] = UNSET
    financial_settings: Union[Unset, "FinancialSettings"] = UNSET
    location: Union[Unset, "Location"] = UNSET
    thumbnail_url: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        summary = self.summary

        code = self.code

        maximum_attendees = self.maximum_attendees

        category: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.category, Unset):
            category = self.category.to_dict()

        topic: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.topic, Unset):
            topic = self.topic.to_dict()

        campaign: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.campaign, Unset):
            campaign = self.campaign.to_dict()

        publish_event = self.publish_event

        enable_event_registration_form = self.enable_event_registration_form

        archived = self.archived

        enable_wait_listing = self.enable_wait_listing

        create_accountsfor_attendees = self.create_accountsfor_attendees

        event_description = self.event_description

        event_dates: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.event_dates, Unset):
            event_dates = self.event_dates.to_dict()

        financial_settings: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.financial_settings, Unset):
            financial_settings = self.financial_settings.to_dict()

        location: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.location, Unset):
            location = self.location.to_dict()

        thumbnail_url = self.thumbnail_url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if summary is not UNSET:
            field_dict["summary"] = summary
        if code is not UNSET:
            field_dict["code"] = code
        if maximum_attendees is not UNSET:
            field_dict["maximumAttendees"] = maximum_attendees
        if category is not UNSET:
            field_dict["category"] = category
        if topic is not UNSET:
            field_dict["topic"] = topic
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if publish_event is not UNSET:
            field_dict["publishEvent"] = publish_event
        if enable_event_registration_form is not UNSET:
            field_dict["enableEventRegistrationForm"] = enable_event_registration_form
        if archived is not UNSET:
            field_dict["archived"] = archived
        if enable_wait_listing is not UNSET:
            field_dict["enableWaitListing"] = enable_wait_listing
        if create_accountsfor_attendees is not UNSET:
            field_dict["createAccountsforAttendees"] = create_accountsfor_attendees
        if event_description is not UNSET:
            field_dict["eventDescription"] = event_description
        if event_dates is not UNSET:
            field_dict["eventDates"] = event_dates
        if financial_settings is not UNSET:
            field_dict["financialSettings"] = financial_settings
        if location is not UNSET:
            field_dict["location"] = location
        if thumbnail_url is not UNSET:
            field_dict["thumbnailUrl"] = thumbnail_url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.event_dates import EventDates
        from ..models.financial_settings import FinancialSettings
        from ..models.id_name_pair import IdNamePair
        from ..models.location import Location

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        summary = d.pop("summary", UNSET)

        code = d.pop("code", UNSET)

        maximum_attendees = d.pop("maximumAttendees", UNSET)

        _category = d.pop("category", UNSET)
        category: Union[Unset, IdNamePair]
        if isinstance(_category, Unset):
            category = UNSET
        else:
            category = IdNamePair.from_dict(_category)

        _topic = d.pop("topic", UNSET)
        topic: Union[Unset, IdNamePair]
        if isinstance(_topic, Unset):
            topic = UNSET
        else:
            topic = IdNamePair.from_dict(_topic)

        _campaign = d.pop("campaign", UNSET)
        campaign: Union[Unset, IdNamePair]
        if isinstance(_campaign, Unset):
            campaign = UNSET
        else:
            campaign = IdNamePair.from_dict(_campaign)

        publish_event = d.pop("publishEvent", UNSET)

        enable_event_registration_form = d.pop("enableEventRegistrationForm", UNSET)

        archived = d.pop("archived", UNSET)

        enable_wait_listing = d.pop("enableWaitListing", UNSET)

        create_accountsfor_attendees = d.pop("createAccountsforAttendees", UNSET)

        event_description = d.pop("eventDescription", UNSET)

        _event_dates = d.pop("eventDates", UNSET)
        event_dates: Union[Unset, EventDates]
        if isinstance(_event_dates, Unset):
            event_dates = UNSET
        else:
            event_dates = EventDates.from_dict(_event_dates)

        _financial_settings = d.pop("financialSettings", UNSET)
        financial_settings: Union[Unset, FinancialSettings]
        if isinstance(_financial_settings, Unset):
            financial_settings = UNSET
        else:
            financial_settings = FinancialSettings.from_dict(_financial_settings)

        _location = d.pop("location", UNSET)
        location: Union[Unset, Location]
        if isinstance(_location, Unset):
            location = UNSET
        else:
            location = Location.from_dict(_location)

        thumbnail_url = d.pop("thumbnailUrl", UNSET)

        event = cls(
            id=id,
            name=name,
            summary=summary,
            code=code,
            maximum_attendees=maximum_attendees,
            category=category,
            topic=topic,
            campaign=campaign,
            publish_event=publish_event,
            enable_event_registration_form=enable_event_registration_form,
            archived=archived,
            enable_wait_listing=enable_wait_listing,
            create_accountsfor_attendees=create_accountsfor_attendees,
            event_description=event_description,
            event_dates=event_dates,
            financial_settings=financial_settings,
            location=location,
            thumbnail_url=thumbnail_url,
        )

        event.additional_properties = d
        return event

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
