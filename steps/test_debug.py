from hamcrest import assert_that, contains_string
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then

from data.prod.home_data_prod import HomeDataProd as HD_PROD
from pages.add_user_page import *
from pages.behaviors_report_page import BehaviorsReportPage
from pages.dashboard_page import DashboardPage
from pages.device_management_page import DeviceManagementPage
from pages.driver_profile_page import DriverProfilePage
from pages.driver_vehicle_inspection_reports_page import DriverVehicleInspectionReportsPage
from pages.fleet_map_page import FleetMapPage
from pages.hos_page import HosPage
from pages.library_page import LibraryPage
from pages.login_page import LoginPage
from pages.open_tasks_report_page import OpenTasksReportPage
from pages.recognition_history_page import RecognitionHistoryPage
from pages.user_management_page import UserManagementPage
from steps.common import DC_URL, TestDataEnum

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
COACHING_PAGE = 0
LIBRARY_PAGE = 0
FLEET_PAGE = 0
FLEET_MAP_PAGE = 0
RISK_COMPANY_PAGE = 0
OPEN_TASKS_REPORT_PAGE = 0
BEHAVIORS_REPORT_PAGE = 0
BASE_PAGE = 0
FLEET_MAINT_PAGE = 0
RCD = 0
ID = 0
TD = 0
USER_MANAGEMENT_PAGE = 0
DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE = 0
INSPECTION_SCHEDULES_PAGE = 0
RECOGNITION_HISTORY_PAGE = 0
DEVICE_MANAGEMENT_PAGE = 0
INSPECTION_LIST_MANAGEMENT_PAGE = 0
ADD_USER_PAGE = 0
FLEET_INSIGHT_PAGE = 0
DRIVERS_REPORT_PAGE = 0
HOS_PAGE = 0
FID = 0
LD = 0
FLEET_INSIGHT_TEST_DATA = [TestDataEnum.DRIVER_VEHICLE_SUMMARY,
                           TestDataEnum.TRIP_DRIVER_PROFILE,
                           TestDataEnum.IDLE_DRIVER_PROFILE]
AD = 0
AUD = 0
VSD = 0
FMD = 0

scenarios('../features/debug.feature')


# LQ-306
@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, ADD_USER_PAGE, LIBRARY_PAGE, USER_MANAGEMENT_PAGE, DEVICE_MANAGEMENT_PAGE, OPEN_TASKS_REPORT_PAGE, HD, LD, ID, DRIVER_PROFILE_PAGE, BEHAVIORS_REPORT_PAGE, RECOGNITION_HISTORY_PAGE, FLEET_MAP_PAGE, DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE, HOS_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    LIBRARY_PAGE = LibraryPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)
    DEVICE_MANAGEMENT_PAGE = DeviceManagementPage(browser)
    ADD_USER_PAGE = AddUserPage(browser)
    BEHAVIORS_REPORT_PAGE = BehaviorsReportPage(browser)
    RECOGNITION_HISTORY_PAGE = RecognitionHistoryPage(browser)
    DRIVER_PROFILE_PAGE = DriverProfilePage(browser)
    OPEN_TASKS_REPORT_PAGE = OpenTasksReportPage(browser)
    FLEET_MAP_PAGE = FleetMapPage(browser)
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE = DriverVehicleInspectionReportsPage(browser)
    HOS_PAGE = HosPage(browser)

    browser.get(DC_URL)

    HD = HD_PROD


@when('the user enters username/password, clicks the login button in the page and select company from the list')
def login():
    LOGIN_PAGE.enter_username(HD.dycom_fa_user)
    LOGIN_PAGE.enter_password(HD.dycom_fa_password)
    LOGIN_PAGE.click_login()


@then('the user is successfully logged into the Driver Safety dashboard')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))


# LQ-387
@when('the user signs in to Driver Safety')
def login_to_safety():
    DASHBOARD_PAGE.click_home_tab()


@then('the Dashboard page is displayed & the Drivers count is displayed & the UNASSIGNED DRIVERS count'
      ' is displayed in last 90 days & the DUE FOR COACHING count is displayed in last 90 days '
      '& the FYI NOTIFY count is displayed in last 90 days $ the COLLISIONS count is displayed in'
      ' last 90 days & the POSSIBLE COLLISIONS count is displayed in last 90 days')
def verify_dashboard():
    assert DASHBOARD_PAGE.no_of_unassigned_drivers_is_displayed() is True
    assert DASHBOARD_PAGE.no_of_tasks_is_displayed() is True
    assert DASHBOARD_PAGE.no_of_drivers_is_displayed() is True
    assert DASHBOARD_PAGE.get_unassigned_drivers_text(), contains_string('UNASSIGNED DRIVER')
    assert DASHBOARD_PAGE.get_due_for_coaching_text() == "DUE FOR COACHING"
    assert DASHBOARD_PAGE.get_fyi_notify_text() == "FYI NOTIFY"
    assert_that(DASHBOARD_PAGE.get_collisions_text(), contains_string('COLLISION'))
    assert_that(DASHBOARD_PAGE.get_possible_collisions_text(), contains_string("POSSIBLE COLLISION"))


# LQ-390
@when('the user clicks link')
def click_links():
    DASHBOARD_PAGE.click_unassigned_drivers_link()


@then('the page is displayed')
def verify_links():
    assert DASHBOARD_PAGE.get_assigned_drivers_title() == "ASSIGN DRIVERS"
    DASHBOARD_PAGE.back_to_previous_page()


# LQ-383
@when('the user clicks "INSIGHTS" and the user clicks "OPEN TASKS REPORT" in Open Tasks Report page')
def open_tasks_filter():
    DASHBOARD_PAGE.click_insights_tab()
    DASHBOARD_PAGE.click_open_tasks_report_tab()


@then('the Event profile page is displayed in Open Tasks Report page')
def verify_table_data():
    assert OPEN_TASKS_REPORT_PAGE.get_driver_text() == "DRIVER"
    assert OPEN_TASKS_REPORT_PAGE.get_driver_group_text() == "DRIVER'S GROUP"
    assert OPEN_TASKS_REPORT_PAGE.get_f2f_text() == "FACE-TO-FACE"
    assert OPEN_TASKS_REPORT_PAGE.get_f2f_overdue_text() == "FACE-TO-FACE (OVERDUE)"


# LQ-392
@when('the user is in Driver Safety')
def login_to_dashboard():
    DASHBOARD_PAGE.click_home_tab()


@then('there is "Groups by Highest Score" in "METRICS" & the table are displayed with columns '
      '"GROUP", "COACHABLE SCORE", "COACHABLE SCORE TREND", "COACHABLE EVENTS", COACHABLE EVENTS TREND')
def verify_highest_score_metrics():
    assert DASHBOARD_PAGE.get_groups_by_highest_score_title() == "Groups by Highest Score"
    assert DASHBOARD_PAGE.get_group_title() == "GROUP"
    assert DASHBOARD_PAGE.get_coachable_score_title() == "COACHABLE SCORE"
    assert DASHBOARD_PAGE.get_group_widget_score_trend_title() == "TREND"
    assert DASHBOARD_PAGE.get_coachable_events_title() == "COACHABLE EVENTS"
    assert DASHBOARD_PAGE.get_group_widget_event_trend_title() == "TREND"


# LQ-398
@when('the user is in Dashboard page')
def sign_in_to_dashboard():
    DASHBOARD_PAGE.click_home_tab()


@then(
    'there is "Coaches by Lowest Effectiveness" in "METRICS" & the table are displayed with columns "COACH", "COACHING EFFECTIVENESS", "AVG DAYS TO COACH", "COACHED EVENTS", WITH NOTES')
def verify_coaches_by_lowest_effectiveness():
    assert DASHBOARD_PAGE.get_coachest_by_lowest_effectiveness_title() == "Coaches by Lowest Effectiveness"
    assert DASHBOARD_PAGE.get_coach_title() == "coach"
    assert DASHBOARD_PAGE.get_coaching_effectiveness_title() == "coaching effectiveness"
    assert DASHBOARD_PAGE.get_avg_days_to_coach_title() == "avg days to coach"
    assert DASHBOARD_PAGE.get_coached_events_title() == "coached events"
    assert DASHBOARD_PAGE.get_with_notes_title() == "with notes"


# LQ-404
@when('the user landed in Driver Safety')
def land_in_dashboard():
    DASHBOARD_PAGE.click_home_tab()


@then(
    'there is "Drivers by Highest Score" in "METRICS" & the table are displayed with columns "DRIVER", "COACHABLE SCORE", "TREND", IMPACT')
def verify_drivers_by_highest_score():
    assert DASHBOARD_PAGE.get_drivers_by_highest_score_title() == "Drivers by Highest Score"
    assert DASHBOARD_PAGE.get_driver_title() == "Driver"
    assert DASHBOARD_PAGE.get_driver_widget_coachable_score_title() == "Coachable Score"
    assert DASHBOARD_PAGE.get_driver_widget_trend_title() == "Trend"
    assert DASHBOARD_PAGE.get_impact_title() == "Impact"


# LQ-407
@when('the user is back to Driver Safety')
def user_in_dashboard():
    DASHBOARD_PAGE.click_home_tab()


@then(
    'there is "Behaviors by Highest Frequency" in "METRICS" & the table are displayed with columns "BEHAVIOR", "FREQ.", TREND')
def verify_behaviors_by_highest_frequency():
    assert DASHBOARD_PAGE.get_behaviors_by_highest_frequency_title() == "Behaviors by Highest Frequency"
    DASHBOARD_PAGE.click_behaviors_details_link()
    assert BEHAVIORS_REPORT_PAGE.get_behavior_text() == "BEHAVIOR"
    assert BEHAVIORS_REPORT_PAGE.get_frequency_text() == "FREQUENCY"
    assert BEHAVIORS_REPORT_PAGE.get_trend_text() == "TREND"
    DASHBOARD_PAGE.back_to_previous_page()


# LQ-391
@when('the user clicks "LIBRARY" and the user clicks "RECOGNITION HISTORY"')
def navigate_to_coaching_history():
    global LOGIN_PAGE, DASHBOARD_PAGE, LIBRARY_PAGE, LD, AUD
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_recognition_history()


@then(
    'all recognition history are displayed and the table is displayed with columns "TYPE","DRIVER","GROUP","EVENTID","ISSUED BY","ISSUED DATE","RECOGNITION REASON"')
def verify_coaching_history_displayed():
    assert LIBRARY_PAGE.get_type_column_name_text() == "TYPE"
    assert LIBRARY_PAGE.get_driver_column_name_text() == "DRIVER"
    assert LIBRARY_PAGE.get_group_column_name_text() == "GROUP"
    assert LIBRARY_PAGE.get_event_id_column_name_text() == "EVENT ID"
    assert LIBRARY_PAGE.get_issued_by_column_name_text() == "ISSUED BY"
    assert LIBRARY_PAGE.get_issued_date_column_name_text() == "ISSUED DATE"
    assert LIBRARY_PAGE.get_recognition_reason_column_name_text() == "RECOGNITION REASON"


# LQ-386
@when('the user clicks "LIBRARY" and the user clicks "DATA EXPORT"')
def click_data_export():
    DASHBOARD_PAGE.click_library_tab()
    LIBRARY_PAGE.click_data_export()


@then(
    'the requested records are displayed and the table is displayed with columns "REPORT TYPE", "GROUP", "DATE RANGE", "FILTERS", "REQUESTED DATE","ACTION" and a "New Export" button')
def verify_navigating_to_data_export():
    assert LIBRARY_PAGE.get_data_export_title_text() == "DATA EXPORT"
    assert LIBRARY_PAGE.get_report_type_text() == "REPORT TYPE"
    assert LIBRARY_PAGE.get_group_column_text() == "GROUP"
    assert LIBRARY_PAGE.get_date_range_column_text() == "DATE RANGE"
    assert LIBRARY_PAGE.get_filters_column_text() == "FILTERS"
    assert LIBRARY_PAGE.get_requested_date_column_text() == "REQUESTED DATE"
    assert LIBRARY_PAGE.get_action_column_text() == "ACTION"
    assert LIBRARY_PAGE.get_new_export_button_text() == "New Export"


# LQ-251
@when('the user clicks on Admin tab')
def navigate_to_user_management_page():
    DASHBOARD_PAGE.click_admin_tab()
    sleep(10)


@then('the page header "USER MANAGEMENT" is displayed and the user count are displayed and the table'
      ' is displayed with columns: "NAME", "EMPLOYEE ID", "LYTX BADGE", "PRIMARY DRIVER GROUP", '
      '"ROLES (GROUP)", "STATUS", "LOGIN", "USERNAME"')
def verify_user_management_tabs():
    assert USER_MANAGEMENT_PAGE.user_management_label_is_displayed() is True
    assert USER_MANAGEMENT_PAGE.get_user_management_label() == "USER MANAGEMENT"
    assert USER_MANAGEMENT_PAGE.get_name_label() == "NAME"
    assert USER_MANAGEMENT_PAGE.get_employee_id_label() == "EMPLOYEE ID"
    # assert USER_MANAGEMENT_PAGE.get_lytx_badge_label() == "LYTX BADGE"


# LQ-230
@when('the user clicks the "DEVICES" tab')
def navigate_to_device_management_page():
    USER_MANAGEMENT_PAGE.click_devices_tab()
    sleep(5)


@then('the page header "DEVICE MANAGEMENT" is displayed and the user count are displayed'
      ' and the table is displayed with columns: "DEVICE", "DEVICE TYPE", "VEHICLE", "GROUP", "LAST CONNECTED", '
      '"INITIAL CONNECTION"')
def verify_device_management_table():
    assert DEVICE_MANAGEMENT_PAGE.device_count_is_displayed() is True
    assert DEVICE_MANAGEMENT_PAGE.get_device_management_title() == "DEVICE MANAGEMENT"
    assert DEVICE_MANAGEMENT_PAGE.get_device_column_title() == "DEVICE"
    assert DEVICE_MANAGEMENT_PAGE.get_device_type_column_title() == "DEVICE TYPE"
    assert DEVICE_MANAGEMENT_PAGE.get_group_column_title() == "GROUP"
    assert DEVICE_MANAGEMENT_PAGE.get_status_column_title() == "STATUS"
    assert DEVICE_MANAGEMENT_PAGE.get_last_connected_column_title() == "LAST COMMUNICATED"
    assert DEVICE_MANAGEMENT_PAGE.get_initial_connection_column_title() == "INITIAL CONNECTION"


@when('user clicks on "FLEET TRACKING" on top navigation')
def navigate_to_fleet_tracking():
    DASHBOARD_PAGE.click_fleet_tracking_tab()


@then('user is navigated to "FLEET TRACKING" accordingly')
def verify_fleet_tracking():
    assert FLEET_MAP_PAGE.map_tab_is_displayed() is True


# LQ-15218
@when('the user clicks on Map')
def login():
    FLEET_MAP_PAGE.click_map()


# LQ-544
@when('the user navigates to Insights -> Fleet Operations')
def go_to_fleet_operations():
    FLEET_INSIGHT_PAGE.click_insights()
    FLEET_INSIGHT_PAGE.click_fleet_operations()


@then('the groups tab of Fleet Operations page is displayed')
def assert_fleet_operations_groups_tab():
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_title() == "FLEET OPERATIONS"
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_groups_tab() == "Groups"


# LQ-549
@when('the user clicks Drivers in Fleet Operations page')
def click_fleet_operations_drivers():
    FLEET_INSIGHT_PAGE.click_fleet_operations_drivers()
    sleep(2)


@then('the drivers tab of Fleet Operations page is displayed')
def assert_fleet_operations_drivers_tab():
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_drivers_tab() == "Drivers"


# LQ-558
@when('the user clicks a driver name')
def click_driver_name():
    FLEET_INSIGHT_PAGE.click_driver_name()


@then(
    'the driver name is displayed and the metadata bar is displayed with labels: "EMPLOYEE ID", "GROUP", "VEHICLE NAME", "EMAIL"')
def verify_driver_profile_metadata():
    assert FLEET_INSIGHT_PAGE.get_employee_id_text_driver_profile() == "EMPLOYEE ID"
    assert FLEET_INSIGHT_PAGE.get_group_text_driver_profile() == "GROUP"
    assert FLEET_INSIGHT_PAGE.get_vehicle_name_text_driver_profile() == "VEHICLE NAME"
    assert FLEET_INSIGHT_PAGE.get_email_text_driver_profile() == "EMAIL"


@when('the user clicks the expand icon on the summary section')
def click_expand_icon_driver_profile():
    FLEET_INSIGHT_PAGE.click_expand_icon_driver_profile()


@then('view type buttons are displayed: "Daily Avg", "Total"')
def assert_view_type():
    assert FLEET_INSIGHT_PAGE.get_daily_avg_text_driver_profile() == "Daily Avg"
    assert FLEET_INSIGHT_PAGE.get_total_text_driver_profile() == "Total"


@then(
    'the summary section is displayed with labels: "ROUTE TIME", "DISTANCE", "TRIPS", "STOPS", "STOP TIME", "DRIVING TIME", "ENGINE HOURS", "IDLE VIOLATIONS", "IDLE DURATION", "SPEED VIOLATIONS", "SPEEDING DURATION" on driver profile page')
def assert_summary_section_driver_profile():
    assert FLEET_INSIGHT_PAGE.get_route_time_text_driver_profile() == "ROUTE TIME"
    assert FLEET_INSIGHT_PAGE.get_distance_text_driver_profile() == "DISTANCE"
    assert FLEET_INSIGHT_PAGE.get_trips_text_driver_profile() == "TRIPS"
    assert FLEET_INSIGHT_PAGE.get_stops_text_driver_profile() == "STOPS"
    assert FLEET_INSIGHT_PAGE.get_stop_time_text_driver_profile() == "STOP TIME"
    assert FLEET_INSIGHT_PAGE.get_driving_time_text_driver_profile() == "DRIVING TIME"
    assert FLEET_INSIGHT_PAGE.get_engine_hours_text_driver_profile() == "ENGINE HOURS"
    assert FLEET_INSIGHT_PAGE.get_idle_violations_text_driver_profile() == "IDLE VIOLATIONS"
    assert FLEET_INSIGHT_PAGE.get_idle_duration_text_driver_profile() == "IDLE DURATION"
    assert FLEET_INSIGHT_PAGE.get_speed_violation_text_driver_profile() == "SPEED VIOLATIONS"
    assert FLEET_INSIGHT_PAGE.get_speeding_duration_text_driver_profile() == "SPEEDING DURATION"


@when('the user navigates to Maintenance -> Preventative Maintenance')
def go_to_fleet_maint_pm():
    FLEET_MAINT_PAGE.click_maintenance()
    FLEET_MAINT_PAGE.click_preventative_maintenance()


@then('the Preventative Main labels are shown - Upcoming Services, History & Manage Services')
def assert_preventative_maintenance():
    assert FLEET_MAINT_PAGE.get_preventative_maintenance_title() == "PREVENTATIVE MAINTENANCE"
    assert FLEET_MAINT_PAGE.get_upcoming_services_tab_title() == "Upcoming Services"
    assert FLEET_MAINT_PAGE.get_history_tab_title() == "History"
    assert FLEET_MAINT_PAGE.get_manage_services_title() == "Manage Services"


# LQ-527
@when('the user clicks "Manage Services"')
def click_manage_services_tab():
    FLEET_MAINT_PAGE.click_manage_services()
    # sleep 2s to load services
    sleep(3)


@then('the Manage Services page is displayed')
def assert_manage_services_page():
    assert str(FLEET_MAINT_PAGE.get_row_count()) == FLEET_MAINT_PAGE.get_manage_service_services_count()


@when('the user clicks DVIR')
def go_to_DVIR_page():
    DASHBOARD_PAGE.click_dvir_tab()


@then(
    'Total reports count, reset button, group filter, date filter, status filter, defect filter and wild search filter are shown on "DRIVER VEHICLE INSPECTION REPORTS" page and table columns are: "REPORT ID", "TYPE", "STATUS", "REPORT DATE", "DURATION", "DRIVER", "VEHICLE", "MAJOR VEHICLE DEFECTS", "MINOR VEHICLE DEFECTS", "VEHICLE INSPECTION LIST", "TRAILER", "MAJOR TRAILER DEFECTS", "MINOR TRAILER DEFECTS", "TRAILER INSPECTION LIST", "MECHANIC/AGENT", "REVIEWER"')
def verify_driver_vehicle_inspection_report_page():
    sleep(2)
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_total_report_title() == "Reports"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_groups_filter_title() == "Select Group(s)"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_date_range_filter_title() == "Select Date Range"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_defects_filter_title() == "Defects"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_search_filter_title() == "Select Search"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_reset_button_title() == "Reset"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_report_Id_title() == "REPORT ID"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_type_title() == "TYPE"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_status_title() == "STATUS"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_report_date_title() == "REPORT DATE"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_duration_title() == "DURATION"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_driver_title() == "DRIVER"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_vehicle_title() == "VEHICLE"


@when('the user clicks HOS tab')
def go_to_Hos_page():
    DASHBOARD_PAGE.click_hos_tab()


@then('the HOS main page is loaded successfully')
def verify_user_on_hos_page():
    HOS_PAGE.switch_hos_iframe()
    assert HOS_PAGE.username_is_displayed() is True
    assert HOS_PAGE.company_is_displayed() is True