from selenium.webdriver.common.by import By

from locators.locators_inspection_list_management import LocatorsInspectionListManagementPage as IL
from pages.base_page import BasePage


class InspectionListManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Labels
    def get_vehicle_inspection_list_title(self):
        return self.get_text((By.XPATH, IL.vehicle_inspection_list_title_xpath))

    def get_first_vehicle_inspection_lists(self):
        self.wait_for_element_displayed((By.XPATH, IL.first_vehicle_list_name_xpath))
        return self.get_text((By.XPATH, IL.first_vehicle_list_name_xpath))

    def get_default_title(self):
        return self.get_text((By.XPATH, IL.default_title_xpath))

    # Actions
    def click_duplicate_icon(self):
        self.click((By.XPATH, IL.duplicate_icon_xpath))

    def vehicle_duplicate_icon_displayed(self):
        return self.element_is_displayed((By.XPATH, IL.duplicate_icon_xpath))

    def click_edit_button(self):
        self.click((By.XPATH, IL.edit_list_button_icon_xpath))

    def clear_list_name(self):
        self.clear((By.XPATH, IL.list_name_textbox_xpath))

    def edit_list_name(self, random_name):
        self.type((By.XPATH, IL.list_name_textbox_xpath), random_name)

    def click_save_changes_button(self):
        self.click((By.XPATH, IL.save_changes_button_xpath))

    def get_all_vehicle_inspection_lists(self):
        self.wait_for_element_displayed((By.XPATH, IL.default_inspection_list_xpath))
        return self.get_text((By.XPATH, IL.all_vehicle_inspection_lists_xpath))

    def click_new_list_button(self):
        self.click((By.XPATH, IL.new_list_button_xpath))

    def type_new_list_name(self, list_name):
        self.type((By.XPATH, IL.new_list_name_textbox_xpath), list_name)

    def type_new_section_item(self, section_name):
        self.type((By.XPATH, IL.section_items_textbox_xpath), section_name)

    def type_list_inspection_points(self, points_name):
        self.type((By.XPATH, IL.list_inspection_points_textbox_xpath), points_name)

    def click_create_new_list_button(self):
        self.click((By.XPATH, IL.create_list_button_xpath))

    def click_list_delete_icon(self):
        self.click((By.XPATH, IL.delete_list_icon_xpath))

    def click_inspection_list_delete_button(self):
        self.click((By.XPATH, IL.delete_inspection_list_button_xpath))

    def click_trailer_list_link(self):
        self.wait_for_element_displayed((By.XPATH, IL.trailer_list_link_xpath))
        self.click((By.XPATH, IL.trailer_list_link_xpath))

    def get_trailer_inspection_lists_title(self):
        self.wait_for_expected_text((By.XPATH, IL.trailer_inspection_lists_title_xpath), "Trailer Inspection Lists")
        return self.get_text((By.XPATH, IL.trailer_inspection_lists_title_xpath))

    def get_default_inspection_lists_title(self):
        return self.get_text((By.XPATH, IL.trailer_default_title_xpath))

    def trailer_duplicate_icon_displayed(self):
        return self.element_is_displayed((By.XPATH, IL.trailer_duplicate_icon_xpath))

    def click_trailer_edit_list_button(self):
        self.click((By.XPATH, IL.trailer_edit_list_icon_xpath))

    def clear_trailer_list_name(self):
        self.clear((By.XPATH, IL.trailer_edit_list_name_textbox_xpath))

    def type_new_trailer_list_name(self, bname):
        self.type((By.XPATH, IL.trailer_edit_list_name_textbox_xpath), bname)

    def clear_trailer_inspection_item(self):
        self.clear((By.XPATH, IL.trailer_inspection_items_section_textbox_xpath))

    def type_new_trailer_inspection_item(self, item_name):
        self.type((By.XPATH, IL.trailer_inspection_items_section_textbox_xpath), item_name)

    def clear_trailer_inspection_points(self):
        self.clear((By.XPATH, IL.trailer_inspection_points_textbox_xpath))

    def type_new_trailer_inspection_points(self, point_name):
        self.type((By.XPATH, IL.trailer_inspection_points_textbox_xpath), point_name)

    def click_trailer_save_changes_edit_button(self):
        self.click((By.XPATH, IL.trailer_save_changes_button_xpath))

    def get_first_trailer_list_name(self):
        return self.get_text((By.XPATH, IL.first_trailer_list_name_xpath))

    def click_trailer_new_list_button(self):
        self.click((By.XPATH, IL.new_list_button_xpath))

    def click_trailer_create_new_list_button(self):
        self.click((By.XPATH, IL.trailer_create_new_button_xpath))

    def click_trailer_delete_list_button(self):
        self.click((By.XPATH, IL.trailer_list_delete_button_xpath))

    def click_trailer_delete_list_popup_button(self):
        self.click((By.XPATH, IL.trailer_delete_list_popup_button_xpath))

    def get_all_trailer_inspection_lists(self):
        self.wait_for_element_displayed((By.XPATH, IL.default_inspection_list_xpath))
        return self.get_text((By.XPATH, IL.all_trailer_inspection_list_xpath))

    def get_first_trailer_inspection_list(self):
        self.wait_for_element_displayed((By.XPATH, IL.first_trailer_inspection_list_xpath))
        return self.get_text((By.XPATH, IL.first_trailer_inspection_list_xpath))

    def get_first_trailer_name_list(self):
        return self.get_text((By.XPATH, IL.first_trailer_list_name_xpath))

    def click_trailer_list_duplicate_button(self):
        self.click((By.XPATH, IL.trailer_duplicate_icon_xpath))

    def get_trailer_duplicate_list_name(self):
        return self.get_text((By.XPATH, IL.trailer_list_second_row_xpath))

    def click_vehicle_list_link(self):
        self.click((By.XPATH, IL.vehicle_list_link))

    def get_trailer_new_inspection_list_title(self):
        return self.get_text((By.XPATH, IL.new_inspection_list_title_xpath))

    def list_management_highlighted(self):
        return self.element_is_displayed((By.XPATH, IL.list_management_highlighted_xpath))