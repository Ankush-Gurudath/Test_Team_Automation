from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By

from locators.locators_trailer_management_page import LocatorsTrailerManagement as TM
from pages.base_page import BasePage


class TrailerManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_trailer_tab(self):
        self.click((By.XPATH, TM.trailer_tab_xpath))

    def get_trailer_management_text(self):
        return self.get_text((By.XPATH, TM.trailer_management_text_xpath))

    def get_trailer_column_text(self):
        return self.get_text((By.XPATH, TM.trailer_column_text_xpath))

    def get_group_column_text(self):
        return self.get_text((By.XPATH, TM.group_column_text_xpath))

    def get_license_plate_column_text(self):
        return self.get_text((By.XPATH, TM.license_plate_column_text_xpath))

    def get_vin_column_text(self):
        return self.get_text((By.XPATH, TM.vin_column_text_xpath))

    def get_inspection_list_column_text(self):
        return self.get_text((By.XPATH, TM.inspection_list_column_text_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, TM.reset_button_xpath))

    def click_group_filter(self):
        self.click((By.XPATH, TM.group_filter_xpath))

    def search_group(self, group_name):
        self.type((By.XPATH, TM.search_group_textbox_xpath), group_name)

    def select_searched_group(self):
        self.click((By.XPATH, TM.select_searched_group_xpath))

    def click_done_button(self):
        self.click((By.XPATH, TM.search_group_done_button_xpath))

    def type_trailer_name(self, trailer_name):
        self.type((By.XPATH, TM.search_trailer_textbox_xpath), trailer_name)

    def click_add_trailer_button(self):
        self.click((By.XPATH, TM.add_trailer_button_xpath))

    def search_trailer_name(self, trailer_name):
        self.type((By.XPATH, TM.search_trailer_textbox_xpath), trailer_name)

    def get_searched_trailer_name(self, trailer_name):
        self.wait_for_expected_text((By.XPATH, TM.searched_trailer_name_text_xpath), trailer_name)
        return self.get_text((By.XPATH, TM.searched_trailer_name_text_xpath))

    def click_added_trailer_name(self):
        self.click((By.XPATH, TM.searched_trailer_name_text_xpath))

    def select_first_trailer(self):
        self.wait_for_element_displayed((By.XPATH, TM.select_first_trailer_checkbox_xpath))
        self.click((By.XPATH, TM.select_first_trailer_checkbox_xpath))

    def select_second_trailer(self):
        self.click((By.XPATH, TM.select_second_trailer_checkbox_xpath))

    def click_set_inspection_list_button(self):
        self.click((By.XPATH, TM.set_inspection_list_button_xpath))

    def select_first_inspection_list_dialog(self):
        self.wait_for_element_is_clickable((By.XPATH, TM.select_first_set_inspection_list_dialog_xpath))
        self.click((By.XPATH, TM.select_first_set_inspection_list_dialog_xpath))

    def select_second_inspection_list_dialog(self):
        self.click((By.XPATH, TM.select_second_set_inspection_list_dialog_xpath))

    def click_set_inspection_list_dialog(self):
        self.wait_for_element_is_clickable((By.XPATH, TM.set_inspection_list_dialog_button_xpath))
        self.click((By.XPATH, TM.set_inspection_list_dialog_button_xpath))

    def get_first_inspection_list_text(self, expected_list):
        self.wait_for_expected_text((By.XPATH, TM.first_inspection_list_status_text_xpath), expected_list)
        return self.get_text((By.XPATH, TM.first_inspection_list_status_text_xpath))

    def get_second_inspection_list_text(self):
        self.wait_for_element_displayed((By.XPATH, TM.second_inspection_list_status_text_xpath))
        return self.get_text((By.XPATH, TM.second_inspection_list_status_text_xpath))

    def get_first_trailer_group(self, group_text):
        return self.wait_for_expected_text((By.XPATH, TM.first_trailer_group_xpath), group_text)

    def group_filter_option_is_present(self):
        return self.element_is_displayed((By.XPATH, TM.group_filter_xpath))

    def search_trailer_option_is_present(self):
        return self.element_is_displayed((By.XPATH, TM.search_trailer_textbox_xpath))

    def trailer_count_is_present(self):
        return self.element_is_displayed((By.XPATH, TM.trailer_count_xpath))

    def add_trailer_button_is_present(self):
        return self.element_is_displayed((By.XPATH, TM.add_trailer_button_xpath))

    def click_delete_trailer_button(self):
        self.wait_for_element_displayed((By.ID, TM.delete_trailer_button_id))
        self.click((By.ID, TM.delete_trailer_button_id))

    def click_continue_to_delete_trailer_button(self):
        self.wait_for_element_displayed((By.ID, TM.confirm_delete_trailer_continue_button_id))
        self.click((By.ID, TM.confirm_delete_trailer_continue_button_id))

    def trailer_deleted_message_is_displayed(self):
        self.wait_for_element_displayed((By.XPATH, TM.trailer_deleted_popup_xpath))
        return self.element_is_displayed((By.XPATH, TM.trailer_deleted_popup_xpath))

    def no_trailers_found_message_is_displayed(self):
        self.wait_for_element_displayed((By.XPATH, TM.no_trailers_found_text_xpath))
        return self.element_is_displayed((By.XPATH, TM.no_trailers_found_text_xpath))