import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from locators.locators_location_page import LocatorsLocationPage as LLP
from locators.locators_navigation_menu import LocatorsNavigationMenu as LNM
from locators.locators_vehicle_page import LocatorsVehiclePage as LVP
from pages.base_page import BasePage
import csv
import os

class LocationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_location_nav_menu(self):
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        self.click((By.XPATH, LLP.location_menu_icon))
        self.wait_for_element_displayed((By.XPATH, LLP.highlighted_location_menu_icon))
        self.element_is_displayed((By.XPATH, LLP.highlighted_location_menu_icon))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))

    def get_location_page_title(self):
        self.element_is_displayed((By.XPATH, LNM.page_title))
        return self.get_text((By.XPATH, LNM.page_title)).strip()

    def click_add_location_btn(self):
        self.click((By.XPATH, LLP.add_location_btn))

    def click_location_edit_button(self):
        self.wait_for_element_is_clickable((By.XPATH, LLP.first_location_edit_btn))
        self.click((By.XPATH, LLP.first_location_edit_btn))

    def validate_location_name(self):
        return self.get_text((By.XPATH, LLP.recent_location_name)).strip()

    def validate_location_address_info(self):
        return self.get_text((By.XPATH, LLP.recent_location_address)).strip()

    def validate_contact_info(self):
        contact = ''
        contact += self.get_text((By.XPATH, LLP.recent_contact_name)).strip()
        contact += ' '
        contact += self.get_text((By.XPATH, LLP.recent_contact_no)).strip()
        return contact

    def get_pop_up_title(self):
        self.element_is_displayed((By.XPATH, LLP.add_location_pop_title))
        return self.get_text((By.XPATH, LLP.add_location_pop_title)).strip()

    def click_on_country_dropdown(self):
        self.click((By.XPATH, LLP.country_dropdown))

    def validate_countries_visible(self):
        countries = []
        countries_object = self.find_elements((By.XPATH, LLP.all_country))
        for country in countries_object:
            countries.append(country.text)
        return countries

    def get_location_lbl(self):
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        text = self.get_text((By.XPATH, LLP.location_name)).split('\n')
        return text[0]

    def get_email_lbl(self):
        text = self.get_text((By.XPATH, LLP.email_name)).split('\n')
        return text[0]

    def get_first_name_lbl(self):
        text = self.get_text((By.XPATH, LLP.first_name)).split('\n')
        return text[0]

    def get_last_name_lbl(self):
        text = self.get_text((By.XPATH, LLP.last_name)).split('\n')
        return text[0]

    def get_phone_no_lbl(self):
        text = self.get_text((By.XPATH, LLP.phone_no)).split('\n')
        return text[0]

    def get_country_lbl(self):
        text = self.get_text((By.XPATH, LLP.country)).split('\n')
        return text[0]

    def get_address_lbl(self):
        text = self.get_text((By.XPATH, LLP.address)).split('\n')
        return text[1]

    def get_address_2_lbl(self):
        text = self.get_text((By.XPATH, LLP.address_2)).split('\n')
        return text[0]

    def get_city_lbl(self):
        text = self.get_text((By.XPATH, LLP.city)).split('\n')
        return text[0]

    def get_state_lbl(self):
        text = self.get_text((By.XPATH, LLP.state)).split('\n')
        return text[0]

    def get_postal_code_lbl(self):
        text = self.get_text((By.XPATH, LLP.postal_code)).split('\n')
        return text[0]

    def get_cancel_lbl(self):
        text = self.get_text((By.XPATH, LLP.cancel_btn)).split('\n')
        return text[0]

    def get_inactive_save_btn_lbl(self):
        text = self.get_text((By.XPATH, LLP.inactive_save_btn)).split('\n')
        return text[0]

    def get_inactive_toggle_lbl(self):
        text = self.get_text((By.XPATH, LLP.inactive_toggle_off)).split('\n')
        return text[0]

    def get_active_toggle_lbl(self):
        text = self.get_text((By.XPATH, LLP.active_toggle_on)).split('\n')
        return text[0]

    def get_location_ph(self):
        return self.get_attribute((By.XPATH, LLP.location_txt_box), 'placeholder').strip()

    def get_email_ph(self):
        return self.get_attribute((By.XPATH, LLP.email_txt_box), 'placeholder').strip()

    def get_first_name_ph(self):
        return self.get_attribute((By.XPATH, LLP.first_name_txt_box), 'placeholder').strip()

    def get_last_name_ph(self):
        return self.get_attribute((By.XPATH, LLP.last_txt_box), 'placeholder').strip()

    def get_phone_no_ph(self):
        return self.get_attribute((By.XPATH, LLP.phone_no_txt_box), 'placeholder').strip()

    def get_country_option_ph(self):
        return self.get_text((By.XPATH, LLP.country_ph)).strip()

    def get_address_ph(self):
        return self.get_attribute((By.XPATH, LLP.address_txt_box), 'placeholder').strip()

    def get_address_2_ph(self):
        return self.get_attribute((By.XPATH, LLP.address_2_txt_box), 'placeholder').strip()

    def get_city_ph(self):
        return self.get_attribute((By.XPATH, LLP.city_txt_box), 'placeholder').strip()

    def get_state_ph(self):
        return self.get_attribute((By.XPATH, LLP.state_txt_box), 'placeholder')

    def get_postal_code_ph(self):
        return self.get_attribute((By.XPATH, LLP.postal_code_txt_box), 'placeholder')

    def select_usa_country(self):
        try:
            self.find((By.XPATH, LLP.usa_country))
            self.click((By.XPATH, LLP.usa_country))
            self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        except NoSuchElementException:
            self.click((By.XPATH, LLP.country_dropdown))
            self.click((By.XPATH, LLP.usa_country))
            self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))

    def select_canada_country(self):
        try:
            self.find((By.XPATH, LLP.canada_country))
            self.click((By.XPATH, LLP.canada_country))
            self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        except NoSuchElementException:
            self.click((By.XPATH, LLP.country_dropdown))
            self.click((By.XPATH, LLP.canada_country))
            self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))

    def set_location_name(self):
        random_location_name = self.get_random_name(10)
        self.type((By.XPATH, LLP.location_txt_box), random_location_name)
        return random_location_name

    def set_email(self, email):
        self.type((By.XPATH, LLP.email_txt_box), email)

    def set_first_name(self, email):
        self.type((By.XPATH, LLP.first_name_txt_box), email)

    def set_last_name(self, email):
        self.type((By.XPATH, LLP.last_txt_box), email)

    def set_phone(self, email):
        self.type((By.XPATH, LLP.phone_no_txt_box), email)

    def set_address(self, email):
        self.type((By.XPATH, LLP.address_txt_box), email)

    def set_address2(self, email):
        self.type((By.XPATH, LLP.address_2_txt_box), email)

    def set_city(self, email):
        self.type((By.XPATH, LLP.city_txt_box), email)

    def select_state(self, state):
        self.click((By.XPATH, LLP.state_dropdown))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        self.click((By.XPATH, "//select[@name='state']//option[contains(text(),' " + state + " ')]"))

    def set_postal_code(self, email):
        self.type((By.XPATH, LLP.postal_code_txt_box), email)

    def click_save_btn(self):
        self.click((By.XPATH, LLP.active_save_btn))

    def click_yes_btn_popup(self):
        self.click((By.XPATH, LLP.yes_btn_popup))

    def validate_success_notify_msg(self):
        return self.get_text((By.XPATH, LLP.success_notifi_txt)).strip()

    def validate_success_notify_icon(self):
        time.sleep(2)
        return self.get_text((By.XPATH, LLP.success_notifi_icon)).strip()

    def validate_success_notify_cross_icon(self):
        return self.get_text((By.XPATH, LLP.success_notifi_cross_icon)).strip()

    def validate_location_name_edit_popup(self):
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        return self.get_attribute((By.XPATH, LLP.location_txt_box), 'value').strip()

    def validate_email_edit_popup(self):
        return self.get_attribute((By.XPATH, LLP.email_txt_box), 'value').strip()

    def validate_first_name_edit_popup(self):
        return self.get_attribute((By.XPATH, LLP.first_name_txt_box), 'value').strip()

    def validate_last_name_edit_popup(self):
        return self.get_attribute((By.XPATH, LLP.last_txt_box), 'value').strip()

    def validate_country_edit_popup(self):
        return self.get_attribute((By.XPATH, LLP.country_dropdown), 'value').strip()

    def validate_address_edit_popup(self):
        return self.get_attribute((By.XPATH, LLP.address_txt_box), 'value').strip()

    def validate_address2_edit_popup(self):
        return self.get_attribute((By.XPATH, LLP.address_2_txt_box), 'value').strip()

    def validate_city_edit_popup(self):
        return self.get_attribute((By.XPATH, LLP.city_txt_box), 'value').strip()

    def validate_state_edit_popup(self):
        return self.get_attribute((By.XPATH, LLP.state_dropdown), 'value').strip()

    def validate_postal_code_edit_popup(self):
        return self.get_attribute((By.XPATH, LLP.postal_code_txt_box), 'value').strip()

    def validate_active_status(self):
        return self.get_attribute((By.XPATH, LLP.recent_active_toggle), 'value').strip()

    def close_popup(self):
        self.click((By.XPATH, LLP.cross_icon_pop_up))

    def click_welcome_popup(self):
        self.wait_for_element_is_clickable((By.XPATH, LLP.welcome_popup))
        self.click((By.XPATH, LLP.welcome_popup))

    def validate_welcome_popup_logo(self):
        self.wait_for_element_displayed((By.XPATH, LLP.welcome_popup_logo))
        return self.element_is_displayed((By.XPATH, LLP.welcome_popup_logo))

    def open_support_center(self):
        self.click((By.XPATH, LLP.support_center))

    def validate_welcome_popup_title(self):
        return self.get_text((By.XPATH, LLP.welcome_popup_title)).strip()

    def validate_welcome_popup_info(self):
        return self.get_text((By.XPATH, LLP.welcome_popup_content)).strip()

    def validate_welcome_last_popup_info(self):
        return self.get_text((By.XPATH, LLP.welcome_last_popup_content)).strip()

    def validate_welcome_last_popup_info_bold(self):
        return self.get_text((By.XPATH, LLP.welcome_last_popup_content_bold)).strip()

    def validate_steps_info(self):
        return self.get_text((By.XPATH, LLP.welcome_page_steps_info)).strip()

    def validate_step1(self):
        return self.get_text((By.XPATH, LLP.welcome_page_step1)).strip()

    def validate_step2(self):
        return self.get_text((By.XPATH, LLP.welcome_page_step2)).strip()

    def validate_step3(self):
        return self.get_text((By.XPATH, LLP.welcome_page_step3)).strip()

    def validate_step_heading1(self):
        return self.get_text((By.XPATH, LLP.welcome_page_stepheading1)).strip()

    def validate_step_content1(self):
        return self.get_text((By.XPATH, LLP.welcome_page_step_content1)).strip()

    def validate_step_heading2(self):
        return self.get_text((By.XPATH, LLP.welcome_page_stepheading2)).strip()

    def validate_step_content2(self):
        return self.get_text((By.XPATH, LLP.welcome_page_step_content2)).strip()

    def validate_step_heading3(self):
        return self.get_text((By.XPATH, LLP.welcome_page_stepheading3)).strip()

    def validate_step_content3(self):
        return self.get_text((By.XPATH, LLP.welcome_page_step_content3)).strip()

    def validate_support_center(self):
        self.switch_to_first_tab(1)
        self.wait_till_element_disappear((By.XPATH, LLP.supp_center_loader))
        text = self.get_text((By.XPATH, LLP.support_center_logo_txt))
        self.driver.close()
        return text

    def validate_get_started_btn(self):
        return self.get_text((By.XPATH, LLP.welcome_primary_btn)).strip()

    def validate_primary_btn(self):
        return self.get_text((By.XPATH, LLP.welcome_primary_btn)).strip()

    def validate_secondary_btn(self):
        return self.get_text((By.XPATH, LLP.welcome_secondary_btn)).strip()

    def click_get_started(self):
        self.click((By.XPATH, LLP.welcome_primary_btn))

    def click_next_btn(self):
        self.click((By.XPATH, LLP.welcome_primary_btn))

    def click_done_btn(self):
        self.click((By.XPATH, LLP.welcome_primary_btn))

    def click_ok_btn(self):
        self.click((By.XPATH, LLP.welcome_primary_btn))

    def click_close_popup_btn(self):
        self.click((By.XPATH, LLP.welcome_popup_close_btn))

    def set_search_text(self, search_txt):
        self.type((By.XPATH, LLP.search_txt_box), search_txt)
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))

    def validate_search_result_name(self, location_name):
        records = self.find_elements((By.XPATH, LLP.table_result))
        first_record_txt = records[0].text
        return first_record_txt.startswith(location_name)

    def validate_search_result_count(self):
        records = self.find_elements((By.XPATH, LLP.table_result))
        return len(records)

    def clear_search_tx(self):
        self.clear((By.XPATH, LLP.search_txt_box))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))

    def clear_filters(self):
        self.click((By.XPATH, LVP.clear_all_btn))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))

    def download_location_template(self):
        self.click((By.XPATH, LLP.import_location_btn))
        self.wait_for_element_is_clickable((By.XPATH, LVP.download_template_btn))
        dir_list_before_download = os.listdir(os.path.join(os.path.expanduser('~'), 'Downloads'))
        self.click((By.XPATH, LVP.download_template_btn))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        dir_list_after_download = os.listdir(os.path.join(os.path.expanduser('~'), 'Downloads'))
        downloaded_file = set(dir_list_after_download) - set(dir_list_before_download)
        downloaded_file_name = list(downloaded_file)[0]
        return downloaded_file_name

    def validate_file_header(self, file_name):
        file_path = os.path.join(os.path.expanduser('~'), 'Downloads', file_name)
        with open(file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            headers = next(csv_reader)
        return headers

    def create_locations_in_template(self, file_name, headers, location_data, records):
        file_path = os.path.join(os.path.expanduser('~'), 'Downloads', file_name)
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file:
            field_names = headers
            writer = csv.DictWriter(csv_file, fieldnames=field_names)
            writer.writeheader()
            for i in range(records):
                location_name = 'Location ' + self.get_random_name(10)
                writer.writerow({headers[0]: i,
                                 headers[1]: location_name,
                                 headers[2]: location_data[0],
                                 headers[3]: location_data[1],
                                 headers[4]: location_data[2],
                                 headers[5]: location_data[3],
                                 headers[6]: location_data[4],
                                 headers[7]: location_data[5],
                                 headers[8]: location_data[6],
                                 headers[9]: location_data[7],
                                 headers[10]: location_data[8],
                                 headers[11]: location_data[9],
                                 headers[12]: location_data[10]
                                 })

    def download_records(self):
        dir_list_before_download = os.listdir(os.path.join(os.path.expanduser('~'), 'Downloads'))
        self.click((By.XPATH, LLP.download_location_list))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        dir_list_after_download = os.listdir(os.path.join(os.path.expanduser('~'), 'Downloads'))
        downloaded_file = set(dir_list_after_download) - set(dir_list_before_download)
        downloaded_file_name = list(downloaded_file)[0]
        return downloaded_file_name

    def click_next_page_btn(self):
        self.click((By.XPATH, LLP.pgn_next_btn))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))

    def click_previous_page_btn(self):
        self.click((By.XPATH, LLP.pgn_previous_btn))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))

    def get_page_records(self):
        current_page_records = self.find_elements((By.XPATH, LLP.table_result))
        current_page_records_data = []
        for record in current_page_records:
            current_page_records_data.append(record.text)
        return current_page_records_data

    def validate_new_records(self, first_page_data, second_page_data):
        match_flag = True
        for record_index in range(len(second_page_data)):
            if first_page_data[record_index] != second_page_data[record_index]:
                continue
            else:
                match_flag = False
                break
        return match_flag

    def validate_previous_records(self, first_page_data, second_page_data):
        match_flag = True
        for record_index in range(len(second_page_data)):
            if first_page_data[record_index] == second_page_data[record_index]:
                continue
            else:
                match_flag = False
                break
        return match_flag

    def select_active_filter(self):
        self.click((By.XPATH, LLP.status_filter))
        self.click((By.XPATH, LLP.active_option))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))

    def validate_active_records(self):
        disable_flag = True
        current_page_records_checkbox = self.find_elements((By.XPATH, LLP.table_result_checkbox))
        for checkbox in current_page_records_checkbox:
            if checkbox.is_selected():
                continue
            else:
                disable_flag = False
                break
        return disable_flag

    def select_inactive_filter(self):
        self.click((By.XPATH, LLP.status_filter))
        self.click((By.XPATH, LLP.inactive_option))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))

    def validate_inactive_records(self):
        disable_flag = True
        current_page_records_checkbox = self.find_elements((By.XPATH, LLP.table_result_checkbox))
        for checkbox in current_page_records_checkbox:
            if not checkbox.is_selected():
                continue
            else:
                disable_flag = False
                break
        return disable_flag

    def select_rows(self, records):
        self.click((By.XPATH, LLP.show_rows_dropdown))
        if records == 100:
            self.click((By.XPATH, LLP.rows_100_option))
        elif records == 150:
            self.click((By.XPATH, LLP.rows_150_option))
        elif records == 200:
            self.click((By.XPATH, LLP.rows_200_option))
        elif records == 250:
            self.click((By.XPATH, LLP.rows_250_option))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))

    def validate_records_visible(self):
        current_page_records = self.find_elements((By.XPATH, LLP.table_result))
        return len(current_page_records)

    def upload_template(self, file_name):
        file_path = os.path.join(os.path.expanduser('~'), 'Downloads', file_name)
        self.type((By.XPATH, LVP.import_vehicle), file_path)
        self.wait_for_element_is_clickable((By.XPATH, LVP.next_btn))
        self.click((By.XPATH, LVP.next_btn))
        self.wait_for_element_is_clickable((By.XPATH, LVP.primary_btn))
        self.click((By.XPATH, LVP.primary_btn))
        self.wait_till_element_disappear((By.XPATH, LNM.spinner_icon))
        self.click((By.XPATH, LVP.primary_btn))