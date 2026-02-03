from pytest_bdd import scenarios, given, when, then
from pages.dashboard_page import DashboardPage
from pages.group_page import GroupPage
from pages.location_page import LocationPage
from pages.vehicle_page import VehiclePage
from pages.login_page import LoginPage
from steps.common import WELCOME_URL, ENV
from data.int.home_data_int import HomeDataInt as HD_INT
from data.prod.home_data_prod import HomeDataProd as HD_PROD
from data.stg.home_data_stg import HomeDataStg as HD_STG

IC_URL = WELCOME_URL + '?target=implementationcenter'
LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
LOCATION_PAGE = 0
VEHICLE_PAGE = 0
LOCATION_NAME = 0
GROUP_PAGE = 0
FILE_NAME = 0

scenarios('../features/implementation_center_group.feature')

@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, LOCATION_PAGE, GROUP_PAGE, VEHICLE_PAGE, HD, LD, ID, FILE_NAME

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    LOCATION_PAGE = LocationPage(browser)
    VEHICLE_PAGE = VehiclePage(browser)
    GROUP_PAGE = GroupPage(browser)

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

@then('validate group page app heading and page heading')
def validate_app_and_page_heading():
    GROUP_PAGE.click_group_nav_menu()
    assert GROUP_PAGE.get_group_page_title() == 'Group, Hierarchy, and User Management'
    assert DASHBOARD_PAGE.get_implementation_center_title() == 'Implementation Center'

@when('user download the group template')
def download_template():
    global FILE_NAME
    FILE_NAME = GROUP_PAGE.download_group_template()

@when('user upload group template')
def upload_group_template():
    GROUP_PAGE.upload_template(FILE_NAME)

@then('validate group submission success pop up')
def validate_success_popup():
    under_process_statement = ('Await confirmation from Lytx that your submission has been made and '
                         'visible within the Install Portal. You can then use those new updates'
                         ' when submitting new vehicles and shipment requests.')
    title = GROUP_PAGE.validate_popup_title()
    assert title.startswith('Group_Hierarchy_Template') and title.endswith('successfully submitted')
    assert GROUP_PAGE.validate_popup_description() == 'We have received your new Group and Hierarchy request.'
    assert GROUP_PAGE.validate_popup_support_center() == 'You may also view all your open cases within the Lytx Support Center'
    assert GROUP_PAGE.validate_popup_acknowledgement() == under_process_statement

@then('close submission pop up')
def close_popup():
    GROUP_PAGE.close_popup()

@when('user click on LYTX support center link')
def open_support_center():
    LOCATION_PAGE.open_support_center()

@then('user should land on Lytx support center dashboard')
def validate_support_center_dashboard():
    assert LOCATION_PAGE.validate_support_center() == 'Lytx Support'

@when('user open welcome popup')
def open_welcome_popup():
    LOGIN_PAGE.click_profile_icon()
    LOCATION_PAGE.click_welcome_popup()

@then('validate welcome pop up')
def validate_welcome_popup():
    info = 'Your hub for managing device orders, tracking shipments, scheduling installations, and organizing your vehicle and location details for future requests.'
    steps_info = 'Follow these 3 simple steps to get started:'
    assert LOCATION_PAGE.validate_welcome_popup_logo()
    assert LOCATION_PAGE.validate_welcome_popup_title() == 'Introduction'
    assert LOCATION_PAGE.validate_welcome_popup_info() == info
    assert LOCATION_PAGE.validate_steps_info() == steps_info
    assert LOCATION_PAGE.validate_step1() == 'Setup'
    assert LOCATION_PAGE.validate_step2() == 'Request shipping & installation'
    assert LOCATION_PAGE.validate_step3() == 'Install your device(s)'
    assert LOCATION_PAGE.validate_secondary_btn() == 'Show me later'
    assert LOCATION_PAGE.validate_get_started_btn() == 'Begin Tour'
    LOCATION_PAGE.click_get_started()
    assert LOCATION_PAGE.validate_welcome_popup_title() == 'Setup Options'
    assert LOCATION_PAGE.validate_step_heading1() == 'Groups & Users:'
    assert LOCATION_PAGE.validate_step_content1() == 'Create your company structure, if not already established, then assign vehicles and users to the correct group(s).'
    assert LOCATION_PAGE.validate_step_heading2() == 'Locations:'
    assert LOCATION_PAGE.validate_step_content2() == 'Add shipment and installation addresses for order fulfillment.'
    assert LOCATION_PAGE.validate_step_heading3() == 'Vehicles:'
    assert LOCATION_PAGE.validate_step_content3() == 'Add vehicle details to receive the correct cabling.'
    assert LOCATION_PAGE.validate_secondary_btn() == 'Previous'
    assert LOCATION_PAGE.validate_primary_btn() == 'Next'
    LOCATION_PAGE.click_next_btn()
    assert LOCATION_PAGE.validate_welcome_popup_title() == 'Request Submission & Tracking'
    assert LOCATION_PAGE.validate_step_heading1() == 'Submit a Request:'
    assert LOCATION_PAGE.validate_step_content1() == 'Select your order #, location, and vehicle(s) for shipment & installation.'
    assert LOCATION_PAGE.validate_step_heading2() == 'Track Progress:'
    assert LOCATION_PAGE.validate_step_content2() == 'Monitor shipment and installations on your dashboard.'
    assert LOCATION_PAGE.validate_secondary_btn() == 'Previous'
    assert LOCATION_PAGE.validate_primary_btn() == 'Next'
    LOCATION_PAGE.click_next_btn()
    assert LOCATION_PAGE.validate_welcome_popup_title() == 'Installation Options'
    assert LOCATION_PAGE.validate_step_heading1() == 'Self-Install:'
    assert LOCATION_PAGE.validate_step_content1() == 'Use the Lytx Installation App (LIA) to properly configure your device.'
    assert LOCATION_PAGE.validate_step_heading2() == 'Managed Install:'
    assert LOCATION_PAGE.validate_step_content2() == 'Your installation date(s) will be coordinated shortly after your request has been submitted.'
    assert LOCATION_PAGE.validate_secondary_btn() == 'Previous'
    assert LOCATION_PAGE.validate_primary_btn() == 'Done'
    LOCATION_PAGE.click_done_btn()
    assert LOCATION_PAGE.validate_welcome_popup_title() == 'Final Setup'
    assert LOCATION_PAGE.validate_welcome_last_popup_info_bold() == '''You're ready to get started!'''
    assert LOCATION_PAGE.validate_welcome_last_popup_info() == 'Complete your setup and submit your request'

@then('close welcome popup')
def click_get_started():
    LOCATION_PAGE.click_ok_btn()

@then('validate file should be downloaded')
def validate_file_downloaded():
    assert GROUP_PAGE.validate_file_downloaded(FILE_NAME)