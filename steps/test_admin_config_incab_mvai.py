from pytest_bdd import scenarios, given, when, then
from pages.dashboard_page import DashboardPage
from pages.configuration_setting_page import ConfigurationSettingPage
from pages.login_page import LoginPage
from steps.common import DC_URL, ENV
from pages.user_management_page import UserManagementPage
from data.prod.admin_data_prod import AdminDataProd as AD_PROD
from data.stg.admin_data_stg import AdminDataStg as AD_STG
from data.int.admin_data_int import AdminDataInt as AD_INT

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
CONFIGURATION_SETTING_PAGE = 0
USER_MANAGEMENT_PAGE = 0
AD = 0

scenarios('../features/admin_config_incab_mvai.feature')


# LQ-180649
@given('the "Administrator" user is in the "Program Configuration" tab of "CONFIGURATION SETTINGS"')
def login_as_admin(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, CONFIGURATION_SETTING_PAGE, USER_MANAGEMENT_PAGE, AD

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)
    CONFIGURATION_SETTING_PAGE = ConfigurationSettingPage(browser)

    browser.get(DC_URL)

    if ENV == 'int':
        AD = AD_INT
    elif ENV == 'stg':
        AD = AD_STG
    elif ENV == 'prod':
        AD = AD_PROD
    else:
        raise ValueError(f"Unsupported ENV value: '{ENV}'. Valid options are 'stg', 'int', or 'prod'.")

    LOGIN_PAGE.enter_username(AD.admin_user_name)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_company()
    LOGIN_PAGE.click_select_company_button()
    LOGIN_PAGE.retry_if_login_failed_new_ui(DC_URL, AD.admin_user_name, AD.password, AD.company_name)
    DASHBOARD_PAGE.click_admin_tab()
    USER_MANAGEMENT_PAGE.click_config_setting_tab()
    CONFIGURATION_SETTING_PAGE.click_program_configuration_tab()


@when('the user selects the "In-Cab MV+AI" tab')
def navigate_to_config_setting_page():
    CONFIGURATION_SETTING_PAGE.click_incab_mvai_tab()


@then('the user should see a header "In-Cab MV+AI"')
def verify_in_cab_mvai_header():
    assert CONFIGURATION_SETTING_PAGE.get_incab_mvai_page_title() == "In-Cab MV+AI"


@then('the description should be "These features are compatible with SF300 devices and newer"')
def verify_in_cab_mvai_description():
    assert CONFIGURATION_SETTING_PAGE.incab_mvai_description_is_displayed()


# LQ-180749
@then(
    'the user should see the section "Smoking" with description "Detection of driver smoking while the vehicle is in motion."')
def verify_feature_smoking():
    assert CONFIGURATION_SETTING_PAGE.smoking_description_is_displayed()


# LQ-180750
@then(
    'the user should see the section "Food and Drink" with description "Detection of driver eating or drinking while the vehicle is in motion."')
def verify_feature_food_drink():
    assert CONFIGURATION_SETTING_PAGE.food_drink_description_is_displayed()


# LQ-180751
@then(
    'the user should see the section "Inattentive" with description "Detection of driver lacking sufficient focus on the road while the vehicle is in motion."')
def verify_feature_inattentiveness():
    assert CONFIGURATION_SETTING_PAGE.inattentiveness_description_is_displayed()


# LQ-180752
@then(
    'the user should see the section "Lens Obstruction" with description "Detection of obstruction of the inside lens while the vehicle is in motion."')
def verify_feature_lens_obstruction():
    assert CONFIGURATION_SETTING_PAGE.lens_obstruction_description_is_displayed()


# LQ-180756
@then(
    'the user should see the section "No Seatbelt" with description "Detection of driver not wearing or improperly wearing the seatbelt while the vehicle is in motion."')
def verify_feature_no_seatbelt():
    assert CONFIGURATION_SETTING_PAGE.no_seatbelt_description_is_displayed()


# LQ-180753
@then(
    'the user should see the section "Handheld Device" with description "Detection of driver holding and/or actively using a handheld device while the vehicle is in motion."')
def verify_feature_handheld_device():
    assert CONFIGURATION_SETTING_PAGE.handheld_device_description_is_displayed()


# LQ-180749
@then(
    'the user should see all the sections with three checkboxes: "Audio Alerts", "LED Alerts", "Events" and each checkbox should be clickable')
def verify_all_incab_mvai_checkboxes():
    assert CONFIGURATION_SETTING_PAGE.verify_feature_checkboxes_clickable()

# PHNX-5447
@when('the user clicks the checkbox for Smoking and clicks on save changes')
def click_checkboxes_smoking_and_save():
    CONFIGURATION_SETTING_PAGE.click_smoking_audio_alerts_checkbox()
    CONFIGURATION_SETTING_PAGE.click_save_button_incab_mvai()
    CONFIGURATION_SETTING_PAGE.click_confirmation_popup_save_button()

@then('the changes should be saved with a confirmation message "Changes saved successfully"')
def verify_changes_saved_confirmation_message():
    assert CONFIGURATION_SETTING_PAGE.alert_success_message_is_displayed()

