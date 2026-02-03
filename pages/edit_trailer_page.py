from selenium.webdriver.common.by import By

from locators.locators_edit_trailer_page import LocatorsEditTrailer as ET
from pages.base_page import BasePage


class EditTrailerPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def clear_trailer_name(self):
        self.clear((By.XPATH, ET.trailer_name_textbox_xpath))

    def edit_first_name_trailer(self, edit_trailer):
        self.type((By.XPATH, ET.trailer_name_textbox_xpath), edit_trailer)

    def click_save_trailer(self):
        self.wait_for_element_is_clickable((By.XPATH, ET.save_button_xpath))
        self.click((By.XPATH, ET.save_button_xpath))
        self.wait_for_element_displayed((By.XPATH, ET.update_trailer_success_message_xpath))
