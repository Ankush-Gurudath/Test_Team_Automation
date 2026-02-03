from datetime import datetime
from time import sleep

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By

from locators.locators_device_management import LocatorsDeviceManagement as DM
from pages.base_page import BasePage
from utils.common_util import LocatorUtil


class DeviceManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_device_tab(self):
        self.click((By.XPATH, DM.device_tab_xpath))

    def device_management_title_is_displayed(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                if self.element_is_displayed((By.XPATH, DM.device_management_title_xpath)):
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)
        return self.element_is_displayed((By.XPATH, DM.device_management_title_xpath))

    def get_device_management_title(self):
        if self.element_is_displayed((By.XPATH, DM.error_loading_devices_xpath)) is True:
            self.click_refresh_button()
        return self.get_text((By.XPATH, DM.device_management_title_xpath))

    def get_device_column_title(self):
        return self.get_text((By.XPATH, DM.device_table_text_xpath))

    def get_device_type_column_title(self):
        return self.get_text((By.XPATH, DM.device_type_table_text_xpath))

    def get_first_row_device_type(self, device_type):
        self.wait_for_element_displayed((By.XPATH, LocatorUtil.give_locator(DM.first_row_device_type_xpath, device_type)))
        return self.get_text((By.XPATH, LocatorUtil.give_locator(DM.first_row_device_type_xpath, device_type)))

    def get_asset_column_title(self):
        return self.get_text((By.XPATH, DM.asset_table_text_xpath))

    def get_group_column_title(self):
        return self.get_text((By.XPATH, DM.group_table_text_xpath))

    def get_status_column_title(self):
        return self.get_text((By.XPATH, DM.status_table_text_xpath))

    def get_last_connected_column_title(self):
        return self.get_text((By.XPATH, DM.last_connected_table_text_xpath))

    def get_initial_connection_column_title(self):
        return self.get_text((By.XPATH, DM.initial_connection_table_text_xpath))

    def click_group_filter(self):
        self.click((By.XPATH, DM.group_filter_xpath))

    def search_group_filter(self, group_name1):
        self.type((By.XPATH, DM.search_group_filter_textbox_xpath), group_name1)

    def select_searched_group(self):
        self.click((By.XPATH, DM.select_searched_group_filter_button_xpath))

    def click_done_group_filter(self):
        self.click((By.XPATH, DM.done_group_filter_button_xpath))

    def click_clear_group_filter(self):
        self.click((By.XPATH, DM.clear_group_filter_xpath))

    def click_device_type(self, device_type):
        while self.element_is_displayed((By.XPATH, LocatorUtil.give_locator(DM.select_device_type_button_xpath, device_type))) is False:
            self.click((By.XPATH, DM.device_type_button_xpath))

    def select_device_type(self, device_type):
        self.click((By.XPATH, LocatorUtil.give_locator(DM.select_device_type_button_xpath, device_type)))

    def click_status_filter(self):
        self.click((By.XPATH, DM.status_filter_button_xpath))

    def select_status_filter(self):
        self.click((By.XPATH, DM.select_status_button_xpath))

    def search_device_filter(self, device_name):
        self.type((By.XPATH, DM.search_device_filter_textbox_xpath), device_name)

    def click_reset_button(self):
        self.wait_for_element_displayed((By.XPATH, DM.reset_button_xpath))
        self.click((By.XPATH, DM.reset_button_xpath))
        self.driver.refresh()

    def get_first_device_name(self, device_name):
        self.wait_for_expected_text((By.XPATH, DM.first_row_device_name_xpath), device_name)
        return self.get_text((By.XPATH, DM.first_row_device_name_xpath))

    def get_first_device_text(self):
        self.wait_for_element_displayed((By.XPATH, DM.first_row_device_name_xpath))
        return self.get_text((By.XPATH, DM.first_row_device_name_xpath))

    def get_first_vehicle_name(self):
        self.wait_for_element_displayed((By.XPATH, DM.first_row_vehicle_name_xpath))
        return self.get_text((By.XPATH, DM.first_row_vehicle_name_xpath))

    def get_first_group_name(self, group_name):
        self.wait_for_expected_text((By.XPATH, DM.first_row_group_name_xpath), group_name)
        return self.get_text((By.XPATH, DM.first_row_group_name_xpath))

    def get_first_row_group_name(self):
        self.wait_for_element_displayed((By.XPATH, DM.first_row_group_name_xpath))
        return self.get_text((By.XPATH, DM.first_row_group_name_xpath))

    def get_first_status_name(self, device_status):
        self.wait_for_expected_text((By.XPATH, DM.first_row_status_name_xpath), device_status)
        return self.get_text((By.XPATH, DM.first_row_status_name_xpath))

    def select_first_device(self):
        self.wait_for_element_displayed((By.XPATH, DM.first_row_device_checkbox_xpath))
        self.click((By.XPATH, DM.first_row_device_checkbox_xpath))

    def click_move_group(self):
        self.click((By.XPATH, DM.move_group_tab_xpath))

    def search_group_move(self, group_name):
        self.type((By.XPATH, DM.search_group_move_textbox_xpath), group_name)

    def select_searched_move_group(self):
        self.click((By.XPATH, DM.select_group_move_button_xpath))

    def click_done_move_group(self):
        self.click((By.XPATH, DM.done_group_move_button_xpath))

    def click_continue_move_group(self):
        if self.element_is_displayed((By.XPATH, DM.continue_move_group_button_xpath)) is True:
            self.click((By.XPATH, DM.continue_move_group_button_xpath))
            self.wait_for_element_displayed((By.XPATH, DM.move_group_success_message))

    def click_change_status(self):
        self.click((By.XPATH, DM.change_status_button_xpath))

    def click_status_spare(self):
        self.click((By.XPATH, DM.spare_checkbox_xpath))

    def click_save_change_status(self):
        self.click((By.XPATH, DM.save_change_status_button_xpath))

    def get_device_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, DM.device_count_xpath))
                if count.isdigit():
                    sleep(1)
                else:
                    self.click_refresh_button()
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, DM.device_count_xpath))

    def device_count_is_displayed(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                if self.element_is_displayed((By.XPATH, DM.device_count_xpath)):
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.element_is_displayed((By.XPATH, DM.device_count_xpath))

    def click_first_device_name(self):
        self.wait_for_element_displayed((By.XPATH, DM.first_row_device_name_xpath))
        self.click((By.XPATH, DM.first_row_device_name_xpath))

    def click_device_title(self):
        self.click((By.XPATH, DM.device_table_text_xpath))

    def click_select_search_filter(self):
        self.click((By.XPATH, DM.select_search_filter_xpath))

    def select_device_filter(self):
        self.click((By.XPATH, DM.select_device_filter_xpath))

    def open_or_close_status_filter(self):
        self.click((By.XPATH, DM.remove_status_filter))

    def get_devices_count(self):
        return self.get_text((By.XPATH, DM.devices_count_xpath))

    def get_devices_groups_label(self, index):
        xpath = DM.group_row_text_xpath.format(row=index)

        if index == 1:
            self.wait_for_element_displayed((By.XPATH, xpath))

        return self.get_text((By.XPATH, xpath))


    def click_view_change_history(self):
        self.click((By.XPATH, DM.view_change_history_xpath))

    def get_device_affected_column_title(self):
        return self.get_text((By.XPATH, DM.device_affected_table_text_xpath))

    def get_action_column_title(self):
        return self.get_text((By.XPATH, DM.action_table_text_xpath))

    def get_action_details_column_title(self):
        return self.get_text((By.XPATH, DM.action_details_table_text_xpath))

    def get_editor_column_title(self):
        return self.get_text((By.XPATH, DM.editor_table_text_xpath))

    def get_action_date_column_title(self):
        return self.get_text((By.XPATH, DM.action_date_table_text_xpath))

    def get_device_audit_log_title(self):
        return self.get_text((By.XPATH, DM.device_audit_log_title_xpath))

    def search_device_affected_is_displayed(self):
        return self.element_is_displayed((By.XPATH, DM.search_device_affected_textbox_xpath))

    def select_actions_is_displayed(self):
        return self.element_is_displayed((By.XPATH, DM.select_actions_filter_xpath))

    def download_log_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, DM.download_log_button_xpath))

    def date_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, DM.date_filter_xpath))

    def get_first_device_affected_text(self):
        return self.get_text((By.XPATH, DM.first_device_affected_text_xpath))

    def search_device_affected(self, device_name):
        self.type((By.XPATH, DM.search_device_affected_textbox_xpath), device_name)

    def get_no_audit_logs_message(self):
        self.wait_for_element_displayed((By.XPATH, DM.no_audit_logs_message_xpath))
        return self.get_text((By.XPATH, DM.no_audit_logs_message_xpath))

    def click_reset_in_audit_page(self):
        self.click((By.XPATH, DM.reset_button_audit_page_xpath))

    def click_date_range_dropdown(self):
        self.click((By.XPATH, DM.date_filter_xpath))

    def select_date_range_today(self):
        self.click((By.XPATH, DM.select_date_range_today_xpath))

    def get_action_date(self):
        self.wait_for_element_displayed((By.XPATH, DM.action_date_table_text_xpath))
        return self.get_text((By.XPATH, DM.action_date_table_text_xpath))

    def click_close_device_audit_log(self):
        self.click((By.XPATH, DM.close_view_change_history_xpath))

    def view_change_history_popup_displayed(self):
        self.wait_till_element_disappear((By.XPATH, DM.view_change_history_popup_xpath))
        return self.element_is_displayed((By.XPATH, DM.view_change_history_popup_xpath))

    def click_select_actions_filter(self):
        self.click((By.XPATH, DM.select_actions_filter_xpath))

    def select_action_type_added(self):
        self.click((By.XPATH, DM.select_added_xpath))

    def get_first_action_type_text(self):
        self.wait_for_page_load()
        self.wait_for_element_displayed((By.XPATH, DM.action_type_text_xpath))
        return self.get_text((By.XPATH, DM.action_type_text_xpath))

    def select_action_type_edited(self):
        self.click((By.XPATH, DM.select_edited_xpath))

    def select_deleted_action_type(self):
        self.click((By.XPATH, DM.select_deleted_xpath))

    def select_imported_action_type(self):
        self.click((By.XPATH, DM.select_imported_xpath))

    def click_download_log_button(self):
        self.click((By.XPATH, DM.download_log_button_xpath))

    def get_audit_log_file_name(self):
        date_now = datetime.now().strftime("%b-%d-%Y")
        file_name = 'audit-log-device-' + date_now + '.csv'
        return file_name

    def download_log_button_disabled_displayed(self):
        return self.element_is_displayed((By.XPATH, DM.download_log_button_disabled_xpath))

    def get_first_action_details_text(self):
        self.wait_for_element_displayed((By.XPATH, DM.first_action_details_text_xpath))
        return self.get_text((By.XPATH, DM.first_action_details_text_xpath))
