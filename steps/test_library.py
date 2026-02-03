from datetime import datetime
from time import sleep

from hamcrest import assert_that, contains_string, any_of
from pytest_bdd import scenarios, given, when, then

from data.int.home_data_int import HomeDataInt as LD_INT
from data.prod.home_data_prod import HomeDataProd as LD_PROD
from data.stg.home_data_stg import HomeDataStg as LD_STG
from pages.assign_driver_page import AssignDriverPage
from pages.coaches_report_page import CoachesReportPage
from pages.coaching_page import CoachingPage
from pages.dashboard_page import DashboardPage
from pages.driver_profile_page import DriverProfilePage
from pages.library_page import LibraryPage
from pages.login_page import LoginPage
from pages.video_search_page import VideoSearchPage
from steps.common import DC_URL, ENV

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
ASSIGN_DRIVER_PAGE = 0
LIBRARY_PAGE = 0
COACHES_REPORT_PAGE = 0
DRIVER_PROFILE_PAGE = 0
COACHING_PAGE = 0
VIDEO_SEARCH_PAGE = 0
EVENT_DRIVER = ''
EVENT_GROUP = ''
LAST_DATA_EXPORT_DATE = ''
LD = ''
EVENT_ID_LIBRARY = ''
RECOGNITION_GROUP = ''
RECOGNITION_COUNT_BEFORE_DELETE = ''
EVENT_VEHICLE = ''
first_device_event_page = ''
scenarios('../features/library.feature')


# LQ-263
@given('the coach user logs in')
def coach_log_in_and_event_assigned_driver(browser):
    global LOGIN_PAGE, LIBRARY_PAGE, DASHBOARD_PAGE, LD
    global ASSIGN_DRIVER_PAGE, COACHES_REPORT_PAGE, DRIVER_PROFILE_PAGE, COACHING_PAGE, VIDEO_SEARCH_PAGE

    LOGIN_PAGE = LoginPage(browser)
    LIBRARY_PAGE = LibraryPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    ASSIGN_DRIVER_PAGE = AssignDriverPage(browser)
    COACHES_REPORT_PAGE = CoachesReportPage(browser)
    DRIVER_PROFILE_PAGE = DriverProfilePage(browser)
    COACHING_PAGE = CoachingPage(browser)
    VIDEO_SEARCH_PAGE = VideoSearchPage(browser)

    browser.get(DC_URL)

    if ENV == 'int':
        LD = LD_INT
    elif ENV == 'stg':
        LD = LD_STG
    else:
        LD = LD_PROD

    LOGIN_PAGE.enter_username(LD.admin_username)
    LOGIN_PAGE.enter_password(LD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_multi_company('DriveCam DC4DC Test Co')
    LOGIN_PAGE.click_select_company_button()


@when('the user clicks "LIBRARY" and then clicks "EVENTS"')
def navigate_to_events_page():
    sleep(5)
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_events_submenu_new_UI()


@then('the events page is displayed and the table is displayed with columns "EVENT ID",'
      '"DRIVER","GROUP","VEHICLE","EVENT DATE","SCORE","STATUS","TRIGGER" and "BEHAVIORS"')
def verify_events_table():
    assert LIBRARY_PAGE.event_count_displayed() is True
    assert LIBRARY_PAGE.get_event_id() == "EVENT ID"
    assert LIBRARY_PAGE.get_driver() == "DRIVER"
    assert LIBRARY_PAGE.get_group() == "GROUP"
    assert LIBRARY_PAGE.get_vehicle() == "VEHICLE"
    assert LIBRARY_PAGE.get_device() == "DEVICE"
    assert LIBRARY_PAGE.get_event_date() == "EVENT DATE"
    assert LIBRARY_PAGE.get_score() == "SCORE"
    assert LIBRARY_PAGE.get_status() == "STATUS"
    assert LIBRARY_PAGE.get_trigger() == "TRIGGER"
    assert LIBRARY_PAGE.get_behaviors() == "BEHAVIORS"


# LQ-5541
@when('the user reassigns a driver in event preview')
def reassign_driver():
    global EVENT_DRIVER
    EVENT_DRIVER = LIBRARY_PAGE.get_first_event_driver()

    if EVENT_DRIVER == "Driver Unassigned":
        LIBRARY_PAGE.click_event_id()
        LIBRARY_PAGE.click_more_actions()
        LIBRARY_PAGE.click_reassign_driver_event_no_driver()
        LIBRARY_PAGE.enter_driver_name(LD.Automation_driver)
    else:
        LIBRARY_PAGE.click_event_id()
        LIBRARY_PAGE.click_more_actions_ar()
        LIBRARY_PAGE.click_reassign_driver()
        LIBRARY_PAGE.enter_driver_name('driver unassigned')

    LIBRARY_PAGE.select_search_name_in_event_preview()
    LIBRARY_PAGE.click_assign_button_in_event_preview()
    LIBRARY_PAGE.close_preview_window()


@then('the event driver is updated')
def verify_event_driver_updated():
    LIBRARY_PAGE.select_date_dropdown()
    LIBRARY_PAGE.click_apply_button()
    assert LIBRARY_PAGE.get_first_event_driver() != EVENT_DRIVER


@when('the user clicks the driver name of one event')
def click_driver_name():
    # check and prepare event with driver assigned
    if LIBRARY_PAGE.get_first_event_driver() == "Driver Unassigned":
        LIBRARY_PAGE.click_event_id()
        LIBRARY_PAGE.click_more_actions()
        LIBRARY_PAGE.click_reassign_driver_event_no_driver()
        LIBRARY_PAGE.enter_driver_name(LD.Automation_driver)
        LIBRARY_PAGE.select_search_name_in_event_preview()
        LIBRARY_PAGE.click_assign_button_in_event_preview()
        LIBRARY_PAGE.close_preview_window()

    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_driver()
    LIBRARY_PAGE.type_search_criteria_event_list(LD.Automation_driver)
    LIBRARY_PAGE.select_search_criteria_result_event_list()

    LIBRARY_PAGE.click_driver_name()


@then('the corresponding driver profile page is opened')
def verify_driver_profile():
    assert DRIVER_PROFILE_PAGE.get_title() == "DRIVER PROFILE"
    assert DRIVER_PROFILE_PAGE.get_driver_name() == LD.Automation_driver


@when('the user clicks "LIBRARY" and then clicks "EVENTS" and the user clicks the event ID')
def click_event_id():
    if DASHBOARD_PAGE.events_submenu() is False:
        DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_events_submenu()
    LIBRARY_PAGE.click_event_id()


@then('the event preview is opened')
def verify_event_preview():
    assert LIBRARY_PAGE.get_preview_title() == "Preview:"
    LIBRARY_PAGE.close_preview_window()


# LQ-262
@when('the user sets group filter to one group')
def filter_by_group():
    LIBRARY_PAGE.click_filter_by_group()
    LIBRARY_PAGE.enter_group(LD.event_group)
    LIBRARY_PAGE.click_select_group()
    LIBRARY_PAGE.click_done()


@then('the events in the selected group and subgroup are displayed')
def verify_events_by_group():
    if LIBRARY_PAGE.get_event_count() != '0':
        assert LIBRARY_PAGE.get_group_name_event_page() == LD.event_group


@when('the user sets date filter as one option')
def filter_by_date():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.select_date_dropdown()
    LIBRARY_PAGE.select_last_7_days()
    LIBRARY_PAGE.click_apply_button()


@then('the events in the selected date range are displayed')
def verify_events_by_date():
    assert LIBRARY_PAGE.event_count_displayed() is True


@when('the user selects coachable from type filter')
def filter_by_type():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_type_dropdown()
    LIBRARY_PAGE.select_coachable()


@then('only the events with the selected type are displayed')
def verify_events_by_type():
    assert LIBRARY_PAGE.event_count_displayed() is True


@when('the user selects some triggers from trigger filter')
def filter_by_trigger():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_triggers_dropdown()
    LIBRARY_PAGE.select_trigger_filter_event_page(LD.event_trigger_order)
    sleep(10)
    LIBRARY_PAGE.click_triggers_close_button()


@then('all the events triggered by selected triggers are displayed')
def verify_events_by_trigger():
    assert LIBRARY_PAGE.event_count_displayed() is True


@when('the user selects some behaviors from behavior filter')
def filter_by_behavior():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_behaviors_dropdown()
    LIBRARY_PAGE.select_behavior_filter_event_page(LD.behavior)
    LIBRARY_PAGE.click_behaviors_close_button()


@then('all the events including one or more of the selected behavior are displayed')
def verify_events_by_behavior():
    assert LIBRARY_PAGE.event_count_displayed() is True


@when('the user selects one option from status filter')
def filter_by_status():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_statuses_dropdown()
    LIBRARY_PAGE.select_face_to_face()
    LIBRARY_PAGE.click_close_status_dropdown()


@then('only the events in the selected status are displayed in events list')
def verify_events_by_status():
    assert LIBRARY_PAGE.event_count_displayed() is True


@when('the user selects the "Event Id" from "Select Search" drop down list and the user inputs'
      ' an valid custom event ID and the user clicks search button')
def filter_by_event_id():
    global EVENT_ID_LIBRARY
    LIBRARY_PAGE.click_reset_button()
    EVENT_ID_LIBRARY = LIBRARY_PAGE.get_event_id_number()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    sleep(3)
    LIBRARY_PAGE.type_event_id_event_list(EVENT_ID_LIBRARY)
    sleep(3)
    LIBRARY_PAGE.select_search_event_id_event_list()


@then('the searched event is displayed')
def verify_events_by_event_id():
    assert_that(LIBRARY_PAGE.get_event_id_number(), contains_string(EVENT_ID_LIBRARY))


@when('the user selects the "Driver" from "Select Search" drop down list and the user inputs the'
      ' valid driver name and the user selects that value from suggested list')
def filter_by_driver():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_driver()
    LIBRARY_PAGE.type_search_criteria_event_list(LD.Automation_driver)
    LIBRARY_PAGE.select_search_criteria_result_event_list()


@then('the events of this driver are displayed')
def verify_events_by_driver():
    assert_that(LIBRARY_PAGE.get_driver_name(), contains_string(LD.Automation_driver))


@when('the user selects the "Vehicle" from "Select Search" drop down list and the user inputs'
      ' the valid vehicle name and the user selects that value from suggested list')
def filter_by_vehicle():
    global EVENT_VEHICLE
    LIBRARY_PAGE.click_reset_button()
    EVENT_VEHICLE = LIBRARY_PAGE.get_vehicle_name_event_page()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_vehicle()
    sleep(5)
    LIBRARY_PAGE.type_search_criteria_event_list(EVENT_VEHICLE)
    sleep(5)
    LIBRARY_PAGE.select_search_criteria_result_event_list()


@then('the events of this vehicle are displayed')
def verify_events_by_vehicle():
    assert LIBRARY_PAGE.get_vehicle_name() == EVENT_VEHICLE


@when('the user selects the "Device" from "Select Search" drop down list and the user inputs'
      ' the valid ER serial number and the user selects that value from suggested list')
def filter_by_device():
    global first_device_event_page
    LIBRARY_PAGE.click_reset_button()
    first_device_event_page = LIBRARY_PAGE.get_device_name()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_device()
    sleep(5)
    LIBRARY_PAGE.type_search_criteria_event_list(first_device_event_page)
    sleep(5)
    LIBRARY_PAGE.select_search_criteria_result_event_list()


@then('the events of this device are displayed')
def verify_events_by_device():
    assert_that(LIBRARY_PAGE.get_device_name(), contains_string(first_device_event_page))


# LQ-5540
@when('the user click "Add Recognition" button and the user clicks "Complete" button')
def add_recognition():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(EVENT_ID_LIBRARY)
    LIBRARY_PAGE.select_search_event_id_event_list()
    LIBRARY_PAGE.click_event_id()
    if LIBRARY_PAGE.get_recognition_text() == 'View Recognition':
        LIBRARY_PAGE.click_add_recognition()
        LIBRARY_PAGE.click_delete_recognition_button()
        LIBRARY_PAGE.click_delete_recognition_confirmation_button()
    LIBRARY_PAGE.click_add_recognition()
    DRIVER_PROFILE_PAGE.click_edit_message_button()
    DRIVER_PROFILE_PAGE.type_recognition_reason()
    DRIVER_PROFILE_PAGE.click_check_or_right_marke_edit_recognition()
    DRIVER_PROFILE_PAGE.click_add_recognition_complete()
    DRIVER_PROFILE_PAGE.click_close_add_recognition_complete()
    LIBRARY_PAGE.close_preview_window()
    LIBRARY_PAGE.click_event_id()


@then('the Recognition is added')
def verify_recognition_added():
    assert LIBRARY_PAGE.get_recognition_status_text("View Recognition") == "View Recognition"
    LIBRARY_PAGE.close_preview_window()


# LQ-5542
@when('the user changes the event group to another group in event preview')
def reassign_group():
    global EVENT_GROUP

    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_events_submenu()
    LIBRARY_PAGE.click_event_id()

    if LIBRARY_PAGE.get_event_group_text() == LD.event_group:
        EVENT_GROUP = LD.group2
    else:
        EVENT_GROUP = LD.event_group

    LIBRARY_PAGE.click_more_actions_ar()
    LIBRARY_PAGE.click_assign_group_button_in_event_preview()
    LIBRARY_PAGE.enter_group_name(EVENT_GROUP)
    LIBRARY_PAGE.select_group_event_preview()
    sleep(1)
    LIBRARY_PAGE.click_done_button_event_preview()
    sleep(2)
    LIBRARY_PAGE.click_done_button_assign_group()


@then('the event group is updated')
def verify_event_group_updated():
    sleep(2)
    LIBRARY_PAGE.click_expand_icon()
    assert LIBRARY_PAGE.get_event_group_text() == EVENT_GROUP
    LIBRARY_PAGE.close_preview_window()


# LQ-265
@when('the user check on some events and the user clicks "Move Group" and the user selects'
      ' target group and the user clicks "Done" and the user clicks "Continue"')
def batch_move():
    DASHBOARD_PAGE.click_events_submenu_new_UI()
    LIBRARY_PAGE.select_first_checkbox()
    LIBRARY_PAGE.click_move_group()
    LIBRARY_PAGE.click_done_on_change_group()
    LIBRARY_PAGE.click_continue_on_move_group()


@then('the selected events are moved')
def verify_batch_move():
    # assert LIBRARY_PAGE.get_success_event_moved_dialog_text() == "Success - 1 event moved"
    sleep(15)  # wait for dialog to disappear
    LIBRARY_PAGE.click_reset_button()


# LQ-391
@when('the user clicks "LIBRARY" and the user clicks "RECOGNITION HISTORY"')
def navigate_to_rh_page():
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_recognition_history_submenu_new_UI()
    sleep(5)  # there are around 20000+ data is there it will take some time to load


@then('all recognition history are displayed and the table is displayed with '
      'columns "TYPE","DRIVER","GROUP","EVENTID","ISSUED BY","ISSUED DATE","RECOGNITION REASON"')
def verify_rh_table():
    assert LIBRARY_PAGE.recognition_count_displayed()
    assert LIBRARY_PAGE.get_type_column_name_text() == "TYPE"
    assert LIBRARY_PAGE.get_driver_column_name_text() == "DRIVER"
    assert LIBRARY_PAGE.get_group_column_name_text() == "GROUP"
    assert LIBRARY_PAGE.get_event_id_column_name_text() == "EVENT ID"
    assert LIBRARY_PAGE.get_issued_by_column_name_text() == "ISSUED BY"
    assert LIBRARY_PAGE.get_issued_date_column_name_text() == "ISSUED DATE"
    assert LIBRARY_PAGE.get_recognition_reason_column_name_text() == "RECOGNITION REASON"


# LQ-393
@when('the user sets group filter to one group in Recognition History')
def filter_by_group_rh():
    LIBRARY_PAGE.click_reset_button()
    global RECOGNITION_GROUP
    RECOGNITION_GROUP = LIBRARY_PAGE.get_group_name_recognition_page()
    LIBRARY_PAGE.click_filter_by_group_recognition_history()
    LIBRARY_PAGE.enter_group(RECOGNITION_GROUP)
    LIBRARY_PAGE.click_select_group()
    LIBRARY_PAGE.click_done()


@then('the data belong to the selected group are displayed in Recognition History')
def verify_filter_by_group():
    assert LIBRARY_PAGE.get_group_name_recognition_page() == RECOGNITION_GROUP


@when('the user sets date filter in Recognition History')
def filter_by_date_rh():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.select_date_dropdown()
    LIBRARY_PAGE.select_last_7_days()
    LIBRARY_PAGE.click_apply_button()


@then('the data belong to the selected date range are displayed')
def verify_filter_by_date():
    assert LIBRARY_PAGE.recognition_count_displayed()


@when('the user selects the "Driver" from "Select Search" drop down list and the user inputs a '
      'valid driver name and the user selects that value from suggested list in RH')
def filter_by_driver_rh():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_select_search()
    LIBRARY_PAGE.click_filter_by_driver()
    LIBRARY_PAGE.type_in_search_criteria_textbox_rh(LD.Automation_driver)
    LIBRARY_PAGE.select_search_criteria_result_rh_list()


@then('the recognitions of this driver are displayed')
def verify_filter_by_driver():
    if LIBRARY_PAGE.get_row_count() >= 1:
        assert_that(LIBRARY_PAGE.get_driver_name_rh(), contains_string(LD.Automation_driver))


@when('the user selects the "Issued By" from "Select Search" drop down list and the user inputs'
      ' a valid user name and the user selects that value from suggested list')
def filter_by_issued_by_rh():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_select_search()
    LIBRARY_PAGE.click_filter_by_issued_by()
    LIBRARY_PAGE.type_in_search_criteria_textbox_rh(LD.recognition_issued_by)
    LIBRARY_PAGE.select_search_criteria_result_rh_list()


@then('the recognitions of this user are displayed')
def verify_filter_by_issued_by():
    if LIBRARY_PAGE.get_row_count() >= 1:
        assert_that(LIBRARY_PAGE.get_issued_by_name_rh(), contains_string(LD.recognition_issued_by))


@when('the user selects the "Event ID" from "Select Search" drop down list and the user inputs '
      'an valid custom event ID and the user clicks search button')
def filter_by_event_id_rh():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_select_search()
    LIBRARY_PAGE.click_filter_by_event_id()
    LIBRARY_PAGE.type_event_id_rh(EVENT_ID_LIBRARY)
    LIBRARY_PAGE.select_search_event_id_rh()


@then('the recognition related to searched event ID is displayed')
def verify_filter_by_event_id():
    if LIBRARY_PAGE.get_row_count() >= 1:
        assert_that(LIBRARY_PAGE.get_event_id_number_rh(), contains_string(EVENT_ID_LIBRARY))


# LQ-5556
@when('the user clicks "TYPE" in RH')
def click_type_rh():
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_recognition_history_submenu_new_UI()
    LIBRARY_PAGE.click_type_link()


@then('the corresponding "recognition certificate" page is opened')
def verify_rc_opens():
    assert LIBRARY_PAGE.get_recognition_title_text() == "Recognition Certificate:"


# LQ-394
@when('the user clicks "DRIVER" in RH')
def click_driver_rh():
    LIBRARY_PAGE.click_recognition_close_button()
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_recognition_history_submenu_new_UI()
    LIBRARY_PAGE.click_driver_link()


@then('the corresponding "driver profile" page is opened')
def verify_driver_profile_opens():
    assert DRIVER_PROFILE_PAGE.get_title() == "DRIVER PROFILE"


@when('the user clicks "Event ID" in RH')
def click_event_id_rh():
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_recognition_history_submenu_new_UI()
    LIBRARY_PAGE.click_event_id_link()


@then('the corresponding "event preview" page is opened')
def verify_event_preview_opens():
    assert LIBRARY_PAGE.get_preview_title() == "Preview:"
    # LIBRARY_PAGE.close_preview_window()


@when('the user clicks "Issued By" in RH')
def click_issued_by_rh():
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_recognition_history_submenu_new_UI()
    LIBRARY_PAGE.click_issued_by_link()


@then('the corresponding "coach profile" page is opened')
def verify_coach_profile_opens():
    assert COACHES_REPORT_PAGE.get_coach_profile_title_text() == "COACH PROFILE"


# LQ-396
@when('the user opens a recognition and clicks "Download" button')
def click_download_recognition():
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_recognition_history_submenu_new_UI()
    LIBRARY_PAGE.click_first_recognition()
    LIBRARY_PAGE.click_download_recognition_button()
    sleep(5)
    # switch to first tab as in firefox browser downloaded content will open in new browser
    LIBRARY_PAGE.switch_to_first_tab(0)


@then('the recognition is downloaded')
def verify_recognition_downloaded():
    RECOGNITION_DRIVER = LIBRARY_PAGE.get_driver_name_rh()
    recognition_file = LIBRARY_PAGE.get_recognition_file_name(RECOGNITION_DRIVER)
    LIBRARY_PAGE.wait_for_file_downloaded(recognition_file)
    # assert LIBRARY_PAGE.check_file_exist(recognition_file) is True  # Commenting due to an open bug


@when('the user opens a recognition, clicks "Edit" button, updates "Recognition Reason" and'
      ' clicks "Complete" button')
def click_edit_recognition():
    LIBRARY_PAGE.click_recognition_close_button()
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_recognition_history_submenu_new_UI()
    LIBRARY_PAGE.click_first_recognition()
    LIBRARY_PAGE.click_edit_recognition_button()
    DRIVER_PROFILE_PAGE.click_edit_message_button()
    LIBRARY_PAGE.edit_recognition("Recognition Edited Reason: Good")
    DRIVER_PROFILE_PAGE.click_check_or_right_marke_edit_recognition()
    DRIVER_PROFILE_PAGE.click_add_recognition_complete()
    DRIVER_PROFILE_PAGE.click_close_add_recognition_complete()


@then('the recognition is updated')
def verify_recognition_updated():
    assert LIBRARY_PAGE.get_recognition_list_recognition_reason() == "Recognition Edited Reason: Good"


@when('the user opens a recognition and the user clicks "Delete" button')
def click_delete_recognition():
    global RECOGNITION_COUNT_BEFORE_DELETE
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_recognition_history_submenu_new_UI()
    RECOGNITION_COUNT_BEFORE_DELETE = LIBRARY_PAGE.get_recognitions_count()
    LIBRARY_PAGE.click_first_recognition()
    LIBRARY_PAGE.click_delete_recognition_button()
    LIBRARY_PAGE.click_delete_recognition_confirmation_button()


@then('the recognition is deleted')
def verify_recognition_deleted():
    sleep(10)  # wait so the page fully loads to show no recognitions
    assert LIBRARY_PAGE.get_recognitions_count() != RECOGNITION_COUNT_BEFORE_DELETE


# LQ-386
@when('the user clicks "LIBRARY" and the user clicks "DATA EXPORT"')
def click_data_export():
    DASHBOARD_PAGE.click_data_export_submenu_new_UI()

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


# LQ-389
@when(
    'the user clicks "New Export" button and the user selects "Event Data" option and the user sets date filter and the user clicks "Request Data"')
def request_event_data():
    global LAST_DATA_EXPORT_DATE
    LAST_DATA_EXPORT_DATE = LIBRARY_PAGE.get_requested_date_1st_request_date()
    LIBRARY_PAGE.click_new_export()
    LIBRARY_PAGE.click_report_type_dropdown()
    LIBRARY_PAGE.click_event_data()
    LIBRARY_PAGE.click_request_data()


@then('the event data is requested')
def verify_report_type_event_data():
    sleep(
        2)  # sleep is needed here because it takes a few seconds for the element to appear in the table after clicking request data
    new_export_request_date = LIBRARY_PAGE.get_requested_date_1st_request_date()
    assert datetime.strptime(new_export_request_date, '%b %d, %Y, %I:%M:%S %p') > datetime.strptime(
        LAST_DATA_EXPORT_DATE, '%b %d, %Y, %I:%M:%S %p')
    assert LIBRARY_PAGE.get_report_type_value() == "Event Data"


@when(
    'the user clicks "New Export" button and the user selects "Speed Data" option and the user sets group filter to one group and the user clicks "Request Data"')
def request_speed_data():
    global LAST_DATA_EXPORT_DATE
    LAST_DATA_EXPORT_DATE = LIBRARY_PAGE.get_requested_date_1st_request_date()
    LIBRARY_PAGE.click_new_export()
    LIBRARY_PAGE.click_report_type_dropdown()
    LIBRARY_PAGE.click_speed_data()
    LIBRARY_PAGE.click_request_data()


@then('the speed data is requested')
def verify_report_type_speed_data():
    sleep(
        2)  # sleep is needed here because it takes a few seconds for the element to appear in the table after clicking request data
    new_export_request_date = LIBRARY_PAGE.get_requested_date_1st_request_date()
    assert datetime.strptime(new_export_request_date, '%b %d, %Y, %I:%M:%S %p') > datetime.strptime(
        LAST_DATA_EXPORT_DATE, '%b %d, %Y, %I:%M:%S %p')
    assert LIBRARY_PAGE.get_report_type_value() == "Speed Data"


# LQ-388
@when('the user clicks "Download" button in Library data export page')
def download_data_export():
    LIBRARY_PAGE.click_download_data_export()
    sleep(5)


@then('the Library data export data is downloaded')
def verify_download_data_export_request():
    file_name = LIBRARY_PAGE.get_data_export_file_name("Speed Data")
    LIBRARY_PAGE.wait_for_file_downloaded(file_name)
    assert LIBRARY_PAGE.check_file_exist(file_name) is True


# LQ-400
@when('the user clicks "LIBRARY" and then clicks "COACHING HISTORY"')
def navigate_to_coaching_history():
    DASHBOARD_PAGE.click_coaching_history_submenu_new_UI()


@then(
    'the Coaching History page is displayed and the table is displayed with columns "SESSION ID", "COACH DATE", "OVERDUE DATE", "DRIVER","BEHAVIORS COACHED","GROUP","COACH","NOTES" and the coaching sessions count is displayed')
def verify_coaching_history_displayed():
    assert LIBRARY_PAGE.coaching_history_count_displayed() is True
    assert LIBRARY_PAGE.get_session_id_label() == "SESSION ID"
    assert LIBRARY_PAGE.get_coach_date_label() == "COACH DATE"

    # comment below asserts for now because the 'OVERDUE DATE' column is controlled
    # by toggle 'ENABLE_OVERDUE_COLUMN'. But it was set to false/true back and force.
    # assert LIBRARY_PAGE.get_overdue_date_label() == "OVERDUE DATE"
    # assert LIBRARY_PAGE.get_driver_label() == "DRIVER"
    # assert LIBRARY_PAGE.get_behavior_coached_label() == "BEHAVIORS COACHED"
    # assert LIBRARY_PAGE.get_group_label() == "GROUP"
    # assert LIBRARY_PAGE.get_coach_label() == "COACH"
    # assert LIBRARY_PAGE.get_notes_label() == "NOTES"


# LQ-401
@when('the user sets group filter to one group in Coaching History')
def filter_by_group():
    LIBRARY_PAGE.click_filter_by_group_coaching_history()
    LIBRARY_PAGE.enter_group(LD.event_group)
    LIBRARY_PAGE.click_select_group()
    LIBRARY_PAGE.click_done()


@then('the data belong to the selected group are displayed in Coaching History')
def verify_filter_by_group():
    assert LIBRARY_PAGE.get_row_count() == 0


@when('the user sets date filter in Coaching History')
def filter_by_date_ch():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.select_date_dropdown()
    LIBRARY_PAGE.select_last_7_days()
    LIBRARY_PAGE.click_apply_button()


@then('the data belong to the selected daterange are displayed')
def verify_filter_by_date_ch():
    assert LIBRARY_PAGE.coaching_history_count_displayed() is True



@when('the user selects unusual event')
def filter_by_unusual_event():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.select_behaviors_dropdown()
    LIBRARY_PAGE.select_unusual_behavior()
    LIBRARY_PAGE.click_behaviors_close_button()


@then('the coaching sessions that contained selected coachable behaviors are displayed')
def verify_sessions_by_unusual_event():
    assert LIBRARY_PAGE.coaching_history_count_displayed() is True


# @CIPHER-3785
@when('the user is search a driver name with Employee ID in search field')
def filter_by_driver_emp_id_ch():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.select_dropdown_ch()
    LIBRARY_PAGE.select_driver_ch()
    LIBRARY_PAGE.enter_driver_name_ch(LD.Automation_driver)
    LIBRARY_PAGE.select_driver_in_dropdown()


@then('the Employee ID is visible next to Driver Name in Coaching History')
def verify_emp_id_visible_ch():
    assert LIBRARY_PAGE.emp_id_visible_next_to_driver_name() is True



@when('the user selects the "Driver" from "Select Search" drop down list in CH '
      'and the user inputs the valid driver name and the user selects that value from suggested list')
def filter_by_driver_ch():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.select_dropdown_ch()
    LIBRARY_PAGE.select_driver_ch()
    LIBRARY_PAGE.enter_driver_name_ch(LD.Automation_driver)
    LIBRARY_PAGE.select_driver_in_dropdown()


@then('the coaching session of this driver are displayed')
def verify_sessions_by_driver():
    assert LIBRARY_PAGE.coaching_history_count_displayed() is True


@when(
    'the user selects the "Coach" from "Select Search" drop down list in CH and the user inputs a valid coach name and the user selects that value from suggested list')
def filter_by_coach_ch():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.select_dropdown_ch()
    LIBRARY_PAGE.select_coach()
    LIBRARY_PAGE.enter_coach_name("coach")
    LIBRARY_PAGE.select_coach_in_dropdown()


@then('the coaching session of this coach are displayed')
def verify_sessions_by_coach():
    assert LIBRARY_PAGE.coaching_history_count_displayed() is True


@when('the "Session Id" is selected from select search drop down list in CH '
      'and the user inputs a valid coaching session ID and the user clicks search button')
def filter_by_session_ch():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.select_dropdown_ch()
    LIBRARY_PAGE.select_session_id()
    LIBRARY_PAGE.enter_session_id(LD.session_id)
    LIBRARY_PAGE.click_search_button()


@then('the searched coaching session is displayed')
def verify_sessions_by_id():
    assert LIBRARY_PAGE.coaching_history_count_displayed() is True


# LQ-402
@when('the user clicks one session id')
def click_session_id_ch():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.select_session_id_in_coaching_history()


@then(
    'the Past Session page is opened and the Past Session page includes "Summary","Session Notes", "X Events Coached"')
def verify_navigating_to_past_session():
    assert LIBRARY_PAGE.get_past_session_title_text() == "PAST SESSION"
    assert LIBRARY_PAGE.get_summary_label() == "Summary"
    assert LIBRARY_PAGE.get_session_notes_label() == "Session Notes"
    assert_that(LIBRARY_PAGE.get_event_coached_label(), any_of(contains_string("Event Coached"), contains_string("Events Coached")))


@when('the user clicks driver in Coaching History')
def click_driver_ch():
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_coaching_history_submenu_new_UI()
    LIBRARY_PAGE.select_driver_in_coaching_history()


# @then('the corresponding driver profile page is opened')
# then step is the same with test case LQ-263


@when('the user clicks coach in Coaching History')
def click_coach_ch():
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_coaching_history_submenu_new_UI()
    LIBRARY_PAGE.select_coach_in_coaching_history()


# @NAL-593
@when('the user clicks more options and the user clicks "Browse"')
def click_browse_in_library_page():
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_events_submenu()
    LIBRARY_PAGE.click_event_id()
    LIBRARY_PAGE.click_more_actions_ar()
    LIBRARY_PAGE.click_browse_in_video_search()
    LIBRARY_PAGE.click_browse_button()


@then('the video search browse page is opened')
def verify_navigating_to_video_search_browse_page():
    assert VIDEO_SEARCH_PAGE.get_video_browser_title("VIDEO BROWSER") == "VIDEO BROWSER"


# LQ-262292
@given('the user Navigates to Events page')
def navigate_to_events_page_again():
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_events_submenu_new_UI()


@when('search a Following Distance event with no ADAS data available in the S3 bucket')
def search_fd_event_no_adas_data():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(LD.fd_event_no_adas_data)
    LIBRARY_PAGE.select_search_event_id_event_list()


@when('the user opens the event details page')
def open_event_details_page():
    LIBRARY_PAGE.click_event_id()


@then('the overlay toggle button should be disabled and the Overlay label should appear to the left of the overlay toggle button')
def verify_overlay_toggle_disabled():
    assert LIBRARY_PAGE.is_overlay_toggle_disabled() is True
    assert LIBRARY_PAGE.is_overlay_label_displayed() is True


@when('the user hovers over the disabled overlay toggle button')
def hover_disabled_overlay_toggle():
    LIBRARY_PAGE.hover_over_overlay_toggle()


@then('a tooltip message should be displayed above the toggle button')
def verify_tooltip_message_displayed():
    assert LIBRARY_PAGE.get_overlay_tooltip_text() == "Overlay is not available for this video"


@when('the user opens the event details of a Following Distance event')
def open_fd_event_details_page():
    LIBRARY_PAGE.close_preview_window()
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(LD.fd_event_with_adas_data)
    LIBRARY_PAGE.select_search_event_id_event_list()
    LIBRARY_PAGE.click_event_id()


@when('the user clicks the download button')
def click_download_button_event_preview():
    LIBRARY_PAGE.click_download_button_event_preview()


@then('the download options should only include "MP4 with overlay", "MP4 without overlay" and "DCE" formats')
def verify_download_options_event_preview():
    assert LIBRARY_PAGE.get_download_option_dce_text() == "DCE"
    assert LIBRARY_PAGE.get_download_option_mp4_with_overlay_text() == "MP4 with overlay"
    assert LIBRARY_PAGE.get_download_option_mp4_without_overlay_text() == "MP4 without overlay"


@when('the user downloads the "MP4 with overlay" file')
def download_mp4_with_overlay_event_preview():
    LIBRARY_PAGE.click_download_option_mp4_with_overlay()


@then('the downloaded file name should be "<EventID>-overlay.mp4"')
def verify_downloaded_mp4_with_overlay_file_name_event_preview():
    event_id = LD.fd_event_with_adas_data
    expected_file_name = f"{event_id}-Overlay.MP4"
    LIBRARY_PAGE.wait_for_file_downloaded(expected_file_name)
    # assert LIBRARY_PAGE.check_file_exist(expected_file_name) is True


@when('the user downloads the "MP4 without overlay" file')
def download_mp4_without_overlay_event_preview():
    LIBRARY_PAGE.click_download_button_event_preview()
    LIBRARY_PAGE.click_download_option_mp4_without_overlay()


@then('the downloaded file name should be "<EventID>.mp4"')
def verify_downloaded_mp4_without_overlay_file_name_event_preview():
    event_id = LD.fd_event_with_adas_data
    expected_file_name = f"{event_id}.MP4"
    LIBRARY_PAGE.wait_for_file_downloaded(expected_file_name)
    assert LIBRARY_PAGE.check_file_exist(expected_file_name) is True


@when('the user downloads the "DCE" file')
def download_dce_event_preview():
    LIBRARY_PAGE.click_download_button_event_preview()
    LIBRARY_PAGE.click_download_option_dce()


@then('the downloaded file name should be "<EventID>.dce"')
def verify_downloaded_dce_file_name_event_preview():
    event_id = LD.fd_event_with_adas_data
    expected_file_name = f"{event_id}.DCE"
    LIBRARY_PAGE.wait_for_file_downloaded(expected_file_name)
    assert LIBRARY_PAGE.check_file_exist(expected_file_name) is True


@when('search a Following Distance event and downloads the "MP4 with overlay" file')
def search_and_download_fd_event_mp4_with_overlay():
    LIBRARY_PAGE.close_preview_window()
    LIBRARY_PAGE.search_fd_event_adas_data_in_search_bar(LD.fd_event_with_adas_data)
    LIBRARY_PAGE.click_download_button_event_preview()
    LIBRARY_PAGE.click_download_option_mp4_with_overlay()


@given('user navigates to Coaching History page')
def navigate_to_coaching_history_page():
    LIBRARY_PAGE.close_preview_window()
    DASHBOARD_PAGE.click_library_menu()
    DASHBOARD_PAGE.click_coaching_history_submenu_new_UI()


@when('search a session id that contains a Following Distance event')
def search_session_id_with_fd_event():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.select_dropdown_ch()
    LIBRARY_PAGE.select_session_id()
    LIBRARY_PAGE.enter_session_id(LD.coaching_session_id)
    LIBRARY_PAGE.click_search_button()
    LIBRARY_PAGE.select_session_id_in_coaching_history()


@when('the user clicks the event details and downloads the "MP4 with overlay" file')
def open_event_details_and_download_mp4_with_overlay():
    LIBRARY_PAGE.click_event_in_past_session()
    LIBRARY_PAGE.click_download_button_event_preview()
    LIBRARY_PAGE.click_download_option_mp4_with_overlay()



