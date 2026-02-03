from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By

from locators.locators_dashboard_page import LocatorsDashboard as AC
from locators.locators_navigation_menu import LocatorsNavigationMenu as LNM
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_tasks(self):
        self.element_is_displayed((By.XPATH, AC.tasks_tab_xpath))
        self.click((By.XPATH, AC.tasks_tab_xpath))

    def click_assign_driver_tab(self):
        self.click((By.XPATH, AC.assign_driver_xpath))

    def click_fleet_telematics_tab(self):
        self.wait_for_element_is_clickable((By.ID, AC.fleet_telematics_tab))
        self.click((By.ID, AC.fleet_telematics_tab))

    def click_coaching(self):
        self.element_is_displayed((By.XPATH, AC.coaching_tab_xpath))
        self.click((By.XPATH, AC.coaching_tab_xpath))

    def click_coaching_events(self):
        i = 0
        while i < 10:
            try:
                self.click((By.CSS_SELECTOR, AC.coaching_event_css))
                break
            except (ElementClickInterceptedException, StaleElementReferenceException):
                sleep(1)
                i += 1

        if i == 10:
            self.click((By.CSS_SELECTOR, AC.coaching_event_css))

    def click_coaching_events_new_UI(self):
        i = 0
        while i < 10:
            try:
                self.click((By.XPATH, AC.coaching_event_xpath))
                break
            except (ElementClickInterceptedException, StaleElementReferenceException):
                sleep(1)
                i += 1

        if i == 10:
            self.click((By.XPATH, AC.coaching_event_xpath))

    def click_library_tab(self):
        self.wait_for_page_load()
        self.wait_for_element_is_clickable((By.XPATH, AC.library_tab_xpath))
        i = 0
        while i < 10:
            try:
                self.click((By.XPATH, AC.library_tab_xpath))
                break
            except ElementClickInterceptedException:
                self.close_walkme_dialog()
                sleep(1)
                i += 1

    def click_library_tab_new_ui(self):
        self.wait_for_page_load()
        self.wait_for_element_is_clickable((By.XPATH, AC.library_tab_xpath_new_ui))
        i = 0
        while i < 10:
            try:
                self.click((By.XPATH, AC.library_tab_xpath_new_ui))
                break
            except ElementClickInterceptedException:
                self.close_walkme_dialog()
                sleep(1)
                i += 1

    def click_events(self):
        self.click((By.XPATH, AC.events_tab_button_xpath))

    def click_events_new_ui(self):
        try:
            self.click((By.XPATH, AC.events_tab_button_xpath_new_ui))
        except (ElementClickInterceptedException, TimeoutException):
            self.click_library_tab_new_ui()
            self.click((By.XPATH, AC.events_tab_button_xpath_new_ui))

    def click_coaching_history(self):
        self.click((By.XPATH, AC.coaching_history_button_xpath))

    def click_coaching_history_new_ui(self):
        self.click((By.XPATH, AC.coaching_history_button_xpath_new_ui))

    def click_recognition_history(self):
        self.click((By.XPATH, AC.recognition_history_button_xpath))

    def click_recognition_history_new_ui(self):
        self.click((By.XPATH, AC.recognition_history_button_xpath_new_ui))

    def get_driver_safety_title(self):
        self.element_is_displayed((By.ID, AC.driver_safety_text_id))
        return self.get_text((By.ID, AC.driver_safety_text_id))

    def get_dvir_title(self):
        self.element_is_displayed((By.ID, AC.dvir_tab_id))
        return self.get_text((By.ID, AC.dvir_tab_id))

    def get_fleet_tracking_title(self):
        self.element_is_displayed((By.ID, AC.fleet_tracking_tab_id))
        return self.get_text((By.ID, AC.fleet_tracking_tab_id))

    def get_admin_title(self):
        self.element_is_displayed((By.ID, AC.admin_tab_id))
        return self.get_text((By.ID, AC.admin_tab_id))

    def get_video_search_title(self):
        self.element_is_displayed((By.ID, AC.video_search_tab_id))
        return self.get_text((By.ID, AC.video_search_tab_id))

    def get_hos_title(self):
        self.element_is_displayed((By.ID, AC.hos_tab_id))
        return self.get_text((By.ID, AC.hos_tab_id))

    def get_tasks_title(self):
        self.element_is_displayed((By.XPATH, AC.tasks_label_xpath))
        return self.get_text((By.XPATH, AC.tasks_label_xpath))

    def get_tasks_new_UI_title(self):
        self.element_is_displayed((By.XPATH, AC.tasks_label_new_UI_xpath))
        return self.get_text((By.XPATH, AC.tasks_label_new_UI_xpath))

    def get_metrics_title(self):
        self.element_is_displayed((By.XPATH, AC.metrics_label_xpath))
        return self.get_text((By.XPATH, AC.metrics_label_xpath))

    def get_metrics_new_UI_title(self):
        self.element_is_displayed((By.XPATH, AC.metrics_label_new_UI_xpath))
        return self.get_text((By.XPATH, AC.metrics_label_new_UI_xpath))

    def click_driver_safety_tab(self):
        self.element_is_displayed((By.ID, AC.driver_safety_text_id))
        self.click((By.ID, AC.driver_safety_text_id))

    def click_insights_tab(self):
        self.click((By.XPATH, AC.insights_tab_xpath))

    def click_insights_tab_new_ui(self):
        self.click((By.XPATH, AC.insights_tab_xpath_new_ui))

    def click_open_tasks_report_tab(self):
        self.click((By.XPATH, AC.open_tasks_report_tab_xpath))

    def click_open_tasks_report_tab_new_ui(self):
        self.click((By.XPATH, AC.open_tasks_report_tab_xpath_new_ui))

    def click_drivers_report_tab(self):
        self.click((By.XPATH, AC.drivers_report_tab_xpath))

    def click_behaviors_report_tab(self):
        self.click((By.XPATH, AC.behaviors_report_tab_xpath))

    def click_group_report_tab(self):
        self.click((By.XPATH, AC.group_report_tab_xpath))

    def click_coaches_report_tab(self):
        self.click((By.XPATH, AC.coaches_report_tab_xpath))

    def click_program_status_report_tab(self):
        self.click((By.XPATH, AC.program_status_report_tab_xpath))

    def click_driver_profile_link(self):
        self.scroll_page_down()
        self.wait_for_element_is_clickable((By.XPATH, AC.driver_profile_link_xpath))
        self.click((By.XPATH, AC.driver_profile_link_xpath))

    def click_alert_popup(self):
        self.click((By.XPATH, AC.close_alert_link_xpath))

    def click_home_tab(self):
        n = 0
        while n < 5:
            n += 1
            try:
                self.click((By.XPATH, AC.home_tab_xpath))
                break
            except (StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException):
                sleep(6)

        if n == 5:
            self.click((By.XPATH, AC.home_tab_xpath))

    def click_home_tab_new_ui(self):
        n = 0
        while n < 5:
            n += 1
            try:
                self.click((By.XPATH, AC.home_tab_xpath_new_ui))
                break
            except (StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException):
                sleep(6)

        if n == 5:
            self.click((By.XPATH, AC.home_tab_xpath_new_ui))

    def get_noof_drivers_text(self, locator):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                result = self.element_is_displayed((By.XPATH, locator))
                if result is True:
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.element_is_displayed((By.XPATH, locator))

    def get_unassigned_drivers_text(self):
        return self.get_text((By.XPATH, AC.unassigned_drivers_text_xpath))

    def get_due_for_coaching_text(self):
        return self.get_text((By.XPATH, AC.due_for_coaching_text_xpath))

    def get_fyi_notify_text(self):
        return self.get_text((By.XPATH, AC.fyi_notify_text_xpath))

    def get_collisions_text(self):
        return self.get_text((By.XPATH, AC.collisions_text_xpath))

    def get_possible_collisions_text(self):
        return self.get_text((By.XPATH, AC.possible_collisions_text_xpath))

    def get_unassigned_driver_task_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, AC.unassigned_drivers_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, AC.unassigned_drivers_count_xpath))

    def get_fyi_notify_task_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, AC.fyi_notify_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, AC.fyi_notify_count_xpath))

    def get_due_for_coaching_task_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, AC.due_for_coaching_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, AC.due_for_coaching_count_xpath))

    def get_collision_task_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, AC.collisions_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, AC.collisions_count_xpath))

    def get_possible_collision_task_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, AC.possible_collisions_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, AC.possible_collisions_count_xpath))

    def click_unassigned_drivers_link(self):
        self.element_is_displayed((By.XPATH, AC.unassigned_drivers_text_xpath))
        self.click((By.XPATH, AC.unassigned_drivers_text_xpath))

    def click_due_for_coaching_link(self):
        self.click((By.XPATH, AC.due_for_coaching_text_xpath))

    def click_fyi_notify_link(self):
        self.click((By.XPATH, AC.fyi_notify_text_xpath))

    def click_collisions_link(self):
        self.click((By.XPATH, AC.collisions_text_xpath))

    def click_possible_collisions_link(self):
        self.click((By.XPATH, AC.possible_collisions_text_xpath))

    def get_assigned_drivers_title(self):
        return self.get_text((By.XPATH, AC.assign_driver_title_text_xpath))

    def get_due_for_coaching_title(self):
        return self.get_text((By.XPATH, AC.due_for_coaching_title_text_xpath))

    def get_fyi_notify_title(self):
        return self.get_text((By.XPATH, AC.fyi_notify_title_text_xpath))

    def get_collisions_title(self):
        return self.get_text((By.XPATH, AC.collisions_title_text_xpath))

    def get_possible_collisions_title(self):
        return self.get_text((By.XPATH, AC.possible_collisions_title_text_xpath))

    def back_to_previous_page(self):
        self.back()

    def get_groups_by_highest_score_title(self):
        return self.get_text((By.XPATH, AC.groups_by_highest_score_text_xpath))

    def get_group_title(self):
        return self.get_text((By.XPATH, AC.group_text_xpath))

    def get_coachable_score_title(self):
        return self.get_text((By.XPATH, AC.coachable_score_text_xpath))

    def get_group_widget_score_trend_title(self):
        return self.get_text((By.XPATH, AC.group_widget_score_trend_text_xpath))

    def get_coachable_events_title(self):
        return self.get_text((By.XPATH, AC.coachable_events_text_xpath))

    def get_group_widget_event_trend_title(self):
        return self.get_text((By.XPATH, AC.group_widget_event_trend_text_xpath))

    def get_coachest_by_lowest_effectiveness_title(self):
        return self.get_text((By.XPATH, AC.coaches_by_lowest_effectiveness_text_xpath))
        # return self.get_attribute((By.XPATH, AC.coaches_by_lowest_effectiveness_text_xpath),
        #                           AC.xml_text_content_attribute)

    def get_coach_title(self):
        return self.get_attribute((By.XPATH, AC.coach_text_xpath), AC.xml_text_content_attribute)

    def get_coaching_effectiveness_title(self):
        return self.get_attribute((By.XPATH, AC.coaching_effectiveness_text_xpath), AC.xml_text_content_attribute)

    def get_avg_days_to_coach_title(self):
        return self.get_attribute((By.XPATH, AC.avg_days_to_coach_text_xpath), AC.xml_text_content_attribute)

    def get_coached_events_title(self):
        return self.get_attribute((By.XPATH, AC.coached_events_text_xpath), AC.xml_text_content_attribute)

    def get_with_notes_title(self):
        return self.get_attribute((By.XPATH, AC.with_notes_text_xpath), AC.xml_text_content_attribute)

    def get_drivers_by_highest_score_title(self):
        return self.get_text((By.XPATH, AC.drivers_by_highest_score_text_xpath))

    def get_driver_title(self):
        return self.get_attribute((By.XPATH, AC.driver_text_xpath), AC.xml_text_content_attribute)

    def get_driver_widget_coachable_score_title(self):
        return self.get_attribute((By.XPATH, AC.driver_widget_coachable_score_text_xpath), AC.xml_text_content_attribute)

    def get_driver_widget_trend_title(self):
        return self.get_attribute((By.XPATH, AC.driver_widget_trend_text_xpath), AC.xml_text_content_attribute)

    def get_impact_title(self):
        return self.get_attribute((By.XPATH, AC.impact_text_xpath), AC.xml_text_content_attribute)

    def get_behaviors_by_highest_frequency_title(self):
        return self.get_text((By.XPATH, AC.behaviors_by_highest_frequency_xpath))

    def get_behaviors_details_link(self):
        return self.get_text((By.XPATH, AC.view_details_behaviors_link_xpath))

    def get_groups_details_link(self):
        return self.get_text((By.XPATH, AC.view_details_groups_link_xpath))

    def get_coaches_details_link(self):
        return self.get_text((By.XPATH, AC.view_details_coaches_link_xpath))

    def get_drivers_details_link(self):
        return self.get_text((By.XPATH, AC.view_details_drivers_link_xpath))

    def get_all_dashboard_details_links(self):
        return {
            "drivers": self.get_drivers_details_link(),
            "coaches": self.get_coaches_details_link(),
            "groups": self.get_groups_details_link(),
            "behaviors": self.get_behaviors_details_link()
        }

    def click_behaviors_details_link(self):
        self.scroll_page_down()
        self.click((By.XPATH, AC.view_details_behaviors_link_xpath))

    def click_groups_details_link(self):
        self.scroll_page_down()
        self.click((By.XPATH, AC.view_details_groups_link_xpath))

    def click_coaches_details_link(self):
        self.scroll_page_down()
        self.click((By.XPATH, AC.view_details_coaches_link_xpath))

    def click_drivers_details_link(self):
        self.scroll_page_down()
        self.click((By.XPATH, AC.view_details_drivers_link_xpath))

    def click_group_filter(self):
        self.click((By.XPATH, AC.group_filter_button_xpath))

    def search_group_filter(self, groupname):
        self.type((By.XPATH, AC.group_filter_search_xpath), groupname)

    def select_group_filter(self):
        self.click((By.XPATH, AC.group_filter_select_search_xpath))

    def click_group_filter_done(self):
        self.click((By.XPATH, AC.group_filter_done_button_xpath))

    def get_no_of_tasks(self):
        self.element_is_displayed((By.XPATH, AC.no_of_tasks_xpath))
        return self.get_text((By.XPATH, AC.no_of_tasks_xpath))

    def unassigned_drivers_exists(self):
        self.element_is_displayed((By.ID, AC.no_of_tasks_xpath))
        return True

    def get_group_name_filtered(self):
        self.wait_for_element_displayed((By.XPATH, AC.group_name_filtered_xpath))
        return self.get_text((By.XPATH, AC.group_name_filtered_xpath))

    def get_coach_name_filtered(self):
        self.wait_for_element_displayed((By.XPATH, AC.coach_name_filtered_xpath))
        return self.element_is_displayed((By.XPATH, AC.coach_name_filtered_xpath))

    def get_driver_name_filtered(self):
        self.wait_for_element_displayed((By.XPATH, AC.driver_name_filtered_xpath))
        return self.wait_for_element_displayed((By.XPATH, AC.driver_name_filtered_xpath))

    def get_group_widget_1st_group(self):
        return self.get_text((By.XPATH, AC.group_widget_1st_group_xpath))

    def get_coach_widget_1st_coach(self):
        self.wait_for_element_displayed((By.XPATH, AC.coach_widget_1st_coach_xpath))
        return self.wait_for_element_displayed((By.XPATH, AC.coach_widget_1st_coach_xpath))

    def get_driver_widget_1st_driver(self):
        result = self.element_is_displayed((By.XPATH, AC.driver_widget_1st_driver_xpath))
        if result is False:
            raise TimeoutException
        return result

    def get_behavior_widget_1st_behavior(self):
        return self.get_text((By.XPATH, AC.behavior_widget_1st_behavior_xpath))

    def get_behavior_widget_no_data_msg(self):
        return self.get_text((By.XPATH, AC.behavior_widget_no_data_msg_xpath))

    def click_date_filter(self):
        self.click((By.XPATH, AC.date_filter_button_xpath))

    def clik_date1_filter(self):
        self.click((By.XPATH, AC.from_date_select_xpath))

    def click_date2_filter(self):
        self.click((By.XPATH, AC.end_date_select_xpath))

    def click_apply_filter(self):
        self.click((By.XPATH, AC.apply_button_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, AC.reset_button_xpath))

    def click_collisions_tab(self):
        self.click((By.XPATH, AC.collisions_tab_xpath))

    def click_fyi_notify_tab(self):
        self.click((By.XPATH, AC.fyi_notify_tab_xpath))

    def click_quick_search_tab(self):
        self.click((By.XPATH, AC.quick_search_tab_xpath))

    def click_quick_search_tab_new_UI(self):
        self.click((By.XPATH, AC.quick_search_tab_new_UI_xpath))

    def search_event_id(self, EVENT_ID):
        self.type((By.XPATH, AC.quick_search_text_box_xpath), EVENT_ID)

    def click_search_icon(self):
        self.click((By.XPATH, AC.search_icon_xpath))

    def get_preview_searched_event(self):
        return self.get_text((By.XPATH, AC.preview_searched_event_xpath))

    def click_close_preview_video(self):
        self.click((By.ID, AC.close_preview_video_id))

    def click_admin_tab(self):
        self.wait_till_element_disappear((By.XPATH, "//div[@class='menu-item-loader']/loading-indicator"))
        self.wait_for_element_is_clickable((By.ID, AC.admin_tab_id))
        self.click((By.ID, AC.admin_tab_id))
        self.wait_for_page_to_fully_load()

    def click_video_search_tab(self):
        self.click((By.ID, AC.video_search_tab_id))

    def click_fleet_tracking_tab(self):
        self.element_is_displayed((By.ID, AC.fleet_tracking_tab_id))
        self.click((By.ID, AC.fleet_tracking_tab_id))

    def click_dvir_tab(self):
        self.wait_for_element_displayed((By.ID, AC.dvir_tab_id))
        self.click((By.ID, AC.dvir_tab_id))

    def click_hos_tab(self):
        self.click((By.ID, AC.hos_tab_id))

    def no_of_unassigned_drivers_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, AC.unassigned_drivers_count_xpath))

    def no_of_tasks_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, AC.no_of_tasks_xpath))

    def no_of_drivers_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, AC.no_of_drivers_count_xpath))

    def no_of_drivers_is_displayed_new_ui(self):
        return self.wait_for_element_displayed((By.XPATH, AC.no_of_drivers_count_xpath_newui))

    def video_search_title_is_displayed(self):
        return self.element_is_displayed_no_timeout((By.ID, AC.video_search_tab_id))

    def dvir_title_is_displayed(self):
        return self.element_is_displayed_no_timeout((By.ID, AC.dvir_tab_id))

    def fleet_telematics_title_is_displayed(self):
        return self.element_is_displayed_no_timeout((By.ID, AC.fleet_telematics_tab))

    def fleet_tracking_title_is_displayed(self):
        return self.element_is_displayed_no_timeout((By.ID, AC.fleet_tracking_tab_id))

    def admin_title_is_displayed(self):
        return self.element_is_displayed_no_timeout((By.ID, AC.admin_tab_id))

    def hos_title_is_displayed(self):
        return self.element_is_displayed_no_timeout((By.ID, AC.hos_tab_id))

    def driver_safety_title_is_displayed(self):
        return self.element_is_displayed_no_timeout((By.ID, AC.driver_safety_text_id))

    def behavior_widget_element_is_displayed(self):
        result = self.element_is_displayed((By.XPATH, AC.Behaviors_list))
        if result is False:
            raise TimeoutException
        return result

    def get_implementation_center_title(self):
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        return self.get_text((By.XPATH, AC.app_title))

    def get_safe_driving_trend_title(self):
        return self.get_text((By.XPATH, AC.safe_driving_trend_text_xpath))

    def graph_is_displayed_in_safe_drive_trend(self):
        return self.element_is_displayed((By.CLASS_NAME, AC.safe_driving_trend_graph_class))

    def get_groups_by_highest_safe_drivers_title(self):
        return self.get_text((By.XPATH, AC.groups_by_highest_perc_safe_drivers_xpath))

    def get_group_text(self):
        return self.get_text((By.XPATH, AC.group_text_for_safe_drive_report_widget_xpath))

    def get_percentage_safe_drivers_text(self):
        return self.get_text((By.XPATH, AC.safe_drivers_xpath))

    def get_eligible_for_recognition_text(self):
        return self.get_text((By.XPATH, AC.eligible_for_recognition_text_xpath))

    def get_recognized_text(self):
        return self.get_text((By.XPATH, AC.recognized_xpath))

    def click_safe_driving_report_tab(self):
        self.click((By.XPATH, AC.safe_drivers_report_tab))

    def click_safe_driving_widget_first_group(self):
        self.click((By.XPATH, AC.safe_drive_widget_first_group_xpath))

    def get_safe_driving_widget_first_group_name(self):
        return self.get_text((By.XPATH, AC.safe_drive_widget_first_group_xpath))

    def click_recognise_button(self):
        self.click((By.XPATH, AC.recognize_button_xpath))

    def get_fleet_telematics_title(self):
        return self.get_text((By.ID, AC.fleet_telematics_tab))

    def click_library_menu(self):
        self.click((By.XPATH, AC.library_menu_xpath))

    def click_home_menu(self):
        self.click((By.XPATH, AC.home_menu_xpath))

    def click_insights_menu(self):
        self.click((By.XPATH, AC.insights_menu_xpath))

    def click_recognitions_submenu(self):
        self.click((By.XPATH, AC.recognitions_submenu_xpath))

    def click_events_submenu(self):
        self.click((By.XPATH, AC.events_submenu_xpath))

    def click_events_submenu_new_UI(self):
        try:
            self.click((By.XPATH, AC.events_submenu_xpath))
        except (ElementClickInterceptedException, TimeoutException):
            self.click_library_menu()
            self.click((By.XPATH, AC.events_submenu_xpath))

    def events_submenu(self):
        return self.element_is_displayed((By.XPATH, AC.events_submenu_xpath))

    def click_recognition_history_submenu(self):
        self.click((By.XPATH, AC.recognition_history_submenu_xpath))

    def click_recognition_history_submenu_new_UI(self):
        try:
            self.click((By.XPATH, AC.recognition_history_submenu_xpath))
        except (ElementClickInterceptedException, TimeoutException):
            self.click_library_menu()
            self.click((By.XPATH, AC.recognition_history_submenu_xpath))

    def click_coaching_history_submenu(self):
        self.click((By.XPATH, AC.coaching_history_submenu_xpath))

    def click_coaching_history_submenu_new_UI(self):
        try:
            self.click((By.XPATH, AC.coaching_history_submenu_xpath))
        except (ElementClickInterceptedException, TimeoutException):
            self.click_library_menu()
            self.click((By.XPATH, AC.coaching_history_submenu_xpath))

    def click_data_export_submenu(self):
        self.click((By.XPATH, AC.data_export_submenu_xpath))

    def click_data_export_submenu_new_UI(self):
        try:
            self.click((By.XPATH, AC.data_export_submenu_xpath))
        except (ElementClickInterceptedException, TimeoutException):
            self.click_library_menu()
            self.click((By.XPATH, AC.data_export_submenu_xpath))

    def click_open_tasks_report_submenu(self):
        self.click((By.XPATH, AC.open_tasks_report_submenu_xpath))

    def click_open_tasks_report_submenu_new_UI(self):
        try:
            self.click((By.XPATH, AC.open_tasks_report_submenu_xpath))
        except (ElementClickInterceptedException, TimeoutException):
            self.click_insights_menu()
            self.click((By.XPATH, AC.open_tasks_report_submenu_xpath))

    def click_drivers_report_submenu(self):
        self.click((By.XPATH, AC.drivers_report_submenu_xpath))

    def click_drivers_report_submenu_new_UI(self):
        try:
            self.click((By.XPATH, AC.drivers_report_submenu_xpath))
        except (ElementClickInterceptedException, TimeoutException):
            self.click_insights_menu()
            self.click((By.XPATH, AC.drivers_report_submenu_xpath))

    def click_group_report_submenu(self):
        self.click((By.XPATH, AC.group_report_submenu_xpath))

    def click_group_report_submenu_new_UI(self):
        try:
            self.click((By.XPATH, AC.group_report_submenu_xpath))
        except (ElementClickInterceptedException, TimeoutException):
            self.click_insights_menu()
            self.click((By.XPATH, AC.group_report_submenu_xpath))

    def click_coaches_report_submenu(self):
        self.click((By.XPATH, AC.coaches_report_submenu_xpath))

    def click_coaches_report_submenu_new_UI(self):
        try:
            self.click((By.XPATH, AC.coaches_report_submenu_xpath))
        except (ElementClickInterceptedException, TimeoutException):
            self.click_insights_menu()
            self.click((By.XPATH, AC.coaches_report_submenu_xpath))

    def click_program_status_report_submenu(self):
        self.click((By.XPATH, AC.program_status_report_submenu_xpath))

    def click_program_status_report_submenu_new_UI(self):
        try:
            self.click((By.XPATH, AC.program_status_report_submenu_xpath))
        except (ElementClickInterceptedException, TimeoutException):
            self.click_insights_menu()
            self.click((By.XPATH, AC.program_status_report_submenu_xpath))

    def click_behaviors_report_submenu(self):
        self.click((By.XPATH, AC.behaviors_report_submenu_xpath))

    def click_behaviors_report_submenu_new_UI(self):
        try:
            self.click((By.XPATH, AC.behaviors_report_submenu_xpath))
        except (ElementClickInterceptedException, TimeoutException):
            self.click_insights_menu()
            self.click((By.XPATH, AC.behaviors_report_submenu_xpath))

    def click_data_export(self):
        self.click((By.XPATH, AC.data_export_tab_xpath))

    def get_driver_widget_no_data_msg(self):
        return self.get_text((By.XPATH, AC.driver_widget_no_data_msg_xpath))

    def lytx_geotab_logo_is_displayed(self):
        return self.element_is_displayed((By.XPATH, AC.lytx_geotab_logo_xpath))

    def no_driver_data_displayed(self):
        return self.element_is_displayed((By.XPATH, AC.driver_widget_no_data_msg_xpath))

    def lytx_logo_is_displayed(self):
        return self.element_is_displayed((By.XPATH, AC.lytx_logo_xpath))

    def lytx_logo_is_displayed_old_ui(self):
        return self.element_is_displayed((By.XPATH, AC.lytx_logo_old_ui_xpath))

    def eld_error_message_is_displayed(self):
        return self.element_is_displayed((By.XPATH, AC.eld_error_msg_xpath))

    def switch_ft_iframe_eld(self):
        self.wait_for_page_to_fully_load()
        if self.element_is_displayed((By.CLASS_NAME, AC.eld_frame_class)) is True:
            self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, AC.eld_frame_class))
