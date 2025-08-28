from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OpportunityShiftSearchParam")


@_attrs_define
class OpportunityShiftSearchParam:
    """
    Attributes:
        page_size (Union[Unset, int]):
        current_page (Union[Unset, int]):
        occurrence_id (Union[Unset, str]):
        ng_occurrence_id (Union[Unset, str]):
    """

    page_size: Union[Unset, int] = UNSET
    current_page: Union[Unset, int] = UNSET
    occurrence_id: Union[Unset, str] = UNSET
    ng_occurrence_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        page_size = self.page_size

        current_page = self.current_page

        occurrence_id = self.occurrence_id

        ng_occurrence_id = self.ng_occurrence_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if page_size is not UNSET:
            field_dict["pageSize"] = page_size
        if current_page is not UNSET:
            field_dict["currentPage"] = current_page
        if occurrence_id is not UNSET:
            field_dict["occurrenceId"] = occurrence_id
        if ng_occurrence_id is not UNSET:
            field_dict["ngOccurrenceId"] = ng_occurrence_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        page_size = d.pop("pageSize", UNSET)

        current_page = d.pop("currentPage", UNSET)

        occurrence_id = d.pop("occurrenceId", UNSET)

        ng_occurrence_id = d.pop("ngOccurrenceId", UNSET)

        opportunity_shift_search_param = cls(
            page_size=page_size,
            current_page=current_page,
            occurrence_id=occurrence_id,
            ng_occurrence_id=ng_occurrence_id,
        )

        opportunity_shift_search_param.additional_properties = d
        return opportunity_shift_search_param

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
