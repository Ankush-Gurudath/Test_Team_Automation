from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By

from locators.locators_login_page import LocatorsLogin as LG
from locators.locators_navigation_menu import LocatorsNavigationMenu as LNM
from pages.base_page import BasePage
from steps.common import DC_URL


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_username(self, username):
        try:
            self.find((By.ID, LG.username_textbox_id))
        except(NoSuchElementException, TimeoutException):
            self.click_refresh_button()
            self.wait_for_page_to_fully_load()
        finally:
            self.type((By.ID, LG.username_textbox_id), username)

    def enter_password(self, password):
        self.type((By.ID, LG.password_textbox_id), password)

    def click_login(self):
        self.click((By.ID, LG.login_button_id))

    def enter_sso_username(self, username):
        self.type((By.ID, LG.sso_username_textbox_id), username)

    def enter_sso_relay_state(self, relaystate):
        self.type((By.ID, LG.sso_relay_state_textbox_id), relaystate)

    def click_sso_single_signon(self):
        self.click((By.XPATH, LG.sso_single_signon_button_xpath))

    def retry_if_login_failed(self, login_page, user_name, password, company_name=None):
        login_success_lytx_logo_xpath = LG.login_success_lytx_logo_xpath
        if login_page == DC_URL:
            login_success_lytx_logo_xpath = LG.login_success_lytx_logo_dc_xpath
        if not self.wait_for_element_displayed((By.XPATH, login_success_lytx_logo_xpath)):
            self.driver.get(login_page)
            self.enter_username(user_name)
            self.enter_password(password)
            self.click_login()
        if self.element_is_displayed((By.ID, LG.company_textbox_id)):
            self.open_company_list()
            self.select_multi_company(company_name)
            self.click_select_company_button()

    def retry_if_login_failed_new_ui(self, login_page, user_name, password, company_name=None):
        login_success_lytx_logo_xpath_new_UI = LG.login_success_lytx_logo_xpath_new_UI
        if login_page == DC_URL:
            login_success_lytx_logo_xpath_new_UI = LG.login_success_lytx_logo_xpath_new_UI
        if not self.wait_for_element_displayed((By.XPATH, login_success_lytx_logo_xpath_new_UI)):
            self.driver.get(login_page)
            self.enter_username(user_name)
            self.enter_password(password)
            self.click_login()
        if self.element_is_displayed((By.ID, LG.company_textbox_id)):
            self.open_company_list()
            self.select_multi_company(company_name)
            self.click_select_company_button()

    def click_humanoid(self):
        self.click_element_ignore_exceptions((By.ID, LG.humanoid_id))

    def click_dc_coach_sign_out(self):
        self.click((By.XPATH, LG.dc_coach_log_out_xpath))

    def click_sign_out_new_ui(self):
        self.click((By.XPATH, LG.sign_out_button_ui_xpath))

    def click_dc_driver_sign_out(self):
        self.click((By.XPATH, LG.dc_driver_log_out_xpath))

    def click_dc_admin_sign_out(self):
        self.click((By.XPATH, LG.dc_admin_log_out_xpath))

    def click_fleet_sign_out(self):
        self.click((By.XPATH, LG.fleet_log_out_xpath))

    def click_dvir_sign_out(self):
        self.click((By.XPATH, LG.dvir_log_out_xpath))

    def get_login_page(self):
        return self.get_text((By.ID, LG.login_button_id))

    def click_my_account_button(self):
        self.click((By.XPATH, LG.my_account_button_xpath))

    def lytx_logo_is_displayed(self):
        return self.element_is_displayed((By.XPATH, LG.lytx_logo_xpath))

    def lytx_logo_new_ui_is_displayed(self):
        self.wait_for_element_displayed((By.XPATH, LG.lytx_logo_new_ui_xpath))
        return self.element_is_displayed((By.XPATH, LG.lytx_logo_new_ui_xpath))

    def open_company_list(self):
        self.click((By.ID, LG.company_textbox_id))

    def select_company(self):
        self.click((By.XPATH, LG.selected_company_xpath))

    def select_multi_company(self, company_name):
        self.type((By.ID, LG.company_textbox_id), company_name)
        self.click((By.XPATH, LG.selected_company_xpath))

    def click_select_company_button(self):
        self.click((By.ID, LG.select_company_button_id))

    def click_profile_icon(self):
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        self.click((By.XPATH, LG.profile_icon_implementation_center))

    def click_sign_out_btn(self):
        self.wait_for_element_is_clickable((By.XPATH, LG.sign_out_btn_implementation_center))
        self.click((By.XPATH, LG.sign_out_btn_implementation_center))

    def click_sign_out_button_newui(self):
        self.wait_for_element_is_clickable((By.XPATH, LG.sign_out_button_xpath))
        self.click((By.XPATH, LG.sign_out_button_xpath))

    def click_fleet_sign_out_btn(self):
        self.wait_for_element_is_clickable((By.XPATH, LG.sign_out_btn_fleet))
        self.click((By.XPATH, LG.sign_out_btn_fleet))

    def get_sso_login_unsuccessful_text(self):
        return self.get_text((By.XPATH, LG.sso_login_unsuccessful_xpath))

    def click_profile_btn(self):
        self.wait_for_element_is_clickable((By.ID, LG.profile_button_id))
        self.click((By.ID, LG.profile_button_id))

    def click_log_out_btn(self):
        self.wait_for_element_is_clickable((By.XPATH, LG.log_out_btn))
        self.click((By.XPATH, LG.log_out_btn))

    def select_account(self,account_name):
        self.wait_till_element_disappear((By.ID, LG.login_button_id))
        self.wait_for_element_displayed((By.XPATH, LNM.spinner_icon))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        self.click((By.XPATH,LG.account_dropdown ))
        self.wait_for_element_displayed((By.XPATH, '//div[@role="listbox"]//span[contains(text(),"'+account_name+'")]'))
        self.click((By.XPATH, '//div[@role="listbox"]//span[contains(text(),"'+account_name+'")]'))
        self.click((By.XPATH, LG.select_account_btn))