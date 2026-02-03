from time import sleep

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators.locators_fleet_map_page import LocatorsFleetMap as FML
from pages.base_page import BasePage
from utils.common_util import LocatorUtil


class FleetMapPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Labels
    def get_fleet_tracking_title(self):
        return self.get_text((By.ID, FML.fleet_tracking_title_id))

    def get_pin_panel_close_button(self):
        return self.get_text((By.XPATH, FML.pin_panel_close_xpath))

    def close_geofence_pin_panel(self):
        sleep(2)
        self.click((By.XPATH, FML.geofence_detail_close_xpath))

    def get_pin_panel_address(self):
        return self.get_text((By.XPATH, FML.pin_panel_address_xpath))

    def get_pin_panel_coordinate(self):
        return self.get_text((By.XPATH, FML.pin_panel_coordinate_xpath))

    def get_trip_pin_panel_address(self):
        return self.get_text((By.XPATH, FML.trip_pin_address_xpath))

    def get_trip_pin_panel_coordinate(self):
        return self.get_text((By.XPATH, FML.trip_pin_coordinate_xpath))

    def get_live_pin_panel_details(self):
        i = 0
        while i < 5 and self.get_text((By.XPATH, FML.live_pin_time_since_xpath)) == '':
            sleep(1)
            i += 1

        vehicle_name = self.get_text((By.XPATH, FML.live_pin_vehicle_name_xpath))
        status = self.get_text((By.XPATH, FML.live_pin_status_xpath))
        driver = self.get_text((By.XPATH, FML.live_pin_driver_xpath))
        group = self.get_text((By.XPATH, FML.live_pin_group_xpath))
        device = self.get_text((By.XPATH, FML.live_pin_device_xpath))
        speed = self.get_text((By.XPATH, FML.live_pin_speed_xpath))
        ignition = self.get_text((By.XPATH, FML.live_pin_ignition_xpath))
        occur_time = self.get_text((By.XPATH, FML.live_pin_occur_time_xpath))
        time_since = self.get_text((By.XPATH, FML.live_pin_time_since_xpath))
        # geofence triggering is not shown now, but could not reproducible, comment this for now
        # triggering_geofences = self.get_text((By.XPATH, FML.live_pin_triggering_geofences_xpath))
        triggering_geofences = ""

        panel_detail_dict = {'vehicle_name': vehicle_name, 'status': status, 'driver': driver,
                             'group': group, 'device': device, 'speed': speed,
                             'ignition': ignition, 'triggering_geofences': triggering_geofences,
                             'occur_time': occur_time, 'time_since': time_since}
        return panel_detail_dict

    def get_moving_pin_icon_working_list(self):
        return self.get_attribute((By.XPATH, FML.moving_pin_icon_working_list_xpath), 'src')

    def get_moving_pin_icon_panel_detail(self):
        return self.get_attribute((By.XPATH, FML.moving_pin_icon_panel_detail_xpath), 'src')

    def get_address_icon_panel_detail(self):
        return self.find((By.XPATH, FML.address_icon_panel_detail_xpath))

    def get_date_icon_panel_detail(self):
        return self.find((By.XPATH, FML.date_icon_panel_detail_xpath))

    def add_geofence_to_working_list(self, geofence_name):
        self.load_nothing_in_working_list()
        if self.element_is_displayed((By.XPATH, FML.search_box_xpath)) is False:
            self.click((By.XPATH, FML.map_new_ui_xpath))
        self.type_and_auto_search((By.XPATH, FML.search_box_xpath), geofence_name)
        self.wait_for_expected_text((By.ID, FML.suggestion_list_1st_item_id), geofence_name)
        self.click_element_ignore_exceptions((By.ID, FML.suggestion_list_1st_item_id))

    def add_geofences_to_working_list_search_result(self, geofence_name):
        sleep(1)
        self.click((By.XPATH, FML.clear_working_list_xpath))
        sleep(1)
        self.type((By.XPATH, FML.search_box_xpath), geofence_name)
        sleep(3)
        self.click((By.XPATH, FML.search_icon_xpath))
        sleep(3)
        self.click((By.XPATH, FML.select_all_search_result_xpath))
        sleep(1)
        self.click((By.XPATH, FML.add_to_working_list_xpath))
        sleep(5)

    def add_geofences_to_working_list_search_box(self, geofence_name):
        self.click((By.XPATH, FML.clear_working_list_xpath))
        self.type((By.XPATH, FML.search_box_xpath), geofence_name)
        self.click((By.XPATH, FML.search_icon_xpath))

    def get_title_find_closest_vehicle(self):
        return self.get_text((By.XPATH, FML.title_find_closest_vehicle_xpath))

    def get_coordinates_find_closest_vehicle(self):
        return self.get_text((By.XPATH, FML.coordinates_find_closest_vehicle_xpath))

    def get_address_find_closest_vehicle(self):
        return self.get_text((By.XPATH, FML.address_find_closest_vehicle_xpath))

    def get_1st_vehicle_name_find_closest_vehicle(self):
        return self.get_text((By.XPATH, FML.vehicle_name_1st_closest_vehicle_xpath))

    def get_1st_vehicle_driver_find_closest_vehicle(self):
        return self.get_text((By.XPATH, FML.vehicle_driver_1st_find_closest_vehicle_xpath))

    def get_1st_vehicle_group_find_closest_vehicle(self):
        return self.get_text((By.XPATH, FML.vehicle_group_1st_find_closest_vehicle_xpath))

    def get_1st_vehicle_time_find_closest_vehicle(self):
        return self.get_text((By.XPATH, FML.vehicle_time_1st_find_closest_vehicle_xpath))

    def get_1st_vehicle_distance_find_closest_vehicle(self):
        return self.get_text((By.XPATH, FML.vehicle_distance_1st_find_closest_vehicle_xpath))

    def get_1st_vehicle_delete_find_closest_vehicle(self):
        return self.find((By.ID, FML.delete_1st_vehicle_find_closest_vehicle_id))

    def close_panel_find_closest_vehicle(self):
        sleep(2)
        self.click((By.XPATH, FML.closest_vehicle_panel_close_xpath))

    def click_zoom_in(self):
        self.click((By.XPATH, FML.zoom_in_xpath))

    def click_zoom_out(self):
        self.click((By.XPATH, FML.zoom_out_xpath))

    def click_moving_track_point(self):
        self.wait_for_element_is_clickable((By.XPATH, FML.view_moving_track_point_detail_xpath))
        self.click((By.XPATH, FML.view_moving_track_point_detail_xpath))

    def click_moving_panel_close_button(self):
        self.click((By.XPATH, FML.moving_panel_close_xpath))

    def get_moving_panel_detail(self):
        vehicle_name = self.get_text((By.XPATH, FML.moving_panel_vehicle_name_xpath))
        status = self.get_text((By.XPATH, FML.moving_panel_status_xpath))
        driver = self.get_text((By.XPATH, FML.moving_panel_driver_xpath))
        group = self.get_text((By.XPATH, FML.moving_panel_group_xpath))
        device = self.get_text((By.XPATH, FML.moving_panel_device_xpath))
        occur_time = self.get_text((By.XPATH, FML.moving_panel_occur_time_xpath))
        time_since = self.get_text((By.XPATH, FML.moving_panel_since_time_xpath))
        speed = self.get_text((By.XPATH, FML.moving_panel_speed_xpath))
        address = self.get_text((By.XPATH, FML.moving_panel_address_xpath))
        coordinate = self.get_text((By.XPATH, FML.moving_panel_coordinate_xpath))

        moving_panel_dict = {'vehicle_name': vehicle_name, 'status': status, 'driver': driver,
                             'group': group, 'device': device, 'occur_time': occur_time,
                             'time_since': time_since, 'speed': speed, 'address': address,
                             'coordinate': coordinate}
        return moving_panel_dict

    def google_street_view_is_displayed(self):
        return self.element_is_displayed((By.XPATH, FML.moving_panel_google_street_view_xpath))

    def click_trip_start_pin(self):
        self.click((By.XPATH, FML.view_trip_start_detail_xpath))

    def click_trip_end_pin(self):
        self.click((By.XPATH, FML.view_trip_end_detail_xpath))

    def get_trip_panel_close_button(self):
        return self.get_text((By.XPATH, FML.trip_panel_close_xpath))

    def close_trip_panel(self):
        sleep(2)
        self.click((By.XPATH, FML.trip_panel_close_xpath))

    def get_trip_panel_details(self):
        vehicle_name = self.get_text((By.XPATH, FML.trip_panel_vehicle_name_xpath))
        trip_tag = self.get_text((By.XPATH, FML.trip_tag_xpath))
        driver = self.get_text((By.XPATH, FML.trip_panel_driver_xpath))
        group = self.get_text((By.XPATH, FML.trip_panel_group_xpath))
        device = self.get_text((By.XPATH, FML.trip_panel_device_xpath))
        trip_num = self.get_text((By.XPATH, FML.trip_panel_trip_num_xpath))
        duration = self.get_text((By.XPATH, FML.trip_panel_trip_duration_xpath))
        distance = self.get_text((By.XPATH, FML.trip_panel_distance_xpath))
        max_speed = self.get_text((By.XPATH, FML.trip_panel_max_speed_xpath))
        occur_time = self.get_text((By.XPATH, FML.trip_pin_occur_time_xpath))
        time_since = self.get_text((By.XPATH, FML.trip_pin_time_since_xpath))

        trip_panel_dict = {'vehicle_name': vehicle_name, 'trip_tag': trip_tag,
                           'driver': driver, 'group': group, 'device': device, 'trip_num': trip_num,
                           'duration': duration, 'distance': distance, 'max_speed': max_speed,
                           'occur_time': occur_time, 'time_since': time_since}
        return trip_panel_dict

    def click_speed_violation_pin(self):
        self.click((By.XPATH, FML.view_speed_violation_detail_xpath))

    def get_speed_violation_pin_details(self):
        vehicle_name = self.get_text((By.XPATH, FML.live_pin_vehicle_name_xpath))
        status = self.get_text((By.XPATH, FML.live_pin_status_xpath))
        driver = self.get_text((By.XPATH, FML.live_pin_driver_xpath))
        group = self.get_text((By.XPATH, FML.live_pin_group_xpath))
        device = self.get_text((By.XPATH, FML.live_pin_device_xpath))
        occur_time = self.get_text((By.XPATH, FML.live_pin_occur_time_xpath))
        time_since = self.get_text((By.XPATH, FML.speed_violation_pin_time_since_xpath))
        speed_limit = self.get_text((By.XPATH, FML.speed_violation_pin_speed_limit_xpath))
        max_speed = self.get_text((By.XPATH, FML.speed_violation_pin_max_speed_xpath))
        speed_duration = self.get_text((By.XPATH, FML.speed_violation_pin_duration_xpath))

        panel_detail_dict = {'vehicle_name': vehicle_name, 'status': status, 'driver': driver,
                             'group': group, 'device': device, 'speed_limit': speed_limit,
                             'max_speed': max_speed, 'speed_duration': speed_duration,
                             'occur_time': occur_time, 'time_since': time_since}
        return panel_detail_dict

    def click_idle_violation_pin(self,position):
        self.wait_for_element_is_clickable((By.XPATH,LocatorUtil.give_locator (FML.view_idle_violation_detail_xpath,position)))
        self.click((By.XPATH,LocatorUtil.give_locator (FML.view_idle_violation_detail_xpath,position)))

    def get_idle_violation_pin_details(self):
        vehicle_name = self.get_text((By.XPATH, FML.live_pin_vehicle_name_xpath))
        status = self.get_text((By.XPATH, FML.live_pin_status_xpath))
        driver = self.get_text((By.XPATH, FML.live_pin_driver_xpath))
        group = self.get_text((By.XPATH, FML.live_pin_group_xpath))
        device = self.get_text((By.XPATH, FML.live_pin_device_xpath))
        occur_time = self.get_text((By.XPATH, FML.live_pin_occur_time_xpath))
        time_since = self.get_text((By.XPATH, FML.idle_violation_pin_time_since_xpath))
        idle_duration = self.get_text((By.XPATH, FML.idle_violation_pin_duration_xpath))

        panel_detail_dict = {'vehicle_name': vehicle_name, 'status': status, 'driver': driver,
                             'group': group, 'device': device, 'idle_duration': idle_duration,
                             'occur_time': occur_time, 'time_since': time_since}
        return panel_detail_dict

    def click_geofence_violation_start_pin(self):
        self.click((By.XPATH, FML.view_geofence_violation_start_xpath))

    def get_geofence_violation_start_pin_details(self):
        vehicle_name = self.get_text((By.XPATH, FML.live_pin_vehicle_name_xpath))
        status = self.get_text((By.XPATH, FML.live_pin_status_xpath))
        driver = self.get_text((By.XPATH, FML.live_pin_driver_xpath))
        group = self.get_text((By.XPATH, FML.live_pin_group_xpath))
        device = self.get_text((By.XPATH, FML.live_pin_device_xpath))
        occur_time = self.get_text((By.XPATH, FML.live_pin_occur_time_xpath))
        time_since = self.get_text((By.XPATH, FML.geofence_violation_time_since_xpath))

        panel_detail_dict = {'vehicle_name': vehicle_name, 'status': status, 'driver': driver,
                             'group': group, 'device': device,
                             'occur_time': occur_time, 'time_since': time_since}
        return panel_detail_dict

    def click_geofence_violation_end_pin(self):
        self.click((By.XPATH, FML.view_geofence_violation_end_xpath))

    def get_geofence_violation_end_pin_details(self):
        vehicle_name = self.get_text((By.XPATH, FML.live_pin_vehicle_name_xpath))
        status = self.get_text((By.XPATH, FML.live_pin_status_xpath))
        driver = self.get_text((By.XPATH, FML.live_pin_driver_xpath))
        group = self.get_text((By.XPATH, FML.live_pin_group_xpath))
        device = self.get_text((By.XPATH, FML.live_pin_device_xpath))
        duration = self.get_text((By.XPATH, FML.geofence_violation_duration_xpath))
        occur_time = self.get_text((By.XPATH, FML.live_pin_occur_time_xpath))
        time_since = self.get_text((By.XPATH, FML.geofence_violation_time_since_xpath))

        panel_detail_dict = {'vehicle_name': vehicle_name, 'status': status, 'driver': driver,
                             'group': group, 'device': device, 'duration': duration,
                             'occur_time': occur_time, 'time_since': time_since}
        return panel_detail_dict

    def view_geofence_detail(self):
        self.click((By.XPATH, FML.view_geofence_detail_xpath))

    def click_delete_geofence(self):
        self.click((By.XPATH, FML.geofence_detail_delete_xpath))

    def confirm_delete_geofence(self):
        self.click((By.ID, FML.confirm_delete_id))

    def delete_new_created_geofence(self, retained_geofence, geofence_to_be_deleted):
        count = len(self.find_elements((By.ID, FML.delete_icon_id)))
        i = 0
        while i < count:
            if i == count - 1:
                last_geofence_name_xpath = FML.working_list_geofence_name_1st_xpath
                last_geofence_view_detail_xpath = FML.view_geofence_detail_xpath
            else:
                last_geofence_name_xpath = FML.working_list_geofence_prefix + str(count - i) \
                                           + FML.working_list_geofence_name_suffix
                last_geofence_view_detail_xpath = FML.working_list_geofence_prefix + str(count - i) \
                                                  + FML.working_list_geofence_view_detail_suffix
            if retained_geofence not in self.get_text((By.XPATH, last_geofence_name_xpath)) and \
                    geofence_to_be_deleted in self.get_text((By.XPATH, last_geofence_name_xpath)):
                self.click((By.XPATH, last_geofence_view_detail_xpath))
                self.click_delete_geofence()
                self.confirm_delete_geofence()
                sleep(2)

            i += 1

    def get_geofence_panel_close_button(self):
        self.wait_for_element_is_clickable((By.XPATH, FML.geofence_detail_close_xpath))
        return self.get_text((By.XPATH, FML.geofence_detail_close_xpath))

    def get_geofence_pin_panel_details(self):
        self.element_is_displayed((By.XPATH, FML.geofence_detail_name_xpath))
        sleep(2)

        geofence_name = self.get_text((By.XPATH, FML.geofence_detail_name_xpath))
        settings = self.get_text((By.XPATH, FML.geofence_detail_setting_xpath))
        status = self.get_text((By.XPATH, FML.geofence_detail_status_xpath))
        facing = self.get_text((By.XPATH, FML.geofence_detail_facing_xpath))
        days = self.get_text((By.XPATH, FML.geofence_detail_days_xpath))
        time = self.get_text((By.XPATH, FML.geofence_detail_time_xpath))
        vehicles = self.get_text((By.XPATH, FML.geofence_detail_vehicles_xpath))

        panel_detail_dict = {'geofence_name': geofence_name, 'settings': settings, 'status': status,
                             'facing': facing, 'days': days, 'time': time, 'vehicles': vehicles}
        return panel_detail_dict

    def get_geofence_panel_edit_button(self):
        return self.get_text((By.XPATH, FML.geofence_detail_edit_xpath))

    def get_geofence_panel_delete_button(self):
        return self.get_text((By.XPATH, FML.geofence_detail_delete_xpath))

    def get_create_geofence_label(self):
        return self.get_text((By.ID, FML.geofence_label_id))

    def get_vehicle_name(self):
        self.wait_for_element_displayed((By.XPATH, FML.vehicle_name_label_xpath))
        return self.get_text((By.XPATH, FML.vehicle_name_label_xpath))

    # live pins
    def get_live_vehicle_pin(self):
        return self.find((By.XPATH, FML.live_map_pin_xpath))

    def check_live_map_refreshed(self, live_vehicle_pin):
        refresh = False
        wait_time: int = 0
        try:
            while wait_time < 30:
                live_vehicle_pin.get_attribute("aria-label")
                wait_time += 1
                sleep(1)
        except (StaleElementReferenceException, WebDriverException):
            refresh = True

        return refresh

    def get_live_pin_vehicle_name(self):
        vehicle_name = None
        wait_time: int = 0
        while vehicle_name is None:
            try:
                # live pin refreshes automatically, we need to re-capture the web element
                vehicle_name = self.get_attribute((By.XPATH, FML.live_map_pin_xpath), "aria-label")
            except (StaleElementReferenceException, TimeoutException):
                vehicle_name = None

            sleep(2)
            wait_time += 1
            if wait_time == 10:
                break

        return vehicle_name

    # history pins
    def click_vehicle_pin(self):
        self.click((By.XPATH, FML.live_map_pin_xpath))

    def close_map_pin_panel(self):
        self.wait_for_element_is_clickable((By.XPATH, FML.pin_panel_close_xpath))
        self.click((By.XPATH, FML.pin_panel_close_xpath))

    def get_trip_start_on_map(self):
        attempts = 0
        while attempts < 5:
            try:
                return self.get_attribute((By.XPATH, FML.trip_start_map_xpath), "src")
            except StaleElementReferenceException:
                sleep(1)
                attempts += 1

        return self.get_attribute((By.XPATH, FML.trip_start_map_xpath), "src")

    def get_trip_end_on_map(self):
        attempts = 0
        while attempts < 5:
            try:
                return self.get_attribute((By.XPATH, FML.trip_end_map_xpath), "src")
            except StaleElementReferenceException:
                sleep(1)
                attempts += 1

        return self.get_attribute((By.XPATH, FML.trip_end_map_xpath), "src")

    def get_trip_on_working_list(self):
        return self.get_attribute((By.ID, FML.trip_icon_id), "src")

    def get_route_on_working_list(self):
        return self.get_attribute((By.ID, FML.routes_icon_id), "src")

    # create geofence
    def create_geofence_by_address(self, address, geofence_name):
        # self.click((By.XPATH, FML.clear_working_list_xpath))
        self.click((By.XPATH, FML.settings_tab_xpath))
        sleep(1)
        self.click((By.ID, FML.create_geofence_settings_id))
        sleep(1)
        self.change_geofence_shape('Use Address')
        self.type((By.ID, FML.geofence_location_id), address)
        sleep(5)
        self.type((By.ID, FML.geofence_location_id), Keys.ARROW_DOWN)
        sleep(1)
        self.type((By.ID, FML.geofence_location_id), Keys.ENTER)
        self.type((By.ID, FML.geofence_name_id), geofence_name)
        self.type((By.ID, FML.geofence_name_id), Keys.PAGE_DOWN)
        self.click((By.XPATH, FML.create_geofence_save_xpath))

    # edit geofence
    def click_edit_geofence(self):
        self.click((By.XPATH, FML.geofence_detail_edit_xpath))

    def change_geofence_shape(self, shape):
        if shape == 'Circle':
            self.click((By.XPATH, FML.geofence_shape_circle_xpath))

        if shape == 'Square':
            self.click((By.XPATH, FML.geofence_shape_square_xpath))

        if shape == 'Custom':
            self.click((By.XPATH, FML.geofence_shape_custom_xpath))

        if shape == 'Use Address':
            self.click((By.XPATH, FML.geofence_shape_use_address_xpath))

    def change_geofence_name(self, geofence_name):
        self.clear((By.ID, FML.geofence_name_id))
        self.type((By.ID, FML.geofence_name_id), geofence_name)

    def save_geofence_changes(self):
        self.click((By.XPATH, FML.create_geofence_save_xpath))

    # Actions
    def click_map(self):
        self.click((By.XPATH, FML.map_xpath))

    def click_map_new_ui(self):
        self.click((By.XPATH, FML.map_new_ui_xpath))

    def map_tab_is_displayed(self):
        refresh_attempts = 0
        while not self.element_is_displayed((By.XPATH, FML.map_xpath)) and refresh_attempts < 3:
            self.click_refresh_button()
            refresh_attempts += 1
        return self.wait_for_element_displayed((By.XPATH, FML.map_xpath))

    def map_tab_is_displayed_new_UI(self):
        refresh_attempts = 0
        while not self.element_is_displayed((By.XPATH, FML.map_new_ui_xpath)) and refresh_attempts < 3:
            self.click_refresh_button()
            refresh_attempts += 1
        return self.wait_for_element_displayed((By.XPATH, FML.map_new_ui_xpath))

    def click_map_with_home(self):
        self.click((By.XPATH, FML.map_with_home_xpath))

    def click_history_button(self):
        self.click((By.ID, FML.history_selector_id))

    def set_history_date_range(self, start_month, start_day, start_year, end_month, end_day, end_year):
        self.click((By.XPATH, FML.date_range_start_month_xpath))
        self.type((By.XPATH, FML.date_range_start_month_xpath), start_month)
        self.click((By.XPATH, FML.date_range_start_day_xpath))
        self.type((By.XPATH, FML.date_range_start_day_xpath), start_day)
        self.click((By.XPATH, FML.date_range_start_year_xpath))
        self.type((By.XPATH, FML.date_range_start_year_xpath), start_year)
        self.click((By.XPATH, FML.date_range_end_month_xpath))
        self.type((By.XPATH, FML.date_range_end_month_xpath), end_month)
        self.click((By.XPATH, FML.date_range_end_day_xpath))
        self.type((By.XPATH, FML.date_range_end_day_xpath), end_day)
        self.click((By.XPATH, FML.date_range_end_year_xpath))
        self.type((By.XPATH, FML.date_range_end_year_xpath), end_year)

    def click_apply_button(self):
        self.click((By.ID, FML.apply_button_id))

    def click_working_list(self):
        self.click((By.XPATH, FML.working_list_tab_xpath))

    def clear_working_list(self):
        self.click((By.XPATH, FML.clear_working_list_xpath))

    def load_nothing_in_working_list(self):
        self.click((By.XPATH, FML.settings_tab_xpath))
        self.click((By.XPATH, FML.settings_load_no_vehicle))
        self.click((By.XPATH, FML.settings_load_no_equipment))
        self.click((By.XPATH, FML.settings_load_no_geofence))
        self.click_refresh_button()

    def enter_vehicle_name(self, vehicle):
        self.type_and_auto_search((By.XPATH, FML.search_box_xpath), vehicle)

    def search_for_vehicle(self):
        self.click((By.XPATH, FML.search_icon_xpath))

    def select_vehicle(self):
        self.click((By.XPATH, FML.select_vehicle_xpath))

    def select_vehicle_from_suggestion_list(self):
        self.click_element_ignore_exceptions((By.ID, FML.suggestion_list_1st_item_id))

    def add_address_in_working_list(self, address):
        self.type_and_auto_search((By.XPATH, FML.search_box_xpath), address)
        self.wait_for_expected_text((By.ID, FML.suggestion_list_1st_item_id), address)
        self.click_element_ignore_exceptions((By.ID, FML.suggestion_list_1st_item_id))


    def add_to_working_list(self):
        self.click((By.XPATH, FML.add_to_working_list_xpath))

    def click_settings(self):
        self.click((By.XPATH, FML.settings_tab_xpath))

    def click_create_geofence(self):
        self.click((By.ID, FML.geofence_label_id))

    def click_geofence_cancel_button(self):
        self.click((By.ID, FML.cancel_button_id))

    def click_speed_icon(self):
        self.wait_for_element_is_clickable((By.ID, FML.speed_icon_id))
        self.click((By.ID, FML.speed_icon_id))

    def click_idle_icon(self):
        self.wait_for_element_is_clickable((By.ID, FML.idle_icon_id))
        self.click((By.ID, FML.idle_icon_id))

    def click_geofence_icon(self):
        self.click((By.ID, FML.geofence_icon_id))

    def click_trip_icon(self):
        self.click((By.ID, FML.trip_icon_id))

    def click_routes_icon(self):
        self.click((By.ID, FML.routes_icon_id))

    def click_view_detail_address(self):
        self.click((By.XPATH, FML.view_detail_address_xpath))

    def click_find_closest_vehicle(self):
        self.click((By.XPATH, FML.find_closest_vehicle_xpath))

    def click_last_4_hours_history(self):
        self.click((By.XPATH, FML.last_4_hours_xpath))

    def click_working_list_filter(self):
        self.click((By.XPATH, FML.working_list_filter_xpath))

    def close_working_list_filter(self):
        self.click((By.XPATH, FML.close_working_list_filter_xpath))

    def set_working_list_filters(self, options_to_change_dict):
        for key in options_to_change_dict:
            self.click((By.ID, FML.working_list_filter_prefix + key))

    def get_vehicle_name_history(self):
        return self.get_text((By.XPATH, FML.vehicle_name_in_history_xpath))

    def delete_vehicle_history(self):
        self.click((By.XPATH, FML.delete_vehicle_history_xpath))

    # working list elements
    def get_working_list_geofence(self):
        self.wait_for_element_displayed((By.XPATH, FML.working_list_geofence_name_xpath))
        geofence_name = self.get_text((By.XPATH, FML.working_list_geofence_name_xpath))
        status = self.get_text((By.XPATH, FML.working_list_geofence_status_xpath))
        type = self.get_text((By.XPATH, FML.working_list_geofence_type_xpath))

        working_list_geofence_dict = {'geofence_name': geofence_name,
                                      'status': status, 'type': type, }
        return working_list_geofence_dict

    def get_working_list_1st_geofence(self):
        geofence_name = self.get_text((By.XPATH, FML.working_list_geofence_name_1st_xpath))
        status = self.get_text((By.XPATH, FML.working_list_geofence_status_1st_xpath))
        type = self.get_text((By.XPATH, FML.working_list_geofence_type_1st_xpath))

        working_list_geofence_dict = {'geofence_name': geofence_name,
                                      'status': status, 'type': type, }
        return working_list_geofence_dict

    def get_working_list_2nd_geofence(self):
        geofence_name = self.get_text((By.XPATH, FML.working_list_geofence_name_2nd_xpath))
        status = self.get_text((By.XPATH, FML.working_list_geofence_status_2nd_xpath))
        type = self.get_text((By.XPATH, FML.working_list_geofence_type_2nd_xpath))

        working_list_geofence_dict = {'geofence_name': geofence_name,
                                      'status': status, 'type': type, }
        return working_list_geofence_dict

    # when there is only one message, use get_working_list_message
    def get_working_list_message(self):
        return self.get_text((By.XPATH, FML.working_list_message))

    # when there are multiple messages in working list, use get_working_list_message_x
    # those get_working_list_message_x are not used for now
    def get_working_list_message_one(self):
        return self.get_text((By.XPATH, FML.working_list_message_one))

    def get_working_list_message_two(self):
        return self.get_text((By.XPATH, FML.working_list_message_two))

    def get_working_list_message_three(self):
        return self.get_text((By.XPATH, FML.working_list_message_three))

    def get_working_list_message_four(self):
        return self.get_text((By.XPATH, FML.working_list_message_four))

    def get_working_list_message_five(self):
        return self.get_text((By.XPATH, FML.working_list_message_five))

    def get_working_list_message_six(self):
        return self.get_text((By.XPATH, FML.working_list_message_six))

    def get_working_list_message_seven(self):
        return self.get_text((By.XPATH, FML.working_list_message_seven))

    def select_vehicle_history(self):
        self.click((By.XPATH, FML.select_vehicle_in_history_xpath))

    def search_equipment(self, equipment_name):
        self.type_and_auto_search((By.XPATH, FML.search_box_xpath), equipment_name)
        self.wait_for_expected_text((By.ID, FML.suggestion_list_1st_item_id), equipment_name)

    def add_equipment_to_working_list(self):
        self.click_element_ignore_exceptions((By.ID, FML.suggestion_list_1st_item_id))

    def equipment_is_added_to_working_list(self):
        self.wait_for_element_displayed((By.XPATH, FML.equipment_working_list_xpath))
        return self.element_is_displayed((By.XPATH, FML.equipment_working_list_xpath))

    def equipment_is_shown_on_map(self):
        self.wait_for_element_displayed((By.XPATH, FML.equipment_live_map_xpath))
        return self.element_is_displayed((By.XPATH, FML.equipment_live_map_xpath))

    def get_equipment_working_list(self):
        return self.get_text((By.XPATH, FML.equipment_working_list_xpath))

    def click_1st_equipment_working_list(self):
        self.click((By.XPATH, FML.equipment_working_list_xpath))

    def get_1st_equipment_state_working_list(self):
        return self.get_attribute((By.XPATH, FML.equipment_state_working_list_xpath), 'class')

    def get_live_pin_equipment_name(self):
        equipment_name = None
        wait_time: int = 0
        while equipment_name is None:
            try:
                # live pin refreshes automatically, we need to re-capture the web element
                equipment_name = self.get_attribute((By.XPATH, FML.equipment_live_map_xpath), "aria-label")
            except (StaleElementReferenceException, TimeoutException):
                equipment_name = None

            sleep(2)
            wait_time += 1
            if wait_time == 20:
                break

        return equipment_name

    def click_live_pin_equipment(self):
        try:
            self.wait_for_element_is_clickable((By.XPATH, FML.equipment_live_map_xpath))
        except(StaleElementReferenceException):
            sleep(2)
            self.wait_for_element_is_clickable((By.XPATH, FML.equipment_live_map_xpath))
        self.click_element_ignore_exceptions((By.XPATH, FML.equipment_live_map_xpath))

    def get_equipment_live_pin_panel_details(self):
        i = 0
        while i < 5 and self.get_text((By.XPATH, FML.live_pin_equipment_time_since_xpath)) == '':
            sleep(1)
            i += 1

        equipment_name = self.get_text((By.XPATH, FML.live_pin_equipment_name_xpath))
        status = self.get_text((By.XPATH, FML.live_pin_equipment_status_xpath))
        group = self.get_text((By.XPATH, FML.live_pin_equipment_group_xpath))
        device = self.get_text((By.XPATH, FML.live_pin_equipment_device_xpath))
        occur_time = self.get_text((By.XPATH, FML.live_pin_equipment_occur_time_xpath))
        time_since = self.get_text((By.XPATH, FML.live_pin_equipment_time_since_xpath))
        address = self.get_text((By.XPATH, FML.live_pin_equipment_address_xpath))
        coordinate = self.get_text((By.XPATH, FML.live_pin_equipment_coordinate_since_xpath))

        panel_detail_dict = {'equipment_name': equipment_name, 'status': status, 'group': group,
                             'device': device, 'occur_time': occur_time, 'time_since': time_since,
                             'address': address, 'coordinate': coordinate}
        return panel_detail_dict

    def get_working_list_button_is_diplayed(self):
        return self.element_is_displayed((By.XPATH, FML.working_list_button_xpath))

    def get_map_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, FML.map_button_xpath))

    def get_check_box_is_displayed(self):
        return self.element_is_displayed((By.XPATH, FML.check_box_button_xpath))

    def click_the_working_list_button(self):
        self.click((By.XPATH, FML.working_list_button_xpath))

    def click_map_button(self):
        self.click((By.XPATH, FML.map_button_xpath))

    def get_geofence_name_text(self):
        return self.get_text((By.XPATH, FML.name_text_xpath))

    def clear_search_box(self):
        self.clear((By.XPATH, FML.search_box_xpath))

    def get_vehicle_name_text(self):
        return self.get_text((By.XPATH, FML.name_text_xpath))

    def get_equipment_name_text(self):
        return self.get_text((By.XPATH, FML.name_text_xpath))

    def get_settings_tab_text(self):
        return self.get_text((By.XPATH, FML.settings_tab_xpath))

    def click_left_faced_arrow(self):
        self.click((By.XPATH, FML.left_faced_arrow_xpath))

    def get_left_navigation_collapsed(self):
        return self.element_is_displayed((By.XPATH, FML.left_navigation_collapsed_xpath))

    def click_right_faced_arrow(self):
        self.click((By.XPATH, FML.right_faced_arrow_xpath))

    def get_left_navigation_expanded(self):
        return self.element_is_displayed((By.XPATH, FML.left_navigation_expanded_xpath))