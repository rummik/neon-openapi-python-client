from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.opportunity import Opportunity
    from ..models.pagination import Pagination


T = TypeVar("T", bound="OpportunitySearchResult")


@_attrs_define
class OpportunitySearchResult:
    """
    Attributes:
        pagination (Union[Unset, Pagination]):
        opportunity_list (Union[Unset, list['Opportunity']]):
    """

    pagination: Union[Unset, "Pagination"] = UNSET
    opportunity_list: Union[Unset, list["Opportunity"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        opportunity_list: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.opportunity_list, Unset):
            opportunity_list = []
            for opportunity_list_item_data in self.opportunity_list:
                opportunity_list_item = opportunity_list_item_data.to_dict()
                opportunity_list.append(opportunity_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pagination is not UNSET:
            field_dict["pagination"] = pagination
        if opportunity_list is not UNSET:
            field_dict["opportunityList"] = opportunity_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.opportunity import Opportunity
        from ..models.pagination import Pagination

        d = dict(src_dict)
        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        opportunity_list = []
        _opportunity_list = d.pop("opportunityList", UNSET)
        for opportunity_list_item_data in _opportunity_list or []:
            opportunity_list_item = Opportunity.from_dict(opportunity_list_item_data)

            opportunity_list.append(opportunity_list_item)

        opportunity_search_result = cls(
            pagination=pagination,
            opportunity_list=opportunity_list,
        )

        opportunity_search_result.additional_properties = d
        return opportunity_search_result

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
