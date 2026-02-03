from random import randint
from time import sleep
from selenium.webdriver.common.by import By

from locators.locators_add_user import LocatorsAddUser as AU
from pages.base_page import BasePage


class AddUserPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def add_user_title_is_displayed(self):
        return self.wait_for_element_displayed((By.ID, AU.add_user_title_id))

    def add_first_name(self, random_name):
        self.wait_for_element_displayed((By.XPATH, AU.first_name_textbox_xpath))
        self.type((By.XPATH, AU.first_name_textbox_xpath), random_name)

    def add_last_name(self, lastname):
        self.type((By.XPATH, AU.last_name_textbox_xpath), lastname)

    def add_employee_id(self, employeeid):
        self.type((By.XPATH, AU.employee_id_textbox_xpath), employeeid)

    def add_email_address(self, email):
        self.type((By.XPATH, AU.email_address_textbox_xpath), email)

    def add_cell_phone(self):
        random_digits = randint(100000, 999999)
        prefix = 4352
        # Combine the prefix with the random digits
        phone_number = f"{prefix}{random_digits}"
        self.type((By.XPATH, AU.cell_phone_textbox_xpath), phone_number)
        while self.element_is_displayed((By.XPATH, AU.cellphone_already_exists_error_xpath)) or self.element_is_displayed((By.XPATH, AU.Invalid_cell_phone_number)):
            self.find((By.XPATH, AU.cell_phone_textbox_xpath)).clear()
            random_digit = randint(100000, 999999)
            phone_number = f"{prefix}{random_digit}"
            self.find((By.XPATH, AU.cell_phone_textbox_xpath)).send_keys(phone_number)
            sleep(1)

    def click_login_enabled(self, value):
        self.scroll_page_down()
        self.wait_for_expected_text((By.XPATH, AU.login_enabled_checkbox_xpath), value)
        self.click((By.XPATH, AU.login_enabled_checkbox_xpath))
        self.scroll_page_down()

    def add_user_name(self, username):
        self.type((By.XPATH, AU.user_name_textbox_xpath), username)
        i = 0
        while self.element_is_displayed((By.XPATH, AU.login_username_error_xpath)):
            self.find((By.XPATH, AU.user_name_textbox_xpath)).send_keys(i)
            i += 1
            sleep(1)

    def add_password(self, password):
        self.type((By.XPATH, AU.password_textbox_xpath), password)

    def click_group(self):
        self.scroll_page_down()
        self.click((By.XPATH, AU.group_selector_xpath))

    def search_group(self, group_role):
        self.type((By.XPATH, AU.search_group_textbox_xpath), group_role)

    def select_group(self):
        self.click((By.XPATH, AU.select_searched_group_button_xpath))

    def click_group_done(self):
        self.click((By.XPATH, AU.group_done_button_xpath))

    def click_select_role(self):
        self.click((By.XPATH, AU.select_role_button_xpath))

    def click_coach_role(self):
        self.click((By.XPATH, AU.coach_role_button_xpath))

    def click_create_user(self):
        self.click_element_ignore_exceptions((By.ID, AU.create_button_id))
        i = 0
        while self.element_is_displayed((By.XPATH, AU.login_username_error_xpath)):
            self.find((By.XPATH, AU.user_name_textbox_xpath)).send_keys(i)
            i += 1
            sleep(1)
            self.click_element_ignore_exceptions((By.ID, AU.create_button_id))
        self.wait_till_element_disappear((By.XPATH, AU.user_created_success_message_xpath))
        self.wait_for_page_load()

    def click_driver_role(self):
        self.click((By.XPATH, AU.driver_role_button_xpath))

    def get_lytx_badge_message(self):
        return self.get_text((By.XPATH, AU.lytx_badge_message_xpath))

    def click_cancel_button(self):
        self.scroll_page_down()
        self.click((By.XPATH, AU.cancel_button_xpath))
