from datetime import datetime
from time import sleep

import pytz
from selenium.common import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By

from locators.locators_inspection_schedules_page import LocatorsInspectionSchedules as IS
from pages.base_page import BasePage


class InspectionSchedulesPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Labels
    def get_inspection_schedules_title(self):
        self.wait_for_element_displayed((By.XPATH, IS.inspection_schedules_title_xpath))
        return self.get_text((By.XPATH, IS.inspection_schedules_title_xpath))

    def get_reports_title(self):
        return self.get_text((By.XPATH, IS.reports_count_title_xpath))

    def get_vehicle_name_title(self):
        return self.get_text((By.XPATH, IS.vehicle_name_title_xpath))

    def get_vehicle_group_title(self):
        return self.get_text((By.XPATH, IS.vehicle_group_title_xpath))

    def get_status_title(self):
        return self.get_text((By.XPATH, IS.status_title_xpath))

    def get_due_date_title(self):
        return self.get_text((By.XPATH, IS.due_date_title_xpath))

    def get_inspection_list_title(self):
        return self.get_text((By.XPATH, IS.inspection_list_title_xpath))

    def get_inspection_frequency_title(self):
        return self.get_text((By.XPATH, IS.inspection_frequency_title_xpath))

    def get_last_inspected_date_title(self):
        return self.get_text((By.XPATH, IS.last_inspected_date_title_xpath))

    def get_last_inspected_driver_title(self):
        return self.get_text((By.XPATH, IS.last_inspected_driver_title_xpath))

    # Filters
    def click_groups_filter(self):
        self.click((By.XPATH, IS.groups_filter_button_xpath))

    def search_groups_filter(self, searched_group):
        self.type((By.XPATH, IS.search_group_textbox_xpath), searched_group)

    def select_groups_filter(self):
        self.click((By.XPATH, IS.select_group_filter_button_xpath))

    def select_groups_root_filter(self):
        self.click((By.XPATH, IS.trailer_select_group_root_xpath))

    def click_done_button(self):
        self.click((By.XPATH, IS.done_button_group_filter_xpath))

    def click_inspection_lists_filter(self):
        self.click((By.XPATH, IS.inspection_list_filter_button_xpath))

    def select_inspection_lists_filter(self):
        self.click((By.XPATH, IS.select_inspection_list_filter_xpath))

    def get_selected_inspection_list(self):
        self.wait_for_element_displayed((By.XPATH, IS.selected_inspection_list_text_xpath))
        return self.get_text((By.XPATH, IS.selected_inspection_list_text_xpath))

    def close_vehicle_inspection_list(self):
        self.click((By.XPATH, IS.close_vehicle_inspection_list_xpath))

    def click_status_filter(self):
        self.click((By.XPATH, IS.status_filter_button_xpath))

    def select_status_filter(self):
        self.click((By.XPATH, IS.select_status_filter_button_xpath))

    def search_vehicle_name_filter(self, searched_vehicle):
        self.type((By.XPATH, IS.search_vehicle_name_textbox_xpath), searched_vehicle)

    def click_search_vehicle_icon(self):
        self.click((By.XPATH, IS.search_vehicle_name_icon_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, IS.reset_button_xpath))

    def get_vehicle_group_first_row_text(self):
        self.wait_for_element_displayed((By.XPATH, IS.vehicle_group_first_row_text_xpath))
        return self.get_text((By.XPATH, IS.vehicle_group_first_row_text_xpath))

    def get_status_first_row_text(self):
        self.wait_for_element_displayed((By.XPATH, IS.status_first_row_text_xpath))
        return self.get_text((By.XPATH, IS.status_first_row_text_xpath))

    def get_inspection_list_first_row_text(self):
        self.wait_for_element_displayed((By.XPATH, IS.inspection_list_first_row_text_xpath))
        return self.get_text((By.XPATH, IS.inspection_list_first_row_text_xpath))

    def get_vehicle_name_first_row_text(self):
        try:
            return self.get_text((By.XPATH, IS.vehicle_name_first_row_text_xpath))
        except TimeoutException:
            sleep(2)
            return self.get_text((By.XPATH, IS.vehicle_name_first_row_text_xpath))

    def click_download_csv_report(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click((By.XPATH, IS.download_csv_button_xpath))
        # wait for download complete
        sleep(20)

    def get_dvir_list_file_name(self):
        date_now = datetime.now(tz=pytz.timezone("US/Pacific")).strftime("%Y-%m-%d")
        file_name = 'Dvir Full DVIR List' + ' ' + date_now + '.csv'
        return file_name

    def click_trailer_schedules_link(self):
        self.click((By.XPATH, IS.trailer_schedules_link_xpath))

    def get_trailer_reports_title(self):
        return self.get_text((By.XPATH, IS.reports_trailer_title_xpath))

    def get_inspection_list_column_text(self):
        return self.get_text((By.XPATH, IS.inspection_list_column_xpath))

    def get_trailer_name_column_text(self):
        return self.get_text((By.XPATH, IS.trailer_name_column_xpath))

    def get_trailer_group_column_text(self):
        return self.get_text((By.XPATH, IS.trailer_group_column_xpath))

    def get_status_column_text(self):
        return self.get_text((By.XPATH, IS.status_column_xpath))

    def get_due_date_column_text(self):
        return self.get_text((By.XPATH, IS.due_date_column_xpath))

    def get_inspection_frequency_column_text(self):
        return self.get_text((By.XPATH, IS.inspection_frequency_column_xpath))

    def get_last_inspected_date_column_text(self):
        return self.get_text((By.XPATH, IS.last_inspected_date_column_xpath))

    def get_last_inspected_driver_column_text(self):
        return self.get_text((By.XPATH, IS.last_inspected_driver_column_xpath))

    def click_trailer_group_filter_button(self):
        self.click((By.XPATH, IS.trailer_group_filter_button_xpath))

    def search_trailer_groups_filter(self, searched_group):
        self.type((By.XPATH, IS.trailer_search_group_filter_xpath), searched_group)

    def select_trailer_group_filter(self):
        self.click((By.XPATH, IS.select_group_filter_button_xpath))

    def click_trailer_schedule_group_done_button(self):
        self.click((By.XPATH, IS.trailer_group_done_button_xpath))

    def click_trailer_inspection_list_filter(self):
        self.click((By.XPATH, IS.trailer_inspection_list_filter_button_xpath))

    def select_trailer_inspection_list_filter(self):
        self.click((By.XPATH, IS.trailer_select_inspection_list_button_xpath))

    def get_selected_trailer_inspection_list(self):
        return self.get_text((By.XPATH, IS.selected_trailer_inspection_list_text_xpath))

    def click_status_inspection_list_filter(self):
        self.click((By.XPATH, IS.trailer_status_filter_button_xpath))

    def select_status_inspection_list_filter(self):
        self.click((By.XPATH, IS.trailer_select_status_button_xpath))

    def search_trailer_name_filter(self, searched_trailer):
        self.type((By.XPATH, IS.search_trailer_name_filter_textbox_xpath), searched_trailer)

    def click_trailer_search_name_icon(self):
        self.click((By.XPATH, IS.click_search_trailer_name_icon_xpath))

    def click_trailer_reset_button(self):
        self.click((By.XPATH, IS.trailer_reset_button_xpath))

    def get_first_trailer_group_text(self):
        self.wait_for_element_displayed((By.XPATH, IS.first_trailer_group_text_xpath))
        return self.get_text((By.XPATH, IS.first_trailer_group_text_xpath))

    def get_first_trailer_inspection_list_text(self):
        self.wait_for_element_displayed((By.XPATH, IS.first_trailer_inspection_list_text_xpath))
        return self.get_text((By.XPATH, IS.first_trailer_inspection_list_text_xpath))

    def get_first_trailer_status_text(self):
        self.wait_for_element_displayed((By.XPATH, IS.first_trailer_status_text_xpath))
        return self.get_text((By.XPATH, IS.first_trailer_status_text_xpath))

    def get_first_trailer_name_text_stg(self):
        return self.get_text((By.XPATH, IS.first_trailer_name_text_stg_xpath))

    def get_first_trailer_name_text_int(self):
        return self.get_text((By.XPATH, IS.first_trailer_name_text_int_xpath))

    def close_trailer_inspection_list(self):
        self.click((By.XPATH, IS.close_trailer_inspection_list_xpath))
