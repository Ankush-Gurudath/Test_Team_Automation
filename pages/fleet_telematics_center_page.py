from locators.locators_fleet_telematics_centerpage import LocatorsFleetTelematicsCenterPage as LF
from pages.base_page import BasePage
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common import TimeoutException, NoSuchElementException, StaleElementReferenceException


class FleetTelematicsCenterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def switch_ft_iframe(self):
        self.wait_for_page_to_fully_load()
        if self.element_is_displayed((By.CLASS_NAME, LF.iframe_class)) is True:
            self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, LF.iframe_class))
            self.wait_for_page_to_fully_load()

    def search_asset_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.search_asset_id))

    def nearest_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.nearest_xpath))

    def status_dropdown_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.status_dropdown_id))

    def saved_views_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.saved_views_id))

    def show_hidden_reports_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.show_hidden_reports_id))

    def eld_unverified_logs_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.eld_unverified_logs_xpath))

    def hos_violation_breakdown_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.hos_violation_breakdown_xpath))

    def safety_is_displayed(self):
        self.scroll_to_element(self.find((By.XPATH, LF.safety_xpath)))
        return self.element_is_displayed((By.XPATH, LF.safety_xpath))

    def find_asset_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.find_asset_xpath))

    def status_change_sort_direction_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.status_change_sort_direction_xpath))

    def click_sort_by_dropdown_icon(self):
        self.click((By.XPATH, LF.sort_by_dropdown_icon_xpath))

    def get_distance_option_text(self):
        return self.get_text((By.XPATH, LF.distance_option_text_xpath))

    def get_exceptions_option_text(self):
        return self.get_text((By.XPATH, LF.exceptions_option_text_xpath))

    def update_list_with_map_checkbox_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.update_list_with_map_checkbox_xpath))

    def map_option_setting_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.map_option_setting_xpath))

    def add_zone_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.add_zone_xpath))

    def mc_refresh_icon_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.mc_refresh_icon_id))

    def mc_zoom_in_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.mc_zoom_in_xpath))

    def mc_zoom_out_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.mc_zoom_out_xpath))

    def plannedvsactual_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.plannedvsactual_header_xpath))

    def pa_search_assets_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.pa_search_assets_xpath))

    def enrollAssets_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.enrollAssets_id))

    def pa_options_dropdown_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.pa_options_dropdown_id))

    def rs_display_table_is_displayed(self):
        self.wait_for_element_displayed((By.XPATH, LF.rs_display_table_xpath))
        return self.element_is_displayed((By.XPATH, LF.rs_display_table_xpath))

    def asset_xpath_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.rs_asset_xpath))

    def pa_report_dropdown_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.pa_report_dropdown_id))

    def trip_history_header_is_displayed(self):
        return self.wait_for_element_displayed((By.ID, LF.trip_history_header_id))

    def search_bar_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.search_bar_id))

    def select_different_options_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.select_different_options_xpath))

    def live_positions_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.live_positions_id))

    def reports_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.reports_id))

    def show_all_trips_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.show_all_trips_xpath))

    def date_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.date_xpath))

    def routes_header_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.routes_header_xpath))

    def routes_search_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.routes_search_id))

    def routes_addnewroute_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.routes_addnewroute_id))

    def routes_filters_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.routes_filter_xpath))

    def routes_columns_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.routes_columns_id))

    def click_routes_columns(self):
        self.click((By.ID, LF.routes_columns_id))

    def routes_reset_to_default_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.routes_reset_to_default_xpath))

    def routes_name_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.routes_name_xpath))

    def routes_assigned_asset_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.routes_assigned_asset_xpath))

    def routes_scheduled_start_time_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.routes_scheduled_start_time_xpath))

    def routes_status_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.routes_status_xpath))

    def route_summary_report_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.route_summary_report_header_xpath))

    def rs_options_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.rs_options_id))

    def rs_stop_processing_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.rs_stop_processing_id))

    def rs_reports_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.rs_reports_id))

    def unmatched_route_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.unmatched_route_header_xpath))

    def ur_options_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.ur_options_id))

    def ur_reports_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.ur_reports_id))

    def import_routes_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.import_routes_header_xpath))

    def drop_file_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.drop_file_id))

    def import_file_table_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.import_file_table_xpath))

    def route_completion_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.route_completion_header_xpath))

    def rc_options_dropdown_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.rc_options_dropdown_xpath))

    def rc_report_dropdown_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.rc_report_dropdown_xpath))

    def rc_settings_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.rc_settings_id))

    def rc_zoom_in_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.rc_zoom_in_xpath))

    def rc_zoom_out_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.rc_zoom_out_xpath))

    def material_management_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.material_management_header_xpath))

    def mm_options_dropdown_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.mm_options_dropdown_xpath))

    def mm_report_dropdown_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.mm_report_dropdown_xpath))

    def zones_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zones_header_xpath))

    def zones_search_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.zones_search_id))

    def zones_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zones_filter_xpath))

    def filters_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.filters_xpath))

    def zones_addnewzone_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.zones_addnewzone_id))

    def zones_types_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.zones_types_id))

    def zonevisits_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zonevisits_header_xpath))

    def zv_search_assets_dropdown_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.zv_search_assets_dropdown_id))

    def zv_sort_dropdown_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.zv_sort_dropdown_id))

    def zv_summary_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.zv_summary_id))

    def zv_options_dropdown_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.zv_options_dropdown_id))

    def zone_types_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zone_types_header_xpath))

    def zt_add_zone_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.zt_add_zone_id))

    def zt_search_name_comment_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zt_search_name_comment_xpath))

    def search_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zt_search_name_comment_xpath))

    def zone_types_customer_is_displayed(self):
        self.wait_for_element_displayed((By.XPATH, LF.zone_types_customer_xpath))
        return self.element_is_displayed((By.XPATH, LF.zone_types_customer_xpath))

    def zone_types_home_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zone_types_home_xpath))

    def zone_types_inhouse_service_center_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zone_types_inhouse_service_center_xpath))

    def zone_types_office_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zone_types_office_xpath))

    def zone_types_vendor_service_center_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zone_types_vendor_service_center_xpath))

    def importzones_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.importzones_header_xpath))

    def importzones_options_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.importzones_options_id))

    def importzones_upload_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.importzones_upload_id))

    def importzones_table_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.importzones_table_xpath))

    def drivercongregation_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.drivercongregation_header_xpath))

    def assetlocationsharing_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.assetlocationsharing_header_xpath))

    def assetlocationsharing_sort_by_asset_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.assetlocationsharing_sort_by_asset_id))

    def linkedassets_header_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.linkedassets_header_xpath))

    def reports_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.reports_button_xpath))

    def linkedassets_groups_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.linkedassets_groups_xpath))

    def linkedassets_primary_asset_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.linkedassets_primary_asset_xpath))

    def linkedassets_linked_asset_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.linkedassets_linked_asset_xpath))

    def riskmanagement_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.riskmanagement_header_xpath))

    def options_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.options_xpath))

    def hoslogs_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.hoslogs_header_xpath))

    def unidentifieddriving_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.unidentifieddriving_header_xpath))

    def hosviolations_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.hosviolations_header_xpath))

    def hosavailability_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.hosavailability_header_xpath))

    def timecardreport_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.timecardreport_header_xpath))

    def iftareport_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.iftareport_header_xpath))

    def cleantruckcheckprogram_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.cleantruckcheckprogram_header_xpath))

    def assetinspection_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.assetinspection_header_xpath))

    def faults_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.faults_header_xpath))

    def filter_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.filter_button_xpath))

    def sort_by_fault_code_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.sort_by_fault_code_xpath))

    def report_button_in_fault_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.report_button_in_fault__xpath))

    def dismiss_faults_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.dismiss_faults_button_xpath))

    def columns_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.columns_button_xpath))

    def click_sort_by_fault_code_dropdown(self):
        self.click((By.XPATH, LF.sort_by_fault_code_drop_down_xpath))

    def get_fault_code_option_text(self):
        return self.get_text((By.XPATH, LF.fault_code_option_text_xpath))

    def get_description_option_text(self):
        return self.get_text((By.XPATH, LF.description_option_text_xpath))

    def get_times_logged_option_text(self):
        return self.get_text((By.XPATH, LF.times_logged_option_text_xpath))

    def get_source_option_text(self):
        return self.get_text((By.XPATH, LF.source_option_text_xpath))

    def get_severity_option_text(self):
        return self.get_text((By.XPATH, LF.severity_option_text_xpath))

    def click_columns_dropdown(self):
        self.click((By.XPATH, LF.columns_button_xpath))

    def get_fault_code_text(self):
        return self.get_text((By.XPATH, LF.fault_code_text_xpath))

    def get_description_text(self):
        return self.get_text((By.XPATH, LF.description_text_xpath))

    def get_current_status_text(self):
        return self.get_text((By.XPATH, LF.current_status_text_xpath))

    def get_times_logged_text(self):
        return self.get_text((By.XPATH, LF.times_logged_text_xpath))

    def get_source_text(self):
        return self.get_text((By.XPATH, LF.source_text_xpath))

    def get_protocol_text(self):
        return self.get_text((By.XPATH, LF.protocol_text_xpath))

    def get_advanced_details_text(self):
        return self.get_text((By.XPATH, LF.advanced_details_text_xpath))

    def get_selection_text(self):
        return self.get_text((By.XPATH, LF.selection_text_xpath))

    def get_severity_text(self):
        return self.get_text((By.XPATH, LF.severity_text_xpath))

    def get_controller_text(self):
        return self.get_text((By.XPATH, LF.controller_text_xpath))

    def measurements_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.measurements_header_xpath))

    def group_by_diagnostic_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.group_by_diagnostic_xpath))

    def report_button_in_measurement_page_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.report_button_measurement_page_xpath))

    def click_group_by_diagnostic_dropdown(self):
        self.click((By.XPATH, LF.group_by_diagnostic_dropdown_xpath))

    def get_diagnostic_option_text(self):
        return self.get_text((By.XPATH, LF.diagnostic_option_text_xpath))

    def speed_profile_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.speed_profile_header_xpath))

    def filter_button_in_speed_profile_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.filter_button_in_speed_profile_xpath))

    def view_trips_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.view_trips_button_xpath))

    def log_data_and_collisions_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.log_data_and_collisions_header_xpath))

    def reports_button_in_log_data_and_collisions_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.reports_button_log_data_and_collisions_xpath))

    def search_bar_log_data_and_collisions_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.search_bar_log_data_and_collisions_xpath))

    def filters_menu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.filters_menu_xpath))

    def sort_by_vehicle_and_date_time_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.sort_by_vehicle_and_date_time_xpath))

    def apply_changes_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.apply_changes_button_xpath))

    def click_filter_menu(self):
        self.click((By.XPATH, LF.filters_menu_xpath))

    def click_sort_by_vehicle_and_date_time_dropdown(self):
        self.click((By.XPATH, LF.sort_by_vehicle_and_date_time_dropdown_xpath))

    def get_vehicle_and_date_time_option_text(self):
        return self.get_text((By.XPATH, LF.vehicle_and_date_time_option_text_xpath))

    def get_reason_and_date_time_option_text(self):
        return self.get_text((By.XPATH, LF.reason_and_date_time_option_text_xpath))

    def get_record_type_and_date_time_option_text(self):
        return self.get_text((By.XPATH, LF.record_type_and_date_time_option_text_xpath))

    def maintenanceschedules_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.maintenanceschedules_header_xpath))

    def myreports_header_is_displayed(self):
        self.wait_for_element_displayed((By.XPATH, LF.myreports_header_xpath))
        return self.element_is_displayed((By.XPATH, LF.myreports_header_xpath))

    def rules_header_is_displayed(self):
        self.wait_for_element_displayed((By.XPATH, LF.rules_header_xpath))
        return self.element_is_displayed((By.XPATH, LF.rules_header_xpath))

    def safetysection_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.safetysection_id))

    def exceptions_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.exceptions_header_xpath))

    def message_header_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.message_header_xpath))

    def new_message_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.new_message_xpath))

    def notifications_header_is_displayed(self):
        self.wait_for_page_load()
        return self.wait_for_element_displayed((By.XPATH, LF.notifications_header_xpath))

    def notifications_types_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.notifications_types_xpath))

    def sustainabilityoverview_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.sustainabilityoverview_header_xpath))

    def mfuel_and_ev_energyusage_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.mfuel_and_ev_energyusage_header_xpath))

    def ev_batteryhealth_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.ev_batteryhealth_header_xpath))

    def ev_charginghistory_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.ev_charginghistory_header_xpath))

    def bev_rangecapability_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.bev_rangecapability_header_xpath))

    def assign_driver_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.assign_driver_header_xpath))

    def collisions_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.collisions_header_xpath))

    def fyinotify_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.fyinotify_header_xpath))

    def due_for_coaching_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.due_for_coaching_header_xpath))

    def opentasksreport_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.opentasksreport_header_xpath))

    def driversreport_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.driversreport_header_xpath))

    def groupreport_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.groupreport_header_xpath))

    def coachesreport_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.coachesreport_header_xpath))

    def programstatusreport_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.programstatusreport_header_xpath))

    def behaviorsreport_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.behaviorsreport_header_xpath))

    def events_header_is_displayed(self):
        if not self.element_is_displayed((By.XPATH, LF.events_header_xpath)):
            self.click_refresh_button()
        return self.wait_for_element_displayed((By.XPATH, LF.events_header_xpath))

    def coachinghistory_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.coachinghistory_header_xpath))

    def recognitionhistory_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.recognitionhistory_header_xpath))

    def dataexport_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.dataexport_header_xpath))

    def search_textbox_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.search_textbox_xpath))

    def vehicles_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.vehicles_header_xpath))

    def map_search_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.map_search_header_xpath))

    def saved_videos_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.saved_videos_header_xpath))

    def video_tags_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.video_tags_header_xpath))

    def users_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.users_header_xpath))

    def admin_vehicles_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.admin_vehicles_header_xpath))

    def telematics_assets_is_displayed(self):
        asset_header = self.element_is_displayed((By.XPATH, LF.telematics_assets_header_xpath))
        geotab_agreement = self.element_is_displayed((By.XPATH, LF.telematics_assets_agreement_xpath))
        if asset_header is True:
            return asset_header
        else:
            return geotab_agreement

    def devices_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.devices_header_xpath))

    def telematics_assets_tab_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.telematics_assets_tab_id))

    def telematics_cameras_tab_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.telematics_cameras_tab_id))

    def switch_to_frame_with_element_recursive(self, element_locator, timeout=20, depth=0):
        indent = "  " * depth
        try:
            self.find(element_locator)
            return True
        except TimeoutException:
            pass

        iframes = self.driver.find_elements(By.TAG_NAME, "iframe")

        for i, iframe in enumerate(iframes):
            self.driver.switch_to.frame(iframe)
            found = self.switch_to_frame_with_element_recursive(element_locator, timeout, depth + 1)
            if found:
                return True
            self.driver.switch_to.parent_frame()

        if depth == 0:
            self.driver.switch_to.default_content()
            print(f"{indent} Element not found in any iframe or default content after timeout.")
        return False

    def asset_header_is_displayed(self):
        self.switch_to_frame_with_element_recursive((By.XPATH, LF.telematics_assets_header_xpath))
        self.wait_for_element_displayed((By.XPATH, LF.telematics_assets_header_xpath))
        return self.element_is_displayed((By.XPATH, LF.telematics_assets_header_xpath))

    def geofences_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.geofences_header_xpath))

    def admin_insights_driver_id_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.admin_insights_driver_id_header_xpath))

    def config_settings_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.config_settings_header_xpath))

    def powertrain_fuel_types_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.powertrain_fuel_types_xpath))

    def emission_intensity_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.emission_intensity_xpath))

    def tailpipe_emissions_avoided_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.tailpipe_emissions_avoided_xpath))

    def fuel_energy_economy_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.fuel_energy_economy_xpath))

    def ev_charging_history_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.ev_charging_history_xpath))

    def fill_up_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.fill_up_xpath))

    def type_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.type_xpath))

    def click_custom_report(self):
        self.click((By.ID, LF.custom_report_id))

    def custom_report_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.custom_report_id))

    def custom_report_title_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.custom_report_title_xpath))

    def upload_file_is_displayed(self):
        try:
            if not self.element_is_displayed((By.XPATH, LF.upload_file_xpath)):
                self.click_custom_report()
        except (StaleElementReferenceException, TimeoutException):
            self.switch_ft_iframe()
            self.click_custom_report()
        return self.element_is_displayed((By.XPATH, LF.upload_file_xpath))

    def addrules_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.addrules_id))

    def click_addrules_button(self):
        self.click((By.ID, LF.addrules_id))

    def reprocessdata_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.reprocessdata_id))

    def report_setup_header_is_displayed(self):
        self.wait_for_page_to_fully_load()
        try:
            report_setup_header_displayed = self.wait_for_element_displayed((By.XPATH, LF.report_setup_header_xpath))
            if report_setup_header_displayed:
                return True
        except (StaleElementReferenceException, TimeoutException):
            self.switch_ft_iframe()
            return self.element_is_displayed((By.XPATH, LF.report_setup_header_xpath))
        return False

    def notification_template_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.notification_template_id))

    def distribution_lists_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.distribution_lists_id))

    def exception_rule_edit_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.exception_rule_edit_header_xpath))

    def save_button_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.save_button_id))

    def disabled_save_button_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.disabled_save_button_xpath))

    def cancel_button_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.cancel_button_id))

    def click_back_button(self):
        self.click((By.XPATH, LF.back_button_xpath))

    def name_tab_is_displayed(self):
        self.wait_for_element_displayed((By.ID, LF.name_tab_id))
        return self.element_is_displayed((By.ID, LF.name_tab_id))

    def condition_tab_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.condition_tab_id))

    def notifications_tab_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.notifications_tab_id))

    def media_tab_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.media_tab_id))

    def comment_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.comment_id))

    def assets_tab_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.assets_tab_id))

    def users_tab_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.users_tab_id))

    def reload_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.reload_id))

    def all_colors_displayed(self):
        for xpath in LF.color_xpaths:
            if not self.element_is_displayed((By.XPATH, xpath)):
                print(f"Color element not displayed: {xpath}")
                return False
        return True

    def system_settings_header_is_displayed(self):
        try:
            self.wait_for_element_displayed((By.XPATH, LF.system_settings_xpath))
        except (TimeoutException, NoSuchElementException):
            self.wait_for_element_displayed((By.XPATH, LF.system_settings_xpath))
        return True

    def general_tab_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.general_id))

    def maps_tab_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.maps_id))

    def hos_tab_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.hos_id))

    def edit_icon_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.edit_icon_xpath))

    def invisible_delete_icon_only_root_group_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.invisible_delete_icon_only_root_group_xpath))

    def delete_icon_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.delete_icon_xpath))

    def user_account_tab_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.userAccounts_id))

    def communications_tab_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.communications_id))

    def data_purge_tab_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.dataPurge_id))

    def addins_tab_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.addIns_xpath))

    def work_hours_header_is_displayed(self):
        self.wait_for_page_load()
        return self.element_is_displayed((By.XPATH, LF.work_hours_header_xpath))

    def work_hours_search_box_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.work_hours_search_id))

    def sort_by_name_button_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.work_hours_sort_button_id))

    def total_items_text_is_displayed(self):
        return self.get_text((By.ID, LF.total_items_text_id))

    def all_hours_text_is_displayed(self):
        return self.get_text((By.XPATH, LF.all_hours_text_xpath))

    def early_departure_hours_text_is_displayed(self):
        return self.get_text((By.XPATH, LF.early_departure_hours_text_xpath))

    def late_arrival_text_hours_is_displayed(self):
        return self.get_text((By.XPATH, LF.late_arrival_hours_text_xpath))

    def lunch_hours_text_is_displayed(self):
        return self.get_text((By.XPATH, LF.lunch_hours_text_xpath))

    def standard_hours_text_is_displayed(self):
        return self.get_text((By.XPATH, LF.standard_hours_text_xpath))

    def audit_log_header_is_displayed(self):
        self.wait_for_page_load()
        return self.element_is_displayed((By.XPATH, LF.audit_log_header_xpath))

    def audit_log_search_box_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.audit_log_search_id))

    def options_drop_down_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.options_dropdown_id))

    def user_login_text_is_displayed(self):
        return self.get_text((By.XPATH, LF.user_login_xpath))

    def get_work_order_management_page_title(self):
        self.wait_for_element_displayed((By.XPATH, LF.work_order_management_page_title_xpath))
        return self.get_text((By.XPATH, LF.work_order_management_page_title_xpath))

    def requests_tab_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.requests_tab_xpath))

    def orders_tab_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.orders_tab_xpath))

    def jobs_tab_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.jobs_tab_xpath))

    def schedules_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.schedules_button_xpath))

    def work_request_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.work_request_button_xpath))

    def groups_filter_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.group_filter_xpath))

    def assets_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.assets_filter_xpath))

    def filters_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.filters_xpath))

    def get_asset_column_name(self):
        return self.get_text((By.XPATH, LF.asset_column_title_xpath))

    def get_source_column_name(self):
        return self.get_text((By.XPATH, LF.source_column_title_xpath))

    def get_maintenance_type_column_name(self):
        return self.get_text((By.XPATH, LF.maintenance_type_column_title_xpath))

    def get_categories_column_name(self):
        return self.get_text((By.XPATH, LF.categories_column_title_xpath))

    def get_severity_column_name(self):
        return self.get_text((By.XPATH, LF.severity_column_title_xpath))

    def get_triggered_date_column_name(self):
        return self.get_text((By.XPATH, LF.triggered_column_title_xpath))

    def get_status_column_name(self):
        return self.get_text((By.XPATH, LF.status_column_title_xpath))

    def get_description_column_name(self):
        return self.get_text((By.XPATH, LF.description_column_title_xpath))

    def click_setting_icon(self):
        self.click((By.XPATH, LF.setting_icon_xpath))

    def get_asset_setting_name(self):
        return self.get_text((By.XPATH, LF.asset_setting_name_xpath))

    def get_source_setting_name(self):
        return self.get_text((By.XPATH, LF.source_setting_name_xpath))

    def get_maintenance_type_setting_name(self):
        return self.get_text((By.XPATH, LF.maintenance_type_setting_name_xpath))

    def get_categories_setting_name(self):
        return self.get_text((By.XPATH, LF.categories_setting_name_xpath))

    def get_severity_setting_name(self):
        return self.get_text((By.XPATH, LF.severity_setting_name_xpath))

    def get_triggered_date_setting_name(self):
        return self.get_text((By.XPATH, LF.triggered_date_setting_name_xpath))

    def get_status_setting_name(self):
        return self.get_text((By.XPATH, LF.status_setting_name_xpath))

    def get_description_setting_name(self):
        return self.get_text((By.XPATH, LF.description_setting_name_xpath))

    def get_is_overdue_setting_name(self):
        return self.get_text((By.XPATH, LF.is_overdue_setting_name_xpath))

    def get_current_odometer_setting_name(self):
        return self.get_text((By.XPATH, LF.current_odometer_setting_name_xpath))

    def get_service_due_on_odometer_setting_name(self):
        return self.get_text((By.XPATH, LF.service_due_on_odometer_setting_name_xpath))

    def get_service_due_on_engine_hours_setting_name(self):
        return self.get_text((By.XPATH, LF.service_due_on_engine_hours_setting_name_xpath))

    def get_current_engine_hours_setting_name(self):
        return self.get_text((By.XPATH, LF.current_engine_hours_setting_name_xpath))

    def get_due_on_date_setting_name(self):
        return self.get_text((By.XPATH, LF.due_on_date_setting_name_xpath))

    def get_service_due_in_kilometers_setting_name(self):
        return self.get_text((By.XPATH, LF.service_due_in_kilometers_setting_name_xpath))

    def get_service_due_in_miles_setting_name(self):
        return self.get_text((By.XPATH, LF.service_due_in_miles_setting_name_xpath))

    def get_service_due_in_hours_setting_name(self):
        return self.get_text((By.XPATH, LF.service_due_in_hours_setting_name_xpath))

    def get_last_engine_hours_setting_name(self):
        return self.get_text((By.XPATH, LF.last_engine_hours_setting_name_xpath))

    def get_last_maintenance_date_setting_name(self):
        return self.get_text((By.XPATH, LF.last_maintenance_date_setting_name_xpath))

    def get_last_odometer_setting_name(self):
        return self.get_text((By.XPATH, LF.last_odometer_setting_name_xpath))

    def get_expiration_date_setting_name(self):
        return self.get_text((By.XPATH, LF.expiration_date_setting_name_xpath))

    def click_filters_button(self):
        self.click((By.XPATH, LF.filters_xpath))

    def get_filters_pop_up_title(self):
        self.wait_for_element_is_clickable((By.XPATH, LF.filters_pop_up_title_xpath))
        return self.get_text((By.XPATH, LF.filters_pop_up_title_xpath))

    def get_groups_filter_option_in_pop_up(self):
        return self.get_text((By.XPATH, LF.groups_filter_option_xpath))

    def get_assets_filter_option_in_pop_up(self):
        return self.get_text((By.XPATH, LF.assets_filter_option_xpath))

    def get_include_archived_data_filter_option_in_pop_up(self):
        return self.get_text((By.XPATH, LF.include_archived_data_filter_option_xpath))

    def get_maintenance_types_filter_option_in_pop_up(self):
        return self.get_text((By.XPATH, LF.maintenance_types_filter_option_xpath))

    def get_sources_filter_option_in_pop_up(self):
        return self.get_text((By.XPATH, LF.sources_filter_option_xpath))

    def get_severity_filter_option_in_pop_up(self):
        return self.get_text((By.XPATH, LF.severity_filter_option_xpath))

    def get_show_snoozed_requests_filter_option_in_pop_up(self):
        return self.get_text((By.XPATH, LF.show_snoozed_requests_filter_option_xpath))

    def click_group_filter_in_filter_pop_up(self):
        self.click((By.XPATH, LF.group_filter_in_filter_pop_up_xpath))

    def select_asset_information_check_box(self):
        self.click((By.XPATH, LF.asset_information_check_box_xpath))

    def click_apply_button(self):
        self.click((By.XPATH, LF.apply_button_xpath))

    def close_group_drop_down(self):
        self.click((By.XPATH, LF.close_group_drop_down_xpath))

    def get_selected_group_filter_in_filters_pop_up(self):
        return self.get_attribute((By.XPATH, LF.selected_group_in_group_filter_xpath), "placeholder")

    def click_assets_filter_in_filter_pop_up(self):
        self.click((By.XPATH, LF.assets_filter_in_filter_pop_up_xpath))

    def select_asset_check_box(self):
        self.click((By.XPATH, LF.asset_check_box_xpath))

    def close_asset_drop_down(self):
        self.click((By.XPATH, LF.asset_drop_down_xpath))

    def get_selected_asset_filter_in_filters_pop_up(self):
        return self.element_is_displayed((By.XPATH, LF.selected_asset_filter_in_filters_pop_up_xpath))

    def click_maintenance_filter_in_filter_pop_up(self):
        self.click((By.XPATH, LF.maintenance_filter_in_filter_pop_up_xpath))

    def select_maintenance_check_box(self):
        self.click((By.XPATH, LF.maintenance_check_box_xpath))

    def close_maintenance_drop_down(self):
        self.click((By.XPATH, LF.maintenance_drop_down_xpath))

    def get_selected_maintenance_filter_in_filters_pop_up(self):
        return self.get_attribute((By.XPATH, LF.maintenance_filter_in_filter_pop_up_xpath), "placeholder")

    def click_sources_filter_in_filter_pop_up(self):
        self.click((By.XPATH, LF.sources_filter_in_filter_pop_up_xpath))

    def get_select_all_text(self):
        return self.get_text((By.XPATH, LF.select_all_checkbox_xpath))

    def get_manual_checkbox(self):
        return self.get_text((By.XPATH, LF.manual_checkbox_xpath))

    def get_data_insight_checkbox(self):
        return self.get_text((By.XPATH, LF.data_insight_checkbox_xpath))

    def get_scheduled_checkbox(self):
        return self.get_text((By.XPATH, LF.scheduled_checkbox_xpath))

    def get_driver_reported_checkbox(self):
        return self.get_text((By.XPATH, LF.driver_reported_checkbox_xpath))

    def get_faults_checkbox(self):
        return self.get_text((By.XPATH, LF.faults_checkbox_xpath))

    def click_manual_checkbox(self):
        self.click((By.XPATH, LF.manual_checkbox_xpath))

    def close_sources_drop_down(self):
        self.click((By.XPATH, LF.sources_drop_down_xpath))

    def is_manual_filter_applied(self):
        return self.element_is_displayed((By.XPATH, LF.manual_filter_applied_xpath))

    def click_severity_dropdown(self):
        self.click((By.XPATH, LF.severity_dropdown_xpath))

    def get_select_all_severity(self):
        return self.get_text((By.XPATH, LF.select_all_severity_xpath))

    def get_unknown_severity(self):
        return self.get_text((By.XPATH, LF.unknown_severity_xpath))

    def get_low_severity(self):
        return self.get_text((By.XPATH, LF.low_severity_xpath))

    def get_medium_severity(self):
        return self.get_text((By.XPATH, LF.medium_severity_xpath))

    def get_high_severity(self):
        return self.get_text((By.XPATH, LF.high_severity_xpath))

    def get_critical_severity(self):
        return self.get_text((By.XPATH, LF.critical_severity_xpath))

    def click_high_severity(self):
        self.click((By.XPATH, LF.high_severity_option_xpath))
        self.click_severity_dropdown()

    def get_applied_severity_filter(self):
        return self.get_attribute((By.XPATH, LF.applied_severity_filter_xpath), "placeholder")

    def close_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.close_button_xpath))

    def click_close_button(self):
        self.click((By.XPATH, LF.close_button_xpath))

    def click_orders_tab(self):
        self.click((By.XPATH, LF.orders_tab_xpath))

    def bulk_upload_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.bulk_upload_button_xpath))

    def work_order_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.work_order_xpath))

    def status_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.status_filter_xpath))

    def click_status_filter(self):
        self.click((By.XPATH, LF.status_filter_xpath))

    def get_open_dropdown_value(self):
        return self.get_text((By.XPATH, LF.open_dropdown_value_xpath))

    def get_assigned_dropdown_value(self):
        return self.get_text((By.XPATH, LF.assigned_dropdown_value_xpath))

    def get_in_progress_dropdown_value(self):
        return self.get_text((By.XPATH, LF.in_progress_dropdown_value_xpath))

    def get_on_hold_dropdown_value(self):
        return self.get_text((By.XPATH, LF.on_hold_dropdown_value_xpath))

    def get_completed_dropdown_value(self):
        return self.get_text((By.XPATH, LF.completed_dropdown_value_xpath))

    def get_canceled_dropdown_value(self):
        return self.get_text((By.XPATH, LF.canceled_dropdown_value_xpath))

    def get_clear_dropdown_value(self):
        return self.get_text((By.XPATH, LF.clear_dropdown_value_xpath))

    def get_cancel_dropdown_value(self):
        return self.get_text((By.XPATH, LF.cancel_dropdown_value_xpath))

    def get_apply_dropdown_value(self):
        return self.get_text((By.XPATH, LF.apply_dropdown_value_xpath))

    def get_order_reference_column_name(self):
        return self.get_text((By.XPATH, LF.order_reference_column_name_xpath))

    def get_date_started_column_name(self):
        return self.get_text((By.XPATH, LF.date_started_column_name_xpath))

    def get_date_created_column_name(self):
        return self.get_text((By.XPATH, LF.date_created_column_name_xpath))

    def get_date_completed_column_name(self):
        return self.get_text((By.XPATH, LF.date_completed_column_name_xpath))

    def get_priority_column_name(self):
        return self.get_text((By.XPATH, LF.priority_column_name_xpath))

    def get_asset_setting_name_in_order_page(self):
        return self.get_text((By.XPATH, LF.asset_setting_name_in_order_page_xpath))

    def get_order_reference_setting_name(self):
        return self.get_text((By.XPATH, LF.order_reference_setting_name_xpath))

    def get_date_created_setting_name(self):
        return self.get_text((By.XPATH, LF.date_created_setting_name_xpath))

    def get_date_completed_setting_name(self):
        return self.get_text((By.XPATH, LF.date_completed_setting_name_xpath))

    def get_priority_setting_name(self):
        return self.get_text((By.XPATH, LF.priority_setting_name_xpath))

    def get_status_setting_name_order_page(self):
        return self.get_text((By.XPATH, LF.status_setting_name_order_page_xpath))

    def get_engine_hours_reading_setting_name(self):
        return self.get_text((By.XPATH, LF.engine_hours_reading_setting_name_xpath))

    def get_odometer_reading_setting_name(self):
        return self.get_text((By.XPATH, LF.odometer_setting_name_xpath))

    def get_assigned_to_setting_name(self):
        return self.get_text((By.XPATH, LF.assigned_to_setting_name_xpath))

    def get_due_on_date_setting_name_order_page(self):
        return self.get_text((By.XPATH, LF.get_due_on_date_setting_name_order_page_xpath))

    def get_labor_costs_setting_name(self):
        return self.get_text((By.XPATH, LF.labor_costs_setting_name_xpath))

    def get_notes_setting_name(self):
        return self.get_text((By.XPATH, LF.notes_setting_name_xpath))

    def get_opened_by_setting_name(self):
        return self.get_text((By.XPATH, LF.opened_by_setting_name_xpath))

    def get_parts_cost_setting_name(self):
        return self.get_text((By.XPATH, LF.parts_cost_setting_name_xpath))

    def get_reason_for_repair_setting_name(self):
        return self.get_text((By.XPATH, LF.reason_for_repair_setting_name_xpath))

    def get_repair_class_setting_name(self):
        return self.get_text((By.XPATH, LF.get_repair_class_setting_name_xpath))

    def get_shipping_cost_setting_name(self):
        return self.get_text((By.XPATH, LF.shipping_cost_setting_name_xpath))

    def get_tax_cost_setting_name(self):
        return self.get_text((By.XPATH, LF.tax_cost_setting_name_xpath))

    def get_total_cost_setting_name(self):
        return self.get_text((By.XPATH, LF.total_cost_setting_name_xpath))

    def get_last_updated_setting_name(self):
        return self.get_text((By.XPATH, LF.last_updated_setting_name_xpath))

    def get_repair_site_setting_name(self):
        return self.get_text((By.XPATH, LF.repair_site_setting_name_xpath))

    def get_job_count_setting_name(self):
        return self.get_text((By.XPATH, LF.job_count_setting_name_xpath))

    def get_reset_setting_name(self):
        return self.get_text((By.XPATH, LF.reset_setting_name_xpath))

    def get_status_filter_option_in_pop_up(self):
        return self.get_text((By.XPATH, LF.status_filter_option_xpath))

    def get_date_created_filter_option_in_pop_up(self):
        return self.get_text((By.XPATH, LF.date_created_filter_option_xpath))

    def get_references_filter_option_in_pop_up(self):
        return self.get_text((By.XPATH, LF.references_filter_option_xpath))

    def get_priority_filter_option_in_pop_up(self):
        return self.get_text((By.XPATH, LF.priority_filter_option_xpath))

    def click_status_dropdown(self):
        self.click((By.XPATH, LF.status_drop_down_xpath))

    def click_open_status(self):
        self.click((By.XPATH, LF.open_status_xpath))

    def close_status_drop_down(self):
        self.click((By.XPATH, LF.status_drop_down_xpath))

    def get_applied_status_text(self):
        return self.get_attribute((By.XPATH, LF.applied_status_text_xpath), 'placeholder')

    def click_select_date_button(self):
        self.click((By.XPATH, LF.select_date_button_xpath))

    def get_date_created_header(self):
        return self.get_text((By.XPATH, LF.date_created_header_xpath))

    def click_today_option(self):
        self.click((By.XPATH, LF.today_option_xpath))

    def get_applied_date_filter_text(self):
        return self.get_text((By.XPATH, LF.applied_today_filter_xpath))

    def is_priority_low_visible(self):
        return self.element_is_displayed((By.XPATH, LF.priority_low_xpath))

    def is_priority_medium_visible(self):
        return self.element_is_displayed((By.XPATH, LF.priority_medium_xpath))

    def is_priority_high_visible(self):
        return self.element_is_displayed((By.XPATH, LF.priority_high_xpath))

    def is_priority_critical_visible(self):
        return self.element_is_displayed((By.XPATH, LF.priority_critical_xpath))

    def click_priority_low(self):
        self.click((By.XPATH, LF.priority_low_xpath))

    def is_priority_low_checked(self):
        return self.element_is_displayed((By.XPATH, LF.priority_low_checkbox_checked_xpath))

    def click_jobs_sub_tab(self):
        self.click((By.XPATH, LF.jobs_tab_xpath))

    def date_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.date_filter_jobs_page_xpath))

    def get_select_all_dropdown_value(self):
        return self.get_text((By.XPATH, LF.select_all_dropdown_value_xpath))

    def click_calender_filter(self):
        self.click((By.XPATH, LF.date_filter_jobs_page_xpath))

    def get_date_completed_text(self):
        return self.get_text((By.XPATH, LF.date_completed_text_xpath))

    def get_today_text(self):
        return self.get_text((By.XPATH, LF.today_text_xpath))

    def get_yesterday_text(self):
        return self.get_text((By.XPATH, LF.yesterday_text_xpath))

    def get_this_week_text(self):
        return self.get_text((By.XPATH, LF.this_week_text_xpath))

    def get_last_week_text(self):
        return self.get_text((By.XPATH, LF.last_week_text_xpath))

    def get_this_month_text(self):
        return self.get_text((By.XPATH, LF.this_month_text_xpath))

    def get_last_month_text(self):
        return self.get_text((By.XPATH, LF.last_month_text_xpath))

    def get_last_3_months_text(self):
        return self.get_text((By.XPATH, LF.last_3_months_text_xpath))

    def get_custom_text(self):
        return self.get_text((By.XPATH, LF.custom_text_xpath))

    def clear_button_is_present_and_disabled(self):
        return self.wait_for_element_displayed((By.XPATH, LF.clear_button_disabled_xpath))

    def get_asset_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.asset_setting_name_in_jobs_page_xpath))

    def get_order_reference_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.order_reference_setting_name_in_jobs_page_xpath))

    def get_source_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.source_setting_name_in_jobs_page_xpath))

    def get_maintenance_type_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.maintenance_type_setting_name_in_jobs_page_xpath))

    def get_categories_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.categories_setting_name_in_jobs_page_xpath))

    def get_status_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.status_setting_name_in_jobs_page_xpath))

    def get_date_started_setting_name(self):
        return self.get_text((By.XPATH, LF.date_started_setting_name_xpath))

    def get_date_completed_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.date_completed_setting_name_in_jobs_page_xpath))

    def get_date_created_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.date_created_setting_name_in_jobs_page_xpath))

    def get_triggered_date_setting_in_jobs_page_name(self):
        return self.get_text((By.XPATH, LF.triggered_date_setting_name_in_jobs_page_xpath))

    def get_engine_hours_reading_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.engine_hours_reading_setting_name_in_jobs_page_xpath))

    def get_odometer_reading_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.odometer_reading_setting_name_in_jobs_page_xpath))

    def get_hours_setting_name(self):
        return self.get_text((By.XPATH, LF.hours_setting_name_xpath))

    def get_labor_costs_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.labor_costs_setting_name_in_jobs_page_xpath))

    def get_parts_cost_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.parts_cost_setting_name_in_jobs_page_xpath))

    def get_shipping_cost_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.shipping_cost_setting_name_in_jobs_page_xpath))

    def get_tax_cost_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.tax_cost_setting_name_in_jobs_page_xpath))

    def get_total_cost_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.total_cost_setting_name_in_jobs_page_xpath))

    def get_priority_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.priority_setting_name_in_jobs_page_xpath))

    def get_reset_setting_name_in_jobs_page(self):
        return self.get_text((By.XPATH, LF.reset_setting_name_in_jobs_page_xpath))

    def schedule_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.schedule_button_xpath))

    def search_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.search_filter_xpath))

    def frequency_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.frequency_filter_xpath))

    def repeats_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.repeats_filter_xpath))

    def setting_icon_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.setting_icon_xpath))

    def get_name_column_text(self):
        return self.get_text((By.XPATH, LF.name_column_text_xpath))

    def get_categories_column_text(self):
        return self.get_text((By.XPATH, LF.categories_column_text_xpath))

    def get_repeats_column_text(self):
        return self.get_text((By.XPATH, LF.repeats_column_text_xpath))

    def get_frequency_column_text(self):
        return self.get_text((By.XPATH, LF.frequency_column_text_xpath))

    def get_assets_added_column_text(self):
        return self.get_text((By.XPATH, LF.assets_added_column_text_xpath))

    def click_frequency_drop_down(self):
        self.click((By.XPATH, LF.frequency_filter_xpath))

    def get_frequency_based_on_distance_text(self):
        return self.get_text((By.XPATH, LF.frequency_based_on_distance_text_xpath))

    def get_frequency_based_on_months_text(self):
        return self.get_text((By.XPATH, LF.frequency_based_on_months_text_xpath))

    def get_frequency_based_on_weeks_text(self):
        return self.get_text((By.XPATH, LF.frequency_based_on_weeks_text_xpath))

    def get_frequency_based_on_days_text(self):
        return self.get_text((By.XPATH, LF.frequency_based_on_days_text_xpath))

    def get_frequency_based_on_engine_hours_text(self):
        return self.get_text((By.XPATH, LF.frequency_based_on_engine_hours_text_xpath))

    def click_repeats_filter(self):
        self.click((By.XPATH, LF.repeats_filter_xpath))

    def get_yes_option_text(self):
        return self.get_text((By.XPATH, LF.yes_option_text_xpath))

    def get_no_option_text(self):
        return self.get_text((By.XPATH, LF.no_option_text_xpath))

    def get_name_setting_text(self):
        return self.get_text((By.XPATH, LF.name_setting_text_xpath))

    def get_categories_setting_text(self):
        return self.get_text((By.XPATH, LF.categories_setting_text_xpath))

    def get_repeats_setting_text(self):
        return self.get_text((By.XPATH, LF.repeats_setting_text_xpath))

    def get_frequency_setting_text(self):
        return self.get_text((By.XPATH, LF.frequency_setting_text_xpath))

    def get_assets_added_setting_text(self):
        return self.get_text((By.XPATH, LF.assets_added_setting_text_xpath))

    def get_days_setting_text(self):
        return self.get_text((By.XPATH, LF.days_setting_text_xpath))

    def get_weeks_setting_text(self):
        return self.get_text((By.XPATH, LF.weeks_setting_text_xpath))

    def get_months_setting_text(self):
        return self.get_text((By.XPATH, LF.months_setting_text_xpath))

    def get_day_of_week_setting_text(self):
        return self.get_text((By.XPATH, LF.day_of_week_setting_text_xpath))

    def get_day_of_month_setting_text(self):
        return self.get_text((By.XPATH, LF.day_of_month_setting_text_xpath))

    def get_engine_hours_setting_text(self):
        return self.get_text((By.XPATH, LF.engine_hours_setting_text_xpath))

    def get_distance_setting_text(self):
        return self.get_text((By.XPATH, LF.distance_setting_text_xpath))

    def get_event_date_setting_text(self):
        return self.get_text((By.XPATH, LF.event_date_setting_text_xpath))

    def get_source_setting_text(self):
        return self.get_text((By.XPATH, LF.source_setting_text_xpath))

    def search_bar_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.search_bar_xpath))

    def defect_lists_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.defect_lists_xpath))

    def report_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.report_button_xpath))

    def inspection_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.inspection_button_xpath))

    def sort_by_asset_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.sort_by_asset_xpath))

    def click_sort_by_asset_dropdown(self):
        self.click((By.XPATH, LF.sort_by_asset_drop_down_xpath))

    def click_linkedassets_title(self):
        self.click((By.XPATH, LF.linked_assets_title_xpath))
        self.wait_for_page_to_fully_load()

    def click_safe_driving_report_tab(self):
        self.click((By.XPATH, LF.safe_driving_report_tab_xpath))

    def get_asset_option_text(self):
        return self.get_text((By.XPATH, LF.asset_option_text_xpath))

    def get_date_option_text(self):
        return self.get_text((By.XPATH, LF.date_option_text_xpath))

    def get_duration_option_text(self):
        return self.get_text((By.XPATH, LF.duration_option_text_xpath))

    def get_setting_header_text(self):
        return self.get_text((By.XPATH, LF.setting_header_xpath))

    def get_group_header_text(self):
        return self.get_text((By.XPATH, LF.group_header_xpath))

    def get_minimum_distance_driven_header_text(self):
        return self.get_text((By.XPATH, LF.minimum_distance_driven_header_xpath))

    def click_settings_icon(self):
        self.click((By.XPATH, LF.settings_icon_in_asset_inspection_xpath))

    def get_reset_to_default_text(self):
        return self.get_text((By.XPATH, LF.reset_to_default_text_xpath))

    def get_date_and_time_text(self):
        return self.get_text((By.XPATH, LF.date_and_time_text_xpath))

    def get_asset_name_text(self):
        return self.get_text((By.XPATH, LF.asset_name_text_xpath))

    def get_driver_text(self):
        return self.get_text((By.XPATH, LF.driver_text_xpath))

    def get_status_text(self):
        return self.get_text((By.XPATH, LF.status_text_xpath))

    def get_defects_text(self):
        return self.get_text((By.XPATH, LF.defects_text_xpath))

    def get_comments_text(self):
        return self.get_text((By.XPATH, LF.comments_text_xpath))

    def get_inspection_type_text(self):
        return self.get_text((By.XPATH, LF.inspection_type_text_xpath))

    def get_asset_type_text(self):
        return self.get_text((By.XPATH, LF.asset_type_text_xpath))

    def get_certification_text(self):
        return self.get_text((By.XPATH, LF.certification_text_xpath))

    def get_duration_text(self):
        return self.get_text((By.XPATH, LF.duration_text_xpath))

    def name_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.name_field_xpath))

    def color_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.color_field_xpath))

    def publish_to_groups_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.publish_to_groups_field_xpath))

    def comment_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.comment_field_xpath))

    def click_publish_to_groups_drop_down(self):
        self.click((By.XPATH, LF.publish_to_groups_field_open_drop_down_xpath))

    def select_first_group_from_dropdown(self):
        self.click((By.XPATH, LF.first_group_in_dropdown_xpath))
        self.click((By.XPATH, LF.select_all_xpath))
        self.click((By.XPATH, LF.publish_to_groups_field_close_drop_down_xpath))  # Closing the dropdown

    def all_groups_displayed_in_dropdown(self):
        return self.get_text((By.XPATH, LF.first_group_list_xpath))

    def click_cross_mark_next_to_selected_groups(self):
        self.click((By.XPATH, LF.cross_mark_next_to_selected_group_xpath))

    def all_groups_removed(self):
        return self.element_is_displayed((By.XPATH, LF.cross_mark_next_to_selected_group_xpath))

    def click_condition_tab(self):
        self.click((By.ID, LF.condition_tab_id))

    def condition_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.condition_header_xpath))

    def engine_data_condition_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.engine_data_condition_xpath))

    def click_engine_data_condition(self):
        self.click((By.XPATH, LF.engine_data_condition_xpath))

    def get_active_fault_option_text(self):
        return self.get_text((By.XPATH, LF.active_fault_option_text_xpath))

    def get_any_fault_option_text(self):
        return self.get_text((By.XPATH, LF.any_fault_option_text_xpath))

    def get_measurement_or_data_option_text(self):
        return self.get_text((By.XPATH, LF.measurement_or_data_option_text_xpath))

    def engine_data_header_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.engine_data_header_in_engine_data_condition_id))

    def type_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.type_field_in_engine_data_condition_xpath))

    def diagnostic_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.diagnostic_field_in_engine_data_condition_xpath))

    def add_a_condition_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.add_a_condition_field_in_engine_data_condition_xpath))

    def display_all_diagnostic_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.display_all_diagnostic_field_in_engine_data_condition_xpath))

    def click_zone_or_zone_type_textbox(self):
        self.click((By.XPATH, LF.zone_or_zone_type_textbox_xpath))

    def zone_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zone_header_in_zone_condition_xpath))

    def get_type_option_text(self):
        return self.get_text((By.XPATH, LF.type_option_text_xpath))

    def get_zone_option_text(self):
        return self.get_text((By.XPATH, LF.zone_option_text_xpath))

    def get_event_option_text(self):
        return self.get_text((By.XPATH, LF.event_option_text_xpath))

    def get_entering_option_text(self):
        return self.get_text((By.XPATH, LF.entering_option_text_xpath))

    def get_exiting_option_text(self):
        return self.get_text((By.XPATH, LF.exiting_option_text_xpath))

    def get_outside_option_text(self):
        return self.get_text((By.XPATH, LF.outside_option_text_xpath))

    def get_inside_option_text(self):
        return self.get_text((By.XPATH, LF.inside_option_text_xpath))

    def add_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.add_button_xpath))

    def click_new_message_button(self):
        self.click((By.XPATH, LF.message_button_xpath))

    def new_message_popup_header_title(self):
        return self.get_text((By.XPATH, LF.new_message_popup_header_title_xpath))

    def new_message_popup_description(self):
        return self.get_text((By.XPATH, LF.new_message_popup_description_xpath))

    def search_filter_is_displayed_in_message_popup(self):
        return self.element_is_displayed((By.XPATH, LF.search_filter_in_message_popup_xpath))

    def compose_message_button_is_disabled(self):
        return self.element_is_displayed((By.XPATH, LF.compose_message_button_disabled_xpath))

    def assets_subtab_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.assets_subtab_xpath))

    def assets_list_with_checkboxes_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.assets_list_with_checkboxes_xpath))

    def click_users_subtab_in_message_popup(self):
        self.click((By.XPATH, LF.users_subtab_in_message_popup_xpath))

    def users_list_with_checkboxes_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.users_list_with_checkboxes_xpath))

    def select_any_user_in_message_popup(self):
        self.click((By.XPATH, LF.first_user_in_users_list_xpath))

    def click_compose_message_button(self):
        self.click((By.XPATH, LF.compose_message_button_xpath))

    def back_to_asset_selection_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.back_to_asset_selection_xpath))

    def user_name_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.user_name_xpath))

    def search_icon_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.search_icon_xpath))

    def cross_mark_symbol_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.cross_mark_symbol_xpath))

    def click_roads_with_speed_limit_textbox(self):
        self.click((By.XPATH, LF.roads_with_speed_limit_textbox_xpath))

    def roads_with_speed_limit_dialog_box_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.roads_with_speed_limit_dialog_box_xpath))

    def get_over_option_text(self):
        return self.get_text((By.XPATH, LF.over_option_text_xpath))

    def get_under_option_text(self):
        return self.get_text((By.XPATH, LF.under_option_text_xpath))

    def empty_text_box_under_over_and_under_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.empty_text_box_under_over_and_under_xpath))

    def click_speed_textbox(self):
        self.click((By.XPATH, LF.speed_textbox_xpath))

    def speed_dialog_box_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.speed_dialog_box_xpath))

    def click_speed_limit_textbox(self):
        self.click((By.XPATH, LF.speed_limit_textbox_xpath))

    def speed_limit_dialog_box_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.speed_limit_dialog_box_xpath))

    def truck_speed_limit_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.truck_speed_limit_field_xpath))

    def yes_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.yes_button_xpath))

    def no_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.no_button_xpath))

    def over_the_limit_by_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.over_the_limit_by_field_xpath))

    def exclude_estimated_speed_limits_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.exclude_estimated_speed_limits_field_xpath))

    def on_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.on_button_xpath))

    def off_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.off_button_xpath))

    def click_more_dropdown(self):
        self.click((By.XPATH, LF.more_dropdown_xpath))

    def get_device_header_text(self):
        return self.get_text((By.XPATH, LF.device_header_text_xpath))

    def get_ignition_option_text(self):
        return self.get_text((By.XPATH, LF.ignition_option_text_xpath))

    def get_driver_option_text(self):
        return self.get_text((By.XPATH, LF.driver_option_text_xpath))

    def get_group_option_text(self):
        return self.get_text((By.XPATH, LF.group_option_text_xpath))

    def get_asset_inspection_defect_option_text(self):
        return self.get_text((By.XPATH, LF.asset_inspection_defect_option_text_xpath))

    # Trip
    def get_trip_header_text(self):
        return self.get_text((By.XPATH, LF.trip_header_text_xpath))

    def get_driving_option_text(self):
        return self.get_text((By.XPATH, LF.driving_option_text_xpath))

    def get_stop_option_text(self):
        return self.get_text((By.XPATH, LF.stop_option_text_xpath))

    def get_trip_distance_option_text(self):
        return self.get_text((By.XPATH, LF.trip_distance_option_text_xpath))

    def get_trip_duration_option_text(self):
        return self.get_text((By.XPATH, LF.trip_duration_option_text_xpath))

    # Auxiliaries
    def get_auxiliaries_header_text(self):
        return self.get_text((By.XPATH, LF.auxiliaries_header_text_xpath))

    def get_aux_1_option_text(self):
        return self.get_text((By.XPATH, LF.aux_1_option_text_xpath))

    def get_aux_2_option_text(self):
        return self.get_text((By.XPATH, LF.aux_2_option_text_xpath))

    def get_aux_3_option_text(self):
        return self.get_text((By.XPATH, LF.aux_3_option_text_xpath))

    def get_aux_4_option_text(self):
        return self.get_text((By.XPATH, LF.aux_4_option_text_xpath))

    def get_aux_5_option_text(self):
        return self.get_text((By.XPATH, LF.aux_5_option_text_xpath))

    def get_aux_6_option_text(self):
        return self.get_text((By.XPATH, LF.aux_6_option_text_xpath))

    def get_aux_7_option_text(self):
        return self.get_text((By.XPATH, LF.aux_7_option_text_xpath))

    def get_aux_8_option_text(self):
        return self.get_text((By.XPATH, LF.aux_8_option_text_xpath))

    # Work Hours
    def get_work_hours_header_text(self):
        return self.get_text((By.XPATH, LF.work_hours_header_text_xpath))

    def get_after_work_hours_rule_option_text(self):
        return self.get_text((By.XPATH, LF.after_work_hours_rule_option_text_xpath))

    def get_work_hours_rule_option_text(self):
        return self.get_text((By.XPATH, LF.work_hours_rule_option_text_xpath))

    def get_after_work_hours_device_option_text(self):
        return self.get_text((By.XPATH, LF.after_work_hours_device_option_text_xpath))

    def get_device_work_hours_option_text(self):
        return self.get_text((By.XPATH, LF.device_work_hours_option_text_xpath))

    # Wrappers
    def get_wrappers_header_text(self):
        return self.get_text((By.XPATH, LF.wrappers_header_text_xpath))

    def get_is_value_more_than_option_text(self):
        return self.get_text((By.XPATH, LF.is_value_more_than_option_text_xpath))

    def get_is_value_less_than_option_text(self):
        return self.get_text((By.XPATH, LF.is_value_less_than_option_text_xpath))

    def get_is_value_equal_to_option_text(self):
        return self.get_text((By.XPATH, LF.is_value_equal_to_option_text_xpath))

    # Logic
    def get_logic_header_text(self):
        return self.get_text((By.XPATH, LF.logic_header_text_xpath))

    def get_and_option_text(self):
        return self.get_text((By.XPATH, LF.and_option_text_xpath))

    def get_or_option_text(self):
        return self.get_text((By.XPATH, LF.or_option_text_xpath))

    def click_notifications_tab(self):
        return self.click((By.XPATH, LF.notifications_tab_xpath))

    def notifications_recipients_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.notifications_recipients_header_xpath))

    def add_email_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.add_email_option_xpath))

    def add_alert_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.add_alert_option_xpath))

    def add_driver_feedback_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.add_driver_feedback_option_xpath))

    def more_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.more_option_xpath))

    def help_section_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.help_section_xpath))

    def summary_in_help_section_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.summary_in_help_section_xpath))

    # --- Add Email ---
    def click_add_email_option(self):
        return self.click((By.XPATH, LF.add_email_option_xpath))

    def template_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.template_field_xpath))

    def email_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.email_field_xpath))

    def click_template_dropdown(self):
        return self.click((By.XPATH, LF.template_dropdown_xpath))

    def get_default_email_template_option_text(self):
        return self.get_text((By.XPATH, LF.default_email_template_option_text_xpath))

    def get_add_new_template_option_text(self):
        return self.get_text((By.XPATH, LF.add_new_template_option_text_xpath))

    def click_add_new_template_option(self):
        return self.click((By.XPATH, LF.add_new_template_option_text_xpath))

    def warning_popup_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.warning_popup_xpath))

    def click_email_textbox(self):
        return self.click((By.XPATH, LF.email_textbox_xpath))

    def email_dropdown_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.email_dropdown_xpath))

    def click_add_alert_dropdown(self):
        return self.click((By.XPATH, LF.add_alert_dropdown_xpath))

    def get_popup_option_text(self):
        return self.get_text((By.XPATH, LF.popup_option_text_xpath))

    def get_popup_description_option_text(self):
        return self.get_text((By.XPATH, LF.popup_description_xpath))

    def get_urgent_popup_option_text(self):
        return self.get_text((By.XPATH, LF.urgent_popup_option_text_xpath))

    def get_urgent_popup_description_text(self):
        return self.get_text((By.XPATH, LF.urgent_popup_description_xpath))

    def get_log_only_option_text(self):
        return self.get_text((By.XPATH, LF.log_only_option_text_xpath))

    def get_log_only_description_text(self):
        return self.get_text((By.XPATH, LF.log_only_description_xpath))

    def click_add_driver_feedback_dropdown(self):
        return self.click((By.XPATH, LF.add_driver_feedback_dropdown_xpath))

    def get_beep_three_times_text(self):
        return self.get_text((By.XPATH, LF.beep_three_times_option_text_xpath))

    def get_beep_three_times_description_text(self):
        return self.get_text((By.XPATH, LF.beep_three_times_description_xpath))

    def get_beep_three_times_rapidly_text(self):
        return self.get_text((By.XPATH, LF.beep_three_times_rapidly_option_text_xpath))

    def get_beep_three_times_rapidly_description_text(self):
        return self.get_text((By.XPATH, LF.beep_three_times_rapidly_description_xpath))

    def get_beep_ten_times_rapidly_text(self):
        return self.get_text((By.XPATH, LF.beep_ten_times_rapidly_option_text_xpath))

    def get_beep_ten_times_rapidly_description_text(self):
        return self.get_text((By.XPATH, LF.beep_ten_times_rapidly_description_xpath))

    def get_text_message_option_text(self):
        return self.get_text((By.XPATH, LF.text_message_option_text_xpath))

    def get_text_message_description_text(self):
        return self.get_text((By.XPATH, LF.text_message_description_xpath))

    def get_go_talk_option_text(self):
        return self.get_text((By.XPATH, LF.go_talk_option_text_xpath))

    def get_go_talk_description_text(self):
        return self.get_text((By.XPATH, LF.go_talk_description_xpath))

    def get_change_status_option_text(self):
        return self.get_text((By.XPATH, LF.change_status_option_text_xpath))

    def get_change_status_description_text(self):
        return self.get_text((By.XPATH, LF.change_status_description_xpath))

    def click_more_options_dropdown(self):
        return self.click((By.XPATH, LF.more_options_dropdown_xpath))

    def get_web_request_option_text(self):
        return self.get_text((By.XPATH, LF.web_request_option_text_xpath))

    def get_web_request_description_text(self):
        return self.get_text((By.XPATH, LF.web_request_description_xpath))

    def get_assign_to_group_option_text(self):
        return self.get_text((By.XPATH, LF.assign_to_group_option_text_xpath))

    def get_assign_to_group_description_text(self):
        return self.get_text((By.XPATH, LF.assign_to_group_description_xpath))

    def get_email_to_group_option_text(self):
        return self.get_text((By.XPATH, LF.email_to_group_option_text_xpath))

    def get_email_to_group_description_text(self):
        return self.get_text((By.XPATH, LF.email_to_group_description_xpath))

    def get_distribution_list_option_text(self):
        return self.get_text((By.XPATH, LF.distribution_list_option_text_xpath))

    def get_distribution_list_description_text(self):
        return self.get_text((By.XPATH, LF.distribution_list_description_xpath))

    def get_assign_as_personal_business_option_text(self):
        return self.get_text((By.XPATH, LF.assign_as_personal_business_option_text_xpath))

    def get_assign_as_personal_business_description_text(self):
        return self.get_text((By.XPATH, LF.assign_as_personal_business_description_xpath))

    def click_media_upload_tab(self):
        return self.click((By.XPATH, LF.media_upload_tab_xpath))

    def media_upload_settings_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.media_upload_settings_header_xpath))

    def media_type_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.media_type_field_xpath))

    def information_symbol_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.information_symbol_xpath))

    def hover_on_information_symbol(self):
        element = self.find((By.XPATH, LF.information_symbol_xpath))
        return self.move_to_element(element)

    def information_symbol_message_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.information_symbol_message_xpath))

    def video_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.video_button_xpath))

    def snapshot_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.snapshot_button_xpath))

    def none_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.none_button_xpath))

    def click_cancel_button(self):
        return self.click((By.XPATH, LF.cancel_button_xpath))

    def click_notification_template_button(self):
        return self.click((By.XPATH, LF.notification_template_button_xpath))

    def notification_templates_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.notification_templates_header_xpath))

    def search_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.search_option_xpath))

    def sort_by_name_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.sort_by_name_option_xpath))

    def add_email_template_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.add_email_template_option_xpath))

    def add_web_template_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.add_web_template_option_xpath))

    def add_text_template_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.add_text_template_option_xpath))

    def click_add_email_template_button(self):
        return self.click((By.XPATH, LF.add_email_template_button_xpath))

    def email_template_edit_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.email_template_edit_header_xpath))

    def subject_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.subject_field_xpath))

    def body_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.body_field_xpath))

    def exception_report_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.exception_report_field_xpath))

    def click_do_not_attach_exceptions_detail_report_dropdown(self):
        return self.click((By.XPATH, LF.do_not_attach_exceptions_detail_report_dropdown_xpath))

    def get_do_not_attach_exceptions_detail_report_option_text(self):
        return self.get_text((By.XPATH, LF.do_not_attach_exceptions_detail_report_option_text_xpath))

    def get_default_exceptions_detail_report_option_text(self):
        return self.get_text((By.XPATH, LF.default_exceptions_detail_report_option_text_xpath))

    def get_possible_collisions_option_text(self):
        return self.get_text((By.XPATH, LF.possible_collisions_option_text_xpath))

    def get_advanced_exceptions_detail_report_option_text(self):
        return self.get_text((By.XPATH, LF.advanced_exceptions_detail_report_option_text_xpath))

    def get_tokens_name(self, index):
        return self.get_text(
            (By.XPATH, f"(//*[@class='template-token-list__token-row noTranslate tokenRow'][{index}]/button)"))

    def get_token_description(self, index):
        return self.get_text(
            (By.XPATH, f"(//*[@class='template-token-list__token-row noTranslate tokenRow'][{index}]/span)"))

    def click_cancel_button_in_email_template_edit_page(self):
        return self.click((By.XPATH, LF.cancel_button_in_email_template_edit_page_xpath))

    def click_add_web_template_button(self):
        return self.click((By.XPATH, LF.add_web_template_button_xpath))

    def web_request_template_edit_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.web_request_template_edit_header_xpath))

    def template_name_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.template_name_field_xpath))

    def url_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.url_field_xpath))

    def http_request_type_field_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.http_request_type_field_xpath))

    def available_tokens_section_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.available_tokens_section_xpath))

    def get_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.get_button_xpath))

    def post_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.post_button_xpath))

    def linked_assets_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.linked_assets_xpath))

    def installation_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.installation_xpath))

    def asset_reports_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.asset_reports_button_xpath))

    def create_assets_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.create_assets_button_xpath))

    def click_addins_tab(self):
        self.wait_for_element_displayed((By.XPATH, LF.addIns_xpath))
        self.wait_for_element_is_clickable((By.XPATH, LF.addIns_xpath))
        try:
            self.click((By.XPATH, LF.addIns_xpath))
        except (TimeoutException, NoSuchElementException):
            self.click((By.XPATH, LF.addIns_xpath))
        return True

    def click_save_config_button(self):
        self.scroll_page_up()
        self.click((By.ID, LF.save_config_id))

    def save_button_state_is_enabled(self):
        return self.wait_for_element_enabled((By.ID, LF.save_config_id))

    def click_delete_icon_of_selected_add_ins(self):
        self.click((By.XPATH, LF.addIns_delete_icon_xpath))

    def search_delete_existing_add_ins(self, add_in_name: str):
        delete_xpath = (
            f"//div[contains(@class,'editable-list-item__body')]"
            f"[.//div[contains(@class,'editable-list-item__text') and normalize-space()='{add_in_name}']]"
            f"//button[@data-name='IconDelete2']"
        )
        try:
            delete_element = self.find((By.XPATH, delete_xpath))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", delete_element)
            self.wait_for_element_is_clickable((By.XPATH, delete_xpath))
            delete_element.click()
            print(f" Scrolled to and clicked delete for add-in: {add_in_name}")
        except Exception as e:
            print(f" Could not delete add-in '{add_in_name}': {e}")

    def click_create_add_ins(self):
        self.click((By.XPATH, LF.create_add_in_xpath))

    def click_config_text_area(self):
        self.click((By.XPATH, LF.config_text_area_xpath))

    def fbt_in_list_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.fbt_in_list_xpath))

    def add_config_in_text_area(self, new_config_data: str):
        textarea = self.find((By.XPATH, LF.config_text_area_xpath))
        textarea.click()
        textarea.clear()
        textarea.send_keys(Keys.CONTROL + "a")
        textarea.send_keys(Keys.DELETE)
        textarea.send_keys(Keys.CONTROL + "a")
        textarea.send_keys(Keys.DELETE)
        textarea.send_keys(new_config_data)
        sleep(1)
        self.click((By.XPATH, LF.config_done_xpath))

    def fbt_header_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.fbt_header_xpath))

    def hos_driver_summary_header_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.hos_driver_summary_header_xpath))

    def compliance_data_summary_tab_in_map_is_displayed(self):
        self.click((By.XPATH, LF.map_show_addin_icon_xpath))
        return self.wait_for_element_displayed((By.XPATH, LF.compliance_data_summary_tab_in_map_xpath))

    def import_hos_logs_header_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.import_hos_logs_header_xpath))

    def evsa_header_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.evsa_header_xpath))

    def eld_settings_validator_header_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.eld_settings_validator_header_xpath))

    def eld_support_header_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.eld_support_header_xpath))

    def addin_header_is_displayed_new_ui(self, addin_name):
        headers = {
            "import hos logs": LF.import_hos_logs_header_xpath,
            "evsa": LF.evsa_header_xpath,
            "eld settings validator": LF.eld_settings_validator_header_xpath,
            "eld info config": LF.eld_support_header_xpath,
            "hos driver summary": LF.hos_driver_summary_header_xpath,
            "fbt": LF.fbt_header_xpath,
        }
        header_xpath = headers.get(addin_name)
        if not header_xpath:
            raise ValueError(f"Unknown add-in name: {addin_name}")
        self.wait_for_page_to_fully_load()
        self.scroll_page_up()
        self.wait_for_element_displayed((By.XPATH, header_xpath))
        return self.element_is_displayed((By.XPATH, header_xpath))

    def holidays_header_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.holidays_header_xpath))

    def click_add_holiday_button(self):
        self.click((By.ID, LF.add_work_holiday_id))

    def add_holiday_button_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.add_work_holiday_id))

    def holiday_name_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.holiday_name_id))

    def holiday_date_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.holiday_date_id))

    def holiday_group_id_is_displayed(self):
        return self.element_is_displayed((By.ID, LF.holiday_group_id))

    def add_holiday_page_header_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, LF.add_holiday_header_xpath))

    def cancel_holiday_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.cancel_holiday_xpath))

    def save_holiday_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.save_holiday_xpath))

    def default_group_id_value_1_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.default_group_id_xpath))

    def name_column_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.name_column_header_xpath))

    def date_column_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.date_column_header_xpath))

    def group_column_header_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.group_column_header_xpath))