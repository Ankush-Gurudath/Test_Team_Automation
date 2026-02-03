from selenium.webdriver.common.by import By

from locators.locators_driver_id_page import LocatorsDriverId as DI
from pages.base_page import BasePage


class DriverIdPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_driver_assignment_tab(self):
        self.click((By.XPATH, DI.driver_assignment_tab_xpath))

    def click_group_filter_button(self):
        self.click((By.XPATH, DI.filter_group_button_xpath))

    def search_group_filter(self, groupname):
        self.type((By.XPATH, DI.search_filter_group_textbox_xpath), groupname)

    def select_search_group_filter_button(self):
        self.click((By.XPATH, DI.select_search_filter_group_button_xpath))

    def click_done_group_filter_button(self):
        self.click((By.XPATH, DI.done_filter_group_button_xpath))

    def click_date_filter_button(self):
        self.click((By.XPATH, DI.date_filter_button_xpath))

    def select_first_date_filter_button(self):
        self.click((By.XPATH, DI.first_date_filter_button_xpath))

    def select_second_date_filter_button(self):
        self.click((By.XPATH, DI.second_date_filter_button_xpath))

    def click_date_filter_done_button(self):
        self.click((By.XPATH, DI.done_filter_date_button_xpath))

    def click_search_filter_button(self):
        self.click((By.XPATH, DI.search_filter_button_xpath))

    def click_search_driver_filter_button(self):
        self.click((By.XPATH, DI.search_driver_filter_button_xpath))

    def click_search_vehicle_filter_button(self):
        self.click((By.XPATH, DI.search_vehicle_filter_button_xpath))

    def search_criteria_filter(self, searchDV):
        self.type((By.XPATH, DI.search_criteria_filter_textbox_xpath), searchDV)

    def click_searched_name_button_xpath(self):
        self.click((By.XPATH, DI.select_searched_name_button_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, DI.reset_button_xpath))

    def get_first_vehicle_name_text(self):
        return self.get_text((By.XPATH, DI.vehicle_name_first_row_xpath))

    def get_first_group_name_text(self):
        return self.get_text((By.XPATH, DI.group_name_first_row_xpath))

    def get_first_driver_name_text(self):
        return self.get_text((By.XPATH, DI.driver_name_first_row_xpath))
