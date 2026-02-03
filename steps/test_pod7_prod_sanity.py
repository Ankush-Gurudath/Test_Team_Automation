from hamcrest import assert_that, contains_string
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then
from pages.add_user_page import *
from pages.add_vehicle_page import AddVehiclePage
from pages.behaviors_report_page import BehaviorsReportPage
from pages.dashboard_page import DashboardPage
from pages.device_management_page import DeviceManagementPage
from pages.device_profile_page import DeviceProfilePage
from pages.driver_profile_page import DriverProfilePage
from pages.driver_vehicle_inspection_reports_page import DriverVehicleInspectionReportsPage
from pages.edit_user_page import EditUserPage
from pages.fleet_insights_page import FleetInsightsPage
from pages.fleet_maint_page import FleetMaintPage
from pages.fleet_map_page import FleetMapPage
from pages.fleet_telematics_center_page import FleetTelematicsCenterPage
from pages.fleet_telematics_left_panel_page import FleetTelematicsPageLeftPanel
from pages.inspection_list_management_page import InspectionListManagementPage
from pages.inspection_schedules_page import InspectionSchedulesPage
from pages.library_page import LibraryPage
from pages.login_page import LoginPage
from pages.open_tasks_report_page import OpenTasksReportPage
from pages.recognition_history_page import RecognitionHistoryPage
from pages.risk_company import RiskCompanyPage
from pages.user_management_page import UserManagementPage
from pages.video_search_page import VideoSearchPage
from steps.common import DC_URL, TestDataEnum, WELCOME_URL
from data.prod.fleet_insights_data_prod import FleetInsightsDataProd as FID
from data.prod.home_data_prod import HomeDataProd as HD
from data.prod.video_search_data_prod import VideoSearchDataProd as VSD
from data.prod.risk_company_data_prod import RiskCompanyDataProd as RCD
from pages.inspection_list_assignment_page import InspectionListAssignmentPage
from pages.vehicle_management_page import VehicleManagementPage
from pages.geofence_management_page import GeofenceManagementPage
from pages.trailer_management_page import TrailerManagementPage
from pages.configuration_setting_page import ConfigurationSettingPage
from pages.equipment_management_page import EquipmentManagementPage
from pages.driver_id_assignment_page import DriverIdAssignmentPage
from pages.device_health_page import DeviceHealthPage
from pages.coaching_page import CoachingPage
from pages.assign_driver_page import AssignDriverPage
from pages.collisions_page import CollisionsPage
from pages.fyi_notify_page import FyiNotifyPage
from pages.drivers_report_page import DriversReportPage
from pages.group_report_page import GroupReportPage
from pages.coaches_report_page import CoachesReportPage
from pages.program_status_report_page import ProgramStatusReportPage
from pages.consent_report_page import ConsentReportPage

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
COACHING_PAGE = 0
LIBRARY_PAGE = 0
FLEET_MAP_PAGE = 0
RISK_COMPANY_PAGE = 0
OPEN_TASKS_REPORT_PAGE = 0
BEHAVIORS_REPORT_PAGE = 0
BASE_PAGE = 0
FLEET_MAINT_PAGE = 0
USER_MANAGEMENT_PAGE = 0
DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE = 0
INSPECTION_SCHEDULES_PAGE = 0
RECOGNITION_HISTORY_PAGE = 0
DEVICE_MANAGEMENT_PAGE = 0
INSPECTION_LIST_MANAGEMENT_PAGE = 0
FLEET_INSIGHT_PAGE = 0
INSPECTION_LIST_ASSIGNMENT_PAGE = 0
EDIT_USER_PAGE = 0
VEHICLE_MANAGEMENT_PAGE = 0
ADD_VEHICLE_PAGE = 0
DEVICE_PROFILE_PAGE = 0
GEOFENCE_MANAGEMENT_PAGE = 0
TRAILER_MANAGEMENT_PAGE = 0
CONFIGURATION_SETTING_PAGE = 0
EQUIPMENT_MANAGEMENT_PAGE = 0
DRIVER_ID_ASSIGNMENT_PAGE = 0
DEVICE_HEALTH_PAGE = 0
ASSIGN_DRIVER_PAGE = 0
COLLISIONS_PAGE = 0
FYI_NOTIFY_PAGE = 0
DRIVERS_REPORT_PAGE = 0
GROUP_REPORT_PAGE = 0
COACHES_REPORT_PAGE = 0
PROGRAM_STATUS_REPORT_PAGE = 0
CONSENT_REPORT_PAGE = 0
FLEET_TELEMATICS_PAGE = 0
FLEET_TELEMATICS_CENTER_PAGE = 0

scenarios('../features/pod7_prod_sanity.feature')


# LQ-306
@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, COACHING_PAGE, FYI_NOTIFY_PAGE, COLLISIONS_PAGE, ASSIGN_DRIVER_PAGE, DEVICE_HEALTH_PAGE, DRIVER_ID_ASSIGNMENT_PAGE, \
        EQUIPMENT_MANAGEMENT_PAGE, CONFIGURATION_SETTING_PAGE, TRAILER_MANAGEMENT_PAGE, GEOFENCE_MANAGEMENT_PAGE, EDIT_USER_PAGE, VEHICLE_MANAGEMENT_PAGE, ADD_VEHICLE_PAGE, \
        DEVICE_PROFILE_PAGE, LIBRARY_PAGE, USER_MANAGEMENT_PAGE, DEVICE_MANAGEMENT_PAGE, OPEN_TASKS_REPORT_PAGE, LD, ID, DRIVER_PROFILE_PAGE, BEHAVIORS_REPORT_PAGE, RECOGNITION_HISTORY_PAGE, \
        DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE, INSPECTION_SCHEDULES_PAGE, INSPECTION_LIST_MANAGEMENT_PAGE, INSPECTION_LIST_ASSIGNMENT_PAGE, FLEET_MAP_PAGE, FLEET_MAINT_PAGE, FLEET_INSIGHT_PAGE, VIDEO_SEARCH_PAGE, \
        DRIVERS_REPORT_PAGE, GROUP_REPORT_PAGE, COACHES_REPORT_PAGE, PROGRAM_STATUS_REPORT_PAGE, CONSENT_REPORT_PAGE, FLEET_TELEMATICS_PAGE, FLEET_TELEMATICS_CENTER_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    LIBRARY_PAGE = LibraryPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)
    DEVICE_MANAGEMENT_PAGE = DeviceManagementPage(browser)
    BEHAVIORS_REPORT_PAGE = BehaviorsReportPage(browser)
    RECOGNITION_HISTORY_PAGE = RecognitionHistoryPage(browser)
    DRIVER_PROFILE_PAGE = DriverProfilePage(browser)
    OPEN_TASKS_REPORT_PAGE = OpenTasksReportPage(browser)
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE = DriverVehicleInspectionReportsPage(browser)
    INSPECTION_SCHEDULES_PAGE = InspectionSchedulesPage(browser)
    INSPECTION_LIST_MANAGEMENT_PAGE = InspectionListManagementPage(browser)
    INSPECTION_LIST_ASSIGNMENT_PAGE = InspectionListAssignmentPage(browser)
    FLEET_MAP_PAGE = FleetMapPage(browser)
    FLEET_MAINT_PAGE = FleetMaintPage(browser)
    FLEET_INSIGHT_PAGE = FleetInsightsPage(browser)
    VIDEO_SEARCH_PAGE = VideoSearchPage(browser)
    EDIT_USER_PAGE = EditUserPage(browser)
    VEHICLE_MANAGEMENT_PAGE = VehicleManagementPage(browser)
    ADD_VEHICLE_PAGE = AddVehiclePage(browser)
    DEVICE_PROFILE_PAGE = DeviceProfilePage(browser)
    GEOFENCE_MANAGEMENT_PAGE = GeofenceManagementPage(browser)
    TRAILER_MANAGEMENT_PAGE = TrailerManagementPage(browser)
    CONFIGURATION_SETTING_PAGE = ConfigurationSettingPage(browser)
    EQUIPMENT_MANAGEMENT_PAGE = EquipmentManagementPage(browser)
    DRIVER_ID_ASSIGNMENT_PAGE = DriverIdAssignmentPage(browser)
    DEVICE_HEALTH_PAGE = DeviceHealthPage(browser)
    COACHING_PAGE = CoachingPage(browser)
    ASSIGN_DRIVER_PAGE = AssignDriverPage(browser)
    COLLISIONS_PAGE = CollisionsPage(browser)
    FYI_NOTIFY_PAGE = FyiNotifyPage(browser)
    DRIVERS_REPORT_PAGE = DriversReportPage(browser)
    GROUP_REPORT_PAGE = GroupReportPage(browser)
    COACHES_REPORT_PAGE = CoachesReportPage(browser)
    PROGRAM_STATUS_REPORT_PAGE = ProgramStatusReportPage(browser)
    CONSENT_REPORT_PAGE = ConsentReportPage(browser)
    FLEET_TELEMATICS_PAGE = FleetTelematicsPageLeftPanel(browser)
    FLEET_TELEMATICS_CENTER_PAGE = FleetTelematicsCenterPage(browser)

    browser.get(WELCOME_URL)


@when('the user enters a newly created username/password and clicks the login button in the page')
def login():
    LOGIN_PAGE.enter_username(HD.pod7_full_access_username)
    LOGIN_PAGE.enter_password(HD.password2)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed_new_ui(WELCOME_URL, HD.pod7_full_access_username, HD.password2)


@then('the user is successfully logged into the Driver Safety dashboard in the same company')
def verify_login():
    assert DASHBOARD_PAGE.get_driver_safety_title() == "Driver Safety"


# LQ-387
@when('the user signs in to Driver Safety')
def login_to_safety():
    DASHBOARD_PAGE.click_home_menu()


@then('the Dashboard page is displayed & the Drivers count is displayed & the UNASSIGNED DRIVERS count'
      ' is displayed in last 90 days & the DUE FOR COACHING count is displayed in last 90 days '
      '& the FYI NOTIFY count is displayed in last 90 days $ the COLLISIONS count is displayed in'
      ' last 90 days & the POSSIBLE COLLISIONS count is displayed in last 90 days')
def verify_dashboard():
    # assert DASHBOARD_PAGE.no_of_unassigned_drivers_is_displayed() is True
    # assert DASHBOARD_PAGE.no_of_tasks_is_displayed() is True
    # assert DASHBOARD_PAGE.no_of_drivers_is_displayed() is True
    assert_that(DASHBOARD_PAGE.get_unassigned_drivers_text(), contains_string("UNASSIGNED DRIVER"))
    assert DASHBOARD_PAGE.get_due_for_coaching_text() == "DUE FOR COACHING"
    assert DASHBOARD_PAGE.get_fyi_notify_text() == "FYI NOTIFY"
    assert_that(DASHBOARD_PAGE.get_collisions_text(), contains_string('COLLISION'))
    assert_that(DASHBOARD_PAGE.get_possible_collisions_text(), contains_string("POSSIBLE COLLISION"))
    # Validate all dashboard details links contain the expected label
    for _name, link_text in DASHBOARD_PAGE.get_all_dashboard_details_links().items():
        assert_that(link_text, contains_string("View Details"))


# LQ-390
@when('the user clicks link')
def click_links():
    DASHBOARD_PAGE.click_unassigned_drivers_link()


@then('the page is displayed')
def verify_links():
    assert DASHBOARD_PAGE.get_assigned_drivers_title() == "ASSIGN DRIVERS"
    DASHBOARD_PAGE.back_to_previous_page()


# LQ-392
@when('the user is in Driver Safety')
def login_to_dashboard():
    DASHBOARD_PAGE.click_home_menu()


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
    DASHBOARD_PAGE.click_home_menu()


@then(
    'there is "Coaches by Lowest Effectiveness" in "METRICS" & the table are displayed with columns "COACH", "COACHING EFFECTIVENESS", "AVG DAYS TO COACH", "COACHED EVENTS", WITH NOTES')
def verify_coaches_by_lowest_effectiveness():
    assert DASHBOARD_PAGE.get_coachest_by_lowest_effectiveness_title(), IsEqualIgnoringCase(
        "Coaches by Lowest Effectiveness")
    assert DASHBOARD_PAGE.get_coach_title() == "coach"
    assert DASHBOARD_PAGE.get_coaching_effectiveness_title(), IsEqualIgnoringCase("coaching effectiveness")
    assert DASHBOARD_PAGE.get_avg_days_to_coach_title() == "avg days to coach"
    assert DASHBOARD_PAGE.get_coached_events_title() == "coached events"
    assert DASHBOARD_PAGE.get_with_notes_title() == "with notes"


# LQ-404
@when('the user landed in Driver Safety')
def land_in_dashboard():
    DASHBOARD_PAGE.click_home_menu()


@then(
    'there is "Drivers by Highest Score" in "METRICS" & the table are displayed with columns "DRIVER", "COACHABLE SCORE", "TREND", IMPACT')
def verify_drivers_by_highest_score():
    assert DASHBOARD_PAGE.get_drivers_by_highest_score_title(), IsEqualIgnoringCase("Drivers by Highest Score")
    assert DASHBOARD_PAGE.get_driver_title() == "Driver"
    assert DASHBOARD_PAGE.get_driver_widget_coachable_score_title() == "Coachable Score"
    assert DASHBOARD_PAGE.get_driver_widget_trend_title() == "Trend"
    assert DASHBOARD_PAGE.get_impact_title() == "Impact"


# LQ-407
# LQ-93743
@when('the user is back to Driver Safety')
def user_in_dashboard():
    DASHBOARD_PAGE.click_home_menu()


@then(
    'there is "Behaviors by Highest Frequency" in "METRICS" & the table are displayed with columns "BEHAVIOR", "FREQ.", TREND')
def verify_behaviors_by_highest_frequency():
    assert DASHBOARD_PAGE.get_behaviors_by_highest_frequency_title() == "Behaviors by Highest Frequency"
    DASHBOARD_PAGE.click_behaviors_details_link()
    assert BEHAVIORS_REPORT_PAGE.get_behavior_text() == "BEHAVIOR"
    assert BEHAVIORS_REPORT_PAGE.get_frequency_text() == "FREQUENCY"
    assert BEHAVIORS_REPORT_PAGE.get_trend_text() == "TREND"
    DASHBOARD_PAGE.back_to_previous_page()


# LQ-93743
@then('there is "Safe Driving Trend" in "METRICS" and the graph and pi chart is displayed')
def verify_Safe_Driving_Trend():
    assert DASHBOARD_PAGE.get_safe_driving_trend_title(), IsEqualIgnoringCase("Safe Driving Trend")
    assert DASHBOARD_PAGE.graph_is_displayed_in_safe_drive_trend() is True


# LQ-93743
@then(
    'there is "Groups by Highest % Safe Drivers" in "METRICS" and the table contains columns "group","% safe drivers", "eligible for recognition", "recognized"')
def verify_Groups_by_Highest_Safe_Drivers():
    assert DASHBOARD_PAGE.get_groups_by_highest_safe_drivers_title(), IsEqualIgnoringCase(
        "Groups by Highest % Safe Drivers")
    assert DASHBOARD_PAGE.get_group_text() == "GROUP"
    assert DASHBOARD_PAGE.get_percentage_safe_drivers_text() == "% SAFE DRIVERS"
    assert DASHBOARD_PAGE.get_eligible_for_recognition_text(), IsEqualIgnoringCase("eligible for recognition")
    assert DASHBOARD_PAGE.get_recognized_text(), IsEqualIgnoringCase("recognized")


# LQ-266
@given('Safety Manager user is in Driver Safety')
def navigate_to_dashboard_page():
    DASHBOARD_PAGE.click_home_menu()


@given('Safety Manager user is in Due For Coaching page')
@when('the user clicks "TASKS" & the user clicks DUE FOR COACHING')
def go_to_due_for_coaching():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_due_for_coaching_link()


@then('the task count is displayed & there are some information on the card')
def verify_coaching_card():
    assert DASHBOARD_PAGE.get_due_for_coaching_title() == "DUE FOR COACHING"
    assert_that(COACHING_PAGE.get_task_coaching_label(), contains_string("Task"))
    assert COACHING_PAGE.get_group_card_label() == "GROUP"
    assert COACHING_PAGE.get_vehicle_card_label() == "VEHICLE"
    assert COACHING_PAGE.get_event_date_card_label() == "EVENT DATE"
    assert COACHING_PAGE.get_time_card_label() == "TIME"
    assert COACHING_PAGE.get_overdue_date_card_label() == "OVERDUE DATE"
    assert COACHING_PAGE.get_behaviors_card_label(), contains_string("BEHAVIORS")
    # assert COACHING_PAGE.get_no_coach_events_card_label() == "Coach Event"


@when('the user clicks "Coach X Events" of the first bundle card')
def go_to_driver_coaching_session():
    DASHBOARD_PAGE.click_coaching_events_new_UI()
    if COACHING_PAGE.continue_button_is_displayed():
        COACHING_PAGE.click_continue_button()


@then('the Driver Coaching Session page is opened &  there is driver info in the page')
def verify_coaching_session():
    assert COACHING_PAGE.get_driver_coaching_session_label_new_UI() == "DRIVER COACHING SESSION"
    assert COACHING_PAGE.get_employee_id_label() == "EMPLOYEE ID"
    assert COACHING_PAGE.get_group_label() == "GROUP"
    assert COACHING_PAGE.get_email_label() == "EMAIL"


@when('the user clicks "TASKS" and the user clicks "ASSIGN DRIVERS"')
def click_task():
    FLEET_TELEMATICS_PAGE.click_assign_drivers_submenu()


@then(
    'the task count is displayed & there is "Assign Selected" button with un-selectable status & there is "Move Group" button with un-selectable status & there are "VEHICLE", "GROUP", "EVENT DATE", "EVENT ID", "BEHAVIORS" column & there are checkbox & "ASSIGN" button for each Assign Driver task')
def verify_task():
    assert ASSIGN_DRIVER_PAGE.get_assign_select_button_text() == "Assign Selected"
    assert ASSIGN_DRIVER_PAGE.get_disabled_status_of_assign_selected_button() == "true"
    assert ASSIGN_DRIVER_PAGE.get_move_group_button_text() == "Move Group"
    assert ASSIGN_DRIVER_PAGE.get_disabled_status_of_move_group_button() == "true"
    assert ASSIGN_DRIVER_PAGE.get_vehicle_text() == "VEHICLE"
    assert ASSIGN_DRIVER_PAGE.get_group_text() == "GROUP"
    assert ASSIGN_DRIVER_PAGE.get_event_date_text() == "EVENT DATE"
    assert ASSIGN_DRIVER_PAGE.get_event_id_text() == "EVENT ID"
    assert ASSIGN_DRIVER_PAGE.get_behavior_text(), contains_string("BEHAVIORS")
    assert ASSIGN_DRIVER_PAGE.get_assign_button_text() == 'Assign'


# LQ-318
@when('the user clicks "TASKS" and the user clicks "COLLISIONS"')
def navigate_to_collisions_page():
    FLEET_TELEMATICS_PAGE.click_collisions_submenu()


@then(
    'the task count is displayed and there are "DRIVER NAME", "GROUP", "VEHICLE", "EVENT DATE", "TIME" for each card and there is "Preview" button')
def verify_collision_task_page():
    assert isinstance(COLLISIONS_PAGE.get_driver_name_text(), str) or (
            COLLISIONS_PAGE.get_driver_name_text() == "Driver Unassigned")
    assert COLLISIONS_PAGE.get_group_text_new_ui() == "GROUP"
    assert COLLISIONS_PAGE.get_vehicle_text_new_UI() == "VEHICLE"
    assert COLLISIONS_PAGE.get_event_date_text_new_UI() == "EVENT DATE"
    assert COLLISIONS_PAGE.get_time_text_new_UI() == "TIME"
    assert COLLISIONS_PAGE.get_preview_button_text_new_UI() == "Preview"


@when('the user clicks "TASKS" & the user clicks "FYI NOTIFY"')
def go_to_fyi_task():
    FLEET_TELEMATICS_PAGE.click_fyinotify_submenu()


@then(
    'there are "GROUP", "VEHICLE", "EVENT DATE", "TIME" for each card & there is "Preview" button')  # need to add behavior label once api creates event with behavior
def view_fyi_task():
    assert COLLISIONS_PAGE.get_group_text_new_ui() == "GROUP"
    assert COLLISIONS_PAGE.get_vehicle_text_new_UI() == "VEHICLE"
    assert COLLISIONS_PAGE.get_event_date_text_new_UI() == "EVENT DATE"
    assert COLLISIONS_PAGE.get_time_text_new_UI() == "TIME"
    assert COLLISIONS_PAGE.get_preview_button_text_new_UI() == "Preview"


# LQ-383
@when('the user clicks "INSIGHTS" and the user clicks "OPEN TASKS REPORT" in Open Tasks Report page')
def open_tasks_filter():
    FLEET_TELEMATICS_PAGE.click_insights_menu()
    FLEET_TELEMATICS_PAGE.click_open_tasks_report_submenu()


@then('the Event profile page is displayed in Open Tasks Report page')
def verify_table_data():
    assert OPEN_TASKS_REPORT_PAGE.get_driver_text() == "DRIVER"
    assert OPEN_TASKS_REPORT_PAGE.get_driver_group_text() == "DRIVER'S GROUP"
    assert OPEN_TASKS_REPORT_PAGE.get_f2f_text() == "FACE-TO-FACE"
    assert OPEN_TASKS_REPORT_PAGE.get_f2f_overdue_text() == "FACE-TO-FACE (OVERDUE)"


# LQ-339
@when('the user clicks "INSIGHTS" and the user clicks "DRIVERS REPORT" in Drivers Report page')
def driver_scores_tab():
    FLEET_TELEMATICS_PAGE.click_drivers_report_submenu()


@then('the Driver Scores tab is selected and the number of drivers is displayed '
      'and the table is displayed with columns "DRIVER NAME", "GROUP", "COACHABLE SCORE Total", '
      '"COACHABLE SCORE Trend", "COACHABLE EVENTS Total", "COACHABLE EVENTS Trend", '
      '"TOTAL SCORE Total", "TOTAL SCORE Trend", "TOTAL EVENTS Total", "TOTAL EVENTS Trend" '
      'in Drivers Report page')
def verify_driver_scores():
    assert DRIVERS_REPORT_PAGE.get_driver_text() == "DRIVER"
    assert DRIVERS_REPORT_PAGE.get_group_text() == "GROUP"
    assert DRIVERS_REPORT_PAGE.get_coachable_score_text() == "COACHABLE SCORE"
    assert DRIVERS_REPORT_PAGE.get_coachable_events_text() == "COACHABLE EVENTS"
    assert DRIVERS_REPORT_PAGE.get_total_score_text() == "TOTAL SCORE"
    assert DRIVERS_REPORT_PAGE.get_total_events_text() == "TOTAL EVENTS"


# LQ-366
@when('the user clicks "INSIGHTS" And the user clicks "GROUP REPORT" in Group Report page')
def group_report_tab():
    FLEET_TELEMATICS_PAGE.click_group_report_submenu()


@then('the number of group is displayed and the table is displayed with columns "GROUP", '
      '"# OF VEHICLES", "COACHABLE SCORE Total", "COACHABLE SCORE Trend", '
      '"COACHABLE EVENTS Total", "COACHABLE EVENTS Trend" in Group Report page')
def verify_group_report_table():
    sleep(3)  # Report takes time to render
    assert GROUP_REPORT_PAGE.get_group_text() == "GROUP"
    assert GROUP_REPORT_PAGE.get_num_of_vehicles_text() == "# OF VEHICLES"
    assert GROUP_REPORT_PAGE.get_coachable_score_text() == "COACHABLE SCORE"
    assert GROUP_REPORT_PAGE.get_coachable_events_text() == "COACHABLE EVENTS"


# LQ-379
@when('the user clicks "INSIGHTS" And the user clicks "COACHES REPORT" in Coaches Report page')
def coaches_report_tab():
    FLEET_TELEMATICS_PAGE.click_coaches_report_submenu()


@then('the number of coaches is displayed  in Coaches Report page And the table is displayed '
      'with columns "COACH", "GROUP", "COACHING EFFECTIVENESS", "AVG DAYS TO COACH", '
      '"COACHED EVENTS", "WITH NOTES", "LAST LOGIN" in Coaches Report page')
def verify_coaches_report_table():
    sleep(2)  # Subgroups animation takes a few seconds to display. I couldn't find a workaround.
    assert COACHES_REPORT_PAGE.get_coach_text() == "COACH"
    assert COACHES_REPORT_PAGE.get_group_text() == "GROUP"
    assert COACHES_REPORT_PAGE.get_avg_days_to_coach_text() == "AVG DAYS TO COACH"
    assert COACHES_REPORT_PAGE.get_coached_events_text() == "COACHED EVENTS"
    assert COACHES_REPORT_PAGE.get_with_notes_text() == "WITH NOTES"
    assert COACHES_REPORT_PAGE.get_last_login_text() == "LAST LOGIN"


# LQ-369
@when('the user clicks "INSIGHTS" And the user clicks "PROGRAM STATUS REPORT" '
      'in Program Status Report page')
def program_status_report_tab():
    FLEET_TELEMATICS_PAGE.click_program_status_report_submenu()


@then('the number of subgroups is displayed And the table is displayed with columns "GROUP", '
      '"# OF DEVICES", "UNASSIGNED DRIVERS", "OVERDUE FOR CHECK-IN", "OVERDUE FOR COACHING", '
      '"COACHING EFFECTIVENESS", "PROGRAM EFFECTIVENESS" in Program Status Report page')
def verify_program_status_report_table():
    sleep(5)  # Subgroups animation takes a few seconds to display. I couldn't find a workaround.
    assert PROGRAM_STATUS_REPORT_PAGE.get_group_text() == "GROUP"
    assert PROGRAM_STATUS_REPORT_PAGE.get_num_of_devices_text() == "# OF DEVICES"
    assert PROGRAM_STATUS_REPORT_PAGE.get_unassigned_drivers_text() == "UNASSIGNED DRIVERS"
    assert PROGRAM_STATUS_REPORT_PAGE.get_overdue_for_checkin_text() == "OVERDUE FOR CHECK-IN"
    assert PROGRAM_STATUS_REPORT_PAGE.get_overdue_for_coaching_text() == "OVERDUE FOR COACHING"
    assert PROGRAM_STATUS_REPORT_PAGE.get_coaching_effectiveness_text() == "COACHING EFFECTIVENESS"
    assert PROGRAM_STATUS_REPORT_PAGE.get_program_effectiveness_text() == "PROGRAM EFFECTIVENESS"


# LQ-372
@when('the user clicks "INSIGHTS" and the user clicks "BEHAVIORS REPORT" in Behaviors Report page')
def behaviors_report_tab():
    FLEET_TELEMATICS_PAGE.click_behaviors_report_submenu()


@then('the number of behaviors is displayed and  the table is displayed with columns "BEHAVIOR", '
      '"FREQUENCY", "TREND" in Behaviors Report page')
def verify_behave_table():
    assert BEHAVIORS_REPORT_PAGE.get_behavior_text() == "BEHAVIOR"
    assert BEHAVIORS_REPORT_PAGE.get_frequency_text() == "FREQUENCY"
    assert BEHAVIORS_REPORT_PAGE.get_trend_text() == "TREND"


# LQ-263
@when('the user clicks "LIBRARY" and then clicks "EVENTS"')
def navigate_to_events_page():
    FLEET_TELEMATICS_PAGE.click_library_menu()
    FLEET_TELEMATICS_PAGE.click_events_submenu()


@then('the events page is displayed and the table is displayed with columns "EVENT ID",'
      '"DRIVER","GROUP","VEHICLE","EVENT DATE","SCORE","STATUS","TRIGGER" and "BEHAVIORS"')
def verify_events_table():
    assert LIBRARY_PAGE.get_event_id() == "EVENT ID"
    assert LIBRARY_PAGE.get_driver() == "DRIVER"
    assert LIBRARY_PAGE.get_group() == "GROUP"
    assert LIBRARY_PAGE.get_vehicle() == "VEHICLE"
    assert LIBRARY_PAGE.get_device() == "DEVICE"
    assert LIBRARY_PAGE.get_event_date() == "EVENT DATE"
    assert LIBRARY_PAGE.get_score() == "SCORE"
    assert LIBRARY_PAGE.get_status() == "STATUS"
    assert LIBRARY_PAGE.get_trigger() == "TRIGGER"
    assert LIBRARY_PAGE.get_behaviors(), contains_string("BEHAVIORS")


# LQ-400
@when('the user clicks "LIBRARY" and then clicks "COACHING HISTORY"')
def navigate_to_coaching_history():
    FLEET_TELEMATICS_PAGE.click_coachinghistory_submenu()


@then(
    'the Coaching History page is displayed and the table is displayed with columns "SESSION ID", "COACH DATE", "OVERDUE DATE", "DRIVER","BEHAVIORS COACHED","GROUP","COACH","NOTES" and the coaching sessions count is displayed')
def verify_coaching_history_displayed():
    assert LIBRARY_PAGE.get_sessions_label_new_UI() == "Sessions"
    assert LIBRARY_PAGE.get_session_id_label() == "SESSION ID"
    assert LIBRARY_PAGE.get_coach_date_label() == "COACH DATE"


# LQ-391
@when('the user clicks "LIBRARY" and the user clicks "RECOGNITION HISTORY"')
def navigate_to_coaching_history():
    global LOGIN_PAGE, DASHBOARD_PAGE, LIBRARY_PAGE, LD
    FLEET_TELEMATICS_PAGE.click_library_menu()
    FLEET_TELEMATICS_PAGE.click_recognitionhistory_submenu()


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
    FLEET_TELEMATICS_PAGE.click_dataexport_submenu()


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
    DASHBOARD_PAGE.close_pendo_dialog()
    assert FLEET_TELEMATICS_CENTER_PAGE.users_header_is_displayed()
    assert USER_MANAGEMENT_PAGE.get_user_management_label() == "USER MANAGEMENT"
    assert USER_MANAGEMENT_PAGE.get_name_label() == "NAME"
    assert USER_MANAGEMENT_PAGE.get_employee_id_label() == "EMPLOYEE ID"
    # assert USER_MANAGEMENT_PAGE.get_lytx_badge_label() == "LYTX BADGE"


# LQ-254
@when('the "Full Access" user is in the Edit User page')
def open_edit_user_page():
    USER_MANAGEMENT_PAGE.click_first_user()


@then('Edit user page displayed')
def edit_user_page_displayed():
    EDIT_USER_PAGE.edit_user_title_is_displayed()


# LQ-236
@when('the user clicks the "VEHICLES" tab')
def user_clicks_vehicles_tab():
    USER_MANAGEMENT_PAGE.click_vehicle_tab()


@then(
    'the page header "VEHICLE MANAGEMENT" and the vehicle count are displayed and the table is displayed with columns: "VEHICLE", "GROUP", "DRIVER", "DEVICE", "LAST CHECK IN", "STATUS"')
def verify_column_headers():
    assert VEHICLE_MANAGEMENT_PAGE.get_vehicle_page_title_text() == "VEHICLE MANAGEMENT"

    assert VEHICLE_MANAGEMENT_PAGE.get_vehicle_column_text() == "VEHICLE"
    assert VEHICLE_MANAGEMENT_PAGE.get_group_column_text() == "GROUP"
    assert VEHICLE_MANAGEMENT_PAGE.get_driver_column_text() == "DRIVER"
    assert_that(VEHICLE_MANAGEMENT_PAGE.get_device_column_text(), contains_string("DEVICE"))
    assert VEHICLE_MANAGEMENT_PAGE.get_last_connected_column_text() == "LAST CHECK IN"
    assert VEHICLE_MANAGEMENT_PAGE.get_status_column_text() == "STATUS"


# LQ-239
@when('the user clicks on "Add Vehicle"')
def user_clicks_add_vehicle_tab():
    VEHICLE_MANAGEMENT_PAGE.click_add_vehicle_button()


@then('the Add vehicle page is displayed')
def add_vehicle_page_is_displayed():
    assert ADD_VEHICLE_PAGE.add_vehicle_page_displayed() is True
    assert ADD_VEHICLE_PAGE.add_group_button_displayed() is True


# LQ-230
@when('the user clicks the "DEVICES" tab')
def navigate_to_device_management_page():
    USER_MANAGEMENT_PAGE.click_devices_tab()


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


# LQ-4456
@when('the user clicks a device link')
def navigate_to_device_profile_page():
    DEVICE_PROFILE_PAGE.click_device_serial_number()


@then('the "DEVICE PROFILE" page is opened')
def verify_device_profile_page():
    assert DEVICE_PROFILE_PAGE.get_device_profile_title() == 'DEVICE PROFILE'
    assert DEVICE_PROFILE_PAGE.get_device_profile_summary_device() == 'Device'


# LQ-3557
@when('the user clicks "GEOFENCES"')
def navigate_to_geofences():
    USER_MANAGEMENT_PAGE.click_geofences_tab()


@then(
    'the page header "GEOFENCE MANAGEMENT" and geofence count are displayed and the table is displayed with columns: "GEOFENCE", "GROUP", "RECENT ACTIVITY", "STATUS", "ASSETS", "TRIGGER TYPE", "CREATED DATE", "SOURCE"')
def verify_geofence_page():
    sleep(5)
    assert GEOFENCE_MANAGEMENT_PAGE.get_geofence_page_title() == "GEOFENCE MANAGEMENT"
    assert GEOFENCE_MANAGEMENT_PAGE.get_geofence_column_text() == "GEOFENCE"
    assert GEOFENCE_MANAGEMENT_PAGE.get_group_column_text() == "GROUP"
    assert GEOFENCE_MANAGEMENT_PAGE.get_recent_activity_column_text() == "RECENT ACTIVITY"
    assert GEOFENCE_MANAGEMENT_PAGE.get_status_column_text() == "STATUS"
    assert GEOFENCE_MANAGEMENT_PAGE.get_assets_column_text() == "ASSETS"
    assert GEOFENCE_MANAGEMENT_PAGE.get_trigger_type_column_text() == "TRIGGER TYPE"
    assert GEOFENCE_MANAGEMENT_PAGE.get_created_date_column_text() == "CREATED DATE"
    assert GEOFENCE_MANAGEMENT_PAGE.get_source_column_text() == "SOURCE"


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


# LQ-242
@when('the user clicks CONFIG SETTING')
def navigate_to_config_setting_page():
    USER_MANAGEMENT_PAGE.click_config_setting_tab()


@then('Full access role is in tier 1 by default')
def verify_tier_1_full_access_role():
    assert CONFIGURATION_SETTING_PAGE.get_config_setting_page_title(), IsEqualIgnoringCase("Configuration Settings")


# LQ-7126
@when('the user clicks the "EQUIPMENT" tab')
def navigate_to_equipment_management_page():
    EQUIPMENT_MANAGEMENT_PAGE.click_equipment()


@then(
    'the page header "EQUIPMENT MANAGEMENT" is displayed and the table is displayed with columns: "EQUIPMENT", "DEVICE", "GROUP", "LAST CONNECTED", "STATUS"')
def verify_user_management_tabs():
    assert EQUIPMENT_MANAGEMENT_PAGE.get_equipment_management_title_text() == "EQUIPMENT MANAGEMENT"
    assert EQUIPMENT_MANAGEMENT_PAGE.get_equipment_column_name_text() == "EQUIPMENT"
    assert EQUIPMENT_MANAGEMENT_PAGE.get_device_column_name_text() == "DEVICE"
    assert EQUIPMENT_MANAGEMENT_PAGE.get_group_column_name_text() == "GROUP"
    assert EQUIPMENT_MANAGEMENT_PAGE.get_last_connected_column_name_text() == "LAST CONNECTED"
    assert EQUIPMENT_MANAGEMENT_PAGE.get_status_column_name_text() == "STATUS"


@when('the user click on the "Consent Report" module')
def user_clicks_consent_report_tab():
    USER_MANAGEMENT_PAGE.click_insights_tab()
    CONSENT_REPORT_PAGE.click_consent_report_tab()


@then('the user should see all the filter like "All Available Groups", "Status", "Search Name or ID" and "Reset"')
def user_should_see_all_filters():
    assert CONSENT_REPORT_PAGE.group_filter_is_displayed() is True
    assert CONSENT_REPORT_PAGE.status_filter_is_displayed() is True
    assert CONSENT_REPORT_PAGE.search_name_or_id_is_displayed() is True
    assert CONSENT_REPORT_PAGE.reset_button_is_displayed() is True


@then('the user should see the count of Drivers with tabs named "Facial ID", "Video Safety" and "Distraction and '
      'Fatigue Detection"')
def user_should_see_count_and_all_tabs():
    assert CONSENT_REPORT_PAGE.driver_count_is_displayed() is True
    assert CONSENT_REPORT_PAGE.facial_id_tab_is_displayed() is True


# @LQ-157939
# @when('the user is in "Facial ID" product tab') # This step is not needed as this step is covered in LQ-136386


@then('the user should see the title "Consent Report" and the user should see the columns "NAME","GROUPS","STATUS", '
      '"SENT DATE" and "REQUESTED DATE"')
def user_should_see_all_columns():
    assert CONSENT_REPORT_PAGE.get_page_title() == "CONSENT REPORT"
    assert CONSENT_REPORT_PAGE.get_name_column_label() == "NAME"
    assert CONSENT_REPORT_PAGE.get_groups_column_label() == "GROUPS"
    assert CONSENT_REPORT_PAGE.get_status_column_label() == "STATUS"
    assert CONSENT_REPORT_PAGE.get_sent_date_column_label() == "SENT DATE"
    assert CONSENT_REPORT_PAGE.get_received_date_column_label() == "RECEIVED DATE"


@then('the user see the options "0 selected","Clear All","Download PDF", "Revoke Consent" and "CSV"')
def user_should_see_all_options():
    assert CONSENT_REPORT_PAGE.clear_all_option_is_displayed() is True
    #Buttons were removed for now since they didn't work and no customer was using them
    # assert CONSENT_REPORT_PAGE.download_pdf_option_is_displayed() is True
    # assert CONSENT_REPORT_PAGE.revoke_consent_option_is_displayed() is True
    assert CONSENT_REPORT_PAGE.csv_option_is_displayed() is True


@when('the user clicks DVIR')
def go_to_DVIR_page():
    DASHBOARD_PAGE.click_dvir_tab()


@then(
    'Total reports count, reset button, group filter, date filter, status filter, defect filter and wild search filter are shown on "DRIVER VEHICLE INSPECTION REPORTS" page and table columns are: "REPORT ID", "TYPE", "STATUS", "REPORT DATE", "DRIVER", "VEHICLE", "MAJOR VEHICLE DEFECTS", "MINOR VEHICLE DEFECTS", "VEHICLE INSPECTION LIST", "TRAILER", "MAJOR TRAILER DEFECTS", "MINOR TRAILER DEFECTS", "TRAILER INSPECTION LIST", "MECHANIC/AGENT", "REVIEWER"')
def verify_driver_vehicle_inspection_report_page():
    # assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_total_report_title() == "Reports"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_groups_filter_title() == "Select Group(s)"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_date_range_filter_title() == "Select Date Range"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_statuses_filter_title() == "Status"
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


@then(
    'the page header "INSPECTION SCHEDULES" is displayed & the count of the vehicle schedule report is displayed & the table is displayed with columns')
def verify_inspection_schedules_table():
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_schedules_title() == "INSPECTION SCHEDULES"
    assert_that(INSPECTION_SCHEDULES_PAGE.get_reports_title(), contains_string("Report"))
    assert INSPECTION_SCHEDULES_PAGE.get_vehicle_name_title() == "VEHICLE NAME"
    assert INSPECTION_SCHEDULES_PAGE.get_vehicle_group_title() == "VEHICLE GROUP"
    assert INSPECTION_SCHEDULES_PAGE.get_status_title() == "STATUS"
    assert INSPECTION_SCHEDULES_PAGE.get_due_date_title() == "DUE DATE"
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_list_title() == "INSPECTION LIST"
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_frequency_title() == "INSPECTION FREQUENCY"
    assert INSPECTION_SCHEDULES_PAGE.get_last_inspected_date_title() == "LAST INSPECTED DATE"
    assert INSPECTION_SCHEDULES_PAGE.get_last_inspected_driver_title() == "LAST INSPECTED DRIVER"


# LQ-12461
@when('user clicks "SCHEDULE" on left navigation & user clicks "Trailer Schedule"')
def navigate_to_trailer_schedule_tab():
    INSPECTION_SCHEDULES_PAGE.click_trailer_schedules_link()


@then(
    'the page header "INSPECTION SCHEDULES" is displayed & the count of the trailer schedule report is displayed & the table is displayed with columns')
def verify_trailer_schedule_table():
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_schedules_title() == "INSPECTION SCHEDULES"
    assert INSPECTION_SCHEDULES_PAGE.get_trailer_reports_title() == "Reports"
    assert INSPECTION_SCHEDULES_PAGE.get_trailer_name_column_text() == "TRAILER NAME"
    assert INSPECTION_SCHEDULES_PAGE.get_trailer_group_column_text() == "TRAILER GROUP"
    assert INSPECTION_SCHEDULES_PAGE.get_status_column_text() == "STATUS"
    assert INSPECTION_SCHEDULES_PAGE.get_due_date_column_text() == "DUE DATE"
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_list_column_text() == "INSPECTION LIST"
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_frequency_column_text() == "INSPECTION FREQUENCY"
    assert INSPECTION_SCHEDULES_PAGE.get_last_inspected_date_column_text() == "LAST INSPECTED DATE"
    assert INSPECTION_SCHEDULES_PAGE.get_last_inspected_driver_column_text() == "LAST INSPECTED DRIVER"


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


# @LQ-12447
@when('the "Full Access" user is in the Trailer list page')
def navigate_to_trailer_list():
    INSPECTION_LIST_MANAGEMENT_PAGE.click_trailer_list_link()


@then(
    'the title "TRAILER INSPECTION LISTS" is displayed & there is a default trailer inspection list and named "Default" & there is a duplicate icon behind the list name')
def verify_trailer_inspection_list():
    assert INSPECTION_LIST_MANAGEMENT_PAGE.get_trailer_inspection_lists_title() == "TRAILER INSPECTION LISTS"
    assert INSPECTION_LIST_MANAGEMENT_PAGE.get_default_inspection_lists_title() == "Default"
    assert INSPECTION_LIST_MANAGEMENT_PAGE.trailer_duplicate_icon_displayed() is True


# LQ-12430
@when('the user clicks the "List Settings" tab & the user clicks "List Assignment"')
def navigate_to_list_assignment():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_list_assignment_tab()


@then(
    'the page header "INSPECTION LIST ASSIGNMENT" is displayed & the vehicle count is displayed & the table is displayed with columns: "VEHICLE", "GROUP", "VEHICLE TYPE" and "INSPECTION LIST"')
def verify_inspection_list_assignment_page():
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_assignment_title() == "INSPECTION LIST ASSIGNMENT"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_vehicle_count_title() == "Vehicles"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_vehicle_table_title() == "VEHICLE"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_group_table_title() == "GROUP"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_vehicle_type_table_title() == "VEHICLE TYPE"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_table_title() == "INSPECTION LIST"


# LQ-12433
@when('the user clicks the "Trailer Assignment" tab')
def navigate_to_trailer_list_assignment_page():
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_trailer_assignment_tab()


@then(
    'the page header "INSPECTION LIST ASSIGNMENT" is displayed & the trailer count is displayed & the table is displayed with columns: "TRAILER", "GROUP", "TRAILER TYPE" and "INSPECTION LIST"')
def verify_trailer_assignment_titles():
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_assignment_title() == "INSPECTION LIST ASSIGNMENT"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_trailers_count() == "Trailers"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_trailer_column() == "TRAILER"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_group_title() == "GROUP"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_trailer_type_title() == "TRAILER TYPE"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_column_title() == "INSPECTION LIST"


@when('the user clicks on Map')
def login():
    DASHBOARD_PAGE.click_fleet_tracking_tab()

@then('the Fleet application is displayed')
def assert_fleet_app():
    assert FLEET_MAP_PAGE.map_tab_is_displayed_new_UI() is True
    FLEET_MAP_PAGE.click_map_new_ui()
    assert FLEET_MAP_PAGE.get_settings_tab_text() == "SETTINGS"


@when('the user navigates to Maintenance -> Preventative Maintenance')
def go_to_fleet_maint_pm():
    FLEET_MAINT_PAGE.click_maintenance_new_ui()
    FLEET_MAINT_PAGE.click_preventative_maintenance_new_ui()


@then('the Preventative Main labels are shown - Upcoming Services, History & Manage Services')
def assert_preventative_maintenance():
    assert FLEET_MAINT_PAGE.get_preventative_maintenance_title() == "PREVENTATIVE MAINTENANCE"
    assert FLEET_MAINT_PAGE.get_upcoming_services_tab_title() == "Upcoming Services"
    assert FLEET_MAINT_PAGE.get_history_tab_title() == "History"
    assert FLEET_MAINT_PAGE.get_manage_services_title() == "Manage Services"


@when('the user clicks "History"')
def click_history_tab():
    FLEET_MAINT_PAGE.click_history_tab()


@then(
    'the table is displayed with columns: "VEHICLE", "GROUP", "SERVICE", "INTERVAL", "DATE SERVICED", "ODOMETER", "ENGINE HOURS", "NOTES", "ACTION" & the number of Services is displayed')
def assert_history_page():
    assert FLEET_MAINT_PAGE.get_vehicle_preventative_maintenance() == "VEHICLE"
    assert FLEET_MAINT_PAGE.get_group_preventative_maintenance() == "GROUP"
    assert FLEET_MAINT_PAGE.get_service_preventative_maintenance() == "SERVICE"
    assert FLEET_MAINT_PAGE.get_interval_preventative_maintenance() == "INTERVAL"
    assert FLEET_MAINT_PAGE.get_date_serviced_preventative_maintenance() == "DATE SERVICED"
    assert FLEET_MAINT_PAGE.get_odometer_preventative_maintenance() == "ODOMETER"
    assert FLEET_MAINT_PAGE.get_engine_hours_preventative_maintenance() == "ENGINE HOURS"
    assert FLEET_MAINT_PAGE.get_notes_preventative_maintenance() == "NOTES"
    assert FLEET_MAINT_PAGE.get_action_preventative_maintenance() == "ACTION"


# LQ-527
@when('the user clicks "Manage Services"')
def click_manage_services_tab():
    FLEET_MAINT_PAGE.click_manage_services()


@then('the Manage Services page is displayed')
def assert_manage_services_page():
    assert FLEET_MAINT_PAGE.get_manage_service_services_count() is True


# LQ-531
@when('the user navigates to Maintenance -> Diagnostic Trouble Codes')
def click_dtc():
    FLEET_MAINT_PAGE.click_dtc_new_ui()


@then(
    'the DTC page is displayed and the number of Codes, group filter and reset icon are displayed on the header bar and the table is displayed with columns: "VEHICLE", "GROUP", "DATE", "CODE (DESCRIPTION)"')
def assert_dtc():
    assert FLEET_MAINT_PAGE.get_dtc_title() == "DIAGNOSTIC TROUBLE CODES"
    assert FLEET_MAINT_PAGE.group_filter_displayed_dtc_page() is True
    assert FLEET_MAINT_PAGE.get_vehicle_column_text_dtc_page() == "VEHICLE"
    assert FLEET_MAINT_PAGE.get_group_column_text_dtc_page() == "GROUP"
    assert FLEET_MAINT_PAGE.get_date_column_text_dtc_page() == "DATE"
    assert FLEET_MAINT_PAGE.get_code_column_text_dtc_page() == "CODE (DESCRIPTION)"


# LQ-544
@when('the user navigates to Insights -> Fleet Operations')
def go_to_fleet_operations():
    FLEET_INSIGHT_PAGE.click_insights_new_ui()
    FLEET_INSIGHT_PAGE.click_fleet_operations_new_ui()


@then('the groups tab of Fleet Operations page is displayed')
def assert_fleet_operations_groups_tab():
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_title() == "FLEET OPERATIONS"
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_groups_tab() == "Groups"


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
    assert FLEET_INSIGHT_PAGE.get_idle_violations_text_driver_profile() == "IDLE OVERAGE"
    assert FLEET_INSIGHT_PAGE.get_idle_duration_text_driver_profile() == "IDLE VIOLATIONS DURATION"
    assert FLEET_INSIGHT_PAGE.get_speed_violation_text_driver_profile() == "SPEED VIOLATIONS"
    assert FLEET_INSIGHT_PAGE.get_speeding_duration_text_driver_profile() == "SPEED VIOLATIONS DURATION"


# LQ-547
@when('the user clicks Vehicles in Fleet Operations page')
def click_fleet_operations_vehicles():
    FLEET_INSIGHT_PAGE.click_insights_new_ui()
    FLEET_INSIGHT_PAGE.click_fleet_operations_new_ui()
    FLEET_INSIGHT_PAGE.click_fleet_operations_vehicles()


@then('the vehicles tab of Fleet Operations page is displayed')
def assert_fleet_operations_vehicles_tab():
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_vehicles_tab() == "Vehicles"


# LQ-545
@when('the user inputs some characters in Search Vehicles box')
def search_vehicle_vehicle_profile():
    FLEET_INSIGHT_PAGE.search_vehicle_vehicle_profile(FID.vehicle)


@when('the user selects one vehicle')
def select_vehicle_vehicle_profile():
    FLEET_INSIGHT_PAGE.select_vehicle_profile(FID.vehicle)


@then('the vehicle profile page is displayed')
def assert_fleet_operations_vehicle_profile():
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_vehicle_profile() == "VEHICLE PROFILE"


# @LQ-550
@when('the user clicks "INSIGHTS" and the user clicks "FLEET DATA"')
def click_fleet_data():
    FLEET_INSIGHT_PAGE.click_insights_new_ui()
    FLEET_INSIGHT_PAGE.click_fleet_data_new_ui()


@then('the metrics is displayed with columns: "AVERAGE", "TOTAL"')
def assert_metrics_column():
    assert FLEET_INSIGHT_PAGE.get_average_text() == "AVERAGE"
    assert FLEET_INSIGHT_PAGE.get_total_text() == "TOTAL"


@then('the metrics is displayed with values: "DISTANCE", "ENGINE HOURS", "DRIVING HOURS", '
      '"IDLE TIME", "IDLE PTO TIME", "FUEL CONSUMED", "DRIVING FUEL", "IDLING FUEL", "PTO IDLING FUEL", '
      '"FUEL ECONOMY", "DRIVING FUEL ECONOMY"')
def assert_metrics_detail():
    assert "DISTANCE" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "ENGINE HOURS" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "DRIVING HOURS" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "IDLE TIME" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "IDLE PTO TIME" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "FUEL CONSUMED" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "DRIVING FUEL" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "IDLING FUEL" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "PTO IDLING FUEL" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "FUEL ECONOMY" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "DRIVING FUEL ECONOMY" in FLEET_INSIGHT_PAGE.get_metric_detail_text()


@when('the user clicks "GROUP" tab')
def click_group_tab():
    FLEET_INSIGHT_PAGE.click_group_tab()


@then(
    'the table is displayed with columns: "GROUP", "DISTANCE, "ENGINE HOURS, "DRIVING HOURS", "IDLE TIME", "IDLE PTO TIME", "FUEL CONSUMED", "DRIVING FUEL", "IDLING FUEL", "PTO IDLING FUEL", "FUEL ECONOMY", "DRIVING FUEL ECONOMY"')
def assert_group_tab_table():
    assert FLEET_INSIGHT_PAGE.get_groups_text() == "GROUP"
    assert FLEET_INSIGHT_PAGE.get_distance_text() == "DISTANCE"
    assert FLEET_INSIGHT_PAGE.get_engine_hours_text() == "ENGINE HOURS"
    assert FLEET_INSIGHT_PAGE.get_driving_hours_text() == "DRIVING HOURS"
    assert FLEET_INSIGHT_PAGE.get_idle_time_text() == "IDLE TIME"
    assert FLEET_INSIGHT_PAGE.get_idle_pto_time_text() == "IDLE PTO TIME"
    assert FLEET_INSIGHT_PAGE.get_fuel_consumed_text() == "FUEL CONSUMED"
    assert FLEET_INSIGHT_PAGE.get_driving_fuel_text() == "DRIVING FUEL"
    assert FLEET_INSIGHT_PAGE.get_idling_fuel_text() == "IDLING FUEL"
    assert FLEET_INSIGHT_PAGE.get_pto_idling_fuel_text() == "PTO IDLING FUEL"
    assert FLEET_INSIGHT_PAGE.get_fuel_economy_text() == "FUEL ECONOMY"
    assert FLEET_INSIGHT_PAGE.get_driving_fuel_economy_text() == "DRIVING FUEL ECONOMY"


@when('the user clicks "VEHICLE" tab')
def click_vehicle_tab():
    FLEET_INSIGHT_PAGE.click_vehicle_tab()


@then(
    'the table is displayed with columns: "VEHICLE", "ODOMETER READING", "DISTANCE", "ENGINE HOURS", '
    '"DRIVING HOURS, "IDLE TIME", "IDLE PTO TIME", "FUEL CONSUMED", "DRIVING FUEL", "IDLING FUEL", "PTO IDLING FUEL", '
    '"FUEL ECONOMY", "DRIVING FUEL ECONOMY"')
def assert_vehicle_tab_table():
    assert FLEET_INSIGHT_PAGE.get_vehicle_text() == "VEHICLE"
    assert FLEET_INSIGHT_PAGE.get_vehicle_odometer_reading_text() == "ODOMETER READING"
    assert FLEET_INSIGHT_PAGE.get_vehicle_distance_text() == "DISTANCE"
    assert FLEET_INSIGHT_PAGE.get_vehicle_engine_hours_text() == "ENGINE HOURS"
    assert FLEET_INSIGHT_PAGE.get_vehicle_driving_hours_text() == "DRIVING HOURS"
    assert FLEET_INSIGHT_PAGE.get_vehicle_idle_time_text() == "IDLE TIME"
    assert FLEET_INSIGHT_PAGE.get_vehicle_idle_pto_time_text() == "IDLE PTO TIME"
    assert FLEET_INSIGHT_PAGE.get_vehicle_fuel_consumed_text() == "FUEL CONSUMED"
    assert FLEET_INSIGHT_PAGE.get_vehicle_driving_fuel_text() == "DRIVING FUEL"
    assert FLEET_INSIGHT_PAGE.get_vehicle_idling_fuel_text() == "IDLING FUEL"
    assert FLEET_INSIGHT_PAGE.get_vehicle_pto_idling_fuel_text() == "PTO IDLING FUEL"
    assert FLEET_INSIGHT_PAGE.get_vehicle_fuel_economy_text() == "FUEL ECONOMY"
    assert FLEET_INSIGHT_PAGE.get_vehicle_driving_fuel_economy_text() == "DRIVING FUEL ECONOMY"


# LQ-7134
@when('the user clicks "INSIGHTS" and then clicks "EQUIPMENT STATUS"')
def click_equipment_status():
    FLEET_INSIGHT_PAGE.click_equipment_status_new_ui()


@then(
    'the table is displayed with columns: "EQUIPMENT", "GROUP", "DEVICE SERIAL NUMBER", "LAST LOCATION", '
    '"LAST CONNECTED", "LAST MOVEMENT", "STATIONARY DURATION", "BATTERY LEVEL"')
def assert_insights_equipment_status():
    assert FLEET_INSIGHT_PAGE.get_equipment_status_title() == "EQUIPMENT STATUS"
    assert FLEET_INSIGHT_PAGE.get_equipment_text() == "EQUIPMENT"
    assert FLEET_INSIGHT_PAGE.get_equipment_group_text() == "GROUP"
    assert FLEET_INSIGHT_PAGE.get_equipment_device_text() == "DEVICE SERIAL #"
    assert FLEET_INSIGHT_PAGE.get_equipment_last_location_text() == "LAST LOCATION"
    assert FLEET_INSIGHT_PAGE.get_equipment_last_connected_text() == "LAST CONNECTED"
    assert FLEET_INSIGHT_PAGE.get_equipment_last_movement_text() == "LAST MOVEMENT"
    assert FLEET_INSIGHT_PAGE.get_equipment_stationary_text() == "STATIONARY DURATION"
    assert FLEET_INSIGHT_PAGE.get_equipment_battery_text() == "BATTERY LEVEL"


# LQ-519
@when('the user navigates to Insights -> Geofences')
def click_geofences():
    FLEET_INSIGHT_PAGE.click_geofences()


@then('the Geofences page is displayed')
def assert_geofences():
    assert FLEET_INSIGHT_PAGE.get_geofences_title() == "GEOFENCES"


# LQ-562
@when('the user clicks a geofence or search and select a geofence to go to geofence profile page')
def go_to_geofence_profile():
    FLEET_INSIGHT_PAGE.search_geofence_geofences(FID.geofence)
    FLEET_INSIGHT_PAGE.select_1st_geofence_geofences(FID.geofence)


@then(
    'the metadata bar is displayed with labels: "GEOFENCE NAME", "DATE CREATED", "DAYS APPLIED", "RANGE OF TIME", "Trigger Type", "GROUP", "SUBGROUPS", "VEHICLES"')
def assert_metadata_bar_geofence_profile():
    assert FLEET_INSIGHT_PAGE.get_geofence_profile_metadata_name() == "GEOFENCE NAME"
    assert FLEET_INSIGHT_PAGE.geofence_profile_metadata_date_created() == "DATE CREATED"
    assert FLEET_INSIGHT_PAGE.geofence_profile_metadata_days_applied() == "DAYS APPLIED"
    assert FLEET_INSIGHT_PAGE.geofence_profile_metadata_time() == "RANGE OF TIME"
    assert FLEET_INSIGHT_PAGE.geofence_profile_metadata_type() == "Trigger Type"
    assert FLEET_INSIGHT_PAGE.geofence_profile_metadata_group() == "GROUP"
    assert FLEET_INSIGHT_PAGE.geofence_profile_metadata_subgroup() == "SUBGROUPS"
    assert FLEET_INSIGHT_PAGE.geofence_profile_metadata_vehicles() == "VEHICLES"


# LQ-514
@when('the user navigates to Insights -> State Mileage')
def click_state_mileage():
    FLEET_INSIGHT_PAGE.click_insights_new_ui()
    FLEET_INSIGHT_PAGE.click_state_mileage_new_ui()


@then(
    'the State Mileage page is displayed and the table is displayed with columns: "VEHICLE", "GROUP", "DEVICE SERIAL", "STATE,COUNTRY", "DISTANCE" and the number of records is displayed')
def assert_state_mileage():
    assert FLEET_INSIGHT_PAGE.get_state_mileage_title() == "STATE MILEAGE"
    assert FLEET_INSIGHT_PAGE.get_vehicle_column_text_state_mileage() == "VEHICLE"
    assert FLEET_INSIGHT_PAGE.get_group_column_text_state_mileage() == "GROUP"
    assert FLEET_INSIGHT_PAGE.get_device_serial_column_text_state_mileage() == "DEVICE SERIAL #"
    assert FLEET_INSIGHT_PAGE.get_state_country_column_text_state_mileage() == "STATE, COUNTRY"
    assert FLEET_INSIGHT_PAGE.get_distance_column_text_state_mileage() == "DISTANCE"


@when('the user clicks "INSIGHTS" and the user clicks "STATE MILEAGE"')
# do nothing due to state mileage is opened already

@then('the summary contains "METRICS", "TOTAL", "TOTAL DISTANCE", distance for each state')
def assert_summary_state_mileage():
    assert FLEET_INSIGHT_PAGE.get_metrics_text_state_mileage() == "METRICS"
    assert FLEET_INSIGHT_PAGE.get_total_distance_text_state_mileage() == "TOTAL DISTANCE"
    assert FLEET_INSIGHT_PAGE.get_total_text_state_mileage() == "TOTAL"


# LQ-457
@when('the user clicks "INSIGHTS" and the user selects "DATA EXPORT')
def click_data_export():
    FLEET_INSIGHT_PAGE.click_data_export_new_ui()


@then('there are group, date, vehicle filters and the table is displayed with columns '
      '"ACTION", "REPORT TYPE", "GROUP", "START DATE", "END DATE", "VEHICLE", "REQUESTED DATE')
def assert_data_export():
    assert FLEET_INSIGHT_PAGE.get_data_export_title() == "DATA EXPORT"
    assert FLEET_INSIGHT_PAGE.get_action_label() == "ACTION"
    assert FLEET_INSIGHT_PAGE.get_report_type_label() == "REPORT TYPE"
    assert FLEET_INSIGHT_PAGE.get_group_label() == "GROUP"
    assert FLEET_INSIGHT_PAGE.get_start_date_label() == "START DATE"
    assert FLEET_INSIGHT_PAGE.get_end_date_label() == "END DATE"
    assert FLEET_INSIGHT_PAGE.get_vehicle_label() == "VEHICLE"
    assert FLEET_INSIGHT_PAGE.get_requested_date_label() == "REQUESTED DATE"


@then(
    'the summary section is displayed with labels: "TOTAL TRIGGERS", "TOTAL DURATION", "TOTAL VEHICLES", "DRIVING TIME IN GEOFENCES", "IDLE TIME IN GEOFENCES", "STOP TIME IN GEOFENCES"')
def assert_summary_section_geofence_profile():
    assert FLEET_INSIGHT_PAGE.geofence_profile_detail_triggers() == FID.triggers_detail_count


@when('user enters username and password and hits SignIn button')
def login_to_video_search():
    DASHBOARD_PAGE.click_video_search_tab()


@then('the user is successfully logged into the Video Search page')
def verify_login():
    assert VIDEO_SEARCH_PAGE.get_video_search_title() == "Video Search"


# LQ-205
@when('the Video Reviewer Plus user is in Video Search page')
def go_to_video_search_page():
    VIDEO_SEARCH_PAGE.click_vehicle_tab_new()


@then(
    'the vehicle count is displayed and the table is displayed with columns: "ACTIONS", "VEHICLES", "DEVICE", "LAST COMMUNICATED", "GROUP", "VIEWS"')
def verify_table_vehicle_page():
    assert VIDEO_SEARCH_PAGE.video_tag_count_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.get_actions_column_text() == "ACTIONS"
    assert VIDEO_SEARCH_PAGE.get_vehicles_column_text() == "VEHICLES"
    assert VIDEO_SEARCH_PAGE.get_device_column_text() == "DEVICE"
    assert VIDEO_SEARCH_PAGE.get_last_communicated_column_text() == "LAST COMMUNICATED"
    assert VIDEO_SEARCH_PAGE.get_group_column_text() == "GROUP"
    assert VIDEO_SEARCH_PAGE.get_views_column_text() == "VIEWS"


# LQ-207
@when('the user clicks on the Library and the user selects Saved Videos')
def go_to_saved_videos_page():
    VIDEO_SEARCH_PAGE.click_library_tab_new()
    VIDEO_SEARCH_PAGE.click_saved_videos_tab_new()


@then(
    'the video count is displayed and the table is displayed with columns: "VIDEO NAME","STATUS","TAG TYPE","VEHICLE","GROUP","LENGTH","VIEWS","VIDEO DATE","REQUEST DATE"')
def verify_table_saved_videos_page():
    assert VIDEO_SEARCH_PAGE.get_video_name_column_text() == "VIDEO NAME"
    assert VIDEO_SEARCH_PAGE.get_status_column_text() == "STATUS"
    assert VIDEO_SEARCH_PAGE.get_tag_type_column_text() == "TAG TYPE"
    assert VIDEO_SEARCH_PAGE.get_vehicle_column_saved_videos_text() == "VEHICLE"
    assert VIDEO_SEARCH_PAGE.get_group_column_saved_videos_text() == "GROUP"
    assert VIDEO_SEARCH_PAGE.get_length_column_text() == "LENGTH"
    assert VIDEO_SEARCH_PAGE.get_views_column_saved_videos_text() == "VIEWS"
    assert VIDEO_SEARCH_PAGE.get_video_date_column_text() == "VIDEO DATE"
    assert VIDEO_SEARCH_PAGE.get_request_date_column_text() == "REQUEST DATE"


# LQ-10128
@when('the user clicks on the Library and the user selects Video Tags')
def go_to_video_tags_page():
    VIDEO_SEARCH_PAGE.click_video_tags_tab_new()


@then(
    'the video tag count is displayed and the table is displayed with columns: "ACTIONS","VEHICLE","TAG NAME","CATEGORY","AVAILABLE VIEWS","GROUP","RECORD DATE"')
def verify_table_video_tags_page():
    assert VIDEO_SEARCH_PAGE.get_vehicle_count_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.get_actions_column_video_tags_text() == "ACTIONS"
    assert VIDEO_SEARCH_PAGE.get_vehicle_column_video_tags_text() == "VEHICLE"
    assert VIDEO_SEARCH_PAGE.get_tag_name_column_text() == "TAG NAME"
    assert VIDEO_SEARCH_PAGE.get_category_column_text() == "CATEGORY"
    assert VIDEO_SEARCH_PAGE.get_available_views_column_text() == "AVAILABLE VIEWS"
    assert VIDEO_SEARCH_PAGE.get_group_column_video_tags_text() == "GROUP"
    assert VIDEO_SEARCH_PAGE.get_record_date_column_text() == "RECORD DATE"


# lQ-204
@when('user clicks on "Browse" from the ACTIONS for one vehicle')
def click_browse_button(context):
    context['live_present'] = VIDEO_SEARCH_PAGE.click_browse_button()


@then('user is navigated to "Browser" in VIDEO BROWSER page')
def assert_browse_button(context):
    assert VIDEO_SEARCH_PAGE.get_video_browser_title("VIDEO BROWSER") == "VIDEO BROWSER"
    if context['live_present']:
        assert VIDEO_SEARCH_PAGE.browser_tab_is_active() is True
        assert VIDEO_SEARCH_PAGE.live_tab_is_active() is False


@when('user clicks on "Live" from the ACTIONS for one vehicle')
def click_live_button():
    VIDEO_SEARCH_PAGE.click_vehicle_tab_new()
    VIDEO_SEARCH_PAGE.click_live_button()


@then('user is navigated to "Live" in VIDEO BROWSER page')
def assert_live_button():
    assert VIDEO_SEARCH_PAGE.get_video_browser_title("VIDEO BROWSER") == "VIDEO BROWSER"
    assert VIDEO_SEARCH_PAGE.browser_tab_is_active() is False
    assert VIDEO_SEARCH_PAGE.live_tab_is_active() is True


# LQ-203
@when('the user clicks on "live" link')
# do nothing due to the live tab is opened already

@then(
    'the outside video is live played on the left and the map is displayed on the right with current position and the '
    'GSP speed is displayed on the bottom')
def assert_live_stream():
    assert VIDEO_SEARCH_PAGE.outside_view_live_tab_is_active() is True
    assert "GPS SPEED" in VIDEO_SEARCH_PAGE.get_gps_speed_text("GPS SPEED")


# LQ-202
@given('"Video Reviewer Plus" user is in browser tab of VIDEO BROWSER page')
def go_to_browser_tab():
    VIDEO_SEARCH_PAGE.click_browser_tab()


@when(
    'user clicks on the "Save To Library" button and user enters a video name in input box and user clicks "Save" button and user clicks "Go To Video" button on the success popup modal')
def save_video():
    VIDEO_SEARCH_PAGE.click_save_to_library()
    VIDEO_SEARCH_PAGE.type_video_name('Save Video Test')
    VIDEO_SEARCH_PAGE.click_save_button()
    VIDEO_SEARCH_PAGE.click_go_to_video_button()


@then('the 120 seconds video for all the views is received and the user is navigated to Video Player page')
def assert_save_video():
    assert VIDEO_SEARCH_PAGE.get_video_player_title("VIDEO PLAYER") == "VIDEO PLAYER"


# LQ-373
@given('the welcome login page is displayed for RDS company')
def launch_welcome_login_page(browser):
    global LOGIN_PAGE, RISK_COMPANY_PAGE, BEHAVIORS_REPORT_PAGE, BASE_PAGE, FLEET_TELEMATICS_PAGE

    LOGIN_PAGE = LoginPage(browser)
    RISK_COMPANY_PAGE = RiskCompanyPage(browser)
    BEHAVIORS_REPORT_PAGE = BehaviorsReportPage(browser)
    FLEET_TELEMATICS_PAGE = FleetTelematicsPageLeftPanel(browser)
    BASE_PAGE = BasePage(browser)
    browser.get(DC_URL)


@when('the user login WS for a risk company')
def login_risk_company():
    LOGIN_PAGE.enter_username(RCD.risk_fa_user_pod7)
    LOGIN_PAGE.enter_password(RCD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed_new_ui(DC_URL, RCD.risk_fa_user_pod7, RCD.password)


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
    RISK_COMPANY_PAGE.click_home_menu()
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
    FLEET_TELEMATICS_PAGE.click_insights_menu()
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
