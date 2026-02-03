from datetime import datetime
from selenium.webdriver.common.by import By
from locators.locators_consent_report_page import LocatorsConsentReport as CR
from pages.base_page import BasePage


class ConsentReportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_consent_report_tab(self):
        return self.click((By.XPATH, CR.consent_report_tab_xpath))

    def group_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.group_filter_xpath))

    def status_filter_is_displayed(self):
        return self.element_is_displayed((By.ID, CR.status_filter_id))

    def search_name_or_id_is_displayed(self):
        return self.element_is_displayed((By.ID, CR.search_name_or_id_id))

    def reset_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.reset_button_xpath))

    def driver_count_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.driver_count_xpath))

    def facial_id_tab_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.facial_id_tab_xpath))

    def distraction_and_fatigue_detection_tab_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.distraction_and_fatigue_detection_tab_xpath))

    def video_safety_tab_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.video_safety_tab_xpath))

    def click_group_filter_button(self):
        self.click((By.XPATH, CR.group_filter_xpath))

    def click_search_by_group_field(self):
        self.wait_for_element_displayed((By.XPATH, CR.search_by_group_field_xpath))
        self.click((By.XPATH, CR.search_by_group_field_xpath))

    def search_group_filter(self, consent_group_name):
        self.type((By.XPATH, CR.search_by_group_field_xpath), consent_group_name)

    def select_group(self):
        self.click((By.XPATH, CR.select_group_xpath))

    def click_done_button(self):
        self.click((By.XPATH, CR.done_button_xpath))

    def get_first_group_name(self):
        return self.get_text((By.XPATH, CR.first_group_name_xpath))

    def click_status_filter_button(self):
        self.click((By.XPATH, CR.status_filter_xpath))

    def select_not_received_status_button(self):
        self.click((By.XPATH, CR.not_received_status_button_xpath))

    def select_received_status_button(self):
        self.click((By.XPATH, CR.received_status_button_xpath))

    def select_revoked_status_button(self):
        self.click((By.XPATH, CR.revoked_status_button_xpath))

    def select_opted_out_status_button(self):
        self.click((By.XPATH, CR.opted_out_status_button_xpath))

    def not_received_status_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.not_received_status_button_xpath))

    def received_status_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.received_status_button_xpath))

    def revoked_status_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.revoked_status_button_xpath))

    def opted_out_status_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.opted_out_status_button_xpath))

    def type_search_name_field(self, name):
        self.type((By.XPATH, CR.search_name_xpath), name)
        self.wait_for_page_load()

    def get_first_row_driver_name(self):
        self.wait_for_element_displayed((By.XPATH, CR.first_row_driver_name_xpath))
        return self.get_text((By.XPATH, CR.first_row_driver_name_xpath))

    def get_name_column_label(self):
        return self.get_text((By.XPATH, CR.name_column_label_xpath))

    def get_groups_column_label(self):
        return self.get_text((By.XPATH, CR.groups_column_label_xpath))

    def get_status_column_label(self):
        return self.get_text((By.XPATH, CR.status_column_label_xpath))

    def get_sent_date_column_label(self):
        return self.get_text((By.XPATH, CR.sent_date_column_label_xpath))

    def get_received_date_column_label(self):
        return self.get_text((By.XPATH, CR.received_date_column_label_xpath))

    def clear_all_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.clear_all_option_xpath))

    def download_pdf_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.download_pdf_option_xpath))

    def revoke_consent_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.revoke_consent_option_xpath))

    def csv_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.csv_option_xpath))

    def click_csv_option(self):
        self.click((By.XPATH, CR.csv_option_xpath))

    def get_facial_id_file_name(self):
        date_now = datetime.now().strftime("%Y-%m-%d")
        file_name = date_now + '_Facial ID_Consent_Status_Report' + '.csv'
        return file_name
    
    def get_pdf_file_name(self, consent_id):
        file_name = consent_id + '.pdf'
        return file_name

    def click_reset_button(self):
        self.click((By.XPATH, CR.reset_button_xpath))
        self.wait_for_page_load()

    def get_page_title(self):
        return self.get_text((By.XPATH, CR.consent_report_title_xpath))

    def get_first_row_status(self):
        self.wait_for_element_displayed((By.XPATH, CR.get_first_row_status_xpath))
        return self.get_text((By.XPATH, CR.get_first_row_status_xpath))

    def click_download_pdf_option(self):
        self.click((By.XPATH, CR.download_pdf_xpath))

    def click_search_name_field(self):
        self.click((By.XPATH, CR.search_name_xpath))

    def click_last_page_number(self):
        self.click((By.XPATH, CR.last_page_number_xpath))

    def get_last_page_driver_name_text(self):
        self.scroll_page_down()
        return self.get_text((By.XPATH, CR.get_last_page_driver_name_xpath))

    def click_enable_facial_id_link(self):
        self.click((By.XPATH, CR.enable_facial_id_link_xpath))

    def get_user_count_for_selected_group_after_creating_user(self):
        self.wait_for_element_displayed((By.XPATH, CR.user_count_xpath))
        return self.get_text((By.XPATH, CR.user_count_xpath))

    def get_user_count_for_selected_group_after_deleting_user(self):
        self.wait_for_element_displayed((By.XPATH, CR.user_count_xpath))
        return self.get_text((By.XPATH, CR.user_count_xpath))

    def click_enable_product_cancel_button(self):
        self.click((By.ID, CR.enable_product_cancel_button_id))

    def click_save_changes(self):
        self.wait_for_element_displayed((By.XPATH, CR.save_changes_button_xpath))
        self.click((By.XPATH, CR.save_changes_button_xpath))

    def user_count_for_selected_group_after_deleting_user_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CR.user_count_xpath))

    def edit_password(self, password):
        self.clear((By.XPATH, CR.password_textbox_xpath))
        self.type((By.XPATH, CR.password_textbox_xpath), password)