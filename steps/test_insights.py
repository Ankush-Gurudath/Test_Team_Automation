from time import sleep

from hamcrest import assert_that, contains_string
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then

from pages.behaviors_report_page import BehaviorsReportPage
from pages.coaches_profile_page import CoachesProfilePage
from pages.coaches_report_page import CoachesReportPage
from pages.dashboard_page import DashboardPage
from pages.drivers_report_page import DriversReportPage
from pages.group_report_page import GroupReportPage
from pages.library_page import LibraryPage
from pages.login_page import LoginPage
from pages.open_tasks_report_page import OpenTasksReportPage
from pages.program_status_report_page import ProgramStatusReportPage
from pages.safe_driving_report_page import SafeDrivingReportPage
from steps.common import DC_URL, ENV
from data.int.ws_insights_data_int import InsightsDataInt as ID_INT
from data.prod.ws_insights_data_prod import InsightsDataProd as ID_PROD
from data.stg.ws_insights_data_stg import InsightsDataStg as ID_STG

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
OPEN_TASKS_REPORT_PAGE = 0
COACHES_REPORT_PAGE = 0
global DRIVERS_REPORT_PAGE
BEHAVIORS_REPORT_PAGE = 0
PROGRAM_STATUS_REPORT_PAGE = 0
GROUP_REPORT_PAGE = 0
COACHES_PROFILE_PAGE = 0
LIBRARY_PAGE = 0
SAFE_DRIVING_REPORT_PAGE = 0

ID = 0
coach_name = ""
group_name = ""
first_driver_name = ""
continual_driver = ""
Coaches_report_group_name = ""
program_status_group_name = ""

scenarios('../features/insights.feature')


# @LQ-384
@given('the coach user logs in')
def launch_browser_and_login(browser):
    global LOGIN_PAGE, OPEN_TASKS_REPORT_PAGE, DASHBOARD_PAGE, DRIVERS_REPORT_PAGE
    global GROUP_REPORT_PAGE, COACHES_REPORT_PAGE, PROGRAM_STATUS_REPORT_PAGE, BEHAVIORS_REPORT_PAGE
    global COACHES_PROFILE_PAGE, LIBRARY_PAGE, ID, SAFE_DRIVING_REPORT_PAGE

    LOGIN_PAGE = LoginPage(browser)
    OPEN_TASKS_REPORT_PAGE = OpenTasksReportPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    GROUP_REPORT_PAGE = GroupReportPage(browser)
    COACHES_REPORT_PAGE = CoachesReportPage(browser)
    DRIVERS_REPORT_PAGE = DriversReportPage(browser)
    PROGRAM_STATUS_REPORT_PAGE = ProgramStatusReportPage(browser)
    BEHAVIORS_REPORT_PAGE = BehaviorsReportPage(browser)
    COACHES_PROFILE_PAGE = CoachesProfilePage(browser)
    LIBRARY_PAGE = LibraryPage(browser)
    SAFE_DRIVING_REPORT_PAGE = SafeDrivingReportPage(browser)

    browser.get(DC_URL)

    if ENV == 'int':
        ID = ID_INT
    elif ENV == 'stg':
        ID = ID_STG
    else:
        ID = ID_PROD

    LOGIN_PAGE.enter_username(ID.admin_username)
    LOGIN_PAGE.enter_password(ID.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_multi_company('DriveCam DC4DC Test Co')
    LOGIN_PAGE.click_select_company_button()


@when('the user clicks "INSIGHTS" and the user clicks "OPEN TASKS REPORT" '
      'And the user sets group filter to one group in Open Tasks Report page')
def open_tasks_filter():
    DASHBOARD_PAGE.click_insights_menu()
    DASHBOARD_PAGE.click_open_tasks_report_submenu_new_UI()
    OPEN_TASKS_REPORT_PAGE.click_filter_by_group()
    OPEN_TASKS_REPORT_PAGE.enter_group(ID.group)
    OPEN_TASKS_REPORT_PAGE.click_select_group()
    OPEN_TASKS_REPORT_PAGE.click_done()


@then('the data belong to the group are listed in Open Tasks Report page')
def verify_filter_group():
    assert OPEN_TASKS_REPORT_PAGE.task_count_displayed() is True


@when('the user enters some characters into "Search Name or ID" field in Open Tasks Report page')
def open_tasks_search():
    global first_driver_name
    OPEN_TASKS_REPORT_PAGE.click_reset()
    first_driver_name = OPEN_TASKS_REPORT_PAGE.get_first_driver_name()
    OPEN_TASKS_REPORT_PAGE.enter_name_id(first_driver_name)
    sleep(2)
    OPEN_TASKS_REPORT_PAGE.click_select_name()


@then('the data belong to the driver are listed in Open Tasks Report page')
def verify_search_name_id():
    assert OPEN_TASKS_REPORT_PAGE.task_count_displayed() is True


# LQ-383
@when('the user clicks "INSIGHTS" and the user clicks "OPEN TASKS REPORT" '
      'in Open Tasks Report page')
def display_table():
    OPEN_TASKS_REPORT_PAGE.click_reset()


@then('the number of drivers is displayed in Open Tasks Report page')
# @And  ('the table is displayed with columns "DRIVER NAME", "DRIVER GROUP",
# "FACE-TO-FACE",  "FACE-TO-FACE(OVERDUE) ",  "FYI NOTIFY"')
def verify_table_data():
    assert OPEN_TASKS_REPORT_PAGE.task_count_displayed() is True
    assert OPEN_TASKS_REPORT_PAGE.get_driver_text() == "DRIVER"
    assert OPEN_TASKS_REPORT_PAGE.get_driver_group_text() == "DRIVER'S GROUP"
    assert OPEN_TASKS_REPORT_PAGE.get_f2f_text() == "FACE-TO-FACE"
    assert OPEN_TASKS_REPORT_PAGE.get_f2f_overdue_text() == "FACE-TO-FACE (OVERDUE)"


# LQ-385
@when('the user clicks the Tasks Link in Open Tasks Report page')
def open_tasks_links():
    OPEN_TASKS_REPORT_PAGE.click_event_link()


@then('the Event profile page is displayed in Open Tasks Report page')
def verify_links():
    assert OPEN_TASKS_REPORT_PAGE.get_event_profile_text() == "EVENTS"


# LQ-339
@when('the user clicks "INSIGHTS" and the user clicks "DRIVERS REPORT" in Drivers Report page')
def driver_scores_tab():
    DASHBOARD_PAGE.click_insights_menu()
    DASHBOARD_PAGE.click_drivers_report_submenu_new_UI()


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


# LQ-340
@when('the user sets group filter to one group in Drivers Report page')
def driver_filter_group():
    DRIVERS_REPORT_PAGE.click_filter_group()
    DRIVERS_REPORT_PAGE.search_filter_group(ID.group)
    DRIVERS_REPORT_PAGE.select_search_filter()
    DRIVERS_REPORT_PAGE.click_done()


@then('the data belong to the group are listed in Drivers Report page')
def verify_group_filter():
    assert DRIVERS_REPORT_PAGE.task_count_displayed() is True


@when('the user sets date filter in Driver Scores in Drivers Report page')
def filter_date():
    DRIVERS_REPORT_PAGE.select_date_filter()
    DRIVERS_REPORT_PAGE.select_from_date()
    DRIVERS_REPORT_PAGE.select_end_date()
    DRIVERS_REPORT_PAGE.click_apply()


@then('the data belong to the date are listed in Driver Scores in Drivers Report page')
def verify_date_filter():
    assert DRIVERS_REPORT_PAGE.task_count_displayed() is True


@when('the user sets behavior filter to one behavior in Driver Scores in Drivers Report page')
def behavior_filter():
    DRIVERS_REPORT_PAGE.select_behavior()


@then('the data belong to the behavior are listed in Driver Scores in Drivers Report page')
def verify_behavior_filter():
    assert DRIVERS_REPORT_PAGE.task_count_displayed() is True


@when('the user enters some characters into "Search Name or ID" field in Driver Scores '
      'and the user selects a driver from the suggestion list in Drivers Report page')
def search_name_id():
    DRIVERS_REPORT_PAGE.search_by_name(ID.driver2)
    DRIVERS_REPORT_PAGE.select_search_name()


@then('the data belong to the driver are listed in Driver Scores in Drivers Report page')
def verify_search_name():
    assert DRIVERS_REPORT_PAGE.task_count_displayed() is True


# LQ-341
@when('the user clicks the Driver Scores link in Drivers Report page')
def get_profile_link_driver_scores():
    DRIVERS_REPORT_PAGE.click_driver_scores_link()


@then('the Driver Profile page is displayed in Drivers Report page')
def verify_driver_profile_behave():
    assert DRIVERS_REPORT_PAGE.get_driver_profile_driver_scores() == ID.driver2


# NAL-323
@when('the user clicks the first driver in Drivers Report page')
def click_driver_name():
    DRIVERS_REPORT_PAGE.back_to_previous_page()
    DRIVERS_REPORT_PAGE.click_reset()
    DRIVERS_REPORT_PAGE.click_first_driver_name()


@then('the events are displayed in descending order based on date in driver profile page')
def verify_event_date_descending_order():
    assert DRIVERS_REPORT_PAGE.are_event_dates_descending() is True


# LQ-342
@when('the user clicks "Continual Behaviors" in Drivers Report page')
def continual_behave():
    DRIVERS_REPORT_PAGE.back_to_previous_page()
    DRIVERS_REPORT_PAGE.click_reset_driver_score()
    DRIVERS_REPORT_PAGE.click_continual()


@then('the Continual Behaviors tab is selected and the number of drivers is displayed '
      'and the table is displayed with columns "DRIVER NAME", "GROUP", "HANDHELD DEVICE Duration", '
      '"HANDHELD DEVICE % Of Drive Time", "INATTETIVE Duration", "INATTETIVE % Of Drive Time", '
      '"FOOD OR DRINK Duration", "FOOD OR DRINK % Of Drive Time", "DRIVER SMOKING Duration", '
      '"DRIVER SMOKING % Of Drive Time", "POLICY SPEED Duration", "POLICY SPEED % Of Drive Time", '
      '"NO SEAT BELT Duration", "NO SEAT BELT % Of Drive Time" in Drivers Report page')
def verify_continual_behavior_table():
    assert DRIVERS_REPORT_PAGE.get_driver_behave_text() == "DRIVER"
    assert DRIVERS_REPORT_PAGE.get_group_behave_text() == "GROUP"
    assert DRIVERS_REPORT_PAGE.get_continual_behavior_1st() == "HANDHELD DEVICE"


# LQ-343
@when('the user sets group filter to one group in continual behavior in Drivers Report page')
def filter_group_behave():
    DRIVERS_REPORT_PAGE.click_filter_group_behave()
    DRIVERS_REPORT_PAGE.search_group_behave(ID.group)
    DRIVERS_REPORT_PAGE.select_search_filter_behave()
    DRIVERS_REPORT_PAGE.click_done_search_behave()


@then('the data belong to the group are listed in continual behavior in Drivers Report page')
def verify_continual_behavior_filter_group():
    assert DRIVERS_REPORT_PAGE.task_count_displayed() is True


@when('the user sets date filter in continual behavior in Drivers Report page')
def filter_date_behave():
    DRIVERS_REPORT_PAGE.click_date_filter_behave()
    DRIVERS_REPORT_PAGE.select_from_date_behave()
    DRIVERS_REPORT_PAGE.select_end_date_behave()
    DRIVERS_REPORT_PAGE.click_apply_date_behave()


@then('the data belong to the date are listed in continual behavior in Drivers Report page')
def verify_date_filter_behave():
    assert DRIVERS_REPORT_PAGE.task_count_displayed() is True


@when('the user enters some characters into "Search Name or ID" field in continual behavior '
      'and the user selects a driver from the suggestion list in Drivers Report page')
def search_name_id_behave():
    global continual_driver
    continual_driver = DRIVERS_REPORT_PAGE.get_first_driver_name()
    DRIVERS_REPORT_PAGE.clear_search_name_behave()
    DRIVERS_REPORT_PAGE.search_name_behave(continual_driver)
    DRIVERS_REPORT_PAGE.select_search_name_behave()


@then('the data belong to the driver are listed in continual behavior in Drivers Report page')
def verify_search_name_behave():
    assert DRIVERS_REPORT_PAGE.task_count_displayed() is True


# LQ-344
@when('the user clicks Continual Behaviors tab and clicks the first driver in Drivers Report page')
def get_profile_link_behave():
    DRIVERS_REPORT_PAGE.click_profile_link_behave()


@then('the Driver Profile page for the chosen result is displayed in Drivers Report page')
def verify_driver_profile_behave_chosen_result():
    assert DRIVERS_REPORT_PAGE.get_driver_profile_behave_text() == continual_driver


# LQ-345
@when('the user clicks "Alerts" in Drivers Report page')
def get_alert_link_behave():
    DRIVERS_REPORT_PAGE.back_to_previous_page()
    DRIVERS_REPORT_PAGE.click_reset()
    DRIVERS_REPORT_PAGE.click_alert_link()


@then('the Alerts tab is selected and the number of drivers is displayed and the table is displayed'
      ' with columns "DRIVER NAME", "GROUP", "ALERTS Total", "ALERTS Trend" in Drivers Report page')
def verify_alert_table():
    assert DRIVERS_REPORT_PAGE.get_driver_alert_text() == "DRIVER"
    assert DRIVERS_REPORT_PAGE.get_group_alert_text() == "GROUP"
    assert DRIVERS_REPORT_PAGE.get_total_alerts_text() == "TOTAL ALERTS"
    assert DRIVERS_REPORT_PAGE.get_handheld_alert_text() == "HANDHELD DEVICE"
    assert DRIVERS_REPORT_PAGE.get_inattentive_alert_text() == "INATTENTIVE"
    assert DRIVERS_REPORT_PAGE.get_food_or_drink_alert_text() == "FOOD OR DRINK"
    assert DRIVERS_REPORT_PAGE.get_driver_smoking_alert_text() == "DRIVER SMOKING"
    assert DRIVERS_REPORT_PAGE.get_policy_speed_alert_text() == "POLICY SPEED"
    assert DRIVERS_REPORT_PAGE.get_posted_speed_alert_text() == "POSTED SPEED"
    assert DRIVERS_REPORT_PAGE.get_no_seat_belt_alert_text() == "NO SEAT BELT"
    assert DRIVERS_REPORT_PAGE.get_lens_obstruct_alert_text() == "LENS OBSTRUCTION"
    assert DRIVERS_REPORT_PAGE.get_lane_departed_alert_text() == "LANE DEPARTURE"
    assert DRIVERS_REPORT_PAGE.get_rolling_alert_text() == "ROLLING STOP"
    assert DRIVERS_REPORT_PAGE.get_follow_dist_alert() == "FOLLOWING DISTANCE"
    assert DRIVERS_REPORT_PAGE.get_critical_dist_alert() == "CRITICAL DISTANCE"


# LQ-346
@when('the user sets group filter to one group in Alert in Drivers Report page')
def group_filter_alert():
    DRIVERS_REPORT_PAGE.click_reset_alert()
    DRIVERS_REPORT_PAGE.click_filter_alert_group()
    DRIVERS_REPORT_PAGE.search_filter_group_alert(ID.group)
    DRIVERS_REPORT_PAGE.select_search_filter_group_alert()
    DRIVERS_REPORT_PAGE.click_done_filter_group_alert()


@then('the data belong to the group are listed in Alert in Drivers Report page')
def verify_filter_group_alert():
    assert DRIVERS_REPORT_PAGE.task_count_displayed() is True


@when('the user sets date filter in Alert in Drivers Report page')
def filter_date_alert():
    DRIVERS_REPORT_PAGE.click_filter_date_alert()
    DRIVERS_REPORT_PAGE.select_from_date_alert()
    DRIVERS_REPORT_PAGE.select_end_date_alert()
    DRIVERS_REPORT_PAGE.click_apply_date_alert()


@then('the data belong to the date are listed in Alert in Drivers Report page')
def verify_date_filter_alert():
    assert DRIVERS_REPORT_PAGE.task_count_displayed() is True


@when('the user sets behavior filter to one behavior in Alert in Drivers Report page')
def filter_behave_alert():
    DRIVERS_REPORT_PAGE.click_behave_alert()
    DRIVERS_REPORT_PAGE.select_behave_alert()


@then('the data belong to the behavior are listed in Alert in Drivers Report page')
def verify_behave_filter_alert():
    assert DRIVERS_REPORT_PAGE.get_length_of_columns() == 5


@when('the user enters some characters into "Search Name or ID" field in Alert '
      'and the user selects a driver from the suggestion list in Drivers Report page')
def filter_search_name_alert():
    DRIVERS_REPORT_PAGE.clear_search_name_alert()
    DRIVERS_REPORT_PAGE.search_name_alert(ID.driver2)
    DRIVERS_REPORT_PAGE.select_search_name_alert()


@then('the data belong to the driver are listed in Alert in Drivers Report page')
def verify_search_name_alert():
    assert DRIVERS_REPORT_PAGE.get_first_driver_name() == ID.driver2


# LQ-347
@when('the user clicks the first driver in Alert in Drivers Report page')
def get_profile_link_alert():
    DRIVERS_REPORT_PAGE.click_profile_link_alert()


@then('the Driver Profile page for the chosen result is displayed for Alert in Drivers Report page')
def verify_driver_profile_alert():
    assert DRIVERS_REPORT_PAGE.get_driver_profile_alert_text() == ID.driver2



# LQ-366
@when('the user clicks "INSIGHTS" And the user clicks "GROUP REPORT" in Group Report page')
def group_report_tab():
    # DRIVERS_REPORT_PAGE.back_to_previous_page()
    DASHBOARD_PAGE.click_insights_menu()
    DASHBOARD_PAGE.click_group_report_submenu_new_UI()
    GROUP_REPORT_PAGE.click_reset_alert()


@then('the number of group is displayed and the table is displayed with columns "GROUP", '
      '"# OF VEHICLES", "COACHABLE SCORE Total", "COACHABLE SCORE Trend", '
      '"COACHABLE EVENTS Total", "COACHABLE EVENTS Trend" in Group Report page')
def verify_group_report_table():
    sleep(3)  # Report takes time to render
    assert GROUP_REPORT_PAGE.get_group_text() == "GROUP"
    assert GROUP_REPORT_PAGE.get_num_of_vehicles_text() == "# OF VEHICLES"
    assert GROUP_REPORT_PAGE.get_coachable_score_text() == "COACHABLE SCORE"
    assert GROUP_REPORT_PAGE.get_coachable_events_text() == "COACHABLE EVENTS"


# LQ-367
@when('the user sets group filter to one group in Group Report page')
def group_filter_group():
    GROUP_REPORT_PAGE.click_reset_alert()
    GROUP_REPORT_PAGE.click_filter_by_group()
    GROUP_REPORT_PAGE.search_filter_by_group(ID.group)
    GROUP_REPORT_PAGE.select_search_filter_by_group()
    GROUP_REPORT_PAGE.click_done_filter_by_group()


@then('the data belong to the group are listed in Group Report page')
def verify_group_report_filter_group():
    assert GROUP_REPORT_PAGE.get_first_group_name() == ID.group


@when('the user sets date filter in Group Report page')
def group_filter_date():
    GROUP_REPORT_PAGE.click_reset_alert()
    GROUP_REPORT_PAGE.click_date_filter()
    GROUP_REPORT_PAGE.select_from_date_filter()
    GROUP_REPORT_PAGE.select_end_date_filter()
    GROUP_REPORT_PAGE.click_apply_filter()


@then('the data belong to the date are listed in Group Report page')
def verify_group_report_filter_date():
    assert GROUP_REPORT_PAGE.task_count_displayed() is True


@when('the user sets behavior filter to one behavior in Group Report page')
def group_behavior_filter():
    GROUP_REPORT_PAGE.click_behaviors_filter()
    GROUP_REPORT_PAGE.select_behaviors_filter()


@then('the data belong to the behavior are listed in Group Report page')
def verify_group_report_filter_behavior():
    assert GROUP_REPORT_PAGE.task_count_displayed() is True


@when('the user sets Normalized filter to "Normalized by number of Vehicles" in Group Report page')
def group_normalized_filter():
    GROUP_REPORT_PAGE.click_normalized_filter()
    GROUP_REPORT_PAGE.select_normalized_filter()


@then('the normalized data are displayed in Group Report page')
def verify_group_report_filter_normalized():
    assert GROUP_REPORT_PAGE.task_count_displayed() is True


# LQ-368
@when('the user clicks the Group Link in Group Report page')
def group_links():
    GROUP_REPORT_PAGE.click_on_group_link()


@then('the Drivers Report page is displayed for the chosen result in Group Report page')
def verify_group_report_links():
    assert GROUP_REPORT_PAGE.get_drivers_report_page_text() == "DRIVERS REPORT"


# LQ-379
@when('the user clicks "INSIGHTS" And the user clicks "COACHES REPORT" in Coaches Report page')
def coaches_report_tab():
    DASHBOARD_PAGE.click_coaches_report_submenu_new_UI()
    COACHES_REPORT_PAGE.click_reset()


@then('the number of coaches is displayed  in Coaches Report page And the table is displayed '
      'with columns "COACH", "GROUP", "COACHING EFFECTIVENESS", "AVG DAYS TO COACH", '
      '"COACHED EVENTS", "WITH NOTES", "LAST LOGIN" in Coaches Report page')
def verify_coaches_report_table():
    sleep(2)  # Subgroups animation takes a few seconds to display. I couldn't find a workaround.
    assert COACHES_REPORT_PAGE.get_num_of_coaches_text() is True
    assert COACHES_REPORT_PAGE.get_coach_text() == "COACH"
    assert COACHES_REPORT_PAGE.get_group_text() == "GROUP"
    assert COACHES_REPORT_PAGE.get_avg_days_to_coach_text() == "AVG DAYS TO COACH"
    assert COACHES_REPORT_PAGE.get_coached_events_text() == "COACHED EVENTS"
    assert COACHES_REPORT_PAGE.get_with_notes_text() == "WITH NOTES"
    assert COACHES_REPORT_PAGE.get_last_login_text() == "LAST LOGIN"


# LQ-381
@when('the user sets group filter to one group in Coaches Report page')
def coaches_filter_group():
    global Coaches_report_group_name
    Coaches_report_group_name = COACHES_REPORT_PAGE.get_group_name()
    COACHES_REPORT_PAGE.click_filter_by_group_coaches()
    COACHES_REPORT_PAGE.search_filter_by_group_coaches(Coaches_report_group_name)
    COACHES_REPORT_PAGE.select_filter_by_group_coaches()
    COACHES_REPORT_PAGE.click_done_filter_by_group_coaches()


@then('the data belong to the group are listed in Coaches Report page')
def verify_filter_by_group_coach():
    assert_that(COACHES_REPORT_PAGE.get_group_name(), contains_string(Coaches_report_group_name))


@when('the user sets date filter in Coaches Report page')
def coaches_filter_by_date():
    COACHES_REPORT_PAGE.click_filter_by_date_coaches()
    COACHES_REPORT_PAGE.select_from_date_by_date_coaches()
    COACHES_REPORT_PAGE.select_end_date_by_date_coaches()
    COACHES_REPORT_PAGE.click_apply_by_date_coaches()


@then('the data belong to the date are listed in Coaches Report page')
def verify_filter_by_date_coach():
    assert COACHES_REPORT_PAGE.get_num_of_coaches_text() is True


@when('the user selects "Coaches with Activity" in coach filter in Coaches Report page')
def coaches_filter_by_group_activity():
    COACHES_REPORT_PAGE.click_filter_by_coaches_activity()
    COACHES_REPORT_PAGE.select_filter_by_coaches_activity()


@then('the coaches belong to the filter are listed in Coaches Report page')
def verify_filter_by_coaches_activity():
    assert COACHES_REPORT_PAGE.get_num_of_coaches_text() is True


@when('the user selects "Selected Group Data Only" in data filter And the user sets '
      'group filter to one group in Coaches Report page')
def coaches_filter_by_group_data_only():
    COACHES_REPORT_PAGE.click_filter_by_group_data_only()
    COACHES_REPORT_PAGE.select_filter_by_group_data_only()


@then('the data only belong to the selected group are listed  in Coaches Report page')
def verify_filter_by_selected_group_data():
    assert COACHES_REPORT_PAGE.get_num_of_coaches_text() is True
    COACHES_REPORT_PAGE.click_reset()


# LQ-382
@when('the user clicks the Coaches link in Coaches Report page')
def click_coaches_link():
    global coach_name
    coach_name = COACHES_REPORT_PAGE.get_coach_name()
    COACHES_REPORT_PAGE.click_coach_link()


@then('the Coaches profile is displayed in Coaches Report page')
def verify_coaches_link():
    assert COACHES_REPORT_PAGE.get_coach_profile_text() == coach_name
    COACHES_REPORT_PAGE.back_to_previous_page()


# LQ-369
@when('the user clicks "INSIGHTS" And the user clicks "PROGRAM STATUS REPORT" '
      'in Program Status Report page')
def program_status_report_tab():
    DASHBOARD_PAGE.click_program_status_report_submenu_new_UI()


@then('the number of subgroups is displayed And the table is displayed with columns "GROUP", '
      '"# OF DEVICES", "UNASSIGNED DRIVERS", "OVERDUE FOR CHECK-IN", "OVERDUE FOR COACHING", '
      '"COACHING EFFECTIVENESS", "PROGRAM EFFECTIVENESS" in Program Status Report page')
def verify_program_status_report_table():
    sleep(5)  # Subgroups animation takes a few seconds to display. I couldn't find a workaround.
    assert PROGRAM_STATUS_REPORT_PAGE.get_num_of_subgroups_text() is True
    assert PROGRAM_STATUS_REPORT_PAGE.get_group_text() == "GROUP"
    assert PROGRAM_STATUS_REPORT_PAGE.get_num_of_devices_text() == "# OF DEVICES"
    assert PROGRAM_STATUS_REPORT_PAGE.get_unassigned_drivers_text() == "UNASSIGNED DRIVERS"
    assert PROGRAM_STATUS_REPORT_PAGE.get_overdue_for_checkin_text() == "OVERDUE FOR CHECK-IN"
    assert PROGRAM_STATUS_REPORT_PAGE.get_overdue_for_coaching_text() == "OVERDUE FOR COACHING"
    assert PROGRAM_STATUS_REPORT_PAGE.get_coaching_effectiveness_text() == "COACHING EFFECTIVENESS"
    assert PROGRAM_STATUS_REPORT_PAGE.get_program_effectiveness_text() == "PROGRAM EFFECTIVENESS"


# LQ-370
@when('the user sets group filter to one group in program status report page')
def program_status_filter_group():
    global program_status_group_name
    program_status_group_name = PROGRAM_STATUS_REPORT_PAGE.get_first_group_name()
    PROGRAM_STATUS_REPORT_PAGE.click_filter_by_group()
    PROGRAM_STATUS_REPORT_PAGE.search_filter_by_group(program_status_group_name)
    PROGRAM_STATUS_REPORT_PAGE.select_filter_by_group()
    PROGRAM_STATUS_REPORT_PAGE.click_done_button()


@then('the data belong to the group are listed in program status report page')
def verify_filter_by_group_program_status_report():
    assert PROGRAM_STATUS_REPORT_PAGE.get_first_group_name() == program_status_group_name
    assert PROGRAM_STATUS_REPORT_PAGE.get_num_of_subgroups_text() is True  # there is a total row and will be counted
    PROGRAM_STATUS_REPORT_PAGE.click_reset()


# LQ-371
@when('the user clicks a Unassigned drivers value')
def click_unassigned_driver_value():
    PROGRAM_STATUS_REPORT_PAGE.click_unassigned_driver_link()


@then('the Assign Drivers page is displayed')
def assert_unassigned_driver_link():
    assert PROGRAM_STATUS_REPORT_PAGE.get_assigned_driver_page_text() == "ASSIGN DRIVERS"

    PROGRAM_STATUS_REPORT_PAGE.back_to_previous_page()
    PROGRAM_STATUS_REPORT_PAGE.click_reset()


@when('the user clicks a group link')
def click_group_link():
    PROGRAM_STATUS_REPORT_PAGE.click_group_link()


@then('the Program Status Report page is displayed')
def assert_group_link():
    assert PROGRAM_STATUS_REPORT_PAGE.get_program_status_report_page_text() == "PROGRAM STATUS REPORT"

    PROGRAM_STATUS_REPORT_PAGE.click_reset()


@when('the user clicks a overdue for coaching value')
def click_overdue_for_coaching_link():
    PROGRAM_STATUS_REPORT_PAGE.click_overdue_for_coaching_link()


@then('the Due For Coaching page is displayed')
def assert_overdue_for_coaching_link():
    assert PROGRAM_STATUS_REPORT_PAGE.get_due_for_coaching_page_text() == "DUE FOR COACHING"


@when('the user clicks a coaching effectiveness value')
def click_coaching_effectiveness_link():
    DASHBOARD_PAGE.click_insights_menu()
    DASHBOARD_PAGE.click_program_status_report_submenu()
    PROGRAM_STATUS_REPORT_PAGE.click_reset()
    PROGRAM_STATUS_REPORT_PAGE.click_coaching_effectiveness_link()


@then('the Coaches Report page is displayed')
def assert_coaching_effectiveness_link():
    assert PROGRAM_STATUS_REPORT_PAGE.get_coaches_report_page_text() == "COACHES REPORT"


# LQ-372
@when('the user clicks "INSIGHTS" and the user clicks "BEHAVIORS REPORT" in Behaviors Report page')
def behaviors_report_tab():
    DASHBOARD_PAGE.click_behaviors_report_submenu_new_UI()


@then('the number of behaviors is displayed and  the table is displayed with columns "BEHAVIOR", '
      '"FREQUENCY", "TREND" in Behaviors Report page')
def verify_behave_table():
    assert BEHAVIORS_REPORT_PAGE.get_behavior_text() == "BEHAVIOR"
    assert BEHAVIORS_REPORT_PAGE.get_frequency_text() == "FREQUENCY"
    assert BEHAVIORS_REPORT_PAGE.get_trend_text() == "TREND"
    # comment this due to SCRUMP-3093
    # assert BEHAVIORS_REPORT_PAGE.get_num_behave() == ID.event_behavior_count


# LQ-374
@when('the user sets group filter to one group in Behaviors Report page')
def behavior_filter_group():
    global behaviors_report_
    BEHAVIORS_REPORT_PAGE.click_filter_group_behave()
    BEHAVIORS_REPORT_PAGE.search_filter_group_behave(ID.group)
    BEHAVIORS_REPORT_PAGE.select_search_filter_group_behave()
    BEHAVIORS_REPORT_PAGE.click_done_behave()


@then('the data belong to the group are listed in Behaviors Report page')
def verify_filter_group_behave():
    assert BEHAVIORS_REPORT_PAGE.get_num_of_behaviors_text() is True


@when('the user sets date filter in Behaviors Report page')
def behavior_filter_date():
    BEHAVIORS_REPORT_PAGE.click_filter_date_behave()
    BEHAVIORS_REPORT_PAGE.click_from_date_behave()
    BEHAVIORS_REPORT_PAGE.click_end_date_behave()
    BEHAVIORS_REPORT_PAGE.click_apply_behave()


@then('the data belong to the date are listed in Behaviors Report page')
def verify_filter_date_behave():
    assert BEHAVIORS_REPORT_PAGE.get_num_of_behaviors_text() is True
    BEHAVIORS_REPORT_PAGE.click_reset_button()


# LQ-377
@when('the user clicks the first frequency value')
def click_first_frequency_value():
    BEHAVIORS_REPORT_PAGE.click_first_frequency_value()


@then('the Drivers Report page for the chosen result is displayed')
def assert_link_of_frequency_value():
    assert BEHAVIORS_REPORT_PAGE.get_driver_report_text() == "DRIVERS REPORT"


# LQ-308
@given('Safety Manager user is in Coaches Report page')
def navigate_to_coaches_report_page():
    DASHBOARD_PAGE.click_insights_menu()
    DASHBOARD_PAGE.click_coaches_report_submenu_new_UI()


@when('the user clicks a coach name')
def navigate_to_coach_profile_page():
    COACHES_REPORT_PAGE.click_reset()
    COACHES_REPORT_PAGE.click_coach_link()


@then('Coach Profile page is opened & the coach info are shown with: "EMPLOYEE ID","GROUP","EMAIL", LAST LOGIN')
def verify_coach_profile_view_page():
    sleep(5)
    assert COACHES_PROFILE_PAGE.get_coach_profile_text() == "COACH PROFILE"
    assert COACHES_PROFILE_PAGE.get_employee_id_text() == "EMPLOYEE ID"
    assert COACHES_PROFILE_PAGE.get_group_text() == "GROUP"
    assert COACHES_PROFILE_PAGE.get_email_text() == "EMAIL"
    assert COACHES_PROFILE_PAGE.get_last_login_text() == "LAST LOGIN"
    assert COACHES_PROFILE_PAGE.get_coaching_effectiveness_text() == "COACHING EFFECTIVENESS"
    assert COACHES_PROFILE_PAGE.get_coached_behaviors_text() == "COACHED BEHAVIORS"
    assert COACHES_PROFILE_PAGE.get_repeated_behaviors_text() == "REPEATED BEHAVIORS"
    assert COACHES_PROFILE_PAGE.get_coached_events_text() == "COACHED EVENTS"
    assert COACHES_PROFILE_PAGE.get_avg_days_to_coach_text() == "AVG DAYS TO COACH"
    assert COACHES_PROFILE_PAGE.get_with_notes_text() == "WITH NOTES"
    assert COACHES_PROFILE_PAGE.get_coaching_effectiveness_graph_text() == "Coaching Effectiveness (%)"
    assert COACHES_PROFILE_PAGE.get_driver_text() == "DRIVER"
    assert COACHES_PROFILE_PAGE.get_drivers_coaching_effectiveness_text() == "COACHING EFFECTIVENESS"
    assert COACHES_PROFILE_PAGE.get_drivers_behaviors_group_text() == "BEHAVIOR GROUPS"
    assert COACHES_PROFILE_PAGE.get_drivers_coached_behaviors_text() == "COACHED BEHAVIORS"
    assert COACHES_PROFILE_PAGE.get_drivers_repeated_behaviors_text() == "REPEATED BEHAVIORS"


@when('the user clicks Behavior Groups tab')
def go_to_behavior_tab():
    COACHES_PROFILE_PAGE.click_behaviors_group_tab()


@then(
    'the table is displayed with columns:"BEHAVIOR GROUPS","COACHING EFFECTIVENESS","DRIVER","COACHED BEHAVIORS", REPEATED BEHAVIORS')
def verify_behavior_groups_tab():
    assert COACHES_PROFILE_PAGE.get_behavior_group_text() == "BEHAVIOR GROUP"
    assert COACHES_PROFILE_PAGE.get_behavior_coaching_effectiveness_text() == "COACHING EFFECTIVENESS"
    assert COACHES_PROFILE_PAGE.get_behavior_drivers_text() == "DRIVERS"
    assert COACHES_PROFILE_PAGE.get_coached_behaviors_group_text() == "COACHED BEHAVIORS"
    assert COACHES_PROFILE_PAGE.get_repeated_behaviors_group_text() == "REPEATED BEHAVIORS"


# LQ-90415
@when('user clicks on Home button')
def user_clicks_home_tab():
    DASHBOARD_PAGE.click_home_tab()


@then('there is Safe Driving Trend present in Metrics and trend chart is present along with pi-chart')
def verify_safe_driving_trend_metrics():
    assert DASHBOARD_PAGE.get_safe_driving_trend_title(), IsEqualIgnoringCase("Safe Driving Trend")
    assert DASHBOARD_PAGE.graph_is_displayed_in_safe_drive_trend() is True


# LQ-90415
@then(
    'there is Groups by highest % Safe drivers trend is present with columns "GROUP", "% SAFE DRIVERS", "ELIGIBLE FOR RECOGNITION", "RECOGNIZED"')
def verify_groups_by_highest_safe_drivers():
    assert DASHBOARD_PAGE.get_groups_by_highest_safe_drivers_title(), IsEqualIgnoringCase(
            "Groups by Highest % Safe Drivers")
    assert DASHBOARD_PAGE.get_group_text() == "GROUP"
    assert DASHBOARD_PAGE.get_percentage_safe_drivers_text() == "% SAFE DRIVERS"
    assert DASHBOARD_PAGE.get_eligible_for_recognition_text(), IsEqualIgnoringCase("eligible for recognition")
    assert DASHBOARD_PAGE.get_recognized_text(), IsEqualIgnoringCase("recognized")


# LQ-90417
@when('user clicks on group name')
def user_clicks_on_group():
    global group_name
    group_name = DASHBOARD_PAGE.get_safe_driving_widget_first_group_name()
    DASHBOARD_PAGE.click_safe_driving_widget_first_group()


@then('user should navigate to Safe driving report and same group filter applied in the page')
def verify_navigation_from_widget_to_report_page():
    assert SAFE_DRIVING_REPORT_PAGE.group_page_is_displayed_in_safe_driver_report() is True
    assert SAFE_DRIVING_REPORT_PAGE.get_filtered_group_name() == group_name


# LQ-90419
@when('user clicks "Recognize" button in widget')
def user_clicks_recoginse_in_safe_drive_widget():
    DASHBOARD_PAGE.click_home_tab()
    DASHBOARD_PAGE.click_recognise_button()


@then('user should navigate to Safe driving report - drivers page')
def verify_navigation_from_widget_to_safe_drive_report_driver_page():
    assert SAFE_DRIVING_REPORT_PAGE.safe_driving_page_is_displayed() is True
    assert SAFE_DRIVING_REPORT_PAGE.get_text_tooltip_next_to_driver_count() == "Drivers must achieve a specified minimum driving distance and have a coachable score of 0 within the month to be eligible for safety recognition."


# LQ-75797 and  LQ-95442
@when('the user clicks Insights and clicks Safe Driving Report')
def user_opens_safe_driving_report():
    DASHBOARD_PAGE.click_insights_menu()
    DASHBOARD_PAGE.click_safe_driving_report_tab()


@then('the Safe Driving Report page is loaded correctly the table is displayed with columns: "DRIVER", "GROUP", '
      '"DISTANCE DRIVEN", "ACHIEVEMENT", "NON-COACHABLE BEHAVIORS"')
def verify_safe_driving_report():
    assert SAFE_DRIVING_REPORT_PAGE.safe_driving_page_is_displayed() is True
    assert SAFE_DRIVING_REPORT_PAGE.get_driver_text() == "DRIVER"
    assert SAFE_DRIVING_REPORT_PAGE.get_group_text() == "GROUP"
    assert SAFE_DRIVING_REPORT_PAGE.get_distance_driven_text() == "DISTANCE DRIVEN"
    assert SAFE_DRIVING_REPORT_PAGE.get_achievement_text() == "ACHIEVEMENT"
    assert SAFE_DRIVING_REPORT_PAGE.get_non_coachable_behaviors_text() == "NON-COACHABLE BEHAVIORS"


@then('there is a verbiage under the table "Reports are provided for informational purposes only and may vary based on data availability.  Reports may contain data generated by AI, which is not to be used for employment-related decisions without appropriate human supervision."')
def verify_verbiage_below_table():
    assert SAFE_DRIVING_REPORT_PAGE.get_verbiage_text() == "Reports are provided for informational purposes only and may vary based on data availability. Reports may contain data generated by AI, which is not to be used for employment-related decisions without appropriate human supervision."


# LQ-90421
@when('user hover on the Achievement icon')
def hover_on_achievement_icon():
    SAFE_DRIVING_REPORT_PAGE.click_reset()
    SAFE_DRIVING_REPORT_PAGE.hover_on_achievement_icon()


@then('tool-tip named "Coachable Score of X in XX XXXX" is present')
def verify_tool_tip_for_achievement_icon():
    assert_that(SAFE_DRIVING_REPORT_PAGE.get_achievement_icon_text(), contains_string("Coachable Score of"))


# LQ-121697
@when('user click on group filter and user selects one group')
def user_clicks_on_group_filter():
    SAFE_DRIVING_REPORT_PAGE.click_reset()
    SAFE_DRIVING_REPORT_PAGE.click_on_group_filter()
    SAFE_DRIVING_REPORT_PAGE.enter_group_name(ID.group)
    SAFE_DRIVING_REPORT_PAGE.click_select_group()
    SAFE_DRIVING_REPORT_PAGE.click_done()


@then('the data belong to the group are listed in Safe driving Report page')
def verify_data_for_group_filter():
    assert SAFE_DRIVING_REPORT_PAGE.safe_driving_page_is_displayed() is True


# LQ-121697
@when('user clicks on quarter filter button and user selects first quarter')
def user_click_quarter_filter():
    SAFE_DRIVING_REPORT_PAGE.click_reset()
    SAFE_DRIVING_REPORT_PAGE.click_quarter_filter()
    SAFE_DRIVING_REPORT_PAGE.select_first_quarter()


@then('data belong to quarter should be displayed')
def verify_data_for_group_filter():
    assert SAFE_DRIVING_REPORT_PAGE.safe_driving_page_is_displayed() is True


# LQ-121683
@when('user clicks on filter button - include/exclude drivers and user selects first data')
def user_clicks_include_exclude_filter_button():
    SAFE_DRIVING_REPORT_PAGE.click_reset()
    SAFE_DRIVING_REPORT_PAGE.click_include_exclude_filter()
    SAFE_DRIVING_REPORT_PAGE.select_include_filter()


@then('data belongs to drivers should be displayed for include/exclude behaviors')
def verify_data_for_group_filter():
    assert SAFE_DRIVING_REPORT_PAGE.safe_driving_page_is_displayed() is True


# LQ-121682
@when('user clicks and searches the driver name')
def type_driver_name_in_searchbox():
    SAFE_DRIVING_REPORT_PAGE.click_reset()
    SAFE_DRIVING_REPORT_PAGE.search_driver_name("sachin b")
    SAFE_DRIVING_REPORT_PAGE.select_driver_name()


@then('data belongs to driver should displayed')
def verify_data_for_search_driver():
    assert SAFE_DRIVING_REPORT_PAGE.safe_driving_page_is_displayed() is True
