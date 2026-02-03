from time import sleep

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By

from locators.locators_device_health_page import LocatorsDeviceHealth as DH
from pages.base_page import BasePage


class DeviceHealthPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_device_column_label(self):
        return self.get_text((By.XPATH, DH.device_label_xpath))

    def get_device_type_column_label(self):
        return self.get_text((By.XPATH, DH.device_type_label_xpath))

    def get_overdue_for_check_in_column_label(self):
        return self.get_text((By.XPATH, DH.overdue_for_check_in_label_xpath))

    def get_power_disconnects_column_label(self):
        return self.get_text((By.XPATH, DH.power_disconnects_label_xpath))

    def get_ignition_not_detected_column_label(self):
        return self.get_text((By.XPATH, DH.ignition_not_detected_label_xpath))

    def get_open_rma_column_label(self):
        return self.get_text((By.XPATH, DH.open_rma_label_xpath))

    def get_all_device_issues_summary_label(self):
        return self.get_text((By.XPATH, DH.all_device_issues_label_summary_xpath))

    def get_overdue_for_check_in_summary_label(self):
        return self.get_text((By.XPATH, DH.overdue_for_check_in_summary_label_xpath))

    def get_power_disconnects_summary_label(self):
        return self.get_text((By.XPATH, DH.power_disconnects_summary_label_xpath))

    def get_ignition_not_detected_summary_label(self):
        return self.get_text((By.XPATH, DH.ignition_not_detected_summary_label_xpath))

    def get_open_rma_summary_label(self):
        return self.get_text((By.XPATH, DH.open_rma_summary_label_xpath))

    def get_all_device_issues_graph_label(self):
        return self.get_text((By.XPATH, DH.all_device_issues_graph_label_xpath))

    def click_group_filter_button(self):
        self.click((By.XPATH, DH.group_filter_button_xpath))

    def search_group_filter(self, group_name):
        self.type((By.XPATH, DH.search_group_filter_textbox_xpath), group_name)

    def select_searched_group_filter_button(self):
        self.click((By.XPATH, DH.select_group_filter_button_xpath))

    def click_done_group_filter_button(self):
        self.click((By.XPATH, DH.done_group_filter_button_xpath))

    def click_select_issue_filter_button(self):
        self.wait_for_element_displayed((By.XPATH, DH.all_device_issues_graph_label_xpath))
        self.click((By.XPATH, DH.select_issue_filter_button_xpath))

    def select_overdue_filter_button(self):
        self.click((By.XPATH, DH.select_overdue_issue_button_xpath))

    def select_power_disconnect_filter_button(self):
        self.click((By.XPATH, DH.select_power_disconnects_button_xpath))

    def click_select_search_filter_button(self):
        self.click((By.XPATH, DH.select_search_filter_button_xpath))

    def select_device_search_filter_button(self):
        self.click((By.XPATH, DH.select_search_device_button_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, DH.reset_button_xpath))

    def select_vehicle_search_filter_button(self):
        self.click((By.XPATH, DH.select_search_vehicle_button_xpath))

    def search_criteria_filter(self, search_DV):
        self.type((By.XPATH, DH.search_criteria_textbox_xpath), search_DV)

    def get_first_row_device_text(self):
        return self.get_text((By.XPATH, DH.first_device_text_xpath))

    def get_first_row_vehicle_text(self):
        return self.get_text((By.XPATH, DH.first_vehicle_text_xpath))

    def get_first_row_overdue_text(self):
        return self.get_text((By.XPATH, DH.first_row_overdue_text_xpath))

    def get_first_row_power_disconnect_text(self):
        return self.get_text((By.XPATH, DH.first_row_power_disconnects_text_xpath))

    def get_power_disconnects_graph_text(self):
        return self.get_text((By.XPATH, DH.power_disconnects_graph_xpath))

    def get_overdue_for_check_in_graph_text(self):
        return self.get_text((By.XPATH, DH.overdue_for_check_in_graph_xpath))

    def get_device_count(self, attempts=5):
        i = 0
        while i < attempts:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, DH.device_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, DH.device_count_xpath))

    # table column when set the issue filter as power disconnect
    def get_device_column_text(self):
        return self.get_text((By.XPATH, DH.device_column_text_xpath))

    def get_device_type_column_text(self):
        return self.get_text((By.XPATH, DH.device_type_column_text_xpath))

    def get_vehicle_column_text(self):
        return self.get_text((By.XPATH, DH.vehicle_column_text_xpath))

    def get_group_column_text(self):
        return self.get_text((By.XPATH, DH.group_column_text_xpath))

    def get_disconnect_time_column_text(self):
        return self.get_text((By.XPATH, DH.disconnect_time_column_text_xpath))

    def get_reconnect_time_column_text(self):
        return self.get_text((By.XPATH, DH.reconnect_time_column_text_xpath))

    def get_duration_column_text(self):
        return self.get_text((By.XPATH, DH.duration_column_text_xpath))
