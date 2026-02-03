from datetime import datetime
from time import sleep

from hamcrest import assert_that, contains_string
from pytest_bdd import scenarios, given, when, then, parsers
from pages.add_vehicle_page import *
from pages.device_profile_page import DeviceProfilePage
from pages.dashboard_page import DashboardPage
from pages.edit_vehicle_page import EditVehiclePage
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage
from pages.vehicle_management_page import VehicleManagementPage
from pages.device_management_page import DeviceManagementPage
from pages.add_user_page import AddUserPage
from steps.common import DC_URL, ENV
from data.prod.home_data_prod import HomeDataProd as HD_PROD
from data.int.home_data_int import HomeDataInt as HD_INT
from data.stg.home_data_stg import HomeDataStg as HD_STG

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
USER_MANAGEMENT_PAGE = 0
VEHICLE_MANAGEMENT_PAGE = 0
ADD_VEHICLE_PAGE = 0
EDIT_VEHICLE_PAGE = 0
DEVICE_MANAGEMENT_PAGE = 0
DEVICE_PROFILE_PAGE = 0
ADD_USER_PAGE = 0
AD = 0
scenarios('../features/device_status.feature')


# LQ-304
@given('Admin user logs in into Admin page')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, USER_MANAGEMENT_PAGE, VEHICLE_MANAGEMENT_PAGE, ADD_VEHICLE_PAGE, EDIT_VEHICLE_PAGE, DEVICE_MANAGEMENT_PAGE, AD, ADD_USER_PAGE, DEVICE_PROFILE_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)
    VEHICLE_MANAGEMENT_PAGE = VehicleManagementPage(browser)
    ADD_VEHICLE_PAGE = AddVehiclePage(browser)
    EDIT_VEHICLE_PAGE = EditVehiclePage(browser)
    DEVICE_MANAGEMENT_PAGE = DeviceManagementPage(browser)
    ADD_USER_PAGE = AddUserPage(browser)
    DEVICE_PROFILE_PAGE = DeviceProfilePage(browser)

    browser.get(DC_URL)

    if ENV == 'int':
        HD = HD_INT
    elif ENV == 'stg':
        HD = HD_STG
    else:
        HD = HD_PROD

    LOGIN_PAGE.enter_username(HD.fullaccess_1129)
    LOGIN_PAGE.enter_password(HD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed(DC_URL, HD.fullaccess_1129, HD.password)

    DASHBOARD_PAGE.click_admin_tab()


@when('user navigates to Device Management page')
def login():
    USER_MANAGEMENT_PAGE.click_devices_tab()


@then('Device Management Page is displayed')
def verify_login():
    assert DEVICE_MANAGEMENT_PAGE.get_device_management_title() == "DEVICE MANAGEMENT"


@when(parsers.parse('the user search for {device} and clicks the device'))
def search_and_click_device(device):
    USER_MANAGEMENT_PAGE.click_devices_tab()
    DEVICE_MANAGEMENT_PAGE.click_reset_button()
    DEVICE_MANAGEMENT_PAGE.click_select_search_filter()
    DEVICE_MANAGEMENT_PAGE.select_device_filter()
    DEVICE_MANAGEMENT_PAGE.search_device_filter(device)
    DEVICE_PROFILE_PAGE.click_device_serial_number()


@when(parsers.parse('user clicks the Request New image for {device}'))
def request_new_image():
    global last_updated_image
    DEVICE_PROFILE_PAGE.scroll_page_down()
    last_updated_image = DEVICE_PROFILE_PAGE.get_new_time_for_updated_image()
    DEVICE_PROFILE_PAGE.click_request_new_image()


@then('a new image should be displayed in the UI')
def verify_request_new_image():
    DEVICE_PROFILE_PAGE.wait_for_load_new_image()
    assert DEVICE_PROFILE_PAGE.get_new_time_for_updated_image() != last_updated_image
