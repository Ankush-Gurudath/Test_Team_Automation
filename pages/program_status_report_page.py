from selenium.webdriver.common.by import By

from locators.locators_program_status_report_page import LocatorsProgramStatusReportPage as PR
from pages.base_page import BasePage


class ProgramStatusReportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_num_of_subgroups_text(self):
        self.wait_till_element_disappear((By.XPATH, PR.total_count_load_xpath))
        return self.element_is_displayed((By.XPATH, PR.num_of_subgroups_text_xpath))

    def get_group_text(self):
        return self.get_text((By.XPATH, PR.group_text_xpath))

    def get_num_of_devices_text(self):
        return self.get_text((By.XPATH, PR.num_of_devices_text_xpath))

    def get_unassigned_drivers_text(self):
        return self.get_text((By.XPATH, PR.unassigned_drivers_text_xpath))

    def get_overdue_for_checkin_text(self):
        return self.get_text((By.XPATH, PR.overdue_for_check_in_text_xpath))

    def get_overdue_for_coaching_text(self):
        return self.get_text((By.XPATH, PR.overdue_for_coaching_text_xpath))

    def get_coaching_effectiveness_text(self):
        return self.get_text((By.XPATH, PR.coaching_effectiveness_text_xpath))

    def get_program_effectiveness_text(self):
        return self.get_text((By.XPATH, PR.program_effectiveness_text_xpath))

    def get_program_status_report_page_text(self):
        return self.get_text((By.XPATH, PR.program_status_report_page_text_xpath))

    def get_assigned_driver_page_text(self):
        return self.get_text((By.XPATH, PR.assign_driver_page_text_xpath))

    # Filters
    def click_filter_by_group(self):
        self.click((By.XPATH, PR.filter_by_group_program_status_button_xpath))

    def search_filter_by_group(self, group_name):
        self.type((By.XPATH, PR.search_by_group_program_status_textbox_xpath), group_name)

    def select_filter_by_group(self):
        self.click((By.XPATH, PR.select_search_by_group_program_status_button_xpath))

    def click_done_button(self):
        self.click((By.XPATH, PR.done_filter_program_status_button_xpath))

    def click_reset(self):
        self.wait_for_element_displayed((By.XPATH, PR.reset_program_status_button_xpath))
        self.click((By.XPATH, PR.reset_program_status_button_xpath))

    def click_group_link(self):
        self.wait_for_element_displayed((By.XPATH, PR.group_link_text_xpath))
        self.click((By.XPATH, PR.group_link_text_xpath))

    def click_unassigned_driver_link(self):
        self.wait_for_element_displayed((By.XPATH, PR.unassigned_driver_link_text_xpath))
        self.click((By.XPATH, PR.unassigned_driver_link_text_xpath))

    def click_overdue_for_coaching_link(self):
        self.wait_for_element_displayed((By.XPATH, PR.overdue_for_coaching_link_text_xpath))
        self.click((By.XPATH, PR.overdue_for_coaching_link_text_xpath))

    def click_coaching_effectiveness_link(self):
        self.wait_for_element_displayed((By.XPATH, PR.coaching_effectiveness_link_text_xpath))
        self.click((By.XPATH, PR.coaching_effectiveness_link_text_xpath))

    def get_due_for_coaching_page_text(self):
        return self.get_text((By.XPATH, PR.due_for_coaching_text_xpath))

    def get_coaches_report_page_text(self):
        return self.get_text((By.XPATH, PR.coaches_report_text_xpath))

    def back_to_previous_page(self):
        self.back()

    def get_first_group_name(self):
        return self.get_text((By.XPATH, PR.first_group_name_text_xpath))
