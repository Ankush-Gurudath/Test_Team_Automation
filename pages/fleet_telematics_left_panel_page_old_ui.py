from selenium.webdriver.common.by import By
from locators.locators_fleet_telematics_left_panel_old_ui import LocatorsFleetTelematicsLeftPanelOldUI as LF
from pages.base_page import BasePage


class FleetTelematicsPageLeftPanelOldUI(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def more_charts_button_is_displayed(self):
        self.wait_for_page_load()
        return self.element_is_displayed((By.ID, LF.more_charts_button))

    def switch_ft_iframe(self):
        self.wait_for_page_to_fully_load()
        if self.element_is_displayed((By.CLASS_NAME, LF.iframe_class)) is True:
            self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, LF.iframe_class))

    def click_dashboard_menu(self):
        self.click((By.XPATH, LF.dashboard_menu_xpath))
        self.wait_for_page_load()

    def click_map_menu(self):
        self.click((By.XPATH, LF.map_menu_xpath))
        self.wait_for_page_load()
        self.wait_for_page_load()

    def click_compliance_menu(self):
        self.wait_for_element_is_clickable((By.XPATH, LF.compliance_menu_xpath))
        self.click((By.XPATH, LF.compliance_menu_xpath))

    def click_productivity_menu(self):
        self.click((By.XPATH, LF.productivity_menu_xpath))

    def click_maintenance_menu(self):
        self.wait_for_element_is_clickable((By.XPATH, LF.maintenance_menu_xpath))
        self.click((By.XPATH, LF.maintenance_menu_xpath))

    def click_sustainability_menu(self):
        self.click((By.XPATH, LF.sustainability_menu_xpath))

    def click_reports_menu(self):
        self.click((By.XPATH, LF.reports_menu_xpath))

    def click_myreports_submenu(self):
        self.click((By.XPATH, LF.myreports_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_report_setup_submenu(self):
        self.click((By.XPATH, LF.reportsetup_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_rules_submenu(self):
        self.click((By.XPATH, LF.rules_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_exceptions_submenu(self):
        self.click((By.XPATH, LF.exceptions_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_reports_menu_dropdown(self):
        self.click((By.XPATH, LF.reports_menu_xpath))

    def click_notifications_menu(self):
        self.click((By.XPATH, LF.notifications_menu_xpath))
        self.wait_for_page_to_fully_load()

    def click_config_menu(self):
        self.click((By.XPATH, LF.config_menu_xpath))
        self.wait_for_page_to_fully_load()

    def click_fleet_settings_submenu(self):
        self.click((By.XPATH, LF.fleet_settings_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_work_hours_submenu(self):
        self.click((By.XPATH, LF.work_hours_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_audit_log_submenu(self):
        self.click((By.XPATH, LF.audit_log_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_messages_menu(self):
        self.click((By.XPATH, LF.messages_menu_xpath))
        self.wait_for_page_to_fully_load()

    def click_rulesandexceptions_menu(self):
        self.click((By.XPATH, LF.rulesandexceptions_menu_xpath))

    def click_rulesandexceptions_menu_dropdown(self):
        self.click((By.XPATH, LF.rulesandexceptions_menu_xpath))

    def click_routes_submenu_dropdown(self):
        self.click((By.XPATH, LF.routes_submenu_dropdown_xpath))

    def click_routes_subchild(self):
        self.click((By.XPATH, LF.routes_subchild_xpath))

    def click_plannedvsactualroutes_subchild(self):
        self.click((By.XPATH, LF.plannedvsactualroutes_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_routesummary_subchild(self):
        self.click((By.XPATH, LF.routesummary_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_routecompletion_subchild(self):
        self.click((By.XPATH, LF.routecompletion_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_materialmanagement_subchild(self):
        self.click((By.XPATH, LF.materialmanagement_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_zones_submenu(self):
        self.click((By.XPATH, LF.zones_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_zones_subchild(self):
        self.click((By.XPATH, LF.zones_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_zonetypes_subchild(self):
        self.click((By.XPATH, LF.zonetypes_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_zonevisits_subchild(self):
        self.click((By.XPATH, LF.zonevisits_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_importzones_subchild(self):
        self.click((By.XPATH, LF.importzones_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_importroutes_subchild(self):
        self.click((By.XPATH, LF.importroutes_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_assetlocationsharing_submenu(self):
        self.click((By.XPATH, LF.assetlocationsharing_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_linkedassets_submenu(self):
        self.click((By.XPATH, LF.linkedassets_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_riskmanagement_submenu(self):
        self.click((By.XPATH, LF.riskmanagement_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_compliance_menu_dropdown(self):
        self.click((By.XPATH, LF.compliance_menu_dropdown_xpath))

    def click_unmatchedroute_subchild_dropdown(self):
        self.click((By.XPATH, LF.unmatchedroute_subchild_xpath))

    def click_publicworks_submenu_dropdown(self):
        self.wait_for_element_is_clickable((By.XPATH, LF.publicworks_submenu_dropdown_xpath))
        self.click((By.XPATH, LF.publicworks_submenu_dropdown_xpath))

    def click_zones_submenu_dropdown(self):
        self.click((By.XPATH, LF.zones_submenu_dropdown_xpath))

    def click_drivercongregation_submenu(self):
        self.click((By.XPATH, LF.drivercongregation_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_driskmanagement_submenu(self):
        self.click((By.XPATH, LF.riskmanagement_submenu_xpath))

    def click_triphistory_submenu(self):
        self.click((By.XPATH, LF.triphistory_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_hos_submenu_dropdown(self):
        self.click((By.XPATH, LF.hos_submenu_dropdown_xpath))

    def click_hos_submenu(self):
        self.click((By.XPATH, LF.hos_submenu_xpath))

    def click_hoslogs_subchild(self):
        self.click((By.XPATH, LF.logs_xpath))
        self.wait_for_page_to_fully_load()

    def click_unidentified_driving_subchild(self):
        self.click((By.XPATH, LF.unidentified_driving_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_violations_subchild(self):
        self.click((By.XPATH, LF.violations_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_availability_subchild(self):
        self.click((By.XPATH, LF.availability_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_timecardreport_submenu(self):
        self.click((By.XPATH, LF.timecardreport_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_iftareport_submenu(self):
        self.click((By.XPATH, LF.iftareport_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_cleantruckcheck_submenu(self):
        self.click((By.XPATH, LF.cleantruckcheck_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_assetinspection_submenu(self):
        self.click((By.XPATH, LF.assetinspection_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_reminders_submenu(self):
        self.click((By.XPATH, LF.reminders_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_faults_subchild(self):
        self.click((By.XPATH, LF.faults_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_measurements_subchild(self):
        self.click((By.XPATH, LF.measurements_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_speed_profile_subchild(self):
        self.click((By.XPATH, LF.speed_profile_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_log_data_and_collisions_subchild(self):
        self.click((By.XPATH, LF.Log_data_and_collisions_subchild_xpath))
        self.wait_for_page_to_fully_load()

    def click_sustainabilitycenter_submenu(self):
        self.click((By.XPATH, LF.sustainabilitycenter_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_fuel_energy_usage_submenu(self):
        self.click((By.XPATH, LF.fuel_energy_usage_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_evbatteryhealth_submenu(self):
        self.click((By.XPATH, LF.evbatteryhealth_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_evcharginghistory_submenu(self):
        self.click((By.XPATH, LF.evcharginghistory_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_bevrangecapability_submenu(self):
        self.click((By.XPATH, LF.bevrangecapability_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_arrow_left_direction(self):
        self.click((By.XPATH, LF.arrow_left_direction))

    def click_arrow_right_direction(self):
        self.click((By.XPATH, LF.arrow_right_direction))

    def click_fyinotify_submenu(self):
        self.click((By.XPATH, LF.fyinotify_submenu_xpath))
        self.wait_for_page_to_fully_load()

    def click_collisions_submenu(self):
        self.click((By.XPATH, LF.collisions_submenu_xpath))

    def click_due_for_coaching_submenu(self):
        self.click((By.XPATH, LF.due_for_coaching_submenu_xpath))

    def click_assign_drivers_submenu(self):
        self.click((By.XPATH, LF.assign_drivers_submenu_xpath))

    def click_insights_menu(self):
        self.click((By.XPATH, LF.insights_menu_xpath))

    def click_open_tasks_report_submenu(self):
        self.click((By.XPATH, LF.open_tasks_report_submenu_xpath))

    def click_drivers_report_submenu(self):
        self.click((By.XPATH, LF.drivers_report_submenu_xpath))

    def click_group_report_submenu(self):
        self.click((By.XPATH, LF.group_report_submenu_xpath))

    def click_coaches_report_submenu(self):
        self.click((By.XPATH, LF.coaches_report_submenu_xpath))

    def click_library_menu(self):
        self.click((By.XPATH, LF.library_menu_xpath))

    def click_program_status_report_submenu(self):
        self.click((By.XPATH, LF.program_status_report_submenu_xpath))

    def click_behaviors_report_submenu(self):
        self.click((By.XPATH, LF.behaviors_report_submenu_xpath))

    def click_events_submenu(self):
        self.click((By.XPATH, LF.events_submenu_xpath))

    def click_coachinghistory_submenu(self):
        self.click((By.XPATH, LF.coachinghistory_submenu_xpath))

    def click_recognitionhistory_submenu(self):
        self.click((By.XPATH, LF.recognitionhistory_submenu_xpath))

    def click_dataexport_submenu(self):
        self.click((By.XPATH, LF.dataexport_submenu_xpath))

    def click_search_submenu_old_ui(self):
        self.click((By.XPATH, LF.search_submenu_xpath_old_ui))

    def click_vehicles_menu(self):
        self.click((By.XPATH, LF.vehicles_menu_xpath))

    def click_map_search_menu(self):
        self.click((By.XPATH, LF.map_search_menu_xpath))

    def click_vs_library_menu(self):
        self.click((By.XPATH, LF.vs_library_menu_xpath))

    def click_saved_videos_submenu(self):
        self.click((By.XPATH, LF.saved_videos_submenu_xpath))

    def click_video_tags_submenu(self):
        self.click((By.XPATH, LF.video_tags_submenu_xpath))

    def click_users_menu(self):
        self.click((By.XPATH, LF.users_menu_xpath))

    def click_admin_vehicles_menu(self):
        self.click((By.XPATH, LF.admin_vehicles_menu_xpath))

    def click_telematics_assets_menu(self):
        self.click((By.XPATH, LF.telematics_assets_menu_xpath))
        self.wait_for_page_to_fully_load()

    def click_telematics_assets_menu_old_ui(self):
        self.click((By.XPATH, LF.telematics_assets_menu_xpath_old_ui))

    def click_devices_menu(self):
        self.click((By.XPATH, LF.devices_menu_xpath))

    def click_geofences_menu(self):
        self.click((By.XPATH, LF.geofences_menu_xpath))

    def click_admin_insights_menu(self):
        self.click((By.XPATH, LF.admin_insights_menu_xpath))

    def click_insights_driver_id_menu(self):
        self.click((By.XPATH, LF.insights_driver_id_menu_xpath))

    def click_config_settings_menu(self):
        self.click((By.XPATH, LF.config_settings_menu_xpath))

    def wait_for_fleet_telematics_page_load(self):
        return self.wait_for_element_displayed((By.XPATH, LF.telematicsLoaded_xpath))

    def lytx_geotab_logo_is_displayed(self):
        self.wait_for_element_displayed((By.XPATH, LF.lytx_geotab_logo_xpath))
        return self.element_is_displayed((By.XPATH, LF.lytx_geotab_logo_xpath))

    def left_navigation_expand_mode_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.left_navigation_expand_mode_xpath))

    def left_navigation_collapse_mode_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.left_navigation_collapse_mode_xpath))

    def arrow_right_direction_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.arrow_right_direction))

    def arrow_left_direction_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.arrow_left_direction))

    def dashboard_menu_is_displayed(self):
        self.wait_for_element_displayed((By.XPATH, LF.dashboard_menu_xpath))
        return self.element_is_displayed((By.XPATH, LF.dashboard_menu_xpath))

    def map_menu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.map_menu_xpath))

    def productivity_menu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.productivity_menu_xpath))

    def maintenance_menu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.maintenance_menu_xpath))

    def compliance_menu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.compliance_menu_xpath))

    def sustainability_menu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.sustainability_menu_xpath))

    def reports_menu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.reports_menu_xpath))

    def rulesandexceptions_menu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.rulesandexceptions_menu_xpath))

    def messages_menu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.messages_menu_xpath))

    def notifications_menu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.notifications_menu_xpath))

    def addins_menu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.addins_menu_xpath))

    def marketplace_menu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.marketplace_menu_xpath))

    def config_menu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.config_menu_xpath))

    def trip_history_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.triphistory_submenu_xpath))

    def routes_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.routes_submenu_xpath))

    def plannedvsactualroutes_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.plannedvsactualroutes_subchild_xpath))

    def routesummary_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.routesummary_subchild_xpath))

    def unmatchedroute_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.unmatchedroute_subchild_xpath))

    def importroutes_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.importroutes_subchild_xpath))

    def publicworks_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.publicworks_submenu_xpath))

    def routecompletion_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.routecompletion_subchild_xpath))

    def materialmanagement_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.materialmanagement_subchild_xpath))

    def zones_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zones_submenu_xpath))

    def zones_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zones_subchild_xpath))

    def zonetypes_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zonetypes_subchild_xpath))

    def zonevisits_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zonevisits_subchild_xpath))

    def importzones_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.importzones_subchild_xpath))

    def drivercongregation_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.drivercongregation_submenu_xpath))

    def assetlocationsharing_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.assetlocationsharing_submenu_xpath))

    def linkedassets_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.linkedassets_submenu_xpath))

    def riskmanagement_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.riskmanagement_submenu_xpath))

    def productivity_menu_dropdown_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.productivity_menu_dropdown_xpath))

    def routes_submenu_dropdown_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.routes_submenu_dropdown_xpath))

    def publicworks_submenu_dropdown_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.publicworks_submenu_dropdown_xpath))

    def routes_completion_submenu_dropdown_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.routes_submenu_dropdown_xpath))

    def zones_submenu_dropdown_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.zones_submenu_dropdown_xpath))

    def hos_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.hos_submenu_xpath))

    def logs_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.logs_xpath))

    def unidentified_driving_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.unidentified_driving_subchild_xpath))

    def violations_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.violations_subchild_xpath))

    def availability_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.availability_subchild_xpath))

    def timecardreport_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.timecardreport_submenu_xpath))

    def iftareport_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.iftareport_submenu_xpath))

    def cleantruckcheck_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.cleantruckcheck_submenu_xpath))

    def assetinspection_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.assetinspection_submenu_xpath))

    def diagnostics_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.diagnostic_measurements_submenu_xpath))

    def reminders_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.reminders_submenu_xpath))

    def faults_subchild_xpath_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.faults_subchild_xpath))

    def measurements_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.measurements_subchild_xpath))

    def sustainabilitycenter_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.sustainabilitycenter_submenu_xpath))

    def fuel_energy_usage_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.fuel_energy_usage_submenu_xpath))

    def evbatteryhealth_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.evbatteryhealth_submenu_xpath))

    def evcharginghistory_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.evcharginghistory_submenu_xpath))

    def bevrangecapability_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.bevrangecapability_submenu_xpath))

    def myreports_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.myreports_submenu_xpath))

    def reportsetup_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.reportsetup_submenu_xpath))

    def dashboard_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.dashboard_subchild_xpath))

    def reportviews_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.reportviews_subchild_xpath))

    def emailedreports_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.emailedreports_subchild_xpath))

    def rules_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.rules_submenu_xpath))

    def exceptions_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.exceptions_submenu_xpath))

    def settings_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.fleet_settings_submenu_xpath))

    def work_hours_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.work_hours_submenu_xpath))

    def holidays_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.holidays_submenu_xpath))

    def audit_log_submenu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.audit_log_submenu_xpath))

    def maintenance_center_sub_menu_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.maintenance_center_sub_menu_xpath))

    def speed_profile_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.speed_profile_subchild_xpath))

    def log_data_and_collisions_subchild_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.Log_data_and_collisions_subchild_xpath))

    def click_maintenance_center_submenu_dropdown(self):
        self.click((By.XPATH, LF.maintenance_center_sub_menu_xpath))

    def work_order_sub_child_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.work_order_sub_child_xpath))

    def schedules_sub_child_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LF.schedules_sub_child_xpath))

    def click_work_order_sub_menu(self):
        self.click((By.XPATH, LF.work_order_sub_child_xpath))

    def click_schedules_child_menu(self):
        self.click((By.XPATH, LF.schedules_sub_child_xpath))


