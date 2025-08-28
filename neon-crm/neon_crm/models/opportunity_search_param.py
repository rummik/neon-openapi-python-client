from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpportunitySearchParam")


@_attrs_define
class OpportunitySearchParam:
    """
    Attributes:
        page_size (Union[Unset, int]):
        current_page (Union[Unset, int]):
        event_id (Union[Unset, str]):
        ng_event_id (Union[Unset, str]):
    """

    page_size: Union[Unset, int] = UNSET
    current_page: Union[Unset, int] = UNSET
    event_id: Union[Unset, str] = UNSET
    ng_event_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_size = self.page_size

        current_page = self.current_page

        event_id = self.event_id

        ng_event_id = self.ng_event_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if ng_event_id is not UNSET:
            field_dict["ngEventId"] = ng_event_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_size = d.pop("pageSize", UNSET)

        current_page = d.pop("currentPage", UNSET)

        event_id = d.pop("eventId", UNSET)

        ng_event_id = d.pop("ngEventId", UNSET)

        opportunity_search_param = cls(
            page_size=page_size,
            current_page=current_page,
            event_id=event_id,
            ng_event_id=ng_event_id,
        )

        opportunity_search_param.additional_properties = d
        return opportunity_search_param

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
