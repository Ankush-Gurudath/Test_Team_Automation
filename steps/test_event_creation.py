from hamcrest import assert_that, contains_string
from pytest_bdd import scenarios, given, when, then

from data.int.home_data_int import HomeDataInt as LD_INT
from data.prod.home_data_prod import HomeDataProd as LD_PROD
from data.stg.home_data_stg import HomeDataStg as LD_STG
from pages.assign_driver_page import AssignDriverPage
from pages.coaching_page import CoachingPage
from pages.collisions_page import CollisionsPage
from pages.dashboard_page import DashboardPage
from pages.library_page import LibraryPage
from pages.login_page import LoginPage
from steps.common import ENV, WELCOME_URL

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
ASSIGN_DRIVER_PAGE = 0
LIBRARY_PAGE = 0
COACHES_REPORT_PAGE = 0
DRIVER_PROFILE_PAGE = 0
COACHING_PAGE = 0
COLLISIONS_PAGE = 0

EVENT_DRIVER = ''
EVENT_GROUP = ''
LAST_DATA_EXPORT_DATE = ''
LD = ''

scenarios('../features/event_creation.feature')


# LQ-263
@given('the coach user logs in')
def coach_log_in_and_event_assigned_driver(browser):
    global LOGIN_PAGE, LIBRARY_PAGE, DASHBOARD_PAGE, LD, ASSIGN_DRIVER_PAGE, COACHING_PAGE, COLLISIONS_PAGE

    LOGIN_PAGE = LoginPage(browser)
    COLLISIONS_PAGE = CollisionsPage(browser)
    COACHING_PAGE = CoachingPage(browser)
    LIBRARY_PAGE = LibraryPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    ASSIGN_DRIVER_PAGE = AssignDriverPage(browser)

    browser.get(WELCOME_URL)

    if ENV == 'int':
        LD = LD_INT
    elif ENV == 'stg':
        LD = LD_STG
    else:
        LD = LD_PROD

    LOGIN_PAGE.enter_username(LD.single_user_name)
    LOGIN_PAGE.enter_password(LD.password_single_user)
    LOGIN_PAGE.click_login()


@when('the user clicks "LIBRARY" and then clicks "EVENTS"')
def navigate_to_events_page():
    assert DASHBOARD_PAGE.get_driver_safety_title() == "DRIVER SAFETY"
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_events()
    LIBRARY_PAGE.click_search_dropdown()
    LIBRARY_PAGE.select_device()
    LIBRARY_PAGE.type_in_search_criteria_textbox_rh(LD.device_id)
    LIBRARY_PAGE.select_search_criteria_result_event_list()


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
    assert LIBRARY_PAGE.get_behaviors() == "BEHAVIORS"


# LQ-47009
@when('the user adds a behavior')
def reassign_driver():
    global EVENT_DRIVER
    EVENT_DRIVER = LIBRARY_PAGE.get_first_event_driver()

    if EVENT_DRIVER == "Driver Unassigned":
        LIBRARY_PAGE.click_event_id()
        LIBRARY_PAGE.click_more_actions()
        LIBRARY_PAGE.click_reassign_driver_event_no_driver()
        LIBRARY_PAGE.enter_driver_name(LD.driver)
    else:
        LIBRARY_PAGE.click_event_id()
        LIBRARY_PAGE.click_more_actions_ar()
        LIBRARY_PAGE.click_reassign_driver()
        LIBRARY_PAGE.enter_driver_name('driver unassigned')

    LIBRARY_PAGE.select_search_name_in_event_preview()
    LIBRARY_PAGE.click_assign_button_in_event_preview()
    LIBRARY_PAGE.click_edit_behavior()
    LIBRARY_PAGE.add_behavior_and_save()
    LIBRARY_PAGE.click_edit_behavior()
    LIBRARY_PAGE.add_behavior_and_save()


@then('the behavior is added')
def verify_behavior_added():
    assert_that(LIBRARY_PAGE.get_first_behavior_text(), contains_string('Cell Handheld'))
    assert_that(LIBRARY_PAGE.get_second_behavior_text(), contains_string('Camera Issue'))


# LQ-6820
@when('the user removes a behavior')
def verify_behavior_removed():
    LIBRARY_PAGE.remove_first_behavior()


@then('the behavior is removed')
def verify_behavior_removed():
    assert LIBRARY_PAGE.second_behavior_is_displayed() is False


# LQ-5544
@when('the user clicks "Coach Event" & the user clicks "Complete Session"')
def driver_self_coaching():
    COLLISIONS_PAGE.click_coach_now_button()
    COLLISIONS_PAGE.click_confirm_button()
    COACHING_PAGE.click_video()
    COACHING_PAGE.click_add_events()
    COACHING_PAGE.send_event_notes("Self coaching was successful")
    COACHING_PAGE.click_submit_button()
    COACHING_PAGE.click_action_plan()
    COACHING_PAGE.click_complete_session()
    COACHING_PAGE.click_save_complete_session()


@then('the event is coached')
def assert_driver_self_coaching():
    assert COACHING_PAGE.get_complete_session_message() == "Coaching session saved."
    COACHING_PAGE.click_close_complete_session()