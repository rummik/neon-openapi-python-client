from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.shift_and_volunteer import ShiftAndVolunteer


T = TypeVar("T", bound="AssignmentVolunteers")


@_attrs_define
class AssignmentVolunteers:
    """
    Attributes:
        volunteers (list['ShiftAndVolunteer']):
    """

    volunteers: list["ShiftAndVolunteer"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        volunteers = []
        for volunteers_item_data in self.volunteers:
            volunteers_item = volunteers_item_data.to_dict()
            volunteers.append(volunteers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "volunteers": volunteers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shift_and_volunteer import ShiftAndVolunteer

        d = dict(src_dict)
        volunteers = []
        _volunteers = d.pop("volunteers")
        for volunteers_item_data in _volunteers:
            volunteers_item = ShiftAndVolunteer.from_dict(volunteers_item_data)

            volunteers.append(volunteers_item)

        assignment_volunteers = cls(
            volunteers=volunteers,
        )

        assignment_volunteers.additional_properties = d
        return assignment_volunteers

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
