from time import sleep

from selenium.common import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from locators.locators_edit_vehicle_page import LocatorsEditVehiclePage as EV
from pages.base_page import BasePage


class EditVehiclePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clear_vehicle_name(self):
        self.clear((By.XPATH, EV.vehicle_name_textbox_xpath))

    def edit_vehicle_name(self, vehicle_name):
        self.type((By.XPATH, EV.vehicle_name_textbox_xpath), vehicle_name)

    def click_edit_vehicle_save_button(self):
        self.wait_for_element_is_clickable((By.XPATH, EV.save_edit_vehicle_button_xpath))
        self.click((By.XPATH, EV.save_edit_vehicle_button_xpath))
        self.wait_till_element_disappear((By.XPATH, EV.update_vehicle_success_message_xpath))

    def click_delete_button_in_edit_vehicle_page(self):
        self.click((By.XPATH, EV.delete_button_in_edit_vehicle_page))
        self.wait_for_page_to_fully_load()

    def click_continue_button_pop_up(self):
        self.click((By.XPATH, EV.delete_vehicle_continue_button))
        self.wait_for_page_to_fully_load()
        max_attempts = 2
        attempts = 0
        while attempts < max_attempts:
            try:
                if self.element_is_displayed((By.XPATH, EV.delete_vehicle_continue_button)):
                    self.click((By.XPATH, EV.delete_vehicle_continue_button))
                    self.wait_for_page_to_fully_load()
                    attempts += 1
                else:
                    break
            except (TimeoutException, StaleElementReferenceException, NoSuchElementException):
                break

    def continue_button_displayed(self):
        displayed = self.element_is_displayed((By.XPATH, EV.continue_alert_xpath))
        if displayed is True:
            return displayed
        return None

    def click_continue_alert(self):
        if self.element_is_displayed((By.XPATH, EV.continue_alert_xpath)) is True:
            self.click((By.XPATH, EV.continue_alert_xpath))

    def get_dvir_access_status_text(self):
        return self.get_text((By.XPATH, EV.dvir_access_status_xpath))

    # associate device with the vehicle
    def input_device(self, device_name):
        n = 0
        while n < 5:
            n += 1
            try:
                if self.element_is_displayed((By.XPATH, EV.assign_device_textbox_xpath)):
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(2)
        self.clear((By.XPATH, EV.assign_device_textbox_xpath))
        self.type((By.XPATH, EV.assign_device_textbox_xpath), device_name)
        self.find((By.XPATH, EV.assign_device_textbox_xpath)).send_keys(Keys.BACK_SPACE)
        self.wait_for_page_to_fully_load()

    def get_device_name(self):
        n = 0
        while n < 5:
            n += 1
            try:
                if self.element_is_displayed((By.XPATH, EV.assign_device_textbox_xpath)):
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(2)

        return self.get_text((By.XPATH, EV.assign_device_textbox_xpath))

    def assign_device(self, device_name):
        if self.element_is_displayed((By.XPATH, EV.search_magnifier_xpath)):
            self.type((By.XPATH, EV.assign_device_textbox_xpath), device_name)
        else:
            self.click((By.XPATH, EV.search_cancel_xpath))
            self.type((By.XPATH, EV.assign_device_textbox_xpath), device_name)

    def select_searched_device(self):
        self.click((By.XPATH, EV.select_searched_device_xpath))

    def continual_button_is_displayed(self):
        return self.element_is_displayed((By.ID, EV.continual_button_id))

    def click_continual_button(self):
        self.click((By.ID, EV.continual_button_id))

    def click_status_filter(self):
        self.click((By.XPATH, EV.status_filter_xpath))

    def select_in_service_status_filter(self):
        self.click((By.XPATH, EV.status_filter_in_service_xpath))
