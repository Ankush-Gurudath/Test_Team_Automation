from time import sleep

from selenium.webdriver.common.by import By

from locators.locators_open_tasks_report_page import LocatorsOpenTasksReport as OT
from pages.base_page import BasePage


class OpenTasksReportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_filter_by_group(self):
        self.click((By.XPATH, OT.filter_group_button_xpath))

    def enter_group(self, group_name):
        self.type((By.XPATH, OT.search_by_group_box_xpath), group_name)

    def click_select_group(self):
        self.click((By.XPATH, OT.select_group_search_xpath))

    def click_done(self):
        self.click((By.XPATH, OT.done_button_xpath))

    def enter_name_id(self, name_id):
        self.type((By.XPATH, OT.search_name_box_xpath), name_id)

    def click_select_name(self):
        self.wait_for_element_displayed((By.XPATH, OT.select_name_search_xpath))
        self.click((By.XPATH, OT.select_name_search_xpath))

    def click_reset(self):
        self.click((By.XPATH, OT.reset_link_xpath))

    def get_driver_text(self):
        return self.get_text((By.XPATH, OT.driver_text_xpath))

    def get_driver_group_text(self):
        return self.get_text((By.XPATH, OT.driver_group_text_xpath))

    def get_f2f_text(self):
        return self.get_text((By.XPATH, OT.face_to_face_text_xpath))

    def get_f2f_overdue_text(self):
        return self.get_text((By.XPATH, OT.face_to_face_overdue_text_xpath))

    def get_fyi_notify_text(self):
        return self.get_text((By.XPATH, OT.fyi_notify_text_xpath))

    def click_driver_link(self):
        self.click((By.XPATH, OT.driver_link_xpath))

    def click_event_link(self):
        self.click((By.XPATH, OT.event_link_xpath))

    def get_drivers_number(self):
        return self.get_text((By.XPATH, OT.driver_number_text_xpath))

    def get_driver_name(self):
        return self.get_text((By.XPATH, OT.driver_link_xpath))

    def get_driver_profile_text(self):
        return self.get_text((By.XPATH, OT.driver_profile_text_xpath))

    def get_event_link_text(self):
        return self.get_attribute((By.XPATH, OT.event_link_xpath))

    def get_event_profile_text(self):
        return self.get_text((By.XPATH, OT.event_profile_text_xpath))

    def task_count_displayed(self):
        i = 1
        while i < 5:
            total_tasks = self.get_text((By.XPATH, OT.total_count))
            if total_tasks.isdigit():
                return self.element_is_displayed((By.XPATH, OT.total_count))
            i = i+1
            sleep(1)
        return False

    def get_first_driver_name(self):
        driver_full_name = self.get_text((By.XPATH, OT.driver_link_xpath))
        driver = driver_full_name.split(' ')
        if len(driver) > 2:
            driver_full_name = driver[0] + ' ' + driver[1]
        return driver_full_name

