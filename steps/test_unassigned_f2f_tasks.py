from time import sleep

from hamcrest import assert_that, contains_string
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then

from pages.assign_driver_page import AssignDriverPage
from pages.coaching_page import CoachingPage
from pages.dashboard_page import DashboardPage
from pages.driver_profile_page import DriverProfilePage
from pages.events_page import EventsPage
from pages.fyi_notify_page import FyiNotifyPage
from pages.library_page import LibraryPage
from pages.login_page import LoginPage
from steps.common import AutomationDataManager, DC_URL, TestDataEnum, ENV
from data.int.ws_tasks_data_int import TaskDataInt as TD_INT
from data.prod.ws_tasks_data_prod import TaskDataProd as TD_PROD
from data.stg.ws_tasks_data_stg import TaskDataStg as TD_STG

LOGIN_PAGE = 0
COACHING_PAGE = 0
DASHBOARD_PAGE = 0
ASSIGN_DRIVER_PAGE = 0
EVENTS_PAGE = 0
LIBRARY_PAGE = 0
DRIVER_PROFILE_PAGE = 0
FYI_NOTIFY_PAGE = 0
TD = 0
TASK_TEST_DATA = [TestDataEnum.AUTH_TOKEN,
                  TestDataEnum.VAULT_SECRETS,
                  TestDataEnum.F2F_EVENT_1ST,
                  TestDataEnum.F2F_EVENT_2ND,
                  TestDataEnum.F2F_EVENT_3RD,
                  TestDataEnum.F2F_EVENT_4TH,
                  TestDataEnum.SELF_EVENT_1ST]

scenarios('../features/tasks_unassigned_driver_and_f2f_tasks.feature')


# LQ-313
@given('the coach user logs in')
def launch_welcome_login_page(browser):
    global LOGIN_PAGE, COACHING_PAGE, DASHBOARD_PAGE, ASSIGN_DRIVER_PAGE, \
        LIBRARY_PAGE, EVENTS_PAGE, DRIVER_PROFILE_PAGE, FYI_NOTIFY_PAGE, TD

    LOGIN_PAGE = LoginPage(browser)
    COACHING_PAGE = CoachingPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    ASSIGN_DRIVER_PAGE = AssignDriverPage(browser)
    LIBRARY_PAGE = LibraryPage(browser)
    EVENTS_PAGE = EventsPage(browser)
    DRIVER_PROFILE_PAGE = DriverProfilePage(browser)
    FYI_NOTIFY_PAGE = FyiNotifyPage(browser)

    browser.get(DC_URL)

    if ENV == 'int':
        TD = TD_INT
    elif ENV == 'stg':
        TD = TD_STG
    else:
        TD = TD_PROD

    LOGIN_PAGE.enter_username(TD.full_access_user)
    LOGIN_PAGE.enter_password(TD.password)
    LOGIN_PAGE.click_login()
    sleep(20)

    # clear data:
    if DASHBOARD_PAGE.get_unassigned_driver_task_count() != "0":
        DASHBOARD_PAGE.click_unassigned_drivers_link()
        ASSIGN_DRIVER_PAGE.click_assign_driver_checkbox()
        ASSIGN_DRIVER_PAGE.click_assign_selected_button()
        ASSIGN_DRIVER_PAGE.search_assign_driver(TD.driver_user)
        ASSIGN_DRIVER_PAGE.select_searched_driver()
        ASSIGN_DRIVER_PAGE.click_assign()
        sleep(5)
        DASHBOARD_PAGE.click_home_tab()

    if DASHBOARD_PAGE.get_due_for_coaching_task_count() != "0":
        DASHBOARD_PAGE.click_due_for_coaching_link()
        while int(COACHING_PAGE.get_task_count()) > 0:
            DASHBOARD_PAGE.click_coaching_events()
            if COACHING_PAGE.continue_button_is_displayed() is True:
                COACHING_PAGE.click_continue_button()
            COACHING_PAGE.click_video()
            COACHING_PAGE.click_complete_session()
            COACHING_PAGE.click_save_complete_session()
            COACHING_PAGE.click_close_complete_session()
        DASHBOARD_PAGE.click_home_tab()


@when('the user clicks "TASKS" and the user clicks "ASSIGN DRIVERS"')
def click_task():
    # user automation API to prepare events
    global tadm
    tadm = AutomationDataManager()
    tadm.create_test_credentials(TASK_TEST_DATA)
    sleep(20)  # wait for the data that created by the API actually exists in the db

    DASHBOARD_PAGE.click_refresh_button()
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_assign_driver_tab()


@then('the task count is displayed & there is "Assign Selected" button with un-selectable status & there is "Move Group" button with un-selectable status & there are "VEHICLE", "GROUP", "EVENT DATE", "EVENT ID", "BEHAVIORS" column & there are checkbox & "ASSIGN" button for each Assign Driver task')
def verify_task():
    assert ASSIGN_DRIVER_PAGE.get_count() == "5"
    assert ASSIGN_DRIVER_PAGE.get_assign_select_button_text() == "Assign Selected"
    assert ASSIGN_DRIVER_PAGE.get_disabled_status_of_assign_selected_button() == "true"
    assert ASSIGN_DRIVER_PAGE.get_vehicle_text() == "VEHICLE"
    assert ASSIGN_DRIVER_PAGE.get_group_text() == "GROUP"
    assert ASSIGN_DRIVER_PAGE.get_event_date_text() == "EVENT DATE"
    assert ASSIGN_DRIVER_PAGE.get_event_id_text() == "EVENT ID"
    assert_that(ASSIGN_DRIVER_PAGE.get_behavior_text(), IsEqualIgnoringCase("BEHAVIORS"))
    assert_that(ASSIGN_DRIVER_PAGE.get_assign_button_text(), IsEqualIgnoringCase("Assign"))


# LQ-315
@when('the user sets group filter to one group in assign driver page')
def click_filter_by_group():
    ASSIGN_DRIVER_PAGE.click_filter_by_group_button()
    ASSIGN_DRIVER_PAGE.search_filter_by_group(TD.group)
    ASSIGN_DRIVER_PAGE.select_search_filter_by_group()
    ASSIGN_DRIVER_PAGE.click_done_button()


@then('the Assign Driver tasks belong to the group are listed in assign driver page')
def verify_filter_by_group():
    assert_that(ASSIGN_DRIVER_PAGE.get_group_name_text(), contains_string(TD.group))


# LQ-316
@when('coach is able to see Assign Drivers tasks on the dashboard page and clicks on the tasks and directed to the Assign Driver page')
def click_assign_driver():
    ASSIGN_DRIVER_PAGE.click_reset_button()
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_assign_driver_tab()
    ASSIGN_DRIVER_PAGE.click_assign_button()
    ASSIGN_DRIVER_PAGE.search_assign_driver(TD.driver_user)
    ASSIGN_DRIVER_PAGE.select_searched_driver()


@then('coach must successfully assign a driver to an event')
def verify_assign_driver():
    ASSIGN_DRIVER_PAGE.click_assign()


# LQ-317
@when('the user checks some events and the user clicks "Assign Selected" button and the user inputs some characters in input box of pop-up and the user selects one driver and the user clicks "Assign" button')
def batch_assign_driver():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_assign_driver_tab()
    ASSIGN_DRIVER_PAGE.click_assign_driver_checkbox()
    ASSIGN_DRIVER_PAGE.click_third_assign_driver_task_checkbox()
    ASSIGN_DRIVER_PAGE.click_fourth_assign_driver_task_checkbox()
    ASSIGN_DRIVER_PAGE.click_assign_selected_button()
    ASSIGN_DRIVER_PAGE.search_assign_driver(TD.driver_user)
    ASSIGN_DRIVER_PAGE.select_searched_driver()
    ASSIGN_DRIVER_PAGE.click_assign()


@then('these events are assigned to driver')
def verify_batch_assign_driver():
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_events()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(tadm.F2F_EVENT_ID_2ND)
    LIBRARY_PAGE.select_search_event_id_event_list()
    assert_that(LIBRARY_PAGE.get_first_event_driver(), contains_string(TD.driver_user))
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(tadm.F2F_EVENT_ID_3RD)
    LIBRARY_PAGE.select_search_event_id_event_list()
    assert_that(LIBRARY_PAGE.get_first_event_driver(), contains_string(TD.driver_user))
    LIBRARY_PAGE.click_reset_button()


# LQ-266
@given('Safety Manager user is in Driver Safety')
def navigate_to_dashboard_page():
    DASHBOARD_PAGE.click_home_tab()


@when('the user clicks "TASKS" & the user clicks DUE FOR COACHING')
def go_to_due_for_coaching():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_coaching()


@then('the task count is displayed & there are some information on the card')
def verify_coaching_card():
    assert COACHING_PAGE.get_coaching_session_title() == "DUE FOR COACHING"
    assert_that(COACHING_PAGE.get_task_coaching_label(), contains_string("Task"))
    assert COACHING_PAGE.get_driver_name_card_label() == TD.driver_user
    assert COACHING_PAGE.get_group_card_label() == "GROUP"
    assert COACHING_PAGE.get_vehicle_card_label() == "VEHICLE"
    assert COACHING_PAGE.get_event_date_card_label() == "EVENT DATE"
    assert COACHING_PAGE.get_time_card_label() == "TIME"
    assert COACHING_PAGE.get_overdue_date_card_label() == "OVERDUE DATE"
    assert COACHING_PAGE.get_behaviors_card_label() == "BEHAVIORS"
    assert COACHING_PAGE.get_no_coach_events_card_label() == "Coach Event"


# LQ-274
@given('Safety Manager user is in Due For Coaching page')
def navigate_to_coaching_page():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_coaching()


@when('the user clicks "Coach X Events" of the first bundle card')
def go_to_driver_coaching_session():
    DASHBOARD_PAGE.click_coaching_events()


@then('the Driver Coaching Session page is opened &  there is driver info in the page')
def verify_coaching_session():
    assert COACHING_PAGE.get_driver_coaching_session_label() == "DRIVER COACHING SESSION"
    assert COACHING_PAGE.get_driver_name_label() == TD.driver_user
    assert COACHING_PAGE.get_employee_id_label() == "EMPLOYEE ID"
    assert COACHING_PAGE.get_group_label() == "GROUP"
    assert COACHING_PAGE.get_email_label() == "EMAIL"
    assert COACHING_PAGE.get_coaching_history_label() == "Coaching History - Last 180 Days"
    assert COACHING_PAGE.get_event_video_label() == "Event Video"
    assert COACHING_PAGE.get_video_section_label() == "Inside + Outside"
    assert COACHING_PAGE.get_share_label() == "Share"
    assert COACHING_PAGE.get_add_recognition_label() == "Add Recognition"
    assert COACHING_PAGE.get_contact_lytx_label() == "Contact Lytx"
    assert COACHING_PAGE.get_more_actions_label() == "More Actions"
    assert COACHING_PAGE.get_behaviors_label() == "BEHAVIORS"
    assert COACHING_PAGE.get_event_date_label() == "EVENT DATE"
    assert COACHING_PAGE.get_event_label() == "EVENT"
    assert COACHING_PAGE.get_status_label() == "STATUS"
    assert COACHING_PAGE.get_trigger_label() == "TRIGGER"
    assert COACHING_PAGE.get_score_label() == "SCORE"
    assert COACHING_PAGE.get_lytx_comments_label() == "Lytx Comments"
    assert COACHING_PAGE.get_events_notes_label() == "Event Notes"
    assert COACHING_PAGE.get_complete_coaching_message_label() == "To complete a coaching session, at least one event must be viewed."


# LQ-267
@given('Safety Manager user is back in Due For Coaching page')
def navigate_back_to_coaching_page():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_coaching()


@when('the user sets group filter to one group')
def sets_group_filter():
    COACHING_PAGE.click_coaching_filter_by_group()
    COACHING_PAGE.search_coaching_filter_by_group(TD.group)
    COACHING_PAGE.select_search_coaching_filter_by_group()
    COACHING_PAGE.click_done_button_filter_by_group()


@then('the data belong to the group are listed')
def verify_group_filter():
    assert_that(COACHING_PAGE.get_group_name_card(), contains_string(TD.group))


@when('the user sets trigger filter to one trigger')
def sets_trigger_filter():
    COACHING_PAGE.click_coaching_reset_filter()
    COACHING_PAGE.click_triggers_filter()
    COACHING_PAGE.select_triggers_filter()
    COACHING_PAGE.click_tasks_label()


@then('the data belong to the trigger are listed')
def verify_trigger_filter():
    assert COACHING_PAGE.get_filter_message_text() == "There are no Due for Coaching tasks with the selected criteria."
    COACHING_PAGE.click_coaching_reset_filter()


@when('the user sets behavior filter to one behavior')
def sets_behavior_filter():
    COACHING_PAGE.click_coaching_reset_filter()
    COACHING_PAGE.click_behaviors_filter()
    COACHING_PAGE.select_behaviors_filter()
    COACHING_PAGE.click_tasks_label()


@then('the data belong to the behavior are listed')
def verify_behavior_filter():
    assert COACHING_PAGE.get_filter_message_text() == "There are no Due for Coaching tasks with the selected criteria."
    COACHING_PAGE.click_coaching_reset_filter()


@when('the user enters some characters into "Search Name or ID" field')
def sets_search_name_filter():
    COACHING_PAGE.click_coaching_reset_filter()
    COACHING_PAGE.search_name_filter(TD.driver_user)


@then('the data that have the inputted characters in their name or employeeid are shown')
def verify_search_name_filter():
    assert COACHING_PAGE.get_driver_name_card_label() == TD.driver_user
    COACHING_PAGE.click_coaching_reset_filter()


# LQ-6905
@given('coach is on Driver Coaching Session page')
def navigate_to_coaching_session_page():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_coaching()
    DASHBOARD_PAGE.click_coaching_events()


@when('coach clicks on share button')
def share_video():
    COACHING_PAGE.click_video()
    COACHING_PAGE.click_share()


@then('coach must successfully share a coaching event')
def video_is_shared():
    COACHING_PAGE.click_share_copy()
    COACHING_PAGE.click_share_close()
    COACHING_PAGE.click_add_session_tab()
    COACHING_PAGE.send_share_event_link()
    COACHING_PAGE.click_event_notes_submit()
    assert_that(COACHING_PAGE.get_share_event_link(), contains_string(TD.share_event_link))
    assert TD.share_event_link in COACHING_PAGE.get_share_event_link()


# LQ-312
@when('coach clicks on Add Recognition Tab')
def go_to_add_recognition():
    COACHING_PAGE.click_add_recognition_button()


@then('coach must successfully Add Recognition to a coaching event')
def add_recognition():
    COACHING_PAGE.clear_reason_text_box()
    COACHING_PAGE.send_reason_text_box("Thanks for great accomplishment")
    COACHING_PAGE.click_complete_recognition()
    assert COACHING_PAGE.get_recognition_message() == "Thanks for great accomplishment"
    COACHING_PAGE.click_delete_recognition()
    COACHING_PAGE.click_close_recognition()


# LQ-268
@when('coach clicks on Contact Lytx Tab')
def go_to_contact_lytx():
    COACHING_PAGE.click_contact_lytx()


@then('coach must successfully fill out and submit the Contact Lytx form')
def submit_contact_lytx_form():
    COACHING_PAGE.select_contact_issue()
    COACHING_PAGE.select_other_concern()
    COACHING_PAGE.send_contact_message("Unable to coach")
    COACHING_PAGE.click_contact_submit()
    assert COACHING_PAGE.get_contact_submit_message() == "Your request was successfully submitted"
    COACHING_PAGE.click_contact_done()


# LQ-275
@when('the user plays the video and the user adds event notes and the user adds session notes and the user clicks "Complete Session"')
def coaching_event():
    COACHING_PAGE.click_video()
    COACHING_PAGE.click_add_events()
    COACHING_PAGE.send_event_notes("Coaching was successful")
    COACHING_PAGE.click_event_notes_submit()
    COACHING_PAGE.click_add_session_tab()
    COACHING_PAGE.send_session_text("Coaching was successful")
    COACHING_PAGE.click_submit_button()
    COACHING_PAGE.click_complete_session()
    COACHING_PAGE.click_save_complete_session()


@then('the event is successfully coached')
def assert_coach_event():
    assert COACHING_PAGE.get_complete_session_message() == "Coaching session saved."
    COACHING_PAGE.click_close_complete_session()

@given('the user clicks "LIBRARY" and then clicks "COACHING HISTORY"')
def navigate_to_coaching_history():
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_coaching_history()

@when('the user selects the "Coach" from "Select Search" drop down list in CH and the user inputs a valid coach name and the user selects that value from suggested list')
def search_coach_in_coaching_history():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.select_dropdown_ch()
    LIBRARY_PAGE.select_coach()
    LIBRARY_PAGE.enter_coach_name(TD.full_access_user)
    LIBRARY_PAGE.select_coach_in_dropdown()


@then('the coaching date is correct')
def verify_coaching_date():
    assert_that(LIBRARY_PAGE.get_coaching_date_text_coaching_history_tab(), contains_string(LIBRARY_PAGE.get_time_today()))


# LQ-573
@when('coach clicks on Add Event Note button')
def go_to_event_note():
    COACHING_PAGE.click_add_events()


@then('coach must successfully add Event notes to a coaching event')
def add_event_note():
    COACHING_PAGE.send_event_notes("Coaching was successful")
    COACHING_PAGE.click_event_notes_submit()
    assert COACHING_PAGE.get_event_note() == "Coaching was successful"


@when('coach clicks on Add Session Note button')
def go_to_add_session():
    COACHING_PAGE.click_add_session_tab()


@then('coach must successfully add Session notes to a coaching event')
def add_session():
    COACHING_PAGE.send_session_text("Coaching was successful")
    COACHING_PAGE.click_submit_button()
    assert COACHING_PAGE.get_session_note() == "Coaching was successful"


# LQ-574
@when('coach clicks on Complete session button')
def go_to_complete_session():
    COACHING_PAGE.click_video()


@then('coach must successfully complete a coaching session event')
def complete_session():
    COACHING_PAGE.click_complete_session()
    COACHING_PAGE.click_save_complete_session()
    assert COACHING_PAGE.get_complete_session_message() == "Coaching session saved."
    COACHING_PAGE.click_close_complete_session()


# LQ-5543
@given('the "Coach" user is in event preview')
def navigate_to_event_preview():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_coaching()
    DASHBOARD_PAGE.click_coaching_events()


@when('the user selects "Marked as Self Coaching" from more action & the user clicks "Yes, Confirm" button')
def click_on_self_coaching_tab(context):
    context['EVENT_ID'] = COACHING_PAGE.get_event_id()
    COACHING_PAGE.click_more_actions_tab()
    COACHING_PAGE.click_self_coaching_tab()
    COACHING_PAGE.click_confirm_self_coaching_button()


@then('the event status is changed to self coaching')
def verify_self_coaching_status(context):
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_events()
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(context['EVENT_ID'])
    LIBRARY_PAGE.select_search_event_id_event_list()
    assert LIBRARY_PAGE.get_first_event_status() == "Self Coaching"

    LIBRARY_PAGE.click_reset_button()


# LQ-1994
@given('driver with an F2F status event')
def driver_with_f2f_event():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_coaching()


@when('the coach user clicks kebab in the task card & the user clicks "Notify Driver" & the user clicks "Notify"')
def click_notify_driver():
    COACHING_PAGE.click_kebab_icon()
    COACHING_PAGE.click_notify_driver()
    COACHING_PAGE.click_notify_button()


@then('the event status is "Remote Coaching : Driver Notified"')
def verify_remote_driver_notified_event_status():
    DASHBOARD_PAGE.click_coaching_events()
    assert COACHING_PAGE.get_remote_event_status() == "Remote Coaching : Driver Notified"

    # clear data
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_fyi_notify_tab()
    while FYI_NOTIFY_PAGE.get_fyi_task_count() != "0":
        FYI_NOTIFY_PAGE.click_preview_button()
        FYI_NOTIFY_PAGE.click_resolve_button()
        FYI_NOTIFY_PAGE.click_confirm_button()
        if FYI_NOTIFY_PAGE.close_preview_button_displayed() is True:
            FYI_NOTIFY_PAGE.close_preview_page()


# 17902
@given('the Full Access user is in Events page there are some F2F events filtered out')
def fileter_F2F_Event():
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_events()
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(tadm.F2F_EVENT_ID_4TH)
    LIBRARY_PAGE.select_search_event_id_event_list()


@when(
    'the user clicks one F2F event id and the user clicks "More Actions" button the user clicks "Mark as FYI Notify" option and the user clicks "Yes,Confirm"')
def set_mark_as_fyi_notify():
    LIBRARY_PAGE.click_event_id()
    LIBRARY_PAGE.click_more_actions()
    LIBRARY_PAGE.click_mark_as_fyi_notify()
    LIBRARY_PAGE.click_confirm_mark_as_fyi_notify()
    LIBRARY_PAGE.close_preview_window()


@then('the F2F status event changes to FYI Notify')
def assert_mark_as_fyi_notify():
    assert LIBRARY_PAGE.get_first_event_status() == "FYI Notify"


@given('the Full Access user is in Events page there are some self-coaching events filtered out')
def filter_self_coaching_event():
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(tadm.SELF_EVENT_ID_1ST)
    LIBRARY_PAGE.select_search_event_id_event_list()


@when(
    'the user clicks one self-coaching event id and the user clicks "More Actions" button the user clicks "Mark as FYI Notify" option and the user clicks "Yes,Confirm"')
def set_mark_as_fyi_notify_for_self_coaching():
    LIBRARY_PAGE.click_event_id()
    LIBRARY_PAGE.click_more_actions()
    LIBRARY_PAGE.click_mark_as_fyi_notify()
    LIBRARY_PAGE.click_confirm_mark_as_fyi_notify()
    LIBRARY_PAGE.close_preview_window()


@then('the Self Coaching status event changes to FYI Notify')
def assert_mark_as_fyi_notify_for_self_coaching():
    assert LIBRARY_PAGE.get_first_event_status() == "FYI Notify"

    LIBRARY_PAGE.click_event_id()
    LIBRARY_PAGE.click_coach_later()
    LIBRARY_PAGE.click_yes_confirm_button()


@given('the Full Access user is in Due for coaching page')
def go_to_due_for_coaching_page():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_fyi_notify_tab()
    FYI_NOTIFY_PAGE.click_kebab()
    FYI_NOTIFY_PAGE.select_reassign_driver()
    FYI_NOTIFY_PAGE.search_driver(TD.driver_user)
    FYI_NOTIFY_PAGE.select_search_driver()
    FYI_NOTIFY_PAGE.click_assign_button()
    FYI_NOTIFY_PAGE.click_preview_button()
    FYI_NOTIFY_PAGE.click_coach_later_button()
    FYI_NOTIFY_PAGE.click_confirm_button()
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_coaching()


@when(
    'the user previews F2F event and the user clicks "More Actions" button and the user clicks "Mark as FYI Notify" option and the user clicks "Yes,Confirm"')
def mark_as_fyi_notify_on_due_for_coaching():
    COACHING_PAGE.click_preview_button()
    COACHING_PAGE.click_event_id_filter()
    COACHING_PAGE.select_event_id()
    COACHING_PAGE.click_more_actions_event_preview_page()
    COACHING_PAGE.click_mark_as_fyi_notify()
    COACHING_PAGE.click_yes_confirm_button()
    COACHING_PAGE.close_preview_page()


@then('the previewed F2F events move to FYI Notify task')
def assert_mark_as_fyi_notify_due_for_coaching_page():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_fyi_notify_tab()
    assert FYI_NOTIFY_PAGE.get_fyi_task_count() == "1"

    # clear data
    FYI_NOTIFY_PAGE.click_preview_button()
    FYI_NOTIFY_PAGE.click_resolve_button()
    FYI_NOTIFY_PAGE.click_confirm_button()


@given('the Full Access user is in Assign Drivers page')
def go_to_assign_driver_page():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_assign_driver_tab()


@when(
    'the user previews one event and the user clicks "More Actions" button and the user clicks "Mark as FYI Notify" option and the user clicks "Yes,Confirm"')
def mark_as_fyi_notify_assign_driver_page():
    ASSIGN_DRIVER_PAGE.click_preview_button()
    ASSIGN_DRIVER_PAGE.click_more_actions_button()
    ASSIGN_DRIVER_PAGE.click_mark_as_fyi_notify()
    ASSIGN_DRIVER_PAGE.click_yes_confirm_button()
    ASSIGN_DRIVER_PAGE.close_preview_page()


@then('the previewed events move to FYI Notify task')
def assert_mark_as_fyi_notify_assign_driver_page():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_fyi_notify_tab()
    assert FYI_NOTIFY_PAGE.get_fyi_task_count() == "1"

    # clear data
    FYI_NOTIFY_PAGE.click_preview_button()
    FYI_NOTIFY_PAGE.click_resolve_button()
    FYI_NOTIFY_PAGE.click_confirm_button()


# LQ-311
@given('"Driver" user is in Driver Profile page')
def go_to_driver_profile():
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_coach_sign_out()
    LOGIN_PAGE.enter_username(TD.driver_user_name)
    LOGIN_PAGE.enter_password(TD.password)
    sleep(10)
    LOGIN_PAGE.click_login()
    sleep(20)


@when('the user clicks "View Remote Events" button and the user plays video on event preview modal')
def driver_view_remote_event():
    DRIVER_PROFILE_PAGE.click_view_remote_event_button()
    DRIVER_PROFILE_PAGE.play_video()
    DRIVER_PROFILE_PAGE.click_expand_icon()


@then('the event status is updated to "Remote Coaching: Driver Viewed"')
def verify_remote_driver_viewed_event_status():
    DRIVER_PROFILE_PAGE.close_preview_modal()
    DRIVER_PROFILE_PAGE.click_view_remote_event_button()
    assert DRIVER_PROFILE_PAGE.get_event_status() == "Remote Coaching : Driver Viewed"
    DRIVER_PROFILE_PAGE.close_preview_modal()


# LQ-5544
@given('"Driver" user is in Due For Coaching page')
def driver_in_due_for_coaching_page():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_coaching()


@when('the user clicks "Coach Event" & the user clicks "Complete Session"')
def driver_self_coaching():
    DASHBOARD_PAGE.click_coaching_events()
    COACHING_PAGE.click_video()
    COACHING_PAGE.click_add_events()
    COACHING_PAGE.send_event_notes("Self coaching was successful")
    COACHING_PAGE.click_submit_button()
    COACHING_PAGE.click_add_session_tab()
    COACHING_PAGE.send_session_text("Self coaching was successful")
    COACHING_PAGE.click_submit_button()
    COACHING_PAGE.click_complete_session()
    COACHING_PAGE.click_save_complete_session()


@then('the event is coached')
def assert_driver_self_coaching():
    assert COACHING_PAGE.get_complete_session_message() == "Coaching session saved."
    COACHING_PAGE.click_close_complete_session()

    # clear the remote event:
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_driver_sign_out()
    LOGIN_PAGE.enter_username(TD.coach_user)
    LOGIN_PAGE.enter_password(TD.password)
    LOGIN_PAGE.click_login()
    sleep(20)

    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_coaching()
    DASHBOARD_PAGE.click_coaching_events()
    COACHING_PAGE.click_video()
    COACHING_PAGE.click_complete_session()
    COACHING_PAGE.click_save_complete_session()
