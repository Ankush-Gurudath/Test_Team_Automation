import time
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from locators.locators_hos import LocatorsHos as LH
from pages.base_page import BasePage


class HosPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def username_is_displayed(self):
        self.wait_for_element_displayed((By.ID, LH.hos_username_id))
        return self.element_is_displayed((By.ID, LH.hos_username_id))

    def company_is_displayed(self):
        return self.element_is_displayed((By.ID, LH.hos_company_id))

    def switch_hos_iframe(self):
        self.wait_for_element_displayed((By.CLASS_NAME, LH.hos_iframe_class))
        self.driver.switch_to.frame(self.driver.find_element(By.CLASS_NAME, LH.hos_iframe_class))

    def switch_iframe(self):
        time.sleep(30)
        self.driver.switch_to.frame(0)

    def click_accept_cookies_button(self):
        self.wait_for_element_is_clickable((By.ID, LH.walkme_iframe_id))
        i = 0
        while i < 10:
            try:
                self.click((By.XPATH, LH.compliance_menu))
                break
            except ElementClickInterceptedException:
                self.driver.switch_to.frame(LH.walkme_iframe_id)
                self.click((By.XPATH, LH.accept_cookies_button))
                self.driver.switch_to.default_content()
                self.driver.switch_to.frame(0)
                i += 1

    def click_compliance_menu(self):
        self.click((By.XPATH, LH.compliance_menu))

    def click_hos(self):
        self.click((By.XPATH, LH.compliance_hos_button))

    def click_hos_logs(self):
        self.click((By.XPATH, LH.compliance_hos_logs_button))

    def click_violations(self):
        self.click((By.XPATH, LH.compliance_hos_violations_button))

    def search_all_drivers(self):
        self.click((By.XPATH, LH.drivers_drop_down))
        self.click((By.XPATH, LH.select_all))
        self.click((By.XPATH, LH.apply_change_button))

    def click_assets_menu(self):
        self.click((By.XPATH, LH.assets_menu_button))

    def get_assets_title(self):
        return self.get_text((By.XPATH, LH.assets_title))

    def get_hos_logs_title(self):
        return self.get_text((By.XPATH, LH.hos_logs_title))

    def get_hos_violations_title(self):
        return self.get_text((By.XPATH, LH.hos_violations_title))
