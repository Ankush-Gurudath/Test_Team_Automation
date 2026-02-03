from time import sleep

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By

from locators.locators_license_management import LocatorsLicenseManagement as LM
from pages.base_page import BasePage


class LicenseManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Actions
    def click_licensing(self):
        self.element_is_displayed((By.XPATH, LM.licensing_button_xpath))
        self.click((By.XPATH, LM.licensing_button_xpath))

    # Get Text
    def get_license_column_text(self):
        return self.get_text((By.ID, LM.license_column_id))

    def get_services_column_text(self):
        return self.get_text((By.XPATH, LM.services_column_xpath))

    def get_cost_center_column_text(self):
        return self.get_text((By.ID, LM.cost_center_column_id))

    def get_group_column_text(self):
        return self.get_text((By.ID, LM.group_column_id))

    def get_vehicle_column_text(self):
        return self.get_text((By.ID, LM.vehicle_column_id))

    def get_device_column_text(self):
        return self.get_text((By.ID, LM.device_column_id))

    def get_license_status_column_text(self):
        return self.get_text((By.ID, LM.license_status_column_id))

    def get_device_licenses_label_text(self):
        self.element_is_displayed((By.XPATH, LM.device_licenses_label_xpath))
        return self.get_text((By.XPATH, LM.device_licenses_label_xpath))

    def get_device_services_activation_label_text(self):
        self.element_is_displayed((By.XPATH, LM.device_services_activation_label_xpath))
        return self.get_text((By.XPATH, LM.device_services_activation_label_xpath))

    def get_devices_activated_label_text(self):
        return self.get_text((By.XPATH, LM.devices_activated_label_xpath))

    def get_licenses_assigned_label_xpath(self):
        return self.get_text((By.XPATH, LM.licenses_assigned_activated_label_xpath))

    def get_license_management_title_text(self):
        return self.get_text((By.XPATH, LM.license_management_title_xpath))

    # Filter
    def click_group_filter(self):
        self.click((By.XPATH, LM.group_filter_xpath))

    def search_group(self, group_name):
        self.type((By.XPATH, LM.search_group_xpath), group_name)

    def select_search_group(self):
        self.click((By.XPATH, LM.select_searched_group_xpath))

    def click_done_button(self):
        self.click((By.XPATH, LM.done_button_group_filter_xpath))

    def click_service_filter(self):
        self.click((By.XPATH, LM.service_filter_xpath))

    def select_driver_safety_service(self):
        self.click((By.XPATH, LM.select_driver_safety_service_xpath))

    def click_arrow_service_filter(self):
        self.click((By.XPATH, LM.arrow_icon_service_filter_xpath))

    def click_device_type_filter(self):
        self.click((By.XPATH, LM.select_device_type_filter_xpath))

    def select_device_type(self):
        self.click((By.XPATH, LM.select_DC2_device_type_xpath))

    def click_arrow_device_type(self):
        self.click((By.XPATH, LM.arrow_icon_device_type_filter_xpath))

    def click_license_status_filter(self):
        self.click((By.XPATH, LM.select_license_status_xpath))

    def select_assigned_license_status(self):
        self.click((By.XPATH, LM.select_assigned_status_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, LM.reset_button_xpath))

    def click_select_search_filter(self):
        self.click((By.XPATH, LM.select_search_filter_xpath))

    def select_device(self):
        self.click((By.XPATH, LM.select_device_xpath))

    def select_license(self):
        self.click((By.XPATH, LM.select_license_xpath))

    def select_vehicle(self):
        self.click((By.XPATH, LM.select_vehicle_xpath))

    def input_search_criteria(self, search_criteria):
        self.type((By.XPATH, LM.search_criteria_input_xpath), search_criteria)

    def get_license_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, LM.license_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, LM.license_count_xpath))
