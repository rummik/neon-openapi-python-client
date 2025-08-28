from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pagination import Pagination
    from ..models.pledge import Pledge


T = TypeVar("T", bound="AccountPledgeSearchResult")


@_attrs_define
class AccountPledgeSearchResult:
    """
    Attributes:
        account_id (Union[Unset, str]):
        pledges (Union[Unset, list['Pledge']]):
        pagination (Union[Unset, Pagination]):
    """

    account_id: Union[Unset, str] = UNSET
    pledges: Union[Unset, list["Pledge"]] = UNSET
    pagination: Union[Unset, "Pagination"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        pledges: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.pledges, Unset):
            pledges = []
            for pledges_item_data in self.pledges:
                pledges_item = pledges_item_data.to_dict()
                pledges.append(pledges_item)

        pagination: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.pagination, Unset):
            pagination = self.pagination.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if pledges is not UNSET:
            field_dict["pledges"] = pledges
        if pagination is not UNSET:
            field_dict["pagination"] = pagination

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pagination import Pagination
        from ..models.pledge import Pledge

        d = dict(src_dict)
        account_id = d.pop("accountId", UNSET)

        pledges = []
        _pledges = d.pop("pledges", UNSET)
        for pledges_item_data in _pledges or []:
            pledges_item = Pledge.from_dict(pledges_item_data)

            pledges.append(pledges_item)

        _pagination = d.pop("pagination", UNSET)
        pagination: Union[Unset, Pagination]
        if isinstance(_pagination, Unset):
            pagination = UNSET
        else:
            pagination = Pagination.from_dict(_pagination)

        account_pledge_search_result = cls(
            account_id=account_id,
            pledges=pledges,
            pagination=pagination,
        )

        account_pledge_search_result.additional_properties = d
        return account_pledge_search_result

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
