from hamcrest import assert_that
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then

from data.prod.home_data_prod import HomeDataProd as HD_PROD
from pages.dashboard_page import DashboardPage
from pages.fleet_telematics_left_panel_page import FleetTelematicsPageLeftPanel
from pages.hos_page import HosPage
from pages.login_page import LoginPage
from steps.common import DC_URL
from steps.test_sanity_fleet_telematics_left_panel import FLEET_TELEMATICS_PAGE
from pages.fleet_telematics_center_page import FleetTelematicsCenterPage

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
BASE_PAGE = 0
HOS_PAGE = 0
HD = 0
FLEET_TELEMATICS_PAGE = 0
FLEET_TELEMATICS_CENTER_PAGE = 0



scenarios('../features/sanity_prod_geotab.feature')


# LQ-306
@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, HD, HOS_PAGE, FLEET_TELEMATICS_PAGE, FLEET_TELEMATICS_CENTER_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    HOS_PAGE = HosPage(browser)
    FLEET_TELEMATICS_PAGE = FleetTelematicsPageLeftPanel(browser)
    FLEET_TELEMATICS_CENTER_PAGE = FleetTelematicsCenterPage(browser)

    browser.get(DC_URL)

    HD = HD_PROD


@when('the user enters username/password, clicks the login button in the page and select company from the list')
def login():
    LOGIN_PAGE.enter_username(HD.geotab_user_name)
    LOGIN_PAGE.enter_password(HD.geotab_password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_multi_company(HD.company_name_geotab)
    LOGIN_PAGE.click_select_company_button()


@then('the user is successfully logged into the Driver Safety dashboard')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))


@when('the user clicks HOS tab')
def go_to_Hos_page():
    DASHBOARD_PAGE.click_hos_tab()


@then('the HOS main page is loaded successfully')
def verify_user_on_hos_page():
    HOS_PAGE.switch_hos_iframe()
    HOS_PAGE.accept_geotab_end_user_agreement()
    assert FLEET_TELEMATICS_PAGE.more_charts_button_is_displayed() is True



@when("the user clicks Compliance and navigates to logs")
def navigate_to_logs():
    HOS_PAGE.click_compliance_menu()
    HOS_PAGE.click_hos()
    HOS_PAGE.click_hos_logs()


@then("the HOS Logs page is loaded successfully")
def verify_hos_logs_loads():
    assert_that(HOS_PAGE.get_hos_logs_title(), IsEqualIgnoringCase("HOS Logs"))


@when("the user clicks Compliance and navigates to Violations")
def navigate_to_violations():
    HOS_PAGE.click_compliance_menu()
    HOS_PAGE.click_hos()
    HOS_PAGE.click_violations()
    HOS_PAGE.search_all_drivers()


@then("the HOS Violations page is loaded successfully")
def verify_violations_page_loads():
    assert_that(HOS_PAGE.get_hos_violations_title(), IsEqualIgnoringCase("HOS Violations"))


@when("the user clicks the Assets menu item")
def navigate_to_assets():
    HOS_PAGE.click_assets_menu()


@then("the Assets page is loaded successfully")
def assets_page_loads():
    assert FLEET_TELEMATICS_CENTER_PAGE.asset_header_is_displayed()
    assert FLEET_TELEMATICS_CENTER_PAGE.search_bar_displayed()
