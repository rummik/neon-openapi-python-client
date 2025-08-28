from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.volunteer_role_api_status import VolunteerRoleApiStatus
from ..models.volunteer_role_api_status_color import VolunteerRoleApiStatusColor
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.timestamps import Timestamps


T = TypeVar("T", bound="VolunteerRoleApi")


@_attrs_define
class VolunteerRoleApi:
    """
    Attributes:
        name (str):
        status_color (VolunteerRoleApiStatusColor):
        status (VolunteerRoleApiStatus):
        id (Union[Unset, str]):
        description (Union[Unset, str]):
        timestamps (Union[Unset, Timestamps]):
    """

    name: str
    status_color: VolunteerRoleApiStatusColor
    status: VolunteerRoleApiStatus
    id: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    timestamps: Union[Unset, "Timestamps"] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        status_color = self.status_color.value

        status = self.status.value

        id = self.id

        description = self.description

        timestamps: Union[Unset, dict[str, Any]] = UNSET
        if not isinstance(self.timestamps, Unset):
            timestamps = self.timestamps.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "statusColor": status_color,
                "status": status,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if description is not UNSET:
            field_dict["description"] = description
        if timestamps is not UNSET:
            field_dict["timestamps"] = timestamps

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.timestamps import Timestamps

        d = dict(src_dict)
        name = d.pop("name")

        status_color = VolunteerRoleApiStatusColor(d.pop("statusColor"))

        status = VolunteerRoleApiStatus(d.pop("status"))

        id = d.pop("id", UNSET)

        description = d.pop("description", UNSET)

        _timestamps = d.pop("timestamps", UNSET)
        timestamps: Union[Unset, Timestamps]
        if isinstance(_timestamps, Unset):
            timestamps = UNSET
        else:
            timestamps = Timestamps.from_dict(_timestamps)

        volunteer_role_api = cls(
            name=name,
            status_color=status_color,
            status=status,
            id=id,
            description=description,
            timestamps=timestamps,
        )

        volunteer_role_api.additional_properties = d
        return volunteer_role_api

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
