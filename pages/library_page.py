from datetime import datetime
from time import sleep

from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, \
    StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from locators.locators_library_page import LocatorsLibrary as LB
from pages.base_page import BasePage
from utils.common_util import LocatorUtil


class LibraryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_coaching_history(self):
        self.click((By.XPATH, LB.coaching_history_tab_xpath))

    def click_coaching_history_new_ui(self):
        self.click((By.XPATH, LB.coaching_history_tab_xpath_new_ui))

    def click_first_recognition(self):
        self.click((By.XPATH, LB.first_recognition_link_xpath))

    def click_delete_recognition_confirmation_button(self):
        self.click((By.XPATH, LB.recognition_confirm_delete_button_xpath))

    def edit_recognition(self, recognition_reason):
        self.clear((By.XPATH, LB.recognition_page_recognition_reason_xpath))
        self.type((By.XPATH, LB.recognition_page_recognition_reason_xpath), recognition_reason)

    def click_recognition_complete_button(self):
        self.click((By.XPATH, LB.recognition_complete_button_xpath))

    def get_recognition_list_recognition_reason(self):
        return self.get_text((By.XPATH, LB.recognition_list_recognition_reason_xpath))

    def click_download_recognition_button(self):
        self.click((By.XPATH, LB.recognition_download_button_xpath))

    def get_recognition_issued_date(self):
        return self.get_text((By.XPATH, LB.recognition_issued_date_xpath))

    def get_recognition_file_name(self, driver_name):
        date_now_text = self.get_recognition_issued_date()
        date_now = datetime.strptime(date_now_text, "%b %d, %Y").strftime("%Y-%m-%d")

        file_name = driver_name + ' Recognition ' + date_now + '.pdf'
        return file_name

    def click_edit_recognition_button(self):
        self.click((By.XPATH, LB.recognition_edit_button_xpath))

    def click_delete_recognition_button(self):
        self.click((By.XPATH, LB.recognition_delete_button_xpath))

    def click_recognition_close_button(self):
        self.click((By.XPATH, LB.recognition_close_button_xpath))

    def click_type_link(self):
        self.click((By.XPATH, LB.type_link_xpath))

    def click_driver_link(self):
        self.click((By.XPATH, LB.driver_link_xpath))

    def click_event_id_link(self):
        self.wait_till_element_disappear((By.XPATH, LB.video_player_xpath))
        self.click((By.XPATH, LB.event_id_link_xpath))

    def click_issued_by_link(self):
        self.click((By.XPATH, LB.issued_by_link_xpath))

    def click_filter_by_event_id(self):
        self.click((By.XPATH, LB.filter_by_event_id_dropdown_xpath))

    def click_filter_by_issued_by(self):
        self.click((By.XPATH, LB.filter_by_issued_by_dropdown_xpath))

    def click_filter_by_driver(self):
        self.click((By.XPATH, LB.filter_by_driver_dropdown_xpath))

    def click_select_search(self):
        self.click((By.ID, LB.filter_by_search_dropdown_id))

    def type_in_search_criteria_textbox_rh(self, search_text):
        self.type((By.XPATH, LB.filter_by_search_criteria_textbox_xpath), search_text)

    def type_event_id_rh(self, event_id):
        self.type((By.XPATH, LB.filter_by_event_id_textbox_xpath), event_id)

    def select_search_criteria_result_rh_list(self):
        sleep(2)
        self.type((By.XPATH, LB.filter_by_search_criteria_textbox_xpath), Keys.ENTER)

    def select_search_event_id_rh(self):
        self.type((By.XPATH, LB.filter_by_event_id_textbox_xpath), Keys.ENTER)

    def select_search_criteria_result_device_id(self):
        self.click((By.XPATH, LB.device_id_button_xpath))

    def get_driver_name_rh(self):
        return self.get_text((By.XPATH, LB.driver_link_xpath))

    def get_issued_by_name_rh(self):
        return self.get_text((By.XPATH, LB.issued_by_link_xpath))

    def get_event_id_number_rh(self):
        return self.get_text((By.XPATH, LB.event_id_link_xpath))

    def click_close_on_success_message(self):
        self.click((By.XPATH, LB.move_group_continue_button_xpath))

    def click_continue_on_move_group(self):
        self.click((By.XPATH, LB.move_group_continue_button_xpath))

    def click_done_on_change_group(self):
        self.click((By.XPATH, LB.change_group_done_button_xpath))

    def click_move_group(self):
        self.click((By.XPATH, LB.move_group_button_xpath))

    def select_first_checkbox(self):
        self.click((By.XPATH, LB.select_first_event_id_checkbox_xpath))

    def click_yes_confirm_button(self):
        self.click((By.XPATH, LB.yes_confirm_button_xpath))

    def click_cancel(self):
        self.click((By.XPATH, LB.cancel_button_xpath))

    def click_coach_now(self):
        self.click((By.ID, LB.coach_now_button_id))

    def click_coach_later(self):
        self.click((By.ID, LB.coach_later_button_id))

    def click_resolve(self):
        self.click((By.ID, LB.resolve_button_id))

    def click_close_status_dropdown(self):
        self.click((By.XPATH, LB.close_status_dropdown_button_xpath))

    def select_search_name_in_event_preview(self):
        self.click((By.XPATH, LB.select_search_name_xpath))

    def click_assign_button_in_event_preview(self):
        self.click((By.XPATH, LB.event_preview_assign_button_xpath))

    def enter_driver_name(self, driver_name):
        self.type((By.XPATH, LB.event_preview_assign_driver_textbox_xpath), driver_name)

    def click_assign_group_button_in_event_preview(self):
        self.click((By.XPATH, LB.more_actions_button_reassign_group_xpath))

    def enter_group_name(self, group_name):
        self.type((By.XPATH, LB.event_preview_assign_group_textbox_xpath), group_name)

    def select_group_event_preview(self):
        self.click((By.XPATH, LB.event_preview_select_group_xpath))

    def click_done_button_event_preview(self):
        self.click((By.XPATH, LB.event_preview_done_button_xpath))

    def click_done_button_assign_group(self):
        self.click((By.XPATH, LB.reassign_group_done_button_xpath))

    def click_expand_icon(self):
        self.click((By.XPATH, LB.event_detail_expand_icon_xpath))

    def get_event_group_text(self):
        return self.get_text((By.XPATH, LB.event_group_text_xpath))

    def click_mark_as_self_coaching(self):
        self.click((By.XPATH, LB.mark_as_self_coaching_button_xpath))

    # click reassign driver when there IS driver assigned to the event
    def click_reassign_driver(self):
        self.click((By.XPATH, LB.reassign_driver_button_xpath))

    # click reassign driver when there is NO driver assigned to the event
    def click_reassign_driver_event_no_driver(self):
        self.click((By.XPATH, LB.reassign_driver_button_wd_xpath))

    def click_more_actions(self):
        self.click((By.XPATH, LB.more_actions_button_xpath))

    def click_more_actions_ar(self):
        self.click((By.XPATH, LB.more_actions_button_ar_xpath))

    def click_close_recognition(self):
        self.click((By.XPATH, LB.close_recognition_button_xpath))

    def click_complete_recognition(self):
        self.click((By.XPATH, LB.complete_recognition_button_xpath))

    def click_add_recognition(self):
        n = 0
        while n < 5:
            n += 1
            if self.get_text((By.XPATH, LB.add_recognition_button_xpath)) == 'Add Recognition':
                break
            else:
                sleep(5)
        self.click((By.XPATH, LB.add_recognition_button_xpath))

    def click_search_button(self):
        self.click((By.XPATH, LB.select_search_button_xpath))

    def click_search_dropdown(self):
        self.click((By.ID, LB.select_search_drop_down_id))

    def select_device(self):
        self.click((By.XPATH, LB.select_device_button_xpath))

    def select_vehicle(self):
        self.click((By.XPATH, LB.select_vehicle_button_xpath))

    def select_driver(self):
        self.click((By.XPATH, LB.select_driver_button_xpath))

    def type_search_criteria_event_list(self, search_text):
        self.type((By.XPATH, LB.event_list_search_criteria_xpath), search_text)

    def type_event_id_event_list(self, event_id):
        self.type((By.XPATH, LB.event_list_search_event_id_xpath), event_id)

    def select_search_criteria_result_event_list(self):
        sleep(2)
        self.type((By.XPATH, LB.event_list_search_criteria_xpath), Keys.ENTER)

    def select_search_event_id_event_list(self):
        self.type((By.XPATH, LB.event_list_search_event_id_xpath), Keys.ENTER)

    def select_event_id(self):
        self.click((By.XPATH, LB.select_event_id_button_xpath))

    def get_event_id_number(self):
        return self.get_text((By.XPATH, LB.event_id_button_xpath))

    def get_driver_name(self):
        return self.get_text((By.XPATH, LB.driver_name_text_xpath))

    def get_vehicle_name(self):
        return self.get_text((By.XPATH, LB.vehicle_name_text_xpath))

    def get_device_name(self):
        return self.get_text((By.XPATH, LB.device_name_text_xpath))

    def select_face_to_face(self):
        self.click((By.XPATH, LB.select_face_to_face_button_xpath))

    def select_fyi_notify(self):
        self.click((By.XPATH, LB.select_fyi_notify_button_xpath))

    def click_statuses_close_button(self):
        self.click((By.XPATH, LB.statuses_close_button_xpath))

    def click_statuses_dropdown(self):
        self.click((By.ID, LB.filter_by_status_button_id))

    def select_handheld_device(self):
        self.click((By.XPATH, LB.select_handheld_device_button_xpath))

    def click_behaviors_close_button(self):
        self.click((By.XPATH, LB.behaviors_close_button_xpath))

    def click_behaviors_dropdown(self):
        self.click((By.ID, LB.filter_by_behavior_button_id))

    def select_none_selected(self):
        self.click((By.XPATH, LB.select_none_selected_button_xpath))

    def select_trigger_filter_event_page(self, trigger_order):
        trigger_xpath = LB.trigger_filter_xpath_prefix + str(trigger_order) + ']'
        self.click((By.XPATH, trigger_xpath))

    def select_behavior_filter_event_page(self, behavior_name):
        self.wait_for_element_displayed((By.XPATH, LocatorUtil.give_locator(LB.behavior_filter_xpath, behavior_name)))
        self.click((By.XPATH, LocatorUtil.give_locator(LB.behavior_filter_xpath, behavior_name)))

    def click_triggers_close_button(self):
        self.click((By.XPATH, LB.triggers_close_button_xpath))

    def click_triggers_dropdown(self):
        self.click((By.ID, LB.filter_by_trigger_button_id))

    def click_type_dropdown(self):
        self.click((By.ID, LB.filter_by_type_button_id))

    def click_reset_button(self):
        self.click((By.XPATH, LB.reset_button_xpath))

    def select_date_dropdown(self):
        self.click((By.XPATH, LB.select_date_button_xpath))

    def select_last_7_days(self):
        self.click((By.XPATH, LB.select_last_7_days_button_xpath))

    def select_last_90_days(self):
        self.click((By.XPATH, LB.select_last_90_days_button_xpath))

    def set_date_range_events_page(self, start_month, start_day, start_year, end_month, end_day, end_year):
        self.click((By.XPATH, LB.events_page_date_range_start_year_xpath))
        self.type((By.XPATH, LB.events_page_date_range_start_year_xpath), start_year)
        self.click((By.XPATH, LB.events_page_date_range_start_month_xpath))
        self.type((By.XPATH, LB.events_page_date_range_start_month_xpath), start_month)
        self.click((By.XPATH, LB.events_page_date_range_start_day_xpath))
        self.type((By.XPATH, LB.events_page_date_range_start_day_xpath), start_day)
        self.click((By.XPATH, LB.events_page_date_range_end_year_xpath))
        self.type((By.XPATH, LB.events_page_date_range_end_year_xpath), end_year)
        self.click((By.XPATH, LB.events_page_date_range_end_month_xpath))
        self.type((By.XPATH, LB.events_page_date_range_end_month_xpath), end_month)
        self.click((By.XPATH, LB.events_page_date_range_end_day_xpath))
        self.type((By.XPATH, LB.events_page_date_range_end_day_xpath), end_day)

    def click_apply_button(self):
        self.click((By.ID, LB.apply_button_id))

    def select_coachable(self):
        self.click((By.XPATH, LB.select_coachable_button_xpath))

    def click_filter_by_group(self):
        self.click((By.ID, LB.filter_by_group_button_id))

    def enter_group(self, group_name):
        self.type((By.XPATH, LB.search_by_group_box_xpath), group_name)

    def click_select_group(self):
        self.click((By.XPATH, LB.select_group_search_xpath))

    def click_done(self):
        self.click((By.XPATH, LB.done_button_xpath))

    def get_sessions_label(self):
        return self.get_text((By.XPATH, LB.sessions_label_xpath))

    def get_sessions_label_new_UI(self):
        return self.get_text((By.XPATH, LB.sessions_label_xpath_new_UI))

    def get_event_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, LB.event_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, LB.event_count_xpath))

    def get_event_id(self):
        return self.get_text((By.XPATH, LB.event_id_text_xpath))

    def get_driver(self):
        return self.get_text((By.XPATH, LB.driver_text_xpath))

    def get_group(self):
        return self.get_text((By.XPATH, LB.group_text_xpath))

    def get_vehicle(self):
        return self.get_text((By.XPATH, LB.vehicle_text_xpath))

    def get_device(self):
        return self.get_text((By.XPATH, LB.device_text_xpath))

    def get_event_date(self):
        return self.get_text((By.XPATH, LB.event_date_text_xpath))

    def get_score(self):
        return self.get_text((By.XPATH, LB.score_text_xpath))

    def get_status(self):
        return self.get_text((By.XPATH, LB.status_text_xpath))

    def get_trigger(self):
        return self.get_text((By.XPATH, LB.trigger_text_xpath))

    def get_behaviors(self):
        return self.get_text((By.XPATH, LB.behaviors_text_xpath))

    def get_preview_title(self):
        return self.get_text((By.XPATH, LB.events_preview_text_xpath))

    def get_recognition_status_text(self, expected_status):
        n = 0
        while n < 10:
            n += 1
            if self.get_text((By.XPATH, LB.add_recognition_button_xpath)) == expected_status:
                break
            else:
                sleep(5)
        return self.get_text((By.XPATH, LB.add_recognition_button_xpath))

    def get_success_event_assigned_dialog_text(self):
        return self.get_text((By.XPATH, LB.success_event_assigned_dialog_xpath))

    def get_success_event_moved_dialog_text(self):
        return self.get_text((By.XPATH, LB.success_event_moved_dialog_xpath))

    def get_event_preview_status_text(self):
        return self.get_text((By.XPATH, LB.event_preview_status_xpath))

    def get_type_column_name_text(self):
        return self.get_text((By.XPATH, LB.type_column_name_xpath))

    def get_driver_column_name_text(self):
        return self.get_text((By.XPATH, LB.driver_column_name_xpath))

    def get_group_column_name_text(self):
        return self.get_text((By.XPATH, LB.group_column_name_recognition_history_xpath))

    def get_event_id_column_name_text(self):
        return self.get_text((By.XPATH, LB.event_id_column_name_xpath))

    def get_issued_by_column_name_text(self):
        return self.get_text((By.XPATH, LB.issued_by_column_name_xpath))

    def get_issued_date_column_name_text(self):
        return self.get_text((By.XPATH, LB.issued_date_column_name_xpath))

    def get_recognition_reason_column_name_text(self):
        return self.get_text((By.XPATH, LB.recognition_reason_column_name_xpath))

    def get_recognition_title_text(self):
        return self.get_text((By.XPATH, LB.recognition_certificate_title_xpath))

    def click_driver_name(self):
        self.click((By.XPATH, LB.driver_name_text_xpath))

    def click_event_id(self):
        self.wait_till_element_disappear((By.XPATH, LB.video_player_xpath))
        self.click((By.XPATH, LB.event_id_button_xpath))

    def close_preview_window(self):
        i = 0
        while i < 10:
            i += 1
            try:
                self.click((By.XPATH, LB.close_preview_button_xpath))
                break
            except (ElementClickInterceptedException, StaleElementReferenceException):
                sleep(4)

        if i >= 10:
            self.click((By.XPATH, LB.close_preview_button_xpath))

    def select_behaviors_dropdown(self):
        self.click((By.XPATH, LB.behaviors_drop_down_xpath))

    def select_unusual_behavior(self):
        self.click((By.XPATH, LB.unusual_event_check_box_xpath))

    def select_dropdown_ch(self):
        self.click((By.XPATH, LB.select_search_drop_down_ch_xpath))

    def click_filter_by_coach(self):
        self.click((By.XPATH, LB.filter_by_coach_dropdown_xpath))

    def select_coach(self):
        self.click((By.XPATH, LB.coaching_history_coach_xpath))

    def select_driver_ch(self):
        self.click((By.XPATH, LB.coaching_history_driver_xpath))

    def select_session_id(self):
        self.click((By.XPATH, LB.coaching_history_session_id_xpath))

    def enter_coach_name(self, coach_name):
        self.type((By.XPATH, LB.search_name_or_id_ch_textbox_xpath), coach_name)

    def enter_driver_name_ch(self, driver_name):
        self.type((By.XPATH, LB.search_name_or_id_ch_textbox_xpath), driver_name)

    def enter_session_id(self, session_id):
        self.type((By.XPATH, LB.search_session_id_ch_textbox_xpath), session_id)

    def select_driver_in_dropdown(self):
        self.click((By.XPATH, LB.first_driver_in_dropdown_xpath))

    def select_coach_in_dropdown(self):
        self.click((By.XPATH, LB.first_coach_in_dropdown_xpath))

    def select_session_id_in_coaching_history(self):
        self.click((By.XPATH, LB.session_id_value_xpath))

    def select_driver_in_coaching_history(self):
        self.click((By.XPATH, LB.driver_value_xpath))

    def select_coach_in_coaching_history(self):
        self.click((By.XPATH, LB.coach_value_xpath))

    def get_past_session_title_text(self):
        return self.get_text((By.XPATH, LB.past_session_title_xpath))

    def get_summary_label(self):
        return self.get_text((By.XPATH, LB.summary_label_xpath))

    def get_session_notes_label(self):
        return self.get_text((By.XPATH, LB.session_notes_label_xpath))

    def get_event_coached_label(self):
        return self.get_text((By.XPATH, LB.event_coached_label_xpath))

    def click_data_export(self):
        self.click((By.XPATH, LB.data_export_tab_xpath))

    def click_data_export_new_ui(self):
        self.click((By.XPATH, LB.data_export_tab_xpath_new_ui))

    def get_data_export_title_text(self):
        return self.get_text((By.XPATH, LB.data_export_title_xpath))

    def get_report_type_text(self):
        return self.get_text((By.XPATH, LB.report_type_column_name_xpath))

    def get_group_column_text(self):
        return self.get_text((By.XPATH, LB.group_column_name_xpath))

    def get_date_range_column_text(self):
        return self.get_text((By.XPATH, LB.date_range_column_name_xpath))

    def get_filters_column_text(self):
        return self.get_text((By.XPATH, LB.filters_column_name_xpath))

    def get_requested_date_column_text(self):
        return self.get_text((By.XPATH, LB.requested_date_column_name_xpath))

    def get_action_column_text(self):
        return self.get_text((By.XPATH, LB.action_column_name_xpath))

    def get_new_export_button_text(self):
        return self.get_text((By.XPATH, LB.new_export_button_xpath))

    def click_new_export(self):
        self.click((By.XPATH, LB.new_export_button_xpath))

    def get_requested_date_1st_request_date(self):
        n = 0
        while n < 5:
            n += 1
            try:
                return self.get_text((By.XPATH, LB.requested_date_1st_request_xpath))
                break
            except (ElementClickInterceptedException, StaleElementReferenceException):
                sleep(6)

        if n == 5:
            return self.get_text((By.XPATH, LB.requested_date_1st_request_xpath))

    def get_report_type_value(self):
        return self.get_text((By.XPATH, LB.report_type_value_xpath))

    def wait_for_download_data_export(self):
        status = ""
        generate_time: int = 0
        while status != "Download":
            sleep(10)
            self.click_refresh_button()
            sleep(5)
            status = self.get_text((By.XPATH, LB.data_export_action_xpath))
            generate_time += 1
            if generate_time == 30:
                break

    def click_download_data_export(self):
        self.wait_for_download_data_export()
        self.click((By.XPATH, LB.data_export_action_xpath))
        # wait for download complete
        sleep(20)

    def get_request_date_range(self):
        return self.get_text((By.XPATH, LB.request_date_range_text_xpath))

    def get_data_export_file_name(self, report_type):
        date_range = self.get_request_date_range().split("—")
        date_start_text = date_range[0].strip()
        date_start = datetime.strptime(date_start_text, "%b %d, %Y").strftime("%Y-%m-%d")
        date_end_text = date_range[-1].strip()
        date_end = datetime.strptime(date_end_text, "%b %d, %Y").strftime("%Y-%m-%d")

        file_name = report_type + ' ' + date_start + '_' + date_end + '.csv'
        return file_name

    def click_report_type_dropdown(self):
        self.click((By.ID, LB.report_type_dropdown_id))

    def click_event_data(self):
        self.click((By.XPATH, LB.event_data_text_xpath))

    def click_speed_data(self):
        self.click((By.XPATH, LB.speed_data_text_xpath))

    def click_request_data(self):
        self.click((By.ID, LB.request_data_button_id))
        sleep(2)

    def get_session_id_label(self):
        return self.get_text((By.XPATH, LB.session_ID_label_xpath))

    def get_coach_date_label(self):
        return self.get_text((By.XPATH, LB.coach_date_label_xpath))

    def get_overdue_date_label(self):
        return self.get_text((By.XPATH, LB.overdue_date_label_xpath))

    def get_driver_label(self):
        return self.get_text((By.XPATH, LB.driver_label_xpath))

    def get_behavior_coached_label(self):
        return self.get_text((By.XPATH, LB.behaviors_coached_label_xpath))

    def get_group_label(self):
        return self.get_text((By.XPATH, LB.group_label_xpath))

    def get_coach_label(self):
        return self.get_text((By.XPATH, LB.coach_label_xpath))

    def get_action_plan_label(self):
        return self.get_text((By.XPATH, LB.action_plan_label_xpath))

    def get_notes_label(self):
        return self.get_text((By.XPATH, LB.notes_label_xpath))

    def get_first_event_status(self):
        try:
            return self.get_text((By.XPATH, LB.first_event_status_xpath))
        except TimeoutException:
            return self.get_text((By.XPATH, LB.first_event_status_xpath))

    def get_first_event_behavior(self):
        self.wait_for_element_displayed((By.XPATH, LB.first_event_behavior_xpath))
        return self.get_text((By.XPATH, LB.first_event_behavior_xpath))

    def get_first_event_driver(self):
        return self.get_text((By.XPATH, LB.first_event_driver_xpath))

    def delete_recognitions(self):
        count = self.get_row_count()
        i = 0
        while i < count:
            self.click_first_recognition()
            self.click_delete_recognition_button()
            self.click_delete_recognition_confirmation_button()
            i = + 1

    def delete_recognitions_new_UI(self):
        self.click_first_recognition()
        self.click_delete_recognition_button()
        self.click_delete_recognition_confirmation_button()

    def click_mark_as_fyi_notify(self):
        self.click((By.XPATH, LB.mark_as_fyi_notify_button_xpath))

    def click_confirm_mark_as_fyi_notify(self):
        self.click((By.XPATH, LB.confirm_mark_as_fyi_notify_button_xpath))

    def close_walkme(self):
        walkme_dialog_count = len(self.find_elements((By.XPATH, LB.walkme_close_button_xpath)))
        i = 0
        while i < walkme_dialog_count:
            self.find_elements((By.XPATH, LB.walkme_close_button_xpath))[0].click()
            i += 1
            sleep(2)

    def event_count_is_displayed(self):
        result = self.element_is_displayed((By.XPATH, LB.event_count_xpath))
        # if result is False:
        #     raise TimeoutException
        return result
        # return self.element_is_displayed((By.XPATH, LB.event_count_xpath))

    def event_displayed_with_details(self):
        result = self.element_is_displayed((By.XPATH, LB.event_row_with_details_xpath))
        # if result is False:
        #     raise TimeoutException
        return result
        # return self.element_is_displayed((By.XPATH, LB.event_row_with_details_xpath))

    def click_add_behavior(self):
        self.click((By.XPATH, LB.add_behavior_xpath))

    def click_edit_behavior(self):
        self.click((By.ID, LB.edit_behavior_id))

    def add_behavior_and_save(self):
        if self.element_is_displayed((By.XPATH, LB.add_behavior_xpath)) is True:
            self.click((By.XPATH, LB.add_behavior_xpath))
            sleep(2)
        self.click((By.XPATH, LB.plus_add_behavior_xpath))
        sleep(2)
        self.click((By.XPATH, LB.event_preview_add_behavior_drop_down_xpath))
        sleep(2)
        BEHAVIOR_NAME = self.get_text((By.XPATH, LB.select_first_behavior_in_drop_down_xpath))
        self.click((By.XPATH, LB.select_first_behavior_in_drop_down_xpath))
        self.click((By.XPATH, LB.select_behavior_not_captured_reason))
        self.click((By.ID, LB.reason_done_button_id))
        self.click((By.XPATH, LB.event_preview_add_behavior_save_button_xpath))
        return BEHAVIOR_NAME

    def remove_first_behavior(self, BEHAVIOR_NAME=None):
        remove_behavior_xpath = f"//*[text()='{BEHAVIOR_NAME}']/following-sibling::button"
        self.click((By.ID, LB.edit_behavior_id))
        if BEHAVIOR_NAME is None:
            self.click((By.XPATH, LB.remove_behavior_button_xpath))
        else:
            self.click((By.XPATH, remove_behavior_xpath))
        self.click((By.XPATH, LB.select_incorrect_behavior_identified_reason))
        self.click((By.ID, LB.reason_done_button_id))
        self.click((By.XPATH, LB.event_preview_add_behavior_save_button_xpath))

    def get_first_behavior_text(self):
        return self.get_text((By.XPATH, LB.first_behavior))

    def get_second_behavior_text(self):
        return self.get_text((By.XPATH, LB.second_behavior))

    def second_behavior_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LB.second_behavior))

    def event_count_displayed(self):
        self.wait_for_element_displayed((By.XPATH, LB.event_count_xpath))
        elements = self.find_elements((By.XPATH, LB.event_count_xpath))
        return len(elements) > 0

    def get_group_name_event_page(self):
        return self.get_text((By.XPATH, LB.group_name_event_page_xpath))

    def get_vehicle_name_event_page(self):
        return self.get_text((By.XPATH, LB.vehicle_name_event_page_xpath))

    def recognition_count_displayed(self):
        self.wait_for_element_displayed((By.XPATH, LB.recognition_count_xpath))
        elements = self.find_elements((By.XPATH, LB.recognition_count_xpath))
        return len(elements) > 0

    def get_group_name_recognition_page(self):
        self.wait_for_element_displayed((By.XPATH, LB.group_name_recognition_page_xpath))
        return self.get_text((By.XPATH, LB.group_name_recognition_page_xpath))

    def get_recognitions_count(self):
        self.wait_for_element_displayed((By.XPATH, LB.recognition_count_xpath))
        return self.get_text((By.XPATH, LB.recognition_count_xpath))

    def coaching_history_count_displayed(self):
        self.wait_for_element_displayed((By.XPATH, LB.session_count_label_xpath))
        elements = self.find_elements((By.XPATH, LB.session_count_label_xpath))
        return len(elements) > 0

    def get_recognition_text(self):
        return self.element_is_displayed((By.XPATH, LB.recognition_text_xpath))

    def click_recognition(self):
        self.click((By.XPATH, LB.recognition_text_xpath))

    def click_filter_by_group_recognition_history(self):
        self.click((By.ID, LB.filter_by_group_recognition_history_id))

    def click_filter_by_group_coaching_history(self):
        self.click((By.ID, LB.filter_by_group_coaching_history_id))

    def get_added_behavior_text(self):
        self.wait_till_element_disappear((By.XPATH, LB.loading_indicator_xpath))
        behaviors = self.find_elements((By.XPATH, LB.added_behavior_text_xpath))
        behavior_names = [elem.text.strip() for elem in behaviors]
        return behavior_names

    def get_behavior_name(self):
        self.wait_till_element_disappear((By.XPATH, LB.loading_indicator_xpath))
        return self.get_text((By.XPATH, LB.behavior_name_xpath))

    def click_download_button(self):
        self.click((By.XPATH, LB.download_button_xpath))

    def click_mp4_button(self):
        self.click((By.XPATH, LB.mp4_button_xpath))

    def get_event_video_file_name_with_format(self, EVENT_ID_LIBRARY):
        file_name = EVENT_ID_LIBRARY + '.MP4'
        return file_name

    def get_coaching_date_text_coaching_history_tab(self):
        return self.get_text((By.XPATH, LB.coaching_date_text_coaching_history_tab_xpath))


    def click_browse_in_video_search(self):
        self.click((By.XPATH, LB.browse_in_video_search_xpath))

    def click_browse_button(self):
        self.click((By.XPATH, LB.browse_button_xpath))

    def emp_id_visible_next_to_driver_name(self):
        return self.element_is_displayed((By.XPATH, LB.emp_id_next_to_driver_name_xpath))

    def is_overlay_toggle_disabled(self):
        return self.element_is_displayed((By.XPATH, LB.overlay_toggle_xpath))

    def is_overlay_label_displayed(self):
        return self.element_is_displayed((By.XPATH, LB.overlay_label_xpath))

    def hover_over_overlay_toggle(self):
        element = self.find((By.XPATH, LB.overlay_toggle_xpath))
        self.move_to_element(element)

    def get_overlay_tooltip_text(self):
        return self.get_text((By.XPATH, LB.overlay_tooltip_xpath))

    def click_download_button_event_preview(self):
        self.click((By.XPATH, LB.download_button_event_preview_xpath))

    def get_download_option_dce_text(self):
        return self.get_text((By.XPATH, LB.download_option_dce_xpath))

    def get_download_option_mp4_with_overlay_text(self):
        return self.get_text((By.XPATH, LB.download_option_mp4_with_overlay_xpath))

    def get_download_option_mp4_without_overlay_text(self):
        return self.get_text((By.XPATH, LB.download_option_mp4_without_overlay_xpath))

    def search_fd_event_adas_data_in_search_bar(self, event_id):
        self.click((By.XPATH, LB.library_search_bar_xpath))
        self.type((By.XPATH, LB.library_search_input_xpath), event_id)
        self.click((By.XPATH, LB.library_search_button_xpath))
        self.wait_till_element_disappear((By.XPATH, LB.loading_indicator_xpath))

    def click_event_in_past_session(self):
        self.click((By.XPATH, LB.event_id_link_coaching_history_xpath))

    def click_download_option_dce(self):
        self.click((By.XPATH, LB.download_option_dce_xpath))

    def click_download_option_mp4_with_overlay(self):
        self.click((By.XPATH, LB.download_option_mp4_with_overlay_xpath))
        self.wait_till_element_disappear((By.XPATH, LB.download_loading_xpath))

    def click_download_option_mp4_without_overlay(self):
        self.click((By.XPATH, LB.download_option_mp4_without_overlay_xpath))

