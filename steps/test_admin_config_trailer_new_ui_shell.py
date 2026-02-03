from hamcrest import assert_that
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase, equal_to_ignoring_case
from pytest_bdd import scenarios, given, when, then
from pages.add_user_page import AddUserPage
from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from pages.configuration_setting_page import ConfigurationSettingPage
from pages.login_page import LoginPage
from steps.common import ENV, NEW_UI_FTM_URL
from pages.user_management_page import UserManagementPage
from pages.trailer_management_page import TrailerManagementPage
from pages.edit_trailer_page import EditTrailerPage
from pages.add_trailer_page import AddTrailerPage
from data.prod.admin_data_prod import AdminDataProd as AD_PROD
from data.stg.admin_data_stg import AdminDataStg as AD_STG
from data.int.admin_data_int import AdminDataInt as AD_INT

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
CONFIGURATION_SETTING_PAGE = 0
USER_MANAGEMENT_PAGE = 0
TRAILER_MANAGEMENT_PAGE = 0
AD = 0
ADD_TRAILER_PAGE = 0
ADD_USER_PAGE = 0
EDIT_TRAILER_PAGE = 0

scenarios('../features/admin_config_trailer_new_ui_shell.feature')


# LQ-242
@given('Administrator user is in Admin')
def login_as_admin(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, CONFIGURATION_SETTING_PAGE, TRAILER_MANAGEMENT_PAGE, USER_MANAGEMENT_PAGE, AD, ADD_TRAILER_PAGE, EDIT_TRAILER_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)
    TRAILER_MANAGEMENT_PAGE = TrailerManagementPage(browser)
    CONFIGURATION_SETTING_PAGE = ConfigurationSettingPage(browser)
    ADD_TRAILER_PAGE = AddTrailerPage(browser)
    EDIT_TRAILER_PAGE = EditTrailerPage(browser)

    browser.get(NEW_UI_FTM_URL)

    if ENV == 'int':
        AD = AD_INT
    elif ENV == 'stg':
        AD = AD_STG
    elif ENV == 'prod':
        AD = AD_PROD
    else:
        raise ValueError(f"Unsupported ENV value: {ENV!r}. Must be one of 'int', 'stg', or 'prod'.")

    LOGIN_PAGE.enter_username(AD.admin_user_name)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_company()
    LOGIN_PAGE.click_select_company_button()
    DASHBOARD_PAGE.click_admin_tab()


@when('the user clicks CONFIG SETTING')
def navigate_to_config_setting_page():
    USER_MANAGEMENT_PAGE.click_config_setting_tab()


@then('Full access role is in tier 1 by default with "Role","Description" and "Admin Permission"')
def verify_tier_1_full_access_role():
    assert CONFIGURATION_SETTING_PAGE.get_tier1_label() == "Tier 1"
    assert CONFIGURATION_SETTING_PAGE.get_role_label() == "ROLE"
    assert_that(CONFIGURATION_SETTING_PAGE.get_description_label(), equal_to_ignoring_case("Description"))
    assert_that(CONFIGURATION_SETTING_PAGE.get_admin_permission_label(), equal_to_ignoring_case("Admin Permission"))


@then('the user should see the "Edit" icon for the first tier')
def user_should_see_edit_icon():
    assert CONFIGURATION_SETTING_PAGE.edit_icon_is_displayed() is True


# LQ-244
@when('the user click the "Add New Tier" button & the user selects some roles & the user clicks "Confirm" on the popup')
def add_new_tier():
    CONFIGURATION_SETTING_PAGE.click_add_new_tier_button()
    CONFIGURATION_SETTING_PAGE.click_select_roles_button()
    CONFIGURATION_SETTING_PAGE.click_first_role_dropdown_button()
    CONFIGURATION_SETTING_PAGE.click_role_twice_button()
    CONFIGURATION_SETTING_PAGE.click_select_roles_confirm_button()


@then('the selected roles are listed under the newly added tier')
def verify_new_role_tier():
    assert CONFIGURATION_SETTING_PAGE.get_new_role_added_text() == "API Developer"


@then('the user should see the both "Edit" and "Delete" icon')
def user_should_see_the_both_edit_and_delete_icon_for_second_tier():
    assert CONFIGURATION_SETTING_PAGE.edit_icon_for_second_tier_displayed() is True
    assert CONFIGURATION_SETTING_PAGE.delete_icon_for_second_tier_displayed() is True


# LQ-5557
@when(
    'the user clicks "Edit Tier" icon for tier 1 & the user checks some roles & the user clicks "Confirm" on the popup')
def edit_tier():
    CONFIGURATION_SETTING_PAGE.click_edit_tier_button()
    CONFIGURATION_SETTING_PAGE.click_edit_roles_button()
    if CONFIGURATION_SETTING_PAGE.role_already_selected() is True:
        CONFIGURATION_SETTING_PAGE.delete_role_already_selected()
        CONFIGURATION_SETTING_PAGE.click_role_twice_button()
        CONFIGURATION_SETTING_PAGE.click_edit_roles_confirm_button()
        CONFIGURATION_SETTING_PAGE.click_refresh_button()
        CONFIGURATION_SETTING_PAGE.click_edit_tier_button()
        CONFIGURATION_SETTING_PAGE.click_edit_roles_button()
    CONFIGURATION_SETTING_PAGE.click_select_roles_edit_button()
    CONFIGURATION_SETTING_PAGE.click_role_twice_button()
    CONFIGURATION_SETTING_PAGE.click_edit_roles_confirm_button()


@then('the checked roles are updated')
def verify_edit_tier_roles():
    assert CONFIGURATION_SETTING_PAGE.get_second_tier2_role_text() == "API Developer Read Only"


@when('the user clicks on the "Delete Tier" button & the user clicks "Confirm" button on the popup')
def delete_tier():
    CONFIGURATION_SETTING_PAGE.click_delete_tier_button()
    CONFIGURATION_SETTING_PAGE.click_confirm_delete_tier_button()


@then('the tier is deleted')
def verify_delete_tier():
    assert CONFIGURATION_SETTING_PAGE.get_tier2_text("Unranked Tier") == "Unranked Tier"


# LQ-12128
@when('the user clicks the "TRAILER" tab')
def go_to_trailer_management_page():
    TRAILER_MANAGEMENT_PAGE.click_trailer_tab()


@then(
    'the page header "TRAILER MANAGEMENT" is displayed and the table is displayed with columns: "TRAILER", "GROUP", "LICENSE PLATE", "VIN", "INSPECTION LIST"')
def verify_trailer_management_page():
    assert TRAILER_MANAGEMENT_PAGE.get_trailer_management_text() == "TRAILER MANAGEMENT"
    assert TRAILER_MANAGEMENT_PAGE.get_trailer_column_text() == "TRAILER"
    assert TRAILER_MANAGEMENT_PAGE.get_group_column_text() == "GROUP"
    assert TRAILER_MANAGEMENT_PAGE.get_license_plate_column_text() == "LICENSE PLATE"
    assert TRAILER_MANAGEMENT_PAGE.get_vin_column_text() == "VIN"
    assert TRAILER_MANAGEMENT_PAGE.get_inspection_list_column_text() == "INSPECTION LIST"


@then('the user should see the filters like "Select Group(s)", "Search Trailer" and "Reset"')
def user_should_see_filters():
    assert TRAILER_MANAGEMENT_PAGE.group_filter_option_is_present() is True
    assert TRAILER_MANAGEMENT_PAGE.search_trailer_option_is_present() is True


@then('the user should see the Trailers count and "Add Trailers" button')
def the_user_should_see_trailer_count_and_add_trailer_option():
    assert TRAILER_MANAGEMENT_PAGE.trailer_count_is_present() is True
    assert TRAILER_MANAGEMENT_PAGE.add_trailer_button_is_present() is True


# LQ-12129
@when('the user sets group filter to one group on the Trailer Management page')
def set_group_filter_trailer_management_page():
    TRAILER_MANAGEMENT_PAGE.click_group_filter()
    TRAILER_MANAGEMENT_PAGE.search_group(AD.group)
    TRAILER_MANAGEMENT_PAGE.select_searched_group()
    TRAILER_MANAGEMENT_PAGE.click_done_button()


@then('the Trailer belong to the group are listed')
def verify_group_filter_trailer_management_page():
    assert TRAILER_MANAGEMENT_PAGE.get_first_trailer_group(AD.group) == AD.group


@when('the user enters some characters into "Search Trailer" field on the Trailer Management page')
def search_trailer():
    TRAILER_MANAGEMENT_PAGE.type_trailer_name("TestTrailer")


@then('the Trailers that contained the inputted characters are shown')
def verify_search_trailer_trailer_management_page():
    assert TRAILER_MANAGEMENT_PAGE.get_row_count(10) == 0
    TRAILER_MANAGEMENT_PAGE.click_reset_button()


# LQ-12159
@when(
    'the user clicks on "Add Trailer" & the user enters required fields: "Group" and "Trailer Name" & the user enters required fields: "Group" and "Trailer Name"')
def add_new_trailer():
    global tabn
    tabn = AddUserPage(BasePage)
    tabn.get_random_string()
    tabn.get_random_name(6)
    TRAILER_MANAGEMENT_PAGE.click_add_trailer_button()
    ADD_TRAILER_PAGE.click_group_trailer_filter()
    ADD_TRAILER_PAGE.search_group_trailer_filter(AD.group)
    ADD_TRAILER_PAGE.select_searched_group()
    ADD_TRAILER_PAGE.click_done_trailer_group_button()
    ADD_TRAILER_PAGE.type_trailer_name(tabn.random_name)
    ADD_TRAILER_PAGE.type_vin_number(tabn.random_word)
    ADD_TRAILER_PAGE.click_create_trailer()


@then('the Trailer is added')
def verify_added_new_trailer():
    TRAILER_MANAGEMENT_PAGE.search_trailer_name(tabn.random_name)
    assert TRAILER_MANAGEMENT_PAGE.get_searched_trailer_name(tabn.random_name) == tabn.random_name


# LQ-17331
@when(
    'the user clicks on the name of a trailer & the user changes "Trailer Name" on Edit Trailer page & the user sets one group & the user clicks "Save Changes"')
def edit_trailer_name():
    TRAILER_MANAGEMENT_PAGE.click_added_trailer_name()
    EDIT_TRAILER_PAGE.clear_trailer_name()
    EDIT_TRAILER_PAGE.edit_first_name_trailer(tabn.random_word)
    EDIT_TRAILER_PAGE.click_save_trailer()
    TRAILER_MANAGEMENT_PAGE.click_reset_button()


@then('the First Name of the edited trailer is updated')
def verify_edit_trailer_name():
    TRAILER_MANAGEMENT_PAGE.search_trailer_name(tabn.random_word)
    assert TRAILER_MANAGEMENT_PAGE.get_searched_trailer_name(tabn.random_word) == tabn.random_word


# LQ-15957
@when('the "users" checks one trailer and the "users" clicks "Set Inspection List"')
def set_single_inspection_list_for_trailer():
    TRAILER_MANAGEMENT_PAGE.click_reset_button()
    TRAILER_MANAGEMENT_PAGE.select_first_trailer()
    TRAILER_MANAGEMENT_PAGE.click_set_inspection_list_button()
    TRAILER_MANAGEMENT_PAGE.select_second_inspection_list_dialog()
    TRAILER_MANAGEMENT_PAGE.click_set_inspection_list_dialog()


@then('the inspection list is assigned to the selected trailer')
def verify_single_inspection_list_for_trailer():
    assert TRAILER_MANAGEMENT_PAGE.get_first_inspection_list_text(
        AD.second_trailer_inspection_list) == AD.second_trailer_inspection_list


@when('the "users" checks one or more trailers & the "users" clicks "Set Inspection List"')
def set_multiple_inspection_list_for_trailer():
    TRAILER_MANAGEMENT_PAGE.select_first_trailer()
    TRAILER_MANAGEMENT_PAGE.select_second_trailer()
    TRAILER_MANAGEMENT_PAGE.click_set_inspection_list_button()
    TRAILER_MANAGEMENT_PAGE.select_first_inspection_list_dialog()
    TRAILER_MANAGEMENT_PAGE.select_second_inspection_list_dialog()
    TRAILER_MANAGEMENT_PAGE.click_set_inspection_list_dialog()


@then('the inspection lists are assigned to the selected trailers')
def assert_multiple_inspection_list_for_trailer():
    second_list = AD.second_trailer_inspection_list + ", " + AD.first_trailer_inspection_list
    assert TRAILER_MANAGEMENT_PAGE.get_first_inspection_list_text(second_list) == second_list
    assert TRAILER_MANAGEMENT_PAGE.get_second_inspection_list_text() == second_list


@when('the user clicks the "Program Configuration" tab')
def user_clicks_program_configuration_tab():
    CONFIGURATION_SETTING_PAGE.click_program_configuration_tab()


@then('the user should see the behavior "Critical Distance" and the alerts like "Audio Alerts","LED Alerts" and "Events"')
def verify_user_should_see_critical_distance():
    assert CONFIGURATION_SETTING_PAGE.get_critical_distance_text() == "Critical Distance"
    assert CONFIGURATION_SETTING_PAGE.get_audio_alerts_text() == "Audio Alerts"
    assert CONFIGURATION_SETTING_PAGE.get_led_alerts_text() == "LED Alerts"
    assert CONFIGURATION_SETTING_PAGE.get_events_text() == "Events"


@then('the user should see the behavior "Following Distance" and the alerts like "Audio Alerts","LED Alerts" and "Events"')
def verify_user_should_see_following_distance():
    assert CONFIGURATION_SETTING_PAGE.get_following_distance_text() == "Following Distance"
    assert CONFIGURATION_SETTING_PAGE.get_audio_alerts_for_following_distance_text() == "Audio Alerts"
    assert CONFIGURATION_SETTING_PAGE.get_led_alerts_for_following_distance_text() == "LED Alerts"
    assert CONFIGURATION_SETTING_PAGE.get_events_for_following_distance_text() == "Events"


@then('the user should see the behavior "Lane Departure" and the alerts like "Audio Alerts","LED Alerts" and "Events"')
def verify_user_should_see_lane_departure():
    assert CONFIGURATION_SETTING_PAGE.get_lane_departure_text() == "Lane Departure"
    assert CONFIGURATION_SETTING_PAGE.get_audio_alerts_for_lane_departure_text() == "Audio Alerts"
    assert CONFIGURATION_SETTING_PAGE.get_led_alerts_for_lane_departure_text() == "LED Alerts"
    assert CONFIGURATION_SETTING_PAGE.get_events_for_lane_departure_text() == "Events"


@then('the user should see the behavior "Rolling Stop" and the alerts like "Audio Alerts","LED Alerts" and "Events"')
def verify_user_should_see_rolling_stop():
    assert CONFIGURATION_SETTING_PAGE.get_rolling_stop_text() == "Rolling Stop"
    assert CONFIGURATION_SETTING_PAGE.get_audio_alerts_for_rolling_stop_text() == "Audio Alerts"
    assert CONFIGURATION_SETTING_PAGE.get_led_alerts_for_rolling_stop_text() == "LED Alerts"
    assert CONFIGURATION_SETTING_PAGE.get_events_for_rolling_stop_text() == "Events"


@when('the user clicks the "Action Plan" tab')
def user_clicks_action_plan_tab():
    CONFIGURATION_SETTING_PAGE.click_action_plan_tab()


@then('the user should see the corrective action title and "Edit" button in Action Plan')
def user_should_see_corrective_action_title_and_edit_button():
    assert CONFIGURATION_SETTING_PAGE.get_corrective_action_title_text() == "Corrective Action"
    assert CONFIGURATION_SETTING_PAGE.edit_button_in_action_plan_is_displayed() is True




#CHIPER-4016
@when('the user clicks on "Add Corrective Action" & the user enters required fields: "Name" and "Description" & the user clicks "Save"')
def add_corrective_action():
    CONFIGURATION_SETTING_PAGE.click_edit_button_in_action_plan()
    CONFIGURATION_SETTING_PAGE.click_add_corrective_action_button()
    CONFIGURATION_SETTING_PAGE.type_corrective_action_name(AD.corrective_action_name)
    CONFIGURATION_SETTING_PAGE.type_corrective_action_description(AD.corrective_action_description)
    CONFIGURATION_SETTING_PAGE.click_save_corrective_action_button()


@then('the Corrective Action is added')
def verify_added_corrective_action():
    assert CONFIGURATION_SETTING_PAGE.get_added_corrective_action_text() == AD.corrective_action_name


@when('the user clicks on "Delete" button for a corrective action & the user clicks "Confirm" on the popup')
def delete_corrective_action():
    CONFIGURATION_SETTING_PAGE.click_edit_button_in_action_plan()
    CONFIGURATION_SETTING_PAGE.click_delete_button_in_action_plan()
    CONFIGURATION_SETTING_PAGE.click_confirm_delete_corrective_action_button()
    CONFIGURATION_SETTING_PAGE.click_save_corrective_action_button()


@then('the Corrective Action is deleted')
def verify_deleted_corrective_action():
    assert CONFIGURATION_SETTING_PAGE.added_creative_action_plan_is_deleted() is False



