from hamcrest import assert_that, contains_string
from pytest_bdd import scenarios, given, when, then

from pages.fleet_map_page import FleetMapPage
from pages.login_page import LoginPage
from steps.common import FLEET_URL
from data.prod.home_data_prod import HomeDataProd as HD_PROD


LOGIN_PAGE = 0
FLEET_MAP_PAGE = 0
HD = 0

scenarios('../features/sanity_fleet_customers.feature')


# LQ-15218
@given('the login page is displayed')
def launch_browser(browser):
    global LOGIN_PAGE, FLEET_MAP_PAGE, HD

    LOGIN_PAGE = LoginPage(browser)
    FLEET_MAP_PAGE = FleetMapPage(browser)

    browser.get(FLEET_URL)
    HD = HD_PROD

@when('the user enters a JBHunt username/password and clicks the login button')
def login():
    LOGIN_PAGE.enter_username(HD.jbhunt_single_company_username)
    LOGIN_PAGE.enter_password(HD.jbhunt_single_company_password)
    LOGIN_PAGE.click_login()

@when('the user enters a Foodliner username/password and clicks the login button')
def login():
    LOGIN_PAGE.enter_username(HD.foodliner_username)
    LOGIN_PAGE.enter_password(HD.customer_at_risk_password)
    LOGIN_PAGE.click_login()

@when('the user enters a UPS username/password and clicks the login button')
def login():
    LOGIN_PAGE.enter_username(HD.ups_username)
    LOGIN_PAGE.enter_password(HD.customer_at_risk_password)
    LOGIN_PAGE.click_login()


@when('the user enters a Ryder username/password and clicks the login button')
def login():
    LOGIN_PAGE.enter_username(HD.ryder_username)
    LOGIN_PAGE.enter_password(HD.customer_at_risk_password)
    LOGIN_PAGE.click_login()


@then('the Fleet application is displayed')
def assert_fleet_app():
    FLEET_MAP_PAGE.click_map()
    assert_that(FLEET_MAP_PAGE.get_fleet_tracking_title(), contains_string("FLEET TRACKING"))
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_fleet_sign_out_btn()