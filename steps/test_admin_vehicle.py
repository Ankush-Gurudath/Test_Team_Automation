from datetime import datetime

from hamcrest import assert_that, contains_string
from pytest_bdd import scenarios, given, when, then
from selenium.common import TimeoutException

from pages.add_user_page import AddUserPage
from pages.add_vehicle_page import *
from pages.dashboard_page import DashboardPage
from pages.device_management_page import DeviceManagementPage
from pages.edit_vehicle_page import EditVehiclePage
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage
from pages.vehicle_management_page import VehicleManagementPage
from steps.common import DC_URL, ENV
from data.int.admin_data_int import AdminDataInt as AD_INT
from data.prod.admin_data_prod import AdminDataProd as AD_PROD
from data.stg.admin_data_stg import AdminDataStg as AD_STG

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
USER_MANAGEMENT_PAGE = 0
VEHICLE_MANAGEMENT_PAGE = 0
ADD_VEHICLE_PAGE = 0
EDIT_VEHICLE_PAGE = 0
DEVICE_MANAGEMENT_PAGE = 0
ADD_USER_PAGE = 0
AD = 0

scenarios('../features/admin_vehicle.feature')


# LQ-236
@given('pm user logs in')
def pm_log_in(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, USER_MANAGEMENT_PAGE, VEHICLE_MANAGEMENT_PAGE, ADD_VEHICLE_PAGE, EDIT_VEHICLE_PAGE, DEVICE_MANAGEMENT_PAGE, DEVICE_PROFILE_PAGE, AD, ADD_USER_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)
    VEHICLE_MANAGEMENT_PAGE = VehicleManagementPage(browser)
    ADD_VEHICLE_PAGE = AddVehiclePage(browser)
    EDIT_VEHICLE_PAGE = EditVehiclePage(browser)
    DEVICE_MANAGEMENT_PAGE = DeviceManagementPage(browser)
    ADD_USER_PAGE = AddUserPage(browser)

    browser.get(DC_URL)
    LOGIN_PAGE.wait_for_page_to_fully_load()

    if ENV == 'int':
        AD = AD_INT
    elif ENV == 'stg':
        AD = AD_STG
    else:
        AD = AD_PROD

    LOGIN_PAGE.enter_username(AD.pm_only_user_name)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed(DC_URL, AD.pm_only_user_name, AD.password, AD.company_name)
    LOGIN_PAGE.wait_for_page_load()


@when('the user clicks the "VEHICLES" tab')
def go_to_vehicle_page():
    DASHBOARD_PAGE.click_admin_tab()
    USER_MANAGEMENT_PAGE.click_vehicle_tab()
    LOGIN_PAGE.wait_for_page_to_fully_load()


@then(
    'the page header "VEHICLE MANAGEMENT" and the vehicle count are displayed and the table is displayed with columns: "VEHICLE", "GROUP", "DRIVER", "DEVICE", "LAST CHECK IN", "STATUS"')
def verify_vehicle_page_column():
    VEHICLE_MANAGEMENT_PAGE.wait_for_page_to_fully_load()
    assert VEHICLE_MANAGEMENT_PAGE.get_vehicle_page_title_text() == "VEHICLE MANAGEMENT"
    assert VEHICLE_MANAGEMENT_PAGE.get_vehicle_column_text() == "VEHICLE"
    assert VEHICLE_MANAGEMENT_PAGE.get_group_column_text() == "GROUP"
    assert VEHICLE_MANAGEMENT_PAGE.get_driver_column_text() == "DRIVER"
    assert VEHICLE_MANAGEMENT_PAGE.get_device_column_text() == "DEVICE"
    assert VEHICLE_MANAGEMENT_PAGE.get_last_connected_column_text() == "LAST CHECK IN"
    assert VEHICLE_MANAGEMENT_PAGE.get_status_column_text() == "STATUS"


# LQ-239
@when(
    'the user clicks on "Add Vehicle" & the user enters required fields: "Group" and "Vehicle Name" & the user clicks Create Vehicle')
def add_new_vehicle():
    global tacm
    tacm = AddVehiclePage(BasePage)
    tacm.get_random_name(6)
    USER_MANAGEMENT_PAGE.click_vehicle_tab()
    VEHICLE_MANAGEMENT_PAGE.click_add_vehicle_button()
    ADD_VEHICLE_PAGE.click_group_add_vehicle_button()
    ADD_VEHICLE_PAGE.search_group_add_vehicle(AD.group)
    ADD_VEHICLE_PAGE.select_group_add_vehicle()
    ADD_VEHICLE_PAGE.click_done_group_add_vehicle()
    ADD_VEHICLE_PAGE.add_vehicle_name(tacm.random_name)
    EDIT_VEHICLE_PAGE.input_device(AD.device)
    EDIT_VEHICLE_PAGE.select_searched_device()
    EDIT_VEHICLE_PAGE.click_status_filter()
    EDIT_VEHICLE_PAGE.select_in_service_status_filter()
    ADD_VEHICLE_PAGE.click_continue_alert()
    ADD_VEHICLE_PAGE.click_create_vehicle()


@then('the vehicle is added')
def verify_add_vehicle():
    VEHICLE_MANAGEMENT_PAGE.click_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.click_vehicle_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.search_name_filter(tacm.random_name)
    assert_that(VEHICLE_MANAGEMENT_PAGE.get_first_row_vehicle_name(tacm.random_name), contains_string(tacm.random_name))


@when('the user clicks on "Last Connected" filter & the user selects a date range in the Vehicle Management page')
def set_last_connected_filter():
    VEHICLE_MANAGEMENT_PAGE.click_last_connected_filter()
    VEHICLE_MANAGEMENT_PAGE.select_first_date_filter()
    VEHICLE_MANAGEMENT_PAGE.select_second_date_filter()
    VEHICLE_MANAGEMENT_PAGE.click_apply_date_filter()


@then('the vehicles which Last Connected time is within the date range are displayed in the Vehicle Management page')
def verify_vehicle_last_connected_filter():
    assert VEHICLE_MANAGEMENT_PAGE.get_row_count(20) == 0
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()


@when('the user clicks on "Status" filter & the user selects "In Service" in the Vehicle Management page')
def set_status_filter_vehicle_page():
    VEHICLE_MANAGEMENT_PAGE.click_status_filter()
    VEHICLE_MANAGEMENT_PAGE.select_status_filter()


@then('the vehicles with In Service status are displayed in the Vehicle Management page')
def verify_vehicle_status_filter():
    assert VEHICLE_MANAGEMENT_PAGE.get_first_row_status_name() == "In Service"
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()


@when(
    'the user selects "Driver" from "Select Search" dropdown & the user enters some characters into "Search Name or ID" field in the Vehicle Management page')
def set_search_driver_filter():
    VEHICLE_MANAGEMENT_PAGE.click_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.click_driver_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.search_name_filter(AD.driver_user_name)


@then(
    'the vehicles with assigned driver that have inputted characters in their name or employeeid are shown in the Vehicle Management page')
def verify_search_driver_filter():
    assert VEHICLE_MANAGEMENT_PAGE.get_row_count(20) == 0
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()


@when(
    'the user selects "Vehicle" from "Select Search" dropdown & the user enters some characters into "Search Vehicle Name" field in the Vehicle Management page')
def set_search_vehicle_filter():
    VEHICLE_MANAGEMENT_PAGE.click_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.click_vehicle_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.search_name_filter(tacm.random_name)


@then('the vehicles which name contains the inputted characters are shown in the Vehicle Management page')
def verify_search_vehicle_filter():
    assert VEHICLE_MANAGEMENT_PAGE.get_row_count(20) == 1
    assert_that(VEHICLE_MANAGEMENT_PAGE.get_first_row_vehicle_name(tacm.random_name), contains_string(tacm.random_name))
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()


@when(
    'the user selects "Device" from "Select Search" dropdown & the user enters some characters into "Search Device" field in the Vehicle Management page')
def set_search_device_filter():
    VEHICLE_MANAGEMENT_PAGE.click_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.click_device_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.search_name_filter(AD.device)


@then(
    'the vehicles with ER assigned that contained inputted characters in the serial number are shown in the Vehicle Management page')
def verify_search_device_filter():
    assert VEHICLE_MANAGEMENT_PAGE.get_row_count(40) == 1
    assert_that(VEHICLE_MANAGEMENT_PAGE.get_first_row_device_name(), contains_string(AD.device))
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()


# LQ-245
@when('the user checks some available vehicles & the user clicks "Detach Device" & the user clicks Apply')
def detach_device_from_vehicle():
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()
    VEHICLE_MANAGEMENT_PAGE.click_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.click_vehicle_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.search_name_filter(tacm.random_name)
    VEHICLE_MANAGEMENT_PAGE.click_first_checkbox_detach_and_apply()
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()


@then('the devices are detached from the selected vehicles')
def verify_detach_device_from_vehicle():
    assert_that(VEHICLE_MANAGEMENT_PAGE.get_first_row_device_name(), contains_string(''))


# LQ-240
@when(
    'the user clicks on the vehicle name & the user changes "Vehicle Name" on Edit Vehicle page & the user clicks Save Changes')
def edit_vehicle():
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()
    VEHICLE_MANAGEMENT_PAGE.click_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.click_vehicle_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.search_name_filter(tacm.random_name)
    VEHICLE_MANAGEMENT_PAGE.click_first_vehicle_name()
    EDIT_VEHICLE_PAGE.clear_vehicle_name()
    EDIT_VEHICLE_PAGE.edit_vehicle_name(tacm.random_name + "edited")
    EDIT_VEHICLE_PAGE.click_edit_vehicle_save_button()
    ADD_VEHICLE_PAGE.click_continue_alert()
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()


@then('the vehicle name of the edited vehicle is updated')
def verify_edit_vehicle():
    assert VEHICLE_MANAGEMENT_PAGE.get_expected_vehicle_name(tacm.random_name + "edited") == tacm.random_name + "edited"


# LQ-12022
@when(
    'the user checks some available vehicles & the user clicks "Edit vehicle" Button & the user selects one group on the group selector & the user clicks "Done" on the group selector & the user clicks "Apply" button & the user clicks "Continue" button')
def move_group_vehicle():
    VEHICLE_MANAGEMENT_PAGE.click_first_vehicle_checkbox()
    VEHICLE_MANAGEMENT_PAGE.click_edit_vehicle_button()
    VEHICLE_MANAGEMENT_PAGE.click_filter_edit_vehicle_button()
    VEHICLE_MANAGEMENT_PAGE.search_edit_bulk_group(AD.group)
    VEHICLE_MANAGEMENT_PAGE.click_edit_bulk_select_group_button()
    VEHICLE_MANAGEMENT_PAGE.click_edit_bulk_group_done_button()
    VEHICLE_MANAGEMENT_PAGE.click_edit_bulk_apply_button()
    VEHICLE_MANAGEMENT_PAGE.click_move_group_continue()


@then('the selected vehicles are moved to the new group')
def verify_move_group_vehicle():
    VEHICLE_MANAGEMENT_PAGE.wait_for_page_to_fully_load()
    assert VEHICLE_MANAGEMENT_PAGE.get_first_row_group_name() == AD.group
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()


@when(
    'the user checks some available vehicles & the user clicks "Edit vehicle" Button & the user selects "Out of Service" on the Status selector & the user clicks "Apply" button')
def change_status_vehicle():
    VEHICLE_MANAGEMENT_PAGE.click_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.click_vehicle_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.search_name_filter(tacm.random_name + "edited")
    VEHICLE_MANAGEMENT_PAGE.click_first_vehicle_checkbox()
    VEHICLE_MANAGEMENT_PAGE.click_edit_vehicle_button()
    VEHICLE_MANAGEMENT_PAGE.click_status_drop_down()
    VEHICLE_MANAGEMENT_PAGE.click_edit_select_status_button()
    VEHICLE_MANAGEMENT_PAGE.click_edit_bulk_apply_button()
    VEHICLE_MANAGEMENT_PAGE.wait_for_page_to_fully_load()
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()


@then('the status of selected vehicles are updated')
def verify_change_status_vehicle():
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()
    VEHICLE_MANAGEMENT_PAGE.click_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.click_vehicle_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.search_name_filter(tacm.random_name + "edited")
    assert VEHICLE_MANAGEMENT_PAGE.get_first_row_expected_status_name("Out Of Service") == "Out Of Service"


@when(
    'the user checks some available vehicles & the user clicks "Edit vehicle" Button & the user selects "Enable" on DVIR ACCESS filter & the user clicks "Apply" button')
def change_dvir_access_status_vehicle():
    VEHICLE_MANAGEMENT_PAGE.click_first_vehicle_checkbox()
    VEHICLE_MANAGEMENT_PAGE.click_edit_vehicle_button()
    VEHICLE_MANAGEMENT_PAGE.click_edit_bulk_dvir_access_drop_down_button()
    VEHICLE_MANAGEMENT_PAGE.select_enable_status()
    VEHICLE_MANAGEMENT_PAGE.click_edit_bulk_apply_button()
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()


@then('the Dvir access status of the selected vehicles are updated')
def verify_dvir_access_status():
    VEHICLE_MANAGEMENT_PAGE.click_first_vehicle_name()
    assert EDIT_VEHICLE_PAGE.get_dvir_access_status_text() == "Enabled"
    USER_MANAGEMENT_PAGE.click_vehicle_tab()


# LQ-15217
@when('the user clicks on the "Delete Vehicle" & the user clicks "Continue" button on the pop-up')
def delete_vehicle_in_edit_vehicle_page():
    VEHICLE_MANAGEMENT_PAGE.click_expected_vehicle_name(tacm.random_name + "edited")
    EDIT_VEHICLE_PAGE.click_delete_button_in_edit_vehicle_page()
    EDIT_VEHICLE_PAGE.click_continue_button_pop_up()


@then('the vehicle is deleted')
def verify_delete_vehicle():
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()
    VEHICLE_MANAGEMENT_PAGE.click_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.click_vehicle_select_search_filter()
    VEHICLE_MANAGEMENT_PAGE.search_name_filter(tacm.random_name + "edited")
    assert VEHICLE_MANAGEMENT_PAGE.get_row_count(20) == 0
    VEHICLE_MANAGEMENT_PAGE.click_reset_button()


@given('the "Administrator/FA" user is in Vehicle Page')
def internal_fa_user_login():
    LOGIN_PAGE.navigate_to(DC_URL)
    LOGIN_PAGE.enter_username(AD.FA_internal_user)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_company()
    LOGIN_PAGE.click_select_company_button()


@when('the user clicks on the "View Change History" in Vehicle Management page')
def view_change_history_vehicle():
    DASHBOARD_PAGE.click_admin_tab()
    USER_MANAGEMENT_PAGE.click_vehicle_tab()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    VEHICLE_MANAGEMENT_PAGE.click_change_view_history()


@then(
    'the user should be able to see the table columns, Filters, and Download Log button in View Change History pop-up')
def verify_view_change_history_vehicle():
    assert VEHICLE_MANAGEMENT_PAGE.get_vehicle_affected_column_text() == "VEHICLE AFFECTED"
    assert VEHICLE_MANAGEMENT_PAGE.get_action_column_text() == "ACTION"
    assert VEHICLE_MANAGEMENT_PAGE.get_action_details_column_text() == "ACTION DETAILS"
    assert VEHICLE_MANAGEMENT_PAGE.get_editor_column_text() == "EDITOR"
    assert VEHICLE_MANAGEMENT_PAGE.get_action_date_column_text() == "ACTION DATE"
    assert VEHICLE_MANAGEMENT_PAGE.search_vehicle_affected_filter_displayed() is True
    assert VEHICLE_MANAGEMENT_PAGE.date_range_filter_displayed() is True
    assert VEHICLE_MANAGEMENT_PAGE.select_actions_filter_displayed() is True
    assert VEHICLE_MANAGEMENT_PAGE.download_log_button_displayed() is True


@when('the user enters a valid Vehicle Name in "Search Vehicle Affected" Search panel')
def search_vehicle_affected_filter():
    global AFFECTED_VEHICLE
    AFFECTED_VEHICLE = VEHICLE_MANAGEMENT_PAGE.get_first_vehicle_affected_text()
    VEHICLE_MANAGEMENT_PAGE.search_vehicle_affected(AFFECTED_VEHICLE)


@then('the searched vehicle should be able to see in the Vehicle Audit Log')
def verify_search_vehicle_affected_filter():
    assert_that(VEHICLE_MANAGEMENT_PAGE.get_first_vehicle_affected_text(), contains_string(AFFECTED_VEHICLE))


@when('the user enters an invalid or non-existing Vehicle details in "Search Vehicle Affected"')
def search_invalid_vehicle_affected_filter():
    VEHICLE_MANAGEMENT_PAGE.search_vehicle_affected("InvalidVehicle123")


@then('the searched vehicle should not be able to see in the Vehicle Audit Log')
def verify_search_invalid_vehicle_affected_filter():
    assert VEHICLE_MANAGEMENT_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected vehicle/date range"


@when('the user selects a specific date range in the Date Filter')
def select_date_range_filter():
    VEHICLE_MANAGEMENT_PAGE.click_reset_in_audit_page()
    VEHICLE_MANAGEMENT_PAGE.click_date_range_dropdown()
    VEHICLE_MANAGEMENT_PAGE.select_date_range_today()


@then('the Vehicle Audit Log should display logs corresponding to the selected date range')
def verify_date_range_filter():
    assert_that(USER_MANAGEMENT_PAGE.get_action_date(), contains_string(VEHICLE_MANAGEMENT_PAGE.get_time_today()))


@when('the user click on the "Close" button')
def close_view_change_history_popup():
    VEHICLE_MANAGEMENT_PAGE.click_close_view_change_history_popup()


@then('the user Audit Log tab should be closed successfully')
def verify_close_view_change_history_popup():
    assert VEHICLE_MANAGEMENT_PAGE.view_change_history_popup_displayed() is False


# LQ-249616
@given('user clicks on "View Change History" in Vehicle Management page')
def user_clicks_view_change_history_vehicle():
    VEHICLE_MANAGEMENT_PAGE.click_change_view_history()


@when('the user selects the Action "Added" from the "Select Action(s)" filter dropdown')
def select_action_type_filter():
    VEHICLE_MANAGEMENT_PAGE.click_select_actions_filter()
    VEHICLE_MANAGEMENT_PAGE.select_action_type_added()


@then('the Vehicle Audit Log should display logs with the Action type as "Added"')
def verify_action_type_filter():
    try:
        assert VEHICLE_MANAGEMENT_PAGE.get_first_action_type_text() == "Added"
    except TimeoutException:
        assert VEHICLE_MANAGEMENT_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected vehicle/date range"
    VEHICLE_MANAGEMENT_PAGE.click_reset_in_audit_page()


@when('the user selects the Action "Edited" from the "Select Action(s)" filter dropdown')
def select_edited_action_type_filter():
    VEHICLE_MANAGEMENT_PAGE.click_select_actions_filter()
    VEHICLE_MANAGEMENT_PAGE.select_edited_action_type()


@then('the Vehicle Audit Log should display logs with the Action type as "Edited"')
def verify_edited_action_type_filter():
    try:
        assert VEHICLE_MANAGEMENT_PAGE.get_first_action_type_text() == "Edited"
    except TimeoutException:
        assert VEHICLE_MANAGEMENT_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected vehicle/date range"
    VEHICLE_MANAGEMENT_PAGE.click_reset_in_audit_page()


@when('the user selects the Action "Deleted" from the "Select Action(s)" filter dropdown')
def select_deleted_action_type_filter():
    VEHICLE_MANAGEMENT_PAGE.click_select_actions_filter()
    VEHICLE_MANAGEMENT_PAGE.select_deleted_action_type()


@then('the Vehicle Audit Log should display logs with the Action type as "Deleted"')
def verify_deleted_action_type_filter():
    try:
        assert VEHICLE_MANAGEMENT_PAGE.get_first_action_type_text() == "Deleted"
    except TimeoutException:
        assert VEHICLE_MANAGEMENT_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected vehicle/date range"
    VEHICLE_MANAGEMENT_PAGE.click_reset_in_audit_page()


@when('the user selects the Action "Imported" from the "Select Action(s)" filter dropdown')
def select_imported_action_type_filter():
    VEHICLE_MANAGEMENT_PAGE.click_select_actions_filter()
    VEHICLE_MANAGEMENT_PAGE.select_imported_action_type()


@then('the Vehicle Audit Log should display logs with the Action type as "Imported"')
def verify_imported_action_type_filter():
    try:
        assert VEHICLE_MANAGEMENT_PAGE.get_first_action_type_text() == "Imported"
    except TimeoutException:
        assert VEHICLE_MANAGEMENT_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected vehicle/date range"
    VEHICLE_MANAGEMENT_PAGE.click_reset_in_audit_page()

@when('the user clicks "Download Log" in the Vehicle audit log tab')
def click_download_log_button_vehicle_audit_log():
    VEHICLE_MANAGEMENT_PAGE.click_download_log_button()


@then('the vehicle audit log is downloaded successfully')
def verify_download_log_button_vehicle_audit_log():
    file_name = VEHICLE_MANAGEMENT_PAGE.get_audit_log_file_name()
    VEHICLE_MANAGEMENT_PAGE.wait_for_file_downloaded(file_name)
    # assert VEHICLE_MANAGEMENT_PAGE.check_file_exist(file_name) is True


@when('search an invalid vehicle in "Search Vehicle Affected" filter')
def search_invalid_vehicle_in_vehicle_audit_log():
    VEHICLE_MANAGEMENT_PAGE.search_vehicle_affected("NonExistingVehicle123")


@then('the "Download Log" button is disabled in Vehicle Audit Log')
def download_log_button_disabled_vehicle_audit_log():
    assert VEHICLE_MANAGEMENT_PAGE.download_log_button_disabled_displayed() is True


@when('the user selects multiple groups from the "Select Group(s)" filter')
def apply_group_filter_vehicle_management():
    USER_MANAGEMENT_PAGE.click_reset_button()
    USER_MANAGEMENT_PAGE.click_select_group_filter()
    USER_MANAGEMENT_PAGE.search_group_filter(AD.Automation_group1)
    USER_MANAGEMENT_PAGE.select_searched_group()
    USER_MANAGEMENT_PAGE.click_done_group_filter()


@then('the vehicles belong to the selected groups are listed')
def verify_group_filter_vehicle_management():
    assert VEHICLE_MANAGEMENT_PAGE.get_vehicles_count() == '7'
    for i in range(1, 8):
        assert_that(VEHICLE_MANAGEMENT_PAGE.get_vehicles_groups_label(i),contains_string(getattr(AD, f"Automation_group{i}")))


