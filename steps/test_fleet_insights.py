from time import sleep

from pytest_bdd import scenarios, when, then, given
from pages.dashboard_page import DashboardPage
from pages.equipment_management_page import EquipmentManagementPage
from pages.fleet_insights_page import FleetInsightEquipmentStatusAssetType as AssetType
from pages.fleet_insights_page import FleetInsightsPage
from pages.login_page import LoginPage
from steps.common import FLEET_URL, ENV, AutomationDataManager, TestDataEnum
from data.int.fleet_insights_data_int import FleetInsightsDataInt as FID_INT
from data.prod.fleet_insights_data_prod import FleetInsightsDataProd as FID_PROD
from data.stg.fleet_insights_data_stg import FleetInsightsDataStg as FID_STG
from steps.test_admin_consent_report import DASHBOARD_PAGE
from steps.test_admin_equipment_management import EQUIPMENT_MANAGEMENT_PAGE

LOGIN_PAGE = 0
FLEET_INSIGHT_PAGE = 0
FID = 0
DASHBOARD_PAGE = 0
EQUIPMENT_MANAGEMENT_PAGE = 0

equipment_count = 0
equipment_with_device_count = 0

scenarios('../features/fleet_insights.feature')


# LQ-544
@given('user logins to fleet page')
def login_to_fleet_page(browser):
    global LOGIN_PAGE, FLEET_INSIGHT_PAGE, FID, DASHBOARD_PAGE, EQUIPMENT_MANAGEMENT_PAGE

    LOGIN_PAGE = LoginPage(browser)
    FLEET_INSIGHT_PAGE = FleetInsightsPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    EQUIPMENT_MANAGEMENT_PAGE = EquipmentManagementPage(browser)

    browser.get(FLEET_URL)

    if ENV == 'int':
        FID = FID_INT
    elif ENV == 'stg':
        FID = FID_STG
    else:
        FID = FID_PROD


    LOGIN_PAGE.enter_username(FID.user_name)
    LOGIN_PAGE.enter_password(FID.password)

    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed(FLEET_URL, FID.user_name, FID.password)


@when('the user navigates to Insights -> Fleet Operations')
def go_to_fleet_operations():
    FLEET_INSIGHT_PAGE.click_insights()
    FLEET_INSIGHT_PAGE.click_fleet_operations()


@then('the groups tab of Fleet Operations page is displayed')
def assert_fleet_operations_groups_tab():
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_title() == "FLEET OPERATIONS"
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_groups_tab() == "Groups"


# LQ-543
@when('the user sets group filter to one group in Fleet Operations page Groups tab')
def driver_filter_group():
    FLEET_INSIGHT_PAGE.click_filter_group_group()
    FLEET_INSIGHT_PAGE.search_filter_group(FID.group)
    FLEET_INSIGHT_PAGE.select_group_from_search_filter_suggestion_list()
    FLEET_INSIGHT_PAGE.click_done()
    sleep(2)


@then('the data belong to the group are listed in Fleet Operations page Groups tab')
def assert_fleet_operations_group_filter_groups_tab():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == FID.fleet_operation_groups_tab_group_count

@when('the user sets date filter in Fleet Operations page Groups tab')
def filter_date_group():
    FLEET_INSIGHT_PAGE.select_date_filter_group()
    FLEET_INSIGHT_PAGE.set_fleet_operation_date_range(FID.fleet_operation_date_range_start_month_xpath,
                                                      FID.fleet_operation_date_range_start_day_xpath,
                                                      FID.fleet_operation_date_range_start_year_xpath,
                                                      FID.fleet_operation_date_range_end_month_xpath,
                                                      FID.fleet_operation_date_range_end_day_xpath,
                                                      FID.fleet_operation_date_range_end_year_xpath)
    FLEET_INSIGHT_PAGE.click_apply()
    sleep(2)


@then('the data belong to the date are listed in Fleet Operations page Groups tab')
def assert_fleet_operations_date_filter_groups_tab():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == FID.fleet_operation_groups_tab_date_filter_count
    FLEET_INSIGHT_PAGE.click_reset_driver_tab()

# LQ-549
@when('the user clicks Drivers in Fleet Operations page')
def click_fleet_operations_drivers():
    FLEET_INSIGHT_PAGE.click_fleet_operations_drivers()


@then('the drivers tab of Fleet Operations page is displayed')
def assert_fleet_operations_drivers_tab():
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_drivers_tab() == "Drivers"


# LQ-548
@when('the user sets group filter to one group in Fleet Operations page Drivers tab')
def driver_filter_group_drivers_tab():
    FLEET_INSIGHT_PAGE.click_filter_group_group()
    FLEET_INSIGHT_PAGE.search_filter_group(FID.group)
    FLEET_INSIGHT_PAGE.select_group_from_search_filter_suggestion_list()
    FLEET_INSIGHT_PAGE.click_done()
    sleep(2)


@then('the data belong to the group are listed in Fleet Operations page Drivers tab')
def assert_fleet_operations_group_filter_drivers_tab():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == FID.fleet_operation_drivers_tab_date_group_filter_count


@when('the user sets date filter in Fleet Operations page Drivers tab')
def filter_date_driver():
    FLEET_INSIGHT_PAGE.select_date_filter_group()
    FLEET_INSIGHT_PAGE.set_fleet_operation_date_range(FID.fleet_operation_date_range_start_month_xpath,
                                                      FID.fleet_operation_date_range_start_day_xpath,
                                                      FID.fleet_operation_date_range_start_year_xpath,
                                                      FID.fleet_operation_date_range_end_month_xpath,
                                                      FID.fleet_operation_date_range_end_day_xpath,
                                                      FID.fleet_operation_date_range_end_year_xpath)
    FLEET_INSIGHT_PAGE.click_apply()
    sleep(2)


@then('the data belong to the date are listed in Fleet Operations page Drivers tab')
def assert_fleet_operations_date_filter_drivers_tab():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == 1

    # FLEET_INSIGHT_PAGE.click_reset_driver_tab()


# LQ-2346
@when('the user clicks a driver name in the bottom table')
def go_to_driver_profile():
    FLEET_INSIGHT_PAGE.click_driver_name()


@then('the driver profile page is displayed')
def verify_driver_profile_page():
    assert FLEET_INSIGHT_PAGE.get_driver_profile_page_title() == 'DRIVER PROFILE'


# LQ-558
@when('the user clicks a driver name')
def click_driver_name():
    sleep(1)  # nothing to do there since it's already in driver profile page


@then(
    'the driver name is displayed and the metadata bar is displayed with labels: "EMPLOYEE ID", "GROUP", "VEHICLE NAME", "EMAIL"')
def verify_driver_profile_metadata():
    assert FLEET_INSIGHT_PAGE.get_employee_id_text_driver_profile() == "EMPLOYEE ID"
    assert FLEET_INSIGHT_PAGE.get_group_text_driver_profile() == "GROUP"
    assert FLEET_INSIGHT_PAGE.get_vehicle_name_text_driver_profile() == "VEHICLE NAME"
    assert FLEET_INSIGHT_PAGE.get_email_text_driver_profile() == "EMAIL"
    assert FLEET_INSIGHT_PAGE.get_driver_name_text_driver_profile() == FID.driver


@when('the user clicks the expand icon on the summary section')
def click_expand_icon_driver_profile():
    FLEET_INSIGHT_PAGE.click_expand_icon_driver_profile()


@then('view type buttons are displayed: "Daily Avg", "Total"')
def assert_view_type():
    assert FLEET_INSIGHT_PAGE.get_daily_avg_text_driver_profile() == "Daily Avg"
    assert FLEET_INSIGHT_PAGE.get_total_text_driver_profile() == "Total"


@then(
    'the summary section is displayed with labels: "ROUTE TIME", "DISTANCE", "TRIPS", "STOPS", "STOP TIME", "DRIVING TIME", "ENGINE HOURS", "IDLE VIOLATIONS", "IDLE DURATION", "SPEED VIOLATIONS", "SPEEDING DURATION" on driver profile page')
def assert_summary_section_driver_profile():
    assert FLEET_INSIGHT_PAGE.get_route_time_text_driver_profile() == "ROUTE TIME"
    assert FLEET_INSIGHT_PAGE.get_distance_text_driver_profile() == "DISTANCE"
    assert FLEET_INSIGHT_PAGE.get_trips_text_driver_profile() == "TRIPS"
    assert FLEET_INSIGHT_PAGE.get_stops_text_driver_profile() == "STOPS"
    assert FLEET_INSIGHT_PAGE.get_stop_time_text_driver_profile() == "STOP TIME"
    assert FLEET_INSIGHT_PAGE.get_driving_time_text_driver_profile() == "DRIVING TIME"
    assert FLEET_INSIGHT_PAGE.get_engine_hours_text_driver_profile() == "ENGINE HOURS"
    assert FLEET_INSIGHT_PAGE.get_idle_violations_text_driver_profile() == "IDLE VIOLATIONS"
    assert FLEET_INSIGHT_PAGE.get_idle_duration_text_driver_profile() == "IDLE DURATION"
    assert FLEET_INSIGHT_PAGE.get_speed_violation_text_driver_profile() == "SPEED VIOLATIONS"
    assert FLEET_INSIGHT_PAGE.get_speeding_duration_text_driver_profile() == "SPEEDING DURATION"


# LQ-559
@when('the user clicks a date and open the trip')
def open_trip_driver_profile():
    FLEET_INSIGHT_PAGE.click_date_filter_driver_profile()
    FLEET_INSIGHT_PAGE.set_driver_profile_date_range(FID.driver_profile_date_range_start_month,
                                                     FID.driver_profile_date_range_start_day,
                                                     FID.driver_profile_date_range_start_year,
                                                     FID.driver_profile_date_range_end_month,
                                                     FID.driver_profile_date_range_end_day,
                                                     FID.driver_profile_date_range_end_year)
    FLEET_INSIGHT_PAGE.click_apply_driver_profile()
    FLEET_INSIGHT_PAGE.click_trip_item_driver_profile_trip()


@then(
    'the first trip is displayed with labels: "Trip1", start time, start address, end time, end address, "VEHICLE", "TRIP DURATION", "DISTANCE", "MAX SPEED", "STOP DURATION"')
def asset_trip_driver_profile_trip():
    assert FLEET_INSIGHT_PAGE.get_trip1_text_driver_profile_trip() == "Trip 1"
    assert FLEET_INSIGHT_PAGE.start_time_displayed_driver_profile_trip() is True
    assert FLEET_INSIGHT_PAGE.start_address_driver_profile_trip() == FID.trip_start_address
    assert FLEET_INSIGHT_PAGE.end_time_displayed_driver_profile_trip() is True
    assert FLEET_INSIGHT_PAGE.end_address_driver_profile_trip() == FID.trip_end_address
    assert FLEET_INSIGHT_PAGE.get_vehicle_text_driver_profile_trip() == "VEHICLE"
    assert FLEET_INSIGHT_PAGE.get_trip_duration_text_driver_profile_trip() == "TRIP DURATION"
    assert FLEET_INSIGHT_PAGE.get_distance_text_driver_profile_trip() == "DISTANCE"
    assert FLEET_INSIGHT_PAGE.get_max_speed_text_driver_profile_trip() == "MAX SPEED"
    assert FLEET_INSIGHT_PAGE.get_stop_duration_text_driver_profile_trip() == "STOP DURATION"


# LQ-560
@when('the user clicks "Idles" and open the idle')
def open_idle_driver_profile_idle():
    FLEET_INSIGHT_PAGE.click_idle_tab_driver_profile()
    FLEET_INSIGHT_PAGE.click_idle_driver_profile_idle()


@then('the first idle is displayed with labels: "Idle1", start time, end time, address, "VEHICLE", "IDLE DURATION"')
def assert_idle_driver_profile_idle():
    assert FLEET_INSIGHT_PAGE.get_idle1_text_driver_profile_idle() == "Idle 1"
    assert FLEET_INSIGHT_PAGE.get_address_driver_profile_idle() == FID.address
    assert FLEET_INSIGHT_PAGE.time_displayed_driver_profile_idle() is True
    assert FLEET_INSIGHT_PAGE.get_vehicle_text_driver_profile_idle() == "VEHICLE"
    assert FLEET_INSIGHT_PAGE.get_idle_duration_text_driver_profile_idle() == "IDLE DURATION"


# LQ-557
@when('the user sets date filter in Driver Profile page')
def set_date_filer_driver_profile():
    FLEET_INSIGHT_PAGE.click_date_filter_driver_profile()
    FLEET_INSIGHT_PAGE.select_last_90_days_driver_profile()
    FLEET_INSIGHT_PAGE.click_apply_driver_profile()


@then('the data with selected filters are displayed on the idles in Driver Profile page')
def assert_date_filter_driver_profile_idle():
    assert FLEET_INSIGHT_PAGE.get_idle_count_driver_profile() == "Idles"


@then('the data with selected filters are displayed on the trips in Driver Profile page')
def assert_date_filter_driver_profile_trip():
    FLEET_INSIGHT_PAGE.click_trip_tab_driver_profile()
    assert FLEET_INSIGHT_PAGE.get_trip_count_driver_profile() == "Trips"


# LQ-547
@when('the user clicks Vehicles in Fleet Operations page')
def click_fleet_operations_vehicles():
    FLEET_INSIGHT_PAGE.click_insights()
    FLEET_INSIGHT_PAGE.click_fleet_operations()
    FLEET_INSIGHT_PAGE.click_fleet_operations_vehicles()


@then('the vehicles tab of Fleet Operations page is displayed')
def assert_fleet_operations_vehicles_tab():
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_vehicles_tab() == "Vehicles"


# LQ-546
@when('the user sets group filter to one group in Fleet Operations page Vehicles tab')
def driver_filter_group_vehicles_tab():
    FLEET_INSIGHT_PAGE.click_filter_group_group()
    FLEET_INSIGHT_PAGE.search_filter_group(FID.vehicle_group)
    FLEET_INSIGHT_PAGE.select_group_from_search_filter_suggestion_list()
    FLEET_INSIGHT_PAGE.click_done()
    sleep(2)


@then('the data belong to the group are listed in Fleet Operations page Vehicles tab')
def assert_fleet_operations_group_filter_vehicles_tab():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == 0


@when('the user sets date filter in Fleet Operations page Vehicles tab')
def filter_date_vehicle():
    FLEET_INSIGHT_PAGE.select_date_filter_group()
    FLEET_INSIGHT_PAGE.set_fleet_operation_date_range(FID.fleet_operation_date_range_start_month_xpath,
                                                      FID.fleet_operation_date_range_start_day_xpath,
                                                      FID.fleet_operation_date_range_start_year_xpath,
                                                      FID.fleet_operation_date_range_end_month_xpath,
                                                      FID.fleet_operation_date_range_end_day_xpath,
                                                      FID.fleet_operation_date_range_end_year_xpath)
    FLEET_INSIGHT_PAGE.click_apply()
    sleep(2)


@then('the data belong to the date are listed in Fleet Operations page Vehicles tab')
def assert_fleet_operations_date_filter_vehicles_tab():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == 0


# LQ-545
@when('the user inputs some characters in Search Vehicles box')
def search_vehicle_vehicle_profile():
    FLEET_INSIGHT_PAGE.search_vehicle_vehicle_profile(FID.vehicle)


@when('the user selects one vehicle')
def select_vehicle_vehicle_profile():
    sleep(2)  # sleep here to make sure the search result is loaded
    FLEET_INSIGHT_PAGE.select_vehicle_profile(FID.vehicle)


@then('the vehicle profile page is displayed')
def assert_fleet_operations_vehicle_profile():
    assert FLEET_INSIGHT_PAGE.get_fleet_operations_vehicle_profile() == "VEHICLE PROFILE"


# LQ-553
@when('the user clicks the expand icon on metadata bar')
def expand_driver_profile_metadata():
    FLEET_INSIGHT_PAGE.click_expand_metadata_icon()


@then('the metadata bar is displayed with labels: "VEHICLE NAME", "GROUP", "DRIVER", '
      '"DEVICE", "STATUS", "MAKE & MODEL", "LICENSE PLATE", "HIBERNATION SETTING", '
      '"VIN", "VEHICLE TYPE", "SEAT BELT TYPE"')
def assert_vehicle_profile_metadata():
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_vehicle_name() == "VEHICLE NAME"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_group() == "GROUP"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_driver() == "DRIVER"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_device() == "DEVICE"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_status() == "STATUS"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_make() == "MAKE & MODEL"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_license() == "LICENSE PLATE"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_hibernation() == "HIBERNATION SETTING"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_vin() == "VIN"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_vehicle_type() == "VEHICLE TYPE"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_seat_belt() == "SEAT BELT TYPE"


# LQ-552
@when('the user sets date filter in vehicle profile page')
def filter_date_vehicle_profile():
    FLEET_INSIGHT_PAGE.click_date_filter_vehicle_profile()
    FLEET_INSIGHT_PAGE.set_vehicle_profile_date_range(FID.vehicle_profile_date_range_start_month,
                                                      FID.vehicle_profile_date_range_start_day,
                                                      FID.vehicle_profile_date_range_start_year,
                                                      FID.vehicle_profile_date_range_end_month,
                                                      FID.vehicle_profile_date_range_end_day,
                                                      FID.vehicle_profile_date_range_end_year)
    FLEET_INSIGHT_PAGE.click_apply()
    sleep(2)


@then('the data with selected filters are displayed on the trips')
def assert_vehicle_profile_trip():
    sleep(3)
    assert FLEET_INSIGHT_PAGE.get_trip_count() == "Trips"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_route_time_value() == FID.vehicle_profile_route_time


@then('the data with selected filters are displayed on the idles')
def assert_vehicle_profile_idle():
    FLEET_INSIGHT_PAGE.click_idle_tab()
    assert FLEET_INSIGHT_PAGE.get_idle_count() == "Idles"


@then('the summary section is displayed with labels: "ROUTE TIME", "DISTANCE", '
      '"TRIPS", "STOPS", "STOP TIME", "DRIVING TIME", "ENGINE HOURS", "IDLE VIOLATIONS", '
      '"IDLE DURATION", "SPEED VIOLATIONS", "SPEEDING DURATION"')
def assert_vehicle_profile_summary():
    FLEET_INSIGHT_PAGE.click_expand_summary_icon()
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_route_time() == "ROUTE TIME"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_distance() == "DISTANCE"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_trips() == "TRIPS"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_stops() == "STOPS"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_stop_time() == "STOP TIME"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_driving_time() == "DRIVING TIME"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_engine_hours() == "ENGINE HOURS"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_idle_violation() == "IDLE VIOLATIONS"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_idle_duration() == "IDLE DURATION"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_speed_violation() == "SPEED VIOLATIONS"
    assert FLEET_INSIGHT_PAGE.get_vehicle_profile_speed_duration() == "SPEEDING DURATION"


# LQ-554
@when('the user clicks a date')
def click_date_trip():
    FLEET_INSIGHT_PAGE.click_trip_tab()
    FLEET_INSIGHT_PAGE.click_date_filter_vehicle_profile()
    FLEET_INSIGHT_PAGE.set_vehicle_profile_date_range(FID.vehicle_profile_date_range_start_month,
                                                      FID.vehicle_profile_date_range_start_day,
                                                      FID.vehicle_profile_date_range_start_year,
                                                      FID.vehicle_profile_date_range_end_month,
                                                      FID.vehicle_profile_date_range_end_day,
                                                      FID.vehicle_profile_date_range_end_year)
    FLEET_INSIGHT_PAGE.click_apply()
    FLEET_INSIGHT_PAGE.click_trip_vehicle_profile()


@then('the first trip is displayed with labels: "Trip1", start time, start address, end time, '
      'end address, "DRIVER", "TRIP DURATION", "DISTANCE", "MAX SPEED", "STOP DURATION"')
def assert_vehicle_profile_trip_detail():
    assert FLEET_INSIGHT_PAGE.get_trip_num_vehicle_profile() == 'Trip 1'
    assert FLEET_INSIGHT_PAGE.get_trip_driver_vehicle_profile() == 'DRIVER'
    assert FLEET_INSIGHT_PAGE.get_trip_duration_vehicle_profile() == 'TRIP DURATION'
    assert FLEET_INSIGHT_PAGE.get_trip_distance_vehicle_profile() == 'DISTANCE'
    assert FLEET_INSIGHT_PAGE.get_trip_speed_vehicle_profile() == 'MAX SPEED'
    assert FLEET_INSIGHT_PAGE.get_trip_stop_duration_vehicle_profile() == 'STOP DURATION'


# LQ-555
@when('the user clicks "Idles" and clicks a date')
def click_date_idle():
    FLEET_INSIGHT_PAGE.click_idle_tab()
    FLEET_INSIGHT_PAGE.click_date_filter_vehicle_profile()
    FLEET_INSIGHT_PAGE.set_vehicle_profile_date_range(FID.vehicle_profile_date_range_start_month,
                                                      FID.vehicle_profile_date_range_start_day,
                                                      FID.vehicle_profile_date_range_start_year,
                                                      FID.vehicle_profile_date_range_end_month,
                                                      FID.vehicle_profile_date_range_end_day,
                                                      FID.vehicle_profile_date_range_end_year)
    FLEET_INSIGHT_PAGE.click_apply()
    FLEET_INSIGHT_PAGE.click_idle_vehicle_profile()


@then(
    'the first idle is displayed with labels: "Idle1", "START TIME", "END TIME", "ADDRESS", "DRIVER", "IDLE DURATION"')
def assert_vehicle_profile_idle_detail():
    assert FLEET_INSIGHT_PAGE.get_idle_num_vehicle_profile() == 'Idle 1'
    assert FLEET_INSIGHT_PAGE.get_idle_driver_vehicle_profile() == 'DRIVER'
    assert FLEET_INSIGHT_PAGE.get_idle_duration_vehicle_profile() == 'IDLE DURATION'
    # assert FLEET_INSIGHT_PAGE.get_idle_detail_address() == "11500 Rancho Carmel Drive, San Diego, California 92128"
    # assert (FLEET_INSIGHT_PAGE.get_idle_detail_duration() - 33) <= 1


# LQ-7134
@when('the user clicks "INSIGHTS" and then clicks "EQUIPMENT STATUS"')
def click_equipment_status():
    FLEET_INSIGHT_PAGE.click_insights()
    FLEET_INSIGHT_PAGE.click_equipment_status()


@then(
    'the table is displayed with columns: "EQUIPMENT", "GROUP", "DEVICE SERIAL NUMBER", "LAST LOCATION", '
    '"LAST CONNECTED", "LAST MOVEMENT", "STATIONARY DURATION", "BATTERY LEVEL"')
def assert_insights_equipment_status():
    assert FLEET_INSIGHT_PAGE.get_equipment_status_title() == "EQUIPMENT STATUS"
    assert FLEET_INSIGHT_PAGE.get_equipment_text() == "EQUIPMENT"
    assert FLEET_INSIGHT_PAGE.get_equipment_group_text() == "GROUP"
    assert FLEET_INSIGHT_PAGE.get_equipment_device_text() == "DEVICE SERIAL #"
    assert FLEET_INSIGHT_PAGE.get_equipment_last_location_text() == "LAST LOCATION"
    assert FLEET_INSIGHT_PAGE.get_equipment_last_connected_text() == "LAST CONNECTED"
    assert FLEET_INSIGHT_PAGE.get_equipment_last_movement_text() == "LAST MOVEMENT"
    assert FLEET_INSIGHT_PAGE.get_equipment_stationary_text() == "STATIONARY DURATION"
    assert FLEET_INSIGHT_PAGE.get_equipment_battery_text() == "BATTERY LEVEL"
    assert FLEET_INSIGHT_PAGE.equipment_data_loaded() is True


# LQ-7135
@when('the user selects a group in the group filter in Equipment Status page')
def equipment_status_filter_by_group():
    FLEET_INSIGHT_PAGE.click_group_filter_equipment_status()
    FLEET_INSIGHT_PAGE.select_group_group_filter_equipment_status(FID.group)
    FLEET_INSIGHT_PAGE.select_search_group_equipment_status()
    FLEET_INSIGHT_PAGE.apply_group_filter_equipment_status()


@then('the data with selected group are displayed on the table in Equipment Status page')
def assert_insights_equipment_status_filter_by_group():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == FID.equipment_group_filter_row_count



@when('the user select Equipment and the user sets search criteria in Equipment Status page')
def equipment_status_filter_by_equipment():
    FLEET_INSIGHT_PAGE.click_search_assert_type_equipment_status()
    FLEET_INSIGHT_PAGE.select_select_search_item_equipment_status(AssetType.Equipment)
    FLEET_INSIGHT_PAGE.type_search_criteria_equipment_status("Equip")


@then('the data with select Equipment are displayed on the table in Equipment Status page')
def assert_insights_equipment_status_filter_by_equipment():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == 0


@when('the user navigates to Insights -> Equipment Status')
def go_to_equipment_status():
    FLEET_INSIGHT_PAGE.click_reset_button()


@then('the number of records is displayed in Equipment Status page')
def assert_equipment_status_record_count():
    global equipment_count
    equipment_count = FLEET_INSIGHT_PAGE.get_equipment_status_record_count()


@when('the user select Device and the user sets search criteria in Equipment Status page')
def equipment_status_filter_by_device():
    FLEET_INSIGHT_PAGE.click_search_assert_type_equipment_status()
    FLEET_INSIGHT_PAGE.select_select_search_item_equipment_status(AssetType.Device)
    FLEET_INSIGHT_PAGE.type_search_criteria_equipment_status("Device")


@then('the data with select Device are displayed on the table in Equipment Status page')
def assert_insights_equipment_status_filter_by_device():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == 0


# LQ-519
@when('the user navigates to Insights -> Geofences')
def click_geofences():
    FLEET_INSIGHT_PAGE.click_insights()
    FLEET_INSIGHT_PAGE.click_geofences()


@then('the Geofences page is displayed')
def assert_geofences():
    assert FLEET_INSIGHT_PAGE.get_geofences_title() == "GEOFENCES"


# LQ-520
@when('the user sets date filter in Geofences page')
def filter_date_geofences():
    FLEET_INSIGHT_PAGE.click_date_filter_geofences()
    FLEET_INSIGHT_PAGE.set_geofences_date_range(FID.geofences_date_range_start_month,
                                                FID.geofences_date_range_start_day,
                                                FID.geofences_date_range_start_year, FID.geofences_date_range_end_month,
                                                FID.geofences_date_range_end_day, FID.geofences_date_range_end_year)
    FLEET_INSIGHT_PAGE.click_apply_button_geofences()


@then('the data within selected date range are displayed in METRICS, TREND, table')
def assert_filter_date_geofences():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == FID.geofence_date_filter_row_count


@when('the user sets group filter to one group in Geofences page')
def filter_group_geofences():
    FLEET_INSIGHT_PAGE.click_group_filter_geofences()
    FLEET_INSIGHT_PAGE.search_group_geofences(FID.geofence_group)
    FLEET_INSIGHT_PAGE.select_group_geofences()
    FLEET_INSIGHT_PAGE.click_done_geofences()


@then('the data with selected group are displayed in METRICS, TREND, table')
def assert_filter_group_geofences():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == FID.geofence_group_filter_row_count


# LQ-562
@when('the user clicks a geofence or search and select a geofence to go to geofence profile page')
def go_to_geofence_profile():
    FLEET_INSIGHT_PAGE.search_geofence_geofences(FID.geofence)
    FLEET_INSIGHT_PAGE.select_1st_geofence_geofences(FID.geofence)


@then(
    'the metadata bar is displayed with labels: "GEOFENCE NAME", "DATE CREATED", "DAYS APPLIED", "RANGE OF TIME", "Trigger Type", "GROUP", "SUBGROUPS", "VEHICLES"')
def assert_metadata_bar_geofence_profile():
    assert FLEET_INSIGHT_PAGE.get_geofence_profile_metadata_name() == "GEOFENCE NAME"
    assert FLEET_INSIGHT_PAGE.geofence_profile_metadata_date_created() == "DATE CREATED"
    assert FLEET_INSIGHT_PAGE.geofence_profile_metadata_days_applied() == "DAYS APPLIED"
    assert FLEET_INSIGHT_PAGE.geofence_profile_metadata_time() == "RANGE OF TIME"
    assert FLEET_INSIGHT_PAGE.geofence_profile_metadata_type() == "Trigger Type"
    assert FLEET_INSIGHT_PAGE.geofence_profile_metadata_group() == "GROUP"
    assert FLEET_INSIGHT_PAGE.geofence_profile_metadata_subgroup() == "SUBGROUPS"
    assert FLEET_INSIGHT_PAGE.geofence_profile_metadata_vehicles() == "VEHICLES"


@when('the user search and select a geofence in geofence profile page')
def search_geofence_in_geofence_profile():
    FLEET_INSIGHT_PAGE.search_geofence_geofence_profile(FID.geofence)
    FLEET_INSIGHT_PAGE.select_1st_geofence_geofence_profile(FID.geofence)
    FLEET_INSIGHT_PAGE.click_geofence_profile_date_picker()
    FLEET_INSIGHT_PAGE.set_geofence_profile_date_range(FID.geofence_profile_date_range_start_month,
                                                       FID.geofence_profile_date_range_start_day,
                                                       FID.geofence_profile_date_range_start_year,
                                                       FID.geofence_profile_date_range_end_month,
                                                       FID.geofence_profile_date_range_end_day,
                                                       FID.geofence_profile_date_range_end_year)
    FLEET_INSIGHT_PAGE.click_apply_button()


@then(
    'the date picker selector is displayed and the vehicle is displayed below the summary section and the Vehicle Name, Start Point Date/Time, duration are displayed')
def assert_date_picker_and_details_geofence_profile():
    assert FLEET_INSIGHT_PAGE.geofence_profile_summary_date_picker_is_displayed() is True



@then(
    'the summary section is displayed with labels: "TOTAL TRIGGERS", "TOTAL DURATION", "TOTAL VEHICLES", "DRIVING TIME IN GEOFENCES", "IDLE TIME IN GEOFENCES", "STOP TIME IN GEOFENCES"')
def assert_summary_section_geofence_profile():
    assert FLEET_INSIGHT_PAGE.geofence_profile_summary_total_trigger() == "TOTAL TRIGGERS"
    assert FLEET_INSIGHT_PAGE.geofence_profile_summary_total_duration() == "TOTAL DURATION"
    assert FLEET_INSIGHT_PAGE.geofence_profile_summary_total_vehicle() == "TOTAL VEHICLES"
    assert FLEET_INSIGHT_PAGE.geofence_profile_summary_driving_time() == "DRIVING TIME IN GEOFENCES"
    assert FLEET_INSIGHT_PAGE.geofence_profile_summary_idle_time() == "IDLE TIME IN GEOFENCES"
    assert FLEET_INSIGHT_PAGE.geofence_profile_summary_stop_time() == "STOP TIME IN GEOFENCES"


# LQ-563
@when('the user clicks a vehicle')
def click_vehicle_trigger_section_geofence_profile():
    FLEET_INSIGHT_PAGE.click_geofence_profile_trigger_vehicle()


@then(
    'the trigger is displayed with labels: "Trigger Start", Start Point Date/Time, Start Point Address, "Trigger End", End Point Date/Time, End Point Address, "DRIVER", "TRIGGER TYPE", "DRIVING TIME", "STOP TIME", "IDLE TIME", "DURATION" and the selected trigger is displayed on the map')
def assert_trigger_section_geofence_profile():
    assert FLEET_INSIGHT_PAGE.geofence_profile_trigger_trigger_start() == "Trigger Start"
    assert FLEET_INSIGHT_PAGE.geofence_profile_trigger_trigger_end() == "Trigger End"
    assert FLEET_INSIGHT_PAGE.geofence_profile_trigger_driver() == "DRIVER"
    assert FLEET_INSIGHT_PAGE.geofence_profile_trigger_trigger_type() == "TRIGGER TYPE"
    assert FLEET_INSIGHT_PAGE.geofence_profile_trigger_driving_time() == "DRIVING TIME"
    assert FLEET_INSIGHT_PAGE.geofence_profile_trigger_stop_time() == "STOP TIME"
    assert FLEET_INSIGHT_PAGE.geofence_profile_trigger_idle_time() == "IDLE TIME"
    assert FLEET_INSIGHT_PAGE.geofence_profile_trigger_duration() == "DURATION"
    # assert FLEET_INSIGHT_PAGE.geofence_profile_trigger_geofence_pin_is_displayed() is True

# LQ-561
@when('the user sets date filter in geofence profile page')
def set_filter_geofence_profile():
    FLEET_INSIGHT_PAGE.click_date_filter_geofence_profile()
    FLEET_INSIGHT_PAGE.set_geofence_profile_date_range(FID.geofence_profile_date_range_start_month,
                                                       FID.geofence_profile_date_range_start_day,
                                                       FID.geofence_profile_date_range_start_year,
                                                       FID.geofence_profile_date_range_end_month,
                                                       FID.geofence_profile_date_range_end_day,
                                                       FID.geofence_profile_date_range_end_year)
    FLEET_INSIGHT_PAGE.click_apply_button()


@then(
    'the data with selected filters are displayed on the summary section and the data with selected filters are displayed on the triggers')
def assert_filter_geofence_profile():
    assert FLEET_INSIGHT_PAGE.geofence_profile_summary_total_trigger_count() == FID.triggers_count
    assert FLEET_INSIGHT_PAGE.geofence_profile_summary_total_vehicle_count() == FID.vehicle_count
    assert FLEET_INSIGHT_PAGE.geofence_profile_summary_total_duration_time() == FID.geofence_profile_total_duration
    assert FLEET_INSIGHT_PAGE.geofence_profile_summary_driving_time_num() == FID.geofence_profile_driving_time
    assert FLEET_INSIGHT_PAGE.geofence_profile_summary_idle_time_num() == FID.geofence_profile_idle_time
    assert FLEET_INSIGHT_PAGE.geofence_profile_summary_stop_time_num() == FID.geofence_profile_stop_time
    assert FLEET_INSIGHT_PAGE.geofence_profile_detail_triggers() == "Triggers (4)"


# LQ-514
@when('the user navigates to Insights -> State Mileage')
def click_state_mileage():
    FLEET_INSIGHT_PAGE.click_insights()
    FLEET_INSIGHT_PAGE.click_state_mileage()


@then(
    'the State Mileage page is displayed and the table is displayed with columns: "VEHICLE", "GROUP", "DEVICE SERIAL", "STATE,COUNTRY", "DISTANCE" and the number of records is displayed')
def assert_state_mileage():
    assert FLEET_INSIGHT_PAGE.get_state_mileage_title() == "STATE MILEAGE"
    assert FLEET_INSIGHT_PAGE.get_vehicle_column_text_state_mileage() == "VEHICLE"
    assert FLEET_INSIGHT_PAGE.get_group_column_text_state_mileage() == "GROUP"
    assert FLEET_INSIGHT_PAGE.get_device_serial_column_text_state_mileage() == "DEVICE SERIAL #"
    assert FLEET_INSIGHT_PAGE.get_state_country_column_text_state_mileage() == "STATE, COUNTRY"
    assert FLEET_INSIGHT_PAGE.get_distance_column_text_state_mileage() == "DISTANCE"
    assert FLEET_INSIGHT_PAGE.get_count_of_records_state_mileage() == FID.state_mileage_count


@when('the user clicks "INSIGHTS" and the user clicks "STATE MILEAGE"')
# do nothing due to state mileage is opened already

@then('the summary contains "METRICS", "TOTAL", "TOTAL DISTANCE", distance for each state')
def assert_summary_state_mileage():
    assert FLEET_INSIGHT_PAGE.get_metrics_text_state_mileage() == "METRICS"
    assert FLEET_INSIGHT_PAGE.get_total_distance_text_state_mileage() == "TOTAL DISTANCE"
    assert FLEET_INSIGHT_PAGE.get_total_text_state_mileage() == "TOTAL"


@when('the user clicks on a state')
def click_total_distance():
    FLEET_INSIGHT_PAGE.click_total_distance_text_state_mileage()


@then('the trend is updated with data of the selected state')
def assert_trend_header():
    assert FLEET_INSIGHT_PAGE.get_trend_header_text_state_mileage() == "Total Distance (mi)"


# LQ-515
@when('the user sets group filter to one group in State Mileage page')
def filter_group_state_mileage():
    FLEET_INSIGHT_PAGE.click_group_filter_state_mileage()
    FLEET_INSIGHT_PAGE.search_group_state_mileage(FID.group)
    FLEET_INSIGHT_PAGE.select_group_state_mileage()
    FLEET_INSIGHT_PAGE.click_done_state_mileage()


@then('the data belong to the group are displayed in metrics, trend, table')
def assert_filter_group_state_mileage():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == 0


@when('the user sets date filter in State Mileage page')
def filter_date__state_mileage():
    FLEET_INSIGHT_PAGE.click_date_filter_state_mileage()
    FLEET_INSIGHT_PAGE.select_last_60_days_state_mileage()
    FLEET_INSIGHT_PAGE.click_apply_button_state_mileage()


@then('the data belong to the date are displayed in metrics, trend, table')
def assert_filter_date_state_mileage():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == 0


# LQ-457
@when('the user clicks "INSIGHTS" and the user selects "DATA EXPORT')
def click_data_export():
    FLEET_INSIGHT_PAGE.click_insights()
    FLEET_INSIGHT_PAGE.click_data_export()


@then('there are group, date, vehicle filters and the table is displayed with columns '
      '"ACTION", "REPORT TYPE", "GROUP", "START DATE", "END DATE", "VEHICLE", "REQUESTED DATE')
def assert_data_export():
    assert FLEET_INSIGHT_PAGE.get_data_export_title() == "DATA EXPORT"
    assert FLEET_INSIGHT_PAGE.get_action_label() == "ACTION"
    assert FLEET_INSIGHT_PAGE.get_report_type_label() == "REPORT TYPE"
    assert FLEET_INSIGHT_PAGE.get_group_label() == "GROUP"
    assert FLEET_INSIGHT_PAGE.get_start_date_label() == "START DATE"
    assert FLEET_INSIGHT_PAGE.get_end_date_label() == "END DATE"
    assert FLEET_INSIGHT_PAGE.get_vehicle_label() == "VEHICLE"
    assert FLEET_INSIGHT_PAGE.get_requested_date_label() == "REQUESTED DATE"


# LQ-458
@when('the user sets date filter in Data Export report')
def sets_date_filter_data_export():
    FLEET_INSIGHT_PAGE.clear_existing_data_export_history()
    FLEET_INSIGHT_PAGE.select_date_range()


@when('the user clicks "Request Data"')
def click_request_data():
    FLEET_INSIGHT_PAGE.click_request_data()


@then('the report is requested')
def assert_data_export_request():
    assert FLEET_INSIGHT_PAGE.get_request_status() == "In Progress"
    assert FLEET_INSIGHT_PAGE.get_request_type() == "Detailed History"


# LQ-459
@when('the user clicks "Download" button of a request')
def download_detailed_history():
    FLEET_INSIGHT_PAGE.download_detailed_history()


@then('the report is downloaded')
def assert_download_detailed_history():
    file_name = FLEET_INSIGHT_PAGE.get_data_export_file_name()

    # the downloaded file has similar name but with different suffix like '_2', '_3' after each run
    # we could not know the exact file name to validate the existence of the file
    # assert FLEET_INSIGHT_PAGE.check_file_exist(file_name) is True

    FLEET_INSIGHT_PAGE.clear_existing_data_export_history()


# LQ-550
@when('the user clicks "INSIGHTS" and the user clicks "FLEET DATA"')
def click_fleet_data():
    FLEET_INSIGHT_PAGE.click_insights()
    FLEET_INSIGHT_PAGE.click_fleet_data()


@then('the metrics is displayed with columns: "AVERAGE", "TOTAL"')
def assert_metrics_column():
    assert FLEET_INSIGHT_PAGE.get_average_text() == "AVERAGE"
    assert FLEET_INSIGHT_PAGE.get_total_text() == "TOTAL"


@then('the metrics is displayed with values: "DISTANCE", "ENGINE HOURS", "DRIVING HOURS", '
      '"IDLE TIME", "IDLE PTO TIME", "FUEL CONSUMED", "DRIVING FUEL", "IDLING FUEL", "PTO IDLING FUEL", '
      '"FUEL ECONOMY", "DRIVING FUEL ECONOMY"')
def assert_metrics_detail():
    assert "DISTANCE" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "ENGINE HOURS" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "DRIVING HOURS" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "IDLE TIME" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "IDLE PTO TIME" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "FUEL CONSUMED" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "DRIVING FUEL" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "IDLING FUEL" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "PTO IDLING FUEL" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "FUEL ECONOMY" in FLEET_INSIGHT_PAGE.get_metric_detail_text()
    assert "DRIVING FUEL ECONOMY" in FLEET_INSIGHT_PAGE.get_metric_detail_text()


@when('the user clicks Distance column on the metrics on fleet data page')
def click_column_on_metrics():
    FLEET_INSIGHT_PAGE.click_distance_column()


@then('the trend of the selected column is displayed with title')
def assert_graph():
    assert FLEET_INSIGHT_PAGE.get_graph_header_text() == "Distance (mi)"


@when('the user clicks "GROUP" tab')
def click_group_tab():
    FLEET_INSIGHT_PAGE.click_group_tab()


@then(
    'the table is displayed with columns: "GROUP", "DISTANCE, "ENGINE HOURS, "DRIVING HOURS", "IDLE TIME", "IDLE PTO TIME", "FUEL CONSUMED", "DRIVING FUEL", "IDLING FUEL", "PTO IDLING FUEL", "FUEL ECONOMY", "DRIVING FUEL ECONOMY"')
def assert_group_tab_table():
    assert FLEET_INSIGHT_PAGE.get_groups_text() == "GROUP"
    assert FLEET_INSIGHT_PAGE.get_distance_text() == "DISTANCE"
    assert FLEET_INSIGHT_PAGE.get_engine_hours_text() == "ENGINE HOURS"
    assert FLEET_INSIGHT_PAGE.get_driving_hours_text() == "DRIVING HOURS"
    assert FLEET_INSIGHT_PAGE.get_idle_time_text() == "IDLE TIME"
    assert FLEET_INSIGHT_PAGE.get_idle_pto_time_text() == "IDLE PTO TIME"
    assert FLEET_INSIGHT_PAGE.get_fuel_consumed_text() == "FUEL CONSUMED"
    assert FLEET_INSIGHT_PAGE.get_driving_fuel_text() == "DRIVING FUEL"
    assert FLEET_INSIGHT_PAGE.get_idling_fuel_text() == "IDLING FUEL"
    assert FLEET_INSIGHT_PAGE.get_pto_idling_fuel_text() == "PTO IDLING FUEL"
    assert FLEET_INSIGHT_PAGE.get_fuel_economy_text() == "FUEL ECONOMY"
    assert FLEET_INSIGHT_PAGE.get_driving_fuel_economy_text() == "DRIVING FUEL ECONOMY"


@when('the user clicks "VEHICLE" tab')
def click_vehicle_tab():
    FLEET_INSIGHT_PAGE.click_vehicle_tab()
    sleep(2)


@then(
    'the table is displayed with columns: "VEHICLE", "ODOMETER READING", "DISTANCE", "ENGINE HOURS", '
    '"DRIVING HOURS, "IDLE TIME", "IDLE PTO TIME", "FUEL CONSUMED", "DRIVING FUEL", "IDLING FUEL", "PTO IDLING FUEL", '
    '"FUEL ECONOMY", "DRIVING FUEL ECONOMY"')
def assert_vehicle_tab_table():
    assert FLEET_INSIGHT_PAGE.get_vehicle_text() == "VEHICLE"
    assert FLEET_INSIGHT_PAGE.get_vehicle_odometer_reading_text() == "ODOMETER READING"
    assert FLEET_INSIGHT_PAGE.get_vehicle_distance_text() == "DISTANCE"
    assert FLEET_INSIGHT_PAGE.get_vehicle_engine_hours_text() == "ENGINE HOURS"
    assert FLEET_INSIGHT_PAGE.get_vehicle_driving_hours_text() == "DRIVING HOURS"
    assert FLEET_INSIGHT_PAGE.get_vehicle_idle_time_text() == "IDLE TIME"
    assert FLEET_INSIGHT_PAGE.get_vehicle_idle_pto_time_text() == "IDLE PTO TIME"
    assert FLEET_INSIGHT_PAGE.get_vehicle_fuel_consumed_text() == "FUEL CONSUMED"
    assert FLEET_INSIGHT_PAGE.get_vehicle_driving_fuel_text() == "DRIVING FUEL"
    assert FLEET_INSIGHT_PAGE.get_vehicle_idling_fuel_text() == "IDLING FUEL"
    assert FLEET_INSIGHT_PAGE.get_vehicle_pto_idling_fuel_text() == "PTO IDLING FUEL"
    assert FLEET_INSIGHT_PAGE.get_vehicle_fuel_economy_text() == "FUEL ECONOMY"
    assert FLEET_INSIGHT_PAGE.get_vehicle_driving_fuel_economy_text() == "DRIVING FUEL ECONOMY"


# LQ-523
@when('the user sets date filter in Fleet data page')
def sets_date_filter_fleet_data():
    FLEET_INSIGHT_PAGE.click_date_filter_fleet_data()
    FLEET_INSIGHT_PAGE.set_fleet_data_date_range(FID.fleet_data_date_range_start_month,
                                                 FID.fleet_data_date_range_start_day,
                                                 FID.fleet_data_date_range_start_year,
                                                 FID.fleet_data_date_range_end_month,
                                                 FID.fleet_data_date_range_end_day, FID.fleet_data_date_range_end_year)
    FLEET_INSIGHT_PAGE.click_apply_button_fleet_data()


@then('the data with selected date filters are displayed in Fleet data page')
def assert_fleet_data_date_filter():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == FID.fleet_data_filter_date


@when('the user sets group filter to one group in Fleet data page')
def sets_group_filter_fleet_data():
    FLEET_INSIGHT_PAGE.click_group_filter_fleet_data()
    FLEET_INSIGHT_PAGE.search_by_group_fleet_data(FID.group)
    FLEET_INSIGHT_PAGE.select_search_group_fleet_data()
    FLEET_INSIGHT_PAGE.click_done_button_fleet_data()


@then('the data with selected group filters are displayed in Fleet data page')
def assert_fleet_data_group_filter():
    assert FLEET_INSIGHT_PAGE.get_row_count(20) == FID.fleet_data_filter_group


# @LQ-Ad
@when('the user navigates to Admin -> Equipment Management page')
def click_equipment_management():
    DASHBOARD_PAGE.click_admin_tab()
    EQUIPMENT_MANAGEMENT_PAGE.click_equipment()
    EQUIPMENT_MANAGEMENT_PAGE.click_device_column_sorting_button()
    EQUIPMENT_MANAGEMENT_PAGE.click_device_column_sorting_button()


@then('get the number of equipment with attached devices')
def get_equipment_with_attached_devices_count():
    global equipment_with_device_count
    equipment_with_device_count = FLEET_INSIGHT_PAGE.get_equipment_with_attached_devices_count()
    assert FLEET_INSIGHT_PAGE.equipment_count == equipment_with_device_count
