from time import sleep

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By

from locators.locators_geofence_management_page import LocatorsGeofenceManagement as GM
from pages.base_page import BasePage


class GeofenceManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_geofence_page_title(self):
        return self.get_text((By.XPATH, GM.geofence_page_title_xpath))

    def get_geofence_count(self, attempts=10):
        i = 0
        while i < attempts:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, GM.geofence_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, GM.geofence_count_xpath))

    def get_geofence_column_text(self):
        return self.get_text((By.XPATH, GM.geofence_column_text_xpath))

    def get_group_column_text(self):
        return self.get_text((By.XPATH, GM.group_column_text_xpath))

    def get_recent_activity_column_text(self):
        return self.get_text((By.XPATH, GM.recent_activity_column_text_xpath))

    def get_status_column_text(self):
        return self.get_text((By.XPATH, GM.status_column_text_xpath))

    def get_assets_column_text(self):
        return self.get_text((By.XPATH, GM.assets_column_text_xpath))

    def get_trigger_type_column_text(self):
        return self.get_text((By.XPATH, GM.trigger_type_column_text_xpath))

    def get_created_date_column_text(self):
        return self.get_text((By.XPATH, GM.created_date_column_text_xpath))

    def get_source_column_text(self):
        return self.get_text((By.XPATH, GM.source_column_text_xpath))

    def get_group_name_text(self):
        return self.get_text((By.XPATH, GM.group_name_xpath))

    # Filters
    def click_group_filter(self):
        self.click((By.XPATH, GM.group_filter_xpath))

    def search_group(self, group_name):
        self.type((By.XPATH, GM.search_group_xpath), group_name)

    def select_searched_group(self):
        self.click((By.XPATH, GM.select_searched_group_xpath))

    def click_done_button(self):
        self.click((By.XPATH, GM.done_button_xpath))

    def click_recent_activity_filter(self):
        self.click((By.XPATH, GM.recent_activity_filter_xpath))

    def select_last_7_days_recent_activity(self):
        self.click((By.XPATH, GM.recent_activity_last_7_days_xpath))

    def click_apply_button_recent_activity(self):
        self.click((By.XPATH, GM.recent_activity_apply_button_xpath))

    def click_status_filter(self):
        self.click((By.XPATH, GM.status_filter_xpath))

    def select_active_status(self):
        self.click((By.XPATH, GM.select_active_status_xpath))

    def click_created_date_filter(self):
        self.click((By.XPATH, GM.created_date_filter_xpath))

    def set_geofence_created_date_range(self, start_month, start_day, start_year, end_month, end_day, end_year):
        self.click((By.XPATH, GM.created_date_range_start_month_xpath))
        self.type((By.XPATH, GM.created_date_range_start_month_xpath), start_month)
        self.click((By.XPATH, GM.created_date_range_start_day_xpath))
        self.type((By.XPATH, GM.created_date_range_start_day_xpath), start_day)
        self.click((By.XPATH, GM.created_date_range_start_year_xpath))
        self.type((By.XPATH, GM.created_date_range_start_year_xpath), start_year)
        self.click((By.XPATH, GM.created_date_range_end_month_xpath))
        self.type((By.XPATH, GM.created_date_range_end_month_xpath), end_month)
        self.click((By.XPATH, GM.created_date_range_end_day_xpath))
        self.type((By.XPATH, GM.created_date_range_end_day_xpath), end_day)
        self.click((By.XPATH, GM.created_date_range_end_year_xpath))
        self.type((By.XPATH, GM.created_date_range_end_year_xpath), end_year)

    def click_apply_button_created_date(self):
        self.click((By.XPATH, GM.created_date_apply_button_xpath))

    def search_geofence_name(self, geofence_name):
        self.type((By.XPATH, GM.search_geofence_name_input_box_xpath), geofence_name)

    def click_reset_button(self):
        self.click((By.XPATH, GM.reset_button_xpath))
        self.get_geofence_count()

    def click_import_geofence_management(self):
        self.click((By.XPATH, GM.import_button_xpath))

    def download_template_geofence_management(self):
        self.click((By.XPATH, GM.download_template_xpath))

    def geofence_count_displayed(self):
        result = self.element_is_displayed((By.XPATH, GM.geofence_count_xpath))
        return result
