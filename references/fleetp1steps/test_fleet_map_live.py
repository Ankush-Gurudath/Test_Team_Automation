from time import sleep

from hamcrest import assert_that, contains_string
from pytest_bdd import scenarios, given, when, then

from references.fleetpages.address_detail_panel import AddressDetailPanel
from references.fleetpages.find_closest_vehicle_panel import FindClosestVehiclePanel
from references.fleetpages.map_live_page import MapLivePage
from references.loginpages.fleet_login_page import FleetLoginPage
from steps.common import AutomationDataManager, FLEET_URL, TestDataEnum

FLEET_LOGIN_PAGE = 0
MAP_LIVE_PAGE = 0
ADDRESS_DETAIL_PANEL = 0
FIND_CLOSEST_VEHICLE_PANEL = 0
FLEET_TEST_DATA = [TestDataEnum.ENABLE_FUEL_MGMT_UI_TRUE,
                   TestDataEnum.SHOW_IDLE_VIOLATION_TRUE,
                   TestDataEnum.ENABLE_FLEET_PM_TRUE,
                   TestDataEnum.ENABLE_ASSET_TRACKING_TRUE,
                   TestDataEnum.ALLOW_AVL_TRUE,
                   TestDataEnum.VEHICLE,
                   TestDataEnum.DEVICE,
                   TestDataEnum.DRIVER,
                   TestDataEnum.FLEET_DISPATCHER,
                   TestDataEnum.FLEET_TRACKING_DATA]

scenarios('../../features/FLeetP1/map_live.feature')


# LQ-444 FT_Smoke_Map_Live_Set Vehicle And Geofence Visibility
@given('"Fleet Dispatcher" user is in Fleet Tracking')
def login_fleet_page(browser):
    global FLEET_LOGIN_PAGE, MAP_LIVE_PAGE, ADDRESS_DETAIL_PANEL, FIND_CLOSEST_VEHICLE_PANEL

    FLEET_LOGIN_PAGE = FleetLoginPage(browser)
    MAP_LIVE_PAGE = MapLivePage(browser)
    ADDRESS_DETAIL_PANEL = AddressDetailPanel(browser)
    FIND_CLOSEST_VEHICLE_PANEL = FindClosestVehiclePanel(browser)
    browser.get(FLEET_URL)

    tadm = AutomationDataManager()
    tadm.create_test_credentials(FLEET_TEST_DATA)
    FLEET_LOGIN_PAGE.enter_username(tadm.fd_login)
    FLEET_LOGIN_PAGE.enter_password("Login123!")
    sleep(20)  # We need to pause here so the login created by the API actually exists in the db.

    FLEET_LOGIN_PAGE.click_login()


@when('the user clicks toggle of a vehicle in Working List')
def toggle_off_vehicle():
    MAP_LIVE_PAGE.wait_for_fleet_tracking_page_loaded()
    MAP_LIVE_PAGE.wait_for_working_list_loaded(2)
    MAP_LIVE_PAGE.clear_working_list()

    MAP_LIVE_PAGE.working_list_search("TestVehicle")
    MAP_LIVE_PAGE.select_suggestion_list_1st_item("TestVehicle")
    MAP_LIVE_PAGE.click_working_list_1st_item_toggle()


@then('the vehicle is not displayed on Map')
def verify_vehicle_not_displayed():
    assert MAP_LIVE_PAGE.vehicle_pin_is_displayed() is False


@when('the user clicks toggle of a Geofence in Working List')
def toggle_off_geofence():
    MAP_LIVE_PAGE.working_list_search("GeoFence-")
    MAP_LIVE_PAGE.select_suggestion_list_1st_item("GeoFence-")
    MAP_LIVE_PAGE.click_working_list_2nd_item_toggle()


@then('the Geofence is not displayed on Map')
def verify_geofence_not_displayed():
    assert MAP_LIVE_PAGE.geofence_pin_is_displayed() is False


# LQ-513 Remove & add vehicle in Closest Vehicles page
@given('the "Fleet Dispatcher" user is in Closest Vehicles page')
def open_closest_vehicle_page():
    MAP_LIVE_PAGE.click_working_list_1st_item_toggle()
    MAP_LIVE_PAGE.working_list_search("San Diego, CA, USA")
    MAP_LIVE_PAGE.select_suggestion_list_1st_item("San Diego, CA, USA")
    MAP_LIVE_PAGE.click_view_address_detail()

    ADDRESS_DETAIL_PANEL.click_find_closest_vehicle()


@when('the user clicks on the trash icon after a vehicle in Closest Vehicles list')
def click_trash_on_find_closest_vehicle_panel():
    FIND_CLOSEST_VEHICLE_PANEL.click_trash_icon_1st()


@then('the vehicle is removed from Closest Vehicles list and the route of the vehicle is removed from map')
def verify_vehicle_removed_from_list():
    assert FIND_CLOSEST_VEHICLE_PANEL.vehicle_name_1st_is_displayed() is False
    assert FIND_CLOSEST_VEHICLE_PANEL.trash_icon_1st_is_displayed() is False
    assert MAP_LIVE_PAGE.closest_vehicle_estimate_time_is_displayed() is False


@when('the user clicks on another vehicle pin')
def add_vehicle_to_closest_vehicle_list():
    MAP_LIVE_PAGE.click_vehicle_pin_closest_vehicle()


@then(
    'the vehicle is added to Closest Vehicles list and the vehicle is highlighted in Closest Vehicles list and the route of the vehicle is highlighted on map')
def verify_vehicle_added_to_list():
    assert FIND_CLOSEST_VEHICLE_PANEL.vehicle_name_1st_is_displayed() is True
    assert FIND_CLOSEST_VEHICLE_PANEL.trash_icon_1st_is_displayed() is True
    assert MAP_LIVE_PAGE.closest_vehicle_estimate_time_is_displayed() is True
    assert FIND_CLOSEST_VEHICLE_PANEL.vehicle_1st_is_selected() is True


# LQ-448 Search Wild Card
@when('the user clicks on Search box and the user clicks All')
def search_wild_card_all():
    FIND_CLOSEST_VEHICLE_PANEL.close_panel()
    ADDRESS_DETAIL_PANEL.close_panel()
    MAP_LIVE_PAGE.clear_working_list()
    MAP_LIVE_PAGE.working_list_search("All")
    MAP_LIVE_PAGE.select_suggestion_list_1st_item("All")
    MAP_LIVE_PAGE.search_result_select_all()
    MAP_LIVE_PAGE.search_result_add_to_working_list()


@then('all vehicles and geofences are displayed in Search Panel')
def verify_wild_card_all():
    MAP_LIVE_PAGE.wait_for_working_list_loaded(2)
    assert_that(MAP_LIVE_PAGE.working_list_1st_item_name(), contains_string('TestVehicle'))
    assert MAP_LIVE_PAGE.working_list_1st_item_driver() == "Driver: Unassigned"
    assert_that(MAP_LIVE_PAGE.working_list_1st_item_group(), contains_string('TestCompany'))

    assert_that(MAP_LIVE_PAGE.working_list_2nd_item_name(), contains_string('GeoFence-'))
    assert MAP_LIVE_PAGE.working_list_2nd_item_status() == "Status: Active"
    assert MAP_LIVE_PAGE.working_list_2nd_item_type() == "Type: Inside"


@when('the user clicks on Search box and the user clicks All Vehicles')
def search_wild_card_all_vehicles():
    MAP_LIVE_PAGE.clear_working_list()
    MAP_LIVE_PAGE.working_list_search("All Vehicles")
    MAP_LIVE_PAGE.select_suggestion_list_1st_item("All Vehicles")
    MAP_LIVE_PAGE.search_result_select_all()
    MAP_LIVE_PAGE.search_result_add_to_working_list()


@then('all vehicles are displayed in Search Panel')
def verify_wild_card_all_vehicles():
    MAP_LIVE_PAGE.wait_for_working_list_loaded(1)
    assert_that(MAP_LIVE_PAGE.working_list_1st_item_name(), contains_string('TestVehicle'))
    assert MAP_LIVE_PAGE.working_list_1st_item_driver() == "Driver: Unassigned"
    assert_that(MAP_LIVE_PAGE.working_list_1st_item_group(), contains_string('TestCompany'))


@when('the user clicks on Search box and the user clicks All Geofences')
def search_wild_card_all_geofences():
    MAP_LIVE_PAGE.clear_working_list()
    MAP_LIVE_PAGE.working_list_search("All Geofences")
    MAP_LIVE_PAGE.select_suggestion_list_1st_item("All Geofences")
    MAP_LIVE_PAGE.search_result_select_all()
    MAP_LIVE_PAGE.search_result_add_to_working_list()


@then('all geofences are displayed in Search Panel')
def verify_wild_card_all_geofences():
    MAP_LIVE_PAGE.wait_for_working_list_loaded(1)
    assert_that(MAP_LIVE_PAGE.working_list_1st_item_name(), contains_string('GeoFence-'))
    assert MAP_LIVE_PAGE.working_list_1st_item_status() == "Status: Active"
    assert MAP_LIVE_PAGE.working_list_1st_item_type() == "Type: Inside"


@when('the user clicks on Search box and the user clicks All Nearby Vehicles')
def search_wild_card_all_nearby_vehicles():
    MAP_LIVE_PAGE.clear_working_list()
    MAP_LIVE_PAGE.working_list_search("All Nearby Vehicles")
    MAP_LIVE_PAGE.select_suggestion_list_1st_item("All Nearby Vehicles")
    MAP_LIVE_PAGE.search_result_select_all()
    MAP_LIVE_PAGE.search_result_add_to_working_list()


@then('all nearby vehicles are displayed in Search Panel')
def verify_wild_card_all_nearby_vehicles():
    MAP_LIVE_PAGE.wait_for_working_list_loaded(1)
    assert_that(MAP_LIVE_PAGE.working_list_1st_item_name(), contains_string('TestVehicle'))
    assert MAP_LIVE_PAGE.working_list_1st_item_driver() == "Driver: Unassigned"
    assert_that(MAP_LIVE_PAGE.working_list_1st_item_group(), contains_string('TestCompany'))
