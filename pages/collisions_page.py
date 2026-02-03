from time import sleep

from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By

from locators.locators_collisions_page import LocatorsCollisions as LC
from pages.base_page import BasePage


class CollisionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_group_by_filter_collisions(self):
        self.click((By.XPATH, LC.filter_by_group_button_xpath))

    def search_group_by_filter(self, group_name):
        self.type((By.XPATH, LC.search_by_group_textbox_xpath), group_name)

    def select_group_by_filter(self):
        self.click((By.XPATH, LC.select_search_by_group_xpath))

    def click_done_filter_by_group(self):
        self.click((By.XPATH, LC.done_filter_by_group_button_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, LC.reset_button_xpath))

    def search_driver_name(self, driver_name):
        self.type((By.XPATH, LC.search_driver_name_text_box_xpath), driver_name)

    def get_collisions_tasks_text(self):
        return self.get_text((By.XPATH, LC.collision_tasks_text_xpath))

    def get_task_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, LC.task_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, LC.task_count_xpath))

    def get_driver_name_text(self):
        return self.get_text((By.XPATH, LC.driver_name_text_xpath))

    def driver_name_on_task_card_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LC.driver_name_on_task_card_xpath))

    def get_group_text(self):
        return self.get_text((By.XPATH, LC.group_text_xpath))

    def get_group_text_new_ui(self):
        return self.get_text((By.ID, LC.group_text_id))

    def get_vehicle_text(self):
        return self.get_text((By.XPATH, LC.vehicle_text_xpath))

    def get_vehicle_text_new_UI(self):
        return self.get_text((By.ID, LC.vehicle_text_id))

    def get_event_date_text(self):
        return self.get_text((By.XPATH, LC.event_date_text_xpath))

    def get_event_date_text_new_UI(self):
        return self.get_text((By.ID, LC.date_text_id))

    def get_time_text(self):
        return self.get_text((By.XPATH, LC.time_text_xpath))

    def get_time_text_new_UI(self):
        return self.get_text((By.ID, LC.time_text_id))

    def get_preview_button_text(self):
        return self.get_text((By.XPATH, LC.preview_button_text_xpath))

    def get_preview_button_text_new_UI(self):
        return self.get_text((By.XPATH, LC.preview_card_xpath))

    def get_group_name(self):
        return self.get_text((By.XPATH, LC.group_name_xpath))

    def click_preview_button(self):
        self.click((By.XPATH, LC.preview_button_text_xpath))

    def click_resolved_button(self):
        self.scroll_page_down()
        self.wait_for_element_is_clickable((By.ID, LC.resolved_button_id))
        self.click((By.ID, LC.resolved_button_id))

    def click_coach_later_button(self):
        self.click((By.ID, LC.coach_later_button_id))

    def click_confirm_button(self):
        self.click((By.XPATH, LC.confirm_button_xpath))

    def click_no_not_a_collision_button(self):
        self.wait_for_element_is_clickable((By.XPATH, LC.no_not_a_collision_button_xpath))
        self.click((By.XPATH, LC.no_not_a_collision_button_xpath))

    def click_yes_for_possible_collision_button(self):
        self.wait_for_element_is_clickable((By.XPATH, LC.yes_for_possible_collision_button_xpath))
        self.click((By.XPATH, LC.yes_for_possible_collision_button_xpath))

    def click_close_icon(self):
        self.wait_for_element_is_clickable((By.XPATH, LC.close_icon_xpath))
        i = 0
        while i < 10:
            try:
                self.click((By.XPATH, LC.close_icon_xpath))
                break
            except ElementClickInterceptedException:
                sleep(1)
                i += 1

    def click_coach_now_button(self):
        self.click((By.ID, LC.coach_now_button_id))

    def click_kebab(self):
        self.click((By.XPATH, LC.kebab_button_xpath))

    def select_reassign_driver(self):
        self.click((By.XPATH, LC.reassign_driver_xpath))

    def search_driver(self, driver_name):
        self.element_is_displayed((By.XPATH, LC.search_driver_textbox_xpath))
        self.type((By.XPATH, LC.search_driver_textbox_xpath), driver_name)

    def select_search_driver(self):
        self.click((By.XPATH, LC.select_searched_driver_xpath))

    def click_assign_button(self):
        self.click((By.XPATH, LC.assign_button_xpath))
