import datetime
from time import sleep, strptime

from hamcrest import assert_that, contains_string
from pytest_bdd import scenarios, given, when, then

from pages.fleet_maint_page import FleetMaintPage
from pages.login_page import LoginPage
from steps.common import FLEET_URL, ENV
from data.int.fleet_maint_data_int import FleetMaintDataInt as FMD_INT
from data.prod.fleet_maint_data_prod import FleetMaintDataProd as FMD_PROD
from data.stg.fleet_maint_data_stg import FleetMaintDataStg as FMD_STG

LOGIN_PAGE = 0
FLEET_MAINT_PAGE = 0
FMD = 0

scenarios('../features/fleet_maint.feature')


# LQ-511
@given('fleet dispatcher logs in')
def launch_browser_and_login(browser):
    global LOGIN_PAGE, FLEET_MAINT_PAGE, FMD

    LOGIN_PAGE = LoginPage(browser)
    FLEET_MAINT_PAGE = FleetMaintPage(browser)

    browser.get(FLEET_URL)

    if ENV == 'int':
        FMD = FMD_INT
    elif ENV == 'stg':
        FMD = FMD_STG
    else:
        FMD = FMD_PROD

    LOGIN_PAGE.enter_username(FMD.user_name)
    LOGIN_PAGE.enter_password(FMD.password)

    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed(FLEET_URL, FMD.user_name, FMD.password)


@when('the user navigates to Maintenance -> Preventative Maintenance')
def go_to_fleet_maint_pm():
    FLEET_MAINT_PAGE.click_maintenance()
    FLEET_MAINT_PAGE.click_preventative_maintenance()


@then('the Preventative Main labels are shown - Upcoming Services, History & Manage Services')
def assert_preventative_maintenance():
    assert FLEET_MAINT_PAGE.get_preventative_maintenance_title() == "PREVENTATIVE MAINTENANCE"
    assert FLEET_MAINT_PAGE.get_upcoming_services_tab_title() == "Upcoming Services"
    assert FLEET_MAINT_PAGE.get_history_tab_title() == "History"
    assert FLEET_MAINT_PAGE.get_manage_services_title() == "Manage Services"

    # clear service history dirty data if any
    FLEET_MAINT_PAGE.click_history_tab()
    count = int(FLEET_MAINT_PAGE.get_pm_history_service_count())

    for i in range(count):
        if i == count - 1:
            FLEET_MAINT_PAGE.click_pm_history_1st_only_edit()
        else:
            FLEET_MAINT_PAGE.click_pm_history_1st_edit()

        FLEET_MAINT_PAGE.click_date_selector_pm_history_edit_service()
        FLEET_MAINT_PAGE.set_months_ago_history_edit_service(10)
        FLEET_MAINT_PAGE.select_1st_day_pm_history_edit_service()
        FLEET_MAINT_PAGE.click_save_pm_history_edit_service()


# LQ-527
@when('the user clicks "Manage Services"')
def click_manage_services_tab():
    FLEET_MAINT_PAGE.click_manage_services()
    # sleep 2s to load services
    sleep(3)


@then('the Manage Services page is displayed')
def assert_manage_services_page():
    assert FLEET_MAINT_PAGE.get_manage_services_title() == "Manage Services"


# LQ-528
@when('the user clicks the "Create Service" button')
def create_maint_service():
    if FLEET_MAINT_PAGE.newly_created_service_is_displayed() is True:
        FLEET_MAINT_PAGE.click_service_name()
        FLEET_MAINT_PAGE.click_delete_service()
        FLEET_MAINT_PAGE.click_confirm_delete_service()
    if FLEET_MAINT_PAGE.updated_service_list_service_name_is_displayed() is True:
        FLEET_MAINT_PAGE.click_newly_created_service_name()
        FLEET_MAINT_PAGE.click_delete_service()
        FLEET_MAINT_PAGE.click_confirm_delete_service()
    FLEET_MAINT_PAGE.click_create_service()


@when('the user enter some characters in the "SERVICE NAME", "SERVICE INTERVAL (MI)", "DUE SOON THRESHOLD (MI)" field')
def set_service_parameters():
    FLEET_MAINT_PAGE.set_service_parameters("000__A", "1000", "800")
    sleep(4)


@when('the user clicks the save button')
def save_maint_service():
    FLEET_MAINT_PAGE.click_save_service()


@then('the service is created')
def assert_service_is_created():
    assert FLEET_MAINT_PAGE.get_manage_service_name() == '000__A'


# LQ-529
@when('the user clicks a service name')
def edit_service():
    FLEET_MAINT_PAGE.click_service_name()


@when('the user enters some characters in the "SERVICE NAME" field')
def change_service_name():
    FLEET_MAINT_PAGE.update_service_parameters("000___A", "8", "2")
    FLEET_MAINT_PAGE.add_vehicle_to_pm_service()


# When step of LQ-529 is the same with LQ-528

@then('the service is edited')
def assert_service_is_updated():
    assert FLEET_MAINT_PAGE.get_updated_service_name() == "000___A"


# LQ-516
@given('the "Fleet Dispatcher" user is in Fleet Tracking - MAINT. - PREVENTATIVE MAINTENANCE - Upcoming Service page')
def go_to_upcoming_service_page():
    FLEET_MAINT_PAGE.go_to_upcoming_service()


@when(
    'the user enters some characters into search vehicles box and the user selects a vehicle in the search vehicles box')
def filter_by_vehicle_service_due():
    FLEET_MAINT_PAGE.search_vehicle_upcoming_service(FMD.vehicle)
    FLEET_MAINT_PAGE.select_vehicle_upcoming_service(FMD.vehicle)


@then('the data with selected vehicles are displayed on the table')
def assert_filter_by_vehicle_service_due():
    assert FLEET_MAINT_PAGE.get_pm_upcoming_service_count_is_displayed()
    assert_that(FLEET_MAINT_PAGE.get_pm_upcoming_service_1st_vehicle(), contains_string(FMD.vehicle))
    assert_that(FLEET_MAINT_PAGE.get_pm_upcoming_service_1st_group(), contains_string(FMD.group))
    FLEET_MAINT_PAGE.get_newly_created_service_in_pm_upcoming_service_list() == ' 000___A '
    assert FLEET_MAINT_PAGE.get_pm_upcoming_service_1st_status(FMD.status) == FMD.status
    assert FLEET_MAINT_PAGE.get_pm_upcoming_service_1st_action() == 'Complete'


# LQ-521
@when(
    'the user clicks "Complete" hyperlink and the user selects a date and the user selects a time and the users click '
    'the "Complete" button')
def complete_an_upcoming_service():
    FLEET_MAINT_PAGE.click_pm_upcoming_service_1st_action()
    FLEET_MAINT_PAGE.click_pm_complete_service_dialog_complete()


@then('the service of the vehicle is completed and the interval of the service is reset')
def assert_completed_service():
    FLEET_MAINT_PAGE.click_history_tab()

    date_serviced = FLEET_MAINT_PAGE.get_pm_history_1st_date_serviced()
    date_serviced_time = strptime(date_serviced, "%b %d, %Y")
    today = strptime(str(datetime.datetime.now()).split(' ')[0], "%Y-%m-%d")
    yesterday = strptime(str(datetime.datetime.now() + datetime.timedelta(days=-1)).split(' ')[0], "%Y-%m-%d")

    assert_that(FLEET_MAINT_PAGE.get_pm_history_1st_vehicle(), contains_string(FMD.vehicle))
    assert_that(FLEET_MAINT_PAGE.get_pm_history_1st_group(), contains_string(FMD.group))
    assert FLEET_MAINT_PAGE.get_pm_history_1st_service() == '000___A'
    assert FLEET_MAINT_PAGE.get_pm_history_1st_interval() == '8mi'
    assert date_serviced_time <= today
    assert date_serviced_time >= yesterday
    # assert FLEET_MAINT_PAGE.get_pm_history_1st_odometer() == FMD.odometer
    # assert FLEET_MAINT_PAGE.get_pm_history_1st_engine_hours() == '0'
    # assert FLEET_MAINT_PAGE.get_pm_history_1st_notes() == ''


# LQ-522
@when('the user clicks "History"')
def click_history_tab():
    FLEET_MAINT_PAGE.click_history_tab()


@then(
    'the table is displayed with columns: "VEHICLE", "GROUP", "SERVICE", "INTERVAL", "DATE SERVICED", "ODOMETER", "ENGINE HOURS", "NOTES", "ACTION" & the number of Services is displayed')
def assert_history_page():
    assert FLEET_MAINT_PAGE.get_vehicle_preventative_maintenance() == "VEHICLE"
    assert FLEET_MAINT_PAGE.get_group_preventative_maintenance() == "GROUP"
    assert FLEET_MAINT_PAGE.get_service_preventative_maintenance() == "SERVICE"
    assert FLEET_MAINT_PAGE.get_interval_preventative_maintenance() == "INTERVAL"
    assert FLEET_MAINT_PAGE.get_date_serviced_preventative_maintenance() == "DATE SERVICED"
    assert FLEET_MAINT_PAGE.get_odometer_preventative_maintenance() == "ODOMETER"
    assert FLEET_MAINT_PAGE.get_engine_hours_preventative_maintenance() == "ENGINE HOURS"
    assert FLEET_MAINT_PAGE.get_notes_preventative_maintenance() == "NOTES"
    assert FLEET_MAINT_PAGE.get_action_preventative_maintenance() == "ACTION"
    assert FLEET_MAINT_PAGE.get_total_page_count() == FLEET_MAINT_PAGE.get_pm_history_service_count()


# LQ-524
@when('the user sets date filter in PM Service History page')
def date_filter_history_preventative_maintenance():
    FLEET_MAINT_PAGE.click_date_filter_history()
    FLEET_MAINT_PAGE.select_last_60_days_history()
    FLEET_MAINT_PAGE.click_apply_button_history()


@then('the data with selected filters are displayed on the table')
def assert_date_filter_history_preventative_maintenance():
    assert FLEET_MAINT_PAGE.get_total_page_count() == FLEET_MAINT_PAGE.get_pm_history_service_count()


# LQ-526
@when(
    'the user clicks "Edit" hyperlink and the user selects a date and the user selects a time and the users click the "Save" button')
def edit_service_history():
    FLEET_MAINT_PAGE.click_pm_history_1st_edit()
    FLEET_MAINT_PAGE.set_hour_pm_history_edit_service('02')
    FLEET_MAINT_PAGE.set_minute_pm_history_edit_service('02')
    FLEET_MAINT_PAGE.set_period_pm_history_edit_service('PM')
    FLEET_MAINT_PAGE.click_date_selector_pm_history_edit_service()
    FLEET_MAINT_PAGE.select_1st_day_pm_history_edit_service()
    FLEET_MAINT_PAGE.click_save_pm_history_edit_service()


@then('the service of the vehicle is edited')
def edit_history_page_edit_result():
    FLEET_MAINT_PAGE.click_pm_history_1st_edit()
    FLEET_MAINT_PAGE.open_time_selector_pm_history_edit_service()
    time = FLEET_MAINT_PAGE.get_time_pm_history_edit_service()
    assert time[0] == '02'
    assert time[1] == '02'
    assert time[2] == 'PM'

    # update service history data for next run
    FLEET_MAINT_PAGE.click_date_selector_pm_history_edit_service()
    FLEET_MAINT_PAGE.set_months_ago_history_edit_service(10)
    FLEET_MAINT_PAGE.select_1st_day_pm_history_edit_service()
    FLEET_MAINT_PAGE.click_save_pm_history_edit_service()

    # delete the added service for next run
    FLEET_MAINT_PAGE.click_manage_services()
    FLEET_MAINT_PAGE.click_newly_created_service_name()
    FLEET_MAINT_PAGE.click_delete_service()
    FLEET_MAINT_PAGE.click_confirm_delete_service()

# LQ-531
@when('the user navigates to Maintenance -> Diagnostic Trouble Codes')
def click_dtc():
    FLEET_MAINT_PAGE.click_maintenance()
    FLEET_MAINT_PAGE.click_dtc()


@then(
    'the DTC page is displayed and the number of Codes, group filter and reset icon are displayed on the header bar and the table is displayed with columns: "VEHICLE", "GROUP", "DATE", "CODE (DESCRIPTION)"')
def assert_dtc():
    assert FLEET_MAINT_PAGE.get_dtc_title() == "DIAGNOSTIC TROUBLE CODES"
    assert FLEET_MAINT_PAGE.dtc_count_is_displayed() is True
    assert FLEET_MAINT_PAGE.group_filter_displayed_dtc_page() is True
    assert FLEET_MAINT_PAGE.get_vehicle_column_text_dtc_page() == "VEHICLE"
    assert FLEET_MAINT_PAGE.get_group_column_text_dtc_page() == "GROUP"
    assert FLEET_MAINT_PAGE.get_date_column_text_dtc_page() == "DATE"
    assert FLEET_MAINT_PAGE.get_code_column_text_dtc_page() == "CODE (DESCRIPTION)"


# LQ-532
@when('the user selects a group in the group filter in Diagnostic Trouble Codes page')
def filter_group_dtc_page():
    FLEET_MAINT_PAGE.click_group_filter_dtc_page()
    FLEET_MAINT_PAGE.search_by_group_dtc_page(FMD.group)
    FLEET_MAINT_PAGE.select_search_group_dct_page()
    FLEET_MAINT_PAGE.click_done_button_dtc_page()


@then('the data with selected group are displayed on the table in dtc page')
def assert_group_filter_dtc():
    assert FLEET_MAINT_PAGE.get_row_count() == 0
