from selenium.webdriver.common.by import By
from locators.locators_add_vehicle_page import LocatorsAddVehicle as AV
from pages.base_page import BasePage


class AddVehiclePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_group_add_vehicle_button(self):
        self.click((By.XPATH, AV.add_group_button_xpath))

    def search_group_add_vehicle(self, vehicle_group):
        self.type((By.XPATH, AV.search_group_textbox_xpath), vehicle_group)

    def select_group_add_vehicle(self):
        self.click((By.XPATH, AV.select_search_group_button_xpath))

    def click_done_group_add_vehicle(self):
        self.click((By.XPATH, AV.done_group_button_xpath))

    def add_vehicle_name(self, random_name):
        self.type((By.XPATH, AV.vehicle_name_textbox_xpath), random_name)

    def click_create_vehicle(self):
        for _ in range(3):
            self.scroll_page_down()
        self.wait_for_element_is_clickable((By.XPATH, AV.create_vehicle_button_xpath))
        self.click((By.XPATH, AV.create_vehicle_button_xpath))
        while self.continue_button_displayed():
            self.click_continue_alert()
            self.wait_for_page_to_fully_load()
        self.wait_for_element_displayed((By.XPATH, AV.create_vehicle_success_message_xpath))
        self.wait_for_page_to_fully_load()

    def click_continue_alert(self):
        if self.element_is_displayed((By.XPATH, AV.continue_alert_xpath)) is True:
            self.click((By.XPATH, AV.continue_alert_xpath))

    def continue_button_displayed(self):
        displayed = self.element_is_displayed((By.XPATH, AV.continue_alert_xpath))
        if displayed is True:
            return displayed
        return None

    def add_vehicle_page_displayed(self):
        return self.element_is_displayed((By.XPATH, AV.add_vehicle_page_title_xpath))

    def add_group_button_displayed(self):
        return self.element_is_displayed((By.XPATH, AV.add_group_button_xpath))
