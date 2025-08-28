from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.search_criteria import SearchCriteria
    from ..models.search_request_output_fields_item import SearchRequestOutputFieldsItem


T = TypeVar("T", bound="SearchRequest")


@_attrs_define
class SearchRequest:
    """
    Attributes:
        search_fields (Union[Unset, list['SearchCriteria']]):
        output_fields (Union[Unset, list['SearchRequestOutputFieldsItem']]):
        pagination (Union[Unset, Pagination]):
    """

    search_fields: Union[Unset, list["SearchCriteria"]] = UNSET
    output_fields: Union[Unset, list["SearchRequestOutputFieldsItem"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.search_fields, Unset):
            search_fields = []
            for search_fields_item_data in self.search_fields:
                search_fields_item = search_fields_item_data.to_dict()
                search_fields.append(search_fields_item)

        output_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.output_fields, Unset):
            output_fields = []
            for output_fields_item_data in self.output_fields:
                output_fields_item = output_fields_item_data.to_dict()
                output_fields.append(output_fields_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_fields is not UNSET:
            field_dict["searchFields"] = search_fields
        if output_fields is not UNSET:
            field_dict["outputFields"] = output_fields
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.search_criteria import SearchCriteria
        from ..models.search_request_output_fields_item import SearchRequestOutputFieldsItem

        d = dict(src_dict)
        search_fields = []
        _search_fields = d.pop("searchFields", UNSET)
        for search_fields_item_data in _search_fields or []:
            search_fields_item = SearchCriteria.from_dict(search_fields_item_data)

            search_fields.append(search_fields_item)

        output_fields = []
        _output_fields = d.pop("outputFields", UNSET)
        for output_fields_item_data in _output_fields or []:
            output_fields_item = SearchRequestOutputFieldsItem.from_dict(output_fields_item_data)

            output_fields.append(output_fields_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        search_request = cls(
            search_fields=search_fields,
            output_fields=output_fields,
            pagination=pagination,
        )

        search_request.additional_properties = d
        return search_request

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
