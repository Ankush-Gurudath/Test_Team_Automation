from time import sleep

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.by import By

from locators.locators_my_account_page import LocatorsMyAccount as MA
from pages.base_page import BasePage


class MyAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_first_name_text(self):
        return self.get_text((By.XPATH, MA.first_name_label_xpath))

    def my_account_title_is_displayed(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                if self.element_is_displayed((By.XPATH, MA.my_account_title_xpath)):
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)
        return self.element_is_displayed((By.XPATH, MA.my_account_title_xpath))

    def get_last_name_text(self):
        return self.get_text((By.XPATH, MA.last_name_label_xpath))

    def get_employee_id_text(self):
        return self.get_text((By.XPATH, MA.employee_id_xpath))

    def get_contact_information_text(self):
        return self.get_text((By.XPATH, MA.contact_information_label_xpath))

    def get_email_address_text(self):
        return self.get_text((By.XPATH, MA.email_address_label_xpath))

    def get_cellphone_text(self):
        return self.get_text((By.XPATH, MA.cellphone_label_xpath))

    def get_lytx_badge_text(self):
        return self.get_text((By.XPATH, MA.lytx_badge_xpath))

    def get_group_role_assignment_text(self):
        return self.get_text((By.XPATH, MA.group_role_assignment_label_xpath))

    def get_login_text(self):
        return self.get_text((By.XPATH, MA.login_label_xpath))

    def get_username_text(self):
        return self.get_text((By.XPATH, MA.username_label_xpath))

    def get_password_text(self):
        return self.get_text((By.XPATH, MA.password_label_xpath))

    def click_edit_email_button(self):
        self.click((By.XPATH, MA.edit_email_button_xpath))

    def clear_email_address(self):
        self.clear((By.XPATH, MA.email_address_textbox_xpath))

    def edit_email_address(self, email):
        self.type((By.XPATH, MA.email_address_textbox_xpath), email)

    def click_save_edit_email_button(self):
        self.click((By.XPATH, MA.save_button_xpath))

    def click_report_tab(self):
        self.click((By.XPATH, MA.report_tab_xpath))

    def get_report_subscription_text(self):
        return self.get_text((By.XPATH, MA.report_subscription_text_xpath))

    def click_notification_tab(self):
        self.click((By.XPATH, MA.notification_tab_xpath))

    def notification_subscription_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, MA.notification_subscription_text_xpath))

    def get_updated_email_address_text(self):
        self.element_is_displayed((By.XPATH, MA.edit_email_button_xpath))
        return self.get_text((By.XPATH, MA.updated_email_address_text))
