"""Contains all the data models used in inputs/outputs"""

from .account import Account
from .account_contacts import AccountContacts
from .account_custom_field_data import AccountCustomFieldData
from .account_custom_field_data_account_type import AccountCustomFieldDataAccountType
from .account_donation_search_result import AccountDonationSearchResult
from .account_id_and_ref_id_result import AccountIdAndRefIdResult
from .account_id_result import AccountIdResult
from .account_order import AccountOrder
from .account_order_item import AccountOrderItem
from .account_order_item_type import AccountOrderItemType
from .account_order_status import AccountOrderStatus
from .account_pledge_search_result import AccountPledgeSearchResult
from .account_role_api import AccountRoleApi
from .account_search_result import AccountSearchResult
from .account_search_result_item import AccountSearchResultItem
from .account_search_result_item_user_type import AccountSearchResultItemUserType
from .account_windfall import AccountWindfall
from .acknowledgee import Acknowledgee
from .activity import Activity
from .activity_dates import ActivityDates
from .activity_priority import ActivityPriority
from .add_fundraiser_to_campaign_using_post_response_200 import AddFundraiserToCampaignUsingPOSTResponse200
from .add_payment_request import AddPaymentRequest
from .add_payment_request_transaction_type import AddPaymentRequestTransactionType
from .address import Address
from .address_add import AddressAdd
from .address_add_fax_type import AddressAddFaxType
from .address_add_phone_1_type import AddressAddPhone1Type
from .address_add_phone_2_type import AddressAddPhone2Type
from .address_add_phone_3_type import AddressAddPhone3Type
from .address_fax_type import AddressFaxType
from .address_phone_1_type import AddressPhone1Type
from .address_phone_2_type import AddressPhone2Type
from .address_phone_3_type import AddressPhone3Type
from .admission_fee import AdmissionFee
from .api_message import APIMessage
from .assignment_volunteers import AssignmentVolunteers
from .auto_number import AutoNumber
from .base_custom_field_group import BaseCustomFieldGroup
from .base_membership import BaseMembership
from .base_membership_change_type import BaseMembershipChangeType
from .base_membership_enroll_type import BaseMembershipEnrollType
from .base_membership_status import BaseMembershipStatus
from .base_membership_term_unit import BaseMembershipTermUnit
from .basic_attribute import BasicAttribute
from .billing_address import BillingAddress
from .calculate_result import CalculateResult
from .campaign import Campaign
from .campaign_fundraiser import CampaignFundraiser
from .campaign_stats import CampaignStats
from .campaign_status import CampaignStatus
from .catalog import Catalog
from .catalog_status import CatalogStatus
from .category import Category
from .category_status import CategoryStatus
from .check_payment import CheckPayment
from .check_payment_account_type import CheckPaymentAccountType
from .checkbox_single import CheckboxSingle
from .code_name_pair import CodeNamePair
from .code_name_pair_status import CodeNamePairStatus
from .company_account import CompanyAccount
from .consent import Consent
from .consent_data_sharing import ConsentDataSharing
from .consent_email import ConsentEmail
from .consent_mail import ConsentMail
from .consent_phone import ConsentPhone
from .consent_sms import ConsentSms
from .contact import Contact
from .cra_info import CraInfo
from .create_custom_object import CreateCustomObject
from .create_custom_object_object_record_data_type import CreateCustomObjectObjectRecordDataType
from .create_event_ticket_using_post_response_200 import CreateEventTicketUsingPOSTResponse200
from .credit_card_offline_payment import CreditCardOfflinePayment
from .credit_card_online_payment import CreditCardOnlinePayment
from .custom_field import CustomField
from .custom_field_data import CustomFieldData
from .custom_field_data_component import CustomFieldDataComponent
from .custom_field_data_data_type import CustomFieldDataDataType
from .custom_field_data_display_type import CustomFieldDataDisplayType
from .custom_field_data_status import CustomFieldDataStatus
from .custom_field_group import CustomFieldGroup
from .custom_field_group_component import CustomFieldGroupComponent
from .custom_field_option import CustomFieldOption
from .custom_object_email_notification import CustomObjectEmailNotification
from .custom_object_email_notification_notification_type import CustomObjectEmailNotificationNotificationType
from .custom_object_field import CustomObjectField
from .custom_object_field_field_data_type import CustomObjectFieldFieldDataType
from .custom_object_field_list_response import CustomObjectFieldListResponse
from .custom_object_field_list_response_field_data_type import CustomObjectFieldListResponseFieldDataType
from .custom_object_field_response import CustomObjectFieldResponse
from .custom_object_field_response_field_data_type import CustomObjectFieldResponseFieldDataType
from .custom_object_form_layout import CustomObjectFormLayout
from .custom_object_form_layout_entry_response import CustomObjectFormLayoutEntryResponse
from .custom_object_form_layout_response import CustomObjectFormLayoutResponse
from .custom_object_layout_list_field import CustomObjectLayoutListField
from .custom_object_layout_page_item import CustomObjectLayoutPageItem
from .custom_object_list_layout import CustomObjectListLayout
from .custom_object_list_layout_entry_response import CustomObjectListLayoutEntryResponse
from .custom_object_list_layout_response import CustomObjectListLayoutResponse
from .custom_object_page_param import CustomObjectPageParam
from .custom_object_page_param_sort_direction import CustomObjectPageParamSortDirection
from .custom_object_record import CustomObjectRecord
from .custom_object_relation import CustomObjectRelation
from .custom_object_relation_list import CustomObjectRelationList
from .custom_object_relation_list_response import CustomObjectRelationListResponse
from .custom_object_response import CustomObjectResponse
from .custom_object_status import CustomObjectStatus
from .custom_object_validator_rule import CustomObjectValidatorRule
from .custom_object_validator_rule_response import CustomObjectValidatorRuleResponse
from .daf_pay_payment import DafPayPayment
from .date import Date
from .delete_pledge_payment_using_delete_response_200 import DeletePledgePaymentUsingDELETEResponse200
from .delete_recurring_using_delete_response_200 import DeleteRecurringUsingDELETEResponse200
from .delete_ticket_using_delete_response_200 import DeleteTicketUsingDELETEResponse200
from .delete_using_delete1_response_200 import DeleteUsingDELETE1Response200
from .delete_using_delete2_response_200 import DeleteUsingDELETE2Response200
from .delete_using_delete5_response_200 import DeleteUsingDELETE5Response200
from .delete_using_delete6_response_200 import DeleteUsingDELETE6Response200
from .delete_using_delete7_response_200 import DeleteUsingDELETE7Response200
from .delete_using_delete8_response_200 import DeleteUsingDELETE8Response200
from .delete_using_delete9_response_200 import DeleteUsingDELETE9Response200
from .delete_using_delete10_response_200 import DeleteUsingDELETE10Response200
from .delete_using_delete11_response_200 import DeleteUsingDELETE11Response200
from .delete_using_delete12_response_200 import DeleteUsingDELETE12Response200
from .delete_using_delete13_response_200 import DeleteUsingDELETE13Response200
from .delete_windfall_all_using_delete_response_200 import DeleteWindfallAllUsingDELETEResponse200
from .discount_item import DiscountItem
from .discount_item_order_item_type import DiscountItemOrderItemType
from .dob import Dob
from .donation import Donation
from .donation_anonymous_type import DonationAnonymousType
from .donation_item import DonationItem
from .donation_item_anonymous_type import DonationItemAnonymousType
from .donation_item_status import DonationItemStatus
from .donation_response import DonationResponse
from .donation_response_status import DonationResponseStatus
from .donation_status import DonationStatus
from .donor_covered_fees import DonorCoveredFees
from .dyna_recurring_donation import DynaRecurringDonation
from .e_check_payment import ECheckPayment
from .e_check_payment_account_type import ECheckPaymentAccountType
from .edit_custom_object_field import EditCustomObjectField
from .event import Event
from .event_attendee import EventAttendee
from .event_attendee_phone_1_type import EventAttendeePhone1Type
from .event_attendee_registration_status import EventAttendeeRegistrationStatus
from .event_attendees import EventAttendees
from .event_custom_field_data import EventCustomFieldData
from .event_dates import EventDates
from .event_registration import EventRegistration
from .event_registration_item import EventRegistrationItem
from .event_registration_response import EventRegistrationResponse
from .event_registration_response_status import EventRegistrationResponseStatus
from .event_search_result import EventSearchResult
from .event_search_result_item import EventSearchResultItem
from .event_ticket import EventTicket
from .event_ticket_attendees_per_ticket_type import EventTicketAttendeesPerTicketType
from .field_attribute import FieldAttribute
from .field_option_value import FieldOptionValue
from .file import File
from .filter_criteria import FilterCriteria
from .financial_settings import FinancialSettings
from .financial_settings_donations import FinancialSettingsDonations
from .financial_settings_donations_type import FinancialSettingsDonationsType
from .financial_settings_fee_type import FinancialSettingsFeeType
from .formula import Formula
from .formula_empty_field_treat_as import FormulaEmptyFieldTreatAs
from .formula_return_data_type import FormulaReturnDataType
from .gender_vo import GenderVO
from .gender_vo_status import GenderVOStatus
from .generosity_indicator import GenerosityIndicator
from .get_donations_using_get_sort_column import GetDonationsUsingGETSortColumn
from .get_donations_using_get_sort_direction import GetDonationsUsingGETSortDirection
from .get_event_registrations_using_get1_sort_direction import GetEventRegistrationsUsingGET1SortDirection
from .get_event_registrations_using_get1_sort_field import GetEventRegistrationsUsingGET1SortField
from .get_event_registrations_using_get_sort_column import GetEventRegistrationsUsingGETSortColumn
from .get_event_registrations_using_get_sort_direction import GetEventRegistrationsUsingGETSortDirection
from .get_peer_2_peer_fundraiser_using_get_response_200 import GetPeer2PeerFundraiserUsingGETResponse200
from .get_pledges_using_get_sort_column import GetPledgesUsingGETSortColumn
from .get_pledges_using_get_sort_direction import GetPledgesUsingGETSortDirection
from .grant import Grant
from .group_volunteer_search_param import GroupVolunteerSearchParam
from .house_hold_contact_dto import HouseHoldContactDto
from .house_hold_dto import HouseHoldDto
from .http_basic import HttpBasic
from .id_code_name_triple import IdCodeNameTriple
from .id_code_name_triple_2 import IdCodeNameTriple2
from .id_code_name_triple_2_status import IdCodeNameTriple2Status
from .id_code_name_triple_status import IdCodeNameTripleStatus
from .id_name_pair import IdNamePair
from .id_name_pair_status import IdNamePairStatus
from .id_result import IdResult
from .in_kind_payment import InKindPayment
from .individual_account import IndividualAccount
from .individual_to_company import IndividualToCompany
from .installment import Installment
from .layout_field import LayoutField
from .link_individual_to_company import LinkIndividualToCompany
from .list_custom_fields_using_get_category import ListCustomFieldsUsingGETCategory
from .list_membership_levels_using_get_status import ListMembershipLevelsUsingGETStatus
from .list_membership_using_get_sort_column import ListMembershipUsingGETSortColumn
from .list_membership_using_get_sort_direction import ListMembershipUsingGETSortDirection
from .list_objects_response import ListObjectsResponse
from .list_order_using_get_sort_column import ListOrderUsingGETSortColumn
from .list_order_using_get_sort_direction import ListOrderUsingGETSortDirection
from .list_order_using_get_transaction_types_item import ListOrderUsingGETTransactionTypesItem
from .list_product_using_get_status import ListProductUsingGETStatus
from .list_record_response import ListRecordResponse
from .list_recurring_using_get_sort_column import ListRecurringUsingGETSortColumn
from .list_recurring_using_get_sort_direction import ListRecurringUsingGETSortDirection
from .list_recurring_using_get_status import ListRecurringUsingGETStatus
from .list_relation_types_1_relation_type_category import ListRelationTypes1RelationTypeCategory
from .list_relation_types_using_get_relation_type_category import ListRelationTypesUsingGETRelationTypeCategory
from .list_using_get1_component import ListUsingGET1Component
from .list_using_get_user_type import ListUsingGETUserType
from .location import Location
from .login import Login
from .lookup import Lookup
from .master_detail import MasterDetail
from .master_detail_delete_action import MasterDetailDeleteAction
from .member_ship_custom_field_data import MemberShipCustomFieldData
from .membership import Membership
from .membership_auto_renewal import MembershipAutoRenewal
from .membership_calculate_dates_result import MembershipCalculateDatesResult
from .membership_calculate_result import MembershipCalculateResult
from .membership_change_type import MembershipChangeType
from .membership_enroll_type import MembershipEnrollType
from .membership_item import MembershipItem
from .membership_item_change_type import MembershipItemChangeType
from .membership_item_enroll_type import MembershipItemEnrollType
from .membership_item_status import MembershipItemStatus
from .membership_item_term_unit import MembershipItemTermUnit
from .membership_level import MembershipLevel
from .membership_level_id import MembershipLevelId
from .membership_level_scope_type import MembershipLevelScopeType
from .membership_level_status import MembershipLevelStatus
from .membership_level_type import MembershipLevelType
from .membership_levels_response import MembershipLevelsResponse
from .membership_list_response import MembershipListResponse
from .membership_response import MembershipResponse
from .membership_response_status import MembershipResponseStatus
from .membership_status import MembershipStatus
from .membership_term import MembershipTerm
from .membership_term_type import MembershipTermType
from .membership_term_unit import MembershipTermUnit
from .membership_terms_response import MembershipTermsResponse
from .move_to_group import MoveToGroup
from .name_value_pair import NameValuePair
from .neon_pay_setting import NeonPaySetting
from .number import Number
from .object_id_name import ObjectIdName
from .opportunity import Opportunity
from .opportunity_search_param import OpportunitySearchParam
from .opportunity_search_result import OpportunitySearchResult
from .opportunity_shift import OpportunityShift
from .opportunity_shift_search_param import OpportunityShiftSearchParam
from .opportunity_shift_search_result import OpportunityShiftSearchResult
from .opportunity_status import OpportunityStatus
from .opportunity_volunteer_search_param import OpportunityVolunteerSearchParam
from .options_field import OptionsField
from .order import Order
from .order_calculation_result import OrderCalculationResult
from .order_list_response import OrderListResponse
from .order_response import OrderResponse
from .order_response_status import OrderResponseStatus
from .order_shipping import OrderShipping
from .order_status import OrderStatus
from .organization_profile import OrganizationProfile
from .origin import Origin
from .output_fields import OutputFields
from .page_param import PageParam
from .pagination import Pagination
from .pagination_event_registration import PaginationEventRegistration
from .pagination_response_custom_object_field_list_response import PaginationResponseCustomObjectFieldListResponse
from .pagination_response_custom_object_layout_page_item import PaginationResponseCustomObjectLayoutPageItem
from .pagination_response_custom_object_response import PaginationResponseCustomObjectResponse
from .pagination_response_custom_object_validator_rule_response import (
    PaginationResponseCustomObjectValidatorRuleResponse,
)
from .pagination_response_list_record_response import PaginationResponseListRecordResponse
from .pagination_sort_direction import PaginationSortDirection
from .patch_using_patch1_response_200 import PatchUsingPATCH1Response200
from .patch_using_patch2_response_200 import PatchUsingPATCH2Response200
from .patch_using_patch6_response_200 import PatchUsingPATCH6Response200
from .patch_using_patch9_response_200 import PatchUsingPATCH9Response200
from .patch_using_patch10_response_200 import PatchUsingPATCH10Response200
from .patch_using_patch12_response_200 import PatchUsingPATCH12Response200
from .payment import Payment
from .payment_payment_status import PaymentPaymentStatus
from .payment_response import PaymentResponse
from .payment_response_status import PaymentResponseStatus
from .percent import Percent
from .pledge import Pledge
from .pledge_anonymous_type import PledgeAnonymousType
from .pledge_daf_pay_distribution import PledgeDafPayDistribution
from .pledge_payment import PledgePayment
from .pledge_payment_response import PledgePaymentResponse
from .processor_settings import ProcessorSettings
from .product import Product
from .product_custom_field_data import ProductCustomFieldData
from .product_image import ProductImage
from .product_item import ProductItem
from .product_option import ProductOption
from .product_option_item import ProductOptionItem
from .product_option_item_status import ProductOptionItemStatus
from .product_option_selection import ProductOptionSelection
from .product_option_status import ProductOptionStatus
from .product_search_response import ProductSearchResponse
from .product_shipping import ProductShipping
from .product_status import ProductStatus
from .product_type_id import ProductTypeId
from .record_data import RecordData
from .record_response import RecordResponse
from .record_search_criteria import RecordSearchCriteria
from .record_search_criteria_operator import RecordSearchCriteriaOperator
from .record_search_param import RecordSearchParam
from .recurring_donation import RecurringDonation
from .recurring_donation_recurring_period_type import RecurringDonationRecurringPeriodType
from .recurring_donations_response import RecurringDonationsResponse
from .relation_filter import RelationFilter
from .response_entity import ResponseEntity
from .role_volunteer_search_param import RoleVolunteerSearchParam
from .search_criteria import SearchCriteria
from .search_criteria_operator import SearchCriteriaOperator
from .search_criteria_value_list_item import SearchCriteriaValueListItem
from .search_custom_field import SearchCustomField
from .search_custom_field_operators_item import SearchCustomFieldOperatorsItem
from .search_fields import SearchFields
from .search_request import SearchRequest
from .search_request_output_fields_item import SearchRequestOutputFieldsItem
from .search_response import SearchResponse
from .search_response_search_results_item import SearchResponseSearchResultsItem
from .search_response_search_results_item_additional_property import SearchResponseSearchResultsItemAdditionalProperty
from .shift_and_volunteer import ShiftAndVolunteer
from .shift_volunteer_search_param import ShiftVolunteerSearchParam
from .shipping_address import ShippingAddress
from .shipping_address_add import ShippingAddressAdd
from .shipping_address_add_fax_type import ShippingAddressAddFaxType
from .shipping_address_add_phone_1_type import ShippingAddressAddPhone1Type
from .shipping_address_add_phone_2_type import ShippingAddressAddPhone2Type
from .shipping_address_add_phone_3_type import ShippingAddressAddPhone3Type
from .shipping_address_fax_type import ShippingAddressFaxType
from .shipping_address_phone_1_type import ShippingAddressPhone1Type
from .shipping_address_phone_2_type import ShippingAddressPhone2Type
from .shipping_address_phone_3_type import ShippingAddressPhone3Type
from .shipping_method_request import ShippingMethodRequest
from .shipping_method_response import ShippingMethodResponse
from .social_fundraising import SocialFundraising
from .soft_credit import SoftCredit
from .soft_credit_search_result import SoftCreditSearchResult
from .solicitor import Solicitor
from .standard_field import StandardField
from .standard_field_operators_item import StandardFieldOperatorsItem
from .sub_membership import SubMembership
from .sub_membership_change_type import SubMembershipChangeType
from .sub_membership_enroll_type import SubMembershipEnrollType
from .sub_membership_response import SubMembershipResponse
from .sub_membership_response_status import SubMembershipResponseStatus
from .sub_membership_status import SubMembershipStatus
from .sub_membership_term_unit import SubMembershipTermUnit
from .system_user import SystemUser
from .tax_deducible_info import TaxDeducibleInfo
from .tax_deductible_portion import TaxDeductiblePortion
from .text import Text
from .textarea import Textarea
from .ticket import Ticket
from .tickets_per_registration import TicketsPerRegistration
from .tickets_per_registration_operator import TicketsPerRegistrationOperator
from .time_sheet_api import TimeSheetApi
from .time_sheet_api_status import TimeSheetApiStatus
from .time_sheet_item_api import TimeSheetItemApi
from .time_sheet_search_param import TimeSheetSearchParam
from .time_sheet_search_param_status_list_item import TimeSheetSearchParamStatusListItem
from .time_sheet_search_result import TimeSheetSearchResult
from .timestamps import Timestamps
from .tribute import Tribute
from .tribute_type import TributeType
from .update_custom_object import UpdateCustomObject
from .update_event_ticket_using_put_response_200 import UpdateEventTicketUsingPUTResponse200
from .update_using_put1_response_200 import UpdateUsingPUT1Response200
from .update_using_put2_response_200 import UpdateUsingPUT2Response200
from .update_using_put9_response_200 import UpdateUsingPUT9Response200
from .update_using_put11_response_200 import UpdateUsingPUT11Response200
from .user_group_api import UserGroupApi
from .user_group_search_param import UserGroupSearchParam
from .user_group_search_result import UserGroupSearchResult
from .volunteer_account_ids import VolunteerAccountIds
from .volunteer_api import VolunteerApi
from .volunteer_role_api import VolunteerRoleApi
from .volunteer_role_api_status import VolunteerRoleApiStatus
from .volunteer_role_api_status_color import VolunteerRoleApiStatusColor
from .volunteer_role_search_param import VolunteerRoleSearchParam
from .volunteer_role_search_result import VolunteerRoleSearchResult
from .volunteer_search_param import VolunteerSearchParam
from .volunteer_search_result import VolunteerSearchResult
from .webhook import Webhook
from .webhook_trigger import WebhookTrigger
from .wire_payment import WirePayment

__all__ = (
    "Account",
    "AccountContacts",
    "AccountCustomFieldData",
    "AccountCustomFieldDataAccountType",
    "AccountDonationSearchResult",
    "AccountIdAndRefIdResult",
    "AccountIdResult",
    "AccountOrder",
    "AccountOrderItem",
    "AccountOrderItemType",
    "AccountOrderStatus",
    "AccountPledgeSearchResult",
    "AccountRoleApi",
    "AccountSearchResult",
    "AccountSearchResultItem",
    "AccountSearchResultItemUserType",
    "AccountWindfall",
    "Acknowledgee",
    "Activity",
    "ActivityDates",
    "ActivityPriority",
    "AddFundraiserToCampaignUsingPOSTResponse200",
    "AddPaymentRequest",
    "AddPaymentRequestTransactionType",
    "Address",
    "AddressAdd",
    "AddressAddFaxType",
    "AddressAddPhone1Type",
    "AddressAddPhone2Type",
    "AddressAddPhone3Type",
    "AddressFaxType",
    "AddressPhone1Type",
    "AddressPhone2Type",
    "AddressPhone3Type",
    "AdmissionFee",
    "APIMessage",
    "AssignmentVolunteers",
    "AutoNumber",
    "BaseCustomFieldGroup",
    "BaseMembership",
    "BaseMembershipChangeType",
    "BaseMembershipEnrollType",
    "BaseMembershipStatus",
    "BaseMembershipTermUnit",
    "BasicAttribute",
    "BillingAddress",
    "CalculateResult",
    "Campaign",
    "CampaignFundraiser",
    "CampaignStats",
    "CampaignStatus",
    "Catalog",
    "CatalogStatus",
    "Category",
    "CategoryStatus",
    "CheckboxSingle",
    "CheckPayment",
    "CheckPaymentAccountType",
    "CodeNamePair",
    "CodeNamePairStatus",
    "CompanyAccount",
    "Consent",
    "ConsentDataSharing",
    "ConsentEmail",
    "ConsentMail",
    "ConsentPhone",
    "ConsentSms",
    "Contact",
    "CraInfo",
    "CreateCustomObject",
    "CreateCustomObjectObjectRecordDataType",
    "CreateEventTicketUsingPOSTResponse200",
    "CreditCardOfflinePayment",
    "CreditCardOnlinePayment",
    "CustomField",
    "CustomFieldData",
    "CustomFieldDataComponent",
    "CustomFieldDataDataType",
    "CustomFieldDataDisplayType",
    "CustomFieldDataStatus",
    "CustomFieldGroup",
    "CustomFieldGroupComponent",
    "CustomFieldOption",
    "CustomObjectEmailNotification",
    "CustomObjectEmailNotificationNotificationType",
    "CustomObjectField",
    "CustomObjectFieldFieldDataType",
    "CustomObjectFieldListResponse",
    "CustomObjectFieldListResponseFieldDataType",
    "CustomObjectFieldResponse",
    "CustomObjectFieldResponseFieldDataType",
    "CustomObjectFormLayout",
    "CustomObjectFormLayoutEntryResponse",
    "CustomObjectFormLayoutResponse",
    "CustomObjectLayoutListField",
    "CustomObjectLayoutPageItem",
    "CustomObjectListLayout",
    "CustomObjectListLayoutEntryResponse",
    "CustomObjectListLayoutResponse",
    "CustomObjectPageParam",
    "CustomObjectPageParamSortDirection",
    "CustomObjectRecord",
    "CustomObjectRelation",
    "CustomObjectRelationList",
    "CustomObjectRelationListResponse",
    "CustomObjectResponse",
    "CustomObjectStatus",
    "CustomObjectValidatorRule",
    "CustomObjectValidatorRuleResponse",
    "DafPayPayment",
    "Date",
    "DeletePledgePaymentUsingDELETEResponse200",
    "DeleteRecurringUsingDELETEResponse200",
    "DeleteTicketUsingDELETEResponse200",
    "DeleteUsingDELETE10Response200",
    "DeleteUsingDELETE11Response200",
    "DeleteUsingDELETE12Response200",
    "DeleteUsingDELETE13Response200",
    "DeleteUsingDELETE1Response200",
    "DeleteUsingDELETE2Response200",
    "DeleteUsingDELETE5Response200",
    "DeleteUsingDELETE6Response200",
    "DeleteUsingDELETE7Response200",
    "DeleteUsingDELETE8Response200",
    "DeleteUsingDELETE9Response200",
    "DeleteWindfallAllUsingDELETEResponse200",
    "DiscountItem",
    "DiscountItemOrderItemType",
    "Dob",
    "Donation",
    "DonationAnonymousType",
    "DonationItem",
    "DonationItemAnonymousType",
    "DonationItemStatus",
    "DonationResponse",
    "DonationResponseStatus",
    "DonationStatus",
    "DonorCoveredFees",
    "DynaRecurringDonation",
    "ECheckPayment",
    "ECheckPaymentAccountType",
    "EditCustomObjectField",
    "Event",
    "EventAttendee",
    "EventAttendeePhone1Type",
    "EventAttendeeRegistrationStatus",
    "EventAttendees",
    "EventCustomFieldData",
    "EventDates",
    "EventRegistration",
    "EventRegistrationItem",
    "EventRegistrationResponse",
    "EventRegistrationResponseStatus",
    "EventSearchResult",
    "EventSearchResultItem",
    "EventTicket",
    "EventTicketAttendeesPerTicketType",
    "FieldAttribute",
    "FieldOptionValue",
    "File",
    "FilterCriteria",
    "FinancialSettings",
    "FinancialSettingsDonations",
    "FinancialSettingsDonationsType",
    "FinancialSettingsFeeType",
    "Formula",
    "FormulaEmptyFieldTreatAs",
    "FormulaReturnDataType",
    "GenderVO",
    "GenderVOStatus",
    "GenerosityIndicator",
    "GetDonationsUsingGETSortColumn",
    "GetDonationsUsingGETSortDirection",
    "GetEventRegistrationsUsingGET1SortDirection",
    "GetEventRegistrationsUsingGET1SortField",
    "GetEventRegistrationsUsingGETSortColumn",
    "GetEventRegistrationsUsingGETSortDirection",
    "GetPeer2PeerFundraiserUsingGETResponse200",
    "GetPledgesUsingGETSortColumn",
    "GetPledgesUsingGETSortDirection",
    "Grant",
    "GroupVolunteerSearchParam",
    "HouseHoldContactDto",
    "HouseHoldDto",
    "HttpBasic",
    "IdCodeNameTriple",
    "IdCodeNameTriple2",
    "IdCodeNameTriple2Status",
    "IdCodeNameTripleStatus",
    "IdNamePair",
    "IdNamePairStatus",
    "IdResult",
    "IndividualAccount",
    "IndividualToCompany",
    "InKindPayment",
    "Installment",
    "LayoutField",
    "LinkIndividualToCompany",
    "ListCustomFieldsUsingGETCategory",
    "ListMembershipLevelsUsingGETStatus",
    "ListMembershipUsingGETSortColumn",
    "ListMembershipUsingGETSortDirection",
    "ListObjectsResponse",
    "ListOrderUsingGETSortColumn",
    "ListOrderUsingGETSortDirection",
    "ListOrderUsingGETTransactionTypesItem",
    "ListProductUsingGETStatus",
    "ListRecordResponse",
    "ListRecurringUsingGETSortColumn",
    "ListRecurringUsingGETSortDirection",
    "ListRecurringUsingGETStatus",
    "ListRelationTypes1RelationTypeCategory",
    "ListRelationTypesUsingGETRelationTypeCategory",
    "ListUsingGET1Component",
    "ListUsingGETUserType",
    "Location",
    "Login",
    "Lookup",
    "MasterDetail",
    "MasterDetailDeleteAction",
    "Membership",
    "MembershipAutoRenewal",
    "MembershipCalculateDatesResult",
    "MembershipCalculateResult",
    "MembershipChangeType",
    "MemberShipCustomFieldData",
    "MembershipEnrollType",
    "MembershipItem",
    "MembershipItemChangeType",
    "MembershipItemEnrollType",
    "MembershipItemStatus",
    "MembershipItemTermUnit",
    "MembershipLevel",
    "MembershipLevelId",
    "MembershipLevelScopeType",
    "MembershipLevelsResponse",
    "MembershipLevelStatus",
    "MembershipLevelType",
    "MembershipListResponse",
    "MembershipResponse",
    "MembershipResponseStatus",
    "MembershipStatus",
    "MembershipTerm",
    "MembershipTermsResponse",
    "MembershipTermType",
    "MembershipTermUnit",
    "MoveToGroup",
    "NameValuePair",
    "NeonPaySetting",
    "Number",
    "ObjectIdName",
    "Opportunity",
    "OpportunitySearchParam",
    "OpportunitySearchResult",
    "OpportunityShift",
    "OpportunityShiftSearchParam",
    "OpportunityShiftSearchResult",
    "OpportunityStatus",
    "OpportunityVolunteerSearchParam",
    "OptionsField",
    "Order",
    "OrderCalculationResult",
    "OrderListResponse",
    "OrderResponse",
    "OrderResponseStatus",
    "OrderShipping",
    "OrderStatus",
    "OrganizationProfile",
    "Origin",
    "OutputFields",
    "PageParam",
    "Pagination",
    "PaginationEventRegistration",
    "PaginationResponseCustomObjectFieldListResponse",
    "PaginationResponseCustomObjectLayoutPageItem",
    "PaginationResponseCustomObjectResponse",
    "PaginationResponseCustomObjectValidatorRuleResponse",
    "PaginationResponseListRecordResponse",
    "PaginationSortDirection",
    "PatchUsingPATCH10Response200",
    "PatchUsingPATCH12Response200",
    "PatchUsingPATCH1Response200",
    "PatchUsingPATCH2Response200",
    "PatchUsingPATCH6Response200",
    "PatchUsingPATCH9Response200",
    "Payment",
    "PaymentPaymentStatus",
    "PaymentResponse",
    "PaymentResponseStatus",
    "Percent",
    "Pledge",
    "PledgeAnonymousType",
    "PledgeDafPayDistribution",
    "PledgePayment",
    "PledgePaymentResponse",
    "ProcessorSettings",
    "Product",
    "ProductCustomFieldData",
    "ProductImage",
    "ProductItem",
    "ProductOption",
    "ProductOptionItem",
    "ProductOptionItemStatus",
    "ProductOptionSelection",
    "ProductOptionStatus",
    "ProductSearchResponse",
    "ProductShipping",
    "ProductStatus",
    "ProductTypeId",
    "RecordData",
    "RecordResponse",
    "RecordSearchCriteria",
    "RecordSearchCriteriaOperator",
    "RecordSearchParam",
    "RecurringDonation",
    "RecurringDonationRecurringPeriodType",
    "RecurringDonationsResponse",
    "RelationFilter",
    "ResponseEntity",
    "RoleVolunteerSearchParam",
    "SearchCriteria",
    "SearchCriteriaOperator",
    "SearchCriteriaValueListItem",
    "SearchCustomField",
    "SearchCustomFieldOperatorsItem",
    "SearchFields",
    "SearchRequest",
    "SearchRequestOutputFieldsItem",
    "SearchResponse",
    "SearchResponseSearchResultsItem",
    "SearchResponseSearchResultsItemAdditionalProperty",
    "ShiftAndVolunteer",
    "ShiftVolunteerSearchParam",
    "ShippingAddress",
    "ShippingAddressAdd",
    "ShippingAddressAddFaxType",
    "ShippingAddressAddPhone1Type",
    "ShippingAddressAddPhone2Type",
    "ShippingAddressAddPhone3Type",
    "ShippingAddressFaxType",
    "ShippingAddressPhone1Type",
    "ShippingAddressPhone2Type",
    "ShippingAddressPhone3Type",
    "ShippingMethodRequest",
    "ShippingMethodResponse",
    "SocialFundraising",
    "SoftCredit",
    "SoftCreditSearchResult",
    "Solicitor",
    "StandardField",
    "StandardFieldOperatorsItem",
    "SubMembership",
    "SubMembershipChangeType",
    "SubMembershipEnrollType",
    "SubMembershipResponse",
    "SubMembershipResponseStatus",
    "SubMembershipStatus",
    "SubMembershipTermUnit",
    "SystemUser",
    "TaxDeducibleInfo",
    "TaxDeductiblePortion",
    "Text",
    "Textarea",
    "Ticket",
    "TicketsPerRegistration",
    "TicketsPerRegistrationOperator",
    "TimeSheetApi",
    "TimeSheetApiStatus",
    "TimeSheetItemApi",
    "TimeSheetSearchParam",
    "TimeSheetSearchParamStatusListItem",
    "TimeSheetSearchResult",
    "Timestamps",
    "Tribute",
    "TributeType",
    "UpdateCustomObject",
    "UpdateEventTicketUsingPUTResponse200",
    "UpdateUsingPUT11Response200",
    "UpdateUsingPUT1Response200",
    "UpdateUsingPUT2Response200",
    "UpdateUsingPUT9Response200",
    "UserGroupApi",
    "UserGroupSearchParam",
    "UserGroupSearchResult",
    "VolunteerAccountIds",
    "VolunteerApi",
    "VolunteerRoleApi",
    "VolunteerRoleApiStatus",
    "VolunteerRoleApiStatusColor",
    "VolunteerRoleSearchParam",
    "VolunteerRoleSearchResult",
    "VolunteerSearchParam",
    "VolunteerSearchResult",
    "Webhook",
    "WebhookTrigger",
    "WirePayment",
)
