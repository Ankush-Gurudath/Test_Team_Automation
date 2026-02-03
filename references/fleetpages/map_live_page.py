from time import sleep

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By

from references.fleetlocators.locators_map_live_page import LocatorsMapLivePage as MLP
from pages.base_page import BasePage


class MapLivePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # load methods
    def wait_for_fleet_tracking_page_loaded(self):
        i = 0
        while i < 3:
            try:
                self.wait_for_element_is_clickable((By.ID, MLP.fleet_tracking_title_id))
                break
            except TimeoutException:
                sleep(1)
                i += 1

        self.wait_for_element_is_clickable((By.ID, MLP.fleet_tracking_title_id))

    def wait_for_working_list_loaded(self, item_count):
        item_xpath = MLP.working_list_item_toggle_prefix_xpath + str(1) + MLP.working_list_item_toggle_suffix_xpath
        self.wait_for_element_is_clickable((By.XPATH, item_xpath), 180)
        i = 2
        while i <= item_count:
            item_xpath = MLP.working_list_item_toggle_prefix_xpath + str(i) + MLP.working_list_item_toggle_suffix_xpath
            self.wait_for_element_is_clickable((By.XPATH, item_xpath))
            i += 1

    # working list search
    def working_list_search(self, input_text):
        self.type((By.XPATH, MLP.search_box_xpath), input_text)

    def select_suggestion_list_1st_item(self, search_text):
        i = 0
        while i < 10:
            try:
                if search_text in str(self.get_text((By.ID, MLP.suggestion_list_1st_item_id))):
                    break
                else:
                    sleep(2)
            except StaleElementReferenceException:
                sleep(2)

            i += 1

        self.click((By.ID, MLP.suggestion_list_1st_item_id))

    def search_result_select_all(self):
        self.click((By.XPATH, MLP.select_all_xpath))

    def search_result_add_to_working_list(self):
        self.click((By.XPATH, MLP.add_to_working_list_xpath))

    # working list actions
    def clear_working_list(self):
        self.click((By.XPATH, MLP.clear_working_list_xpath))

    def click_working_list_1st_item_toggle(self):
        self.click((By.XPATH, MLP.working_list_1st_item_toggle_xpath))

    def working_list_1st_item_name(self):
        return self.get_text((By.XPATH, MLP.working_list_1st_item_name_xpath))

    def working_list_1st_item_driver(self):
        return self.get_text((By.XPATH, MLP.working_list_1st_item_driver_xpath))

    def working_list_1st_item_group(self):
        return self.get_text((By.XPATH, MLP.working_list_1st_item_group_xpath))

    def working_list_1st_item_status(self):
        return self.get_text((By.XPATH, MLP.working_list_1st_item_status_xpath))

    def working_list_1st_item_type(self):
        return self.get_text((By.XPATH, MLP.working_list_1st_item_type_xpath))

    def click_working_list_2nd_item_toggle(self):
        self.click((By.XPATH, MLP.working_list_2nd_item_toggle_xpath))

    def working_list_2nd_item_name(self):
        return self.get_text((By.XPATH, MLP.working_list_2nd_item_name_xpath))

    def working_list_2nd_item_status(self):
        return self.get_text((By.XPATH, MLP.working_list_2nd_item_status_xpath))

    def working_list_2nd_item_type(self):
        return self.get_text((By.XPATH, MLP.working_list_2nd_item_type_xpath))

    def click_view_address_detail(self):
        self.click((By.XPATH, MLP.address_view_detail_xpath))

    # map pins
    def vehicle_pin_is_displayed(self):
        return self.element_is_displayed((By.XPATH, MLP.vehicle_pin_xpath))

    def geofence_pin_is_displayed(self):
        return self.element_is_displayed((By.XPATH, MLP.geofence_pin_xpath))

    def click_vehicle_pin_closest_vehicle(self):
        self.click((By.XPATH, MLP.vehicle_pin_closest_vehicle_xpath))

    def closest_vehicle_estimate_time_is_displayed(self):
        return self.element_is_displayed((By.XPATH, MLP.closest_vehicle_estimate_time_xpath))
