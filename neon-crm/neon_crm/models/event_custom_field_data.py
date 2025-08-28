from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventCustomFieldData")


@_attrs_define
class EventCustomFieldData:
    """
    Attributes:
        is_event_specific_field (Union[Unset, bool]):
        event_id (Union[Unset, str]):
        attendee_question (Union[Unset, bool]):
        constituent_required (Union[Unset, bool]):
        public_required (Union[Unset, bool]):
        constituent_visible (Union[Unset, bool]):
        public_visible (Union[Unset, bool]):
    """

    is_event_specific_field: Union[Unset, bool] = UNSET
    event_id: Union[Unset, str] = UNSET
    attendee_question: Union[Unset, bool] = UNSET
    constituent_required: Union[Unset, bool] = UNSET
    public_required: Union[Unset, bool] = UNSET
    constituent_visible: Union[Unset, bool] = UNSET
    public_visible: Union[Unset, bool] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_event_specific_field = self.is_event_specific_field

        event_id = self.event_id

        attendee_question = self.attendee_question

        constituent_required = self.constituent_required

        public_required = self.public_required

        constituent_visible = self.constituent_visible

        public_visible = self.public_visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_event_specific_field is not UNSET:
            field_dict["isEventSpecificField"] = is_event_specific_field
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if attendee_question is not UNSET:
            field_dict["attendeeQuestion"] = attendee_question
        if constituent_required is not UNSET:
            field_dict["constituentRequired"] = constituent_required
        if public_required is not UNSET:
            field_dict["publicRequired"] = public_required
        if constituent_visible is not UNSET:
            field_dict["constituentVisible"] = constituent_visible
        if public_visible is not UNSET:
            field_dict["publicVisible"] = public_visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_event_specific_field = d.pop("isEventSpecificField", UNSET)

        event_id = d.pop("eventId", UNSET)

        attendee_question = d.pop("attendeeQuestion", UNSET)

        constituent_required = d.pop("constituentRequired", UNSET)

        public_required = d.pop("publicRequired", UNSET)

        constituent_visible = d.pop("constituentVisible", UNSET)

        public_visible = d.pop("publicVisible", UNSET)

        event_custom_field_data = cls(
            is_event_specific_field=is_event_specific_field,
            event_id=event_id,
            attendee_question=attendee_question,
            constituent_required=constituent_required,
            public_required=public_required,
            constituent_visible=constituent_visible,
            public_visible=public_visible,
        )

        event_custom_field_data.additional_properties = d
        return event_custom_field_data

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
