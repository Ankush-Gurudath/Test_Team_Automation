from time import sleep

from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By

from locators.locators_coaches_report_page import LocatorsCoachesReport as CR
from pages.base_page import BasePage


class CoachesReportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_coach_profile_title_text(self):
        try:
            return self.get_text((By.XPATH, CR.coach_profile_title_text_xpath))
        except StaleElementReferenceException:
            sleep(1)
            return self.get_text((By.XPATH, CR.coach_profile_title_text_xpath))

    def get_num_of_coaches_text(self):
        self.wait_for_element_displayed((By.XPATH, CR.coaches_num_text_xpath))
        return self.element_is_displayed((By.XPATH, CR.coaches_num_text_xpath))

    def get_coach_text(self):
        return self.get_text((By.XPATH, CR.coach_text_xpath))

    def get_group_text(self):
        return self.get_text((By.XPATH, CR.group_text_xpath))

    def get_coaching_effectiveness_text(self):
        return self.get_text((By.XPATH, CR.coaching_effectiveness_text_xpath))

    def get_avg_days_to_coach_text(self):
        return self.get_text((By.XPATH, CR.avg_days_to_coach_text_xpath))

    def get_coached_events_text(self):
        return self.get_text((By.XPATH, CR.coached_events_text_xpath))

    def get_with_notes_text(self):
        return self.get_text((By.XPATH, CR.with_notes_text_xpath))

    def get_last_login_text(self):
        return self.get_text((By.XPATH, CR.last_login_text_xpath))

    # Filters
    def click_filter_by_group_coaches(self):
        self.click((By.XPATH, CR.filter_by_group_coaches_button_xpath))

    def search_filter_by_group_coaches(self, search_group_coaches):
        self.type((By.XPATH, CR.search_by_group_coaches_textbox_xpath), search_group_coaches)

    def select_filter_by_group_coaches(self):
        self.click((By.XPATH, CR.select_search_by_group_coaches_button_xpath))

    def click_done_filter_by_group_coaches(self):
        self.click((By.XPATH, CR.done_search_by_group_coaches_button_xpath))

    # FilterByDate
    def click_filter_by_date_coaches(self):
        self.click((By.XPATH, CR.filter_by_date_coaches_button_xpath))

    def select_from_date_by_date_coaches(self):
        self.click((By.XPATH, CR.from_date_coaches_button_xpath))

    def select_end_date_by_date_coaches(self):
        self.click((By.XPATH, CR.end_date_coaches_button_xpath))

    def click_apply_by_date_coaches(self):
        self.click((By.XPATH, CR.apply_filter_by_date_coaches_button_xpath))

    # FilterByGroupActivity
    def click_filter_by_coaches_activity(self):
        self.click((By.XPATH, CR.coaches_by_activity_filter_button_xpath))

    def select_filter_by_coaches_activity(self):
        self.click((By.XPATH, CR.select_coaches_by_activity_button_xpath))

    # FilterByGroupData
    def click_filter_by_group_data_only(self):
        self.click((By.XPATH, CR.group_data_only_coaches_button_xpath))

    def select_filter_by_group_data_only(self):
        self.click((By.XPATH, CR.select_group_data_button_xpath))

    # Links
    def click_coach_link(self):
        self.click((By.XPATH, CR.coach_link_text_xpath))

    def get_coach_profile_text(self):
        return self.get_text((By.XPATH, CR.coach_profile_text_xpath))

    def back_to_previous_page(self):
        self.back()

    # Reset
    def click_reset(self):
        self.click((By.XPATH, CR.reset_button_xpath))

    def click_coach_name(self):
        self.click((By.XPATH, CR.coach_name_xpath))

    def get_coach_name(self):
        self.wait_for_element_displayed((By.XPATH, CR.first_coach_name_xpath))
        return self.get_text((By.XPATH, CR.first_coach_name_xpath))

    def get_group_name(self):
        group_name = self.get_text((By.XPATH, CR.group_name_xpath))
        return group_name
