from hamcrest import assert_that, contains_string
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from data.prod.geotab_add_ins_data_prod import GeotabAddInsDataPROD as GP_PROD
from data.stg.geotab_add_ins_data_stg import GeotabAddInsDataSTG as GP_STG
from data.stg.geotab_add_ins_data_stg import GeotabAddInsDataSTG as GP_INT
from pages.dashboard_page import DashboardPage
from pages.fleet_telematics_left_panel_page import FleetTelematicsPageLeftPanel
from pages.fleet_telematics_center_page import FleetTelematicsCenterPage
from pages.login_page import LoginPage
from steps.common import ENV, NEW_UI_FTM_URL, GEOTAB_URL
from pytest_bdd import scenarios, given, when, then, parsers
from pages.geotab_page_add_ins_page import GeotabPageAddIns

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
BASE_PAGE = 0
FLEET_TELEMATICS_PAGE = 0
FLEET_TELEMATICS_CENTER_PAGE = 0
GR = 0
GEOTAB_PAGE_ADDIN = 0

scenarios('../features/geotab_page_add_ins.feature')


@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, FLEET_TELEMATICS_PAGE, FLEET_TELEMATICS_CENTER_PAGE, GP, GEOTAB_PAGE_ADDIN

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    FLEET_TELEMATICS_PAGE = FleetTelematicsPageLeftPanel(browser)
    FLEET_TELEMATICS_CENTER_PAGE = FleetTelematicsCenterPage(browser)
    GEOTAB_PAGE_ADDIN = GeotabPageAddIns(browser)

    browser.get(NEW_UI_FTM_URL)

    if ENV == 'stg':
        GP = GP_STG
    elif ENV == 'int':
        GP = GP_INT
    elif ENV == 'prod':
        GP = GP_PROD
    else:
        raise ValueError(f"Unsupported ENV value: '{ENV}'. Valid options are 'stg', 'int', or 'prod'.")


@when(
    'the multi-company user enters username/password, clicks the login button in the page and select company from the list')
def login():
    LOGIN_PAGE.enter_username(GP.username)
    LOGIN_PAGE.enter_password(GP.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_multi_company(GP.company_name)
    LOGIN_PAGE.click_select_company_button()
    LOGIN_PAGE.wait_for_page_load()


@then('the user is successfully logged into the Driver Safety dashboard')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    # Commenting until MEGA-4148 is resolved
    # assert FLEET_TELEMATICS_PAGE.lytx_geotab_logo_is_displayed() is True
    assert DASHBOARD_PAGE.no_of_unassigned_drivers_is_displayed() is True
    assert DASHBOARD_PAGE.get_unassigned_drivers_text() == "UNASSIGNED DRIVERS"
    assert_that(DASHBOARD_PAGE.get_unassigned_drivers_text(), contains_string("UNASSIGNED DRIVER"))
    assert DASHBOARD_PAGE.get_due_for_coaching_text() == "DUE FOR COACHING"
    assert DASHBOARD_PAGE.get_fyi_notify_text() == "FYI NOTIFY"
    assert_that(DASHBOARD_PAGE.get_collisions_text(), contains_string("COLLISION"))
    assert_that(DASHBOARD_PAGE.get_possible_collisions_text(), contains_string("POSSIBLE COLLISION"))


# LQ-108840
@when('the user clicks Fleet Telematics tab')
def navigate_to_fleet_telematics():
    DASHBOARD_PAGE.click_fleet_telematics_tab()
    DASHBOARD_PAGE.wait_for_page_to_fully_load()


@then('the Fleet Telematics main page is loaded successfully')
def verify_user_on_fleet_telematics():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_PAGE.more_charts_button_is_displayed() is True
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.wait_for_page_to_fully_load()


@when('the user clicks config menu > Fleet Settings sub-menu')
def navigate_to_fleet_settings():
    FLEET_TELEMATICS_PAGE.click_config_menu()
    FLEET_TELEMATICS_PAGE.click_fleet_settings_submenu()
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    FLEET_TELEMATICS_PAGE.wait_for_page_to_fully_load()
    FLEET_TELEMATICS_PAGE.wait_for_page_to_fully_load()


@then('the Fleet Settings page is loaded successfully')
def verify_user_on_fleet_settings():
    assert FLEET_TELEMATICS_CENTER_PAGE.system_settings_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.general_tab_is_displayed() is True
    FLEET_TELEMATICS_PAGE.wait_for_page_to_fully_load()
    assert FLEET_TELEMATICS_CENTER_PAGE.addins_tab_is_displayed() is True


@when(parsers.parse(
    'the user clicks Config menu > Fleet Settings sub-menu and add the config "{addin_name}" in the configuration tab'))
def add_config(addin_name):
    FLEET_TELEMATICS_CENTER_PAGE.click_addins_tab()
    FLEET_TELEMATICS_CENTER_PAGE.scroll_page_down()
    FLEET_TELEMATICS_CENTER_PAGE.click_create_add_ins()
    if addin_name == "fbt":
        FLEET_TELEMATICS_CENTER_PAGE.add_config_in_text_area(GP.fbt)
    elif addin_name == "eld support":
        FLEET_TELEMATICS_CENTER_PAGE.add_config_in_text_area(GP.eld_support)
    elif addin_name == "compliance data summary":
        FLEET_TELEMATICS_CENTER_PAGE.add_config_in_text_area(GP.compliance_data_summary)
    elif addin_name == "eld settings validator":
        FLEET_TELEMATICS_CENTER_PAGE.add_config_in_text_area(GP.eld_settings_validator)
    elif addin_name == "evsa":
        FLEET_TELEMATICS_CENTER_PAGE.add_config_in_text_area(GP.evsa)
    elif addin_name == "import hos logs":
        FLEET_TELEMATICS_CENTER_PAGE.add_config_in_text_area(GP.import_hos_logs)
    elif addin_name == "hos driver summary":
        FLEET_TELEMATICS_CENTER_PAGE.add_config_in_text_area(GP.hos_driver_summary)
    FLEET_TELEMATICS_CENTER_PAGE.click_save_config_button()


@then('the user should be able to add the config')
def verify_config():
    assert FLEET_TELEMATICS_CENTER_PAGE.disabled_save_button_is_displayed() is True
    FLEET_TELEMATICS_CENTER_PAGE.click_refresh_button()
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)


@when('the user click on AddIns menu')
def click_addins_menu():
    FLEET_TELEMATICS_PAGE.scroll_page_down()
    FLEET_TELEMATICS_PAGE.click_addins_menu()


@then('the AddIns menu is displayed with all the configured addins in left panel')
def verify_addins_menu():
    assert FLEET_TELEMATICS_PAGE.fbt_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE.hos_driver_summary_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE.import_hos_logs_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE.eld_info_config_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE.eld_settings_validator_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE.evsa_submenu_is_displayed() is True


@when(parsers.parse('the user click on "{addin_name}" config in the AddIns menu'))
def click_addins_submenu(addin_name):
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_addin_submenu(addin_name)


@then(parsers.parse('"{addin_name}" page loads fine'))
def verify_addins_submenus(addin_name):
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.addin_header_is_displayed_new_ui(addin_name) is True


@given('mygeotab login page is displayed in the browser')
def launch_geotab_browser(browser):
    browser.get(GEOTAB_URL)
    GEOTAB_PAGE_ADDIN.wait_for_page_to_fully_load()


@when('the fa user enters username and password')
def enter_geotab_user_credentials():
    GEOTAB_PAGE_ADDIN.enter_username(GP.fa_username)
    GEOTAB_PAGE_ADDIN.enter_password(GP.fa_password)
    GEOTAB_PAGE_ADDIN.click_login()
    GEOTAB_PAGE_ADDIN.wait_for_page_to_fully_load()


@then('the user logs into the geotab dashboard with header "Product Guide" and company logo mygeotab is displayed')
def verify_geotab_dashboard():
    assert GEOTAB_PAGE_ADDIN.dashboard_is_displayed() is True
    assert GEOTAB_PAGE_ADDIN.company_logo_is_displayed() is True


@when(parsers.parse('user search and click on "{addin_name}" config in mygeotab dashboard'))
def search_addin(addin_name):
    GEOTAB_PAGE_ADDIN.search_and_click_addin(addin_name)


@then(parsers.parse('"{addin_name}" page with header should load fine'))
def verify_addin_page(addin_name):
    assert GEOTAB_PAGE_ADDIN.verify_addins_page(addin_name) is True


@when('user search for compliance data summary in Map menu')
def search_compliance_data_summary():
    GEOTAB_PAGE_ADDIN.click_map_menu()


@then('compliance data summary should be present in Map menu')
def verify_compliance_data_summary():
    assert GEOTAB_PAGE_ADDIN.compliance_data_summary_is_displayed() is True