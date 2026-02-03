from time import sleep

from hamcrest import assert_that, contains_string
from pytest_bdd import scenarios, given, when, then
from selenium.common.exceptions import TimeoutException

from locators.locators_dashboard_page import LocatorsDashboard as AC
from pages.assign_driver_page import AssignDriverPage
from pages.behaviors_report_page import BehaviorsReportPage
from pages.coaching_page import CoachingPage
from pages.dashboard_page import DashboardPage
from pages.driver_profile_page import DriverProfilePage
from pages.drivers_report_page import DriversReportPage
from pages.library_page import LibraryPage
from pages.login_page import LoginPage
from pages.recognition_history_page import RecognitionHistoryPage
from steps.common import DC_URL, ENV, AutomationDataManager, NEW_UI_FTM_URL
from data.int.home_data_int import HomeDataInt as HD_INT
from data.prod.home_data_prod import HomeDataProd as HD_PROD
from data.stg.home_data_stg import HomeDataStg as HD_STG

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
DRIVERS_REPORT_PAGE = 0
DRIVER_PROFILE_PAGE = 0
COACHING_PAGE = 0
LIBRARY_PAGE = 0
RECOGNITION_HISTORY_PAGE = 0
ASSIGN_DRIVER_PAGE = 0
BEHAVIORS_REPORT_PAGE = 0
AD = 0
tadm = 0

scenarios('../features/home_new_UI.feature')


# LQ-304
@given('the login page is displayed')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, DRIVER_PROFILE_PAGE, DRIVERS_REPORT_PAGE
    global COACHING_PAGE, LIBRARY_PAGE, RECOGNITION_HISTORY_PAGE, ASSIGN_DRIVER_PAGE, BEHAVIORS_REPORT_PAGE, HD

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    DRIVER_PROFILE_PAGE = DriverProfilePage(browser)
    DRIVERS_REPORT_PAGE = DriversReportPage(browser)
    COACHING_PAGE = CoachingPage(browser)
    LIBRARY_PAGE = LibraryPage(browser)
    ASSIGN_DRIVER_PAGE = AssignDriverPage(browser)
    RECOGNITION_HISTORY_PAGE = RecognitionHistoryPage(browser)
    BEHAVIORS_REPORT_PAGE = BehaviorsReportPage(browser)

    browser.get(NEW_UI_FTM_URL)

    if ENV == 'int':
        HD = HD_INT
    elif ENV == 'stg':
        HD = HD_STG
    else:
        HD = HD_PROD


@when('the user enters a newly created username/password and clicks the login button')
def login():
    LOGIN_PAGE.enter_username(HD.pod2_full_access_username)
    LOGIN_PAGE.enter_password(HD.password2)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_load()


@then('the user is successfully logged into the Driver Safety dashboard')
def verify_login():
    assert DASHBOARD_PAGE.get_driver_safety_title() == "Driver Safety"
    sleep(5)

    # # check and prepare data  ## it is deleting the existing data in PROD for testing company need to debug more to fix so will pickup in upcoming days
    # DASHBOARD_PAGE.click_library_menu()
    # DASHBOARD_PAGE.click_events_submenu()
    # LIBRARY_PAGE.click_search_dropdown()
    # LIBRARY_PAGE.select_event_id()
    # LIBRARY_PAGE.type_event_id_event_list(HD.F2F_event)
    # LIBRARY_PAGE.select_search_event_id_event_list()
    # if LIBRARY_PAGE.get_first_event_driver() != "Driver Unassigned":
    #     LIBRARY_PAGE.click_event_id()
    #     LIBRARY_PAGE.click_more_actions_ar()
    #     LIBRARY_PAGE.click_reassign_driver()
    #     LIBRARY_PAGE.enter_driver_name("Driver Unassigned")
    #     LIBRARY_PAGE.select_search_name_in_event_preview()
    #     LIBRARY_PAGE.click_assign_button_in_event_preview()
    #     LIBRARY_PAGE.close_preview_window()
    #
    # DASHBOARD_PAGE.click_recognition_history_submenu()
    # LIBRARY_PAGE.click_select_search()
    # LIBRARY_PAGE.click_filter_by_driver()
    # LIBRARY_PAGE.type_in_search_criteria_textbox_rh("Driver Unassigned")
    # LIBRARY_PAGE.select_search_criteria_result_rh_list()
    # LIBRARY_PAGE.delete_recognitions_new_UI()

    # global tadm
    # tadm = AutomationDataManager()
    # tadm.create_data_Home_and_insights_suite()


# LQ-387
@when('the user signs in to Driver Safety')
def login_to_safety():
    DASHBOARD_PAGE.click_home_menu()


@then('the Dashboard page is displayed & the Drivers count is displayed & the UNASSIGNED DRIVERS count'
      ' is displayed in last 90 days & the DUE FOR COACHING count is displayed in last 90 days '
      '& the FYI NOTIFY count is displayed in last 90 days $ the COLLISIONS count is displayed in'
      ' last 90 days & the POSSIBLE COLLISIONS count is displayed in last 90 days')
def verify_dashboard():
    # assert DASHBOARD_PAGE.get_noof_drivers_text(AC.no_of_drivers_text_xpath) is True
    assert_that(DASHBOARD_PAGE.get_unassigned_drivers_text(), contains_string("UNASSIGNED DRIVER"))
    assert DASHBOARD_PAGE.get_due_for_coaching_text() == "DUE FOR COACHING"
    assert DASHBOARD_PAGE.get_fyi_notify_text() == "FYI NOTIFY"
    assert_that(DASHBOARD_PAGE.get_collisions_text(), contains_string("COLLISION"))
    assert_that(DASHBOARD_PAGE.get_possible_collisions_text(), contains_string("POSSIBLE COLLISION"))


# LQ-390
@when('the user clicks link')
def click_links():
    DASHBOARD_PAGE.click_unassigned_drivers_link()


@then('the page is displayed')
def verify_links():
    assert DASHBOARD_PAGE.get_assigned_drivers_title() == "ASSIGN DRIVERS"


@when('the user clicks Due for Coaching link')
def click_due_for_coaching_link():
    DASHBOARD_PAGE.click_home_menu()
    DASHBOARD_PAGE.click_due_for_coaching_link()


@then('the Due for Coaching page is displayed')
def verify_due_for_coaching_link():
    assert DASHBOARD_PAGE.get_due_for_coaching_title() == "DUE FOR COACHING"


@when('the user clicks Collision link')
def click_collision_link():
    DASHBOARD_PAGE.click_home_menu()
    DASHBOARD_PAGE.click_collisions_link()


@then('the Collision page is displayed')
def verify_collision_link():
    assert DASHBOARD_PAGE.get_collisions_title() == "COLLISIONS"


@when('the user clicks FYI Notify link')
def click_fyi_notify_link():
    DASHBOARD_PAGE.click_home_menu()
    DASHBOARD_PAGE.click_fyi_notify_link()


@then('the FYI Notify page is displayed')
def verify_fyi_notify_link():
    assert DASHBOARD_PAGE.get_fyi_notify_title() == "FYI NOTIFY"


# LQ-312
@given('"Safety Manager" user is in Driver Profile page')
def navigate_to_driver_profile_page():
    DASHBOARD_PAGE.click_home_menu()
    DASHBOARD_PAGE.click_driver_profile_link()


@when('the user clicks "Add Recognition" button And the user clicks "Complete" button')
def driver_profile_add_recognition():
    DRIVER_PROFILE_PAGE.click_add_recognition()
    DRIVER_PROFILE_PAGE.click_edit_message_button()
    DRIVER_PROFILE_PAGE.type_recognition_reason()
    DRIVER_PROFILE_PAGE.click_check_or_right_marke_edit_recognition()
    DRIVER_PROFILE_PAGE.click_add_recognition_complete()
    DRIVER_PROFILE_PAGE.click_close_add_recognition_complete()


@then('the recognition is added')
def verify_add_recognition():
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_recognition_history_submenu()
    LIBRARY_PAGE.click_select_search()
    LIBRARY_PAGE.click_filter_by_driver()
    LIBRARY_PAGE.click_select_search()
    LIBRARY_PAGE.type_in_search_criteria_textbox_rh("Driver Unassigned")
    LIBRARY_PAGE.select_search_criteria_result_rh_list()
    LIBRARY_PAGE.delete_recognitions_new_UI()
    DASHBOARD_PAGE.click_home_menu()
    sleep(5)


# LQ-310
@when('the user clicks "Coach Event" button')
def click_coach_event():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_assign_driver_tab()
    ASSIGN_DRIVER_PAGE.click_assign_button()
    ASSIGN_DRIVER_PAGE.search_assign_driver(HD.driver)
    ASSIGN_DRIVER_PAGE.select_searched_driver()
    ASSIGN_DRIVER_PAGE.click_assign()
    sleep(5)
    DASHBOARD_PAGE.click_home_menu()
    sleep(25)
    DASHBOARD_PAGE.click_driver_profile_link()
    DRIVER_PROFILE_PAGE.click_coach_event_button()


@then('Driver Coaching Session page is opened')
def verify_coaching_session_page():
    assert COACHING_PAGE.get_driver_coaching_session_label() == "DRIVER COACHING SESSION"

    # unassign driver for the next run
    COACHING_PAGE.click_more_actions_tab()
    COACHING_PAGE.reassign_driver()
    COACHING_PAGE.search_assign_driver("Driver Unassigned")
    COACHING_PAGE.select_searched_driver()
    COACHING_PAGE.click_assign()

    # # coach the event for next run
    # COACHING_PAGE.click_video()
    # COACHING_PAGE.click_complete_session()
    # COACHING_PAGE.click_save_complete_session()
    # COACHING_PAGE.click_close_complete_session()


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
    assert DASHBOARD_PAGE.get_coachest_by_lowest_effectiveness_title() == "Coaches by Lowest Effectiveness"
    assert DASHBOARD_PAGE.get_coach_title() == "coach"
    assert DASHBOARD_PAGE.get_coaching_effectiveness_title() == "coaching effectiveness"
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
    assert DASHBOARD_PAGE.get_drivers_by_highest_score_title() == "Drivers by Highest Score"
    assert DASHBOARD_PAGE.get_driver_title() == "Driver"
    assert DASHBOARD_PAGE.get_driver_widget_coachable_score_title() == "Coachable Score"
    assert DASHBOARD_PAGE.get_driver_widget_trend_title() == "Trend"
    assert DASHBOARD_PAGE.get_impact_title() == "Impact"


# LQ-407
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


# LQ-409
@when('the user sets group filter to one group')
def set_group_filter():
    DASHBOARD_PAGE.click_group_filter()
    DASHBOARD_PAGE.search_group_filter(HD.group)
    DASHBOARD_PAGE.select_group_filter()
    DASHBOARD_PAGE.click_group_filter_done()


@then('the data belong to the group are listed in "TASKS" & in other metrics')
def verify_group_filter():
    assert DASHBOARD_PAGE.get_coach_widget_1st_coach() is True
    # if there is no data in driver widget, assert the no data msg instead
    try:
        assert DASHBOARD_PAGE.get_driver_widget_1st_driver() is True

    except TimeoutException:
        assert DASHBOARD_PAGE.get_driver_widget_no_data_msg() == "There are no Drivers to display."

    # if there is no data in behavior widget, assert the no data msg instead
    try:
        assert DASHBOARD_PAGE.behavior_widget_element_is_displayed() is True

    except TimeoutException:
        assert DASHBOARD_PAGE.get_behavior_widget_no_data_msg() == "There are no Behaviors to display."


@when('the user sets date filter')
def set_date_filter():
    DASHBOARD_PAGE.click_date_filter()
    DASHBOARD_PAGE.clik_date1_filter()
    DASHBOARD_PAGE.click_date2_filter()
    DASHBOARD_PAGE.click_apply_filter()


@then('the data belong to last 90 days are listed in "TASKS" & in other metrics')
def verify_date_filter():
    # assert DASHBOARD_PAGE.get_no_of_tasks() == HD.no_of_tasks
    assert DASHBOARD_PAGE.get_group_name_filtered() == HD.first_sub_group
    assert DASHBOARD_PAGE.get_coach_name_filtered() is True
    # if there is no data in driver widget, assert the no data msg instead
    try:
        assert DASHBOARD_PAGE.get_driver_widget_1st_driver() is True

    except TimeoutException:
        assert DASHBOARD_PAGE.get_driver_widget_no_data_msg() == "There are no Drivers to display."
    DASHBOARD_PAGE.click_reset_button()


# LQ-307
@given('Safety Manager user is in Driver Safety')
def navigate_to_driver_safety():
    DASHBOARD_PAGE.click_home_menu()


@when(
    'the user clicks "SEARCH" button in left navigation & the user inputs a valid event id & the user clicks search icon')
def quick_search_event_id():
    DASHBOARD_PAGE.click_quick_search_tab_new_UI()
    DASHBOARD_PAGE.search_event_id(HD.F2F_event)
    DASHBOARD_PAGE.click_search_icon()


@then('preview modal of the searched event is opened')
def verify_preview_searched_event():
    assert_that(DASHBOARD_PAGE.get_preview_searched_event(), contains_string(HD.F2F_event))
    DASHBOARD_PAGE.click_close_preview_video()


# LQ-309
@given('"Safety Manager" user is in Driver Report page')
def navigate_to_driver_report_page():
    DASHBOARD_PAGE.click_insights_menu()
    DASHBOARD_PAGE.click_drivers_report_submenu()


@when('the user clicks driver name')
def click_driver_name():
    DRIVERS_REPORT_PAGE.click_driver_name()


@then('Driver Profile page is opened & the driver info is displayed')
def verify_driver_profile_info():
    assert DRIVER_PROFILE_PAGE.get_driver_profile_title_text() == "DRIVER PROFILE"
    assert DRIVER_PROFILE_PAGE.get_employee_id_text() == "EMPLOYEE ID"
    assert DRIVER_PROFILE_PAGE.get_driver_group_text() == "GROUP"
    assert DRIVER_PROFILE_PAGE.get_email_text() == "EMAIL"
    assert DRIVER_PROFILE_PAGE.get_coachable_driver_metrics_text() == "Coachable Driver Metrics"
    assert DRIVER_PROFILE_PAGE.get_score_metrics_text() == "SCORE"
    assert DRIVER_PROFILE_PAGE.get_events_metrics_text() == "EVENTS"
    assert DRIVER_PROFILE_PAGE.get_continual_behavior_text() == "CONTINUAL BEHAVIORS"
    assert DRIVER_PROFILE_PAGE.get_coachable_behavior_text() == "COACHABLE BEHAVIOR"
    assert DRIVER_PROFILE_PAGE.get_frequency_text() == "FREQUENCY (A)"
    assert DRIVER_PROFILE_PAGE.get_weights_text() == "WEIGHT (B)"
    assert DRIVER_PROFILE_PAGE.get_points_text() == "POINTS (A × B)"
    assert DRIVER_PROFILE_PAGE.get_event_id_text_events_tab() == "EVENT ID"
    assert DRIVER_PROFILE_PAGE.get_group_text() == "GROUP"
    assert DRIVER_PROFILE_PAGE.get_vehicle_text() == "VEHICLE"
    assert DRIVER_PROFILE_PAGE.get_device_text() == "DEVICE"
    assert DRIVER_PROFILE_PAGE.get_event_date_text() == "EVENT DATE"
    assert DRIVER_PROFILE_PAGE.get_score_event_text() == "SCORE"
    assert DRIVER_PROFILE_PAGE.get_status_text() == "STATUS"
    assert DRIVER_PROFILE_PAGE.get_trigger_text() == "TRIGGER"
    assert DRIVER_PROFILE_PAGE.get_behavior_metrics_text() == "BEHAVIORS"


@when('the user clicks Continual Behaviors tab')
def navigate_to_continual_behaviors_tab():
    DRIVER_PROFILE_PAGE.click_continual_behavior()


@then('the Continual Behaviors drop down is shown & the Summary section & the Incidents section is displayed')
def verify_continual_behaviors_tab():
    assert DRIVER_PROFILE_PAGE.get_summary_count_text() == "Summary"
    assert DRIVER_PROFILE_PAGE.get_behavior_count_text() == "BEHAVIOR"
    assert DRIVER_PROFILE_PAGE.get_duration_count_text() == "DURATION"
    assert DRIVER_PROFILE_PAGE.get_percent_of_drive_time_text() == "% OF DRIVE TIME"
    assert DRIVER_PROFILE_PAGE.get_incidents_tab_text() == "Incidents"
    assert DRIVER_PROFILE_PAGE.get_incidents_behavior_text() == "BEHAVIOR"
    assert DRIVER_PROFILE_PAGE.get_incidents_duration_text() == "DURATION"
    assert DRIVER_PROFILE_PAGE.get_incidents_date_text() == "DATE"


@when('the user clicks Coaching History tab')
def navigate_to_coaching_history_tab():
    DRIVER_PROFILE_PAGE.click_coaching_history_tab()


@then(
    'the table is displayed with columns:"SESSION ID","COACH DATE","OVERDUE DATE", "BEHAVIORS COACHED","COACH", NOTES')
def verify_coaching_history_tab():
    assert DRIVER_PROFILE_PAGE.get_session_id_text() == "SESSION ID"
    assert DRIVER_PROFILE_PAGE.get_coach_date_text() == "COACH DATE"
    # comment out below asserts for now because the 'OVERDUE DATE' column is controlled by toggle 'ENABLE_OVERDUE_COLUMN'. But it was set to false/true back and force
    # assert DRIVER_PROFILE_PAGE.get_overdue_date_text() == "OVERDUE DATE"
    # assert DRIVER_PROFILE_PAGE.get_behaviors_coached_text() == "BEHAVIORS COACHED"
    # assert DRIVER_PROFILE_PAGE.get_coach_text() == "COACH"
    # assert DRIVER_PROFILE_PAGE.get_notes_text() == "NOTES"


@when('the user clicks Recognitions tab')
def navigate_to_recognitions_tab():
    DRIVER_PROFILE_PAGE.click_recognitions_tab()


@then('the table is displayed with columns:"TYPE","EVENT ID","ISSUED BY","ISSUED DATE", RECOGNITION REASON')
def verify_recognitions_tab():
    assert DRIVER_PROFILE_PAGE.get_type_text() == "TYPE"
    assert DRIVER_PROFILE_PAGE.get_event_id_rec_text() == "EVENT ID"
    assert DRIVER_PROFILE_PAGE.get_issued_by_text() == "ISSUED BY"
    assert DRIVER_PROFILE_PAGE.get_issued_date_text() == "ISSUED DATE"
    assert DRIVER_PROFILE_PAGE.get_recognition_reason_text() == "RECOGNITION REASON"
