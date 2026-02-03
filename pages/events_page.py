from selenium.webdriver.common.by import By

from locators.locators_events_page import LocatorsEvents as EV
from pages.base_page import BasePage


class EventsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # SelectSearch
    def select_search(self):
        self.click((By.CSS_SELECTOR, EV.select_search_filter_css))

    def select_event_id(self):
        self.click((By.XPATH, EV.event_id_select_filter_xpath))

    def send_search_event_id(self, event_id):
        self.type((By.CSS_SELECTOR, EV.search_by_id_tab_css), event_id)

    def click_search_button(self):
        self.click((By.XPATH, EV.search_button_xpath))

    # ClickOnevent
    def click_first_event_tab(self):
        self.click((By.XPATH, EV.first_event_tab_xpath))

    def click_second_event_tab(self):
        self.click((By.CSS_SELECTOR, EV.second_event_tab_css))

    # MoreActions
    def click_more_actions(self):
        self.click((By.XPATH, EV.more_actions_tab_xpath))

    def click_reassign_driver(self):
        self.click((By.XPATH, EV.reassign_driver_select_xpath))

    def click_mark_as_f2f(self):
        self.click((By.XPATH, EV.mark_as_f2f_coaching_xpath))

    def click_yes_confirm(self):
        self.click((By.XPATH, EV.yes_confirm_button_xpath))

    # AssignDriver
    def send_search_assign_driver(self, driver):
        self.type((By.XPATH, EV.assign_driver_search_xpath), driver)

    def select_searched_driver(self):
        self.click((By.XPATH, EV.select_assigned_driver_xpath))

    def click_assign_button(self):
        self.click((By.XPATH, EV.assign_button_xpath))

    # CloseVideo
    def click_close_video(self):
        self.click((By.XPATH, EV.close_video_xpath))

    # ClickOnDriver
    def click_driver_link(self):
        self.click((By.XPATH, EV.driver_link_xpath))

    def get_event_status_self_coaching_text(self):
        return self.get_text((By.XPATH, EV.event_status_self_coaching_text_xpath))

    def get_event_status_resolved_text(self):
        return self.get_text((By.XPATH, EV.event_status_resolved_text_xpath))

    def get_event_date_format_label(self):
        global localdate
        date = self.get_text((By.XPATH, EV.first_event_date_xpath)).split()
        self.localdate = date[0].strip()
        return self.localdate

    def event_date_month_is_word(self):
        global localdate
        event_date = self.get_text((By.XPATH, EV.first_event_date_xpath)).split()
        month = self.localdate = event_date[0].strip()
        if month.isalpha():
            return True
        else:
            return False

    def event_date_month_is_word_new_UI(self):
        global localdate
        event_date = self.get_text((By.XPATH, EV.first_event_date_new_UI_xpath)).split()
        month = self.localdate = event_date[0].strip()
        if month.isalpha():
            return True
        else:
            return False

    def move_to_element_overlay_toggle(self):
        web_element = self.find((By.XPATH, EV.overlay_toggle_xpath))
        self.move_to_element(web_element)

    def get_overlay_toggle_text(self):
        return self.get_text((By.XPATH, EV.overlay_toggle_hover_xpath))

    def get_overlay_label_text(self):
        return self.get_text((By.XPATH, EV.overlay_label_xpath))

    def click_download_option_mp4_with_overlay(self):
        self.click((By.XPATH, EV.download_option_mp4_with_overlay_xpath))