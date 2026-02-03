from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from locators.locators_geotab_page_add_ins import LocatorsGeotabPageAddInsPage as GP
from pages.base_page import BasePage


class GeotabPageAddIns(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_username(self, username):
        self.wait_for_page_to_fully_load()
        locator = (By.ID, GP.username_textbox_id)
        self.wait_for_element_displayed(locator)
        self.click(locator)
        self.type(locator, username)
        self.click((By.ID, GP.next_button_id))

    def enter_password(self, password):
        self.click((By.XPATH, GP.password_textbox_xpath))
        self.type((By.XPATH, GP.password_textbox_xpath), password)

    def click_login(self):
        self.click((By.XPATH, GP.login_button_xpath))

    def dashboard_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, GP.dashboard_xpath))

    def company_logo_is_displayed(self):
        self.wait_for_page_to_fully_load()
        return self.wait_for_element_displayed((By.XPATH, GP.company_logo_xpath))

    def compliance_data_summary_is_displayed(self):
        try:
            self.element_is_displayed((By.XPATH, GP.map_page_show_addin_icon_xpath))
            self.click((By.XPATH, GP.map_page_show_addin_icon_xpath))
            return self.wait_for_element_displayed((By.XPATH, GP.compliance_data_summary_tab_xpath))
        except TimeoutException:
            return self.wait_for_element_displayed((By.XPATH, GP.compliance_data_summary_tab_xpath))

    def click_map_menu(self):
        self.click((By.XPATH, GP.map_menu_xpath))

    def product_guide_header_is_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, GP.product_guide_header_xpath))

    def search_and_click_addin(self, addin_name):
        self.click((By.XPATH, GP.search_textbox_xpath))
        self.clear((By.XPATH, GP.search_textbox_xpath))
        self.type((By.XPATH, GP.search_textbox_xpath), addin_name)
        if addin_name == "fbt":
            self.click((By.XPATH, GP.fbt_result_in_search_xpath))
        elif addin_name == "hos driver summary":
            self.click((By.XPATH, GP.hos_driver_summary_result_in_search_xpath))
        elif addin_name == "import hos logs":
            self.click((By.XPATH, GP.import_hos_logs_result_in_search_xpath))
        elif addin_name == "eld support":
            self.click((By.XPATH, GP.eld_support_result_in_search_xpath))
        elif addin_name == "eld settings validator":
            self.click((By.XPATH, GP.eld_settings_validator_result_in_search_xpath))
        elif addin_name == "ev suitability assessment":
            self.click((By.XPATH, GP.evsa_result_in_search_xpath))
            self.clear((By.XPATH, GP.search_textbox_xpath))
        else:
            raise ValueError(f"Unknown add-in name: {addin_name}")

    def verify_addins_page(self, addin_name):
        headers = {
            "fbt": GP.fbt_page_header_xpath,
            "hos driver summary": GP.hos_driver_summary_page_header_xpath,
            "import hos logs": GP.import_hos_logs_page_header_xpath,
            "eld support": GP.eld_support_page_header_xpath,
            "eld settings validator": GP.eld_settings_validator_page_header_xpath,
            "ev suitability assessment": GP.evsa_page_header_xpath
        }
        if addin_name in headers:
            return self.wait_for_element_displayed((By.XPATH, headers[addin_name]))
        else:
            raise ValueError(f"Unknown add-in name: {addin_name}")
