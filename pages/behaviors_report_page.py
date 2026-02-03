from selenium.webdriver.common.by import By

from locators.locators_behaviors_report_page import LocatorsBehaviorsReportPage as BR
from pages.base_page import BasePage


class BehaviorsReportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_behavior_text(self):
        return self.get_text((By.XPATH, BR.behavior_tab_xpath))

    def get_frequency_text(self):
        return self.get_text((By.XPATH, BR.frequency_tab_xpath))

    def get_trend_text(self):
        return self.get_text((By.XPATH, BR.trend_tab_xpath))

    # Filter Group
    def click_filter_group_behave(self):
        self.click((By.XPATH, BR.filter_by_group_behave_button_xpath))

    def search_filter_group_behave(self, search_filter_behave):
        self.type((By.XPATH, BR.search_by_group_behave_textbox_xpath), search_filter_behave)

    def select_search_filter_group_behave(self):
        self.click((By.XPATH, BR.select_search_behave_button_xpath))

    def click_done_behave(self):
        self.click((By.XPATH, BR.done_behave_button_xpath))

    # Filter Date
    def click_filter_date_behave(self):
        self.click((By.XPATH, BR.date_filter_behave_button_xpath))

    def click_from_date_behave(self):
        self.click((By.XPATH, BR.from_date_behave_textbox_xpath))

    def click_end_date_behave(self):
        self.click((By.XPATH, BR.end_date_behave_textbox_xpath))

    def click_apply_behave(self):
        self.click((By.XPATH, BR.apply_behave_button_xpath))

    def get_num_behave(self):
        return self.get_text((By.XPATH, BR.num_of_behave_textbox_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, BR.reset_button_xpath))

    def click_first_frequency_value(self):
        self.wait_for_element_displayed((By.XPATH, BR.first_frequency_value_xpath))
        self.click((By.XPATH, BR.first_frequency_value_xpath))

    def get_driver_report_text(self):
        return self.get_text((By.XPATH, BR.driver_report_title_text_xpath))

    def get_num_of_behaviors_text(self):
        self.wait_till_element_disappear((By.XPATH, BR.total_count_load_xpath))
        return self.element_is_displayed((By.XPATH, BR.count_of_behavior))
