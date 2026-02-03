from datetime import datetime
from time import sleep
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By
from locators.locators_vehicle_management_page import LocatorsVehicleManagement as VM
from pages.base_page import BasePage


class VehicleManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def vehicle_management_title_is_displayed(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                if self.element_is_displayed((By.XPATH, VM.vehicle_management_title_xpath)):
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)
        return self.element_is_displayed((By.XPATH, VM.vehicle_management_title_xpath))

    def vehicle_count_is_displayed(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                if self.element_is_displayed((By.XPATH, VM.vehicle_count_xpath)):
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)
        return self.element_is_displayed((By.XPATH, VM.vehicle_count_xpath))

    def click_group_filter(self):
        self.click((By.XPATH, VM.group_filter_button_xpath))

    def search_group_filter(self, group_name):
        self.type((By.XPATH, VM.search_group_textbox_xpath), group_name)

    def select_group_filter(self):
        self.click((By.XPATH, VM.select_group_filter_button_xpath))

    def click_done_button(self):
        self.click((By.XPATH, VM.done_filter_group_button_xpath))

    def click_last_connected_filter(self):
        self.click((By.XPATH, VM.last_connected_filter_button_xpath))

    def select_first_date_filter(self):
        self.click((By.XPATH, VM.first_date_filter_button_xpath))

    def select_second_date_filter(self):
        self.click((By.XPATH, VM.second_date_filter_button_xpath))

    def click_apply_date_filter(self):
        self.click((By.XPATH, VM.apply_filter_date_button_xpath))

    def click_status_filter(self):
        self.click((By.XPATH, VM.status_filter_button_xpath))

    def select_status_filter(self):
        self.click((By.XPATH, VM.select_status_button_xpath))
        self.wait_for_page_to_fully_load()

    def click_select_search_filter(self):
        try:
            self.element_is_displayed((By.XPATH, VM.select_search_filter_button_xpath))
        except StaleElementReferenceException:
            sleep(2)
        self.click((By.XPATH, VM.select_search_filter_button_xpath))

    def click_vehicle_select_search_filter(self):
        self.click((By.XPATH, VM.vehicle_select_search_button_xpath))

    def click_device_select_search_filter(self):
        self.click((By.XPATH, VM.device_select_search_button_xpath))

    def click_driver_select_search_filter(self):
        self.click((By.XPATH, VM.driver_select_search_button_xpath))

    def search_name_filter(self, search_name):
        self.clear((By.XPATH, VM.search_vehicle_name_textbox_xpath))
        self.type((By.XPATH, VM.search_vehicle_name_textbox_xpath), search_name)
        self.wait_for_page_to_fully_load()

    def click_reset_button(self):
        self.element_is_displayed((By.XPATH, VM.reset_button_xpath))
        self.click((By.XPATH, VM.reset_button_xpath))

    def click_expected_vehicle_name(self, vehicle_name):
        self.scroll_page_up()
        self.wait_for_expected_text((By.XPATH, f'.//*[normalize-space(.)="{vehicle_name}"]'), vehicle_name)
        self.click((By.XPATH, f'.//*[normalize-space(.)="{vehicle_name}"]'))

    def get_first_row_vehicle_name(self, vehicle_name):
        self.wait_for_expected_text((By.XPATH, VM.first_row_vehicle_name_xpath), vehicle_name)
        return self.get_text((By.XPATH, VM.first_row_vehicle_name_xpath))

    def get_first_vehicle_name(self):
        return self.get_text((By.XPATH, VM.first_row_vehicle_name_xpath))

    def get_first_vehicle_name_new_ui(self):
        return self.get_text((By.XPATH, VM.first_vehicle_xpath))

    def get_test_vehicle_name(self):
        return self.get_text((By.XPATH, VM.test_vehicle_name_xpath))

    def get_expected_vehicle_name(self, vehicle_name):
        self.wait_for_expected_text((By.XPATH, f'(.//*[normalize-space(.)="{vehicle_name}"])[1]'), vehicle_name)
        return self.get_text((By.XPATH, f'(.//*[normalize-space(.)="{vehicle_name}"])[1]'))

    def get_expected_vehicle_name_new_ui(self, vehicle_name):
        vehicle_locator = (By.XPATH, f"(//*[normalize-space()='{vehicle_name}'])[1]")
        reset_locator = (By.XPATH, VM.reset_button_xpath)
        max_retries = 3
        for attempt in range(max_retries):
            try:
                if self.wait_for_expected_text(vehicle_locator, vehicle_name):
                    return self.get_text(vehicle_locator)
            except TimeoutException:
                pass
            if attempt < max_retries - 1:
                self.click(reset_locator)
                self.click_select_search_filter()
                self.click_vehicle_select_search_filter()
                self.search_name_filter(vehicle_name)
                self.wait_for_page_to_fully_load()
                self.click(vehicle_locator)
        raise AssertionError(f"Expected vehicle '{vehicle_name}' did not appear after retries")

    def click_first_vehicle_name_new_ui(self, expected_vehicle):
        vehicle_locator = (By.XPATH, VM.first_vehicle_xpath)
        reset_locator = (By.XPATH, VM.reset_button_xpath)
        self.wait_for_page_to_fully_load()
        max_retries = 3
        for attempt in range(max_retries):
            try:
                if self.wait_for_expected_text(vehicle_locator, expected_vehicle):
                    self.click(vehicle_locator)
                    break

                else:
                    self.wait_for_element_is_clickable(reset_locator)
                    self.click(reset_locator)
                    self.element_is_displayed(reset_locator)
                    self.click(reset_locator)
                    self.click_select_search_filter()
                    self.click_vehicle_select_search_filter()
                    self.search_name_filter(expected_vehicle)
                    self.wait_for_page_to_fully_load()
                    self.click(vehicle_locator)

            except (StaleElementReferenceException, ElementClickInterceptedException, TimeoutException):
                if attempt == max_retries - 1:
                    raise
                self.wait_for_page_to_fully_load()
        self.wait_for_page_to_fully_load()

    def get_first_row_group_name(self):
        return self.get_text((By.XPATH, VM.first_row_group_name_xpath))

    def get_first_row_group_name_new_ui(self, expected_group, expected_vehicle):
        group_locator = (By.XPATH, VM.first_row_group_name_xpath)
        reset_locator = (By.XPATH, VM.reset_button_xpath)
        max_retries = 3
        for attempt in range(max_retries):
            try:
                if self.wait_for_expected_text(group_locator, expected_group):
                    return self.get_text(group_locator)
            except TimeoutException:
                pass

            if attempt < max_retries - 1:
                self.element_is_displayed(reset_locator)
                self.click(reset_locator)
                self.click_select_search_filter()
                self.click_vehicle_select_search_filter()
                self.search_name_filter(expected_vehicle)
                self.wait_for_page_to_fully_load()

        raise AssertionError(
            f"Expected group '{expected_group}' did not appear in first row after retries"
        )

    def get_first_row_expected_status_name_new_ui(self, expected_status, expected_vehicle):
        status_locator = (By.XPATH, VM.first_row_status_name_xpath)
        reset_locator = (By.XPATH, VM.reset_button_xpath)
        max_retries = 3
        for attempt in range(max_retries):
            try:
                if self.wait_for_expected_text(status_locator, expected_status):
                    return self.get_text(status_locator)
            except TimeoutException:
                pass

            if attempt < max_retries - 1:
                self.element_is_displayed(reset_locator)
                self.click(reset_locator)
                self.click_select_search_filter()
                self.click_vehicle_select_search_filter()
                self.search_name_filter(expected_vehicle)
                self.wait_for_page_to_fully_load()

        raise AssertionError(
            f"Expected status '{expected_status}' did not appear in first row after retries"
        )

    def get_first_row_driver_name(self):
        return self.get_text((By.XPATH, VM.first_row_driver_name_xpath))

    def get_first_row_device_name(self):
        return self.get_text((By.XPATH, VM.first_row_device_name_xpath))

    def get_first_row_last_connected_name(self):
        return self.get_text((By.XPATH, VM.first_row_last_connected_name_xpath))

    def get_first_row_status_name(self):
        return self.get_text((By.XPATH, VM.first_row_status_name_xpath))

    def get_first_row_expected_status_name(self, status):
        self.wait_for_expected_text((By.XPATH, VM.first_row_status_name_xpath), status)
        return self.get_text((By.XPATH, VM.first_row_status_name_xpath))

    def click_add_vehicle_button(self):
        self.element_is_displayed((By.XPATH, VM.add_vehicle_button_xpath))
        n = 0
        while n < 10:
            n += 1
            try:
                self.click((By.XPATH, VM.add_vehicle_button_xpath))
                break
            except (StaleElementReferenceException, ElementClickInterceptedException):
                sleep(5)
        if n == 5:
            self.click((By.XPATH, VM.add_vehicle_button_xpath))

    def click_first_vehicle_checkbox(self, retries=5, wait_between=2):
        self.wait_for_element_displayed((By.XPATH, VM.select_first_vehicle_checkbox_xpath))
        for attempt in range(1, retries + 1):
            try:
                self.click((By.XPATH, VM.select_first_vehicle_checkbox_xpath))
                return True  # success → no more tries
            except (StaleElementReferenceException, ElementClickInterceptedException):
                sleep(wait_between)
        return False

    def click_move_group_continue(self):
        self.click((By.XPATH, VM.move_group_continue_button_xpath))
        self.wait_for_page_to_fully_load()

    def click_delete_vehicle_button(self):
        self.click((By.XPATH, VM.delete_vehicle_button_xpath))

    def click_confirm_delete_vehicle_button(self):
        self.wait_for_element_displayed((By.XPATH, VM.confirm_delete_vehicle_button_xpath))
        self.click((By.XPATH, VM.confirm_delete_vehicle_button_xpath))

    def click_first_vehicle_name(self):
        self.wait_for_page_to_fully_load()
        self.wait_for_element_displayed((By.XPATH, VM.first_vehicle_selected_xpath))
        sleep(3)
        n = 0
        while n < 10:
            n += 1
            try:
                self.click((By.XPATH, VM.first_vehicle_selected_xpath))
                break
            except (StaleElementReferenceException, ElementClickInterceptedException):
                sleep(5)
        if n == 5:
            self.click((By.XPATH, VM.first_vehicle_selected_xpath))
        self.wait_for_page_to_fully_load()

    def click_detach_device_button(self, retries=5):
        self.wait_for_page_to_fully_load()
        detach_button = (By.XPATH, VM.detach_device_button_xpath)
        self.wait_for_element_displayed(detach_button)
        for attempt in range(1, retries + 1):
            try:
                self.click(detach_button)
                self.element_is_displayed((By.XPATH, VM.apply_detach_device_button_xpath))
                return True
            except (ElementClickInterceptedException, StaleElementReferenceException, TimeoutException):
                self.click_first_vehicle_checkbox()
                self.click(detach_button)
                sleep(1)
        return False

    def click_second_vehicle_button(self):
        self.click((By.XPATH, VM.select_second_vehicle_checkbox_xpath))

    def click_more_option_button(self):
        self.click((By.XPATH, VM.more_option_button_xpath))

    def click_first_checkbox_detach_and_apply(self, timeout=10, retries=3):
        for attempt in range(retries):
            try:
                self.element_is_displayed((By.XPATH, VM.checkbox_xpath))
                self.click((By.XPATH, VM.checkbox_xpath))
                self.wait_for_element_is_clickable((By.XPATH, VM.detach_button_xpath))
                self.click((By.XPATH, VM.detach_button_xpath))
                self.element_is_displayed((By.XPATH, VM.apply_button_xpath))
                self.click((By.XPATH, VM.apply_button_xpath))
                return True
            except (StaleElementReferenceException, TimeoutException, ElementClickInterceptedException):
                if attempt < retries - 1:
                    continue
                else:
                    raise
        return None

    def click_apply_detach_device_button(self):
        self.wait_for_element_is_clickable((By.XPATH, VM.apply_detach_device_button_xpath))
        self.click((By.XPATH, VM.apply_detach_device_button_xpath))
        self.wait_for_element_displayed((By.XPATH, VM.vehicle_detached_from_device_success_message))

    def click_edit_vehicle_button(self):
        self.click((By.XPATH, VM.edit_vehicle_button_xpath))

    def click_filter_edit_vehicle_button(self):
        self.click((By.XPATH, VM.group_filter_edit_vehicle_button_xpath))

    def search_edit_bulk_group(self, group_name):
        self.type((By.XPATH, VM.bulk_edit_search_group_textbox_xpath), group_name)

    def click_edit_bulk_select_group_button(self):
        self.click((By.XPATH, VM.bulk_edit_select_group_button_xpath))

    def click_edit_bulk_group_done_button(self):
        self.click((By.XPATH, VM.bulk_edit_group_done_button_xpath))

    def click_status_drop_down(self):
        self.click((By.XPATH, VM.bulk_edit_open_status_drop_down_button_xpath))

    def click_edit_select_status_button(self):
        self.click((By.XPATH, VM.bulk_edit_select_status_xpath))

    def click_edit_bulk_apply_button(self):
        self.click((By.XPATH, VM.bulk_edit_vehicle_apply_button))
        self.wait_for_page_to_fully_load()

    def click_edit_bulk_dvir_access_drop_down_button(self):
        self.click((By.XPATH, VM.bulk_edit_dvir_access_drop_down_xpath))

    def click_close_search_icon(self):
        self.click((By.XPATH, VM.close_search_icon_xpath))

    def select_enable_status(self):
        self.click((By.XPATH, VM.bulk_edit_select_enable_status_xpath))

    def get_vehicle_page_title_text(self):
        self.wait_for_element_displayed((By.XPATH, VM.vehicle_page_title_xpath))
        return self.get_text((By.XPATH, VM.vehicle_page_title_xpath))

    def get_vehicle_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, VM.vehicle_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, VM.vehicle_count_xpath))

    def get_vehicle_column_text(self):
        return self.get_text((By.XPATH, VM.vehicle_column_text_xpath))

    def get_group_column_text(self):
        return self.get_text((By.XPATH, VM.group_column_text_xpath))

    def get_driver_column_text(self):
        return self.get_text((By.XPATH, VM.driver_column_text_xpath))

    def get_device_column_text(self):
        return self.get_text((By.XPATH, VM.device_column_text_xpath))

    def get_last_connected_column_text(self):
        return self.get_text((By.XPATH, VM.last_connected_column_text_xpath))

    def get_status_column_text(self):
        return self.get_text((By.XPATH, VM.status_column_text_xpath))

    def select_all_checkbox(self):
        self.click((By.XPATH, VM.select_all_checkbox_xpath))

    def delete_vehicles(self):
        self.select_all_checkbox()
        self.click_delete_vehicle_button()
        self.click_confirm_delete_vehicle_button()
        self.wait_for_page_to_fully_load()

    def click_change_view_history(self):
        self.click((By.XPATH, VM.change_view_history_button_xpath))

    def get_vehicle_affected_column_text(self):
        return self.get_text((By.XPATH, VM.vehicle_affected_column_xpath))

    def get_action_column_text(self):
        return self.get_text((By.XPATH, VM.action_column_xpath))

    def get_action_details_column_text(self):
        return self.get_text((By.XPATH, VM.action_details_column_xpath))

    def get_editor_column_text(self):
        return self.get_text((By.XPATH, VM.editor_column_xpath))

    def get_action_date_column_text(self):
        return self.get_text((By.XPATH, VM.action_date_column_xpath))

    def search_vehicle_affected_filter_displayed(self):
        return self.element_is_displayed((By.XPATH, VM.search_vehicle_affected_filter_xpath))

    def date_range_filter_displayed(self):
        return self.element_is_displayed((By.XPATH, VM.date_range_dropdown_xpath))

    def select_actions_filter_displayed(self):
        return self.element_is_displayed((By.XPATH, VM.select_actions_filter_xpath))

    def download_log_button_displayed(self):
        return self.element_is_displayed((By.XPATH, VM.download_log_button_xpath))

    def get_first_vehicle_affected_text(self):
        return self.get_text((By.XPATH, VM.first_vehicle_affected_text_xpath))

    def search_vehicle_affected(self, vehicle_name):
        self.type((By.XPATH, VM.search_vehicle_affected_filter_xpath), vehicle_name)

    def get_no_audit_logs_message(self):
        self.wait_for_element_displayed((By.XPATH, VM.no_audit_logs_message_xpath))
        return self.get_text((By.XPATH, VM.no_audit_logs_message_xpath))

    def click_date_range_dropdown(self):
        self.click((By.XPATH, VM.date_range_dropdown_xpath))

    def select_date_range_today(self):
        self.click((By.XPATH, VM.select_date_range_today_xpath))

    def get_action_date_text(self):
        self.wait_for_element_displayed((By.XPATH, VM.action_date_xpath))
        return self.get_text((By.XPATH, VM.action_date_xpath))

    def click_close_view_change_history_popup(self):
        self.click((By.XPATH, VM.close_view_change_history_xpath))

    def view_change_history_popup_displayed(self):
        self.wait_till_element_disappear((By.XPATH, VM.view_change_history_popup_xpath))
        return self.element_is_displayed((By.XPATH, VM.view_change_history_popup_xpath))

    def click_reset_in_audit_page(self):
        self.click((By.XPATH, VM.reset_button_audit_page_xpath))

    def click_select_actions_filter(self):
        self.click((By.XPATH, VM.select_actions_filter_xpath))

    def select_action_type_added(self):
        self.click((By.XPATH, VM.select_action_type_xpath))

    def get_action_date(self):
        return self.get_text((By.XPATH, VM.action_date_xpath))

    def get_first_action_type_text(self):
        self.wait_for_page_load()
        self.wait_for_element_displayed((By.XPATH, VM.action_type_text_xpath))
        return self.get_text((By.XPATH, VM.action_type_text_xpath))

    def get_first_action_details_text(self):
        self.wait_for_element_displayed((By.XPATH, VM.first_action_details_text_xpath))
        return self.get_text((By.XPATH, VM.first_action_details_text_xpath))

    def select_edited_action_type(self):
        self.click((By.XPATH, VM.select_edited_xpath))

    def select_deleted_action_type(self):
        self.click((By.XPATH, VM.select_deleted_xpath))

    def select_imported_action_type(self):
        self.click((By.XPATH, VM.select_imported_xpath))

    def click_download_log_button(self):
        self.click((By.XPATH, VM.download_log_button_xpath))

    def get_audit_log_file_name(self):
        date_now = datetime.now().strftime("%b-%d-%Y")
        file_name = 'audit-log-vehicle-' + date_now + '.csv'
        return file_name

    def download_log_button_disabled_displayed(self):
        return self.element_is_displayed((By.XPATH, VM.download_log_button_disabled_xpath))

    def get_vehicles_count(self):
        return self.get_text((By.XPATH, VM.vehicles_count_xpath))

    def get_vehicles_groups_label(self, index):
        xpath = VM.group_row_text_xpath.format(row=index)
        if index == 1:
            self.wait_for_element_displayed((By.XPATH, xpath))

        return self.get_text((By.XPATH, xpath))
