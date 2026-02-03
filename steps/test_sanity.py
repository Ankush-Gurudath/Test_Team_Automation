from hamcrest import assert_that, contains_string
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then
from data.int.DVIR_data_int import DvirDataInt as DD_INT
from data.int.fleet_insights_data_int import FleetInsightsDataInt as FID_INT
from data.int.fleet_map_data_int import FleetMapDataInt as FMD_INT
from data.int.home_data_int import HomeDataInt as HD_INT
from data.int.home_data_int import HomeDataInt as LD_INT
from data.int.risk_company_data_int import RiskCompanyDataInt as RCD_INT
from data.int.video_search_data_int import VideoSearchDataInt as VSD_INT
from data.int.ws_insights_data_int import InsightsDataInt as ID_INT
from data.int.ws_tasks_data_int import TaskDataInt as TD_INT
from data.prod.DVIR_data_prod import DvirDataProd as DD_PROD
from data.prod.fleet_insights_data_prod import FleetInsightsDataProd as FID_PROD
from data.prod.fleet_map_data_prod import FleetMapDataProd as FMD_PROD
from data.prod.home_data_prod import HomeDataProd as HD_PROD
from data.prod.home_data_prod import HomeDataProd as LD_PROD
from data.prod.risk_company_data_prod import RiskCompanyDataProd as RCD_PROD
from data.prod.video_search_data_prod import VideoSearchDataProd as VSD_PROD
from data.prod.ws_insights_data_prod import InsightsDataProd as ID_PROD
from data.prod.ws_tasks_data_prod import TaskDataProd as TD_PROD
from data.stg.DVIR_data_stg import DvirDataStg as DD_STG
from data.stg.fleet_insights_data_stg import FleetInsightsDataStg as FID_STG
from data.stg.fleet_map_data_stg import FleetMapDataStg as FMD_STG
from data.stg.home_data_stg import HomeDataStg as HD_STG
from data.stg.home_data_stg import HomeDataStg as LD_STG
from data.stg.risk_company_data_stg import RiskCompanyDataStg as RCD_STG
from data.stg.video_search_data_stg import VideoSearchDataStg as VSD_STG
from data.stg.ws_insights_data_stg import InsightsDataStg as ID_STG
from data.stg.ws_tasks_data_stg import TaskDataStg as TD_STG
from pages.add_user_page import *
from pages.behaviors_report_page import BehaviorsReportPage
from pages.dashboard_page import DashboardPage
from pages.device_management_page import DeviceManagementPage
from pages.driver_profile_page import DriverProfilePage
from pages.driver_vehicle_inspection_reports_page import DriverVehicleInspectionReportsPage
from pages.fleet_insights_page import FleetInsightsPage
from pages.fleet_maint_page import FleetMaintPage
from pages.fleet_map_page import FleetMapPage
from pages.inspection_list_management_page import InspectionListManagementPage
from pages.inspection_schedules_page import InspectionSchedulesPage
from pages.library_page import LibraryPage
from pages.login_page import LoginPage
from pages.open_tasks_report_page import OpenTasksReportPage
from pages.recognition_history_page import RecognitionHistoryPage
from pages.risk_company import RiskCompanyPage
from pages.user_management_page import UserManagementPage
from pages.video_search_page import VideoSearchPage
from steps.common import DC_URL, ENV, TestDataEnum, WELCOME_URL, NEW_UI_FTM_URL
from steps.common import FLEET_URL

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
COACHING_PAGE = 0
LIBRARY_PAGE = 0
RISK_COMPANY_PAGE = 0
OPEN_TASKS_REPORT_PAGE = 0
BEHAVIORS_REPORT_PAGE = 0
BASE_PAGE = 0
FLEET_MAINT_PAGE = 0
RCD = 0
ID = 0
TD = 0
USER_MANAGEMENT_PAGE = 0
INSPECTION_SCHEDULES_PAGE = 0
RECOGNITION_HISTORY_PAGE = 0
DEVICE_MANAGEMENT_PAGE = 0
INSPECTION_LIST_MANAGEMENT_PAGE = 0
ADD_USER_PAGE = 0
FLEET_INSIGHT_PAGE = 0
DRIVERS_REPORT_PAGE = 0
FID = 0
LD = 0
FLEET_INSIGHT_TEST_DATA = [TestDataEnum.DRIVER_VEHICLE_SUMMARY,
                           TestDataEnum.TRIP_DRIVER_PROFILE,
                           TestDataEnum.IDLE_DRIVER_PROFILE]
AD = 0
AUD = 0
VSD = 0
FMD = 0

scenarios('../features/sanity.feature')


# LQ-306
@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, ADD_USER_PAGE, LIBRARY_PAGE, USER_MANAGEMENT_PAGE, DEVICE_MANAGEMENT_PAGE, OPEN_TASKS_REPORT_PAGE, HD, LD, ID, DRIVER_PROFILE_PAGE, BEHAVIORS_REPORT_PAGE, RECOGNITION_HISTORY_PAGE, ENV

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

    if ENV == 'int':
        HD = HD_INT
    elif ENV == 'stg':
        HD = HD_STG
    elif ENV == 'prod':
        HD = HD_PROD
    else:
        raise ValueError(f"Unsupported ENV value: {ENV!r}. Must be one of 'int', 'stg', or 'prod'.")
    browser.get(NEW_UI_FTM_URL)


@when(
    'the user with multi company account enters username/password, clicks the login button in the page and select company from the list')
def login():
    LOGIN_PAGE.enter_username(HD.multi_company_user_name)
    LOGIN_PAGE.enter_password(HD.password_multi_company)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_multi_company(HD.company_name_env1)
    LOGIN_PAGE.click_select_company_button()
    LOGIN_PAGE.wait_for_page_to_fully_load()


@then('the user is successfully logged into the Driver Safety dashboard')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_admin_sign_out()


@when(
    'the user enters username/password for env1, clicks the login button in the page')
def login():
    LOGIN_PAGE.enter_username(HD.username_env1)
    LOGIN_PAGE.enter_password(HD.password_env1)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_multi_company(HD.company_name_env1)
    LOGIN_PAGE.click_select_company_button()


@then('there is "Groups by Highest Score" in "METRICS" & the table are displayed with columns '
      '"GROUP", "COACHABLE SCORE", "COACHABLE SCORE TREND", "COACHABLE EVENTS", COACHABLE EVENTS TREND')
def verify_highest_score_metrics():
    DASHBOARD_PAGE.close_pendo_dialog()
    assert DASHBOARD_PAGE.get_groups_by_highest_score_title() == "Groups by Highest Score"
    assert DASHBOARD_PAGE.get_group_title() == "GROUP"
    assert DASHBOARD_PAGE.get_coachable_score_title() == "COACHABLE SCORE"
    assert DASHBOARD_PAGE.get_group_widget_score_trend_title() == "TREND"
    assert DASHBOARD_PAGE.get_coachable_events_title() == "COACHABLE EVENTS"
    assert DASHBOARD_PAGE.get_group_widget_event_trend_title() == "TREND"


@then(
    'there is "Coaches by Lowest Effectiveness" in "METRICS" & the table are displayed with columns "COACH", "COACHING EFFECTIVENESS", "AVG DAYS TO COACH", "COACHED EVENTS", WITH NOTES')
def verify_coaches_by_lowest_effectiveness():
    assert_that(DASHBOARD_PAGE.get_coachest_by_lowest_effectiveness_title(), IsEqualIgnoringCase(
        "Coaches by Lowest Effectiveness"))
    assert DASHBOARD_PAGE.get_coach_title() == "coach"
    assert_that(DASHBOARD_PAGE.get_coaching_effectiveness_title(), IsEqualIgnoringCase("coaching effectiveness"))
    assert DASHBOARD_PAGE.get_avg_days_to_coach_title() == "avg days to coach"
    assert DASHBOARD_PAGE.get_coached_events_title() == "coached events"
    assert DASHBOARD_PAGE.get_with_notes_title() == "with notes"


@then('the user is successfully logged into the dashboard 1')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))


@when('the user enters a newly created username/password and clicks the login button in the page')
def login():
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_admin_sign_out()
    LOGIN_PAGE.enter_username(HD.coach_user_name)
    LOGIN_PAGE.enter_password(HD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()


@then('the user is successfully logged into the Driver Safety dashboard in the same company')
def verify_login():
    DASHBOARD_PAGE.close_pendo_dialog()
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))


# LQ-387
@when('the user signs in to Driver Safety')
def login_to_safety():
    DASHBOARD_PAGE.click_home_tab_new_ui()


@then('the Dashboard page is displayed & the Drivers count is displayed & the UNASSIGNED DRIVERS count'
      ' is displayed in last 90 days & the DUE FOR COACHING count is displayed in last 90 days '
      '& the FYI NOTIFY count is displayed in last 90 days $ the COLLISIONS count is displayed in'
      ' last 90 days & the POSSIBLE COLLISIONS count is displayed in last 90 days')
def verify_dashboard():
    # assert DASHBOARD_PAGE.get_noof_drivers_text() == HD.no_of_drivers
    #  assert DASHBOARD_PAGE.get_unassigned_drivers_text() == "UNASSIGNED DRIVER"
    assert DASHBOARD_PAGE.get_due_for_coaching_text() == "DUE FOR COACHING"
    assert DASHBOARD_PAGE.get_fyi_notify_text() == "FYI NOTIFY"
    assert DASHBOARD_PAGE.get_collisions_text() == "COLLISIONS"
    assert DASHBOARD_PAGE.get_possible_collisions_text() == "POSSIBLE COLLISIONS"


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
    if DC_URL == 'https://dc-int.drivecaminc.xyz/':
        ID = ID_INT
    elif DC_URL == 'https://dc-stg.drivecam.com/':
        ID = ID_STG
    else:
        ID = ID_PROD
    DASHBOARD_PAGE.click_insights_tab_new_ui()
    DASHBOARD_PAGE.click_open_tasks_report_tab_new_ui()
    OPEN_TASKS_REPORT_PAGE.click_filter_by_group()
    OPEN_TASKS_REPORT_PAGE.enter_group('Vehicle Needs Attention')
    OPEN_TASKS_REPORT_PAGE.click_select_group()
    OPEN_TASKS_REPORT_PAGE.click_done()


@then('the Event profile page is displayed in Open Tasks Report page')
def verify_table_data():
    assert OPEN_TASKS_REPORT_PAGE.get_driver_text() == "DRIVER"
    assert OPEN_TASKS_REPORT_PAGE.get_driver_group_text() == "DRIVER'S GROUP"
    assert OPEN_TASKS_REPORT_PAGE.get_f2f_text() == "FACE-TO-FACE"
    assert OPEN_TASKS_REPORT_PAGE.get_f2f_overdue_text() == "FACE-TO-FACE (OVERDUE)"
    assert OPEN_TASKS_REPORT_PAGE.get_fyi_notify_text() == "FYI NOTIFY"


# LQ-392
@when('the user is in Driver Safety')
def login_to_dashboard():
    DASHBOARD_PAGE.click_home_tab_new_ui()


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
    DASHBOARD_PAGE.click_home_tab_new_ui()


@then(
    'there is "Coaches by Lowest Effectiveness" in "METRICS" & the table are displayed with columns "COACH", "COACHING EFFECTIVENESS", "AVG DAYS TO COACH", "COACHED EVENTS", WITH NOTES')
def verify_coaches_by_lowest_effectiveness():
    assert_that(DASHBOARD_PAGE.get_coachest_by_lowest_effectiveness_title(), IsEqualIgnoringCase(
        "Coaches by Lowest Effectiveness"))
    assert DASHBOARD_PAGE.get_coach_title() == "coach"
    assert_that(DASHBOARD_PAGE.get_coaching_effectiveness_title(), IsEqualIgnoringCase("coaching effectiveness"))
    assert DASHBOARD_PAGE.get_avg_days_to_coach_title() == "avg days to coach"
    assert DASHBOARD_PAGE.get_coached_events_title() == "coached events"
    assert DASHBOARD_PAGE.get_with_notes_title() == "with notes"


# LQ-404
@when('the user landed in Driver Safety')
def land_in_dashboard():
    DASHBOARD_PAGE.click_home_tab_new_ui()


@then(
    'there is "Drivers by Highest Score" in "METRICS" & the table are displayed with columns "DRIVER", "COACHABLE SCORE", "TREND", IMPACT')
def verify_drivers_by_highest_score():
    assert DASHBOARD_PAGE.get_drivers_by_highest_score_title() == "Drivers by Highest Score"
    if DASHBOARD_PAGE.no_driver_data_displayed() is False:
        assert DASHBOARD_PAGE.get_driver_title() == "Driver"
        assert DASHBOARD_PAGE.get_driver_widget_coachable_score_title() == "Coachable Score"
        assert DASHBOARD_PAGE.get_driver_widget_trend_title() == "Trend"
        assert DASHBOARD_PAGE.get_impact_title() == "Impact"


# LQ-407
@when('the user is back to Driver Safety')
def user_in_dashboard():
    DASHBOARD_PAGE.click_home_tab_new_ui()


@then(
    'there is "Behaviors by Highest Frequency" in "METRICS" & the table are displayed with columns "BEHAVIOR", "FREQ.", TREND')
def verify_behaviors_by_highest_frequency():
    assert DASHBOARD_PAGE.get_drivers_by_highest_score_title(), IsEqualIgnoringCase("Drivers by Highest Score")
    DASHBOARD_PAGE.click_behaviors_details_link()
    assert BEHAVIORS_REPORT_PAGE.get_behavior_text() == "BEHAVIOR"
    assert BEHAVIORS_REPORT_PAGE.get_frequency_text() == "FREQUENCY"
    assert BEHAVIORS_REPORT_PAGE.get_trend_text() == "TREND"
    DASHBOARD_PAGE.back_to_previous_page()


# LQ-391
@when('the user clicks "LIBRARY" and the user clicks "COACHING HISTORY"')
def navigate_to_coaching_history():
    DASHBOARD_PAGE.click_library_tab_new_ui()
    DASHBOARD_PAGE.click_coaching_history_new_ui()


@then(
    'all coaching history are displayed and the table is displayed with columns "TYPE","DRIVER","GROUP","EVENTID","ISSUED BY","ISSUED DATE","RECOGNITION REASON"')
def verify_coaching_history_displayed():
    assert LIBRARY_PAGE.get_row_count() == 0
    assert LIBRARY_PAGE.get_session_id_label() == "SESSION ID"
    assert LIBRARY_PAGE.get_coach_date_label() == "COACH DATE"
    assert LIBRARY_PAGE.get_overdue_date_label() == "OVERDUE DATE"
    assert LIBRARY_PAGE.get_driver_label() == "DRIVER"
    assert LIBRARY_PAGE.get_behavior_coached_label() == "BEHAVIORS COACHED"
    assert LIBRARY_PAGE.get_group_label() == "GROUP"
    assert LIBRARY_PAGE.get_coach_label() == "COACH"
    assert LIBRARY_PAGE.get_notes_label() == "NOTES"


# LQ-386
@when('the user clicks "LIBRARY" and the user clicks "DATA EXPORT"')
def click_data_export():
    LIBRARY_PAGE.click_data_export_new_ui()


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


@then('the page header "USER MANAGEMENT" is displayed and the user count are displayed and the table'
      ' is displayed with columns: "NAME", "EMPLOYEE ID", "LYTX BADGE", "PRIMARY DRIVER GROUP", '
      '"ROLES (GROUP)", "STATUS", "LOGIN", "USERNAME"')
def verify_user_management_tabs():
    assert USER_MANAGEMENT_PAGE.user_management_label_is_displayed() is True
    assert USER_MANAGEMENT_PAGE.get_user_management_label() == "USER MANAGEMENT"
    assert USER_MANAGEMENT_PAGE.get_name_label() == "NAME"
    assert USER_MANAGEMENT_PAGE.get_employee_id_label() == "EMPLOYEE ID"
    assert USER_MANAGEMENT_PAGE.get_lytx_badge_label() == "LYTX BADGE"


# LQ-230
@when('the user clicks the "DEVICES" tab')
def navigate_to_device_management_page():
    USER_MANAGEMENT_PAGE.click_devices_tab()
    USER_MANAGEMENT_PAGE.wait_for_page_to_fully_load()


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


# @LQ-12437
@given('full access user logs in DVIR')
def launch_browser(browser):
    global LOGIN_PAGE, DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE, DASHBOARD_PAGE, DD, INSPECTION_SCHEDULES_PAGE, INSPECTION_LIST_MANAGEMENT_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE = DriverVehicleInspectionReportsPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    INSPECTION_SCHEDULES_PAGE = InspectionSchedulesPage(browser)
    INSPECTION_LIST_MANAGEMENT_PAGE = InspectionListManagementPage(browser)

    browser.get(DC_URL)

    if DC_URL == 'https://dc-int.drivecaminc.xyz/':
        DD = DD_INT
    elif DC_URL == 'https://dc-stg.drivecam.com/':
        DD = DD_STG
    else:
        DD = DD_PROD

    LOGIN_PAGE.enter_username(DD.fa_user_name)
    LOGIN_PAGE.enter_password(DD.password)
    LOGIN_PAGE.click_login()


@when('the user clicks DVIR')
def go_to_DVIR_page():
    DASHBOARD_PAGE.click_dvir_tab()
    DASHBOARD_PAGE.wait_for_page_to_fully_load()


@then(
    'Total reports count, reset button, group filter, date filter, status filter, defect filter and wild search filter are shown on "DRIVER VEHICLE INSPECTION REPORTS" page and table columns are: "REPORT ID", "TYPE", "STATUS", "REPORT DATE", "DRIVER", "VEHICLE", "MAJOR VEHICLE DEFECTS", "MINOR VEHICLE DEFECTS", "VEHICLE INSPECTION LIST", "TRAILER", "MAJOR TRAILER DEFECTS", "MINOR TRAILER DEFECTS", "TRAILER INSPECTION LIST", "MECHANIC/AGENT", "REVIEWER"')
def verify_driver_vehicle_inspection_report_page():
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_total_report_title() == "Reports"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_groups_filter_title() == "Select Group(s)"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_date_range_filter_title() == "Select Date Range"
    # comment this due to TOTORO-1815
    # assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_statuses_filter_title() == "Statuses"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_defects_filter_title() == "Defects"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_search_filter_title() == "Select Search"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_reset_button_title() == "Reset"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_report_Id_title() == "REPORT ID"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_type_title() == "TYPE"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_status_title() == "STATUS"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_report_date_title() == "REPORT DATE"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_driver_title() == "DRIVER"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_vehicle_title() == "VEHICLE"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_major_vehicle_defects_title() == "MAJOR VEHICLE DEFECTS"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_minor_vehicle_defects_title() == "MINOR VEHICLE DEFECTS"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_vehicle_inspection_list_title() == "VEHICLE INSPECTION LIST"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_trailer_title() == "TRAILER"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_major_trailer_defects_title() == "MAJOR TRAILER DEFECTS"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_minor_trailers_defects_title() == "MINOR TRAILER DEFECTS"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_trailer_inspection_list_title() == "TRAILER INSPECTION LIST"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_mechanic_agent_title() == "MECHANIC/AGENT"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_reviewer_title() == "REVIEWER"


# LQ-12436
@when('user clicks "SCHEDULE" on left navigation')
def click_schedule_tab():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_schedules_tab()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.wait_for_page_to_fully_load()


@then(
    'the page header "INSPECTION SCHEDULES" is displayed & the count of the vehicle schedule report is displayed & the table is displayed with columns')
def verify_inspection_schedules_table():
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_schedules_title() == "INSPECTION SCHEDULES"
    assert INSPECTION_SCHEDULES_PAGE.get_reports_title() == "Reports"
    assert INSPECTION_SCHEDULES_PAGE.get_vehicle_name_title() == "VEHICLE NAME"
    assert INSPECTION_SCHEDULES_PAGE.get_vehicle_group_title() == "VEHICLE GROUP"
    assert INSPECTION_SCHEDULES_PAGE.get_status_title() == "STATUS"
    assert INSPECTION_SCHEDULES_PAGE.get_due_date_title() == "DUE DATE"
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_list_title() == "INSPECTION LIST"
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_frequency_title() == "INSPECTION FREQUENCY"
    assert INSPECTION_SCHEDULES_PAGE.get_last_inspected_date_title() == "LAST INSPECTED DATE"
    assert INSPECTION_SCHEDULES_PAGE.get_last_inspected_driver_title() == "LAST INSPECTED DRIVER"


# @LQ-12460
@given('the "Full Access" user is landed in the vehicle schedule page')
def navigate_to_vehicle_schedule_page():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_schedules_tab()


@when('the user clicks Download CSV in vehicle schedule page')
def click_on_vehicle_schedule_download_csv():
    INSPECTION_SCHEDULES_PAGE.click_download_csv_report()


@then('the Vehicle Schedule report is downloaded')
def verify_csv_report_downloaded():
    file_name = INSPECTION_SCHEDULES_PAGE.get_dvir_list_file_name()
    assert INSPECTION_SCHEDULES_PAGE.check_file_exist(file_name) is True


# LQ-12446
@when('the "Full Access" user is in the Vehicle list page')
def navigate_to_vehicle_list_management_page():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_list_settings_existing_user_tab()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_list_management_tab_existing_user()


@then(
    'the title "VEHICLE INSPECTION LISTS" is displayed & there is a default vehicle inspection list and named "Default" & there is a duplicate icon behind the list name')
def verify_inspection_management_titles():
    assert INSPECTION_LIST_MANAGEMENT_PAGE.get_vehicle_inspection_list_title() == "VEHICLE INSPECTION LISTS"
    assert INSPECTION_LIST_MANAGEMENT_PAGE.get_default_title() == "Default"
    assert INSPECTION_LIST_MANAGEMENT_PAGE.vehicle_duplicate_icon_displayed() is True


# LQ-300
@given('"Full access" user is in Fleet Dashboard')
def go_to_driver_safety(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, FLEET_PAGE, LIBRARY_PAGE, TD

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    LIBRARY_PAGE = LibraryPage(browser)
    FLEET_PAGE = FleetMapPage(browser)
    browser.get(WELCOME_URL)

    if WELCOME_URL == 'https://login-int.drivecaminc.xyz/':
        TD = TD_INT
    elif WELCOME_URL == 'https://login-stg.drivecam.com/':
        TD = TD_STG
    else:
        TD = TD_PROD

    LOGIN_PAGE.enter_username(TD.full_access_user)
    LOGIN_PAGE.enter_password(TD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed_new_ui(DC_URL, TD.full_access_user, TD.password)


@when('user clicks on "FLEET TRACKING" on top navigation')
def navigate_to_video_search():
    DASHBOARD_PAGE.click_fleet_tracking_tab()


@then('user is navigated to "FLEET TRACKING" accordingly')
def verify_fleet_tracking():
    assert_that(DASHBOARD_PAGE.get_fleet_tracking_title(), IsEqualIgnoringCase("FLEET TRACKING"))


# LQ-15218

@given('the login page is displayed')
def launch_browser(browser):
    global LOGIN_PAGE, FLEET_MAP_PAGE, FMD, RANDOM_NAME

    LOGIN_PAGE = LoginPage(browser)
    FLEET_MAP_PAGE = FleetMapPage(browser)

    browser.get(FLEET_URL)

    if FLEET_URL == 'https://ft-int.drivecaminc.xyz/':
        FMD = FMD_INT
    elif FLEET_URL == 'https://ft-stg.drivecam.com/':
        FMD = FMD_STG
    else:
        FMD = FMD_PROD


@when('the user enters a newly created username/password and clicks the login button')
def login():
    LOGIN_PAGE.enter_username(FMD.user_name)
    LOGIN_PAGE.enter_password(FMD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed_new_ui(FLEET_URL, FMD.user_name, FMD.password)


@then('the Fleet application is displayed')
def assert_fleet_app():
    assert FLEET_MAP_PAGE.map_tab_is_displayed_new_UI() is True
    FLEET_MAP_PAGE.click_map_new_ui()
    assert FLEET_MAP_PAGE.get_settings_tab_text() == "SETTINGS"


# LQ-447 part 1
@when(
    'the user clicks "Clear List" and enters some characters in Search box and selects a geofence in the Suggestion List')
def add_geofence_to_working_list_via_suggestion_list():
    FLEET_MAP_PAGE.add_geofence_to_working_list(FMD.geofence_name_existing)


@then('the geofence is displayed in Working List and the geofence is displayed on Map')
def assert_geofence_detail_in_working_list():
    working_list_geofence = FLEET_MAP_PAGE.get_working_list_geofence()
    assert working_list_geofence['geofence_name'] == FMD.geofence_name_existing


# LQ-544
@given('user logins to fleet page')
def login_to_fleet_page(browser):
    global LOGIN_PAGE, FLEET_INSIGHT_PAGE, FID

    LOGIN_PAGE = LoginPage(browser)
    FLEET_INSIGHT_PAGE = FleetInsightsPage(browser)

    browser.get(FLEET_URL)

    if FLEET_URL == 'https://ft-int.drivecaminc.xyz/':
        FID = FID_INT
    elif FLEET_URL == 'https://ft-stg.drivecam.com/':
        FID = FID_STG
    else:
        FID = FID_PROD

    LOGIN_PAGE.enter_username(FID.user_name)
    LOGIN_PAGE.enter_password(FID.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed_new_ui(FLEET_URL, FID.user_name, FID.password)


@when('the user navigates to Insights -> Fleet Operations')
def go_to_fleet_operations():
    FLEET_INSIGHT_PAGE.click_insights_new_ui()
    FLEET_INSIGHT_PAGE.click_fleet_operations_new_ui()


@then('the groups tab of Fleet Operations page is displayed')
def assert_fleet_operations_groups_tab():
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_title() == "FLEET OPERATIONS"
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_groups_tab() == "Groups"


# LQ-543
@when('the user sets group filter to one group in Fleet Operations page Groups tab')
def driver_filter_group():
    FLEET_INSIGHT_PAGE.click_filter_group_group()
    FLEET_INSIGHT_PAGE.search_filter_group(FID.group)
    FLEET_INSIGHT_PAGE.select_search_filter(FID.group)
    FLEET_INSIGHT_PAGE.click_done()
    sleep(2)


@then('the data belong to the group are listed in Fleet Operations page Groups tab')
def assert_fleet_operations_group_filter_groups_tab():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == 1


# LQ-549
@when('the user clicks Drivers in Fleet Operations page')
def click_fleet_operations_drivers():
    FLEET_INSIGHT_PAGE.click_fleet_operations_drivers()


@then('the drivers tab of Fleet Operations page is displayed')
def assert_fleet_operations_drivers_tab():
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_drivers_tab() == "Drivers"


# LQ-558
@when('the user clicks a driver name')
def click_driver_name():
    pass

@then(
    'the driver name is displayed and the metadata bar is displayed with labels: "EMPLOYEE ID", "GROUP", "VEHICLE NAME", "EMAIL"')
def verify_driver_profile_metadata():
    assert FLEET_INSIGHT_PAGE.get_employee_id_text_driver_profile() == "EMPLOYEE ID"
    assert FLEET_INSIGHT_PAGE.get_group_text_driver_profile() == "GROUP"
    assert FLEET_INSIGHT_PAGE.get_vehicle_name_text_driver_profile() == "VEHICLE NAME"
    assert FLEET_INSIGHT_PAGE.get_email_text_driver_profile() == "EMAIL"
    assert FLEET_INSIGHT_PAGE.get_driver_name_text_driver_profile() == FID.driver


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


# LQ-511
@given('fleet dispatcher logs in')
def launch_browser_and_login(browser):
    global LOGIN_PAGE, FLEET_MAINT_PAGE, FMD

    LOGIN_PAGE = LoginPage(browser)
    FLEET_MAINT_PAGE = FleetMaintPage(browser)

    browser.get(FLEET_URL)

    if FLEET_URL == 'https://ft-int.drivecaminc.xyz/':
        FMD = FMD_INT
    elif FLEET_URL == 'https://ft-stg.drivecam.com/':
        FMD = FMD_STG
    else:
        FMD = FMD_PROD

    LOGIN_PAGE.enter_username(FMD.user_name)
    LOGIN_PAGE.enter_password(FMD.password)

    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed_new_ui(FLEET_URL, FMD.user_name, FMD.password)


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

    # clear service history dirty data if any
    FLEET_MAINT_PAGE.click_history_tab()
    n = int(FLEET_MAINT_PAGE.get_pm_history_service_count())
    while n > 0:
        n -= 1
        if n != 1:
            FLEET_MAINT_PAGE.click_pm_history_1st_edit()
        else:
            FLEET_MAINT_PAGE.click_pm_history_1st_only_edit()
        FLEET_MAINT_PAGE.click_date_selector_pm_history_edit_service()
        FLEET_MAINT_PAGE.set_months_ago_history_edit_service(10)
        FLEET_MAINT_PAGE.select_1st_day_pm_history_edit_service()
        FLEET_MAINT_PAGE.click_save_pm_history_edit_service()


# LQ-527
@when('the user clicks "Manage Services"')
def click_manage_services_tab():
    FLEET_MAINT_PAGE.click_manage_services()
    # sleep 2s to load services
    sleep(3)


@then('the Manage Services page is displayed')
def assert_manage_services_page():
    assert str(FLEET_MAINT_PAGE.get_row_count()) == FLEET_MAINT_PAGE.get_manage_service_services_count()


# LQ-528
@when('the user clicks the "Create Service" button')
def create_maint_service():
    if FLEET_MAINT_PAGE.get_manage_service_services_count() != '0':
        FLEET_MAINT_PAGE.delete_existing_service()

    FLEET_MAINT_PAGE.click_create_service()


@when('the user enter some characters in the "SERVICE NAME", "SERVICE INTERVAL (MI)", "DUE SOON THRESHOLD (MI)" field')
def set_service_parameters():
    FLEET_MAINT_PAGE.set_service_parameters("maint-auto-service", "1000", "800")
    sleep(4)


@when('the user clicks the save button')
def save_maint_service():
    FLEET_MAINT_PAGE.click_save_service()


@then('the service is created')
def assert_service_is_created():
    assert FLEET_MAINT_PAGE.get_manage_service_services_count() == '1'


# LQ-15219
@given('the login page is displayed in Video Search')
def launch_browser(browser):
    global LOGIN_PAGE, VIDEO_SEARCH_PAGE, DASHBOARD_PAGE, VSD

    LOGIN_PAGE = LoginPage(browser)
    VIDEO_SEARCH_PAGE = VideoSearchPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)

    browser.get(DC_URL)

    if DC_URL == 'https://dc-int.drivecaminc.xyz/':
        VSD = VSD_INT
    elif DC_URL == 'https://dc-stg.drivecam.com/':
        VSD = VSD_STG
    else:
        VSD = VSD_PROD


@when('the Video Reviewer Plus user enters a newly created username/password and clicks the login button')
def login():
    LOGIN_PAGE.enter_username(VSD.user_name_real_device)
    LOGIN_PAGE.enter_password(VSD.password_real_device)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()


@then('the user is successfully logged into the Video Search page')
def verify_login():
    assert VIDEO_SEARCH_PAGE.get_video_search_title() == "Video Search"


# LQ-201
@when('the user sets group filter to one group in vehicles page')
def set_group_filter_vehicle_page():
    VIDEO_SEARCH_PAGE.click_group_filter()
    VIDEO_SEARCH_PAGE.search_group(VSD.group)
    sleep(2)
    VIDEO_SEARCH_PAGE.select_searched_group()
    VIDEO_SEARCH_PAGE.click_done_button()


@then('the vehicles belong to the group are listed')
def verify_group_filter_vehicle_page():
    assert VIDEO_SEARCH_PAGE.vehicle_count_displayed() is True
    # assert VIDEO_SEARCH_PAGE.get_row_count() == VSD.no_of_vehicles
    VIDEO_SEARCH_PAGE.click_reset_button()


@when('the user selects "Vehicle Name" from "Select Search" dropdown and the user input some characters in search bar')
def search_by_vehicle_name_vehicle_page():
    VIDEO_SEARCH_PAGE.click_select_search_filter()
    VIDEO_SEARCH_PAGE.select_vehicle_name_dropdown()
    VIDEO_SEARCH_PAGE.search_criteria_textbox(VSD.vehicle)


@then('the vehicles with the inputted characters are listed')
def verify_searched_by_vehicle_name_vehicle_page():
    assert VIDEO_SEARCH_PAGE.vehicle_count_displayed() is True
    # assert VIDEO_SEARCH_PAGE.get_row_count() == VSD.single_vehicle_count
    VIDEO_SEARCH_PAGE.click_reset_button()


@when('the user selects "Serial Number" from "Select Search" dropdown and the user input some characters in search bar')
def search_by_serial_name_vehicle_page():
    VIDEO_SEARCH_PAGE.click_select_search_filter()
    VIDEO_SEARCH_PAGE.select_serial_name_dropdown()
    VIDEO_SEARCH_PAGE.search_criteria_textbox(VSD.device)


@then('the vehicles which attached ER serial number with the inputted characters are listed')
def verify_searched_by_serial_name_vehicle_page():
    assert VIDEO_SEARCH_PAGE.vehicle_count_displayed() is True
    # assert VIDEO_SEARCH_PAGE.get_row_count() == VSD.no_of_vehicles_attached_to_a_device
    VIDEO_SEARCH_PAGE.click_reset_button()


# LQ-373
@given('the welcome login page is displayed for RDS company')
def launch_welcome_login_page(browser):
    global LOGIN_PAGE, RISK_COMPANY_PAGE, BEHAVIORS_REPORT_PAGE, RCD, BASE_PAGE, DASHBOARD_PAGE

    LOGIN_PAGE = LoginPage(browser)
    RISK_COMPANY_PAGE = RiskCompanyPage(browser)
    BEHAVIORS_REPORT_PAGE = BehaviorsReportPage(browser)
    BASE_PAGE = BasePage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)

    browser.get(DC_URL)

    if DC_URL == 'https://dc-int.drivecaminc.xyz/':
        RCD = RCD_INT
    elif DC_URL == 'https://dc-stg.drivecam.com/':
        RCD = RCD_STG
    else:
        RCD = RCD_PROD


@when('the user login WS for a risk company')
def login_risk_company():
    LOGIN_PAGE.enter_username(RCD.risk_fa_user)
    LOGIN_PAGE.enter_password(RCD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed_new_ui(DC_URL, RCD.risk_fa_user, RCD.password)


@then(
    'the Dashboard page is displayed and the Dashboard page includes "Drivers by Highest Score","Categories by Highest Frequency" and And the Dashboard page includes a driver counts, Group filter, Date filter')
def assert_dashboard_page():
    assert RISK_COMPANY_PAGE.get_dashboard_text() == "DASHBOARD"
    assert RISK_COMPANY_PAGE.get_drivers_by_highest_score_text() == "Drivers by Highest Score"
    assert RISK_COMPANY_PAGE.get_categories_by_highest_frequency_text() == "Categories by Highest Frequency"
    assert RISK_COMPANY_PAGE.driver_count_displayed() is True
    assert RISK_COMPANY_PAGE.group_filter_displayed() is True
    assert RISK_COMPANY_PAGE.date_filter_displayed() is True


# LQ-376

@given(
    'the "Safety Manager" user is on Dashboard page of company A & the dcops key "DC_EnableCoaching" is false of company A')
def navigate_to_dashboard_page():
    RISK_COMPANY_PAGE.click_home_tab_new_ui()


@when('the user sets group filter to one group in dashboard page')
def set_group_filter_dashboard():
    RISK_COMPANY_PAGE.click_filter_group_dashboard()
    RISK_COMPANY_PAGE.search_group_filter_dashboard("Vehicle")
    RISK_COMPANY_PAGE.click_searched_group_filter()
    RISK_COMPANY_PAGE.click_done_group_filter()


@then('the data belong to the selected group are displayed in dashboard page')
def verify_group_filter_dashboard():
    RISK_COMPANY_PAGE.click_view_details()
    assert BEHAVIORS_REPORT_PAGE.get_row_count() == 0


@when('the user sets date filter in dashboard page')
def set_date_filter_dashboard():
    RISK_COMPANY_PAGE.click_home_tab_new_ui()
    RISK_COMPANY_PAGE.click_date_filter()
    RISK_COMPANY_PAGE.click_date1_filter()
    RISK_COMPANY_PAGE.click_date2_filter()
    RISK_COMPANY_PAGE.click_apply_date_filter()


@then('the data belong to the selected date range are displayed in dashboard page')
def verify_date_filter_dashboard():
    RISK_COMPANY_PAGE.click_view_details()
    assert BEHAVIORS_REPORT_PAGE.get_row_count() == 0


# LQ-378
@when('the user clicks "INSIGHTS" & the user clicks "DRIVERS REPORT"')
def navigate_to_drivers_report_page():
    RISK_COMPANY_PAGE.click_insights_tab_new_ui()
    RISK_COMPANY_PAGE.click_drivers_report_new_ui()


@then(
    'the drivers report page is opened & there are 3 tabs： "Drivers Scores","Continual Behaviors", "Alerts" & the table of "Driver Scores" is displayed')
def verify_drivers_report_titles():
    assert RISK_COMPANY_PAGE.get_drivers_report_text() == "DRIVERS REPORT"
    assert RISK_COMPANY_PAGE.get_driver_scors_text() == "Driver Scores"
    assert RISK_COMPANY_PAGE.get_continual_behaviors_text() == "Continual Behaviors"
    assert RISK_COMPANY_PAGE.get_alerts_text() == "Alerts"
    assert RISK_COMPANY_PAGE.get_driver_text() == "DRIVER"
    assert RISK_COMPANY_PAGE.get_group_text() == "GROUP"
    assert RISK_COMPANY_PAGE.get_score_text() == "SCORE"
    assert RISK_COMPANY_PAGE.get_events_text() == "EVENTS"
    assert RISK_COMPANY_PAGE.get_recent_notes_text() == "RECENT NOTES"