
from pytest_bdd import scenarios, given, when, then
from pages.dashboard_page import DashboardPage
from pages.location_page import LocationPage
from pages.login_page import LoginPage
from steps.common import WELCOME_URL, ENV
from data.int.home_data_int import HomeDataInt as HD_INT
from data.prod.home_data_prod import HomeDataProd as HD_PROD
from data.stg.home_data_stg import HomeDataStg as HD_STG
from data.prod.location_data_prod import LocationData as LD_PROD
from data.int.location_data_int import LocationData as LD_INT
from data.stg.location_data_stg import LocationData as LD_STG

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
LOCATION_PAGE = 0
LOCATION_NAME = 0
FILE_NAME = 0
LOCATION_COUNT = 0
CURRENT_PAGE_DATA = 0
IC_URL = WELCOME_URL + '?target=implementationcenter'

scenarios('../features/implementation_center_location.feature')

def get_location_headers():
    return [
            'RowNumber* (provide a unique # for each record, e.g. 1,2,3)',
            'LocationName* (provide name of location, e.g. not to exceed 255 characters)',
            'FirstName* (provide location contact first name, e.g. not to exceed 255 characters)',
            'LastName* (provide location contact last name, e.g. not to exceed 255 characters)',
            'Phone* (provide a valid phone number, e.g. 000-000-0000 or 1234567890)',
            'Email* (provide a valid email address, not to exceed 255 characters, e.g. first.last@domain.com)',
            'Address1* (provide a valid address, not to exceed 255 characters)',
            'Address2 (optional address line, must not exceed 255 characters, e.g. Unit #2)',
            'City* (provide a valid city, not exceed 255 characters)',
            'Country* (provide a valid country name, e.g. United States, Canada, or United Kingdom)',
            'State* (provide a valid state identifier, e.g. IL, CA, AB)',
            'PostalCode* (provide a valid postal or zip code, e.g. 60606 or K1A 0B1)',
            'IsActive* (indicate if this location should be marked active, e.g. True, False, Yes, No)'
            ]

@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, LOCATION_PAGE, HD, LD, ID

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    LOCATION_PAGE = LocationPage(browser)

    browser.get(IC_URL)

    if ENV == 'int':
        HD = HD_INT
        LD = LD_INT
    elif ENV == 'stg':
        HD = HD_STG
        LD = LD_STG
    else:
        HD = HD_PROD
        LD = LD_PROD

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

@when('user navigate to location page')
def validate_app_and_page_heading():
    LOCATION_PAGE.click_location_nav_menu()

@then('validate location dashboard app heading and page heading')
def validate_add_location_pop_up_visible():
    assert LOCATION_PAGE.get_location_page_title() == 'Locations'
    assert DASHBOARD_PAGE.get_implementation_center_title() == 'Implementation Center'

@then('validate location page add location pop up')
def validate_add_location_pop_up_visible():
    LOCATION_PAGE.click_add_location_btn()
    assert LOCATION_PAGE.get_pop_up_title() == 'Add Location'

@then('validate all labels and placeholder')
def validate_label_and_placeholder():
    #labels
    assert LOCATION_PAGE.get_location_lbl() == 'LOCATION NAME'
    assert LOCATION_PAGE.get_email_lbl() == 'EMAIL'
    assert LOCATION_PAGE.get_first_name_lbl() == 'FIRST NAME'
    assert LOCATION_PAGE.get_last_name_lbl() == 'LAST NAME'
    assert LOCATION_PAGE.get_phone_no_lbl() == 'PHONE'
    assert LOCATION_PAGE.get_country_lbl() == 'COUNTRY'
    assert LOCATION_PAGE.get_address_lbl() == 'ADDRESS'
    assert LOCATION_PAGE.get_address_2_lbl() == 'ADDRESS2 (OPTIONAL)'
    assert LOCATION_PAGE.get_city_lbl() == 'CITY'
    assert LOCATION_PAGE.get_state_lbl() == 'STATE'
    assert LOCATION_PAGE.get_postal_code_lbl() == 'POSTAL CODE'
    assert LOCATION_PAGE.get_cancel_lbl() == 'Cancel'
    assert LOCATION_PAGE.get_inactive_save_btn_lbl() == 'Save'
    assert LOCATION_PAGE.get_inactive_toggle_lbl() == 'Inactive'
    assert LOCATION_PAGE.get_active_toggle_lbl() == 'Active'
    # placeholders
    assert LOCATION_PAGE.get_location_ph() == 'Add unique name'
    assert LOCATION_PAGE.get_email_ph() == 'email@company.com'
    assert LOCATION_PAGE.get_first_name_ph() == ''
    assert LOCATION_PAGE.get_last_name_ph() == ''
    assert LOCATION_PAGE.get_phone_no_ph() == '000-000-0000'
    assert LOCATION_PAGE.get_country_option_ph() == 'Select Country'
    assert LOCATION_PAGE.get_address_ph() == ''
    assert LOCATION_PAGE.get_address_2_ph() == ''
    assert LOCATION_PAGE.get_city_ph() == ''
    assert LOCATION_PAGE.get_state_ph() == ''
    assert LOCATION_PAGE.get_postal_code_ph() == ''

@when('click on select country dropdown')
def click_on_select_country_dropdown():
    LOCATION_PAGE.click_on_country_dropdown()

@then('validate USA and canada country option visible')
def validate_country_optn_visible():
    assert LOCATION_PAGE.validate_countries_visible()[0] == 'Select Country'
    assert LOCATION_PAGE.validate_countries_visible()[1] == 'UNITED STATES'
    assert LOCATION_PAGE.validate_countries_visible()[2] == 'CANADA'

@when('save the location information')
def save_the_location_information():
    global LOCATION_NAME
    LOCATION_PAGE.select_usa_country()
    LOCATION_NAME = LOCATION_PAGE.set_location_name()
    LOCATION_PAGE.set_email(LD.email)
    LOCATION_PAGE.set_first_name(LD.first_name)
    LOCATION_PAGE.set_last_name(LD.last_name)
    LOCATION_PAGE.set_phone(LD.phone)
    LOCATION_PAGE.set_address(LD.usa_address)
    LOCATION_PAGE.set_address2(LD.usa_address2)
    LOCATION_PAGE.set_city(LD.usa_city)
    LOCATION_PAGE.select_state(LD.usa_state)
    LOCATION_PAGE.set_postal_code(LD.usa_postal_code)
    LOCATION_PAGE.click_save_btn()
    LOCATION_PAGE.click_yes_btn_popup()

@then('Validate location success notification should appear')
def validate_success_notifi():
    assert LOCATION_PAGE.validate_success_notify_icon() == 'check_circle'
    assert LOCATION_PAGE.validate_success_notify_msg() == 'Success - Location added successfully.'
    assert LOCATION_PAGE.validate_success_notify_cross_icon() == 'close'

@then('validate the recently added record on location page')
def validate_recent_location():
    assert LOCATION_PAGE.validate_location_name() == LOCATION_NAME
    assert LOCATION_PAGE.validate_location_address_info() == LD.usa_address+' '+LD.usa_city+', '+LD.usa_state_code+' '+LD.usa_postal_code+' '+LD.usa_country_code
    assert LOCATION_PAGE.validate_contact_info() == LD.first_name+' '+LD.last_name+' '+LD.phone
    assert LOCATION_PAGE.validate_active_status() == 'on'

@when('user navigate to edit location pop up')
def navigate_to_location_on_edit_popup():
    LOCATION_PAGE.click_location_edit_button()

@then('Validate location info on edit location')
def validate_recent_location_on_edit_popup():
    assert LOCATION_PAGE.validate_location_name_edit_popup() == LOCATION_NAME
    assert LOCATION_PAGE.validate_email_edit_popup() == LD.email
    assert LOCATION_PAGE.validate_first_name_edit_popup() == LD.first_name
    assert LOCATION_PAGE.validate_last_name_edit_popup() == LD.last_name
    assert LOCATION_PAGE.validate_country_edit_popup() == LD.usa_country
    assert LOCATION_PAGE.validate_address_edit_popup() == LD.usa_address
    assert LOCATION_PAGE.validate_address2_edit_popup() == LD.usa_address2
    assert LOCATION_PAGE.validate_city_edit_popup() == LD.usa_city
    assert LOCATION_PAGE.validate_state_edit_popup().__contains__(LD.usa_state_edit_pop_up)
    assert LOCATION_PAGE.validate_postal_code_edit_popup() == LD.usa_postal_code

@then('close the edit popup')
def close_edit_popup():
    LOCATION_PAGE.close_popup()

@when('user click on pagination next button')
def click_pagination_next_btn():
    global CURRENT_PAGE_DATA
    CURRENT_PAGE_DATA = LOCATION_PAGE.get_page_records()
    LOCATION_PAGE.click_next_page_btn()

@then('validate next 50 records should be visible')
def validate_next_records():
    global CURRENT_PAGE_DATA
    first_page_data = CURRENT_PAGE_DATA
    second_page_data = LOCATION_PAGE.get_page_records()
    assert LOCATION_PAGE.validate_new_records(first_page_data,second_page_data)

@when('user click on pagination previous button')
def click_pagination_next():
    LOCATION_PAGE.click_previous_page_btn()

@then('validate previous 50 records should be visible')
def validate_previous_records():
    global CURRENT_PAGE_DATA
    first_page_data = CURRENT_PAGE_DATA
    previous_page_data = LOCATION_PAGE.get_page_records()
    assert LOCATION_PAGE.validate_previous_records(first_page_data,previous_page_data)

@when('user select Active filter')
def select_active_filter():
    LOCATION_PAGE.select_active_filter()

@then('validate only active records should be visible under table result')
def validate_active_records():
    assert LOCATION_PAGE.validate_active_records()

@when('user select Inactive filter')
def select_inactive_filter():
    LOCATION_PAGE.select_inactive_filter()

@then('validate only Inactive records should be visible under table result')
def validate_inactive_records():
    assert LOCATION_PAGE.validate_inactive_records()

@when('user select 100 rows count from Show row')
def select_100_rows_filter():
    LOCATION_PAGE.select_rows(100)

@when('user select 150 rows count from Show row')
def select_150_rows_filter():
    LOCATION_PAGE.select_rows(150)

@when('user select 200 rows count from Show row')
def select_200_rows_filter():
    LOCATION_PAGE.select_rows(200)

@when('user select 250 rows count from Show row')
def select_250_rows_filter():
    LOCATION_PAGE.select_rows(250)

@then('validate total 50 records should be visible by default')
def validate_50_records():
    assert LOCATION_PAGE.validate_records_visible() == 50

@then('validate total 100 records should be visible')
def validate_100_records():
    assert LOCATION_PAGE.validate_records_visible() == 100

@then('validate total 150 records should be visible')
def validate_150_records():
    assert LOCATION_PAGE.validate_records_visible() == 150

@then('validate total 200 records should be visible')
def validate_200_records():
    assert LOCATION_PAGE.validate_records_visible() == 200

@then('validate total 250 records should be visible')
def validate_250_records():
    assert LOCATION_PAGE.validate_records_visible() == 250

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

@when('user click on LYTX support center link')
def open_support_center():
    LOCATION_PAGE.open_support_center()

@then('user should land on Lytx support center dashboard')
def validate_support_center_dashboard():
    assert LOCATION_PAGE.validate_support_center() == 'Lytx Support'

@when('user provide the location name to search')
def provide_search_text():
    LOCATION_PAGE.set_search_text(LOCATION_NAME)

@then('validate result table should be filtered based on searched text')
def validate_search_on_location_page():
    assert LOCATION_PAGE.validate_search_result_count() == 1
    assert LOCATION_PAGE.validate_search_result_name(LOCATION_NAME)
    LOCATION_PAGE.clear_search_tx()

@when('user download the location template')
def download_template():
    global FILE_NAME
    FILE_NAME = LOCATION_PAGE.download_location_template()

@then('validate the downloaded location template')
def validate_location_template():
    location_headers = get_location_headers()
    assert LOCATION_PAGE.validate_file_header(FILE_NAME) == location_headers

@when('user upload location template')
def upload_location_template():
    location_headers = get_location_headers()
    global LOCATION_COUNT
    LOCATION_COUNT = 1
    LOCATION_PAGE.create_locations_in_template(FILE_NAME, location_headers,LD.usa_location_data,LOCATION_COUNT)
    LOCATION_PAGE.upload_template(FILE_NAME)

@when('user download location records')
def download_location_csv_file():
    global FILE_NAME
    FILE_NAME = LOCATION_PAGE.download_records()

@then('validate the downloaded location records')
def validate_location_records():
    download_location_headers = ['Location Name',
                                 'Location Address',
                                 'Location Contact',
                                 'Location Contact Phone',
                                 'Location Contact Email',
                                 'Address2',
                                 'Active',]
    assert LOCATION_PAGE.validate_file_header(FILE_NAME) == download_location_headers

@then('validate locations should be imported')
def validate_locations_imported():
    assert LOCATION_PAGE.validate_success_notify_icon() == 'check_circle'
    assert LOCATION_PAGE.validate_success_notify_msg() == 'Success - '+str(LOCATION_COUNT)+' out of '+str(LOCATION_COUNT)+' Locations imported successfully.'
    assert LOCATION_PAGE.validate_success_notify_cross_icon() == 'close'