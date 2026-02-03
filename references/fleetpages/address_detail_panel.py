from selenium.webdriver.common.by import By

from references.fleetlocators.locators_address_detail_panel import AddressDetailPanelLocator as ADLP
from pages.base_page import BasePage


class AddressDetailPanel(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def close_panel(self):
        self.click((By.XPATH, ADLP.close_button_xpath))

    def click_find_closest_vehicle(self):
        self.click((By.XPATH, ADLP.find_closest_vehicle_xpath))
