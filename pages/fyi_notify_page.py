from time import sleep

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By

from locators.locators_fyi_notify_page import LocatorsFyinotify as FN
from pages.base_page import BasePage


class FyiNotifyPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_group_by_filter_fyi_notify(self):
        self.click((By.XPATH, FN.filter_by_group_button_xpath))

    def search_group_by_filter(self, group_name):
        self.type((By.XPATH, FN.search_filter_by_group_textbox_xpath), group_name)

    def select_group_by_filter(self):
        self.click((By.XPATH, FN.select_search_filter_by_group_xpath))

    def click_done_filter_by_group(self):
        self.click((By.XPATH, FN.done_filter_by_group_button_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, FN.reset_fyi_notify_button_xpath))

    def search_driver_name(self, driver_name):
        self.type((By.XPATH, FN.search_driver_name_textbox_xpath), driver_name)

    def get_fyi_notify_tasks_text(self):
        return self.get_text((By.XPATH, FN.fyi_notify_tasks_message_xpath))

    def get_group_text(self):
        return self.get_text((By.XPATH, FN.group_text_xpath))

    def get_vehicle_text(self):
        return self.get_text((By.XPATH, FN.vehicle_text_xpath))

    def get_event_date_text(self):
        return self.get_text((By.XPATH, FN.event_date_text_xpath))

    def get_time_text(self):
        return self.get_text((By.XPATH, FN.time_text_xpath))

    def get_preview_button_text(self):
        return self.get_text((By.XPATH, FN.preview_button_xpath))

    def get_group_name_card(self):
        return self.get_text((By.XPATH, FN.group_card_name_xpath))

    def click_preview_button(self):
        self.click_element_ignore_exceptions((By.XPATH, FN.preview_button_xpath))

    def click_resolve_button(self):
        self.scroll_page_down()
        self.click((By.ID, FN.resolve_button_id))

    def click_coach_now_button(self):
        self.click((By.ID, FN.coach_now_button_id))

    def click_coach_later_button(self):
        self.click((By.ID, FN.coach_later_button_id))

    def click_confirm_button(self):
        self.click((By.XPATH, FN.confirm_button_xpath))
        sleep(2)

    def click_kebab(self):
        self.click((By.XPATH, FN.kebab_button_xpath))

    def select_reassign_driver(self):
        self.click((By.XPATH, FN.reassign_driver_xpath))

    def search_driver(self, driver_name):
        self.type((By.XPATH, FN.search_driver_textbox_xpath), driver_name)

    def select_search_driver(self):
        self.click((By.XPATH, FN.select_searched_driver_xpath))

    def click_assign_button(self):
        self.click((By.XPATH, FN.assign_button_xpath))

    def get_fyi_task_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, FN.fyi_task_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, FN.fyi_task_count_xpath))

    def close_preview_page(self):
        self.click_element_ignore_exceptions((By.XPATH, FN.close_preview_page_button_xpath))

    def close_preview_button_displayed(self):
        return self.element_is_displayed((By.XPATH, FN.close_preview_page_button_xpath))
