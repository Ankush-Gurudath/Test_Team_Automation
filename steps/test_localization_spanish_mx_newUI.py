from time import sleep

from hamcrest import assert_that
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then

from data.int.localization_data_int import LocalizationDataInt as LDI_INT
from data.prod.localization_data_prod import LocalizationDataProd as LDI_PROD
from data.stg.localization_data_stg import LocalizationDataStg as LDI_STG
from locators.locators_dashboard_page import LocatorsDashboard as AC
from pages.assign_driver_page import AssignDriverPage
from pages.coaching_page import CoachingPage
from pages.dashboard_page import DashboardPage
from pages.driver_profile_page import DriverProfilePage
from pages.events_page import EventsPage
from pages.login_page import LoginPage
from steps.common import ENV, WELCOME_URL

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
COACHING_PAGE = 0
BASE_PAGE = 0
DRIVER_PROFILE_PAGE = 0
ASSIGN_DRIVER_PAGE = 0
FLEET_MAINT_PAGE = 0
EVENT_PAGE = 0
LDI = 0

scenarios('../features/localization.feature')


# LQ-306
@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, DRIVER_PROFILE_PAGE, ASSIGN_DRIVER_PAGE, COACHING_PAGE, EVENT_PAGE, LDI

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    COACHING_PAGE = CoachingPage(browser)
    ASSIGN_DRIVER_PAGE = AssignDriverPage(browser)
    DRIVER_PROFILE_PAGE = DriverProfilePage(browser)
    EVENT_PAGE = EventsPage(browser)

    browser.get(WELCOME_URL)

    if ENV == 'int':
        LDI = LDI_INT
    elif ENV == 'stg':
        LDI = LDI_STG
    else:
        LDI = LDI_PROD


@when(
    'the user with multi company account enters username/password, clicks the login button in the page and select company from the list')
def login():
    LOGIN_PAGE.enter_username(LDI.admin_user_name)
    LOGIN_PAGE.enter_password(LDI.admin_password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    sleep(2)
    LOGIN_PAGE.select_multi_company('DriveCam DC4DC Test Co')
    LOGIN_PAGE.click_select_company_button()


@then('the user is successfully logged into the Driver Safety dashboard')
def verify_login():
    DASHBOARD_PAGE.get_noof_drivers_text(AC.no_of_drivers_text_xpath)
    assert_that(DASHBOARD_PAGE.get_tasks_new_UI_title(), IsEqualIgnoringCase(LDI.tasks_es_mx_label))
    assert_that(DASHBOARD_PAGE.get_metrics_new_UI_title(), IsEqualIgnoringCase(LDI.metrics_es_mx_label))


# LQ-53288
@when('the user clicks "LIBRARY" and then clicks "EVENTS"')
def click_coach_event():
    DASHBOARD_PAGE.click_library_tab_new_ui()
    DASHBOARD_PAGE.click_events_new_ui()


@then('the Date displays with correct format for every language')
def verify_coaching_session_page():
    assert EVENT_PAGE.event_date_month_is_word_new_UI() is False
