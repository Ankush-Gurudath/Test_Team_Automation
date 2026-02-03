from datetime import datetime

from hamcrest import assert_that, contains_string
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then
from selenium.common import TimeoutException

from pages.add_vehicle_page import *
from pages.device_profile_page import DeviceProfilePage
from pages.dashboard_page import DashboardPage
from pages.edit_vehicle_page import EditVehiclePage
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage
from pages.vehicle_management_page import VehicleManagementPage
from pages.device_management_page import DeviceManagementPage
from pages.add_user_page import AddUserPage
from steps.common import ENV, NEW_UI_FTM_URL
from data.prod.admin_data_prod import AdminDataProd as AD_PROD
from data.stg.admin_data_stg import AdminDataStg as AD_STG
from data.int.admin_data_int import AdminDataInt as AD_INT

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
USER_MANAGEMENT_PAGE = 0
VEHICLE_MANAGEMENT_PAGE = 0
ADD_VEHICLE_PAGE = 0
EDIT_VEHICLE_PAGE = 0
DEVICE_MANAGEMENT_PAGE = 0
DEVICE_PROFILE_PAGE = 0
ADD_USER_PAGE = 0
AD = 0

scenarios('../features/admin_device_new_ui_shell.feature')


# LQ-236
@given('pm user logs in')
def pm_log_in(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, USER_MANAGEMENT_PAGE, VEHICLE_MANAGEMENT_PAGE, ADD_VEHICLE_PAGE, EDIT_VEHICLE_PAGE, DEVICE_MANAGEMENT_PAGE, AD, ADD_USER_PAGE, DEVICE_PROFILE_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)
    VEHICLE_MANAGEMENT_PAGE = VehicleManagementPage(browser)
    ADD_VEHICLE_PAGE = AddVehiclePage(browser)
    EDIT_VEHICLE_PAGE = EditVehiclePage(browser)
    DEVICE_MANAGEMENT_PAGE = DeviceManagementPage(browser)
    ADD_USER_PAGE = AddUserPage(browser)
    DEVICE_PROFILE_PAGE = DeviceProfilePage(browser)

    browser.get(NEW_UI_FTM_URL)

    if ENV == 'int':
        AD = AD_INT
    elif ENV == 'stg':
        AD = AD_STG
    elif ENV == 'prod':
        AD = AD_PROD
    else:
        raise ValueError(f"Unsupported ENV value: {ENV!r}. Must be one of 'int', 'stg', or 'prod'.")

    LOGIN_PAGE.enter_username(AD.pm_only_user_name)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()


@when('the user clicks the "VEHICLES" tab')
def go_to_vehicle_page():
    global tvehicle
    tvehicle = AddVehiclePage(BasePage)
    tvehicle = tvehicle.get_random_name(4)
    DASHBOARD_PAGE.click_admin_tab()
    USER_MANAGEMENT_PAGE.click_vehicle_tab()
    LOGIN_PAGE.wait_for_page_to_fully_load()

    # Add a vehicle to be used in the tests
    VEHICLE_MANAGEMENT_PAGE.click_add_vehicle_button()
    ADD_VEHICLE_PAGE.click_group_add_vehicle_button()
    ADD_VEHICLE_PAGE.search_group_add_vehicle(AD.devicegroup_group)
    ADD_VEHICLE_PAGE.select_group_add_vehicle()
    ADD_VEHICLE_PAGE.click_done_group_add_vehicle()
    ADD_VEHICLE_PAGE.add_vehicle_name(tvehicle)
    EDIT_VEHICLE_PAGE.input_device(AD.devicetest_device)
    EDIT_VEHICLE_PAGE.select_searched_device()
    EDIT_VEHICLE_PAGE.click_status_filter()
    EDIT_VEHICLE_PAGE.select_in_service_status_filter()
    ADD_VEHICLE_PAGE.click_create_vehicle()
    VEHICLE_MANAGEMENT_PAGE.wait_for_page_to_fully_load()
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()


@then(
    'the page header "VEHICLE MANAGEMENT" and the vehicle count are displayed and the table is displayed with columns: "VEHICLE", "GROUP", "DRIVER", "DEVICE", "LAST CONNECTED", "STATUS"')
def verify_vehicle_page_column():
    VEHICLE_MANAGEMENT_PAGE.get_vehicle_page_title_text() == "VEHICLE MANAGEMENT"


# LQ-230
@when('the user clicks the "DEVICES" tab')
def navigate_to_device_management_page():
    USER_MANAGEMENT_PAGE.click_devices_tab()
    USER_MANAGEMENT_PAGE.close_walkme_dialog()


@then('the page header "DEVICE MANAGEMENT" is displayed and the user count are displayed'
      ' and the table is displayed with columns: "DEVICE", "DEVICE TYPE", "VEHICLE", "GROUP", "LAST CONNECTED", '
      '"INITIAL CONNECTION"')
def verify_device_management_table():
    assert DEVICE_MANAGEMENT_PAGE.get_device_management_title() == "DEVICE MANAGEMENT"
    assert DEVICE_MANAGEMENT_PAGE.device_count_is_displayed() is True
    assert DEVICE_MANAGEMENT_PAGE.get_device_column_title() == "DEVICE"
    assert DEVICE_MANAGEMENT_PAGE.get_device_type_column_title() == "DEVICE TYPE"
    assert DEVICE_MANAGEMENT_PAGE.get_group_column_title() == "GROUP"
    assert DEVICE_MANAGEMENT_PAGE.get_status_column_title() == "STATUS"
    assert DEVICE_MANAGEMENT_PAGE.get_last_connected_column_title() == "LAST COMMUNICATED"
    assert DEVICE_MANAGEMENT_PAGE.get_initial_connection_column_title() == "INITIAL CONNECTION"


# LQ-231
@when('the user sets group filter to one group in Device Management Page')
def set_group_filter_device_management():
    DEVICE_MANAGEMENT_PAGE.click_group_filter()
    DEVICE_MANAGEMENT_PAGE.search_group_filter(AD.devicegroup_group)
    DEVICE_MANAGEMENT_PAGE.select_searched_group()
    DEVICE_MANAGEMENT_PAGE.click_done_group_filter()


@then('the devices belong to the group are listed')
def verify_group_filter_device_management():
    assert_that(DEVICE_MANAGEMENT_PAGE.get_first_group_name(AD.devicegroup_group), IsEqualIgnoringCase(AD.devicegroup_group))


@when('the user clicks on "Device Type" filter & the user selects one type')
def set_device_type_device_management():
    DEVICE_MANAGEMENT_PAGE.click_device_type(AD.device_type)
    DEVICE_MANAGEMENT_PAGE.select_device_type(AD.device_type)
    DEVICE_MANAGEMENT_PAGE.click_device_title()


@then('the devices of the selected type are displayed')
def verify_device_type_filter_device_management():
    assert_that(DEVICE_MANAGEMENT_PAGE.get_first_row_device_type(AD.device_type), IsEqualIgnoringCase(AD.device_type))


@when('the user clicks on "Status" filter & the user selects "In Service"')
def set_status_filter_device_management():
    DEVICE_MANAGEMENT_PAGE.click_status_filter()
    DEVICE_MANAGEMENT_PAGE.select_status_filter()
    DEVICE_MANAGEMENT_PAGE.open_or_close_status_filter()


@then('the devices with "In Service" status are displayed')
def verify_status_filter_device_management():
    assert_that(DEVICE_MANAGEMENT_PAGE.get_first_status_name("In Service"), contains_string("In Service"))


@when('the user enters some characters into "Search Device" field')
def search_device_filter_device_management():
    DEVICE_MANAGEMENT_PAGE.click_reset_button()
    DEVICE_MANAGEMENT_PAGE.click_select_search_filter()
    DEVICE_MANAGEMENT_PAGE.select_device_filter()
    DEVICE_MANAGEMENT_PAGE.search_device_filter(AD.device)


@then('the devices that contained inputted characters in the serial number are shown')
def verify_search_device_filter_device_management():
    assert_that(DEVICE_MANAGEMENT_PAGE.get_first_device_name(AD.device), IsEqualIgnoringCase(AD.device))


# LQ-4456
@when('the user clicks a device link')
def navigate_to_device_profile_page():
    DEVICE_PROFILE_PAGE.click_device_serial_number()


@then('the "DEVICE PROFILE" page is opened and the fields are displayed:"DEVICE", "DEVICE TYPE", "GROUP", "STATUS", '
      '"HEALTH", "LAST COMMUNICATED", "LAST MOVEMENT", "INITIAL CONNECTION"')
def verify_device_profile_page():
    assert DEVICE_PROFILE_PAGE.get_device_profile_title() == 'DEVICE PROFILE'
    assert DEVICE_PROFILE_PAGE.get_device_profile_summary_device() == 'Device'
    assert DEVICE_PROFILE_PAGE.get_device_profile_summary_device_type() == 'DEVICE TYPE'
    assert DEVICE_PROFILE_PAGE.get_device_profile_summary_group() == 'GROUP'
    assert DEVICE_PROFILE_PAGE.get_device_profile_summary_status() == 'STATUS'
    assert DEVICE_PROFILE_PAGE.get_device_profile_summary_health() == 'HEALTH'
    assert DEVICE_PROFILE_PAGE.get_device_profile_summary_last_communicated() == 'LAST COMMUNICATED'
    assert DEVICE_PROFILE_PAGE.get_device_profile_summary_last_movement() == 'LAST MOVEMENT'
    assert DEVICE_PROFILE_PAGE.get_device_profile_summary_initial_connection() == 'INITIAL CONNECTION'


# LQ-233
@when('the user checks some available devices & the user clicks "Move Group" & the user selects one group & the user '
      'clicks "Done" on the Group Selector pop-up')
def device_move_group_device_management():
    USER_MANAGEMENT_PAGE.click_devices_tab()
    DEVICE_MANAGEMENT_PAGE.select_first_device()
    DEVICE_MANAGEMENT_PAGE.click_move_group()
    DEVICE_MANAGEMENT_PAGE.search_group_move(AD.move_group)
    DEVICE_MANAGEMENT_PAGE.select_searched_move_group()
    DEVICE_MANAGEMENT_PAGE.click_done_move_group()
    DEVICE_MANAGEMENT_PAGE.click_continue_move_group()
    DEVICE_MANAGEMENT_PAGE.click_reset_button()
    DEVICE_MANAGEMENT_PAGE.click_select_search_filter()
    DEVICE_MANAGEMENT_PAGE.select_device_filter()
    DEVICE_MANAGEMENT_PAGE.search_device_filter(AD.device)


@then('the selected devices are moved to the new group')
def verify_device_move_group_device_management():
    assert_that(DEVICE_MANAGEMENT_PAGE.get_first_group_name(AD.move_group), IsEqualIgnoringCase(AD.move_group))


# LQ-234
@when(
    'the user checks some available devices & the user clicks "Change Status" & the user selects "Spare" & the user clicks Save')
def change_status_to_spare_device_management():
    DEVICE_MANAGEMENT_PAGE.select_first_device()
    DEVICE_MANAGEMENT_PAGE.click_change_status()
    DEVICE_MANAGEMENT_PAGE.click_status_spare()
    DEVICE_MANAGEMENT_PAGE.click_save_change_status()


@then('the status of selected devices are updated to Spare')
def verify_change_status_to_spare_device_management():
    assert DEVICE_MANAGEMENT_PAGE.get_first_status_name("Spare") == "Spare"

# Delete the vehicle added for the tests
@when('the user click on vehicle menu to delete the vehicle added for tests')
def delete_vehicle_in_edit_vehicle_page():
    USER_MANAGEMENT_PAGE.click_vehicle_tab()
    VEHICLE_MANAGEMENT_PAGE.click_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.click_vehicle_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.search_name_filter(tvehicle)
    VEHICLE_MANAGEMENT_PAGE.click_expected_vehicle_name(tvehicle)
    EDIT_VEHICLE_PAGE.click_delete_button_in_edit_vehicle_page()
    EDIT_VEHICLE_PAGE.click_continue_button_pop_up()
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()


@then('the vehicle is deleted')
def verify_delete_vehicle():
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()
    VEHICLE_MANAGEMENT_PAGE.click_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.click_vehicle_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.search_name_filter(tvehicle)
    assert VEHICLE_MANAGEMENT_PAGE.get_row_count(20) == 0
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()


@given('the "Administrator/FA" user is in Device Page')
def admin_fa_in_device_page(browser):
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_sign_out_new_ui()
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(AD.FA_internal_user)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_company()
    LOGIN_PAGE.click_select_company_button()


@when('the user clicks on the "View Change History" in Device Management page')
def click_view_change_history_device_management():
    DASHBOARD_PAGE.click_admin_tab()
    USER_MANAGEMENT_PAGE.click_devices_tab()
    DEVICE_MANAGEMENT_PAGE.click_view_change_history()


@then('the user should be able to see the table columns: "DEVICE AFFECTED", "ACTION", "ACTION DETAILS","EDITOR", "ACTION DATE" and page header "Device Audit Log"')
def verify_table_columns():
    assert DEVICE_MANAGEMENT_PAGE.get_device_affected_column_title() == "DEVICE AFFECTED"
    assert DEVICE_MANAGEMENT_PAGE.get_action_column_title() == "ACTION"
    assert DEVICE_MANAGEMENT_PAGE.get_action_details_column_title() == "ACTION DETAILS"
    assert DEVICE_MANAGEMENT_PAGE.get_editor_column_title() == "EDITOR"
    assert DEVICE_MANAGEMENT_PAGE.get_action_date_column_title() == "ACTION DATE"
    assert_that(DEVICE_MANAGEMENT_PAGE.get_device_audit_log_title(), contains_string("Device Audit Log"))

@then('The user should be see the filters ‘Search Device Affected’, Date filter and ‘Select Action(s)’ in the header, and the ‘Download Log’ button')
def verify_filters_and_download_button():
    assert DEVICE_MANAGEMENT_PAGE.search_device_affected_is_displayed() is True
    assert DEVICE_MANAGEMENT_PAGE.select_actions_is_displayed() is True
    assert DEVICE_MANAGEMENT_PAGE.download_log_button_is_displayed() is True
    assert DEVICE_MANAGEMENT_PAGE.date_filter_is_displayed() is True


@when('the user enters a valid device number in "Search Device Affected"')
def search_device_affected():
    global AFFECTED_DEVICE
    AFFECTED_DEVICE = DEVICE_MANAGEMENT_PAGE.get_first_device_affected_text()
    DEVICE_MANAGEMENT_PAGE.search_device_affected(AFFECTED_DEVICE)

@then('the system should display only matching logs')
def verify_search_device_affected():
    assert_that(DEVICE_MANAGEMENT_PAGE.get_first_device_affected_text(), IsEqualIgnoringCase(AFFECTED_DEVICE))


@when('the user enters an invalid device number in "Search Device Affected"')
def search_invalid_device_affected():
    DEVICE_MANAGEMENT_PAGE.click_reset_in_audit_page()
    DEVICE_MANAGEMENT_PAGE.search_device_affected("InvalidDevice123")


@then('the system should show no results message')
def verify_no_results_message():
    assert DEVICE_MANAGEMENT_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected device/date range"


@when('the user selects a date range in the Date filter')
def select_date_range_device_audit_log():
    DEVICE_MANAGEMENT_PAGE.click_reset_in_audit_page()
    DEVICE_MANAGEMENT_PAGE.click_date_range_dropdown()
    DEVICE_MANAGEMENT_PAGE.select_date_range_today()


@then('the system should display logs within the selected date range')
def verify_date_range_logs_device_audit_log():
    assert_that(USER_MANAGEMENT_PAGE.get_action_date(), contains_string(DEVICE_MANAGEMENT_PAGE.get_time_today()))


@when('the user clicks on the "Close" button')
def click_close_button_device_audit_log():
    DEVICE_MANAGEMENT_PAGE.click_close_device_audit_log()


@then('the device Audit Log tab should be closed successfully')
def verify_close_device_audit_log():
    assert DEVICE_MANAGEMENT_PAGE.view_change_history_popup_displayed() is False


@given('user moved a device to another group in Device Management page')
def user_move_device_to_another_group(context):
    group_name = DEVICE_MANAGEMENT_PAGE.get_first_row_group_name()
    if group_name == AD.group:
        group_name = AD.group1
    else:
        group_name = AD.group
    context['device_name'] = DEVICE_MANAGEMENT_PAGE.get_first_device_text()
    DEVICE_MANAGEMENT_PAGE.select_first_device()
    DEVICE_MANAGEMENT_PAGE.click_move_group()
    DEVICE_MANAGEMENT_PAGE.search_group_move(group_name)
    DEVICE_MANAGEMENT_PAGE.select_searched_move_group()
    DEVICE_MANAGEMENT_PAGE.click_done_move_group()
    DEVICE_MANAGEMENT_PAGE.click_continue_move_group()
    DEVICE_MANAGEMENT_PAGE.click_reset_button()


@when('user clicks on "View Change History" in Device Management page and search for a device')
def user_clicks_view_change_history_device_management(context):
    DEVICE_MANAGEMENT_PAGE.click_view_change_history()
    DEVICE_MANAGEMENT_PAGE.search_device_affected(context['device_name'])


@then('the Device Audit Log should display logs with the Action type as "Edited" and Action details as Group')
def verify_action_type_edited_and_action_details_group():
    assert DEVICE_MANAGEMENT_PAGE.get_first_action_type_text() == "Edited"
    assert DEVICE_MANAGEMENT_PAGE.get_first_action_details_text() == "Group"


# LQ-249538
@when('the user selects the Action "Added" from the "Select Action(s)" filter dropdown')
def select_action_added_device_audit_log():
    DEVICE_MANAGEMENT_PAGE.click_select_actions_filter()
    DEVICE_MANAGEMENT_PAGE.select_action_type_added()


@then('the Device Audit Log should display logs with the Action type as "Added"')
def verify_action_type_filter():
    try:
        assert DEVICE_MANAGEMENT_PAGE.get_first_action_type_text() == "Added"
    except TimeoutException:
        assert DEVICE_MANAGEMENT_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected device/date range"


@when('the user selects the Action "Edited" from the "Select Action(s)" filter dropdown')
def select_action_edited_device_audit_log():
    DEVICE_MANAGEMENT_PAGE.click_reset_in_audit_page()
    DEVICE_MANAGEMENT_PAGE.click_select_actions_filter()
    DEVICE_MANAGEMENT_PAGE.select_action_type_edited()


@then('the Device Audit Log should display logs with the Action type as "Edited"')
def verify_action_type_edited_filter():
    try:
        assert DEVICE_MANAGEMENT_PAGE.get_first_action_type_text() == "Edited"
    except TimeoutException:
        assert DEVICE_MANAGEMENT_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected device/date range"


@when('the user selects the Action "Deleted" from the "Select Action(s)" filter dropdown')
def select_action_deleted_device_audit_log():
    DEVICE_MANAGEMENT_PAGE.click_reset_in_audit_page()
    DEVICE_MANAGEMENT_PAGE.click_select_actions_filter()
    DEVICE_MANAGEMENT_PAGE.select_deleted_action_type()


@then('the Device Audit Log should display logs with the Action type as "Deleted"')
def verify_action_type_deleted_filter():
    try:
        assert DEVICE_MANAGEMENT_PAGE.get_first_action_type_text() == "Deleted"
    except TimeoutException:
        assert DEVICE_MANAGEMENT_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected device/date range"



@when('the user selects the Action "Imported" from the "Select Action(s)" filter dropdown')
def select_action_imported_device_audit_log():
    DEVICE_MANAGEMENT_PAGE.click_reset_in_audit_page()
    DEVICE_MANAGEMENT_PAGE.click_select_actions_filter()
    DEVICE_MANAGEMENT_PAGE.select_imported_action_type()


@then('the Device Audit Log should display logs with the Action type as "Imported"')
def verify_action_type_imported_filter():
    try:
        assert DEVICE_MANAGEMENT_PAGE.get_first_action_type_text() == "Imported"
    except TimeoutException:
        assert DEVICE_MANAGEMENT_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected device/date range"


# LQ-249600
@when('the user clicks "Download Log" in the Device audit log tab')
def click_download_log_device_audit_log():
    DEVICE_MANAGEMENT_PAGE.click_reset_in_audit_page()
    DEVICE_MANAGEMENT_PAGE.click_download_log_button()


@then('the Device audit log is downloaded successfully')
def verify_download_log_device_audit_log():
    file_name = DEVICE_MANAGEMENT_PAGE.get_audit_log_file_name()
    DEVICE_MANAGEMENT_PAGE.wait_for_file_downloaded(file_name)
    # assert VEHICLE_MANAGEMENT_PAGE.check_file_exist(file_name) is True


@when('search an invalid device in "Search device Affected" filter')
def search_invalid_device_audit_log():
    DEVICE_MANAGEMENT_PAGE.search_device_affected("NoSuchDevice123")


@then('the "Download Log" button is disabled in Device Audit Log')
def verify_download_log_button_disabled():
    assert DEVICE_MANAGEMENT_PAGE.download_log_button_disabled_displayed() is True
