from time import sleep
from pytest_bdd import scenarios, given, when, then
from pages.add_vehicle_page import *
from pages.dashboard_page import DashboardPage
from pages.device_health_page import DeviceHealthPage
from pages.driver_id_assignment_page import DriverIdAssignmentPage
from pages.driver_id_page import DriverIdPage
from pages.edit_vehicle_page import EditVehiclePage
from pages.license_management_page import LicenseManagementPage
from pages.configuration_setting_page import ConfigurationSettingPage
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage
from pages.vehicle_management_page import VehicleManagementPage
from pages.geofence_management_page import GeofenceManagementPage
from pages.device_management_page import DeviceManagementPage
from pages.device_profile_page import DeviceProfilePage
from pages.add_user_page import AddUserPage
from pages.trailer_management_page import TrailerManagementPage
from pages.edit_trailer_page import EditTrailerPage
from pages.add_trailer_page import AddTrailerPage
from steps.common import DC_URL, ENV
from data.prod.admin_data_prod import AdminDataProd as AD_PROD
from data.stg.admin_data_stg import AdminDataStg as AD_STG
from data.int.admin_data_int import AdminDataInt as AD_INT

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
LICENSE_MANAGEMENT_PAGE = 0
USER_MANAGEMENT_PAGE = 0
VEHICLE_MANAGEMENT_PAGE = 0
ADD_VEHICLE_PAGE = 0
EDIT_VEHICLE_PAGE = 0
MY_ACCOUNT_PAGE = 0
DEVICE_HEALTH_PAGE = 0
DRIVER_ID_ASSIGNMENT_PAGE = 0
DRIVER_ID_PAGE = 0
CONFIGURATION_SETTING_PAGE = 0
GEOFENCE_MANAGEMENT_PAGE = 0
DEVICE_MANAGEMENT_PAGE = 0
DEVICE_PROFILE_PAGE = 0
TRAILER_MANAGEMENT_PAGE = 0
ADD_TRAILER_PAGE = 0
ADD_USER_PAGE = 0
EDIT_TRAILER_PAGE = 0
AD = 0

scenarios('../features/admin_license_geofence.feature')


# LQ-153
@given('fa user logs in')
def fa_log_in(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, LICENSE_MANAGEMENT_PAGE, USER_MANAGEMENT_PAGE, VEHICLE_MANAGEMENT_PAGE, ADD_VEHICLE_PAGE, EDIT_VEHICLE_PAGE, MY_ACCOUNT_PAGE, DEVICE_HEALTH_PAGE, DRIVER_ID_ASSIGNMENT_PAGE, DRIVER_ID_PAGE, CONFIGURATION_SETTING_PAGE, GEOFENCE_MANAGEMENT_PAGE, DEVICE_MANAGEMENT_PAGE, DEVICE_PROFILE_PAGE, TRAILER_MANAGEMENT_PAGE, AD, ADD_TRAILER_PAGE, EDIT_TRAILER_PAGE, ADD_USER_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    LICENSE_MANAGEMENT_PAGE = LicenseManagementPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)
    VEHICLE_MANAGEMENT_PAGE = VehicleManagementPage(browser)
    ADD_VEHICLE_PAGE = AddVehiclePage(browser)
    EDIT_VEHICLE_PAGE = EditVehiclePage(browser)
    DRIVER_ID_ASSIGNMENT_PAGE = DriverIdAssignmentPage(browser)
    DEVICE_HEALTH_PAGE = DeviceHealthPage(browser)
    DRIVER_ID_PAGE = DriverIdPage(browser)
    CONFIGURATION_SETTING_PAGE = ConfigurationSettingPage(browser)
    GEOFENCE_MANAGEMENT_PAGE = GeofenceManagementPage(browser)
    DEVICE_PROFILE_PAGE = DeviceProfilePage(browser)
    DEVICE_MANAGEMENT_PAGE = DeviceManagementPage(browser)
    TRAILER_MANAGEMENT_PAGE = TrailerManagementPage(browser)
    ADD_TRAILER_PAGE = AddTrailerPage(browser)
    ADD_USER_PAGE = AddUserPage(browser)
    EDIT_TRAILER_PAGE = EditTrailerPage(browser)

    browser.get(DC_URL)

    if ENV == 'int':
        AD = AD_INT
    elif ENV == 'stg':
        AD = AD_STG
    else:
        AD = AD_PROD

    LOGIN_PAGE.enter_username(AD.pm_fa_user_name)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed_new_ui(DC_URL, AD.pm_fa_user_name, AD.password, AD.company_name)


# LQ-3557
@when('the user clicks "GEOFENCES"')
def navigate_to_geofences():
    # we can delete after license tests are uncomment.
    DASHBOARD_PAGE.click_admin_tab()
    USER_MANAGEMENT_PAGE.click_geofences_tab()


@then(
    'the page header "GEOFENCE MANAGEMENT" and geofence count are displayed and the table is displayed with columns: "GEOFENCE", "GROUP", "RECENT ACTIVITY", "STATUS", "ASSETS", "TRIGGER TYPE", "CREATED DATE", "SOURCE"')
def verify_geofence_page():
    assert GEOFENCE_MANAGEMENT_PAGE.get_geofence_page_title() == "GEOFENCE MANAGEMENT"
    assert GEOFENCE_MANAGEMENT_PAGE.get_geofence_count() == "1"
    assert GEOFENCE_MANAGEMENT_PAGE.get_row_count(10) == 1
    assert GEOFENCE_MANAGEMENT_PAGE.get_geofence_column_text() == "GEOFENCE"
    assert GEOFENCE_MANAGEMENT_PAGE.get_group_column_text() == "GROUP"
    assert GEOFENCE_MANAGEMENT_PAGE.get_recent_activity_column_text() == "RECENT ACTIVITY"
    assert GEOFENCE_MANAGEMENT_PAGE.get_status_column_text() == "STATUS"
    assert GEOFENCE_MANAGEMENT_PAGE.get_assets_column_text() == "ASSETS"
    assert GEOFENCE_MANAGEMENT_PAGE.get_trigger_type_column_text() == "TRIGGER TYPE"
    assert GEOFENCE_MANAGEMENT_PAGE.get_created_date_column_text() == "CREATED DATE"
    assert GEOFENCE_MANAGEMENT_PAGE.get_source_column_text() == "SOURCE"


# LQ-3558
@when('the user sets group filter to one group in Geofences page')
def set_group_filter():
    GEOFENCE_MANAGEMENT_PAGE.click_group_filter()
    GEOFENCE_MANAGEMENT_PAGE.search_group(AD.group)
    GEOFENCE_MANAGEMENT_PAGE.select_searched_group()
    GEOFENCE_MANAGEMENT_PAGE.click_done_button()


@then('the data with selected group are displayed on the table')
def verify_group_filter():
    assert GEOFENCE_MANAGEMENT_PAGE.get_group_name_text() == AD.group
    GEOFENCE_MANAGEMENT_PAGE.click_reset_button()


@when('the user sets date filter of "Recent Activity" in Geofences page')
def set_recent_activity_filter():
    GEOFENCE_MANAGEMENT_PAGE.click_recent_activity_filter()
    GEOFENCE_MANAGEMENT_PAGE.select_last_7_days_recent_activity()
    GEOFENCE_MANAGEMENT_PAGE.click_apply_button_recent_activity()


@then('the data with selected recent activity are displayed on the table')
def verify_recent_activity_filter():
    assert GEOFENCE_MANAGEMENT_PAGE.get_row_count(10) == 0
    GEOFENCE_MANAGEMENT_PAGE.click_reset_button()


@when('the user sets status filter to active status in Geofences page')
def set_status_filter_geofence_page():
    GEOFENCE_MANAGEMENT_PAGE.click_status_filter()
    GEOFENCE_MANAGEMENT_PAGE.select_active_status()


@then('the data with selected status are displayed on the table')
def verify_status_filter():
    assert GEOFENCE_MANAGEMENT_PAGE.get_row_count(10) == 1
    GEOFENCE_MANAGEMENT_PAGE.click_reset_button()


@when('the user sets date filter of "Creation Date" in Geofences page')
def set_created_date_filter():
    GEOFENCE_MANAGEMENT_PAGE.click_created_date_filter()
    GEOFENCE_MANAGEMENT_PAGE.set_geofence_created_date_range(AD.geofence_created_start_day,
                                                             AD.geofence_created_start_month,
                                                             AD.geofence_created_start_year,
                                                             AD.geofence_created_end_day,
                                                             AD.geofence_created_end_month,
                                                             AD.geofence_created_end_year)
    GEOFENCE_MANAGEMENT_PAGE.click_apply_button_created_date()


@then('the data with selected created date are displayed on the table')
def verify_created_date_filter():
    assert GEOFENCE_MANAGEMENT_PAGE.geofence_count_displayed() is True
    GEOFENCE_MANAGEMENT_PAGE.click_reset_button()


@when('the user enters search criteria in "Search Geofence" in Geofences page')
def search_geofence():
    GEOFENCE_MANAGEMENT_PAGE.search_geofence_name(AD.geofence)


@then('the data match the search criteria are displayed on the table')
def verify_search_geofence_name():
    sleep(2)
    # assert GEOFENCE_MANAGEMENT_PAGE.get_row_count(10) == 1
    assert GEOFENCE_MANAGEMENT_PAGE.geofence_count_displayed() is True
    GEOFENCE_MANAGEMENT_PAGE.click_reset_button()


# LQ-3565
@when('the user clicks "Import" and the user clicks "Geofence Excel Template"')
def download_geofence_excel_template():
    GEOFENCE_MANAGEMENT_PAGE.click_import_geofence_management()
    GEOFENCE_MANAGEMENT_PAGE.download_template_geofence_management()


@then('the ImportGeofence template is downloaded')
def verify_import_geofence_template_downloaded():
    GEOFENCE_MANAGEMENT_PAGE.wait_for_file_downloaded('ImportGeofence.xlsx')
    assert GEOFENCE_MANAGEMENT_PAGE.check_file_exist('ImportGeofence.xlsx') is True
