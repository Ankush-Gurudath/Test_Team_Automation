from pages.geotab_report_add_ins_page import GeotabReportAddIns
from hamcrest import assert_that
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then, parsers
from data.prod.geotab_report_add_ins_data_prod import GeotabReportAddInsPRODData as FTD_PROD
from data.stg.geotab_report_add_ins_data_stg import GeotabReportAddInsSTGData as FTD_STG
from data.int.geotab_report_add_ins_data_int import GeotabReportAddInsINTData as FTD_INT
from pages.dashboard_page import DashboardPage
from pages.fleet_telematics_left_panel_page import FleetTelematicsPageLeftPanel
from pages.fleet_telematics_center_page import FleetTelematicsCenterPage
from pages.login_page import LoginPage
from steps.common import ENV, NEW_UI_FTM_URL

GR = 0
BASE_PAGE = 0
GEOTAB_REPORT_PAGE = 0
FLEET_TELEMATICS_PAGE = 0
FLEET_TELEMATICS_CENTER_PAGE = 0
LOGIN_PAGE = 0
DASHBOARD_PAGE = 0


scenarios('../features/geotab_report_add_ins3.feature')


@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, GR, FLEET_TELEMATICS_PAGE, FLEET_TELEMATICS_CENTER_PAGE, GEOTAB_REPORT_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    FLEET_TELEMATICS_PAGE = FleetTelematicsPageLeftPanel(browser)
    GEOTAB_REPORT_PAGE = GeotabReportAddIns(browser)
    FLEET_TELEMATICS_CENTER_PAGE = FleetTelematicsCenterPage(browser)

    # Delete all previously uploaded files from browserstack and upload new set of files
    # # GEOTAB_REPORT_PAGE.delete_all_media_files()
    # GEOTAB_REPORT_PAGE.upload_files_and_store_yaml("xlsx_geotabreports_set3")

    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.wait_for_page_to_fully_load()

    if ENV == 'stg':
        GR = FTD_STG
    elif ENV == 'int':
        GR = FTD_INT
    elif ENV == 'prod':
        GR = FTD_PROD
    else:
        raise ValueError(f"Unsupported ENV value: '{ENV}'. Valid options are 'stg', 'int', or 'prod'.")


@when('the multi-company user enters username/password, clicks the login button in the page and select company from the list')
def login():
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.enter_username(GR.username)
    LOGIN_PAGE.enter_password(GR.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_multi_company(GR.company_name)
    LOGIN_PAGE.click_select_company_button()
    LOGIN_PAGE.wait_for_page_load()
    LOGIN_PAGE.wait_for_page_to_fully_load()


@then('the user is successfully logged into the Driver Safety dashboard')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    # Commenting until MEGA-4148 is resolved
    # assert FLEET_TELEMATICS_PAGE.lytx_geotab_logo_is_displayed() is True


# LQ-108840
@when('the user clicks Fleet Telematics tab')
def navigate_to_fleet_telematics():
    DASHBOARD_PAGE.click_fleet_telematics_tab()


@then('the Fleet Telematics main page is loaded successfully')
def verify_user_on_fleet_telematics():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_PAGE.more_charts_button_is_displayed() is True
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_reports_menu()
    FLEET_TELEMATICS_PAGE.click_report_setup_submenu()
    FLEET_TELEMATICS_PAGE.wait_for_page_to_fully_load()
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()

# LQ-
@when(parsers.parse('the user clicks upload file, configure {report_name} and send email'))
def click_upload_file_configure_email_report(report_name):
    FLEET_TELEMATICS_PAGE.wait_for_page_to_fully_load()
    FLEET_TELEMATICS_CENTER_PAGE.click_custom_report()
    print(f"Uploading report: {report_name}")
    GEOTAB_REPORT_PAGE.file_upload_preloaded_files(report_name)
    # GEOTAB_REPORT_PAGE.upload_file_locally("xlsm_geotabreports_set2", report_name+".xlsm")
    GEOTAB_REPORT_PAGE.configure_report_send_email()
    GEOTAB_REPORT_PAGE.add_individual_email(GR.fleet_telematics_manager_user)
    # GEOTAB_REPORT_PAGE.select_refresh_period_30min()
    GEOTAB_REPORT_PAGE.select_time_now_option()
    GEOTAB_REPORT_PAGE.save_report_and_wait_for_dashboard()
    FLEET_TELEMATICS_PAGE.wait_for_page_to_fully_load()
    FLEET_TELEMATICS_PAGE.wait_for_page_load()


@then(parsers.parse('the user should be able to see the saved {report_name} in dashboard'))
def verify_report_in_dashboard(report_name):
    GEOTAB_REPORT_PAGE.scroll_page_up()
    assert FLEET_TELEMATICS_CENTER_PAGE.report_setup_header_is_displayed() is True
    assert GEOTAB_REPORT_PAGE.saved_report_exists_in_dashboard(report_name) is True
    FLEET_TELEMATICS_CENTER_PAGE.click_refresh_button()
    FLEET_TELEMATICS_PAGE.wait_for_page_to_fully_load()
    FLEET_TELEMATICS_PAGE.wait_for_page_load()
    # assert GEOTAB_REPORT_PAGE.get_reportname_dashboard(report_name) == report_name+"_testautomation"


@when('the user search by test_automation, preview it and click on remove button')
def remove_testdata():
    FLEET_TELEMATICS_CENTER_PAGE.report_setup_header_is_displayed()
    FLEET_TELEMATICS_PAGE.wait_for_page_to_fully_load()
    GEOTAB_REPORT_PAGE.remove_all_automation_reports()
    FLEET_TELEMATICS_CENTER_PAGE.click_refresh_button()
    FLEET_TELEMATICS_PAGE.wait_for_page_to_fully_load()
    FLEET_TELEMATICS_PAGE.wait_for_page_load()


@then('the user should not see the reports with test_automation in dashboard')
def verify_testdata():
    assert FLEET_TELEMATICS_CENTER_PAGE.report_setup_header_is_displayed() is True
    print("----Report deleted successfully----")
    assert GEOTAB_REPORT_PAGE.saved_report_exists_in_dashboard() is False
    GEOTAB_REPORT_PAGE.scroll_page_up()