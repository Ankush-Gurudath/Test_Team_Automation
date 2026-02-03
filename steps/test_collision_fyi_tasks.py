from time import sleep

from hamcrest import assert_that, contains_string
from pytest_bdd import scenarios, given, when, then

from pages.assign_driver_page import AssignDriverPage
from pages.coaching_page import CoachingPage
from pages.collisions_page import CollisionsPage
from pages.dashboard_page import DashboardPage
from pages.driver_profile_page import DriverProfilePage
from pages.events_page import EventsPage
from pages.fleet_map_page import FleetMapPage
from pages.fyi_notify_page import FyiNotifyPage
from pages.library_page import LibraryPage
from pages.login_page import LoginPage
from steps.common import AutomationDataManager, DC_URL, TestDataEnum, ENV, WELCOME_URL
from data.int.ws_tasks_data_int import TaskDataInt as TD_INT
from data.prod.ws_tasks_data_prod import TaskDataProd as TD_PROD
from data.stg.ws_tasks_data_stg import TaskDataStg as TD_STG

LOGIN_PAGE = 0
COACHING_PAGE = 0
DASHBOARD_PAGE = 0
ASSIGN_DRIVER_PAGE = 0
COLLISIONS_PAGE = 0
FYI_NOTIFY_PAGE = 0
EVENTS_PAGE = 0
LIBRARY_PAGE = 0
DRIVER_PROFILE_PAGE = 0
TD = 0
TASK_TEST_DATA = [TestDataEnum.AUTH_TOKEN,
                  TestDataEnum.VAULT_SECRETS,
                  TestDataEnum.COLLISION_EVENT_1ST,
                  TestDataEnum.COLLISION_EVENT_2ND,
                  TestDataEnum.FYI_EVENT_1ST,
                  TestDataEnum.FYI_EVENT_2ND,
                  TestDataEnum.FYI_EVENT_3RD,
                  TestDataEnum.POSSIBLE_COLLISION_EVENT_1ST,
                  TestDataEnum.POSSIBLE_COLLISION_EVENT_2ND
                  ]

scenarios('../features/tasks_collision_and_fyi_tasks.feature')


# LQ-304
@given('the welcome login page is displayed')
def launch_welcome_login_page(browser):
    global LOGIN_PAGE, COACHING_PAGE, DASHBOARD_PAGE, ASSIGN_DRIVER_PAGE, COLLISIONS_PAGE, FYI_NOTIFY_PAGE, \
        LIBRARY_PAGE, EVENTS_PAGE, DRIVER_PROFILE_PAGE, DASHBOARD_PAGE, TD

    LOGIN_PAGE = LoginPage(browser)
    COACHING_PAGE = CoachingPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    ASSIGN_DRIVER_PAGE = AssignDriverPage(browser)
    COLLISIONS_PAGE = CollisionsPage(browser)
    FYI_NOTIFY_PAGE = FyiNotifyPage(browser)
    LIBRARY_PAGE = LibraryPage(browser)
    EVENTS_PAGE = EventsPage(browser)
    DRIVER_PROFILE_PAGE = DriverProfilePage(browser)

    browser.get(WELCOME_URL)

    if ENV == 'int':
        TD = TD_INT
    elif ENV == 'stg':
        TD = TD_STG
    else:
        TD = TD_PROD


@when('the "Coach" user inputs name and password and the user clicks "Sign In" button on welcome login page')
def coach_login_through_welcome_page():
    LOGIN_PAGE.enter_username(TD.coach_user_login)
    LOGIN_PAGE.enter_password(TD.password_login)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed(DC_URL, TD.coach_user_login, TD.password_login)


@then('the Driver Safety page is opened')
def verify_DC_login():
    assert DASHBOARD_PAGE.get_driver_safety_title() == "DRIVER SAFETY"
    sleep(5)


# LQ-305
@when('the user clicks "Sign Out" button from DC')
def dc_coach_sign_out():
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_coach_sign_out()


@then('the DC login page is opened')
def verify_DC_logout():
    assert LOGIN_PAGE.get_login_page() == 'SIGN IN'
    assert DASHBOARD_PAGE.lytx_logo_is_displayed_old_ui() is True


# LQ-324
@given('"Safety Manager" user is in Collisions page')
def navigate_to_collisions_page(browser):
    # will delete this until MAFIA-2707 is fixed
    global LOGIN_PAGE, COACHING_PAGE, DASHBOARD_PAGE, ASSIGN_DRIVER_PAGE, COLLISIONS_PAGE, FYI_NOTIFY_PAGE, \
        LIBRARY_PAGE, EVENTS_PAGE, DRIVER_PROFILE_PAGE, FLEET_PAGE, DASHBOARD_PAGE, TD

    LOGIN_PAGE = LoginPage(browser)
    COACHING_PAGE = CoachingPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    ASSIGN_DRIVER_PAGE = AssignDriverPage(browser)
    COLLISIONS_PAGE = CollisionsPage(browser)
    FYI_NOTIFY_PAGE = FyiNotifyPage(browser)
    LIBRARY_PAGE = LibraryPage(browser)
    EVENTS_PAGE = EventsPage(browser)
    DRIVER_PROFILE_PAGE = DriverProfilePage(browser)
    FLEET_PAGE = FleetMapPage(browser)

    browser.get(WELCOME_URL)

    if ENV == 'int':
        TD = TD_INT
    elif ENV == 'stg':
        TD = TD_STG
    else:
        TD = TD_PROD

    #    browser.get(DC_URL)
    LOGIN_PAGE.enter_username(TD.coach_user)
    LOGIN_PAGE.enter_password(TD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed(DC_URL, TD.coach_user, TD.password)

    # clear data:
    if DASHBOARD_PAGE.get_fyi_notify_task_count() != "0":
        DASHBOARD_PAGE.click_fyi_notify_link()
        while FYI_NOTIFY_PAGE.get_fyi_task_count() != "0":
            FYI_NOTIFY_PAGE.click_preview_button()
            FYI_NOTIFY_PAGE.click_resolve_button()
            FYI_NOTIFY_PAGE.click_confirm_button()
            if FYI_NOTIFY_PAGE.close_preview_button_displayed() is True:
                FYI_NOTIFY_PAGE.close_preview_page()
        DASHBOARD_PAGE.click_home_tab()

    if DASHBOARD_PAGE.get_possible_collision_task_count() != "0":
        while DASHBOARD_PAGE.get_possible_collision_task_count() != "0":
            DASHBOARD_PAGE.click_possible_collisions_link()
            COLLISIONS_PAGE.click_preview_button()
            COLLISIONS_PAGE.click_no_not_a_collision_button()
            COLLISIONS_PAGE.click_confirm_button()
            DASHBOARD_PAGE.click_home_tab()

    if DASHBOARD_PAGE.get_collision_task_count() != "0":
        DASHBOARD_PAGE.click_collisions_link()
        collision_count = int(COLLISIONS_PAGE.get_task_count())
        j = 0
        while j < collision_count:
            COLLISIONS_PAGE.click_preview_button()
            COLLISIONS_PAGE.click_resolved_button()
            COLLISIONS_PAGE.click_confirm_button()
            sleep(10)
            j += 1
        DASHBOARD_PAGE.click_home_tab()

    global tadm
    tadm = AutomationDataManager()
    tadm.create_test_credentials(TASK_TEST_DATA)
    sleep(20)  # wait for the data that created by the API actually exists in the db

    DASHBOARD_PAGE.click_refresh_button()
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_collisions_tab()


@when(
    'the user previews a possible collision event and the user chooses "No,It is not a collision" for the event and the user clicks "Yes,Confirm" in pop-up')
def chose_no_for_possible_collision():
    COLLISIONS_PAGE.click_preview_button()
    COLLISIONS_PAGE.click_no_not_a_collision_button()
    COLLISIONS_PAGE.click_confirm_button()
    sleep(5)


@then('the possible collision event is changed to new status')
def verify_status_of_possible_collision():
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_events()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(tadm.POSSIBLE_COLLISION_EVENT_ID_1ST)
    LIBRARY_PAGE.select_search_event_id_event_list()
    assert LIBRARY_PAGE.get_first_event_status() == "New"


@given('"Safety Manager" user go to Collisions page')
def navigate_to_collisions_page():
    LIBRARY_PAGE.click_reset_button()
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_collisions_tab()


@when(
    'the user previews a possible collision event and the user chooses "Yes,It is a collision" for the event and the user clicks "Yes,Confirm" in pop-up')
def chose_yes_for_possible_collision():
    COLLISIONS_PAGE.click_preview_button()
    COLLISIONS_PAGE.click_yes_for_possible_collision_button()
    COLLISIONS_PAGE.click_confirm_button()
    COLLISIONS_PAGE.click_close_icon()


@then('the event is changed to Collision event')
def verify_behavior_of_possible_collision():
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_events()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(tadm.POSSIBLE_COLLISION_EVENT_ID_2ND)
    LIBRARY_PAGE.select_search_event_id_event_list()
    assert_that(LIBRARY_PAGE.get_first_event_behavior(), contains_string("Collision"))
    # assert LIBRARY_PAGE.get_first_event_behavior() == "Collision"


# LQ-318
@when('the user clicks "TASKS" and the user clicks "COLLISIONS"')
def navigate_to_collisions_page():
    LIBRARY_PAGE.click_reset_button()
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_collisions_tab()


@then(
    'the task count is displayed and there are "DRIVER NAME", "GROUP", "VEHICLE", "EVENT DATE", "TIME" for each card and there is "Preview" button')
def verify_collision_task_page():
    assert COLLISIONS_PAGE.get_task_count() == "3"
    assert COLLISIONS_PAGE.driver_name_on_task_card_is_displayed() is True
    assert COLLISIONS_PAGE.get_group_text() == "GROUP"
    assert COLLISIONS_PAGE.get_vehicle_text() == "VEHICLE"
    assert COLLISIONS_PAGE.get_event_date_text() == "EVENT DATE"
    assert COLLISIONS_PAGE.get_time_text() == "TIME"
    assert COLLISIONS_PAGE.get_preview_button_text() == "Preview"


# LQ-319
@when('the user sets group filter to one group in collisions page')
def set_group_filter_collisions():
    COLLISIONS_PAGE.click_group_by_filter_collisions()
    COLLISIONS_PAGE.search_group_by_filter(TD.group)
    COLLISIONS_PAGE.select_group_by_filter()
    COLLISIONS_PAGE.click_done_filter_by_group()


@then('the tasks belong to the group are listed in collisions page')
def verify_collisions_filter_group():
    assert_that(COLLISIONS_PAGE.get_group_name(), contains_string(TD.group))



# LQ-320
@when('the user inputs some characters in search box in collisions page')
def search_driver_collisions():
    COLLISIONS_PAGE.click_reset_button()
    COLLISIONS_PAGE.search_driver_name(TD.driver_user)


@then('the tasks which driver name contains the inputted characters are shown in collisions page')
def verify_collisions_search():
    assert COLLISIONS_PAGE.get_task_count() == "2"


# LQ-323
@when('the user previews a collision event and the user clicks "Resolve" and the user clicks "Yes,Confirm" in pop-up')
def resolve_collision_task():
    COLLISIONS_PAGE.click_reset_button()
    sleep(2)  # sleep 2s to wait for the reset action to complete
    COLLISIONS_PAGE.click_preview_button()
    COLLISIONS_PAGE.click_resolved_button()
    COLLISIONS_PAGE.click_confirm_button()


@then('the collision event status is resolved')
def verify_resolve_collision_task():
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_events()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(tadm.COLLISION_EVENT_ID_1ST)
    LIBRARY_PAGE.select_search_event_id_event_list()
    assert LIBRARY_PAGE.get_first_event_status() == "Resolved"


@when(
    'the user previews a collision event and the user clicks "Coach Later" and the user clicks "Yes,Confirm" in pop-up')
def coach_later_collision_task():
    LIBRARY_PAGE.click_reset_button()
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_collisions_tab()
    COLLISIONS_PAGE.click_preview_button()
    COLLISIONS_PAGE.click_coach_later_button()
    COLLISIONS_PAGE.click_confirm_button()


@then('the event status is Face-To-Face')
def verify_coach_later_collision_task():
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_events()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(tadm.COLLISION_EVENT_ID_2ND)
    LIBRARY_PAGE.select_search_event_id_event_list()
    assert LIBRARY_PAGE.get_first_event_status() == "Face-To-Face"


@given('"Safety Manager" user is in Collisions page and search a collision event with driver assigned')
def navigate_to_collisions_page():
    LIBRARY_PAGE.click_reset_button()
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_collisions_tab()
    COLLISIONS_PAGE.search_driver_name(TD.driver_user)


@when('the user previews a collision event and the user clicks "Coach Now" and the user clicks "Yes,Confirm" in pop-up')
def coach_now_collision_event():
    COLLISIONS_PAGE.click_preview_button()
    COLLISIONS_PAGE.click_coach_now_button()
    COLLISIONS_PAGE.click_confirm_button()


@then('driver coaching session page is opened and the collision event status is Face-To-Face')
def verify_coach_now_collision_event():
    assert COACHING_PAGE.get_driver_coaching_session_label() == "DRIVER COACHING SESSION"
    assert COACHING_PAGE.get_event_status() == "Face-To-Face"
    assert COACHING_PAGE.get_event_id() == tadm.POSSIBLE_COLLISION_EVENT_ID_2ND

    # clear coach now for collision event data:
    COACHING_PAGE.click_video()
    COACHING_PAGE.click_complete_session()
    COACHING_PAGE.click_save_complete_session()
    COACHING_PAGE.click_close_complete_session()

    # clear coach later for Collision events data or other coaching data:
    while int(COACHING_PAGE.get_task_count()) > 0:
        DASHBOARD_PAGE.click_coaching_events()
        if COACHING_PAGE.continue_button_is_displayed() is True:
            COACHING_PAGE.click_continue_button()
        if COACHING_PAGE.video_error_msg() is False:
            COACHING_PAGE.click_video()
            COACHING_PAGE.click_complete_session()
            COACHING_PAGE.click_save_complete_session()
            COACHING_PAGE.click_close_complete_session()
        elif COACHING_PAGE.change_video_displayed() is True:
            COACHING_PAGE.change_event_video()
            sleep(5)
            COACHING_PAGE.click_video()
            COACHING_PAGE.click_complete_session()
            COACHING_PAGE.click_save_complete_session()
            COACHING_PAGE.click_close_complete_session()
        else:
            break


# LQ-326
@given('Safety Manager user is in FYI Notify page')
def navigate_to_fyi_notify_page():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_fyi_notify_tab()


@when('the user sets group filter to one group in FYI Notify page')
def set_group_filter_fyi_notify():
    FYI_NOTIFY_PAGE.click_group_by_filter_fyi_notify()
    FYI_NOTIFY_PAGE.search_group_by_filter(TD.group)
    FYI_NOTIFY_PAGE.select_group_by_filter()
    FYI_NOTIFY_PAGE.click_done_filter_by_group()


@then('the FYI Notify tasks belong to the group are listed in FYI Notify page')
def verify_fyi_notify_filter_group():
    assert_that(FYI_NOTIFY_PAGE.get_group_name_card(), contains_string(TD.group))


# LQ-327
@when('the user inputs some characters in search box in FYI Notify page')
def search_driver_fyi_notify():
    FYI_NOTIFY_PAGE.click_reset_button()
    FYI_NOTIFY_PAGE.search_driver_name(TD.driver_user)


@then('the tasks which driver name contains the inputted characters are shown in FYI Notify page')
def verify_fyi_notify_search():
    assert FYI_NOTIFY_PAGE.get_fyi_task_count() == "1"  # the task will be bundled for the same driver


# LQ-325
@given('coach user in dashboard page')
def go_to_dashboard_page():
    FYI_NOTIFY_PAGE.click_reset_button()
    DASHBOARD_PAGE.click_home_tab()


@when('the user clicks "TASKS" & the user clicks "FYI NOTIFY"')
def go_to_fyi_task():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_fyi_notify_tab()
    FYI_NOTIFY_PAGE.click_reset_button()


@then(
    'there are "GROUP", "VEHICLE", "EVENT DATE", "TIME" for each card & there is "Preview" button')  # need to add behavior label once api creates event with behavior
def view_fyi_task():
    assert FYI_NOTIFY_PAGE.get_group_text() == 'GROUP'
    assert FYI_NOTIFY_PAGE.get_vehicle_text() == 'VEHICLE'
    assert FYI_NOTIFY_PAGE.get_event_date_text() == 'EVENT DATE'
    assert FYI_NOTIFY_PAGE.get_time_text() == 'TIME'
    assert FYI_NOTIFY_PAGE.get_preview_button_text() == 'Preview'


# LQ-330
@when('the user previews a FYI Notify event & the user clicks "Resolve" & the user clicks "Yes,Confirm" in pop-up')
def resolved_fyi_task():
    FYI_NOTIFY_PAGE.click_preview_button()
    FYI_NOTIFY_PAGE.click_resolve_button()
    FYI_NOTIFY_PAGE.click_confirm_button()


@then('the event status is resolved')
def verify_resolved_status():
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_events()
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(tadm.FYI_EVENT_ID_1ST)
    LIBRARY_PAGE.select_search_event_id_event_list()
    assert LIBRARY_PAGE.get_first_event_status() == "Resolved"


@when('the user previews a FYI Notify event & the user clicks "Coach Later" & the user clicks "Yes,Confirm" in pop-up')
def coach_later_fyi_event():
    LIBRARY_PAGE.click_reset_button()
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_fyi_notify_tab()
    FYI_NOTIFY_PAGE.click_preview_button()
    FYI_NOTIFY_PAGE.click_coach_later_button()
    FYI_NOTIFY_PAGE.click_confirm_button()
    FYI_NOTIFY_PAGE.close_preview_page()


@then('the FYI event status is Face-To-Face')
def verify_coach_later_fyi_event():
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_events()
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(tadm.FYI_EVENT_ID_2ND)
    LIBRARY_PAGE.select_search_event_id_event_list()
    assert LIBRARY_PAGE.get_first_event_status() == "Face-To-Face"


@given('the FYI event with driver assigned')
def assign_driver_to_fyi_event():
    LIBRARY_PAGE.click_reset_button()
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_fyi_notify_tab()
    FYI_NOTIFY_PAGE.search_driver_name(TD.driver_user)


@when('the user previews a FYI Notify even & the user clicks "Coach Now" & the user clicks "Yes,Confirm" in pop-up')
def coach_now_fyi_event():
    FYI_NOTIFY_PAGE.click_preview_button()
    FYI_NOTIFY_PAGE.click_coach_now_button()
    FYI_NOTIFY_PAGE.click_confirm_button()


@then('driver coaching session page is opened and the event status is Face-To-Face')
def verify_coach_now_fyi_event():
    assert COACHING_PAGE.get_driver_coaching_session_label() == "DRIVER COACHING SESSION"
    assert COACHING_PAGE.get_event_status() == "Face-To-Face"
    assert COACHING_PAGE.get_event_id() == tadm.FYI_EVENT_ID_3RD


# LQ-276
@given('"Safety Manager" user is in Due For Coaching page')
def go_to_due_for_coaching():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_coaching()


@when(
    'the user navigate to Driver coaching session page and the user views one event and complete the coaching session')
def bulk_coach():
    COACHING_PAGE.search_name_filter(TD.driver_user)
    DASHBOARD_PAGE.click_coaching_events()
    if COACHING_PAGE.continue_button_is_displayed() is True:
        COACHING_PAGE.click_continue_button()
    if COACHING_PAGE.video_error_msg() is False:
        COACHING_PAGE.click_video()
        COACHING_PAGE.click_complete_session()
        COACHING_PAGE.click_save_complete_session()
        COACHING_PAGE.click_close_complete_session()
    else:
        COACHING_PAGE.change_event_video()
        sleep(5)
        COACHING_PAGE.click_video()
        COACHING_PAGE.click_complete_session()
        COACHING_PAGE.click_save_complete_session()
        COACHING_PAGE.click_close_complete_session()


@then('the both Events are coached')
def assert_bulk_coach():
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_events()
    LIBRARY_PAGE.click_reset_button()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(tadm.FYI_EVENT_ID_2ND)
    LIBRARY_PAGE.select_search_event_id_event_list()
    assert LIBRARY_PAGE.get_first_event_status() == "Resolved"
    LIBRARY_PAGE.click_reset_button()

    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_event_id()
    LIBRARY_PAGE.type_event_id_event_list(tadm.FYI_EVENT_ID_3RD)
    LIBRARY_PAGE.select_search_event_id_event_list()
    assert LIBRARY_PAGE.get_first_event_status() == "Resolved"

    LIBRARY_PAGE.click_reset_button()
