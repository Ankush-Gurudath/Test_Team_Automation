from time import sleep

from selenium.webdriver.common.by import By

from locators.locators_inspection_report import LocatorsInspectionReportPage as IR
from pages.base_page import BasePage


class InspectionReportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Labels
    def get_inspection_report_title(self):
        return self.get_text((By.XPATH, IR.inspection_report_title_xpath))

    def get_report_id_title(self):
        return self.get_text((By.XPATH, IR.report_id_title_xpath))

    def get_inspection_type_title(self):
        return self.get_text((By.XPATH, IR.inspection_type_title_xpath))

    def get_driver_title(self):
        return self.get_text((By.XPATH, IR.driver_title_xpath))

    def get_report_date_title(self):
        return self.get_text((By.XPATH, IR.report_date_title_xpath))

    def get_status_title(self):
        return self.get_text((By.XPATH, IR.status_title_xpath))

    def get_location_title(self):
        return self.get_text((By.XPATH, IR.location_title_xpath))

    def get_license_plate_title_int(self):
        return self.get_text((By.XPATH, IR.license_plate_title_int_xpath))

    def get_license_plate_title_stg(self):
        return self.get_text((By.XPATH, IR.license_plate_title_stg_xpath))

    def get_odometer_title(self):
        return self.get_text((By.XPATH, IR.odometer_title_xpath))

    def get_driver_signature_name_title(self):
        return self.get_text((By.XPATH, IR.driver_signature_name_title_xpath))

    def get_mechanic_signature_title(self):
        return self.get_text((By.XPATH, IR.mechanic_signature_title_xpath))

    def click_add_notes_button(self):
        element = self.find((By.XPATH, IR.add_notes_button_xpath))
        self.scroll_to_element(element)
        self.click((By.XPATH, IR.add_notes_button_xpath))

    def send_notes_text(self, notes):
        self.type((By.XPATH, IR.notes_textbox_xpath), notes)

    def click_add_notes_save_button(self):
        self.click((By.XPATH, IR.save_notes_button_xpath))

    def get_added_notes_text(self):
        return self.get_text((By.XPATH, IR.added_note_text_xpath))

    def click_keboo_button(self):
        self.click((By.XPATH, IR.keboo_button_xpath))

    def get_edit_button_text(self):
        return self.get_text((By.XPATH, IR.edit_dropdown_xpath))

    def get_delete_button_text(self):
        return self.get_text((By.XPATH, IR.delete_dropdown_xpath))

    def click_edit_button(self):
        self.wait_for_element_is_clickable((By.XPATH, IR.edit_dropdown_xpath))
        self.click((By.XPATH, IR.edit_dropdown_xpath))

    def get_edited_note_text(self):
        return self.get_text((By.XPATH, IR.note_edit_textbox_xpath))

    def clear_added_notes(self):
        self.clear((By.XPATH, IR.notes_textbox_xpath))

    def click_delete_notes_button(self):
        self.wait_for_element_is_clickable((By.XPATH, IR.delete_dropdown_xpath))
        self.click((By.XPATH, IR.delete_dropdown_xpath))

    def scroll_down_to_the_end_of_page(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        sleep(3)

    def keboo_displayed(self):
        return self.wait_for_element_displayed((By.XPATH, IR.keboo_button_xpath))

    def click_back_button(self):
        self.wait_for_element_is_clickable((By.XPATH, IR.back_button_xpath))
        self.click((By.XPATH, IR.back_button_xpath))

    def click_resolve_button(self):
        self.wait_for_element_displayed((By.XPATH, IR.resolve_button_xpath))
        self.click((By.XPATH, IR.resolve_button_xpath))

    def click_repaired_button(self):
        self.wait_for_element_displayed((By.XPATH, IR.repaired_button_xpath))
        self.click((By.XPATH, IR.repaired_button_xpath))

    def click_no_repair_needed_button(self):
        self.wait_for_element_displayed((By.XPATH, IR.no_repair_needed_button_xpath))
        self.click((By.XPATH, IR.no_repair_needed_button_xpath))

    def get_repaired_text(self):
        return self.get_text((By.XPATH, IR.repaired_text_xpath))

    def get_reopen_text(self):
        return self.get_text((By.XPATH, IR.reopen_text_xpath))

    def get_no_repair_needed_text(self):
        return self.get_text((By.XPATH, IR.no_repair_needed_text_xpath))

    def click_reopen_button(self):
        self.click((By.XPATH, IR.reopen_text_xpath))

    def get_resolve_text(self):
        return self.get_text((By.XPATH, IR.resolve_button_xpath))
