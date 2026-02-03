from pytest_bdd import scenarios, given, when, then
from pages.dashboard_page import DashboardPage
from pages.device_health_page import DeviceHealthPage
from pages.device_profile_page import DeviceProfilePage
from pages.driver_id_assignment_page import DriverIdAssignmentPage
from pages.driver_id_page import DriverIdPage
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage
from steps.common import DC_URL, ENV
from data.int.admin_data_int import AdminDataInt as AD_INT
from data.prod.admin_data_prod import AdminDataProd as AD_PROD
from data.stg.admin_data_stg import AdminDataStg as AD_STG

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
USER_MANAGEMENT_PAGE = 0
DEVICE_HEALTH_PAGE = 0
DRIVER_ID_ASSIGNMENT_PAGE = 0
DRIVER_ID_PAGE = 0
DEVICE_PROFILE_PAGE = 0
AD = 0

scenarios('../features/admin_insights.feature')


# LQ-235
@given('fa user logs in')
def fa_log_in(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, DEVICE_HEALTH_PAGE, DRIVER_ID_ASSIGNMENT_PAGE, USER_MANAGEMENT_PAGE, DRIVER_ID_PAGE, DEVICE_PROFILE_PAGE, AD

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)
    DRIVER_ID_ASSIGNMENT_PAGE = DriverIdAssignmentPage(browser)
    DEVICE_HEALTH_PAGE = DeviceHealthPage(browser)
    DRIVER_ID_PAGE = DriverIdPage(browser)
    DEVICE_PROFILE_PAGE = DeviceProfilePage(browser)

    browser.get(DC_URL)

    if ENV == 'int':
        AD = AD_INT
    elif ENV == 'stg':
        AD = AD_STG
    else:
        AD = AD_PROD

    LOGIN_PAGE.enter_username(AD.pm_fa_user_name)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed(DC_URL, AD.pm_fa_user_name, AD.password, AD.company_name)


@when('the user clicks "INSIGHTS" & the user clicks "DRIVER ID ASSIGNMENT"')
def navigate_to_driver_id_assignment_page():
    DASHBOARD_PAGE.click_admin_tab()
    USER_MANAGEMENT_PAGE.click_insights_tab()
    USER_MANAGEMENT_PAGE.click_driver_id_assignment_tab()


@then(
    'the trip count is displayed and the table section is displayed with columns: "Vehicle","Group","Driver","Employee ID","Driver ID Source", "Trip Start","Trip End","Duration" & the summary section is displayed with: "ASSIGNED TRIPS", "ASSIGNED BY LYTX BADGE", "ASSIGNED BY VEHICLE", "UNASSIGNED TRIPS" & the graph section is displayed')
def verify_driver_id_assignment_info():
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_trip_count() == "0"
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_row_count(10) == 0
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_vehicle_column_label() == "VEHICLE"
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_group_column_label() == "GROUP"
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_driver_column_label() == "DRIVER"
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_employee_id_label() == "EMPLOYEE ID"
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_driver_id_source_column_label() == "DRIVER ID SOURCE"
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_trip_start_column_label() == "TRIP START"
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_trip_end_column_label() == "TRIP END"
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_duration_column_label() == "DURATION"
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_assigned_trips_summary_label() == "ASSIGNED TRIPS"
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_assigned_by_lytx_badge_summary_label() == "ASSIGNED BY LYTX BADGE"
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_assigned_by_vehicle_summary_label() == "ASSIGNED BY VEHICLE"
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_unassigned_trips_summary_label() == "UNASSIGNED TRIPS"
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_percent_of_all_assigned_trips_graph_label() == "% of All Assigned Trips"


# LQ-228
@when('the user clicks "INSIGHTS" & the user clicks "DEVICE HEALTH"')
def go_to_device_health_page():
    USER_MANAGEMENT_PAGE.click_insights_tab()
    USER_MANAGEMENT_PAGE.click_device_health_tab()


@then(
    'the device count is displayed and the table is displayed with columns: "DEVICE","DEVICE TYPE","VEHICLE","GROUP","OVERDUE FOR CHECK-IN","POWER DISCONNECTS","IGNITION NOT DETECTED","OPEN RMA" & the summary section is displayed with issues: "ALL DEVICE ISSUES", "OVERDUE FOR CHECK-IN", "POWER DISCONNECTS", "IGNITION NOT DETECTED", "OPEN RMA" & the graph section is displayed')
def verify_device_health_info():
    assert DEVICE_HEALTH_PAGE.get_device_count(80) == AD.device_health_count
    assert DEVICE_HEALTH_PAGE.get_row_count(20) == AD.device_health_total_row_count
    assert DEVICE_HEALTH_PAGE.get_device_column_label() == "DEVICE"
    assert DEVICE_HEALTH_PAGE.get_device_type_column_label() == "DEVICE TYPE"
    assert DEVICE_HEALTH_PAGE.get_overdue_for_check_in_column_label() == "OVERDUE FOR CHECK-IN"
    assert DEVICE_HEALTH_PAGE.get_power_disconnects_column_label() == "POWER DISCONNECTS"
    assert DEVICE_HEALTH_PAGE.get_ignition_not_detected_column_label() == "IGNITION NOT DETECTED"
    assert DEVICE_HEALTH_PAGE.get_open_rma_column_label() == "OPEN RMA"
    assert DEVICE_HEALTH_PAGE.get_all_device_issues_summary_label() == "ALL DEVICE ISSUES"
    assert DEVICE_HEALTH_PAGE.get_overdue_for_check_in_summary_label() == "OVERDUE FOR CHECK-IN"
    assert DEVICE_HEALTH_PAGE.get_power_disconnects_summary_label() == "POWER DISCONNECTS"
    assert DEVICE_HEALTH_PAGE.get_ignition_not_detected_summary_label() == "IGNITION NOT DETECTED"
    assert DEVICE_HEALTH_PAGE.get_open_rma_summary_label() == "OPEN RMA"
    assert DEVICE_HEALTH_PAGE.get_all_device_issues_graph_label() == "All Device Issues"


# LQ-238
@given('the "Program Manager" user is in driver id assignment page')
def navigate_to_driver_assignment_page():
    USER_MANAGEMENT_PAGE.click_insights_tab()
    USER_MANAGEMENT_PAGE.click_driver_id_assignment_tab()


@when('the user sets group filter to one group in driver id assignment page')
def set_group_filter_driver_id_assignment():
    DRIVER_ID_ASSIGNMENT_PAGE.click_group_filter_button()
    DRIVER_ID_ASSIGNMENT_PAGE.search_group_filter(AD.group)
    DRIVER_ID_ASSIGNMENT_PAGE.select_search_group_filter_button()
    DRIVER_ID_ASSIGNMENT_PAGE.click_done_group_filter_button()


@then('the data belong to the group are listed in driver id assignment page')
def verify_group_filter_driver_id_assignment():
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_row_count(10) == 0
    DRIVER_ID_ASSIGNMENT_PAGE.click_reset_button()


@given('the "Program Manager" user opens the date range filter on the Driver Id assignment page')
def set_date_filter_driver_id():
    DRIVER_ID_ASSIGNMENT_PAGE.click_date_filter_button()


@when('the user selects date & the user clicks Apply in driver id assignment page')
def apply_date_filter_driver_id_assignment():
    DRIVER_ID_ASSIGNMENT_PAGE.select_first_date_filter_button()
    DRIVER_ID_ASSIGNMENT_PAGE.select_second_date_filter_button()
    DRIVER_ID_ASSIGNMENT_PAGE.click_date_filter_done_button()


@then('the data belong to the date range are listed in driver id assignment page')
def verify_date_filter_driver_id_assignment():
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_row_count(10) == 0
    DRIVER_ID_ASSIGNMENT_PAGE.click_reset_button()


@given(
    'the "Program Manager" user clicks on "Select Search" filter & the user selects Driver in driver id assignment page')
def set_driver_search_driver_id():
    DRIVER_ID_ASSIGNMENT_PAGE.click_search_filter_button()
    DRIVER_ID_ASSIGNMENT_PAGE.click_search_driver_filter_button()


@when(
    'the user enters driver name into "Search Name or ID" field & the user selects one name from suggestion list in driver id assignment page')
def apply_driver_search_driver_id_assignment():
    DRIVER_ID_ASSIGNMENT_PAGE.search_criteria_filter(AD.driver_user_name)
    DRIVER_ID_ASSIGNMENT_PAGE.click_searched_name_button_xpath()


@then('the data belong to the driver name are listed in driver id assignment page')
def verify_search_driver_driver_id_assignment():
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_row_count(10) == 0
    DRIVER_ID_ASSIGNMENT_PAGE.click_reset_button()


@given(
    'the "Program Manager" user clicks on "Select Search" filter & the user selects "Vehicle" in driver id assignment page')
def set_vehicle_search_driver_id():
    DRIVER_ID_ASSIGNMENT_PAGE.click_search_filter_button()
    DRIVER_ID_ASSIGNMENT_PAGE.click_search_vehicle_filter_button()


@when(
    'the user enters vehicle name into "Search Vehicle Name" field & the user selects one vehicle name from suggestion list in driver id assignment page')
def apply_vehicle_search_driver_id_assignment():
    DRIVER_ID_ASSIGNMENT_PAGE.search_criteria_filter(AD.vehicle)
    DRIVER_ID_ASSIGNMENT_PAGE.click_searched_name_button_xpath()


@then('the data belong to the vehicle name are listed in driver id assignment page')
def verify_search_vehicle_driver_id_assignment():
    assert DRIVER_ID_ASSIGNMENT_PAGE.get_row_count(10) == 0
    DRIVER_ID_ASSIGNMENT_PAGE.click_reset_button()


# LQ-229
@given('the "Program Manager" user is in the Device Health page')
def navigate_to_device_health_page():
    USER_MANAGEMENT_PAGE.click_insights_tab()
    USER_MANAGEMENT_PAGE.click_device_health_tab()


@when('the user sets group filter to one group in the Device Health page')
def set_group_filter_device_health():
    DEVICE_HEALTH_PAGE.click_group_filter_button()
    DEVICE_HEALTH_PAGE.search_group_filter(AD.group)
    DEVICE_HEALTH_PAGE.select_searched_group_filter_button()
    DEVICE_HEALTH_PAGE.click_done_group_filter_button()


@then('the data belong to the group are listed in the Device Health page')
def verify_group_filter_device_health():
    assert DEVICE_HEALTH_PAGE.get_row_count(30) == 0
    DEVICE_HEALTH_PAGE.click_reset_button()


@when('the user clicks on "Select Issue" filter & the user selects Overdue for Check-in')
def select_over_due_for_check_in_issue():
    DEVICE_HEALTH_PAGE.get_device_count(50)
    DEVICE_HEALTH_PAGE.click_select_issue_filter_button()
    DEVICE_HEALTH_PAGE.select_overdue_filter_button()
    DEVICE_HEALTH_PAGE.get_device_count(20)


@then('the data belong to the Overdue for Check-in issue are listed in the Device Health page')
def verify_over_due_for_check_in_issue():
    assert DEVICE_HEALTH_PAGE.get_overdue_for_check_in_graph_text() == "Overdue for Check-in"
    DEVICE_HEALTH_PAGE.click_reset_button()


@when('the user clicks on "Select Issue" filter & the user selects Power Disconnects')
def select_power_disconnects_issue():
    DEVICE_HEALTH_PAGE.get_device_count(50)
    DEVICE_HEALTH_PAGE.click_select_issue_filter_button()
    DEVICE_HEALTH_PAGE.select_power_disconnect_filter_button()
    DEVICE_HEALTH_PAGE.get_device_count(20)


@then(
    'the data belong to the Power Disconnects issue are listed in the Device Health page and the table is displayed with columns: "DEVICE", "DEVICE TYPE", "VEHICLE", "GROUP", "DISCONNECT TIME", "RECONNECT TIME","DURATION"')
def verify_power_disconnects_issue():
    assert DEVICE_HEALTH_PAGE.get_power_disconnects_graph_text() == "Power Disconnects"
    assert DEVICE_HEALTH_PAGE.get_device_column_text() == "DEVICE"
    assert DEVICE_HEALTH_PAGE.get_device_type_column_text() == "DEVICE TYPE"
    assert DEVICE_HEALTH_PAGE.get_vehicle_column_text() == "VEHICLE"
    assert DEVICE_HEALTH_PAGE.get_group_column_text() == "GROUP"
    assert DEVICE_HEALTH_PAGE.get_disconnect_time_column_text() == "DISCONNECT TIME"
    assert DEVICE_HEALTH_PAGE.get_reconnect_time_column_text() == "RECONNECT TIME"
    assert DEVICE_HEALTH_PAGE.get_duration_column_text() == "DURATION"
    DEVICE_HEALTH_PAGE.click_reset_button()


@when(
    'the user clicks on "Select Search" filter & the user selects "Device" & the user enters some characters into "Search Device" field in the Device Health page')
def search_device_filter_device_health():
    DEVICE_HEALTH_PAGE.click_select_search_filter_button()
    DEVICE_HEALTH_PAGE.select_device_search_filter_button()
    DEVICE_HEALTH_PAGE.search_criteria_filter(AD.device)
    DEVICE_HEALTH_PAGE.get_device_count(30)


@then('the data that contained inputted characters in the serial number are shown in the Device Health page')
def verify_device_search_device_health():
    assert DEVICE_HEALTH_PAGE.get_device_count(50) == AD.device_health_count_filtered
    assert DEVICE_HEALTH_PAGE.get_row_count(20) == AD.device_health_row_count_filtered
    DEVICE_HEALTH_PAGE.click_reset_button()


@when(
    'the user clicks on "Select Search" filter & the user selects "Vehicle" & the user enters some characters into "Search Vehicle" field in the Device Health page')
def search_vehicle_filter_device_health():
    DEVICE_HEALTH_PAGE.click_select_search_filter_button()
    DEVICE_HEALTH_PAGE.select_vehicle_search_filter_button()
    DEVICE_HEALTH_PAGE.search_criteria_filter(AD.vehicle)
    DEVICE_HEALTH_PAGE.get_device_count(30)


@then('the data that contained inputted characters in the Vehicle name are shown in the Device Health page')
def verify_vehicle_search_device_health():
    assert DEVICE_HEALTH_PAGE.get_device_count(50) == AD.device_health_count_filtered
    assert DEVICE_HEALTH_PAGE.get_row_count(20) == AD.device_health_row_count_filtered
    DEVICE_HEALTH_PAGE.click_reset_button()
