from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from references.loginlocators.locator_fleet_login_page import LocatorsFleetLogin as FL
from pages.base_page import BasePage


class FleetLoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_username(self, username):
        try:
            self.find((By.ID, FL.username_textbox_id))
        except NoSuchElementException:
            self.click_refresh_button()
            sleep(30)
        except TimeoutException:
            self.click_refresh_button()
            sleep(30)
        finally:
            self.type((By.ID, FL.username_textbox_id), username)

    def enter_password(self, password):
        self.type((By.ID, FL.password_textbox_id), password)

    def click_login(self):
        self.click((By.ID, FL.login_button_id))
        sleep(10)
