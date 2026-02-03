from selenium.webdriver.common.by import By

from locators.locators_device_profile_page import LocatorsDeviceProfile as DP
from pages.base_page import BasePage


class DeviceProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_device_serial_number(self):
        self.click((By.XPATH, DP.device_serial_number_xpath))

    def get_device_profile_title(self):
        return self.get_text((By.XPATH, DP.admin_device_profile_title_xpath))

    def get_device_profile_summary_device(self):
        return self.get_text((By.XPATH, DP.device_profile_device_header_xpath))

    def get_device_profile_summary_device_type(self):
        return self.get_text((By.XPATH, DP.device_profile_device_type_header_xpath))

    def get_device_profile_summary_group(self):
        return self.get_text((By.XPATH, DP.device_profile_group_header_xpath))

    def get_device_profile_summary_status(self):
        return self.get_text((By.XPATH, DP.device_profile_status_header_xpath))

    def get_device_profile_summary_health(self):
        return self.get_text((By.XPATH, DP.device_profile_health_header_xpath))

    def get_device_profile_summary_last_communicated(self):
        return self.get_text((By.XPATH, DP.device_profile_last_communicated_header_xpath))

    def get_device_profile_summary_last_movement(self):
        return self.get_text((By.XPATH, DP.device_profile_last_movement_header_xpath))

    def get_device_profile_summary_initial_connection(self):
        return self.get_text((By.XPATH, DP.device_profile_initial_connection_header_xpath))

    def get_device_profile_summary_last_communicated_date(self):
        return self.get_text((By.XPATH, DP.device_profile_last_communicated_date))

    def click_request_new_image(self):
        self.wait_for_element_enabled((By.XPATH, DP.click_request_new_image_disabled_xpath))
        self.click((By.XPATH, DP.request_new_image_xpath))

    def request_new_image_error(self):
        self.get_text((By.XPATH, DP.request_new_image_error))

    def get_new_time_for_updated_image(self):
        return self.get_text((By.XPATH, DP.get_new_time_for_updated_image_xpath))

    def wait_for_load_new_image(self):
        i = 0
        while i < 4:
            element = self.wait_till_element_disappear((By.XPATH, DP.request_image_spinner_xpath))
            i = i + 1
            if element is True:
                break
