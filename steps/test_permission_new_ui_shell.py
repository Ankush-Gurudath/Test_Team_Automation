from hamcrest import assert_that
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then
from data.int.permission_data_int import PermissionDataInt as PDI_INT
from data.prod.permission_data_prod import PermissionDataProd as PDI_PROD
from data.stg.permission_data_stg import PermissionDataStg as PDI_STG
from pages.dashboard_page import DashboardPage
from pages.driver_profile_page import DriverProfilePage
from pages.video_search_page import VideoSearchPage
from pages.fleet_telematics_left_panel_page import FleetTelematicsPageLeftPanel
from pages.login_page import LoginPage
from steps.common import NEW_UI_FTM_URL, ENV, WELCOME_URL, SSO_URL, SSO_URL1, SSO_URL2, FLEET_URL

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
VIDEO_SEARCH_PAGE = 0
DRIVER_PROFILE_PAGE = 0
BASE_PAGE = 0
PDI = 0
FLEET_TELEMATICS_PAGE = 0

scenarios('../features/permission_new_ui_shell.feature')


# LQ-147460
@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, PDI, VIDEO_SEARCH_PAGE, DRIVER_PROFILE_PAGE, FLEET_TELEMATICS_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    VIDEO_SEARCH_PAGE = VideoSearchPage(browser)
    DRIVER_PROFILE_PAGE = DriverProfilePage(browser)
    FLEET_TELEMATICS_PAGE = FleetTelematicsPageLeftPanel(browser)
    browser.get(NEW_UI_FTM_URL)
    if ENV == 'int':
        PDI = PDI_INT
    elif ENV == 'stg':
        PDI = PDI_STG
    elif ENV == 'prod':
        PDI = PDI_PROD


@when(
    'the multi company access user enters username/password, clicks the login button in the page and select company from the list')
def login():
    LOGIN_PAGE.enter_username(PDI.fleet_telematics_multi_company)
    LOGIN_PAGE.enter_password(PDI.fleet_telematics_multi_company_password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_multi_company(PDI.newui_company)
    LOGIN_PAGE.click_select_company_button()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


# @LQ-136509
@when('the full access role user enters username/password and clicks the login button')
def full_access_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.fleet_telematics_fullaccess)
    LOGIN_PAGE.enter_password(PDI.fleet_telematics_fullaccess_password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


@then(
    'the user should successfully login to newui and land on the Driver Safety Home page, and all tabs such as Video Search, Driver Safety, Admin, Fleet Tracking, Fleet Telematics, DVIR should be displayed')
def verify_user_on_driver_safety_with_new_ui_shell_with_dashboard():
    assert LOGIN_PAGE.lytx_logo_new_ui_is_displayed() is True
    assert DASHBOARD_PAGE.get_groups_by_highest_score_title() == "Groups by Highest Score"
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_fleet_telematics_title(), IsEqualIgnoringCase("Fleet Telematics"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert_that(VIDEO_SEARCH_PAGE.get_video_search_title(), IsEqualIgnoringCase("VIDEO SEARCH"))
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is True
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is True
    assert DASHBOARD_PAGE.hos_title_is_displayed() is True
    LOGIN_PAGE.click_profile_btn()
    LOGIN_PAGE.click_sign_out_button_newui()


# LQ-136510
@when('the driver role user enters username/password and clicks the login button')
def driver_user_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.fleet_telematics_driver)
    LOGIN_PAGE.enter_password(PDI.fleet_telematics_driver_password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


@then(
    'the user should successfully login to newui and land on the Driver Safety Home page, tabs such as Driver Safety, Fleet Telematics, DVIR should be displayed and tabs such as Admin, Fleet Tracking, Video Search should not be displayed')
def verify_user_on_driver_safety_with_new_ui_shell():
    assert LOGIN_PAGE.lytx_logo_new_ui_is_displayed() is True
    assert DRIVER_PROFILE_PAGE.get_driver_profile_text_on_login() == "DRIVER PROFILE"
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_fleet_telematics_title(), IsEqualIgnoringCase("Fleet Telematics"))
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is True
    assert DASHBOARD_PAGE.hos_title_is_displayed() is True
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    assert DASHBOARD_PAGE.admin_title_is_displayed() is False
    LOGIN_PAGE.click_profile_btn()
    LOGIN_PAGE.click_sign_out_button_newui()


# LQ-136511
@when('the coach role user enters username/password and clicks the login button')
def coach_user_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.newui_coach_username)
    LOGIN_PAGE.enter_password(PDI.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


# LQ-136490
@when('the safety manager role user enters username/password and clicks the login button')
def safety_manager_user_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.newui_safety_manager_username)
    LOGIN_PAGE.enter_password(PDI.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


# LQ-136493
@when('the safety manager plus role user enters username/password and clicks the login button')
def safety_manager_plus_user_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.newui_safety_manager_plus_username)
    LOGIN_PAGE.enter_password(PDI.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


# LQ-136508
@when('the safety read only role user enters username/password and clicks the login button')
def safety_ro_user_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.newui_safety_read_only_username)
    LOGIN_PAGE.enter_password(PDI.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


# LQ-136489
@when('the program manager role user enters username/password and clicks the login button')
def program_manager_user_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.newui_program_manager_username)
    LOGIN_PAGE.enter_password(PDI.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


# LQ-136507
@when('the program manager assistance role user enters username/password and clicks the login button')
def program_manager_assistance_user_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.newui_program_manager_assistance_username)
    LOGIN_PAGE.enter_password(PDI.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


# LQ-136502
@when('the event dispatcher role user enters username/password and clicks the login button')
def event_dispatcher_user_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.newui_event_dispatcher_username)
    LOGIN_PAGE.enter_password(PDI.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


@then(
    'the user should successfully login to newui and land on the Driver Safety Home page, tabs such as Driver Safety and Admin should be displayed but not fleet telematics')
def verify_user_on_driver_safety_with_new_ui_shell():
    assert LOGIN_PAGE.lytx_logo_new_ui_is_displayed() is True
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert DASHBOARD_PAGE.fleet_telematics_title_is_displayed() is False
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    LOGIN_PAGE.click_profile_btn()
    LOGIN_PAGE.click_sign_out_button_newui()


# LQ-136491
@when('the fleet dispatcher role user enters username/password and clicks the login button')
def fleet_dispatcher_user_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.newui_fleet_dispatcher_username)
    LOGIN_PAGE.enter_password(PDI.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


# LQ-136492
@when('the fleet read only role user enters username/password and clicks the login button')
def fleetro_user_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.newui_fleet_read_only_username)
    LOGIN_PAGE.enter_password(PDI.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


@then(
    'the user should successfully login to newui and land on the Fleet Tracking Home page, tabs such as Fleet Tracking and Admin should be displayed but not fleet telematics')
def verify_user_on_fleet_tracking_with_new_ui_shell():
    assert_that(DASHBOARD_PAGE.get_fleet_tracking_title(), IsEqualIgnoringCase("Fleet Tracking"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert DASHBOARD_PAGE.fleet_telematics_title_is_displayed() is False
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.driver_safety_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    LOGIN_PAGE.click_profile_btn()
    LOGIN_PAGE.click_sign_out_button_newui()


# LQ-136694
@when('the video reviewer role user enters username/password and clicks the login button')
def video_reviewer_user_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.newui_video_reviewer_username)
    LOGIN_PAGE.enter_password(PDI.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


# LQ-136695
@when('the video reviewer plus role user enters username/password and clicks the login button')
def video_reviewer_plus_user_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.newui_video_reviewer_plus_username)
    LOGIN_PAGE.enter_password(PDI.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


@then(
    'the user should successfully login to newui and land on the Video Search page, and fleet telematics should not be displayed')
def verify_user_on_video_search_with_new_ui_shell():
    assert LOGIN_PAGE.lytx_logo_new_ui_is_displayed() is True
    assert_that(DASHBOARD_PAGE.get_video_search_title(), IsEqualIgnoringCase("Video Search"))
    assert DASHBOARD_PAGE.fleet_telematics_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.driver_safety_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    assert DASHBOARD_PAGE.admin_title_is_displayed() is False
    LOGIN_PAGE.click_profile_btn()
    LOGIN_PAGE.click_sign_out_button_newui()


# LQ-147462
@when('the compliance manager role user enters username/password and clicks the login button')
def compliance_manager_user_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.newui_compliance_manager_username)
    LOGIN_PAGE.enter_password(PDI.newui_compliance_role_password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


# LQ-147461
@when('the compliance read only role user enters username/password and clicks the login button')
def compliance_read_only_user_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.newui_compliance_read_only_username)
    LOGIN_PAGE.enter_password(PDI.newui_compliance_role_password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


@then(
    'the user should successfully login to newui and land on the Driver Safety Home page, tabs such as Driver Safety and Admin should be displayed but not fleet telematics')
def verify_user_on_driver_safety_with_new_ui_shell():
    assert LOGIN_PAGE.lytx_logo_new_ui_is_displayed() is True
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert DASHBOARD_PAGE.fleet_telematics_title_is_displayed() is False
    assert DASHBOARD_PAGE.video_search_title_is_displayed() is False
    assert DASHBOARD_PAGE.dvir_title_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_tracking_title_is_displayed() is False
    assert DASHBOARD_PAGE.hos_title_is_displayed() is False
    LOGIN_PAGE.click_profile_btn()
    LOGIN_PAGE.click_sign_out_button_newui()


# LQ-193844
@when('the fleet telematics manager role user enters username/password and clicks the login button')
def fleet_telematics_manager_login(browser):
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(PDI.newui_fleet_telematics_manager_username)
    LOGIN_PAGE.enter_password(PDI.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


@then('the user should successfully login to newui and land on the Admin page and Fleet Telematics should be displayed')
def verify_user_on_fleet_telematics_with_new_ui_shell():
    assert LOGIN_PAGE.lytx_logo_new_ui_is_displayed() is True
    assert_that(DASHBOARD_PAGE.get_fleet_telematics_title(), IsEqualIgnoringCase("Fleet Telematics"))
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    LOGIN_PAGE.click_profile_btn()
    LOGIN_PAGE.click_sign_out_button_newui()

@then('the user should successfully land on the HOS page and fleet telematics should not be displayed')
def verify_user_on_hos():
    assert_that(DASHBOARD_PAGE.get_hos_title(), IsEqualIgnoringCase("HOS"))
    assert DASHBOARD_PAGE.eld_error_message_is_displayed() is False
    assert DASHBOARD_PAGE.fleet_telematics_title_is_displayed() is False
    LOGIN_PAGE.click_profile_btn()
    LOGIN_PAGE.click_sign_out_button_newui()