from selenium.webdriver.common.by import By

from locators.locators_group_report_page import LocatorsGroupReportPage as GR
from pages.base_page import BasePage


class GroupReportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_num_of_subgroups_text(self):
        return self.get_text((By.XPATH, GR.subgroups_text_xpath))

    def get_group_text(self):
        return self.get_text((By.XPATH, GR.group_text_xpath))

    def get_num_of_vehicles_text(self):
        return self.get_text((By.XPATH, GR.num_of_vehicles_text_xpath))

    def get_coachable_score_text(self):
        return self.get_text((By.XPATH, GR.coachable_score_text_xpath))

    def get_coachable_events_text(self):
        return self.get_text((By.XPATH, GR.coachable_events_text_xpath))

    # Filters
    def click_filter_by_group(self):
        self.click((By.XPATH, GR.group_by_filter_tab_xpath))

    def search_filter_by_group(self, search_filter):
        self.type((By.XPATH, GR.search_group_by_filter_textbox_xpath), search_filter)

    def select_search_filter_by_group(self):
        self.click((By.XPATH, GR.select_search_group_by_filter_button_xpath))

    def click_done_filter_by_group(self):
        self.click((By.XPATH, GR.done_filter_button_xpath))

    # DateFilter
    def click_date_filter(self):
        self.click((By.XPATH, GR.date_filter_tab_xpath))

    def select_from_date_filter(self):
        self.click((By.XPATH, GR.from_date_filter_button_xpath))

    def select_end_date_filter(self):
        self.click((By.XPATH, GR.end_date_filter_button_xpath))

    def click_apply_filter(self):
        self.click((By.XPATH, GR.apply_filter_button_xpath))

    # BehaviorsReport
    def click_behaviors_filter(self):
        self.click((By.XPATH, GR.behavior_filter_button_xpath))

    def select_behaviors_filter(self):
        self.click((By.XPATH, GR.select_group_behavior_button_xpath))
        self.click((By.XPATH, GR.close_behavior_filter_xpath))

    # NormalizedFilter
    def click_normalized_filter(self):
        self.click((By.XPATH, GR.normalized_filter_button_xpath))

    def select_normalized_filter(self):
        self.click((By.XPATH, GR.select_normalized_filter_dropdown_xpath))

    # Links
    def click_on_group_link(self):
        self.click((By.XPATH, GR.group_link_textbox_xpath))

    def get_drivers_report_page_text(self):
        return self.get_text((By.XPATH, GR.drivers_report_page_link_textbox_xpath))

    def back_to_previous_page(self):
        self.back()

    def task_count_displayed(self):
        self.wait_for_element_displayed((By.XPATH, GR.subgroups_text_xpath))
        elements = self.find_elements((By.XPATH, GR.subgroups_text_xpath))
        return len(elements) > 0

    def click_reset_alert(self):
        self.click((By.XPATH, GR.reset_button_xpath))

    def get_first_group_name(self):
        return self.get_text((By.XPATH, GR.first_group_name_xpath))

    def get_coachable_events_count(self):
        coachable_events_count = self.get_text((By.XPATH, GR.group_coachable_events_count_xpath))
        return coachable_events_count

    def click_group_coachable_events_count(self):
        self.click((By.XPATH, GR.group_coachable_events_count_xpath))

    def get_events_count(self):
        events_count = self.get_text((By.XPATH, GR.events_count_in_events_page_xpath))
        return events_count
