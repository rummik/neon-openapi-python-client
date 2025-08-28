import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.custom_field import CustomField
    from ..models.id_name_pair import IdNamePair


T = TypeVar("T", bound="Grant")


@_attrs_define
class Grant:
    """
    Attributes:
        id (Union[Unset, str]):
        account_id (Union[Unset, str]):
        status (Union[Unset, IdNamePair]):
        system_user_id (Union[Unset, str]):
        grant_name (Union[Unset, str]):
        due_date (Union[Unset, datetime.datetime]):
        close_date (Union[Unset, datetime.datetime]):
        ask_amount (Union[Unset, float]):
        funded_date (Union[Unset, datetime.datetime]):
        funded_amount (Union[Unset, float]):
        note (Union[Unset, str]):
        campaign (Union[Unset, IdNamePair]):
        fund (Union[Unset, IdNamePair]):
        purpose (Union[Unset, IdNamePair]):
        grant_custom_fields (Union[Unset, list['CustomField']]):
        linked_transaction_id (Union[Unset, str]):
        created_by (Union[Unset, str]):
        created_date (Union[Unset, datetime.datetime]):
        last_modified_by (Union[Unset, str]):
        last_modified_date (Union[Unset, datetime.datetime]):
        parent_grant_id (Union[Unset, str]):
        committed_date (Union[Unset, datetime.datetime]):
        committed_amount (Union[Unset, float]):
    """

    id: Union[Unset, str] = UNSET
    account_id: Union[Unset, str] = UNSET
    status: Union[Unset, "IdNamePair"] = UNSET
    system_user_id: Union[Unset, str] = UNSET
    grant_name: Union[Unset, str] = UNSET
    due_date: Union[Unset, datetime.datetime] = UNSET
    close_date: Union[Unset, datetime.datetime] = UNSET
    ask_amount: Union[Unset, float] = UNSET
    funded_date: Union[Unset, datetime.datetime] = UNSET
    funded_amount: Union[Unset, float] = UNSET
    note: Union[Unset, str] = UNSET
    campaign: Union[Unset, "IdNamePair"] = UNSET
    fund: Union[Unset, "IdNamePair"] = UNSET
    purpose: Union[Unset, "IdNamePair"] = UNSET
    grant_custom_fields: Union[Unset, list["CustomField"]] = UNSET
    linked_transaction_id: Union[Unset, str] = UNSET
    created_by: Union[Unset, str] = UNSET
    created_date: Union[Unset, datetime.datetime] = UNSET
    last_modified_by: Union[Unset, str] = UNSET
    last_modified_date: Union[Unset, datetime.datetime] = UNSET
    parent_grant_id: Union[Unset, str] = UNSET
    committed_date: Union[Unset, datetime.datetime] = UNSET
    committed_amount: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        account_id = self.account_id

        status: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.to_dict()

        system_user_id = self.system_user_id

        grant_name = self.grant_name

        due_date: Union[Unset, str] = UNSET
        if not isinstance(self.due_date, Unset):
            due_date = self.due_date.isoformat()

        close_date: Union[Unset, str] = UNSET
        if not isinstance(self.close_date, Unset):
            close_date = self.close_date.isoformat()

        ask_amount = self.ask_amount

        funded_date: Union[Unset, str] = UNSET
        if not isinstance(self.funded_date, Unset):
            funded_date = self.funded_date.isoformat()

        funded_amount = self.funded_amount

        note = self.note

        campaign: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.campaign, Unset):
            campaign = self.campaign.to_dict()

        fund: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.fund, Unset):
            fund = self.fund.to_dict()

        purpose: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.purpose, Unset):
            purpose = self.purpose.to_dict()

        grant_custom_fields: Union[Unset, list[dict[str, Any]]] = UNSET
        if not isinstance(self.grant_custom_fields, Unset):
            grant_custom_fields = []
            for grant_custom_fields_item_data in self.grant_custom_fields:
                grant_custom_fields_item = grant_custom_fields_item_data.to_dict()
                grant_custom_fields.append(grant_custom_fields_item)

        linked_transaction_id = self.linked_transaction_id

        created_by = self.created_by

        created_date: Union[Unset, str] = UNSET
        if not isinstance(self.created_date, Unset):
            created_date = self.created_date.isoformat()

        last_modified_by = self.last_modified_by

        last_modified_date: Union[Unset, str] = UNSET
        if not isinstance(self.last_modified_date, Unset):
            last_modified_date = self.last_modified_date.isoformat()

        parent_grant_id = self.parent_grant_id

        committed_date: Union[Unset, str] = UNSET
        if not isinstance(self.committed_date, Unset):
            committed_date = self.committed_date.isoformat()

        committed_amount = self.committed_amount

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if status is not UNSET:
            field_dict["status"] = status
        if system_user_id is not UNSET:
            field_dict["systemUserId"] = system_user_id
        if grant_name is not UNSET:
            field_dict["grantName"] = grant_name
        if due_date is not UNSET:
            field_dict["dueDate"] = due_date
        if close_date is not UNSET:
            field_dict["closeDate"] = close_date
        if ask_amount is not UNSET:
            field_dict["askAmount"] = ask_amount
        if funded_date is not UNSET:
            field_dict["fundedDate"] = funded_date
        if funded_amount is not UNSET:
            field_dict["fundedAmount"] = funded_amount
        if note is not UNSET:
            field_dict["note"] = note
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if fund is not UNSET:
            field_dict["fund"] = fund
        if purpose is not UNSET:
            field_dict["purpose"] = purpose
        if grant_custom_fields is not UNSET:
            field_dict["grantCustomFields"] = grant_custom_fields
        if linked_transaction_id is not UNSET:
            field_dict["linkedTransactionId"] = linked_transaction_id
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_date is not UNSET:
            field_dict["createdDate"] = created_date
        if last_modified_by is not UNSET:
            field_dict["lastModifiedBy"] = last_modified_by
        if last_modified_date is not UNSET:
            field_dict["lastModifiedDate"] = last_modified_date
        if parent_grant_id is not UNSET:
            field_dict["parentGrantId"] = parent_grant_id
        if committed_date is not UNSET:
            field_dict["committedDate"] = committed_date
        if committed_amount is not UNSET:
            field_dict["committedAmount"] = committed_amount

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_field import CustomField
        from ..models.id_name_pair import IdNamePair

        d = dict(src_dict)
        id = d.pop("id", UNSET)

        account_id = d.pop("accountId", UNSET)

        _status = d.pop("status", UNSET)
        status: Union[Unset, IdNamePair]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = IdNamePair.from_dict(_status)

        system_user_id = d.pop("systemUserId", UNSET)

        grant_name = d.pop("grantName", UNSET)

        _due_date = d.pop("dueDate", UNSET)
        due_date: Union[Unset, datetime.datetime]
        if isinstance(_due_date, Unset):
            due_date = UNSET
        else:
            due_date = isoparse(_due_date)

        _close_date = d.pop("closeDate", UNSET)
        close_date: Union[Unset, datetime.datetime]
        if isinstance(_close_date, Unset):
            close_date = UNSET
        else:
            close_date = isoparse(_close_date)

        ask_amount = d.pop("askAmount", UNSET)

        _funded_date = d.pop("fundedDate", UNSET)
        funded_date: Union[Unset, datetime.datetime]
        if isinstance(_funded_date, Unset):
            funded_date = UNSET
        else:
            funded_date = isoparse(_funded_date)

        funded_amount = d.pop("fundedAmount", UNSET)

        note = d.pop("note", UNSET)

        _campaign = d.pop("campaign", UNSET)
        campaign: Union[Unset, IdNamePair]
        if isinstance(_campaign, Unset):
            campaign = UNSET
        else:
            campaign = IdNamePair.from_dict(_campaign)

        _fund = d.pop("fund", UNSET)
        fund: Union[Unset, IdNamePair]
        if isinstance(_fund, Unset):
            fund = UNSET
        else:
            fund = IdNamePair.from_dict(_fund)

        _purpose = d.pop("purpose", UNSET)
        purpose: Union[Unset, IdNamePair]
        if isinstance(_purpose, Unset):
            purpose = UNSET
        else:
            purpose = IdNamePair.from_dict(_purpose)

        grant_custom_fields = []
        _grant_custom_fields = d.pop("grantCustomFields", UNSET)
        for grant_custom_fields_item_data in _grant_custom_fields or []:
            grant_custom_fields_item = CustomField.from_dict(grant_custom_fields_item_data)

            grant_custom_fields.append(grant_custom_fields_item)

        linked_transaction_id = d.pop("linkedTransactionId", UNSET)

        created_by = d.pop("createdBy", UNSET)

        _created_date = d.pop("createdDate", UNSET)
        created_date: Union[Unset, datetime.datetime]
        if isinstance(_created_date, Unset):
            created_date = UNSET
        else:
            created_date = isoparse(_created_date)

        last_modified_by = d.pop("lastModifiedBy", UNSET)

        _last_modified_date = d.pop("lastModifiedDate", UNSET)
        last_modified_date: Union[Unset, datetime.datetime]
        if isinstance(_last_modified_date, Unset):
            last_modified_date = UNSET
        else:
            last_modified_date = isoparse(_last_modified_date)

        parent_grant_id = d.pop("parentGrantId", UNSET)

        _committed_date = d.pop("committedDate", UNSET)
        committed_date: Union[Unset, datetime.datetime]
        if isinstance(_committed_date, Unset):
            committed_date = UNSET
        else:
            committed_date = isoparse(_committed_date)

        committed_amount = d.pop("committedAmount", UNSET)

        grant = cls(
            id=id,
            account_id=account_id,
            status=status,
            system_user_id=system_user_id,
            grant_name=grant_name,
            due_date=due_date,
            close_date=close_date,
            ask_amount=ask_amount,
            funded_date=funded_date,
            funded_amount=funded_amount,
            note=note,
            campaign=campaign,
            fund=fund,
            purpose=purpose,
            grant_custom_fields=grant_custom_fields,
            linked_transaction_id=linked_transaction_id,
            created_by=created_by,
            created_date=created_date,
            last_modified_by=last_modified_by,
            last_modified_date=last_modified_date,
            parent_grant_id=parent_grant_id,
            committed_date=committed_date,
            committed_amount=committed_amount,
        )

        grant.additional_properties = d
        return grant

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
