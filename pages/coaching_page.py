from time import sleep

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators.locators_coaching_page import LocatorsCoaching as CP
from pages.base_page import BasePage


class CoachingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Video
    def click_video(self):
        self.scroll_to_element(self.find((By.XPATH, CP.watch_video_xpath)))
        sleep(1)
        self.click((By.XPATH, CP.watch_video_xpath))

    # Share
    def click_share(self):
        self.click((By.XPATH, CP.share_button_xpath))

    def click_share_copy(self):
        self.click((By.XPATH, CP.share_copy_xpath))

    def click_share_close(self):
        self.click((By.XPATH, CP.share_close_xpath))

    # AddRecognition
    def click_add_recognition_button(self):
        self.click((By.XPATH, CP.add_recognition_button_xpath))

    def click_reason_text_box(self):
        self.click((By.XPATH, CP.recognition_reason_xpath))

    def clear_reason_text_box(self):
        self.find((By.XPATH, CP.recognition_reason_xpath)).clear()

    def send_reason_text_box(self, recognition_reason):
        self.type((By.XPATH, CP.recognition_reason_xpath), recognition_reason)

    def send_share_event_link(self):
        self.find((By.ID, CP.add_session_textbox_id)).send_keys(Keys.CONTROL, 'v')

    def get_share_event_link(self):
        return self.get_text((By.CLASS_NAME, CP.session_note_class_name))

    def click_complete_recognition(self):
        self.click((By.CSS_SELECTOR, CP.recognition_complete_css))

    def click_delete_recognition(self):
        self.wait_for_element_displayed((By.CSS_SELECTOR, CP.recognition_delete_css))
        self.click((By.CSS_SELECTOR, CP.recognition_delete_css))

    def click_close_recognition(self):
        self.click((By.CSS_SELECTOR, CP.recognition_close_css))

    # Contact Lytx
    def click_contact_lytx(self):
        self.click((By.XPATH, CP.contact_tab_xpath))

    def select_contact_issue(self):
        self.click((By.XPATH, CP.contact_issue_dropdown_xpath))

    def select_other_concern(self):
        self.click((By.XPATH, CP.contact_other_concern_xpath))

    def send_contact_message(self, contact_message):
        self.type((By.CSS_SELECTOR, CP.contact_message_box_css), contact_message)

    def click_contact_submit(self):
        self.click((By.CSS_SELECTOR, CP.contact_submit_css))

    def click_contact_done(self):
        self.click((By.CSS_SELECTOR, CP.contact_done_css))

    # AddEventNotes
    def click_add_events(self):
        self.scroll_to_element(self.find((By.CSS_SELECTOR, CP.add_event_notes_tab_css)))
        sleep(1)
        self.click((By.CSS_SELECTOR, CP.add_event_notes_tab_css))

    def send_event_notes(self, event_note):
        self.type((By.CSS_SELECTOR, CP.add_events_textbox_css), event_note)

    def click_event_notes_submit(self):
        self.click((By.CSS_SELECTOR, CP.add_events_submit_button_css))

    # AddSessionNotes
    def click_add_session_tab(self):
        self.click((By.ID, CP.add_session_tab_id))

    def send_session_text(self, session_note):
        self.type((By.ID, CP.add_session_textbox_id), session_note)

    def click_submit_button(self):
        self.click((By.CSS_SELECTOR, CP.add_session_submit_button_css))

    # ActionPlan
    def click_action_plan(self):
        self.scroll_to_element(self.find((By.XPATH, CP.action_plan_xpath)))
        sleep(1)
        self.click((By.XPATH, CP.action_plan_xpath))

    # CompleteSession
    def click_complete_session(self):
        self.scroll_page_down()
        self.wait_for_element_is_clickable((By.XPATH, CP.complete_session_xpath))
        self.click((By.XPATH, CP.complete_session_xpath))

    def click_save_complete_session(self):
        self.click((By.CSS_SELECTOR, CP.complete_session_save_css))

    def click_close_complete_session(self):
        self.wait_for_element_is_clickable((By.CSS_SELECTOR, CP.complete_session_close_css))
        self.click((By.CSS_SELECTOR, CP.complete_session_close_css))

    def get_copy_button_text_after_click(self):
        return self.get_text((By.CLASS_NAME, CP.copy_button_text_class_name))

    def get_recognition_message(self):
        return self.get_text((By.CLASS_NAME, CP.recognition_message_class_name))

    def get_contact_submit_message(self):
        return self.get_text((By.ID, CP.contact_submit_message_id))

    # CoachingInfo
    def get_event_note(self):
        return self.get_text((By.CLASS_NAME, CP.event_note_class_name))

    def get_session_note(self):
        return self.get_text((By.XPATH, CP.session_note_xpath))

    def get_complete_session_message(self):
        return self.get_text((By.ID, CP.complete_session_message_id))

    def get_coaching_session_title(self):
        return self.get_text((By.CSS_SELECTOR, CP.coaching_session_title_text_css))

    def get_task_coaching_label(self):
        try:
            self.wait_for_element_displayed((By.XPATH, CP.task_coaching_label_xpath))
            return self.get_text((By.XPATH, CP.task_coaching_label_xpath))
        except StaleElementReferenceException:
            sleep(1)
            self.wait_for_element_displayed((By.XPATH, CP.task_coaching_label_xpath))
            return self.get_text((By.XPATH, CP.task_coaching_label_xpath))

    def get_driver_name_card_label(self):
        try:
            return self.get_text((By.XPATH, CP.driver_name_card_xpath))
        except StaleElementReferenceException:
            sleep(1)
            return self.get_text((By.XPATH, CP.driver_name_card_xpath))

    def get_group_card_label(self):
        return self.get_text((By.ID, CP.group_card_id))

    def get_vehicle_card_label(self):
        return self.get_text((By.ID, CP.vehicle_card_id))

    def get_event_date_card_label(self):
        return self.get_text((By.ID, CP.event_date_card_id))

    def get_event_date_format_label(self):
        return self.get_text((By.ID, CP.date_format_label_xpath))

    def get_time_card_label(self):
        return self.get_text((By.ID, CP.time_card_id))

    def get_overdue_date_card_label(self):
        return self.get_text((By.ID, CP.overdue_date_card_id))

    def get_behaviors_card_label(self):
        return self.get_text((By.ID, CP.behaviors_card_id))

    def get_no_coach_events_card_label(self):
        return self.get_text((By.XPATH, CP.no_coach_events_card_xpath))

    def get_driver_coaching_session_label(self):
        return self.get_text((By.XPATH, CP.driver_coaching_session_title_xpath))

    def get_driver_coaching_session_label_new_UI(self):
        return self.get_text((By.XPATH, CP.driver_coaching_session_title_xpath_new_UI))

    def get_driver_name_label(self):
        return self.get_text((By.XPATH, CP.driver_name_label_xpath))

    def get_employee_id_label(self):
        return self.get_text((By.XPATH, CP.employee_id_xpath))

    def get_group_label(self):
        return self.get_text((By.XPATH, CP.group_label_xpath))

    def get_email_label(self):
        return self.get_text((By.XPATH, CP.email_label_xpath))

    def get_coaching_history_label(self):
        return self.get_text((By.XPATH, CP.coaching_history_label_xpath))

    def get_event_video_label(self):
        return self.get_text((By.XPATH, CP.event_videos_label_xpath))

    def get_video_section_label(self):
        return self.get_text((By.XPATH, CP.video_section_xpath))

    def get_share_label(self):
        return self.get_text((By.XPATH, CP.share_button_xpath))

    def get_add_recognition_label(self):
        return self.get_text((By.XPATH, CP.add_recognition_button_xpath))

    def get_contact_lytx_label(self):
        return self.get_text((By.XPATH, CP.contact_tab_xpath))

    def get_more_actions_label(self):
        return self.get_text((By.XPATH, CP.more_actions_xpath))

    def get_behaviors_label(self):
        return self.get_text((By.XPATH, CP.behaviors_label_xpath))

    def get_event_date_label(self):
        return self.get_text((By.XPATH, CP.event_date_label_xpath))

    def get_event_label(self):
        return self.get_text((By.XPATH, CP.event_label_xpath))

    def get_status_label(self):
        return self.get_text((By.XPATH, CP.status_label_xpath))

    def get_trigger_label(self):
        return self.get_text((By.XPATH, CP.trigger_label_xpath))

    def get_score_label(self):
        return self.get_text((By.XPATH, CP.score_label_xpath))

    def get_lytx_comments_label(self):
        return self.get_text((By.XPATH, CP.lytx_comments_label_xpath))

    def get_events_notes_label(self):
        return self.get_text((By.XPATH, CP.event_notes_label_xpath))

    def get_session_notes_label(self):
        return self.get_text((By.XPATH, CP.session_notes_label_xpath))

    def get_complete_coaching_message_label(self):
        return self.get_text((By.XPATH, CP.complete_session_label_xpath))

    def click_coaching_filter_by_group(self):
        self.click((By.XPATH, CP.filter_by_group_button_xpath))

    def search_coaching_filter_by_group(self, groupname):
        self.type((By.XPATH, CP.filter_by_group_search_box_xpath), groupname)

    def select_search_coaching_filter_by_group(self):
        self.click((By.XPATH, CP.select_search_filter_by_group_xpath))

    def click_done_button_filter_by_group(self):
        self.click((By.XPATH, CP.done_filter_by_group_button_xpath))

    def click_triggers_filter(self):
        self.click((By.XPATH, CP.triggers_filter_button_xpath))

    def select_triggers_filter(self):
        self.click((By.XPATH, CP.select_triggers_filter_xpath))

    def click_behaviors_filter(self):
        self.click((By.XPATH, CP.behaviors_filter_button_xpath))

    def select_behaviors_filter(self):
        self.click((By.XPATH, CP.select_behaviors_filter_xpath))

    def search_name_filter(self, driver_name):
        self.type((By.XPATH, CP.search_name_filter_box_xpath), driver_name)

    def click_coaching_reset_filter(self):
        self.click((By.XPATH, CP.reset_filter_button_xpath))

    def get_group_name_card(self):
        return self.get_text((By.XPATH, CP.group_card_name_xpath))

    def get_behaviors_name_card(self):
        return self.get_text((By.XPATH, CP.behaviors_card_name_xpath))

    def click_tasks_label(self):
        self.click((By.XPATH, CP.task_coaching_label_xpath))

    def get_filter_message_text(self):
        return self.get_text((By.XPATH, CP.filter_message_text_xpath))

    def click_more_actions_tab(self):
        self.scroll_to_element(self.find((By.XPATH, CP.more_actions_xpath)))
        self.wait_for_element_is_clickable((By.XPATH, CP.more_actions_xpath))
        self.click((By.XPATH, CP.more_actions_xpath))

    def reassign_driver(self):
        self.wait_for_element_is_clickable((By.XPATH, CP.reassign_driver_xpath))
        self.click((By.XPATH, CP.reassign_driver_xpath))

    def click_self_coaching_tab(self):
        self.click((By.XPATH, CP.mark_self_coaching_tab_xpath))

    def click_confirm_self_coaching_button(self):
        self.click((By.XPATH, CP.confirm_self_coaching_button_xpath))

    def get_event_id(self):
        return self.get_text((By.XPATH, CP.event_id_xpath))

    def get_event_status(self):
        self.wait_for_element_displayed((By.XPATH, CP.event_status_xpath))
        return self.get_text((By.XPATH, CP.event_status_xpath))

    # notify driver
    def click_kebab_icon(self):
        self.click((By.XPATH, CP.kebab_icon_in_task_card_xpath))

    def click_notify_driver(self):
        self.click((By.XPATH, CP.notify_driver_xpath))

    def click_notify_button(self):
        self.click((By.XPATH, CP.notify_button_xpath))

    def get_remote_event_status(self):
        return self.get_text((By.XPATH, CP.event_status_text_xpath))

    def search_assign_driver(self, driver_name):
        self.type((By.XPATH, CP.assign_driver_search_xpath), driver_name)

    def select_searched_driver(self):
        self.click((By.XPATH, CP.select_assign_driver_search_xpath))

    def click_assign(self):
        self.click((By.XPATH, CP.assign_driver_button_xpath))

    def get_task_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, CP.task_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, CP.task_count_xpath))

    def continue_button_is_displayed(self):
        return self.element_is_displayed((By.ID, CP.continue_button_id))

    def click_continue_button(self):
        self.click((By.ID, CP.continue_button_id))

    def click_preview_button(self):
        self.click((By.XPATH, CP.preview_card_xpath))

    def click_event_id_filter(self):
        self.click((By.XPATH, CP.event_id_filter_xpath))

    def select_event_id(self):
        self.click((By.XPATH, CP.select_event_id_xpath))

    def click_more_actions_event_preview_page(self):
        self.click((By.XPATH, CP.more_actions_event_preview_xpath))

    def click_mark_as_fyi_notify(self):
        self.click((By.XPATH, CP.mark_as_fyi_notify_tab_xpath))

    def click_yes_confirm_button(self):
        self.click((By.XPATH, CP.yes_confirm_button_xpath))

    def close_preview_page(self):
        self.click_element_ignore_exceptions((By.XPATH, CP.close_preview_page_button_xpath))

    def video_error_msg(self):
        return self.element_is_displayed((By.XPATH, CP.video_displayed_xpath))

    def change_event_video(self):
        self.click((By.XPATH, CP.change_video_xpath))

    def change_video_displayed(self):
        return self.element_is_displayed((By.XPATH, CP.change_video_xpath))
