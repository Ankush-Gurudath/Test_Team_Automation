from datetime import datetime, timedelta
from enum import Enum
from time import sleep

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators.locators_fleet_insights_page import LocatorsFleetInsights as FIL
from pages.base_page import BasePage
from utils.common_util import LocatorUtil


class FleetInsightEquipmentStatusAssetType(Enum):
    Equipment = 1
    Device = 2


class FleetInsightsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_apply_button(self):
        self.click((By.ID, FIL.apply_button_id))

    # Labels
    def get_fleet_tracking_title(self):
        return self.get_text((By.ID, FIL.fleet_tracking_title_id))

    # Insights
    def click_insights(self):
        self.click((By.XPATH, FIL.insights_xpath))

    def click_insights_new_ui(self):
        self.click((By.XPATH, FIL.insights_new_ui_xpath))

    def click_insights_dycom(self):
        self.element_is_displayed((By.XPATH, FIL.insights_dycom_xpath))
        self.click((By.XPATH, FIL.insights_dycom_xpath))

    def click_fleet_operations(self):
        self.click((By.XPATH, FIL.fleet_operations_xpath))

    def click_fleet_operations_new_ui(self):
        self.click((By.XPATH, FIL.fleet_operations_new_ui_xpath))

    def click_fleet_operations_vehicles(self):
        self.click((By.XPATH, FIL.vehicles_tab_xpath))

    def click_fleet_operations_drivers(self):
        self.element_is_displayed((By.XPATH, FIL.drivers_tab_xpath))
        self.click((By.XPATH, FIL.drivers_tab_xpath))

    def click_equipment_status(self):
        self.click((By.XPATH, FIL.equipment_status_xpath))

    def click_equipment_status_new_ui(self):
        self.click((By.XPATH, FIL.equipment_status_new_ui_xpath))

    def click_geofences(self):
        self.click((By.XPATH, FIL.geofences_xpath))

    def click_state_mileage(self):
        self.click((By.XPATH, FIL.state_mileage_xpath))

    def click_state_mileage_new_ui(self):
        self.click((By.XPATH, FIL.state_mileage_new_ui_xpath))

    def click_data_export(self):
        self.click((By.XPATH, FIL.data_export_xpath))

    def click_data_export_new_ui(self):
        self.click((By.XPATH, FIL.data_export_new_ui_xpath))

    def click_fleet_data(self):
        self.click((By.XPATH, FIL.fleet_data_xpath))

    def click_fleet_data_new_ui(self):
        self.click((By.XPATH, FIL.fleet_data_new_ui_xpath))

    def get_fleet_operations_title(self):
        self.wait_for_element_displayed((By.XPATH, FIL.fleet_operations_title_xpath))
        return self.get_text((By.XPATH, FIL.fleet_operations_title_xpath))

    def get_fleet_operations_groups_tab(self):
        return self.get_text((By.XPATH, FIL.groups_tab_text_xpath))

    def get_fleet_operations_vehicles_tab(self):
        return self.get_text((By.XPATH, FIL.vehicles_tab_xpath))

    def get_fleet_operations_drivers_tab(self):
        self.wait_for_element_displayed((By.XPATH, FIL.drivers_tab_xpath))
        return self.get_text((By.XPATH, FIL.drivers_tab_xpath))

    def click_filter_group_group(self):
        self.click((By.XPATH, FIL.group_filter_button_group_xpath))

    def click_filter_group_vehicle(self):
        self.click((By.XPATH, FIL.group_filter_button_vehicle_xpath))

    def click_filter_group_driver(self):
        self.click((By.XPATH, FIL.group_filter_button_driver_xpath))

    def search_filter_group(self, search_text):
        self.type((By.XPATH, FIL.search_by_group_textbox_xpath), search_text)
    
    def select_group_from_search_filter_suggestion_list(self):
        self.click((By.XPATH, FIL.select_search_button_xpath))

    def click_done(self):
        self.click((By.XPATH, FIL.done_button_xpath))

    def select_date_filter_vehicle(self):
        self.click((By.XPATH, FIL.date_filter_vehicle_xpath))

    def select_date_filter_group(self):
        self.click((By.XPATH, FIL.date_filter_group_xpath))

    def select_date_filter_driver(self):
        self.click((By.XPATH, FIL.date_filter_driver_xpath))

    def select_from_date_group(self):
        self.click((By.XPATH, FIL.from_date_group_xpath))

    def select_end_date_group(self):
        self.click((By.XPATH, FIL.end_date_group_xpath))

    def select_from_date_vehicle(self):
        self.click((By.XPATH, FIL.from_date_vehicle_xpath))

    def select_end_date_vehicle(self):
        self.click((By.XPATH, FIL.end_date_vehicle_xpath))

    def select_last_90_days_vehicle(self):
        self.click((By.XPATH, FIL.last_90_days_vehicle_xpath))

    def select_from_date_driver(self):
        self.click((By.XPATH, FIL.from_date_driver_xpath))

    def select_end_date_driver(self):
        self.click((By.XPATH, FIL.end_date_driver_xpath))

    def select_last_90_days_driver(self):
        self.click((By.XPATH, FIL.last_90_days_driver_xpath))

    def click_apply(self):
        self.click((By.ID, FIL.apply_button_id))

    def click_reset_driver_tab(self):
        self.click((By.XPATH, FIL.reset_driver_tab_button_xpath))

    def click_driver_name(self):
        self.click((By.XPATH, FIL.driver_name_xpath))

    # Driver profile assertions
    def get_driver_profile_page_title(self):
        return self.get_text((By.XPATH, FIL.driver_profile_title_text_xpath))

    def get_driver_name_text_driver_profile(self):
        self.wait_for_element_displayed((By.XPATH, FIL.driver_name_text_driver_profile_xpath))
        return self.get_text((By.XPATH, FIL.driver_name_text_driver_profile_xpath))

    def get_employee_id_text_driver_profile(self):
        self.wait_for_element_displayed((By.XPATH, FIL.employee_id_text_driver_profile_xpath))
        return self.get_text((By.XPATH, FIL.employee_id_text_driver_profile_xpath))

    def get_group_text_driver_profile(self):
        self.wait_for_element_displayed((By.XPATH, FIL.group_text_driver_profile_xpath))
        return self.get_text((By.XPATH, FIL.group_text_driver_profile_xpath))

    def get_vehicle_name_text_driver_profile(self):
        self.wait_for_element_displayed((By.XPATH, FIL.vehicle_name_text_driver_profile_xpath))
        return self.get_text((By.XPATH, FIL.vehicle_name_text_driver_profile_xpath))

    def get_email_text_driver_profile(self):
        self.wait_for_element_displayed((By.XPATH, FIL.email_text_driver_profile_xpath))
        return self.get_text((By.XPATH, FIL.email_text_driver_profile_xpath))

    def get_daily_avg_text_driver_profile(self):
        return self.get_text((By.XPATH, FIL.daily_avg_text_driver_profile_xpath))

    def get_total_text_driver_profile(self):
        return self.get_text((By.XPATH, FIL.total_text_driver_profile_xpath))

    def click_expand_icon_driver_profile(self):
        self.wait_for_element_displayed((By.XPATH, FIL.expand_driver_summary_icon_xpath))
        self.click((By.XPATH, FIL.expand_driver_summary_icon_xpath))

    def get_route_time_text_driver_profile(self):
        return self.get_text((By.XPATH, FIL.route_time_driver_profile_xpath))

    def get_distance_text_driver_profile(self):
        return self.get_text((By.XPATH, FIL.distance_driver_profile_xpath))

    def get_trips_text_driver_profile(self):
        return self.get_text((By.XPATH, FIL.trips_driver_profile_xpath))

    def get_stops_text_driver_profile(self):
        return self.get_text((By.XPATH, FIL.stops_driver_profile_xpath))

    def get_stop_time_text_driver_profile(self):
        return self.get_text((By.XPATH, FIL.stop_time_driver_profile_xpath))

    def get_driving_time_text_driver_profile(self):
        return self.get_text((By.XPATH, FIL.driving_time_driver_profile_xpath))

    def get_engine_hours_text_driver_profile(self):
        return self.get_text((By.XPATH, FIL.engine_hours_driver_profile_xpath))

    def get_idle_violations_text_driver_profile(self):
        return self.get_text((By.XPATH, FIL.idle_violations_driver_profile_xpath))

    def get_idle_duration_text_driver_profile(self):
        return self.get_text((By.XPATH, FIL.idle_duration_driver_profile_xpath))

    def get_speed_violation_text_driver_profile(self):
        return self.get_text((By.XPATH, FIL.speed_violation_driver_profile_xpath))

    def get_speeding_duration_text_driver_profile(self):
        return self.get_text((By.XPATH, FIL.speeding_duration_driver_profile_xpath))

    def set_driver_profile_date_range(self, start_month, start_day, start_year, end_month, end_day, end_year):
        self.click((By.XPATH, FIL.driver_profile_date_range_start_month_xpath))
        self.type((By.XPATH, FIL.driver_profile_date_range_start_month_xpath), start_month)
        self.click((By.XPATH, FIL.driver_profile_date_range_start_day_xpath))
        self.type((By.XPATH, FIL.driver_profile_date_range_start_day_xpath), start_day)
        self.click((By.XPATH, FIL.driver_profile_date_range_start_year_xpath))
        self.type((By.XPATH, FIL.driver_profile_date_range_start_year_xpath), start_year)
        self.click((By.XPATH, FIL.driver_profile_date_range_end_month_xpath))
        self.type((By.XPATH, FIL.driver_profile_date_range_end_month_xpath), end_month)
        self.click((By.XPATH, FIL.driver_profile_date_range_end_day_xpath))
        self.type((By.XPATH, FIL.driver_profile_date_range_end_day_xpath), end_day)
        self.click((By.XPATH, FIL.driver_profile_date_range_end_year_xpath))
        self.type((By.XPATH, FIL.driver_profile_date_range_end_year_xpath), end_year)

    def click_trip_item_driver_profile_trip(self):
        self.click((By.XPATH, FIL.open_trip_driver_profile_xpath))

    def get_trip1_text_driver_profile_trip(self):
        return self.get_text((By.XPATH, FIL.trip1_label_driver_profile_trip_xpath))

    def start_time_displayed_driver_profile_trip(self):
        return self.element_is_displayed((By.XPATH, FIL.start_time_driver_profile_trip_xpath))

    def start_address_driver_profile_trip(self):
        return self.get_text((By.XPATH, FIL.start_address_driver_profile_trip_xpath))

    def end_time_displayed_driver_profile_trip(self):
        return self.element_is_displayed((By.XPATH, FIL.end_time_driver_profile_trip_xpath))

    def end_address_driver_profile_trip(self):
        return self.get_text((By.XPATH, FIL.end_address_driver_profile_trip_xpath))

    def get_vehicle_text_driver_profile_trip(self):
        return self.get_text((By.XPATH, FIL.vehicle_driver_profile_trip_xpath))

    def get_trip_duration_text_driver_profile_trip(self):
        return self.get_text((By.XPATH, FIL.trip_duration_driver_profile_trip_xpath))

    def get_distance_text_driver_profile_trip(self):
        return self.get_text((By.XPATH, FIL.distance_driver_profile_trip_xpath))

    def get_max_speed_text_driver_profile_trip(self):
        return self.get_text((By.XPATH, FIL.max_speed_driver_profile_trip_xpath))

    def get_stop_duration_text_driver_profile_trip(self):
        return self.get_text((By.XPATH, FIL.stop_duration_driver_profile_trip_xpath))

    def click_idle_tab_driver_profile(self):
        self.click((By.XPATH, FIL.idle_tab_driver_profile_xpath))

    def click_idle_driver_profile_idle(self):
        self.click((By.XPATH, FIL.open_idle_driver_profile_idle_xpath))

    def get_idle1_text_driver_profile_idle(self):
        return self.get_text((By.XPATH, FIL.idle1_text_driver_profile_idle_xpath))

    def get_address_driver_profile_idle(self):
        return self.get_text((By.XPATH, FIL.address_driver_profile_idle_xpath))

    def time_displayed_driver_profile_idle(self):
        return self.element_is_displayed((By.XPATH, FIL.time_driver_profile_idle_xpath))

    def get_vehicle_text_driver_profile_idle(self):
        return self.get_text((By.XPATH, FIL.vehicle_text_driver_profile_idle_xpath))

    def get_idle_duration_text_driver_profile_idle(self):
        return self.get_text((By.XPATH, FIL.idle_duration_driver_profile_idle_xpath))

    def click_date_filter_driver_profile(self):
        self.click((By.XPATH, FIL.date_filter_driver_profile_xpath))

    def select_last_90_days_driver_profile(self):
        self.click((By.XPATH, FIL.last_90_days_driver_profile_xpath))

    def click_apply_driver_profile(self):
        self.click((By.XPATH, FIL.apply_button_driver_profile_xpath))

    def click_trip_tab_driver_profile(self):
        self.click((By.XPATH, FIL.trip_tab_driver_profile_xpath))

    def get_trip_count_driver_profile(self):
        return self.get_text((By.XPATH, FIL.trips_count_driver_profile_xpath))

    def get_idle_count_driver_profile(self):
        return self.get_text((By.XPATH, FIL.idles_count_driver_profile_xpath))

    def get_equipment_status_title(self):
        return self.get_text((By.XPATH, FIL.equipment_status_title_xpath))

    def get_equipment_text(self):
        return self.get_text((By.ID, FIL.equipment_column_title_id))

    def get_equipment_group_text(self):
        return self.get_text((By.ID, FIL.equipment_group_column_id))

    def get_equipment_device_text(self):
        return self.get_text((By.ID, FIL.equipment_device_column_id))

    def get_equipment_last_location_text(self):
        return self.get_text((By.XPATH, FIL.equipment_last_location_column_xpath))

    def get_equipment_last_connected_text(self):
        return self.get_text((By.ID, FIL.equipment_last_connected_column_id))

    def get_equipment_last_movement_text(self):
        return self.get_text((By.ID, FIL.equipment_last_movement_column_id))

    def get_equipment_stationary_text(self):
        return self.get_text((By.XPATH, FIL.equipment_stationary_duration_column_xpath))

    def get_equipment_battery_text(self):
        return self.get_text((By.ID, FIL.equipment_battery_level_column_id))

    def get_geofences_title(self):
        return self.get_text((By.XPATH, FIL.geofences_title_xpath))

    def get_state_mileage_title(self):
        return self.get_text((By.XPATH, FIL.state_mileage_title_xpath))

    def get_data_export_title(self):
        return self.get_text((By.XPATH, FIL.data_export_title_xpath))

    # Fleet Data
    def get_average_text(self):
        self.wait_for_element_displayed((By.XPATH, FIL.average_text_xpath))
        return self.get_text((By.XPATH, FIL.average_text_xpath))

    def get_total_text(self):
        return self.get_text((By.XPATH, FIL.total_text_xpath))

    def get_metric_detail_text(self):
        return self.get_text((By.XPATH, FIL.metric_detail_xpath))

    def click_distance_column(self):
        self.click((By.XPATH, FIL.distance_xpath))

    def get_graph_header_text(self):
        return self.get_text((By.XPATH, FIL.graph_header_title_text_xpath))

    def click_group_tab(self):
        self.click((By.XPATH, FIL.groups_tab_table_xpath))

    def click_vehicle_tab(self):
        self.click((By.XPATH, FIL.vehicles_tab_table_xpath))

    def get_groups_text(self):
        return self.get_text((By.XPATH, FIL.groups_text_xpath))

    def get_distance_text(self):
        return self.get_text((By.XPATH, FIL.distance_text_xpath))

    def get_engine_hours_text(self):
        return self.get_text((By.XPATH, FIL.engine_hours_text_xpath))

    def get_driving_hours_text(self):
        return self.get_text((By.XPATH, FIL.driving_hours_text_xpath))

    def get_idle_time_text(self):
        return self.get_text((By.XPATH, FIL.idle_time_text_xpath))

    def get_idle_pto_time_text(self):
        return self.get_text((By.XPATH, FIL.idle_pto_time_text_xpath))

    def get_fuel_consumed_text(self):
        return self.get_text((By.XPATH, FIL.fuel_consumed_text_xpath))

    def get_driving_fuel_text(self):
        return self.get_text((By.XPATH, FIL.driving_fuel_text_xpath))

    def get_idling_fuel_text(self):
        return self.get_text((By.XPATH, FIL.idling_fuel_text_xpath))

    def get_pto_idling_fuel_text(self):
        return self.get_text((By.XPATH, FIL.pto_idling_fuel_text_xpath))

    def get_fuel_economy_text(self):
        return self.get_text((By.XPATH, FIL.fuel_economy_text_xpath))

    def get_driving_fuel_economy_text(self):
        return self.get_text((By.XPATH, FIL.driving_fuel_economy_text_xpath))

    def get_vehicle_text(self):
        return self.get_text((By.XPATH, FIL.vehicle_text_xpath))

    def get_vehicle_odometer_reading_text(self):
        return self.get_text((By.XPATH, FIL.vehicle_odometer_reading_text_xpath))

    def get_vehicle_distance_text(self):
        return self.get_text((By.XPATH, FIL.vehicle_distance_text_xpath))

    def get_vehicle_engine_hours_text(self):
        return self.get_text((By.XPATH, FIL.vehicle_engine_hours_text_xpath))

    def get_vehicle_driving_hours_text(self):
        return self.get_text((By.XPATH, FIL.vehicle_driving_hours_text_xpath))

    def get_vehicle_idle_time_text(self):
        return self.get_text((By.XPATH, FIL.vehicle_idle_time_text_xpath))

    def get_vehicle_idle_pto_time_text(self):
        return self.get_text((By.XPATH, FIL.vehicle_idle_pto_time_text_xpath))

    def get_vehicle_fuel_consumed_text(self):
        return self.get_text((By.XPATH, FIL.vehicle_fuel_consumed_text_xpath))

    def get_vehicle_driving_fuel_text(self):
        return self.get_text((By.XPATH, FIL.vehicle_driving_fuel_text_xpath))

    def get_vehicle_idling_fuel_text(self):
        return self.get_text((By.XPATH, FIL.vehicle_idling_fuel_text_xpath))

    def get_vehicle_pto_idling_fuel_text(self):
        return self.get_text((By.XPATH, FIL.vehicle_pto_idling_fuel_text_xpath))

    def get_vehicle_fuel_economy_text(self):
        return self.get_text((By.XPATH, FIL.vehicle_fuel_economy_text_xpath))

    def get_vehicle_driving_fuel_economy_text(self):
        return self.get_text((By.XPATH, FIL.vehicle_driving_fuel_economy_text_xpath))

    def click_group_filter_fleet_data(self):
        self.click((By.XPATH, FIL.fleet_data_group_filter_button_xpath))

    def search_by_group_fleet_data(self, groupname):
        self.type((By.XPATH, FIL.fleet_data_search_by_group_textbox_xpath), groupname)

    def select_search_group_fleet_data(self):
        self.click((By.XPATH, FIL.fleet_data_select_search_button_xpath))

    def click_done_button_fleet_data(self):
        self.click((By.XPATH, FIL.fleet_data_done_button_xpath))

    def click_date_filter_fleet_data(self):
        self.click((By.XPATH, FIL.fleet_data_date_filter_xpath))

    def set_fleet_data_date_range(self, start_month, start_day, start_year, end_month, end_day, end_year):
        self.click((By.XPATH, FIL.fleet_data_date_range_start_month_xpath))
        self.type((By.XPATH, FIL.fleet_data_date_range_start_month_xpath), start_month)
        self.click((By.XPATH, FIL.fleet_data_date_range_start_day_xpath))
        self.type((By.XPATH, FIL.fleet_data_date_range_start_day_xpath), start_day)
        self.click((By.XPATH, FIL.fleet_data_date_range_start_year_xpath))
        self.type((By.XPATH, FIL.fleet_data_date_range_start_year_xpath), start_year)
        self.click((By.XPATH, FIL.fleet_data_date_range_end_month_xpath))
        self.type((By.XPATH, FIL.fleet_data_date_range_end_month_xpath), end_month)
        self.click((By.XPATH, FIL.fleet_data_date_range_end_day_xpath))
        self.type((By.XPATH, FIL.fleet_data_date_range_end_day_xpath), end_day)
        self.click((By.XPATH, FIL.fleet_data_date_range_end_year_xpath))
        self.type((By.XPATH, FIL.fleet_data_date_range_end_year_xpath), end_year)

    def click_apply_button_fleet_data(self):
        self.click((By.ID, FIL.apply_button_id))

    # vehicle profile actions
    def search_vehicle_vehicle_profile(self, vehicle_name):
        self.type((By.XPATH, FIL.vehicle_search_xpath), vehicle_name)
        self.find((By.XPATH, FIL.vehicle_search_xpath)).send_keys(Keys.ENTER)

    def select_vehicle_profile(self, vehicle_name):
        self.wait_for_element_displayed((By.XPATH, LocatorUtil.give_locator(FIL.vehicle_suggestion_xpath, vehicle_name)))
        self.click((By.XPATH, LocatorUtil.give_locator(FIL.vehicle_suggestion_xpath, vehicle_name)))

    def click_expand_metadata_icon(self):
        self.click((By.XPATH, FIL.expand_metadata_icon_xpath))

    def click_expand_summary_icon(self):
        self.click((By.XPATH, FIL.expand_vehicle_summary_icon_xpath))

    def click_date_filter_vehicle_profile(self):
        self.click((By.XPATH, FIL.date_filter_vehicle_profile_xpath))

    def set_vehicle_profile_date_range(self, start_month, start_day, start_year, end_month, end_day, end_year):
        self.click((By.XPATH, FIL.vehicle_profile_date_range_start_month_xpath))
        self.type((By.XPATH, FIL.vehicle_profile_date_range_start_month_xpath), start_month)
        self.click((By.XPATH, FIL.vehicle_profile_date_range_start_day_xpath))
        self.type((By.XPATH, FIL.vehicle_profile_date_range_start_day_xpath), start_day)
        self.click((By.XPATH, FIL.vehicle_profile_date_range_start_year_xpath))
        self.type((By.XPATH, FIL.vehicle_profile_date_range_start_year_xpath), start_year)
        self.click((By.XPATH, FIL.vehicle_profile_date_range_end_day_xpath))
        self.click((By.XPATH, FIL.vehicle_profile_date_range_end_month_xpath))
        self.type((By.XPATH, FIL.vehicle_profile_date_range_end_month_xpath), end_month)
        self.click((By.XPATH, FIL.vehicle_profile_date_range_end_day_xpath))
        self.type((By.XPATH, FIL.vehicle_profile_date_range_end_day_xpath), end_day)
        self.click((By.XPATH, FIL.vehicle_profile_date_range_end_year_xpath))
        self.type((By.XPATH, FIL.vehicle_profile_date_range_end_year_xpath), end_year)

    def select_date_of_trip(self):
        # nothing to click here since lack of trip data
        # xpath points to emtpy message label
        self.click((By.XPATH, FIL.date_trip_detail_xpath))

    def select_date_of_idle(self):
        self.click((By.XPATH, FIL.date_idle_detail_xpath))

    def click_trip_tab(self):
        self.click((By.XPATH, FIL.trip_tab_xpath))

    def click_idle_tab(self):
        self.click((By.XPATH, FIL.idle_tab_xpath))

    # vehicle profile assertions
    def get_fleet_operations_vehicle_profile(self):
        try:
            return self.get_text((By.XPATH, FIL.vehicle_profile_title_xpath))
        except TimeoutException:
            sleep(2)
            return self.get_text((By.XPATH, FIL.vehicle_profile_title_xpath))

    def get_trip_count(self):
        return self.get_text((By.XPATH, FIL.trip_count_xpath))

    def click_trip_vehicle_profile(self):
        self.click((By.XPATH, FIL.vehicle_profile_trip_info_xpath))

    def get_trip_num_vehicle_profile(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_trip_num_xpath))

    def get_trip_driver_vehicle_profile(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_trip_driver_xpath))

    def get_trip_duration_vehicle_profile(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_trip_duration_xpath))

    def get_trip_distance_vehicle_profile(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_trip_distance_xpath))

    def get_trip_speed_vehicle_profile(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_trip_speed_xpath))

    def get_trip_stop_duration_vehicle_profile(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_trip_stop_duration_xpath))

    def get_idle_count(self):
        return self.get_text((By.XPATH, FIL.idle_count_xpath))

    def click_idle_vehicle_profile(self):
        self.click((By.XPATH, FIL.vehicle_profile_idle_info_xpath))

    def get_idle_num_vehicle_profile(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_idle_num_xpath))

    def get_idle_driver_vehicle_profile(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_idle_driver_xpath))

    def get_idle_duration_vehicle_profile(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_idle_duration_xpath))

    def get_idle_detail_address(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_idle_address_xpath))

    def get_idle_detail_occur_time(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_idle_occur_time_xpath))

    def get_idle_detail_duration(self):
        occur_time = self.get_idle_detail_occur_time()
        list = occur_time.split(':')
        start_min = int(list[1][:2])
        end_min = int(list[2][:2])
        if end_min < start_min:
            end_min = end_min + 60

        return end_min - start_min

    def get_empty_list_message(self):
        return self.get_text((By.XPATH, FIL.empty_list_message_xpath))

    # metadata texts
    def get_vehicle_profile_vehicle_name(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_vehicle_name_xpath))

    def get_vehicle_profile_group(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_group_xpath))

    def get_vehicle_profile_driver(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_driver_xpath))

    def get_vehicle_profile_device(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_device_xpath))

    def get_vehicle_profile_status(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_status_xpath))

    def get_vehicle_profile_make(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_make_xpath))

    def get_vehicle_profile_license(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_license_xpath))

    def get_vehicle_profile_hibernation(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_hibernation_xpath))

    def get_vehicle_profile_vin(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_vin_xpath))

    def get_vehicle_profile_vehicle_type(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_vehicle_type_xpath))

    def get_vehicle_profile_seat_belt(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_seat_belt_xpath))

    # summary section texts
    def get_vehicle_profile_route_time(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_route_time_xpath))

    def get_vehicle_profile_route_time_value(self):
        self.wait_for_element_displayed((By.XPATH, FIL.vehicle_profile_route_time_value_xpath))
        return self.get_text((By.XPATH, FIL.vehicle_profile_route_time_value_xpath))

    def get_vehicle_profile_idle_duration_value(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_route_time_value_xpath))

    def get_vehicle_profile_distance(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_distance_xpath))

    def get_vehicle_profile_trips(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_trips_xpath))

    def get_vehicle_profile_stops(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_stops_xpath))

    def get_vehicle_profile_stop_time(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_stop_time_xpath))

    def get_vehicle_profile_driving_time(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_driving_time_xpath))

    def get_vehicle_profile_engine_hours(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_engine_hours_xpath))

    def get_vehicle_profile_idle_violation(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_idle_violation_xpath))

    def get_vehicle_profile_idle_duration(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_idle_duration_xpath))

    def get_vehicle_profile_speed_violation(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_speed_violation_xpath))

    def get_vehicle_profile_speed_duration(self):
        return self.get_text((By.XPATH, FIL.vehicle_profile_speed_duration_xpath))

    # filter group on equipment status page
    def click_group_filter_equipment_status(self):
        self.click((By.XPATH, FIL.group_filter_equipment_status_xpath))

    def select_group_group_filter_equipment_status(self, group_name):
        self.type((By.XPATH, FIL.search_by_group_textbox_equipment_status_xpath), group_name)

    def select_search_group_equipment_status(self):
        self.click((By.XPATH, FIL.select_search_button_equipment_status_xpath))

    def apply_group_filter_equipment_status(self):
        self.click((By.XPATH, FIL.done_button_equipment_status_xpath))

    def click_search_assert_type_equipment_status(self):
        self.click((By.XPATH, FIL.equipment_status_search_assert_type_xpath))

    def select_select_search_item_equipment_status(self, asset_type):
        if FleetInsightEquipmentStatusAssetType.Equipment == asset_type:
            self.click((By.XPATH, FIL.equipment_status_asset_type_equipment_xpath))

        if FleetInsightEquipmentStatusAssetType.Device == asset_type:
            self.click((By.XPATH, FIL.equipment_status_asset_type_device_xpath))

    def type_search_criteria_equipment_status(self, search_text):
        self.type((By.XPATH, FIL.search_criteria_equipment_status_xpath), search_text)

    # filter in Insights_State_Mileage page
    def click_group_filter_state_mileage(self):
        self.click((By.XPATH, FIL.group_filter_button_state_mileage_xpath))

    def search_group_state_mileage(self, groupname):
        self.type((By.XPATH, FIL.search_by_group_textbox_state_mileage_xpath), groupname)

    def select_group_state_mileage(self):
        self.click((By.XPATH, FIL.select_search_button_state_mileage_xpath))

    def click_done_state_mileage(self):
        self.click((By.XPATH, FIL.done_button_state_mileage_xpath))

    def click_date_filter_state_mileage(self):
        self.click((By.XPATH, FIL.date_filter_state_mileage_xpath))

    def select_last_60_days_state_mileage(self):
        self.click((By.XPATH, FIL.last_60_days_state_mileage_xpath))

    def click_apply_button_state_mileage(self):
        self.click((By.ID, FIL.apply_button_id))

    def get_vehicle_column_text_state_mileage(self):
        return self.get_text((By.XPATH, FIL.vehicle_column_text_state_mileage_xpath))

    def get_group_column_text_state_mileage(self):
        return self.get_text((By.XPATH, FIL.group_column_text_state_mileage_xpath))

    def get_device_serial_column_text_state_mileage(self):
        return self.get_text((By.XPATH, FIL.device_serial_column_text_state_mileage_xpath))

    def get_state_country_column_text_state_mileage(self):
        return self.get_text((By.XPATH, FIL.state_country_column_text_state_mileage_xpath))

    def get_distance_column_text_state_mileage(self):
        return self.get_text((By.XPATH, FIL.distance_column_text_state_mileage_xpath))

    def get_count_of_records_state_mileage(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, FIL.count_record_state_mileage_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, FIL.count_record_state_mileage_xpath))

    def get_metrics_text_state_mileage(self):
        return self.get_text((By.XPATH, FIL.metrics_text_state_mileage_xpath))

    def get_total_distance_text_state_mileage(self):
        return self.get_text((By.XPATH, FIL.total_distance_text_state_mileage_xpath))

    def get_total_text_state_mileage(self):
        return self.get_text((By.XPATH, FIL.total_text_state_mileage_xpath))

    def click_total_distance_text_state_mileage(self):
        self.click((By.XPATH, FIL.total_distance_text_state_mileage_xpath))

    def get_trend_header_text_state_mileage(self):
        return self.get_text((By.XPATH, FIL.trend_header_text_state_mileage_xpath))

    # data export actions
    def select_date_range(self):
        self.click((By.XPATH, FIL.data_export_select_date_xpath))
        self.click((By.XPATH, FIL.data_export_30_days_xpath))
        self.click_apply_button()

    def click_request_data(self):
        try:
            self.wait_for_element_is_clickable((By.XPATH, FIL.data_export_request_data_id))
        except (TimeoutException, StaleElementReferenceException, ElementClickInterceptedException,
                ElementNotInteractableException):
            self.wait_for_element_is_clickable((By.XPATH, FIL.data_export_request_data_id))
        self.click((By.XPATH, FIL.data_export_request_data_id))
        sleep(3)
        self.click_refresh_button()

    def get_request_status(self):
        return self.get_text((By.XPATH, FIL.data_export_request_status_xpath))

    def get_request_type(self):
        return self.get_text((By.XPATH, FIL.data_export_request_type_xpath))

    def wait_for_download_detailed_history(self):
        status = ""
        generate_time: int = 0
        while status != "Download":
            sleep(20)
            self.click_refresh_button()
            sleep(5)
            status = self.get_text((By.XPATH, FIL.data_export_status_xpath))
            generate_time += 1
            if generate_time == 30:
                break

    def download_detailed_history(self):
        self.wait_for_download_detailed_history()
        self.click((By.XPATH, FIL.data_export_download_xpath))
        # wait for download complete
        sleep(20)

    def get_data_export_file_name(self):
        date_now = datetime.now().strftime("%m-%d-%Y")
        date_last_30 = (datetime.now() - timedelta(days=29)).strftime("%m-%d-%Y")

        file_name = date_last_30 + '_' + date_now + '_DetailedHistory_Lytx.zip'
        return file_name

    def get_action_label(self):
        return self.get_text((By.XPATH, FIL.action_label_xpath))

    def get_report_type_label(self):
        return self.get_text((By.XPATH, FIL.report_type_label_xpath))

    def get_group_label(self):
        return self.get_text((By.XPATH, FIL.group_label_xpath))

    def get_start_date_label(self):
        return self.get_text((By.XPATH, FIL.start_date_label_xpath))

    def get_end_date_label(self):
        return self.get_text((By.XPATH, FIL.end_date_label_xpath))

    def get_vehicle_label(self):
        return self.get_text((By.XPATH, FIL.vehicle_label_xpath))

    def get_requested_date_label(self):
        return self.get_text((By.XPATH, FIL.requested_date_label_xpath))

    def click_cancel_1st_request_data_export(self):
        self.find_elements((By.CLASS_NAME, FIL.data_export_cancel_request_class))[0].click()

    def click_delete_1st_request_data_export(self):
        self.find_elements((By.CLASS_NAME, FIL.data_export_delete_request_class))[0].click()

    def confirm_delete_request_data_export(self):
        self.click((By.ID, FIL.data_export_confirm_delete_request_id))

    def clear_existing_data_export_history(self):
        in_progress_request_count = len(self.find_elements((By.CLASS_NAME, FIL.data_export_cancel_request_class)))
        i = 0
        while i < in_progress_request_count:
            self.click_cancel_1st_request_data_export()
            self.confirm_delete_request_data_export()
            self.click_refresh_button()
            i += 1
            sleep(3)

        complete_request_count = len(self.find_elements((By.CLASS_NAME, FIL.data_export_delete_request_class)))
        i = 0
        while i < complete_request_count:
            self.click_delete_1st_request_data_export()
            self.confirm_delete_request_data_export()
            self.click_refresh_button()
            i += 1
            sleep(3)

    # Geofences
    def click_group_filter_geofences(self):
        self.click((By.XPATH, FIL.geofences_group_filter_button_xpath))

    def search_group_geofences(self, groupname):
        self.type((By.XPATH, FIL.geofences_search_by_group_textbox_xpath), groupname)

    def select_group_geofences(self):
        self.click((By.XPATH, FIL.geofences_select_search_button_xpath))

    def click_done_geofences(self):
        self.click((By.XPATH, FIL.geofences_done_button_xpath))

    def click_date_filter_geofences(self):
        self.click((By.XPATH, FIL.geofences_date_filter_xpath))

    def set_geofences_date_range(self, start_month, start_day, start_year, end_month, end_day, end_year):
        self.click((By.XPATH, FIL.geofences_date_range_start_month_xpath))
        self.type((By.XPATH, FIL.geofences_date_range_start_month_xpath), start_month)
        self.click((By.XPATH, FIL.geofences_date_range_start_day_xpath))
        self.type((By.XPATH, FIL.geofences_date_range_start_day_xpath), start_day)
        self.click((By.XPATH, FIL.geofences_date_range_start_year_xpath))
        self.type((By.XPATH, FIL.geofences_date_range_start_year_xpath), start_year)
        self.click((By.XPATH, FIL.geofences_date_range_end_month_xpath))
        self.type((By.XPATH, FIL.geofences_date_range_end_month_xpath), end_month)
        self.click((By.XPATH, FIL.geofences_date_range_end_day_xpath))
        self.type((By.XPATH, FIL.geofences_date_range_end_day_xpath), end_day)
        self.click((By.XPATH, FIL.geofences_date_range_end_year_xpath))
        self.type((By.XPATH, FIL.geofences_date_range_end_year_xpath), end_year)

    def click_apply_button_geofences(self):
        self.click((By.ID, FIL.apply_button_id))

    def search_geofence_geofences(self, search_text):
        self.type_ignore_exceptions((By.XPATH, FIL.geofences_search_geofence_xpath), search_text, 10)

    def select_1st_geofence_geofences(self, geofence_name):
        self.wait_for_expected_text((By.XPATH, FIL.geofences_search_geofence_1st_xpath), geofence_name)
        self.click((By.XPATH, FIL.geofences_search_geofence_1st_xpath))

    def search_geofence_geofence_profile(self, search_text):
        i = 0
        while i < 10:
            i += 3
            try:
                self.type((By.XPATH, FIL.geofence_profile_search_geofence_xpath), search_text)
                break
            except TimeoutException:
                sleep(2)

    def select_1st_geofence_geofence_profile(self, geofence_name):
        i = 0
        while i < 10:
            i += 2
            try:
                if geofence_name in str(self.get_text((By.XPATH, FIL.geofence_profile_search_geofence_1st_xpath))):
                    break
            except TimeoutException:
                sleep(2)

        self.click((By.XPATH, FIL.geofence_profile_search_geofence_1st_xpath))

    def get_geofence_profile_metadata_name(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_metadata_name_xpath))

    def geofence_profile_metadata_date_created(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_metadata_date_created_xpath))

    def geofence_profile_metadata_days_applied(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_metadata_days_applied_xpath))

    def geofence_profile_metadata_time(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_metadata_time_xpath))

    def geofence_profile_metadata_type(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_metadata_type_xpath))

    def geofence_profile_metadata_group(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_metadata_group_xpath))

    def geofence_profile_metadata_subgroup(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_metadata_subgroup_xpath))

    def geofence_profile_metadata_vehicles(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_metadata_vehicles_xpath))

    def geofence_profile_summary_date_picker_is_displayed(self):
        return self.element_is_displayed((By.XPATH, FIL.geofence_profile_summary_date_picker_xpath))

    def geofence_profile_summary_total_trigger(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_summary_total_trigger_xpath))

    def geofence_profile_summary_total_vehicle(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_summary_total_vehicle_xpath))

    def geofence_profile_summary_total_duration(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_summary_total_duration_xpath))

    def geofence_profile_summary_driving_time(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_summary_driving_time_xpath))

    def geofence_profile_summary_idle_time(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_summary_idle_time_xpath))

    def geofence_profile_summary_stop_time(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_summary_stop_time_xpath))

    def geofence_profile_summary_total_trigger_count(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_summary_total_trigger_count_xpath))

    def geofence_profile_summary_total_vehicle_count(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_summary_total_vehicle_count_xpath))

    def geofence_profile_summary_total_duration_time(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_summary_total_duration_time_xpath))

    def geofence_profile_summary_driving_time_num(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_summary_driving_time_num_xpath))

    def geofence_profile_summary_idle_time_num(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_summary_idle_time_num_xpath))

    def geofence_profile_summary_stop_time_num(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_summary_stop_time_num_xpath))

    def geofence_profile_detail_triggers(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_detail_triggers_xpath))

    def click_date_filter_geofence_profile(self):
        self.click((By.XPATH, FIL.geofence_profile_summary_date_picker_xpath))

    def click_last_30_days_date_picker_geofence_profile(self):
        self.click((By.XPATH, FIL.geofence_profile_summary_date_picker_xpath))

    def click_apply_date_picker_geofence_profile(self):
        self.wait_for_element_is_clickable((By.ID, FIL.apply_button_id))
        self.click((By.ID, FIL.apply_button_id))

    def click_geofence_profile_trigger_vehicle(self):
        self.click((By.XPATH, FIL.geofence_profile_trigger_vehicle_xpath))

    def geofence_profile_trigger_trigger_start(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_trigger_trigger_start_xpath))

    def geofence_profile_trigger_trigger_end(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_trigger_trigger_end_xpath))

    def geofence_profile_trigger_driver(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_trigger_driver_xpath))

    def geofence_profile_trigger_trigger_type(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_trigger_trigger_type_xpath))

    def geofence_profile_trigger_driving_time(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_trigger_driving_time_xpath))

    def geofence_profile_trigger_stop_time(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_trigger_stop_time_xpath))

    def geofence_profile_trigger_idle_time(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_trigger_idle_time_xpath))

    def geofence_profile_trigger_duration(self):
        return self.get_text((By.XPATH, FIL.geofence_profile_trigger_duration_xpath))

    def geofence_profile_trigger_geofence_pin_is_displayed(self):
        sleep(2)
        return self.element_is_displayed((By.XPATH, FIL.geofence_profile_trigger_geofence_pin_xpath))

    def click_geofence_profile_date_picker(self):
        self.click((By.XPATH, FIL.geofence_profile_summary_date_picker_xpath))

    def set_geofence_profile_date_range(self, start_month, start_day, start_year, end_month, end_day, end_year):
        self.click((By.XPATH, FIL.geofence_profile_date_range_start_month_xpath))
        self.type((By.XPATH, FIL.geofence_profile_date_range_start_month_xpath), start_month)
        self.click((By.XPATH, FIL.geofence_profile_date_range_start_day_xpath))
        self.type((By.XPATH, FIL.geofence_profile_date_range_start_day_xpath), start_day)
        self.click((By.XPATH, FIL.geofence_profile_date_range_start_year_xpath))
        self.type((By.XPATH, FIL.geofence_profile_date_range_start_year_xpath), start_year)
        self.click((By.XPATH, FIL.geofence_profile_date_range_end_month_xpath))
        self.type((By.XPATH, FIL.geofence_profile_date_range_end_month_xpath), end_month)
        self.click((By.XPATH, FIL.geofence_profile_date_range_end_day_xpath))
        self.type((By.XPATH, FIL.geofence_profile_date_range_end_day_xpath), end_day)
        self.click((By.XPATH, FIL.geofence_profile_date_range_end_year_xpath))
        self.type((By.XPATH, FIL.geofence_profile_date_range_end_year_xpath), end_year)

    # Dashboard
    def click_dashboard_filter_by_group_dropdown(self):
        self.click((By.ID, FIL.dashboard_filter_by_group_dropdown_id))

    def click_dashboard_filter_by_group_done_button(self):
        self.click((By.XPATH, FIL.dashboard_filter_by_group_done_button_xpath))

    def click_dashboard_filter_by_date_dropdown(self):
        self.click((By.XPATH, FIL.dashboard_filter_by_date_dropdown_xpath))

    def click_dashboard_last_60_days(self):
        self.click((By.XPATH, FIL.dashboard_last_60_days_xpath))

    def click_dashboard_date_apply_button(self):
        self.click((By.XPATH, FIL.dashboard_date_apply_button_xpath))

    def get_vehicles_count(self):
        return self.get_text((By.XPATH, FIL.vehicles_count_xpath))

    def get_vehicles_text_xpath(self):
        return self.get_text((By.XPATH, FIL.vehicles_text_xpath))

    def get_geofence_triggers_text(self):
        return self.get_text((By.ID, FIL.geofence_triggers_text_id))

    def get_geofence_triggers_count(self):
        return self.get_text((By.ID, FIL.geofence_triggers_count_id))

    def get_idle_duration_text(self):
        return self.get_text((By.ID, FIL.idle_duration_text_id))

    def get_idle_duration_count(self):
        return self.get_text((By.ID, FIL.idle_duration_count_id))

    def get_metrics_text(self):
        return self.get_text((By.ID, FIL.metrics_text_id))

    def get_metrics_geofence_triggers(self):
        return self.get_text((By.XPATH, FIL.metrics_geofence_triggers_xpath))

    def get_metrics_geofence_column(self):
        return self.get_text((By.XPATH, FIL.metrics_geofence_column_xpath))

    def get_metrics_group_column(self):
        return self.get_text((By.XPATH, FIL.metrics_group_column_xpath))

    def get_metrics_triggers_column(self):
        return self.get_text((By.XPATH, FIL.metrics_triggers_column_xpath))

    def get_metrics_duration_column(self):
        return self.get_text((By.XPATH, FIL.metrics_duration_column_xpath))

    def get_metrics_idle_duration(self):
        return self.get_text((By.XPATH, FIL.metrics_idle_duration_xpath))

    def set_fleet_operation_date_range(self, start_month, start_day, start_year, end_month, end_day, end_year):
        self.click((By.XPATH, FIL.fleet_operation_date_range_start_month_xpath))
        self.type((By.XPATH, FIL.fleet_operation_date_range_start_month_xpath), start_month)
        self.click((By.XPATH, FIL.fleet_operation_date_range_start_day_xpath))
        self.type((By.XPATH, FIL.fleet_operation_date_range_start_day_xpath), start_day)
        self.click((By.XPATH, FIL.fleet_operation_date_range_start_year_xpath))
        self.type((By.XPATH, FIL.fleet_operation_date_range_start_year_xpath), start_year)
        self.click((By.XPATH, FIL.fleet_operation_date_range_start_year_xpath))
        self.click((By.XPATH, FIL.fleet_operation_date_range_end_month_xpath))
        self.type((By.XPATH, FIL.fleet_operation_date_range_end_month_xpath), end_month)
        self.click((By.XPATH, FIL.fleet_operation_date_range_end_day_xpath))
        self.type((By.XPATH, FIL.fleet_operation_date_range_end_day_xpath), end_day)
        self.click((By.XPATH, FIL.fleet_operation_date_range_end_year_xpath))
        self.type((By.XPATH, FIL.fleet_operation_date_range_end_year_xpath), end_year)

    def set_drivers_tab_date_range(self, start_month, start_day, start_year, end_month, end_day, end_year):
        self.click((By.XPATH, FIL.drivers_tab_date_range_start_month_xpath))
        self.type((By.XPATH, FIL.drivers_tab_date_range_start_month_xpath), start_month)
        self.click((By.XPATH, FIL.drivers_tab_date_range_start_day_xpath))
        self.type((By.XPATH, FIL.drivers_tab_date_range_start_day_xpath), start_day)
        self.click((By.XPATH, FIL.drivers_tab_date_range_start_year_xpath))
        self.type((By.XPATH, FIL.drivers_tab_date_range_start_year_xpath), start_year)
        self.click((By.XPATH, FIL.drivers_tab_date_range_end_month_xpath))
        self.click((By.XPATH, FIL.drivers_tab_date_range_end_month_xpath))
        self.type((By.XPATH, FIL.drivers_tab_date_range_end_month_xpath), end_month)
        self.click((By.XPATH, FIL.drivers_tab_date_range_end_day_xpath))
        self.type((By.XPATH, FIL.drivers_tab_date_range_end_day_xpath), end_day)
        self.click((By.XPATH, FIL.drivers_tab_date_range_end_year_xpath))
        self.type((By.XPATH, FIL.drivers_tab_date_range_end_year_xpath), end_year)

    def set_vehicles_tab_date_range(self, start_month, start_day, start_year, end_month, end_day, end_year):
        self.click((By.XPATH, FIL.vehicles_tab_date_range_start_month_xpath))
        self.type((By.XPATH, FIL.vehicles_tab_date_range_start_month_xpath), start_month)
        self.click((By.XPATH, FIL.vehicles_tab_date_range_start_day_xpath))
        self.type((By.XPATH, FIL.vehicles_tab_date_range_start_day_xpath), start_day)
        self.click((By.XPATH, FIL.vehicles_tab_date_range_start_year_xpath))
        self.type((By.XPATH, FIL.vehicles_tab_date_range_start_year_xpath), start_year)
        self.click((By.XPATH, FIL.vehicles_tab_date_range_end_month_xpath))
        self.click((By.XPATH, FIL.vehicles_tab_date_range_end_month_xpath))
        self.type((By.XPATH, FIL.vehicles_tab_date_range_end_month_xpath), end_month)
        self.click((By.XPATH, FIL.vehicles_tab_date_range_end_day_xpath))
        self.type((By.XPATH, FIL.vehicles_tab_date_range_end_day_xpath), end_day)
        self.click((By.XPATH, FIL.vehicles_tab_date_range_end_year_xpath))
        self.type((By.XPATH, FIL.vehicles_tab_date_range_end_year_xpath), end_year)

    def select_vehicle_search_stg_filter(self):
        self.click((By.XPATH, FIL.select_vehicle_search_button_stg_xpath))

    def select_search_filter(self, group):
        self.click((By.XPATH, LocatorUtil.give_locator(FIL.select_search_filter_xpath, group)))

    def get_fleet_operations_new_ui_text(self):
        return self.get_text((By.XPATH, FIL.fleet_operations_new_ui_xpath))

    def get_fleet_data_new_ui_text(self):
        return self.get_text((By.XPATH, FIL.fleet_data_new_ui_xpath))

    def get_equipment_status_new_ui_text(self):
        return self.get_text((By.XPATH, FIL.equipment_status_new_ui_xpath))

    def get_geofences_new_ui_text(self):
        return self.get_text((By.XPATH, FIL.geofences_xpath))

    def get_state_mileage_new_ui_text(self):
        return self.get_text((By.XPATH, FIL.state_mileage_new_ui_xpath))

    def get_data_export_new_ui_text(self):
        return self.get_text((By.XPATH, FIL.data_export_new_ui_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, FIL.reset_button_xpath))

    def get_equipment_status_record_count(self):
        i = 0
        count_text = ""

        while i < 5:
            i += 1
            sleep(2)
            try:
                count_text = self.get_text((By.XPATH, FIL.equipment_status_record_count_xpath)).strip()

                if count_text.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        # Convert count_text to integer safely
        try:
            self.equipment_count = int(count_text)
        except ValueError:
            self.equipment_count = 0  # fallback if the element text is not numeric

        return self.equipment_count

    def get_equipment_with_attached_devices_count(self):
        self.wait_for_element_displayed((By.XPATH, FIL.device_column_xpath))
        device_cells = self.driver.find_elements(By.XPATH, FIL.device_row_xpath)
        devices_values = [cell.text.strip() for cell in device_cells if cell.text.strip()]
        self.equipment_with_device_count = len(devices_values)
        print(f"✅ Found {self.equipment_with_device_count} Device values: {devices_values}")
        return self.equipment_with_device_count

    def equipment_data_loaded(self):
        return self.element_is_displayed((By.XPATH, FIL.equipment_data_loaded_xpath))

    def count_of_records_state_mileage_is_displayed(self):
        return self.element_is_displayed((By.XPATH, FIL.count_record_state_mileage_xpath))





