from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.locators_safe_driving_report import LocatorsSafeDrivingReport as SDR


class SafeDrivingReportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def safe_driving_page_is_displayed(self):
        return self.element_is_displayed((By.XPATH, SDR.safe_driving_page_title_xpath))

    def get_driver_text(self):
        return self.get_text((By.XPATH, SDR.driver_text_xpath))

    def get_group_text(self):
        return self.get_text((By.XPATH, SDR.group_text_xpath))

    def get_distance_driven_text(self):
        return self.get_text((By.XPATH, SDR.distance_driven_text_xpath))

    def get_achievement_text(self):
        return self.get_text((By.XPATH, SDR.achievement_text_xpath))

    def get_non_coachable_behaviors_text(self):
        return self.get_text((By.XPATH, SDR.non_coachable_behaviors_text_xpath))

    def click_on_group_filter(self):
        self.click((By.XPATH, SDR.group_filter_xpath))

    def enter_group_name(self, group_name):
        self.type((By.XPATH, SDR.input_group_name_xpath), group_name)

    def click_select_group(self):
        self.click((By.XPATH, SDR.select_group_from_dropdown_xpath))

    def click_done(self):
        self.click((By.XPATH, SDR.click_done_xpath))

    def click_quarter_filter(self):
        self.click((By.ID, SDR.click_quarter_filter_ID))

    def select_first_quarter(self):
        self.click((By.XPATH, SDR.first_quarter_xpath))

    def click_reset(self):
        self.click((By.XPATH, SDR.reset_buton_xpath))

    def click_include_exclude_filter(self):
        self.click((By.ID, SDR.click_include_exclude_filter_ID))

    def select_include_filter(self):
        self.click((By.XPATH, SDR.select_include_behaviors_xpath))

    def search_driver_name(self, driver):
        self.type((By.XPATH, SDR.search_driver_input_box_xpath), driver)

    def select_driver_name(self):
        self.click((By.XPATH, SDR.select_first_driver))

    def group_page_is_displayed_in_safe_driver_report(self):
        return self.element_is_displayed((By.XPATH, SDR.group_page_text_xpath))

    def get_filtered_group_name(self):
        return self.get_text((By.XPATH, SDR.filtered_group_name_xpath))

    def get_text_tooltip_next_to_driver_count(self):
        element = self.find((By.XPATH, SDR.tool_tip_icon_xpath))
        self.move_to_element(element)
        return self.get_text((By.XPATH, SDR.driver_count_tool_tip_xpath))

    def get_verbiage_text(self):
        return self.get_text((By.XPATH, SDR.verbiage_text_xpath))

    def hover_on_achievement_icon(self):
        element = self.find((By.XPATH, SDR.achievement_icon_text_xpath))
        self.move_to_element(element)

    def get_achievement_icon_text(self):
        return self.get_text((By.XPATH, SDR.achievement_icon_hover_text_xpath))
