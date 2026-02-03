from time import sleep

from hamcrest import assert_that
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then

from data.int.permission_data_int import PermissionDataInt as PDI_INT
from data.prod.permission_data_prod import PermissionDataProd as PDI_PROD
from data.stg.permission_data_stg import PermissionDataStg as PDI_STG
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from steps.common import DC_URL, ENV, WELCOME_URL, SSO_URL, SSO_URL1, SSO_URL2, FLEET_URL

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
COACHING_PAGE = 0
BASE_PAGE = 0
FLEET_MAINT_PAGE = 0
PDI = 0

scenarios('../features/permission.feature')


# LQ-306
@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, PDI

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)

    browser.get(WELCOME_URL)

    if ENV == 'int':
        PDI = PDI_INT
    elif ENV == 'stg':
        PDI = PDI_STG
    elif ENV == 'prod':
        PDI = PDI_PROD
    else:
        raise ValueError(f"Unsupported ENV value: {ENV!r}. Must be one of 'int', 'stg', or 'prod'.")

@when(
    'the user with multi company account enters username/password, clicks the login button in the page and select company from the list')
def login():
    LOGIN_PAGE.enter_username(PDI.admin_user_name)
    LOGIN_PAGE.enter_password(PDI.admin_password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    sleep(2)
    LOGIN_PAGE.select_multi_company(PDI.oldui_company)
    LOGIN_PAGE.click_select_company_button()


@then('the user is successfully logged into the Driver Safety dashboard')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_dvir_title(), IsEqualIgnoringCase("Dvir"))
    assert_that(DASHBOARD_PAGE.get_fleet_tracking_title(), IsEqualIgnoringCase("Fleet Tracking"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert_that(DASHBOARD_PAGE.get_video_search_title(), IsEqualIgnoringCase("Video Search"))
    assert_that(DASHBOARD_PAGE.get_hos_title(), IsEqualIgnoringCase("Hos"))
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_admin_sign_out()


# @LQ-49067
@when(
    'the full access user lands on dashboard page')
def login():
    LOGIN_PAGE.enter_username(PDI.full_access_user_name)
    LOGIN_PAGE.enter_password(PDI.full_access_password)
    LOGIN_PAGE.click_login()


@then('the full access user should see Driver Safety & Fleet Tracking & Video Search & Admin & HOS tabs')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_dvir_title(), IsEqualIgnoringCase("Dvir"))
    assert_that(DASHBOARD_PAGE.get_fleet_tracking_title(), IsEqualIgnoringCase("Fleet Tracking"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert_that(DASHBOARD_PAGE.get_video_search_title(), IsEqualIgnoringCase("Video Search"))
    assert_that(DASHBOARD_PAGE.get_hos_title(), IsEqualIgnoringCase("Hos"))
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_admin_sign_out()


# @LQ-49069
@when(
    'the safety manager user lands on the dashboard page')
def login():
    LOGIN_PAGE.enter_username(PDI.safety_manager_user_name)
    LOGIN_PAGE.enter_password(PDI.admin_password)
    LOGIN_PAGE.click_login()


@then('the safety manager user should see only Driver Safety & Admin tabs')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_admin_sign_out()


# @LQ-49101
@when(
    'the coach user lands on the dashboard page')
def login():
    LOGIN_PAGE.enter_username(PDI.coach_user_name)
    LOGIN_PAGE.enter_password(PDI.admin_password)
    LOGIN_PAGE.click_login()


@then('the coach user should see only Driver Safety & Admin tabs')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_admin_sign_out()


# @LQ-49102
@when(
    'the program manager user lands on the dashboard page')
def login():
    LOGIN_PAGE.enter_username(PDI.program_manager_user_name)
    LOGIN_PAGE.enter_password(PDI.admin_password)
    LOGIN_PAGE.click_login()


@then('the program manager user should see only Driver Safety & Admin tabs')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_admin_sign_out()


# @LQ-49366
@when(
    'the program manager assistant user lands on the dashboard page')
def login():
    LOGIN_PAGE.enter_username(PDI.program_manager_assist_user_name)
    LOGIN_PAGE.enter_password(PDI.admin_password)
    LOGIN_PAGE.click_login()


@then('the program manager assistant user should see only Driver Safety & Admin tabs')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_admin_sign_out()


# @LQ-49367
@when(
    'the event dispatcher user lands on the dashboard page')
def login():
    LOGIN_PAGE.enter_username(PDI.event_dispatcher_user_name)
    LOGIN_PAGE.enter_password(PDI.admin_password)
    LOGIN_PAGE.click_login()


@then('the event dispatcher user should see only Driver Safety & Admin tabs')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_admin_sign_out()


# @LQ-49368
@when(
    'the safety read only user lands on the dashboard page')
def login():
    LOGIN_PAGE.enter_username(PDI.safety_read_user_name)
    LOGIN_PAGE.enter_password(PDI.admin_password)
    LOGIN_PAGE.click_login()


@then('the safety read only user should see only Driver Safety & Admin tabs')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_admin_sign_out()


# LQ-49369
@when(
    'the driver user lands on the dashboard page')
def login():
    LOGIN_PAGE.enter_username(PDI.driver_user_name)
    LOGIN_PAGE.enter_password(PDI.admin_password)
    LOGIN_PAGE.click_login()


@then('the  driver user should see only Driver Safety & DVIR tabs')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_dvir_title(), IsEqualIgnoringCase("Dvir"))
    assert_that(DASHBOARD_PAGE.get_hos_title(), IsEqualIgnoringCase("Hos"))
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_driver_sign_out()


# @LQ-49370
@when(
    'the fleet dispatcher user lands on the Fleet Tracking page')
def login():
    LOGIN_PAGE.enter_username(PDI.fleet_dispatcher_user_name)
    LOGIN_PAGE.enter_password(PDI.admin_password)
    LOGIN_PAGE.click_login()


@then('the fleet dispatcher user should see only Fleet Tracking & Admin tabs')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_fleet_tracking_title(), IsEqualIgnoringCase("Fleet Tracking"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.driver_safety_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_fleet_sign_out()


# @LQ-49371
@when(
    'the fleet read only user lands on the Fleet Tracking page')
def login():
    LOGIN_PAGE.enter_username(PDI.fleet_read_user_name)
    LOGIN_PAGE.enter_password(PDI.admin_password)
    LOGIN_PAGE.click_login()


@then('the fleet read only user should see only Fleet Tracking & Admin tabs')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_fleet_tracking_title(), IsEqualIgnoringCase("Fleet Tracking"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.driver_safety_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_fleet_sign_out()


# @LQ-49372
@when(
    'the video reviewer user lands on the dashboard page')
def login():
    LOGIN_PAGE.enter_username(PDI.video_reviewer_user_name)
    LOGIN_PAGE.enter_password(PDI.admin_password)
    LOGIN_PAGE.click_login()


@then('the video reviewer user should see only Video Service tab')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_video_search_title(), IsEqualIgnoringCase("Video Search"))
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.driver_safety_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    assert DASHBOARD_PAGE.admin_title_is_displayed() is False
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_admin_sign_out()


# @LQ-49373
@when(
    'the video reviewer plus user lands on the dashboard page')
def login():
    LOGIN_PAGE.enter_username(PDI.video_reviewer_plus_user_name)
    LOGIN_PAGE.enter_password(PDI.admin_password)
    LOGIN_PAGE.click_login()


@then('the video reviewer user should see only Video Service tab')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_video_search_title(), IsEqualIgnoringCase("Video Search"))
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.driver_safety_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    assert DASHBOARD_PAGE.admin_title_is_displayed() is False
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_admin_sign_out()


# LQ-50532
@given('the login page for DC is displayed in the browser')
def launch_browser(browser):
    browser.get(DC_URL)


@when(
    'the full access user lands on dashboard DC page')
def login():
    LOGIN_PAGE.enter_username(PDI.full_access_user_name)
    LOGIN_PAGE.enter_password(PDI.full_access_password)
    LOGIN_PAGE.click_login()


@then('the user is successfully logged into the Driver Safety DC dashboard')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_dvir_title(), IsEqualIgnoringCase("Dvir"))
    assert_that(DASHBOARD_PAGE.get_fleet_tracking_title(), IsEqualIgnoringCase("Fleet Tracking"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert_that(DASHBOARD_PAGE.get_video_search_title(), IsEqualIgnoringCase("Video Search"))
    assert_that(DASHBOARD_PAGE.get_hos_title(), IsEqualIgnoringCase("Hos"))
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_admin_sign_out()


# LQ-50533
@given('the login fleet page is displayed in the browser')
def launch_browser(browser):
    browser.get(FLEET_URL)


@when(
    'the fleet dispatcher user login to fleet login page')
def login():
    LOGIN_PAGE.enter_username(PDI.fleet_dispatcher_user_name)
    LOGIN_PAGE.enter_password(PDI.admin_password)
    LOGIN_PAGE.click_login()


@then('the fleet dispatcher user successfully lands on Fleet Tracking dashboard')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_fleet_tracking_title(), IsEqualIgnoringCase("Fleet Tracking"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.driver_safety_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_fleet_sign_out()


@when(
    'the fleet read only user login to fleet login page')
def login():
    LOGIN_PAGE.enter_username(PDI.fleet_read_user_name)
    LOGIN_PAGE.enter_password(PDI.admin_password)
    LOGIN_PAGE.click_login()


@then('the fleet read only user successfully lands on Fleet Tracking dashboard')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_fleet_tracking_title(), IsEqualIgnoringCase("Fleet Tracking"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.driver_safety_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_fleet_sign_out()


# @LQ-50534
@given('the login SSO page is displayed in the browser')
def launch_browser(browser):
    browser.get(SSO_URL)


@when(
    'the coach user login to sso login page')
def login():
    LOGIN_PAGE.enter_sso_username(PDI.coach_user_name)
    LOGIN_PAGE.enter_sso_relay_state(PDI.password)
    LOGIN_PAGE.click_sso_single_signon()


@then('the coach user successfully lands on Driver Safety dashboard from SSO')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_dc_admin_sign_out()


# LQ-50535
@given('the login SSO page is displayed in the browser for driver user')
def launch_browser(browser):
    browser.get(SSO_URL)


@when(
    'the driver user login to sso login page')
def login():
    LOGIN_PAGE.enter_sso_username(PDI.driver_user_name)
    LOGIN_PAGE.enter_sso_relay_state(PDI.password)
    LOGIN_PAGE.click_sso_single_signon()


@then('the driver user successfully lands on Driver Safety dashboard from SSO')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_dvir_title(), IsEqualIgnoringCase("Dvir"))
    assert_that(DASHBOARD_PAGE.get_hos_title(), IsEqualIgnoringCase("Hos"))
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    assert DASHBOARD_PAGE.admin_title_is_displayed() is False


# @TBD
@given('the Drivecam Online SSO login page is accessed using all uppercase SSO')
def launch_browser_for_uppercase_sso(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE
    LOGIN_PAGE = LoginPage(browser)

    browser.get(SSO_URL1)

# @TBD
@given('the Drivecam Online SSO login page is accessed using all lowercase sso')
def for_uppercase_for_lowercase_sso(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE
    LOGIN_PAGE = LoginPage(browser)

    browser.get(SSO_URL2)


@then('the user is redirected to the cloud SSO login page')
def verify_error_message():
    assert_that(LOGIN_PAGE.get_sso_login_unsuccessful_text(), IsEqualIgnoringCase("Login was unsuccessful."))
