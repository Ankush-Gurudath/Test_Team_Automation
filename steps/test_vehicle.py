from pytest_bdd import scenarios, given, when, then
from pages.dashboard_page import DashboardPage
from pages.location_page import LocationPage
from pages.vehicle_page import VehiclePage
from pages.login_page import LoginPage
from steps.common import WELCOME_URL, ENV
from data.int.home_data_int import HomeDataInt as HD_INT
from data.prod.home_data_prod import HomeDataProd as HD_PROD
from data.stg.home_data_stg import HomeDataStg as HD_STG
from data.int.vehicle_data_int import VehicleData as VD_INT
from data.stg.vehicle_data_stg import VehicleData as VD_STG
from data.prod.vehicle_data_prod import VehicleData as VD_PROD

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
LOCATION_PAGE = 0
LOCATION_NAME = 0
VEHICLE_PAGE = 0
IC_URL = WELCOME_URL + "?target=implementationcenter"

scenarios('../features/implementation_center_vehicle.feature')

def get_vehicle_headers():
    return [
        "VehicleName* (provide a vehicle name, e.g. not to exceed 255 characters)",
        "VIN* (provide a valid and unique VIN, e.g. not to exceed 17 characters i.e. 5XYKT3A10BG070457)",
        "DiagnosticPortOccupied* (required only if light duty VIN detected, e.g. Yes, or No)",
        "DVIR (optional field for driver-vehicle inspection report, e.g. Enabled, or Disabled)",
        "LicenseState (optional provide a valid state identifier, e.g. IL, CA, AB)",
        "LicensePlate (optional provide a valid license plate ID, e.g. not to exceed 50 characters)",
        "Group* (required - use Group Look-up in Implementation Center for accurate naming)",
        "LocationName* (provide a name, e.g. must match existing location name within Install Portal and not to exceed 255 characters)",
        "Quote # (optional provide a upto 10 digit numeric string prefixed with 'Q-')"
    ]

@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, LOCATION_PAGE, VEHICLE_PAGE , HD, VD

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    LOCATION_PAGE = LocationPage(browser)
    VEHICLE_PAGE = VehiclePage(browser)

    browser.get(IC_URL)

    if ENV == 'int':
        HD = HD_INT
        VD = VD_INT
    elif ENV == 'stg':
        HD = HD_STG
        VD = VD_STG
    else:
        HD = HD_PROD
        VD = VD_PROD

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

@then('validate vehicle dashboard app heading and page heading')
def validate_app_and_page_heading():
    VEHICLE_PAGE.click_vehicle_nav_menu()
    assert DASHBOARD_PAGE.get_implementation_center_title() == 'Implementation Center'
    assert VEHICLE_PAGE.get_vehicle_page_title() == "Vehicle Lists"

@when('user click on Add vehicle button on Vehicle Lists page')
def click_on_add_vehicle_button():
    VEHICLE_PAGE.click_add_vehicle_btn()

@then('validate add vehicle pop up')
def validate_add_vehicle_pop_up_visible():
    assert VEHICLE_PAGE.get_pop_up_title() == 'Add Vehicles'

@then('validate all labels and placeholder')
def validate_label_and_placeholder():
    assert VEHICLE_PAGE.get_popup_element_lbl('group','Group') == "GROUP\n*"
    assert VEHICLE_PAGE.get_popup_element_lbl('input','vehicleName') == "VEHICLE NAME\n*"
    assert VEHICLE_PAGE.get_popup_element_lbl('input','vin') == "VIN\n*"
    assert VEHICLE_PAGE.get_popup_element_lbl('input','location') == "LOCATION NAME\n*"
    assert VEHICLE_PAGE.get_popup_element_lbl('select','diagnosticPort') == "DIAGNOSTIC PORT OCCUPIED\n*"
    assert VEHICLE_PAGE.get_additional_lbl() == "ADDITIONAL"
    assert VEHICLE_PAGE.get_popup_element_lbl('select','quote_number') == "ORDER"
    assert VEHICLE_PAGE.get_popup_element_lbl('select','licenseState') == "LICENSE STATE"
    assert VEHICLE_PAGE.get_popup_element_lbl('select','dvir') == "DVIR"
    assert VEHICLE_PAGE.get_popup_element_lbl('input','licensePlate') == "LICENSE PLATE"
    assert VEHICLE_PAGE.get_btn_lbl('button') == "Cancel"
    assert VEHICLE_PAGE.get_btn_lbl('submit') == "Save"
    assert VEHICLE_PAGE.get_btn_lbl('reset') == "Reset"

@when('save the vehicle information')
def save_the_vehicle_information():
    VEHICLE_PAGE.set_group(VD.group)
    VEHICLE_PAGE.set_vehicle_name(VD.vehicle_name)
    VEHICLE_PAGE.set_vin(VD.vin)
    VEHICLE_PAGE.set_location_name(VD.location_name)
    VEHICLE_PAGE.set_diagnostic_port(VD.diagnostic_port)
    VEHICLE_PAGE.set_order(VD.order)
    VEHICLE_PAGE.set_license_state(VD.license_state)
    VEHICLE_PAGE.select_dvir(VD.dvir)
    VEHICLE_PAGE.set_license_plate(VD.license_plate)
    LOCATION_PAGE.click_save_btn()

@then('Validate add vehicle success notification should appear')
def validate_success_notifi():
    assert LOCATION_PAGE.validate_success_notify_icon() == 'check_circle'
    assert LOCATION_PAGE.validate_success_notify_msg() == 'Success - Vehicle added successfully.'
    assert LOCATION_PAGE.validate_success_notify_cross_icon() == 'close'

@then('validate the recently added record on vehicle page')
def validate_recent_location():
    assert VEHICLE_PAGE.validate_vehicle_name() == VD.vehicle_name
    assert VEHICLE_PAGE.validate_vin() == VD.vin
    assert VEHICLE_PAGE.validate_location_name() == VD.location_name
    assert VEHICLE_PAGE.validate_quote() == ""
    assert VEHICLE_PAGE.validate_install_status() == 'Created Not Assigned'

@when('user will delete recently added vehicle')
def delete_vehicle():
    VEHICLE_PAGE.delete_vehicle()

@then('Validate vehicle delete notification should appear')
def validate_delete_notifi():
    assert LOCATION_PAGE.validate_success_notify_icon() == 'check_circle'
    assert LOCATION_PAGE.validate_success_notify_msg() == 'Success - Vehicle deleted successfully.'
    assert LOCATION_PAGE.validate_success_notify_cross_icon() == 'close'

@then('save updated details of vehicle information')
def save_the_updated_vehicle_information():
    VEHICLE_PAGE.clear_vehicle_name()
    VEHICLE_PAGE.set_updated_vehicle_name(VD.updated_vehicle_name)
    VEHICLE_PAGE.clear_vin()
    VEHICLE_PAGE.set_vin(VD.updated_vin)
    VEHICLE_PAGE.clear_location_name()
    VEHICLE_PAGE.set_location_name(VD.updated_location_name)
    VEHICLE_PAGE.set_diagnostic_port(VD.updated_diagnostic_port)
    VEHICLE_PAGE.set_order(VD.updated_order)
    VEHICLE_PAGE.set_license_state(VD.updated_license_state)
    VEHICLE_PAGE.select_dvir(VD.updated_dvir)
    VEHICLE_PAGE.clear_license_plate()
    VEHICLE_PAGE.set_license_plate(VD.updated_license_plate)
    LOCATION_PAGE.click_save_btn()

@then('Validate updated vehicle success notification should appear')
def validate_success_notifi():
    assert  LOCATION_PAGE.validate_success_notify_icon() == 'check_circle'
    assert LOCATION_PAGE.validate_success_notify_msg() == 'Success - Vehicle updated successfully.'
    assert LOCATION_PAGE.validate_success_notify_cross_icon() == 'close'

@when('user click on recently added vehicle')
def user_click_on_recent_vehicle():
    VEHICLE_PAGE.click_vehicle_edit_btn()

@then('Validate vehicle info on edit vehicle')
def validate_edit_vehicle():
    VEHICLE_PAGE.popup_heading() == "Edit Vehicles"
    VEHICLE_PAGE.validate_group_edit_popup() == VD.group
    VEHICLE_PAGE.validate_vehicle_name_edit_popup() == VD.vehicle_name
    VEHICLE_PAGE.validate_vin_edit_popup() == VD.vin
    VEHICLE_PAGE.validate_location_name_edit_popup() == VD.location_name
    VEHICLE_PAGE.validate_dia_edit_popup() == VD.diagnostic_port
    VEHICLE_PAGE.validate_order_edit_popup() == VD.order
    VEHICLE_PAGE.validate_license_state_edit_popup() == VD.license_state
    VEHICLE_PAGE.validate_dvir_edit_popup() == VD.dvir
    VEHICLE_PAGE.validate_license_plate_popup() == VD.license_plate

@when('user provide the vehicle name to search')
def provide_search_text():
    LOCATION_PAGE.set_search_text(VD.updated_vehicle_name)

@then('validate result table should be filtered based on searched text')
def validate_search_on_location_page():
    assert LOCATION_PAGE.validate_search_result_count() == 1
    assert LOCATION_PAGE.validate_search_result_name(VD.updated_vehicle_name)
    LOCATION_PAGE.clear_filters()

@when('user download the vehicle template')
def download_vehicle_template():
    global FILE_NAME
    FILE_NAME = VEHICLE_PAGE.download_vehicle_template()

@then('validate the downloaded vehicle template')
def validate_vehicle_template():
    assert LOCATION_PAGE.validate_file_header(FILE_NAME) == get_vehicle_headers()

@when('user upload vehicle template')
def upload_vehicle_template():
    global VEHICLE_COUNT
    vehicle_headers = get_vehicle_headers()
    VEHICLE_COUNT = 2
    VEHICLE_PAGE.create_vehicles_in_template(FILE_NAME, vehicle_headers, VD.random_vin, VD.vehicle_data, VEHICLE_COUNT)
    VEHICLE_PAGE.upload_template(FILE_NAME)

@when('user download vehicle records')
def download_location_template():
    global FILE_NAME
    FILE_NAME = LOCATION_PAGE.download_records()

@then('validate the downloaded vehicle records')
def validate_location_template():
    assert LOCATION_PAGE.validate_file_header(FILE_NAME) == [
        "Group",
        "Vehicle Name",
        "VIN",
        "License State",
        "License Plate",
        "Diagnostic Port Occupied",
        "DVIR",
        "Location Name",
        "Date Added",
        "Model",
        "Quote #",
        "Install Status"]

@then('validate vehicles should be imported')
def validate_vehicle_imported():
    assert LOCATION_PAGE.validate_success_notify_icon() == 'check_circle'
    assert LOCATION_PAGE.validate_success_notify_msg() == 'Success - '+str(VEHICLE_COUNT)+' out of '+str(VEHICLE_COUNT)+' Vehicles imported successfully.'
    assert LOCATION_PAGE.validate_success_notify_cross_icon() == 'close'

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