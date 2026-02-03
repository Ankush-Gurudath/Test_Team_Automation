from time import sleep

from selenium.common import StaleElementReferenceException, ElementClickInterceptedException, \
    ElementNotInteractableException, TimeoutException, WebDriverException
from selenium.webdriver.common.by import By

from locators.locators_risk_company import LocatorsRiskCompany as RC
from pages.base_page import BasePage


class RiskCompanyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Dashboard
    def get_dashboard_text(self):
        self.wait_for_element_displayed((By.XPATH, RC.dashboard_text_xpath))
        return self.get_text((By.XPATH, RC.dashboard_text_xpath))

    def get_drivers_by_highest_score_text(self):
        self.wait_for_element_displayed((By.XPATH, RC.drivers_by_highest_text_score_text_xpath))
        return self.get_text((By.XPATH, RC.drivers_by_highest_text_score_text_xpath))

    def get_categories_by_highest_frequency_text(self):
        self.wait_for_element_displayed((By.XPATH, RC.categories_by_highest_frequency_text_xpath))
        return self.get_text((By.XPATH, RC.categories_by_highest_frequency_text_xpath))

    def click_view_details(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.view_detail_xpath))

    def driver_count_displayed(self):
        return self.element_is_displayed((By.XPATH, RC.driver_count_xpath))

    def group_filter_displayed(self):
        return self.element_is_displayed((By.XPATH, RC.group_filter_xpath))

    def date_filter_displayed(self):
        return self.element_is_displayed((By.XPATH, RC.date_filter_xpath))

    def click_filter_group_dashboard(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.group_filter_xpath))

    def search_group_filter_dashboard(self, group_name):
        self.type((By.XPATH, RC.search_group_filter_textbox_xpath), group_name)

    def click_searched_group_filter(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.select_searched_group_filter_xpath))

    def click_done_group_filter(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.done_button_group_filter_xpath))

    def click_date_filter(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.date_filter_xpath))

    def click_date1_filter(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.select_date1_button_xpath))

    def click_date2_filter(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.select_date2_button_xpath))

    def click_apply_date_filter(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.apply_date_filter_xpath))

    def click_reset_button(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.reset_button_xpath))

    def click_home_tab(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.home_tab_xpath))

    def click_insights_tab(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.insight_tab_xpath))

    def click_insights_tab_new_ui(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.insight_tab_new_ui_xpath))

    def click_drivers_report_tab(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.drivers_report_tab_xpath))

    def click_drivers_report_new_ui(self):
        try:
            self.click_element_ignore_exceptions((By.XPATH, RC.drivers_report_new_ui_xpath))
        except (ElementClickInterceptedException, TimeoutException, WebDriverException):
            self.click_insights_tab_new_ui()
            self.click_element_ignore_exceptions((By.XPATH, RC.drivers_report_new_ui_xpath))

    def get_drivers_report_text(self):
        self.wait_for_element_displayed((By.XPATH, RC.drivers_report_title_xpath))
        return self.get_text((By.XPATH, RC.drivers_report_title_xpath))

    def get_driver_scors_text(self):
        self.wait_for_element_displayed((By.XPATH, RC.driver_scores_title_xpath))
        return self.get_text((By.XPATH, RC.driver_scores_title_xpath))

    def get_continual_behaviors_text(self):
        self.wait_for_element_displayed((By.XPATH, RC.continual_behaviors_title_xpath))
        return self.get_text((By.XPATH, RC.continual_behaviors_title_xpath))

    def get_alerts_text(self):
        self.wait_for_element_displayed((By.XPATH, RC.alerts_title_xpath))
        return self.get_text((By.XPATH, RC.alerts_title_xpath))

    def get_driver_text(self):
        self.wait_for_element_displayed((By.XPATH, RC.driver_title_xpath))
        return self.get_text((By.XPATH, RC.driver_title_xpath))

    def get_group_text(self):
        self.wait_for_element_displayed((By.XPATH, RC.group_title_xpath))
        return self.get_text((By.XPATH, RC.group_title_xpath))

    def get_score_text(self):
        self.wait_for_element_displayed((By.XPATH, RC.score_title_xpath))
        return self.get_text((By.XPATH, RC.score_title_xpath))

    def get_events_text(self):
        self.wait_for_element_displayed((By.XPATH, RC.events_title_xpath))
        return self.get_text((By.XPATH, RC.events_title_xpath))

    def get_recent_notes_text(self):
        self.wait_for_element_displayed((By.XPATH, RC.recent_notes_title_xpath))
        return self.get_text((By.XPATH, RC.recent_notes_title_xpath))

    def click_categories_filter(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.categories_filter_button_xpath))

    def select_categories_filter(self):
        self.click_element_ignore_exceptions((By.XPATH, RC.select_categories_filter_xpath))

    def click_home_tab_new_ui(self):
        n = 0
        while n < 5:
            n += 1
            try:
                self.click((By.XPATH, RC.home_tab_xpath_new_ui))
                break
            except (StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException):
                sleep(3)

        if n == 5:
            self.click((By.XPATH, RC.home_tab_xpath_new_ui))
