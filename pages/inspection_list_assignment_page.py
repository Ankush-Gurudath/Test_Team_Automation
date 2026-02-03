from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from locators.locators_inspection_list_assignment_page import LocatorsInspectionListAssignmentPage as IL
from pages.base_page import BasePage


class InspectionListAssignmentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Labels
    def get_inspection_list_assignment_title(self):
        return self.get_text((By.XPATH, IL.inspection_list_assignment_title_xpath))

    def get_vehicle_count_title(self):
        return self.get_text((By.XPATH, IL.vehicle_count_title_xpath))

    def get_vehicle_table_title(self):
        return self.get_text((By.XPATH, IL.vehicle_table_title_xpath))

    def get_group_table_title(self):
        return self.get_text((By.XPATH, IL.group_table_title_xpath))

    def get_vehicle_type_table_title(self):
        return self.get_text((By.XPATH, IL.vehicle_type_title_xpath))

    def get_inspection_list_table_title(self):
        return self.get_text((By.XPATH, IL.inspection_list_title_xpath))

    def click_groups_filter(self):
        self.click((By.XPATH, IL.groups_filter_button_xpath))

    def search_groups_filter(self, searched_group):
        self.type((By.XPATH, IL.search_group_filter_textbox_xpath), searched_group)

    def select_first_groups_filter(self):
        self.click((By.XPATH, IL.select_searched_group_filter_xpath))

    def deselect_sub_groups_filter(self):
        self.click((By.XPATH, IL.deselect_sub_group_button_xpath))

    def click_done_groups_filter(self):
        self.click((By.XPATH, IL.group_filter_done_button_xpath))

    def click_vehicle_type_filter(self):
        self.click((By.XPATH, IL.vehicle_type_filter_button_xpath))

    def select_vehicle_type_filter(self):
        self.click((By.XPATH, IL.select_vehicle_type_filter_xpath))

    def click_inspection_list_filter(self):
        self.click((By.XPATH, IL.inspection_list_filter_button_xpath))

    def select_inspection_list_filter(self):
        self.click((By.XPATH, IL.select_inspection_list_filter_xpath))

    def get_selected_inspection_list(self):
        return self.get_text((By.XPATH, IL.first_row_inspection_list_name_xpath))

    def search_vehicle_name_filter(self, searched_name):
        self.type((By.XPATH, IL.search_vehicle_name_textbox_xpath), searched_name)

    def click_inspection_list_search_button(self):
        self.click((By.XPATH, IL.search_vehicle_icon_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, IL.reset_button_xpath))

    def click_trailer_assignment_tab(self):
        self.click((By.XPATH, IL.trailer_assignment_link_xpath))

    def get_inspection_list_trailers_count(self):
        return self.get_text((By.XPATH, IL.trailers_count_text_xpath))

    def get_inspection_list_trailer_column(self):
        return self.get_text((By.XPATH, IL.trailer_column_title_xpath))

    def get_inspection_list_group_title(self):
        return self.get_text((By.XPATH, IL.trailer_group_title_xpath))

    def get_inspection_list_trailer_type_title(self):
        return self.get_text((By.XPATH, IL.trailer_type_title_xpath))

    def get_inspection_list_column_title(self):
        return self.get_text((By.XPATH, IL.trailer_inspection_list_title_xpath))

    def click_trailer_group_filter(self):
        self.click((By.XPATH, IL.group_filter_trailer_button_xpath))

    def search_trailer_group_name_filter(self, searched_name):
        self.type((By.XPATH, IL.search_group_filter_textbox_xpath), searched_name)

    def select_trailer_group_filter(self):
        self.click((By.XPATH, IL.select_searched_group_filter_trailer_xpath))

    def click_done_trailer_group_filter(self):
        self.click((By.XPATH, IL.done_group_filter_trailer_button_xpath))

    def click_trailer_assignment_type_filter(self):
        self.click((By.XPATH, IL.trailer_assignment_type_filter_button_xpath))

    def select_trailer_assignment_type_filter(self):
        self.click((By.XPATH, IL.select_trailer_assignment_type_filter_button))

    def get_selected_trailer_assignment_type(self):
        return self.get_text((By.XPATH, IL.selected_trailer_type_text_xpath))

    def click_trailer_inspection_list_filter(self):
        self.click((By.XPATH, IL.inspection_list_filter_trailer_button_xpath))

    def select_trailer_inspection_list_filter(self):
        self.click((By.XPATH, IL.select_inspection_list_filter_trailer_xpath))

    def close_trailer_inspection_list_filter(self):
        self.click((By.XPATH, IL.close_inspection_list_filter_trailer_xpath))

    def get_selected_trailer_inspection_list_text(self):
        self.wait_for_element_displayed((By.XPATH, IL.selected_inspection_list_trailer_xpath))
        return self.get_text((By.XPATH, IL.selected_inspection_list_trailer_xpath))

    def search_trailer_name_filter(self, searched_name):
        self.type((By.XPATH, IL.search_trailer_name_textbox_xpath), searched_name)

    def click_search_trailer_button(self):
        self.click((By.XPATH, IL.search_trailer_icon_xpath))

    def click_reset_trailer_button(self):
        self.click((By.XPATH, IL.reset_button_trailer_xpath))

    def click_first_trailer_inspection_list(self):
        self.wait_for_element_displayed((By.XPATH, IL.select_first_trailer_list_button_xpath))
        self.click((By.XPATH, IL.select_first_trailer_list_button_xpath))

    def click_second_trailer_inspection_list(self):
        self.click((By.XPATH, IL.select_second_trailer_list_button_xpath))

    def click_set_inspection_list_button(self):
        self.click((By.XPATH, IL.set_trailer_inspection_list_button_xpath))

    def select_default_inspection_list_popup(self):
        self.click((By.XPATH, IL.select_default_set_inspection_list_button))

    def click_set_inspection_list_popup_button(self):
        self.click((By.XPATH, IL.set_inspection_popup_button_xpath))

    def click_trailer_reset_button(self):
        self.click((By.XPATH, IL.reset_button_trailer_xpath))

    def get_trailer_first_inspection_list(self):
        self.wait_for_element_displayed((By.XPATH, IL.first_inspection_list_trailer_text_xpath))
        return self.get_text((By.XPATH, IL.first_inspection_list_trailer_text_xpath))

    def get_trailer_second_inspection_list(self):
        self.wait_for_element_displayed((By.XPATH, IL.second_inspection_list_trailer_text_xpath))
        return self.get_text((By.XPATH, IL.second_inspection_list_trailer_text_xpath))

    def get_first_trailer_group_name(self):
        return self.get_text((By.XPATH, IL.first_trailer_group_text_xpath))

    def get_first_trailer_type_name(self):
        return self.get_text((By.XPATH, IL.first_trailer_type_text_xpath))

    def get_first_trailer_inspection_list(self):
        self.wait_for_element_displayed((By.XPATH, IL.first_inspection_list_trailer_text_xpath))
        return self.get_text((By.XPATH, IL.first_inspection_list_trailer_text_xpath))

    def get_first_trailer_name_int(self):
        return self.get_text((By.XPATH, IL.first_trailer_name_text_int_xpath))

    def get_first_trailer_name_stg(self):
        return self.get_text((By.XPATH, IL.first_trailer_name_text_stg_xpath))

    def click_first_vehicle_inspection_list(self):
        self.wait_for_element_is_clickable((By.XPATH, IL.first_vehicle_checkbox_xpath))
        self.click((By.XPATH, IL.first_vehicle_checkbox_xpath))

    def click_second_vehicle_inspection_list(self):
        self.click((By.XPATH, IL.second_vehicle_checkbox_xpath))

    def click_set_inspection_vehicle_list_button(self):
        self.click((By.XPATH, IL.set_inspection_list_button_xpath))

    def click_inspection_default_checkbox(self):
        self.click((By.XPATH, IL.set_inspection_default_checkbox_xpath))

    def click_set_popup_button(self):
        self.click((By.XPATH, IL.set_button_popup_xpath))

    def get_first_vehicle_inspection_list(self):
        self.wait_for_element_displayed((By.XPATH, IL.first_vehicle_inspection_list_xpath))
        return self.get_text((By.XPATH, IL.first_vehicle_inspection_list_xpath))

    def get_second_vehicle_inspection_list(self):
        self.wait_for_element_displayed((By.XPATH, IL.second_vehicle_inspection_list_xpath))
        return self.get_text((By.XPATH, IL.second_vehicle_inspection_list_xpath))

    def click_vehicle_assignment_tab(self):
        self.click((By.XPATH, IL.vehicle_assignment_link_xpath))

    def click_vehicle_set_popup(self):
        self.click((By.XPATH, IL.vehicle_set_inspection_button_xpath))

    def get_first_vehicle_group_text(self):
        return self.get_text((By.XPATH, IL.first_row_vehicle_group_text_xpath))

    def get_first_row_vehicle_type_text(self):
        return self.get_text((By.XPATH, IL.first_row_vehicle_type_text_xpath))

    def get_first_row_vehicle_name_text(self):
        return self.get_text((By.XPATH, IL.first_row_vehicle_name_text_xpath))

    def get_first_row_inspection_list_text(self):
        self.wait_for_element_displayed((By.XPATH, IL.first_row_inspection_list_text_xpath))
        return self.get_text((By.XPATH, IL.first_row_inspection_list_text_xpath))
