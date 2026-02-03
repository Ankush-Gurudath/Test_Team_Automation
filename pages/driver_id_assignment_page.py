from time import sleep

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By

from locators.locators_driver_id_assignment_page import LocatorsDriverIdAssignment as DA
from pages.base_page import BasePage


class DriverIdAssignmentPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_vehicle_column_label(self):
        return self.get_text((By.XPATH, DA.vehicle_label_xpath))

    def get_group_column_label(self):
        return self.get_text((By.XPATH, DA.group_label_xpath))

    def get_driver_column_label(self):
        return self.get_text((By.XPATH, DA.driver_label_xpath))

    def get_employee_id_label(self):
        return self.get_text((By.XPATH, DA.employee_id_label_xpath))

    def get_driver_id_source_column_label(self):
        return self.get_text((By.XPATH, DA.driver_id_source_label_xpath))

    def get_trip_start_column_label(self):
        return self.get_text((By.XPATH, DA.trip_start_label_xpath))

    def get_trip_end_column_label(self):
        return self.get_text((By.XPATH, DA.trip_end_label_xpath))

    def get_duration_column_label(self):
        return self.get_text((By.XPATH, DA.duration_label_xpath))

    def get_assigned_trips_summary_label(self):
        return self.get_text((By.XPATH, DA.assigned_trips_summary_label_xpath))

    def get_assigned_by_dispatch_api_summary_label(self):
        return self.get_text((By.XPATH, DA.assigned_by_dispatch_api_summary_label_xpath))

    def get_assigned_by_lytx_badge_summary_label(self):
        return self.get_text((By.XPATH, DA.assigned_by_lytx_badge_summary_label_xpath))

    def get_assigned_by_vehicle_summary_label(self):
        return self.get_text((By.XPATH, DA.assigned_by_vehicle_summary_label_xpath))

    def get_unassigned_trips_summary_label(self):
        return self.get_text((By.XPATH, DA.unassigned_trips_summary_label_xpath))

    def get_percent_of_all_assigned_trips_graph_label(self):
        return self.get_text((By.XPATH, DA.percent_of_all_assigned_trips_graph_label_xpath))

    def click_group_filter_button(self):
        self.click((By.XPATH, DA.filter_group_button_xpath))

    def search_group_filter(self, group_name):
        self.type((By.XPATH, DA.search_filter_group_textbox_xpath), group_name)

    def select_search_group_filter_button(self):
        self.click((By.XPATH, DA.select_search_filter_group_button_xpath))

    def click_done_group_filter_button(self):
        self.click((By.XPATH, DA.done_filter_group_button_xpath))

    def click_date_filter_button(self):
        self.click((By.XPATH, DA.date_filter_button_xpath))

    def select_first_date_filter_button(self):
        self.click((By.XPATH, DA.first_date_filter_button_xpath))

    def select_second_date_filter_button(self):
        self.click((By.XPATH, DA.second_date_filter_button_xpath))

    def click_date_filter_done_button(self):
        self.click((By.XPATH, DA.apply_filter_date_button_xpath))

    def click_search_filter_button(self):
        self.click((By.XPATH, DA.search_filter_button_xpath))

    def click_search_driver_filter_button(self):
        self.click((By.XPATH, DA.search_driver_filter_button_xpath))

    def click_search_vehicle_filter_button(self):
        self.click((By.XPATH, DA.search_vehicle_filter_button_xpath))

    def search_criteria_filter(self, search_DV):
        self.type((By.XPATH, DA.search_criteria_filter_textbox_xpath), search_DV)

    def click_searched_name_button_xpath(self):
        self.wait_for_element_displayed((By.XPATH, DA.select_searched_name_button_xpath))
        self.click((By.XPATH, DA.select_searched_name_button_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, DA.reset_button_xpath))

    def get_trip_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, DA.trip_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, DA.trip_count_xpath))
