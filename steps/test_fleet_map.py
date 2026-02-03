import time
from time import sleep

from hamcrest import assert_that, contains_string
from pytest_bdd import scenarios, given, when, then

from pages.fleet_map_page import FleetMapPage
from pages.login_page import LoginPage
from steps.common import FLEET_URL, ENV, AutomationDataManager
from data.int.fleet_map_data_int import FleetMapDataInt as FMD_INT
from data.prod.fleet_map_data_prod import FleetMapDataProd as FMD_PROD
from data.stg.fleet_map_data_stg import FleetMapDataStg as FMD_STG

LOGIN_PAGE = 0
FLEET_MAP_PAGE = 0
RANDOM_NAME = ''
FMD = 0
data = 0

scenarios('../features/fleet_map.feature')


# LQ-15218
@given('the login page is displayed')
def launch_browser(browser):
    global LOGIN_PAGE, FLEET_MAP_PAGE, FMD, RANDOM_NAME

    LOGIN_PAGE = LoginPage(browser)
    FLEET_MAP_PAGE = FleetMapPage(browser)
    RANDOM_NAME = FLEET_MAP_PAGE.get_random_name(8)

    browser.get(FLEET_URL)

    if ENV == 'int':
        FMD = FMD_INT
    elif ENV == 'stg':
        FMD = FMD_STG
    else:
        FMD = FMD_PROD


@when('the user enters a newly created username/password and clicks the login button')
def login():
    LOGIN_PAGE.enter_username(FMD.user_name)
    LOGIN_PAGE.enter_password(FMD.password)

    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed(FLEET_URL, FMD.user_name, FMD.password)


@then('the Fleet application is displayed')
def assert_fleet_app():
    # need update test case after "fleet tracking home" is done
    FLEET_MAP_PAGE.click_map()
    assert FLEET_MAP_PAGE.get_fleet_tracking_title() == "FLEET TRACKING"


# LQ-12380
@when('"Fleet Dispatcher" user is on the Home page (Dashboard)')
def user_lands_on_home():
    print("User is on Home page (Dashboard)")


@then(
    'the metrics table is displayed with columns: "VEHICLE", "GROUP", "IDLE VIOLATIONS", "IDLE DURATION COLUMNS" in Idle Duration widget and the table is displayed with columns: "GEOFENCE", "GROUP", "TRIGGERS", "TRIGGER DURATION COLUMNS" in Geofence Triggers widget')
def assert_dashboard_metrics_table():
    # need update test case after "fleet tracking home" is done
    assert FLEET_MAP_PAGE.get_metrics_text() == "METRICS"
    assert FLEET_MAP_PAGE.get_metrics_geofence_triggers() == "Geofence Triggers"
    assert FLEET_MAP_PAGE.get_metrics_geofence_column() == "GEOFENCE"
    assert FLEET_MAP_PAGE.get_metrics_group_column() == "GROUP"
    assert FLEET_MAP_PAGE.get_metrics_triggers_column() == "TRIGGERS"
    assert FLEET_MAP_PAGE.get_metrics_duration_column() == "DURATION"
    assert FLEET_MAP_PAGE.get_metrics_idle_duration() == "Idle Duration"


# LQ-12386
@when('the user sets group filter to one group in the Dashboard')
def user_changes_group():
    FLEET_MAP_PAGE.click_dashboard_filter_by_group_dropdown()
    FLEET_MAP_PAGE.click_dashboard_filter_by_group_done_button()


@then(
    'the vehicle count is displayed, the Idle Duration count with selected filters are displayed, the data with selected filters are displayed in Idle Duration widget, the Geofence Triggers count with selected filters are displayed, and the data with selected filters are displayed in Geofence Triggers widget')
def assert_dashboard_metrics_table_for_group_filter():
    assert FLEET_MAP_PAGE.get_geofence_triggers_text() == "GEOFENCE TRIGGERS"
    assert FLEET_MAP_PAGE.get_geofence_triggers_count() == "100"
    assert FLEET_MAP_PAGE.get_idle_duration_text() == "IDLE DURATION"
    assert FLEET_MAP_PAGE.get_idle_duration_count() == "--"
    assert FLEET_MAP_PAGE.get_metrics_text() == "METRICS"
    assert FLEET_MAP_PAGE.get_metrics_geofence_triggers() == "Geofence Triggers"
    assert FLEET_MAP_PAGE.get_metrics_geofence_column() == "GEOFENCE"
    assert FLEET_MAP_PAGE.get_metrics_group_column() == "GROUP"
    assert FLEET_MAP_PAGE.get_metrics_triggers_column() == "TRIGGERS"
    assert FLEET_MAP_PAGE.get_metrics_duration_column() == "DURATION"
    assert FLEET_MAP_PAGE.get_metrics_idle_duration() == "Idle Duration"


# Currently, no data to assert in the Idle Duration table.

@when('the user sets date filter in the Dashboard')
def user_changes_date():
    FLEET_MAP_PAGE.click_dashboard_filter_by_date_dropdown()
    FLEET_MAP_PAGE.click_dashboard_last_60_days()
    FLEET_MAP_PAGE.click_dashboard_date_apply_button()


@then(
    'the correct date related data for vehicle count is displayed, the Idle Duration count with selected filters are displayed, the data with selected filters are displayed in Idle Duration widget, the Geofence Triggers count with selected filters are displayed, and the data with selected filters are displayed in Geofence Triggers widget')
def assert_dashboard_metrics_table_for_date_filter():
    assert FLEET_MAP_PAGE.get_geofence_triggers_text() == "GEOFENCE TRIGGERS"
    assert FLEET_MAP_PAGE.get_geofence_triggers_count() == "100"
    assert FLEET_MAP_PAGE.get_idle_duration_text() == "IDLE DURATION"
    assert FLEET_MAP_PAGE.get_idle_duration_count() == "--"
    assert FLEET_MAP_PAGE.get_metrics_text() == "METRICS"
    assert FLEET_MAP_PAGE.get_metrics_geofence_triggers() == "Geofence Triggers"
    assert FLEET_MAP_PAGE.get_metrics_geofence_column() == "GEOFENCE"
    assert FLEET_MAP_PAGE.get_metrics_group_column() == "GROUP"
    assert FLEET_MAP_PAGE.get_metrics_triggers_column() == "TRIGGERS"
    assert FLEET_MAP_PAGE.get_metrics_duration_column() == "DURATION"
    assert FLEET_MAP_PAGE.get_metrics_idle_duration() == "Idle Duration"


# Currently, no data to assert in the Idle Duration table.

# LQ-447 part 1
@when(
    'the user clicks "Clear List" and enters some characters in Search box and selects a geofence in the Suggestion List')
def add_geofence_to_working_list_via_suggestion_list():
    FLEET_MAP_PAGE.add_geofence_to_working_list(FMD.geofence_name_existing)


@then('the geofence is displayed in Working List and the geofence is displayed on Map')
def assert_geofence_detail_in_working_list():
    working_list_geofence = FLEET_MAP_PAGE.get_working_list_geofence()
    assert working_list_geofence['geofence_name'] == FMD.geofence_name_existing
    assert working_list_geofence['status'] == "Status: Active"
    assert working_list_geofence['type'] == "Type: " + FMD.geofence_name_existing_type


# LQ-445
@when('the user clicks "View Details" of a Geofence in Working List')
def view_geofence_detail():
    FLEET_MAP_PAGE.view_geofence_detail()
    sleep(3)


@then('the Geofence detail panel is opened and Geofence Name is displayed and '
      '"Geofence Trigger Settings" is displayed with: "Status", "Facing, Day(s)", "Time", '
      '"Vehicles Group", "IncludeSubgroups" and there are "Edit Geofence", "Delete Geofence" buttons')
def assert_geofence_detail_panel():
    assert FLEET_MAP_PAGE.get_geofence_panel_close_button() == "Close"
    assert FLEET_MAP_PAGE.get_geofence_panel_edit_button() == "Edit Geofence"
    assert FLEET_MAP_PAGE.get_geofence_panel_delete_button() == "Delete Geofence"

    panel_detail_dict = FLEET_MAP_PAGE.get_geofence_pin_panel_details()
    assert panel_detail_dict['geofence_name'] == FMD.geofence_name_existing
    assert panel_detail_dict['settings'] == "Geofence Trigger Settings"
    assert panel_detail_dict['status'] == "Status: Active"
    assert panel_detail_dict['facing'] == "Facing: " + FMD.geofence_name_existing_type
    assert panel_detail_dict['days'] == "Day(s): Everyday"
    assert panel_detail_dict['time'] == "Time: 24hrs"
    assert_that(panel_detail_dict['vehicles'], contains_string('Vehicles:'))
    assert_that(panel_detail_dict['vehicles'], contains_string(FMD.geofence_group))
    assert_that(panel_detail_dict['vehicles'], contains_string('Include Subgroups: Yes'))

    FLEET_MAP_PAGE.close_geofence_pin_panel()


#@LQ-112132
@when('the user search Geofences from search box and the user clicks Search button')
def search_the_geofence_search_box():
    FLEET_MAP_PAGE.add_geofences_to_working_list_search_box("fence-au")


@then('user should able to see matched Geofences with "+ Working List, Map, check box" options')
def search_result_of_geofence():
    assert FLEET_MAP_PAGE.get_geofence_name_text() == FMD.geofence_name_search
    FLEET_MAP_PAGE.get_working_list_button_is_diplayed()
    FLEET_MAP_PAGE.get_map_button_is_displayed()
    FLEET_MAP_PAGE.get_check_box_is_displayed()


@when('user search Geofences from search box and the user clicks Search button and the user clicks "+Working list" button')
def add_the_geofence_to_the_working_list():
    FLEET_MAP_PAGE.click_the_working_list_button()


@then('geofence is added to the working list with desired details')
def geofence_is_added_the_working_list():
    working_list_1st_geofence = FLEET_MAP_PAGE.get_working_list_1st_geofence()
    assert working_list_1st_geofence['geofence_name'] == FMD.geofence_name_search


@when('user search geofence from search box and the user clicks Search button and the user clicks "Map" button')
def geofence_map_button():
    FLEET_MAP_PAGE.add_geofences_to_working_list_search_box("fence-au")
    FLEET_MAP_PAGE.click_map_button()


@then('geofence is centered on map & the desired details of geofence is displayed on left panel')
def geofence_desired_details():
    assert FLEET_MAP_PAGE.get_geofence_panel_close_button() == "Close"
    assert FLEET_MAP_PAGE.get_geofence_panel_edit_button() == "Edit Geofence"
    assert FLEET_MAP_PAGE.get_geofence_panel_delete_button() == "Delete Geofence"
    FLEET_MAP_PAGE.close_geofence_pin_panel()


# LQ-446
@when('the user enters some characters in Search box and the user selects a vehicle in the Suggestion List')
def add_vehicle_to_WL_via_suggestion_list():
    FLEET_MAP_PAGE.clear_search_box()
    FLEET_MAP_PAGE.enter_vehicle_name(FMD.vehicle)
    sleep(4)
    FLEET_MAP_PAGE.select_vehicle_from_suggestion_list()


@then('the vehicles are displayed in Working List and the vehicles are displayed on Map')
def assert_vehicle_added():
    assert FLEET_MAP_PAGE.get_vehicle_name() == FMD.vehicle


@when(
    'the user enters some characters in Search box and the user clicks Search button and the user checks a vehicle and the user clicks "Add to Working List"')
def add_vehicle_to_WL_via_search_result():
    FLEET_MAP_PAGE.clear_working_list()
    FLEET_MAP_PAGE.enter_vehicle_name(FMD.vehicle)
    sleep(2)
    FLEET_MAP_PAGE.search_for_vehicle()
    sleep(2)
    FLEET_MAP_PAGE.select_vehicle()
    sleep(2)
    FLEET_MAP_PAGE.add_to_working_list()


# Then step of LQ-446 is the same with previous scenario of LQ-446


# @LQ-112120
@when('the user search vehicle from search box and the user clicks Search button')
def search_the_vehicle_search_box():
    FLEET_MAP_PAGE.clear_working_list()
    FLEET_MAP_PAGE.enter_vehicle_name(FMD.vehicle)
    FLEET_MAP_PAGE.search_for_vehicle()


@then('user should able to see matched vehicle with "+ Working List, Map, check box" options')
def search_result_of_geofence():
    assert FLEET_MAP_PAGE.get_vehicle_name_text() == FMD.vehicle
    FLEET_MAP_PAGE.get_working_list_button_is_diplayed()
    FLEET_MAP_PAGE.get_map_button_is_displayed()
    FLEET_MAP_PAGE.get_check_box_is_displayed()


@when('user search vehicle from search box and the user clicks Search button and the user clicks "+Working list" button')
def add_the_geofence_to_the_working_list():
    FLEET_MAP_PAGE.click_the_working_list_button()


@then('vehicle is added to the working list with desired details')
def assert_vehicle_added():
    assert FLEET_MAP_PAGE.get_vehicle_name() == FMD.vehicle


@when('user search vehicle from search box and the user clicks Search button and the user clicks "Map" button')
def vehicle_map_button():
    FLEET_MAP_PAGE.clear_working_list()
    FLEET_MAP_PAGE.enter_vehicle_name(FMD.vehicle)
    FLEET_MAP_PAGE.search_for_vehicle()
    FLEET_MAP_PAGE.click_map_button()


@then('vehicle is centered on map & the desired details of vehicle is displayed on left panel')
def vehicle_desired_details():
    assert FLEET_MAP_PAGE.get_pin_panel_close_button() == "Close"
    FLEET_MAP_PAGE.close_geofence_pin_panel()
    FLEET_MAP_PAGE.clear_search_box()
    # panel_detail_dict = FLEET_MAP_PAGE.get_live_pin_panel_details()
    # assert panel_detail_dict['vehicle_name'] == FMD.vehicle


# LQ-449
@when('the user waits for 10 seconds')
def get_live_vehicle_pin():
    FLEET_MAP_PAGE.get_live_vehicle_pin()


@then('the map refreshes and the vehicle is displayed on new location on Map')
def assert_map_refreshed():
    live_vehicle_pin = FLEET_MAP_PAGE.get_live_vehicle_pin()
    assert FLEET_MAP_PAGE.check_live_map_refreshed(live_vehicle_pin) is True


# LQ-7203
@when('the user clicks Zoom in icon on map')
def click_zoom_in_icon():
    FLEET_MAP_PAGE.click_zoom_in()
    sleep(2)


@then('Map Zooms in one level and previous center of map will remain at the center for each zoom level change')
def assert_map_pin_after_zoom_in():
    assert FLEET_MAP_PAGE.get_live_pin_vehicle_name() == FMD.vehicle
    assert FLEET_MAP_PAGE.get_vehicle_name() == FMD.vehicle


@when('the user clicks Zoom out icon on map')
def click_zoom_out_icon():
    FLEET_MAP_PAGE.click_zoom_out()
    FLEET_MAP_PAGE.click_zoom_out()
    sleep(2)


@then('Map Zooms out one level and previous center of map will remain at the center for each zoom level change')
def assert_map_pin_after_zoom_out():
    assert FLEET_MAP_PAGE.get_live_pin_vehicle_name() == FMD.vehicle
    assert FLEET_MAP_PAGE.get_vehicle_name() == FMD.vehicle


# LQ-442
@when('the user clicks a vehicle pin on Map')
def show_pin_detail():
    FLEET_MAP_PAGE.click_vehicle_pin()


@then('the pin detail panel is opened and "Vehicle Name", "Status", "Driver", '
      '"Group", "Device", Occurrence Time, Time since occurrence, "Speed", '
      '"Ignition", Address, Latitude, Longitude are displayed on pin detail panel')
def assert_live_pin_detail_panel():
    assert FLEET_MAP_PAGE.get_pin_panel_close_button() == "Close"

    panel_detail_dict = FLEET_MAP_PAGE.get_live_pin_panel_details()
    assert panel_detail_dict['vehicle_name'] == FMD.vehicle
    assert panel_detail_dict['status'] == FMD.live_pin_status
    assert panel_detail_dict['driver'] == "Driver: " + FMD.driver
    assert panel_detail_dict['group'] == "Group: " + FMD.group
    assert panel_detail_dict['device'] == "Device: " + FMD.device
    assert panel_detail_dict['speed'] == "Speed: " + FMD.live_pin_speed
    assert panel_detail_dict['ignition'] == "Ignition: " + FMD.live_pin_ignition
    assert_that(panel_detail_dict['occur_time'], contains_string(FMD.live_pin_date))
    assert_that(panel_detail_dict['time_since'], contains_string(' ago'))

    assert FLEET_MAP_PAGE.get_pin_panel_address() == FMD.live_pin_address
    assert_that(FLEET_MAP_PAGE.get_pin_panel_coordinate(), contains_string(FMD.live_pin_coordinate))

    FLEET_MAP_PAGE.close_map_pin_panel()


# LQ-7201
@when('the user clicks a moving vehicle on map')
def show_moving_pin_detail():
    sleep(2)
    FLEET_MAP_PAGE.click_vehicle_pin()
    sleep(2)


@then(
    'the details info is displayed on the left panel and icon on top left corner is arrow with green background color '
    'and there are Vehicle, Status, Driver, Group, Device, Date, Speed, Time since position(only has day, hour, minute), Ignition, Street Address info and lat/log '
    'and There are icons in front of vehicle, gps data, address and lat/log sections')
def assert_live_moving_pin_detail_panel():
    current_date = str(time.strftime('%b %#d, %Y, %I:%M:%S %p %Z'))[:12]

    panel_detail_dict = FLEET_MAP_PAGE.get_live_pin_panel_details()
    assert_that(panel_detail_dict['vehicle_name'], contains_string('TestVehicle'))
    assert panel_detail_dict['status'] == "Status: Moving"
    assert panel_detail_dict['driver'] == "Driver: Unassigned"
    assert_that(panel_detail_dict['group'], contains_string('TestCompany'))
    assert_that(panel_detail_dict['device'], contains_string('testDataAutomation'))
    assert panel_detail_dict['speed'] == "Speed: 64mph"
    assert panel_detail_dict['ignition'] == "Ignition: Off (Check wiring)"
    assert_that(panel_detail_dict['occur_time'], contains_string(current_date))
    assert_that(panel_detail_dict['time_since'], contains_string(' ago'))
    # geofence triggering is not shown now, but could not reproducible, comment this for now
    # assert_that(panel_detail_dict['triggering_geofences'], contains_string('Geofence'))

    assert FLEET_MAP_PAGE.get_pin_panel_address() == "Tony Gwynn Memorial Fwy, San Diego, CA 92129, USA"
    assert_that(FLEET_MAP_PAGE.get_pin_panel_coordinate(), contains_string('32.952432, -117.10341'))

    assert_that(FLEET_MAP_PAGE.get_moving_pin_icon_working_list(), contains_string('moving-in'))
    assert_that(FLEET_MAP_PAGE.get_moving_pin_icon_panel_detail(), contains_string('moving-in'))
    assert FLEET_MAP_PAGE.get_address_icon_panel_detail() is not None
    assert FLEET_MAP_PAGE.get_date_icon_panel_detail() is not None

    FLEET_MAP_PAGE.close_map_pin_panel()


# LQ-512
@when(
    'the user adds an address to working list and the user clicks "View Details" and the user clicks "Find Closest Vehicle"')
def add_address_to_WL_via_suggestion_list():
    FLEET_MAP_PAGE.add_address_in_working_list(FMD.closest_vehicle_address)
    FLEET_MAP_PAGE.click_view_detail_address()
    sleep(2)
    FLEET_MAP_PAGE.click_find_closest_vehicle()


@then(
    'three closest vehicles are displayed in Closest Vehicles list and the vehicle name, driver, group, estimation distance and time are displayed in Closest Vehicles list and the first vehicle is highlighted in Closest Vehicles list and the route of the three vehicles are displayed on map and the route of the first vehicle is highlighted on map')
def assert_closest_vehicles():
    estimation = int(FLEET_MAP_PAGE.get_1st_vehicle_time_find_closest_vehicle()[-3:-1])

    assert FLEET_MAP_PAGE.get_title_find_closest_vehicle() == "Closest Vehicles"
    assert_that(FLEET_MAP_PAGE.get_coordinates_find_closest_vehicle(),
                contains_string(FMD.closest_vehicle_address_coordinate))
    assert FLEET_MAP_PAGE.get_address_find_closest_vehicle() == FMD.closest_vehicle_address
    assert FLEET_MAP_PAGE.get_1st_vehicle_name_find_closest_vehicle() == FMD.vehicle
    assert FLEET_MAP_PAGE.get_1st_vehicle_driver_find_closest_vehicle() == "Driver: " + FMD.driver
    assert FLEET_MAP_PAGE.get_1st_vehicle_group_find_closest_vehicle() == "Group: " + FMD.group
    assert_that(FLEET_MAP_PAGE.get_1st_vehicle_time_find_closest_vehicle(), contains_string('h'))
    assert estimation >= FMD.closest_vehicle_estimation_min
    assert estimation <= FMD.closest_vehicle_estimation_max
    # assert FLEET_MAP_PAGE.get_1st_vehicle_distance_find_closest_vehicle() == FMD.closest_vehicle_distance
    assert FLEET_MAP_PAGE.get_1st_vehicle_delete_find_closest_vehicle() is not None

    FLEET_MAP_PAGE.close_panel_find_closest_vehicle()


# LQ-465
@given('the user switch to history mode')
def switch_to_history_mode():
    FLEET_MAP_PAGE.click_history_button()
    FLEET_MAP_PAGE.set_history_date_range(FMD.date_range_start_month, FMD.date_range_start_day,
                                          FMD.date_range_start_year,
                                          FMD.date_range_end_month, FMD.date_range_end_day, FMD.date_range_end_year)
    FLEET_MAP_PAGE.click_apply_button()
    sleep(8)


# @when('the user enters some characters in Search box and the user selects a vehicle in the Suggestion List')
# * When step of LQ-465 is the same with LQ-446
# @then('the vehicles are displayed in Working List and the vehicles are displayed on Map')
# * Then step of LQ-465 is the same with LQ-446

# @when('the user enters some characters in Search box and the user clicks Search button and the user checks a vehicle and the user clicks "Add to Working List"')
# * When step of LQ-465 is the same with LQ-446
# @then('the vehicles are displayed in Working List and the vehicles are displayed on Map')
# * Then step of LQ-465 is the same with LQ-446


# LQ-460
@when(
    'the user adds the vehicle to Working List and the user clicks "View History" and the user clicks "Yesterday" and the user clicks "Apply"')
def show_history():
    # previous test case LQ-465 already switch to history mode and add vehicle to working list
    sleep(1)


@then('the Trip, Route, Point icon are displayed on Working List and the Trip pin, Route line are displayed on Map')
def assert_working_list():
    assert_that(FLEET_MAP_PAGE.get_trip_on_working_list(), contains_string('trips'))
    assert_that(FLEET_MAP_PAGE.get_route_on_working_list(), contains_string('route'))
    assert_that(FLEET_MAP_PAGE.get_trip_start_on_map(), contains_string('transparent'))
    assert_that(FLEET_MAP_PAGE.get_trip_end_on_map(), contains_string('transparent'))


# LQ-461
@when('the user clicks a Moving Track Point Pin on Map')
def view_moving_track_point_pin():
    # disable icons on working list except moving icon
    FLEET_MAP_PAGE.click_speed_icon()
    FLEET_MAP_PAGE.click_idle_icon()
    if ENV == 'stg':
        FLEET_MAP_PAGE.click_geofence_icon()
    # FLEET_MAP_PAGE.click_geofence_icon()
    FLEET_MAP_PAGE.click_trip_icon()
    sleep(1)
    # FLEET_MAP_PAGE.click_moving_track_point() # commenting due to bug CXFA-6394
    sleep(3)


@then(
    'the pin detail panel is opened and "Vehicle Name", "Moving", "Driver", "Group", "Device", Occurrence Time, Time since occurrence, "Speed", "Ignition", Address, Latitude, Longitude are displayed on pin detail panel and Google street view is displayed on pin detail panel')
def assert_moving_track_point_detail():
    # comment this due to bug MEGA-292
    # moving_panel_dict = FLEET_MAP_PAGE.get_moving_panel_detail()
    # assert moving_panel_dict['vehicle_name'] == FMD.vehicle
    # assert moving_panel_dict['status'] == "Status: Moving"
    # assert moving_panel_dict['driver'] == "Driver: " + FMD.driver
    # assert moving_panel_dict['group'] == "Group: " + FMD.group
    # assert moving_panel_dict['device'] == "Device: " + FMD.device
    # assert_that(moving_panel_dict['occur_time'], contains_string(FMD.moving_occur_time))
    # assert_that(moving_panel_dict['time_since'], contains_string(' ago'))
    # assert moving_panel_dict['speed'] == "Speed: " + FMD.moving_speed
    # assert_that(moving_panel_dict['address'], contains_string(FMD.moving_address))
    # assert_that(moving_panel_dict['coordinate'], contains_string(FMD.moving_coordinate))
    #
    # assert FLEET_MAP_PAGE.google_street_view_is_displayed() is True

    # FLEET_MAP_PAGE.click_moving_panel_close_button() # commenting due to bug CXFA-6394
    sleep(2)


# LQ-462
@when('the user clicks a Trip start pin on Map on history page')
def view_trip_start_pin():
    sleep(2)
    FLEET_MAP_PAGE.click_routes_icon()
    FLEET_MAP_PAGE.click_trip_icon()  # click trip icon on working list to enable trips
    sleep(4)
    FLEET_MAP_PAGE.click_trip_start_pin()
    sleep(3)


@then(
    'the start pin detail panel is opened and "Vehicle Name", "Status", "Driver", "Group", "Device", Occurrence Time, "Distance", "Max Speed", Address, Latitude, Longitude, "Stop Duration" are displayed on pin detail panel')
def assert_trip_start_detail():
    assert FLEET_MAP_PAGE.get_trip_panel_close_button() == "Close"

    trip_start_info_dict = FLEET_MAP_PAGE.get_trip_panel_details()
    assert trip_start_info_dict['vehicle_name'] == FMD.vehicle
    assert trip_start_info_dict['trip_tag'] == "Trip Start"
    assert trip_start_info_dict['driver'] == "Driver: " + FMD.driver
    assert trip_start_info_dict['group'] == "Group: " + FMD.group
    assert trip_start_info_dict['device'] == "Device: " + FMD.device
    assert trip_start_info_dict['trip_num'] == "Trip 1 Start"
    assert trip_start_info_dict['duration'] == "Trip Duration: " + FMD.trip_duration
    assert trip_start_info_dict['distance'] == "Distance: " + FMD.trip_distance
    assert trip_start_info_dict['max_speed'] == "Max Speed: " + FMD.trip_max_speed
    assert_that(trip_start_info_dict['occur_time'], contains_string(FMD.trip_start_occur_time))
    assert_that(trip_start_info_dict['time_since'], contains_string(' ago'))

    assert FLEET_MAP_PAGE.get_trip_pin_panel_address() == FMD.trip_start_address
    assert_that(FLEET_MAP_PAGE.get_trip_pin_panel_coordinate(), contains_string(FMD.trip_start_coordinate))

    FLEET_MAP_PAGE.close_trip_panel()


@when('the user clicks a Trip end pin on Map on history page')
def view_trip_end_pin():
    sleep(1)
    FLEET_MAP_PAGE.click_trip_end_pin()
    sleep(3)


@then(
    'the end pin detail panel is opened and "Vehicle Name", "Status", "Driver", "Group", "Device", Occurrence Time, "Distance", "Max Speed", Address, Latitude, Longitude, "Stop Duration" are displayed on pin detail panel')
def assert_trip_end_detail():
    assert FLEET_MAP_PAGE.get_trip_panel_close_button() == "Close"

    trip_end_info_dict = FLEET_MAP_PAGE.get_trip_panel_details()
    assert trip_end_info_dict['vehicle_name'] == FMD.vehicle
    assert trip_end_info_dict['trip_tag'] == "Trip End"
    assert trip_end_info_dict['driver'] == "Driver: " + FMD.driver
    assert trip_end_info_dict['group'] == "Group: " + FMD.group
    assert trip_end_info_dict['device'] == "Device: " + FMD.device
    assert trip_end_info_dict['trip_num'] == "Trip 1 End"
    assert_that(trip_end_info_dict['duration'], contains_string(FMD.trip_duration))
    assert trip_end_info_dict['distance'] == "Distance: " + FMD.trip_distance
    assert trip_end_info_dict['max_speed'] == "Max Speed: " + FMD.trip_max_speed
    assert_that(trip_end_info_dict['occur_time'], contains_string(FMD.trip_end_occur_time))
    assert_that(trip_end_info_dict['time_since'], contains_string(' ago'))

    assert FLEET_MAP_PAGE.get_trip_pin_panel_address() == FMD.trip_end_address
    assert_that(FLEET_MAP_PAGE.get_trip_pin_panel_coordinate(), contains_string(FMD.trip_end_coordinate))

    FLEET_MAP_PAGE.close_trip_panel()


# LQ-463
@when('the user clicks speed violation on Map')
def view_speed_violation_pin():
    global data
    data = AutomationDataManager()
    data.cloud_add_vehicle()
    data.add_device()
    data.send_device_speed_violations()
    sleep(2)
    # disable trip icon on working list, others are already disabled
    FLEET_MAP_PAGE.click_trip_icon()
    sleep(1)
    FLEET_MAP_PAGE.click_speed_icon()  # click speed icon on working list to enable speed violation
    sleep(4)
    FLEET_MAP_PAGE.click_speed_violation_pin()
    sleep(3)


@then(
    'Speed Violation pin detail panel is opened and "Vehicle Name", "Status", "Driver", "Group", "Device", Occurrence Time, "Speed Limit", "Max Speed", "Speed Duration", Address, Latitude, Longitude are displayed on pin detail panel')
def assert_speed_violation_detail():
    assert FLEET_MAP_PAGE.get_pin_panel_close_button() == "Close"

    speed_violation_info_dict = FLEET_MAP_PAGE.get_speed_violation_pin_details()
    assert speed_violation_info_dict['vehicle_name'] == FMD.vehicle
    assert speed_violation_info_dict['status'] == "Status:" + FMD.vehicle_status
    assert speed_violation_info_dict['driver'] == "Driver: " + FMD.driver
    assert speed_violation_info_dict['group'] == "Group: " + FMD.group
    assert speed_violation_info_dict['device'] == "Device: " + FMD.device
    assert speed_violation_info_dict['speed_limit'] == "Speed Limit: " + FMD.speed_violation_speed_limit
    assert speed_violation_info_dict['max_speed'] == "Max Speed: " + FMD.speed_violation_max_speed
    assert speed_violation_info_dict['speed_duration'] == "Speeding Duration: " + FMD.speed_violation_duration
    assert speed_violation_info_dict['occur_time'] == FMD.speed_violation_occur_time
    assert_that(speed_violation_info_dict['time_since'], contains_string(' ago'))

    assert FLEET_MAP_PAGE.get_pin_panel_address() == FMD.speed_violation_address
    assert_that(FLEET_MAP_PAGE.get_pin_panel_coordinate(), contains_string(FMD.speed_violation_coordinate))

    FLEET_MAP_PAGE.close_map_pin_panel()


@when('the user clicks Idle Violation on Map')
def view_idle_violation_pin():
    sleep(2)
    # disable speed icon on working list, others are already disabled
    FLEET_MAP_PAGE.click_speed_icon()
    sleep(1)
    FLEET_MAP_PAGE.click_idle_icon()  # click idle icon on working list to enable idle violation
    sleep(4)
    FLEET_MAP_PAGE.click_idle_violation_pin(FMD.position)
    sleep(3)


@then(
    'Idle Violation pin panel is opened and "Vehicle Name", "Status: Idle Violation", "Driver", "Group", "Device", Occurrence Time, "Idle Duration", Address, Latitude, Longitude are displayed on pin detail panel')
def assert_idle_violation_detail():
    assert FLEET_MAP_PAGE.get_pin_panel_close_button() == "Close"

    idle_violation_info_dict = FLEET_MAP_PAGE.get_idle_violation_pin_details()
    assert idle_violation_info_dict['vehicle_name'] == FMD.vehicle
    assert idle_violation_info_dict['status'] == "Status: Idle Violation"
    assert idle_violation_info_dict['driver'] == "Driver: " + FMD.driver
    assert idle_violation_info_dict['group'] == "Group: " + FMD.group
    assert idle_violation_info_dict['device'] == "Device: " + FMD.device
    assert idle_violation_info_dict['idle_duration'] == "Idle Duration: " + FMD.idle_violation_duration
    assert idle_violation_info_dict['occur_time'] == FMD.idle_violation_occur_time
    assert_that(idle_violation_info_dict['time_since'], contains_string(' ago'))

    assert FLEET_MAP_PAGE.get_pin_panel_address() == FMD.idle_violation_address
    assert_that(FLEET_MAP_PAGE.get_pin_panel_coordinate(), contains_string(FMD.idle_violation_coordinate))

    FLEET_MAP_PAGE.close_map_pin_panel()


# LQ-3314
# LQ-463_part_3
@when('the user clicks Geofence Violation Start pin on Map')
def view_geofence_violation_start_pin():
    sleep(2)
    # disable geofence icon on working list, others are already disabled
    FLEET_MAP_PAGE.click_idle_icon()
    sleep(1)
    FLEET_MAP_PAGE.click_geofence_icon()  # click geofence icon on working list to enable geofence violation
    sleep(4)
    FLEET_MAP_PAGE.click_geofence_violation_start_pin()
    sleep(3)


@then(
    'the Geofence Violation Start pin panel is opened and "Vehicle Name", "Status", "Driver", "Group", "Device", Occurrence Time, Address, Latitude, Longitude are displayed on pin detail panel')
def assert_geofence_violation_start_detail():
    assert FLEET_MAP_PAGE.get_pin_panel_close_button() == "Close"

    geofence_violation_info_dict = FLEET_MAP_PAGE.get_geofence_violation_start_pin_details()
    assert geofence_violation_info_dict['vehicle_name'] == FMD.vehicle
    assert geofence_violation_info_dict['status'] == "Geofence Start (" + FMD.geofence_name_pin_detail + ")"
    assert geofence_violation_info_dict['driver'] == "Driver: Unassigned"
    assert geofence_violation_info_dict['group'] == "Group: " + FMD.group
    assert geofence_violation_info_dict['device'] == "Device: " + FMD.device
    assert geofence_violation_info_dict['occur_time'] == FMD.geofence_activation_start_occur_time
    assert_that(geofence_violation_info_dict['time_since'], contains_string(' ago'))

    assert FLEET_MAP_PAGE.get_pin_panel_address() == FMD.geofence_activation_start_address
    assert_that(FLEET_MAP_PAGE.get_pin_panel_coordinate(), contains_string(FMD.geofence_activation_start_coordinate))

    FLEET_MAP_PAGE.close_map_pin_panel()


# LQ-3317
# LQ-463_part_4
@when('the user clicks Geofence Violation End pin on Map')
def view_geofence_violation_end_pin():
    sleep(2)
    FLEET_MAP_PAGE.click_geofence_violation_end_pin()
    sleep(3)


@then(
    'the Geofence Violation End pin panel is opened and "Vehicle Name", "Status", "Driver", "Group", "Device", Occurrence Time, Address, Latitude, Longitude are displayed on pin detail panel')
def assert_geofence_violation_end_detail():
    assert FLEET_MAP_PAGE.get_pin_panel_close_button() == "Close"

    geofence_violation_info_dict = FLEET_MAP_PAGE.get_geofence_violation_end_pin_details()
    assert geofence_violation_info_dict['vehicle_name'] == FMD.vehicle
    assert geofence_violation_info_dict['status'] == "Geofence End (" + FMD.geofence_name_pin_detail + ")"
    assert geofence_violation_info_dict['driver'] == "Driver: Unassigned"
    assert geofence_violation_info_dict['group'] == "Group: " + FMD.group
    assert geofence_violation_info_dict['device'] == "Device: " + FMD.device
    assert geofence_violation_info_dict['duration'] == "Duration: " + FMD.geofence_activation_end_duration
    assert geofence_violation_info_dict['occur_time'] == FMD.geofence_activation_end_occur_time
    assert_that(geofence_violation_info_dict['time_since'], contains_string(' ago'))

    assert FLEET_MAP_PAGE.get_pin_panel_address() == FMD.geofence_activation_end_address
    assert_that(FLEET_MAP_PAGE.get_pin_panel_coordinate(), contains_string(FMD.geofence_activation_end_coordinate))

    FLEET_MAP_PAGE.close_map_pin_panel()


# LQ-7174
@when(
    'the user clicks the "View History" button & selects a date range for history mode & filter by vehicle from the working list')
def filter_by_vehicle_in_history():
    # unselect address, geofence and equipment
    options_to_change_dict = {'1': 'Addresses', '2': 'Geofences', '3': 'Equipment'}
    sleep(3)
    FLEET_MAP_PAGE.click_history_button()
    FLEET_MAP_PAGE.set_history_date_range(FMD.date_range_start_month, FMD.date_range_start_day,
                                          FMD.date_range_start_year,
                                          FMD.date_range_end_month, FMD.date_range_end_day, FMD.date_range_end_year)
    FLEET_MAP_PAGE.click_apply_button()
    FLEET_MAP_PAGE.click_working_list_filter()
    FLEET_MAP_PAGE.set_working_list_filters(options_to_change_dict)
    FLEET_MAP_PAGE.close_working_list_filter()


@then('Vehicle should be list in the history mode working list')
def assert_vehicle_history():
    assert FLEET_MAP_PAGE.get_vehicle_name_history() == FMD.vehicle


@when('the user deletes vehicle in working list')
def delete_vehicle_history():
    FLEET_MAP_PAGE.delete_vehicle_history()


@then('the deleted asset will not be shown in working list')
def assert_delete_vehicle_history():
    assert FLEET_MAP_PAGE.get_working_list_message() == 'There are no vehicles in your working list.'


@when('the user enter the deleted asset name to search it and the user selects the deleted asset from suggestion list')
def add_delete_vehicle():
    FLEET_MAP_PAGE.enter_vehicle_name(FMD.vehicle)
    sleep(2)
    FLEET_MAP_PAGE.select_vehicle_history()
    sleep(2)


@then('the deleted asset will be shown in working list')
def assert_add_delete_vehicle():
    assert FLEET_MAP_PAGE.get_vehicle_name_history() == FMD.vehicle


# LQ-452
@when(
    'the user clicks SETTINGS and clicks "Create Geofence" and draws a shape on Map and enters a Geofence name and clicks "Create"')
def create_geofence():
    # reselect address, geofence and equipment
    options_to_change_dict = {'1': 'Addresses', '2': 'Geofences', '3': 'Equipment'}
    FLEET_MAP_PAGE.click_working_list_filter()
    FLEET_MAP_PAGE.set_working_list_filters(options_to_change_dict)
    sleep(3)

    # clear data
    FLEET_MAP_PAGE.add_geofences_to_working_list_search_result("fence-au")
    FLEET_MAP_PAGE.delete_new_created_geofence(FMD.geofence_name_existing, FMD.geofence_name_by_address)
    FLEET_MAP_PAGE.delete_new_created_geofence(FMD.geofence_name_existing, FMD.geofence_name_by_square)
    FLEET_MAP_PAGE.clear_working_list()
    sleep(1)
    FLEET_MAP_PAGE.create_geofence_by_address("San Diego", FMD.geofence_name_by_address + RANDOM_NAME)
    sleep(3)


@then('the Geofence is added on Map and added to Working List')
def assert_geofence_added():
    assert FLEET_MAP_PAGE.get_geofence_panel_close_button() == "Close"
    assert FLEET_MAP_PAGE.get_geofence_panel_edit_button() == "Edit Geofence"
    assert FLEET_MAP_PAGE.get_geofence_panel_delete_button() == "Delete Geofence"

    geofence_info_dict = FLEET_MAP_PAGE.get_geofence_pin_panel_details()
    assert geofence_info_dict['geofence_name'] == FMD.geofence_name_by_address + RANDOM_NAME
    assert geofence_info_dict['settings'] == "Geofence Trigger Settings"
    assert geofence_info_dict['status'] == "Status: Active"
    assert geofence_info_dict['facing'] == "Facing: Inside"
    assert geofence_info_dict['days'] == "Day(s): Everyday"
    assert geofence_info_dict['time'] == "Time: 24hrs"
    assert_that(geofence_info_dict['vehicles'], contains_string('Vehicles:'))
    # comment this due to side effect of cxfa-4801
    # assert_that(geofence_info_dict['vehicles'], contains_string(FMD.geofence_group))
    assert_that(geofence_info_dict['vehicles'], contains_string('Include Subgroups: Yes'))

    FLEET_MAP_PAGE.close_geofence_pin_panel()

    FLEET_MAP_PAGE.click_working_list()

    working_list_geofence = FLEET_MAP_PAGE.get_working_list_geofence()
    assert working_list_geofence['geofence_name'] == FMD.geofence_name_by_address + RANDOM_NAME
    assert working_list_geofence['status'] == "Status: Active"
    assert working_list_geofence['type'] == "Type: Inside"


# LQ-453
@when(
    'the user clicks "View Details" of a geofence and clicks "Edit Geofence" and changes the shape and changes the Geofence name and clicks "Save"')
def edit_geofence():
    FLEET_MAP_PAGE.view_geofence_detail()
    sleep(2)
    FLEET_MAP_PAGE.click_edit_geofence()
    sleep(4)
    FLEET_MAP_PAGE.change_geofence_shape("Square")
    FLEET_MAP_PAGE.change_geofence_name(FMD.geofence_name_by_square + RANDOM_NAME)
    FLEET_MAP_PAGE.save_geofence_changes()
    sleep(4)


@then('the Geofence shape is updated on Map and the Geofence name is updated in Working List')
def assert_geofence_updated():
    assert FLEET_MAP_PAGE.get_geofence_panel_close_button() == "Close"
    assert FLEET_MAP_PAGE.get_geofence_panel_edit_button() == "Edit Geofence"
    assert FLEET_MAP_PAGE.get_geofence_panel_delete_button() == "Delete Geofence"

    geofence_info_dict = FLEET_MAP_PAGE.get_geofence_pin_panel_details()
    assert geofence_info_dict['geofence_name'] == FMD.geofence_name_by_square + RANDOM_NAME
    assert geofence_info_dict['settings'] == "Geofence Trigger Settings"
    assert geofence_info_dict['status'] == "Status: Active"
    assert geofence_info_dict['facing'] == "Facing: Inside"
    assert geofence_info_dict['days'] == "Day(s): Everyday"
    assert geofence_info_dict['time'] == "Time: 24hrs"
    assert_that(geofence_info_dict['vehicles'], contains_string('Vehicles:'))
    # comment this due to side effect of cxfa-4801
    # assert_that(geofence_info_dict['vehicles'], contains_string(FMD.geofence_group))
    assert_that(geofence_info_dict['vehicles'], contains_string('Include Subgroups: Yes'))

    FLEET_MAP_PAGE.close_geofence_pin_panel()

    working_list_geofence = FLEET_MAP_PAGE.get_working_list_geofence()
    assert working_list_geofence['geofence_name'] == FMD.geofence_name_by_square + RANDOM_NAME
    assert working_list_geofence['status'] == "Status: Active"
    assert working_list_geofence['type'] == "Type: Inside"


# LQ-447 part 2
@when(
    'the user clicks "Clear List" and enters some characters in Search box and the user clicks Search button and the user checks two Geofences and the user clicks "Add to Working List"')
def add_geofences_to_working_list_via_search_result():
    FLEET_MAP_PAGE.add_geofences_to_working_list_search_result("fence-au")


@then('the geofences are displayed in Working List and the geofences are displayed on Map')
def assert_geofences_added_via_search_result():
    working_list_1st_geofence = FLEET_MAP_PAGE.get_working_list_1st_geofence()
    assert working_list_1st_geofence['geofence_name'] == FMD.geofence_name_search
    assert working_list_1st_geofence['status'] == "Status: Active"
    assert working_list_1st_geofence['type'] == "Type: " + FMD.geofence_name_existing_type

    working_list_2nd_geofence = FLEET_MAP_PAGE.get_working_list_2nd_geofence()
    assert working_list_2nd_geofence['geofence_name'] == FMD.geofence_name_by_square + RANDOM_NAME
    assert working_list_2nd_geofence['status'] == "Status: Active"
    assert working_list_2nd_geofence['type'] == "Type: Inside"

    # steps to delete the geo-fences added by script
    FLEET_MAP_PAGE.delete_new_created_geofence(FMD.geofence_name_existing, FMD.geofence_name_by_address)


# LQ-7177
@given('the "Fleet Dispatcher" user is in Fleet Tracking - Map page')
def login_company_with_equipment(browser):
    browser.get(FLEET_URL)
    LOGIN_PAGE.enter_username(FMD.user_name_equipment)
    LOGIN_PAGE.enter_password(FMD.password_equipment)

    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed(FLEET_URL, FMD.user_name_equipment, FMD.password_equipment)
    FLEET_MAP_PAGE.click_map_with_home()


@when(
    'the user clicks on the search text box and the user enters a equipment name and the user selects the equipment from suggestion list')
def add_equipment_to_working_list():
    FLEET_MAP_PAGE.clear_search_box()
    FLEET_MAP_PAGE.clear_working_list()
    FLEET_MAP_PAGE.search_equipment(FMD.equipment)
    FLEET_MAP_PAGE.add_equipment_to_working_list()


@then('the equipment is added into working list and the added equipment can be displayed on map')
def verify_equipment_in_working_list():
    assert FLEET_MAP_PAGE.equipment_is_added_to_working_list() is True
    # assert FLEET_MAP_PAGE.equipment_is_shown_on_map() is True
    assert FLEET_MAP_PAGE.get_equipment_working_list() == FMD.equipment
    # assert FLEET_MAP_PAGE.get_live_pin_equipment_name() == FMD.equipment_map


# LQ-7159
@when('the user selects an equipment from the working list')
def click_equipment_on_working_list():
    FLEET_MAP_PAGE.click_1st_equipment_working_list()


@then('Map is auto zoomed to show the equipment and the equipment is displayed in the map')
def verify_equipment_is_selected():
    assert FLEET_MAP_PAGE.equipment_is_shown_on_map() is True
    assert_that(FLEET_MAP_PAGE.get_1st_equipment_state_working_list(), contains_string('active'))


# LQ-7176
@when('the user clicks an equipment point on map')
def click_equipment_on_map():
    FLEET_MAP_PAGE.click_live_pin_equipment()


@then(
    'equipment details panel should be opened in the left panel and "Equipment Name", "Status", "Group", "Device", Occurrence Time, Time since occurrence, Address, Latitude, Longitude are displayed on pin detail panel')
def verify_equipment_pin_detail():
    equipment_detail_dict = FLEET_MAP_PAGE.get_equipment_live_pin_panel_details()
    assert equipment_detail_dict['equipment_name'] == FMD.equipment
    # comment this due to bug cxfa-3930
    # assert equipment_detail_dict['status'] == 'Status: Active'
    assert equipment_detail_dict['group'] == FMD.equipment_group
    assert equipment_detail_dict['device'] == FMD.equipment_device
    assert equipment_detail_dict['occur_time'] == FMD.equipment_occur_time
    assert_that(equipment_detail_dict['time_since'], contains_string('ago'))
    assert equipment_detail_dict['address'] == FMD.equipment_address
    assert_that(equipment_detail_dict['coordinate'], contains_string(FMD.equipment_coordinate))


# @LQ-112131
@when('the user search asset from search box and the user clicks Search button')
def search_the_asset_in_search_box():
    FLEET_MAP_PAGE.clear_working_list()
    FLEET_MAP_PAGE.search_equipment(FMD.equipment)
    FLEET_MAP_PAGE.search_for_vehicle()


@then('user should able to see matched asset with "+ Working List, Map, check box" options')
def search_result_of_asset():
    assert FLEET_MAP_PAGE.get_equipment_name_text() == FMD.equipment
    FLEET_MAP_PAGE.get_working_list_button_is_diplayed()
    FLEET_MAP_PAGE.get_map_button_is_displayed()
    FLEET_MAP_PAGE.get_check_box_is_displayed()


@when('user search asset from search box and the user clicks Search button and the user clicks "+Working list" button')
def add_the_asset_to_the_working_list():
    FLEET_MAP_PAGE.click_the_working_list_button()


@then('asset is added to the working list with desired details')
def verify_equipment_in_working_list():
    assert FLEET_MAP_PAGE.get_equipment_working_list() == FMD.equipment


@when('user search asset from search box and the user clicks Search button and the user clicks "Map" button')
def asset_map_button():
    FLEET_MAP_PAGE.clear_working_list()
    FLEET_MAP_PAGE.search_equipment(FMD.equipment)
    FLEET_MAP_PAGE.search_for_vehicle()
    FLEET_MAP_PAGE.click_map_button()


@then('asset is centered on map & the desired details of asset is displayed on left panel')
def asset_desired_details():
    equipment_detail_dict = FLEET_MAP_PAGE.get_equipment_live_pin_panel_details()
    assert equipment_detail_dict['equipment_name'] == FMD.equipment





