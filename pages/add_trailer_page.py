from selenium.webdriver.common.by import By

from locators.locators_add_trailer_page import LocatorsAddTrailerPage as AT
from pages.base_page import BasePage


class AddTrailerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_group_trailer_filter(self):
        self.click((By.XPATH, AT.group_button_xpath))

    def search_group_trailer_filter(self, group_name):
        self.type((By.XPATH, AT.search_group_textbox_xpath), group_name)

    def select_searched_group(self):
        self.click((By.XPATH, AT.select_group_button_xpath))

    def click_done_trailer_group_button(self):
        self.click((By.XPATH, AT.done_group_button_xpath))

    def type_trailer_name(self, trailer_name):
        self.type((By.XPATH, AT.trailer_name_textbox_xpath), trailer_name)

    def type_vin_number(self, vin_num):
        self.type((By.XPATH, AT.vin_textbox_xpath), vin_num)

    def click_create_trailer(self):
        self.wait_for_element_is_clickable((By.XPATH, AT.create_trailer_button_xpath))
        self.click((By.XPATH, AT.create_trailer_button_xpath))
        self.wait_for_element_displayed((By.XPATH, AT.create_trailer_success_message_xpath))
