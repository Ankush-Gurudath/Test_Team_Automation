from time import sleep

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By

from locators.locators_driver_profile_page import LocatorsDriverProfile as DP
from pages.base_page import BasePage


class DriverProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_title(self):
        return self.get_text((By.XPATH, DP.title_text_xpath))

    def get_driver_name(self):
        return self.get_text((By.XPATH, DP.driver_name_text_xpath))

    def click_add_recognition(self):
        self.click((By.XPATH, DP.add_recognition_link_xpath))

    def click_add_recognition_complete(self):
        self.click((By.XPATH, DP.add_recognition_complete_button_xpath))

    def click_close_add_recognition_complete(self):
        self.element_is_displayed((By.XPATH, DP.delete_recognition_button_xpath))
        n = 0
        while n < 5:
            n += 1
            try:
                self.click((By.XPATH, DP.close_add_recognition_button_xpath))
                break
            except StaleElementReferenceException:
                sleep(6)

        if n == 5:
            self.click((By.XPATH, DP.close_add_recognition_button_xpath))

    def click_coach_event_button(self):
        self.click((By.XPATH, DP.coach_event_button_xpath))

    def click_view_remote_event_button(self):
        self.click((By.XPATH, DP.view_remote_event_button_xpath))

    def play_video(self):
        self.click((By.XPATH, DP.play_video_button_xpath))

    def click_expand_icon(self):
        self.click((By.XPATH, DP.expand_icon_xpath))

    def get_event_status(self):
        return self.get_text((By.XPATH, DP.event_status_text_xpath))

    def close_preview_modal(self):
        self.click((By.XPATH, DP.close_preview_icon_xpath))

    # View
    def get_driver_profile_title_text(self):
        return self.get_text((By.XPATH, DP.driver_profile_title_text_xpath))

    def get_employee_id_text(self):
        return self.get_text((By.XPATH, DP.employee_id_text_xpath))

    def get_driver_group_text(self):
        return self.get_text((By.XPATH, DP.driver_group_text_xpath))

    def get_email_text(self):
        return self.get_text((By.XPATH, DP.email_text_xpath))

    # Metrics
    def get_coachable_driver_metrics_text(self):
        return self.get_text((By.XPATH, DP.coachable_driver_metrics_text_xpath))

    def get_score_metrics_text(self):
        return self.get_text((By.XPATH, DP.score_metrics_text_xpath))

    def get_events_metrics_text(self):
        return self.get_text((By.XPATH, DP.events_metrics_text_xpath))

    def get_continual_behavior_text(self):
        return self.get_text((By.XPATH, DP.continual_behavior_metrics_text_xpath))

    # Scorecards
    def get_coachable_behavior_text(self):
        return self.get_text((By.XPATH, DP.coachable_behavior_text_xpath))

    def get_frequency_text(self):
        return self.get_text((By.XPATH, DP.frequency_text_xpath))

    def get_weights_text(self):
        return self.get_text((By.XPATH, DP.weight_text_xpath))

    def get_points_text(self):
        return self.get_text((By.XPATH, DP.points_text_xpath))

    # Events
    def get_event_id_text_events_tab(self):
        return self.get_text((By.XPATH, DP.event_id_text_xpath))

    def get_group_text(self):
        return self.get_text((By.XPATH, DP.event_group_text_xpath))

    def get_vehicle_text(self):
        return self.get_text((By.XPATH, DP.vehicle_text_xpath))

    def get_device_text(self):
        return self.get_text((By.XPATH, DP.device_text_xpath))

    def get_event_date_text(self):
        return self.get_text((By.XPATH, DP.event_date_text_xpath))

    def get_score_event_text(self):
        return self.get_text((By.XPATH, DP.event_score_text_xpath))

    def get_status_text(self):
        return self.get_text((By.XPATH, DP.status_text_xpath))

    def get_trigger_text(self):
        return self.get_text((By.XPATH, DP.trigger_text_xpath))

    def get_behavior_metrics_text(self):
        return self.get_text((By.XPATH, DP.behaviors_metrics_text_xpath))

    # ContinualBehavior
    def click_continual_behavior(self):
        self.scroll_page_down()
        self.click((By.XPATH, DP.continual_behavior_tab_text_xpath))

    def get_summary_count_text(self):
        return self.get_text((By.XPATH, DP.summary_count_text_xpath))

    def get_behavior_count_text(self):
        return self.get_text((By.XPATH, DP.behavior_count_text_xpath))

    def get_duration_count_text(self):
        return self.get_text((By.XPATH, DP.duration_count_text_xpath))

    def get_percent_of_drive_time_text(self):
        return self.get_text((By.XPATH, DP.percent_of_drive_time_text_xpath))

    def get_incidents_tab_text(self):
        return self.get_text((By.XPATH, DP.incidents_tab_text_xpath))

    def get_incidents_behavior_text(self):
        return self.get_text((By.XPATH, DP.behavior_incident_text_xpath))

    def get_incidents_duration_text(self):
        return self.get_text((By.XPATH, DP.duration_incident_text_xpath))

    def get_incidents_date_text(self):
        return self.get_text((By.XPATH, DP.date_incident_text_xpath))

    # CoachingHistory
    def click_coaching_history(self):
        self.click((By.XPATH, DP.coaching_history_tab_text_xpath))

    def click_coaching_history_tab(self):
        self.click((By.XPATH, DP.coaching_history_tab_xpath))

    def get_session_id_text(self):
        return self.get_text((By.XPATH, DP.session_id_text_xpath))

    def get_coach_date_text(self):
        return self.get_text((By.XPATH, DP.coach_date_text_xpath))

    def get_overdue_date_text(self):
        return self.get_text((By.XPATH, DP.overdue_date_text_xpath))

    def get_behaviors_coached_text(self):
        return self.get_text((By.XPATH, DP.behaviors_coached_text_xpath))

    def get_coach_text(self):
        return self.get_text((By.XPATH, DP.coach_text_xpath))

    def get_notes_text(self):
        return self.get_text((By.XPATH, DP.notes_text_xpath))

    # Recognitions
    def click_recognitions_tab(self):
        self.click((By.XPATH, DP.recognitions_tab_xpath))

    def get_type_text(self):
        return self.get_text((By.XPATH, DP.type_text_xpath))

    def get_event_id_rec_text(self):
        return self.get_text((By.XPATH, DP.event_id_rec_text_xpath))

    def get_issued_by_text(self):
        return self.get_text((By.XPATH, DP.issued_by_text_xpath))

    def get_issued_date_text(self):
        return self.get_text((By.XPATH, DP.issued_date_text_xpath))

    def get_recognition_reason_text(self):
        return self.get_text((By.XPATH, DP.recognition_reason_text_xpath))

    def click_edit_message_button(self):
        element = self.find((By.XPATH, DP.edit_message_button_xpath))
        self.scroll_to_element(element)
        self.click((By.XPATH, DP.edit_message_button_xpath))

    def type_recognition_reason(self):
        self.type((By.XPATH, DP.recognition_reason_text_area_xpath), "Recognition added by Automation user")

    def click_check_or_right_marke_edit_recognition(self):
        self.click((By.XPATH, DP.check_or_right_marke_edit_recognition_xpath))

    def get_driver_profile_text_on_login(self):
        return self.get_text((By.XPATH, DP.driver_profile_text_xpath))