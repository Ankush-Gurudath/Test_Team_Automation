from pytest_bdd import scenarios, given, when, then
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from steps.common import WELCOME_URL, ENV
from data.int.home_data_int import HomeDataInt as HD_INT
from data.prod.home_data_prod import HomeDataProd as HD_PROD
from data.stg.home_data_stg import HomeDataStg as HD_STG

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
IC_URL = WELCOME_URL + "?target=implementationcenter"

scenarios('../features/implementation_center_login.feature')

@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, HD

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)

    browser.get(IC_URL)

    if ENV == 'int':
        HD = HD_INT
    elif ENV == 'stg':
        HD = HD_STG
    else:
        HD = HD_PROD

@when('the user with Implementation center account enters username/password, clicks the login button in the page')
def login():
    LOGIN_PAGE.enter_username(HD.implementation_center_username)
    LOGIN_PAGE.enter_password(HD.implementation_center_user_password)
    LOGIN_PAGE.click_login()

@when('user select an account from the account selection dropdown')
def select_account():
    LOGIN_PAGE.select_account(HD.implementation_center_account_name)

@then('User is successfully logged into the Implementation center dashboard and validate page title')
def verify_login():
    assert DASHBOARD_PAGE.get_implementation_center_title() == 'Implementation Center'

@when('user logout from the application')
def logout():
    LOGIN_PAGE.click_profile_icon()
    LOGIN_PAGE.click_sign_out_btn()

@then('verify signin page visible')
def verify_signin_page():
    assert LOGIN_PAGE.get_login_page() == 'SIGN IN'
    assert DASHBOARD_PAGE.lytx_logo_is_displayed() is True