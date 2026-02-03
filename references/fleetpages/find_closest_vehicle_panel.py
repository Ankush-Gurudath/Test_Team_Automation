from selenium.webdriver.common.by import By

from references.fleetlocators.loctors_find_closest_vehicle_panel import FindClosestVehiclePanelLocator as FCVPL
from pages.base_page import BasePage


class FindClosestVehiclePanel(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def close_panel(self):
        self.click((By.XPATH, FCVPL.close_button_xpath))

    def click_trash_icon_1st(self):
        self.click((By.XPATH, FCVPL.trash_icon_1st_xpath))

    def vehicle_1st_is_selected(self):
        if self.get_attribute((By.XPATH, FCVPL.vehicle_1st_xpath), "class") == "row selected":
            return True
        else:
            return False

    def vehicle_name_1st_is_displayed(self):
        return self.element_is_displayed((By.XPATH, FCVPL.vehicle_name_1st_xpath))

    def trash_icon_1st_is_displayed(self):
        return self.element_is_displayed((By.XPATH, FCVPL.trash_icon_1st_xpath))
