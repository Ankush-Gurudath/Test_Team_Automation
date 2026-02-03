from datetime import datetime
from time import sleep

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By

from locators.locators_user_management import LocatorsUserManagement as UM
from pages.base_page import BasePage


class UserManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_user_management_label(self):
        return self.get_text((By.XPATH, UM.user_management_label_xpath))

    def user_management_label_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, UM.user_management_label_xpath))

    def get_name_label(self):
        return self.get_text((By.XPATH, UM.name_label_xpath))

    def get_employee_id_label(self):
        return self.get_text((By.XPATH, UM.employee_id_label_xpath))

    def get_lytx_badge_label(self):
        return self.get_text((By.XPATH, UM.lytx_badge_label_xpath))

    def get_primary_driver_group_label(self):
        return self.get_text((By.XPATH, UM.primary_driver_group_label_xpath))

    def get_roles_label(self):
        return self.get_text((By.XPATH, UM.roles_label_xpath))

    def get_status_label(self):
        return self.get_text((By.XPATH, UM.status_label_xpath))

    def get_login_label(self):
        return self.get_text((By.XPATH, UM.login_label_xpath))

    def get_user_name_label(self):
        return self.get_text((By.XPATH, UM.username_label_xpath))

    def click_select_group_filter(self):
        self.element_is_displayed((By.XPATH, UM.group_filter_first_button_xpath))
        n = 0
        while n < 10:
            n += 1
            try:
                self.click((By.XPATH, UM.group_filter_first_button_xpath))
                break
            except (StaleElementReferenceException, ElementClickInterceptedException):
                sleep(5)
        if n == 5:
            self.click((By.XPATH, UM.group_filter_first_button_xpath))

    def search_group_filter(self, group_name):
        self.type((By.XPATH, UM.search_group_filter_textbox_xpath), group_name)

    def select_searched_group(self):
        self.click((By.XPATH, UM.select_searched_group_filter_xpath))

    def click_done_group_filter(self):
        self.click((By.XPATH, UM.done_group_filter_button_xpath))

    def click_restore_user_button(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click((By.XPATH, UM.restore_user_button_xpath))

    def click_roles_filter(self):
        self.click((By.XPATH, UM.roles_filter_button_xpath))

    def select_roles_filter(self):
        self.click((By.XPATH, UM.select_roles_filter_xpath))

    def apply_select_role(self):
        self.click((By.XPATH, UM.apply_select_role_xpath))

    def click_login_filter(self):
        self.click((By.XPATH, UM.login_filter_button_xpath))

    def select_login_filter(self):
        self.click((By.XPATH, UM.select_login_filter_xpath))

    def click_status_filter(self):
        self.wait_for_element_is_clickable((By.XPATH, UM.status_filter_button_xpath))
        self.click((By.XPATH, UM.status_filter_button_xpath))

    def select_status_filter(self):
        self.click((By.XPATH, UM.select_status_filter_xpath))

    def search_name_filter(self, name):
        try:
            self.wait_for_element_displayed((By.XPATH, UM.search_filter_textbox_xpath))
            self.clear((By.XPATH, UM.search_filter_textbox_xpath))
            self.type((By.XPATH, UM.search_filter_textbox_xpath), name)
        except (TimeoutException, StaleElementReferenceException):
            self.wait_for_element_displayed((By.XPATH, UM.search_filter_textbox_xpath))
            self.clear((By.XPATH, UM.search_filter_textbox_xpath))
            self.type((By.XPATH, UM.search_filter_textbox_xpath), name)

    def click_reset_button(self):
        self.wait_for_element_displayed((By.XPATH, UM.reset_button_xpath))
        self.click((By.XPATH, UM.reset_button_xpath))

    def click_select_all_checkbox(self):
        self.click((By.XPATH, UM.select_all_checkbox_xpath))

    def click_clear_search_button(self):
        self.wait_for_element_displayed((By.XPATH, UM.clear_search_button_xpath))
        self.click((By.XPATH, UM.clear_search_button_xpath))

    def click_active_filter(self):
        self.click((By.XPATH, UM.roles_filter_active_xpath))

    def click_close_status_filter(self):
        self.wait_for_element_is_clickable((By.XPATH, UM.close_status_filter))
        self.click((By.XPATH, UM.close_status_filter))

    def click_add_user(self):
        self.wait_for_element_displayed((By.XPATH, UM.add_user_button_xpath))
        self.click((By.XPATH, UM.add_user_button_xpath))

    def get_user_added_text(self):
        self.wait_for_element_displayed((By.XPATH, UM.user_added_text_xpath))
        return self.get_text((By.XPATH, UM.user_added_text_xpath))

    def click_expected_user(self, username):
        self.wait_for_expected_text((By.XPATH, UM.first_row_user_text_xpath), username)
        self.click((By.XPATH, UM.first_row_user_text_xpath))

    def click_first_user(self):
        self.click((By.XPATH, UM.first_row_user_text_xpath))

    def get_user_group_label(self):
        self.wait_for_element_displayed((By.XPATH, UM.roles_first_row_text_xpath))
        return self.get_text((By.XPATH, UM.roles_first_row_text_xpath))

    def get_first_user_status(self):
        self.wait_for_element_displayed((By.XPATH, UM.status_first_user_xpath))
        return self.get_text((By.XPATH, UM.status_first_user_xpath))

    def click_user_added(self):
        self.click((By.XPATH, UM.user_added_text_xpath))

    def click_users_tab(self):
        self.click((By.XPATH, UM.users_tab_xpath))

    def get_user_edited_text(self):
        return self.get_text((By.XPATH, UM.user_edited_text_xpath))

    def get_first_user_text(self, username):
        self.wait_for_expected_text((By.XPATH, UM.first_row_user_text_xpath), username)
        return self.get_text((By.XPATH, UM.first_row_user_text_xpath))

    def get_first_user_login_text(self):
        return self.get_text((By.XPATH, UM.login_first_user_text_xpath))

    def get_second_user_status(self):
        return self.get_text((By.XPATH, UM.second_user_status_xpath))

    def get_filtered_user_login(self):
        self.wait_for_element_displayed((By.XPATH, UM.filtered_user_login_xpath))
        return self.get_text((By.XPATH, UM.filtered_user_login_xpath))

    def click_active_status(self):
        self.click((By.XPATH, UM.select_active_status_xpath))

    def click_devices_tab(self):
        self.click((By.XPATH, UM.devices_tab_xpath))

    def click_vehicle_tab(self):
        self.click((By.XPATH, UM.vehicles_tab_xpath))
        self.click((By.XPATH, UM.reset_button_xpath))

    def click_driver_id_tab(self):
        self.click((By.XPATH, UM.driver_id_tab_xpath))

    def click_insights_tab(self):
        self.scroll_to_element(self.find((By.XPATH, UM.equipment_management_tab_xpath)))
        self.click((By.XPATH, UM.insights_tab_xpath))

    def click_driver_id_assignment_tab(self):
        self.click((By.XPATH, UM.driver_id_assignment_tab_xpath))

    def click_device_health_tab(self):
        self.click((By.XPATH, UM.device_health_tab_xpath))

    def click_config_setting_tab(self):
        self.click((By.XPATH, UM.config_setting_tab_xpath))

    def click_geofences_tab(self):
        self.click((By.XPATH, UM.geofences_tab_xpath))

    def check_first_user(self):
        self.wait_for_element_displayed((By.XPATH, UM.check_first_user_xpath))
        n = 0
        while n < 10:
            n += 1
            try:
                self.click((By.XPATH, UM.check_first_user_xpath))
                break
            except (StaleElementReferenceException, ElementClickInterceptedException):
                sleep(5)
        if n == 5:
            self.click((By.XPATH, UM.check_first_user_xpath))

    def click_batch_delete_user(self):
        self.click((By.XPATH, UM.batch_delete_user_button_xpath))

    def click_confirm_button(self):
        self.wait_for_element_displayed((By.XPATH, UM.confirm_button_batch_delete_user_xpath))
        self.click((By.XPATH, UM.confirm_button_batch_delete_user_xpath))
        self.wait_till_element_disappear((By.XPATH, UM.users_deleted_success_message_xpath))
        self.wait_for_page_load()

    def clear_status_filter(self):
        self.click((By.XPATH, UM.clear_status_filter_xpath))

    def get_status_of_deleted_user(self):
        return self.get_text((By.XPATH, UM.status_of_deleted_user_xpath))

    def click_edit_group_button(self):
        self.click((By.XPATH, UM.edit_group_button_xpath))

    def click_group_filter_on_edit_group_dialog(self):
        self.click((By.XPATH, UM.group_filter_on_edit_group_dialog_xpath))

    def search_group_on_edit_group_dialog(self, group_name):
        self.type((By.XPATH, UM.search_group_textbox_on_edit_group_dialog_xpath), group_name)

    def select_searched_group_on_edit_group_dialog(self):
        self.click((By.XPATH, UM.select_searched_group_on_edit_group_dialog_xpath))

    def click_done_on_edit_group_dialog(self):
        self.wait_for_element_displayed((By.XPATH, UM.done_button_on_edit_group_dialog_xpath))
        self.click((By.XPATH, UM.done_button_on_edit_group_dialog_xpath))

    def click_role_filter_on_edit_group_dialog(self):
        self.click((By.XPATH, UM.role_filter_on_edit_group_dialog_xpath))

    def select_driver_role_on_edit_group_dialog(self):
        self.click((By.XPATH, UM.select_driver_role_on_edit_group_dialog_xpath))

    def click_apply_on_edit_group_dialog(self):
        self.click((By.XPATH, UM.apply_button_on_edit_group_dialog_xpath))
        self.wait_till_element_disappear((By.XPATH, UM.user_moved_success_message_xpath))

    def click_change_status_button(self):
        self.click((By.XPATH, UM.change_status_button_xpath))

    def select_inactive_status(self):
        self.click((By.XPATH, UM.inactive_status_radio_button_xpath))

    def select_delete_status(self):
        self.click((By.XPATH, UM.delete_status_xpath))

    def click_apply_set_user_status(self):
        self.click((By.XPATH, UM.apply_button_on_set_user_status_xpath))
        self.wait_till_element_disappear((By.XPATH, UM.status_updated_success_message_xpath))

    def click_more_action(self):
        self.click((By.XPATH, UM.more_action_xpath))

    def click_edit_login(self):
        self.click((By.XPATH, UM.edit_login_button_xpath))

    def click_apply_on_edit_login(self):
        self.click((By.XPATH, UM.apply_button_on_edit_login_xpath))

    def get_user_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, UM.user_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, UM.user_count_xpath))

    def user_count_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, UM.user_count_xpath))

    def click_driver_id(self):
        self.click((By.XPATH, UM.driver_id_of_first_user_xpath))
        self.scroll_page_down()

    def get_cancel_button_text(self):
        self.scroll_page_down()
        return self.get_text((By.XPATH, UM.cancel_button_xpath))

    def click_cancel_button(self):
        self.click((By.XPATH, UM.cancel_button_xpath))

    def get_download_badge_button_text(self):
        return self.get_text((By.XPATH, UM.download_badge_button_xpath))

    def get_email_badge_button_text(self):
        return self.get_text((By.XPATH, UM.email_badge_button_xpath))

    def get_total_page_count(self):
        page_count = int("".join(list(filter(str.isdigit, self.get_text((By.XPATH, UM.total_page_count_xpath))))))
        return page_count

    def edit_user_link_is_displayed(self):
        return self.element_is_displayed((By.XPATH, UM.edit_user_link))

    def qr_code_is_displayed(self):
        return self.element_is_displayed((By.XPATH, UM.qr_code_xpath))

    def searched_user_is_displayed(self, name):
        self.wait_for_element_displayed((By.XPATH, f"(//*[contains(text(), '{name}')])[1]"))
        return self.get_text((By.XPATH, f"(//*[contains(text(), '{name}')])[1]"))

    def group_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, UM.group_filter_first_button_xpath))

    def role_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, UM.roles_filter_button_xpath))

    def login_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, UM.login_filter_button_xpath))

    def status_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, UM.status_filter_button_xpath))

    def search_name_or_id_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, UM.search_filter_textbox_xpath))

    def reset_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, UM.reset_button_xpath))

    def import_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, UM.import_button_xpath))

    def add_users_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, UM.add_user_button_xpath))

    def pagination_is_displayed(self):
        return self.element_is_displayed((By.XPATH, UM.paginator_xpath))

    def download_csv_is_displayed(self):
        return self.element_is_displayed((By.XPATH, UM.download_csv_xpath))

    def click_first_user_checkbox(self):
        self.click((By.XPATH, UM.first_user_xpath))

    def click_more_options(self):
        self.click((By.XPATH, UM.more_options_xpath))

    def request_user_consent_is_displayed(self):
        return self.element_is_displayed((By.XPATH, UM.request_user_consent_xpath))

    def click_request_user_consent(self):
        self.click((By.XPATH, UM.request_user_consent_xpath))

    def get_request_user_consent_title(self):
        return self.get_text((By.XPATH, UM.request_user_consent_title_xpath))

    def check_facial_id_checkbox(self):
        self.click((By.XPATH, UM.facial_id_checkbox_xpath))

    def select_communication_mode_email(self):
        self.click((By.XPATH, UM.communication_mode_email_xpath))

    def click_next_button(self):
        self.click((By.XPATH, UM.next_button_xpath))

    def get_confirm_request_title(self):
        return self.get_text((By.XPATH, UM.confirm_request_title_xpath))

    def click_send_request_button(self):
        self.click((By.XPATH, UM.send_request_button_xpath))

    def get_success_message(self):
        self.wait_for_element_displayed((By.XPATH, UM.success_message_xpath))
        return self.get_text((By.XPATH, UM.success_message_xpath))

    def click_user_tab(self):
        self.click((By.XPATH, UM.users_tab_xpath))

    def click_change_view_history(self):
        self.click((By.XPATH, UM.change_view_history_xpath))

    def get_user_affected_label(self):
        return self.get_text((By.XPATH, UM.user_affected_label_xpath))

    def get_action_label(self):
        return self.get_text((By.XPATH, UM.action_label_xpath))

    def get_action_details_label(self):
        return self.get_text((By.XPATH, UM.action_details_label_xpath))

    def get_editor_label(self):
        return self.get_text((By.XPATH, UM.editor_label_xpath))

    def get_action_date_label(self):
        return self.get_text((By.XPATH, UM.action_date_label_xpath))

    def user_audit_log_header_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, UM.user_audit_log_tab_header_xpath))

    def search_user_affected_filter_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, UM.search_user_affected_textbox_xpath))

    def action_type_dropdown_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, UM.action_type_dropdown_xpath))

    def date_filter_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, UM.date_range_dropdown_xpath))

    def reset_button_audit_page_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, UM.reset_button_audit_page_xpath))

    def download_log_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, UM.download_log_button_xpath))

    def search_user_affected(self, user):
        self.type((By.XPATH, UM.search_user_affected_textbox_xpath), user)

    def get_no_audit_logs_message(self):
        self.wait_for_element_displayed((By.XPATH, UM.no_audit_logs_message_xpath))
        return self.get_text((By.XPATH, UM.no_audit_logs_message_xpath))

    def get_first_user_affected_text(self):
        self.wait_for_element_displayed((By.XPATH, UM.first_user_affected_text_xpath))
        return self.get_text((By.XPATH, UM.first_user_affected_text_xpath))

    def click_reset_in_audit_page(self):
        self.click((By.XPATH, UM.reset_button_audit_page_xpath))

    def click_action_type_dropdown(self):
        self.click((By.XPATH, UM.action_type_dropdown_xpath))

    def select_action_type(self):
        self.click((By.XPATH, UM.select_action_type_xpath))

    def get_action_type_text(self):
        return self.get_text((By.XPATH, UM.action_type_text_xpath))

    def get_expected_action_type_text(self, expected_action):
        actual_text = self.get_text((By.XPATH, UM.action_type_added_text_xpath))
        if actual_text != expected_action:
            self.click_reset_in_audit_page()
            self.click_action_type_dropdown()
            self.select_action_type()
        return self.get_text((By.XPATH, UM.action_type_added_text_xpath))

    def select_imported(self):
        self.click((By.XPATH, UM.select_imported_xpath))

    def click_date_range_dropdown(self):
        self.click((By.XPATH, UM.date_range_dropdown_xpath))

    def select_date_range_today(self):
        self.click((By.XPATH, UM.select_date_range_today_xpath))
        self.click((By.XPATH, UM.apply_button_xpath))

    def get_action_date(self):
        return self.get_text((By.XPATH, UM.action_date_xpath))

    def click_close_user_audit_log(self):
        self.click((By.XPATH, UM.close_user_audit_log_xpath))

    def user_audit_log_tab_displayed(self):
        self.wait_till_element_disappear((By.XPATH, UM.user_audit_log_tab_xpath))
        return self.element_is_displayed((By.XPATH, UM.user_audit_log_tab_xpath))

    def click_download_log(self):
        self.click((By.XPATH, UM.download_log_button_xpath))

    def get_audit_log_file_name(self):
        date_now = datetime.now().strftime("%b-%d-%Y")
        file_name = 'audit-log-user-' + date_now + '.csv'
        return file_name

    def download_log_disabled(self):
        return self.element_is_displayed((By.XPATH, UM.download_log_button_disabled_xpath))

    def get_users_groups_label(self, index):
        xpath = UM.group_row_text_xpath.format(row=index)

        if index == 1:
            self.wait_for_element_displayed((By.XPATH, xpath))

        return self.get_text((By.XPATH, xpath))

    def clear_employee_id(self):
        self.clear((By.XPATH, UM.employee_id_textbox_xpath))

    def click_first_page_button(self):
        self.click((By.XPATH, UM.first_page_button_xpath))

    def click_last_page_button(self):
        self.click((By.XPATH, UM.last_page_button_xpath))

    def click_previous_page_button(self):
        self.click((By.XPATH, UM.previous_page_enabled_xpath))

    def click_next_page_button(self):
        self.click((By.XPATH, UM.next_page_enabled_xpath))

    def previous_page_button_is_disabled(self):
        return self.element_is_displayed((By.XPATH, UM.previous_page_disabled_xpath))

    def next_page_button_is_disabled(self):
        return self.element_is_displayed((By.XPATH, UM.next_page_disabled_xpath))

    def get_current_page_number(self):
        return int(self.get_text((By.XPATH, UM.selected_page_xpath)))