from time import sleep

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By

from locators.locators_assign_driver_page import LocatorsAssignDriver as AD
from pages.base_page import BasePage


class AssignDriverPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_assign_button(self):
        self.click((By.XPATH, AD.assign_button_xpath))

    def search_assign_driver(self, driver_name):
        self.type((By.XPATH, AD.assign_driver_search_xpath), driver_name)

    def select_searched_driver(self):
        self.click((By.XPATH, AD.select_assign_driver_search_xpath))

    def click_assign(self):
        self.click((By.XPATH, AD.assign_driver_button_xpath))

    def click_filter_by_group_button(self):
        self.click((By.XPATH, AD.filter_group_button_xpath))

    def search_filter_by_group(self, group_name):
        self.type((By.XPATH, AD.search_group_filter_box_xpath), group_name)

    def select_search_filter_by_group(self):
        self.click((By.XPATH, AD.select_search_group_filter_xpath))

    def click_done_button(self):
        self.click((By.XPATH, AD.done_button_group_filter_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, AD.reset_button_xpath))

    def get_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, AD.task_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, AD.task_count_xpath))

    def get_assign_select_button_text(self):
        return self.get_text((By.XPATH, AD.assign_selected_button_xpath))

    def get_group_name_text(self):
        return self.get_text((By.XPATH, AD.group_name_text_xpath))

    def get_vehicle_text(self):
        return self.get_text((By.XPATH, AD.vehicle_text_xpath))

    def get_group_text(self):
        return self.get_text((By.XPATH, AD.group_text_xpath))

    def get_event_date_text(self):
        return self.get_text((By.XPATH, AD.event_date_text_xpath))

    def get_event_id_text(self):
        return self.get_text((By.XPATH, AD.event_id_text_xpath))

    def get_behavior_text(self):
        return self.get_text((By.XPATH, AD.behavior_text_xpath))

    def get_assign_button_text(self):
        return self.get_text((By.XPATH, AD.assign_button_xpath))

    def get_move_group_button_text(self):
        return self.get_text((By.XPATH, AD.move_group_button_xpath))

    def get_disabled_status_of_move_group_button(self):
        return self.get_attribute((By.XPATH, AD.move_group_button_xpath), 'disabled')

    def get_disabled_status_of_assign_selected_button(self):
        return self.get_attribute((By.XPATH, AD.assign_selected_button_xpath), 'disabled')

    def click_assign_driver_checkbox(self):
        self.click((By.XPATH, AD.assign_driver_checkbox_xpath))

    def click_assign_selected_button(self):
        self.click((By.XPATH, AD.assign_selected_button_xpath))

    def click_third_assign_driver_task_checkbox(self):
        self.click((By.XPATH, AD.third_assign_driver_task_checkbox_xpath))

    def click_fourth_assign_driver_task_checkbox(self):
        self.click((By.XPATH, AD.fourth_assign_driver_task_checkbox_xpath))

    def click_preview_button(self):
        self.click((By.XPATH, AD.preview_button_xpath))

    def close_preview_page(self):
        self.click_element_ignore_exceptions((By.XPATH, AD.close_preview_button_xpath))

    def click_more_actions_button(self):
        self.click((By.XPATH, AD.more_actions_button_xpath))

    def click_mark_as_fyi_notify(self):
        self.click((By.XPATH, AD.mark_as_fyi_notify_xpath))

    def click_yes_confirm_button(self):
        self.click((By.XPATH, AD.yes_confirm_button_xpath))
