from selenium.webdriver.common.by import By
from locators.locators_group_page import LocatorsGroupPage as LGP
from locators.locators_vehicle_page import LocatorsVehiclePage as LVP
from locators.locators_navigation_menu import LocatorsNavigationMenu as LNM
from pages.base_page import BasePage
import os

class GroupPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_group_nav_menu(self):
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        self.click((By.XPATH, LGP.nav_menu))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        self.element_is_displayed((By.XPATH, LGP.highlighted_group_menu_icon))

    def get_group_page_title(self):
        self.element_is_displayed((By.XPATH, LGP.page_title))
        return self.get_text((By.XPATH, LGP.page_title)).strip()

    def download_group_template(self):
        dir_list_before_download = os.listdir(os.path.join(os.path.expanduser('~'), 'Downloads'))
        self.wait_for_element_is_clickable((By.XPATH, LGP.download_group_template_btn))
        self.click((By.XPATH, LGP.download_group_template_btn))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        dir_list_while_download = os.listdir(os.path.join(os.path.expanduser('~'), 'Downloads'))
        temp_file = set(dir_list_while_download) - set(dir_list_before_download)
        temp_file_name = list(temp_file)[0]
        self.wait_till_file_downloaded_local(os.path.join(os.path.expanduser('~'), 'Downloads'),temp_file_name)
        dir_list_after_download = os.listdir(os.path.join(os.path.expanduser('~'), 'Downloads'))
        downloaded_file = set(dir_list_after_download) - set(dir_list_before_download)
        downloaded_file_name = list(downloaded_file)[0]
        return downloaded_file_name

    def upload_template(self,file_name):
        file_path = os.path.join(os.path.expanduser('~'), 'Downloads\\',file_name)
        self.type((By.XPATH, LVP.import_vehicle), file_path)
        self.click((By.XPATH, LGP.submit_btn))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))

    def validate_popup_title(self):
        self.wait_for_element_displayed((By.XPATH, LGP.popup_title))
        self.wait_for_element_is_clickable((By.XPATH, LGP.ok_btn))
        return self.get_text((By.XPATH, LGP.popup_title)).strip()

    def validate_popup_description(self):
        return self.get_text((By.XPATH, LGP.popup_desc)).strip()

    def validate_popup_support_center(self):
        self.wait_for_element_displayed((By.XPATH, LGP.popup_supp_center_link))
        return self.get_text((By.XPATH, LGP.popup_supp_center_desc)).strip()

    def validate_popup_acknowledgement(self):
        return self.get_text((By.XPATH, LGP.popup_submission_ack)).strip()

    def close_popup(self):
        self.click((By.XPATH, LGP.ok_btn))

    def validate_file_downloaded(self,file_name):
        dir_list_after_download = os.listdir(os.path.join(os.path.expanduser('~'), 'Downloads'))
        return True if file_name in dir_list_after_download else False