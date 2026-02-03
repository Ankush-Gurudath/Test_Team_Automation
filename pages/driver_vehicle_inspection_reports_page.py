from datetime import datetime
from time import sleep

from selenium.common import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By

from locators.locators_driver_vehicle_inspection_reports_page import LocatorsDriverVehicleInspectionReportsPage as DV
from pages.base_page import BasePage


class DriverVehicleInspectionReportsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Labels
    def get_total_report_title(self):
        self.wait_for_element_displayed((By.XPATH, DV.total_reports_text_xpath))
        return self.get_text((By.XPATH, DV.total_reports_text_xpath))

    def get_select_groups_filter_title(self):
        self.wait_for_element_displayed((By.XPATH, DV.select_group_filter_text_xpath))
        return self.get_text((By.XPATH, DV.select_group_filter_text_xpath))

    def get_select_date_range_filter_title(self):
        return self.get_text((By.XPATH, DV.select_date_range_text_xpath))

    def get_statuses_filter_title(self):
        return self.get_text((By.XPATH, DV.statuses_filter_text_xpath))

    def get_defects_filter_title(self):
        return self.get_attribute((By.XPATH, DV.defects_filter_text_xpath), "placeholder")

    def get_select_search_filter_title(self):
        return self.get_text((By.XPATH, DV.select_search_filter_text_xpath))

    def get_select_search_criteria_filter_title(self):
        self.wait_for_element_displayed((By.XPATH, DV.select_search_criteria_filter_text_xpath))
        return self.get_text((By.XPATH, DV.select_search_criteria_filter_text_xpath))

    def get_reset_button_title(self):
        return self.get_text((By.XPATH, DV.reset_button_text_xpath))

    def get_report_Id_title(self):
        return self.get_text((By.XPATH, DV.report_Id_text_xpath))

    def get_type_title(self):
        return self.get_text((By.XPATH, DV.type_text_xpath))

    def get_status_title(self):
        return self.get_text((By.XPATH, DV.status_text_xpath))

    def get_report_date_title(self):
        return self.get_text((By.XPATH, DV.report_date_text_xpath))

    def get_duration_title(self):
        return self.get_text((By.XPATH, DV.duration_text_xpath))

    def get_driver_title(self):
        return self.get_text((By.XPATH, DV.driver_text_xpath))

    def get_vehicle_title(self):
        return self.get_text((By.XPATH, DV.vehicle_text_xpath))

    def get_major_vehicle_defects_title(self):
        return self.get_text((By.XPATH, DV.major_vehicle_defects_text_xpath))

    def get_minor_vehicle_defects_title(self):
        return self.get_text((By.XPATH, DV.minor_vehicle_defects_text_xpath))

    def get_vehicle_inspection_list_title(self):
        self.wait_for_element_displayed((By.XPATH, DV.vehicle_inspection_list_text_xpath))
        return self.get_text((By.XPATH, DV.vehicle_inspection_list_text_xpath))

    def get_trailer_title(self):
        return self.get_text((By.XPATH, DV.trailer_text_xpath))

    def get_major_trailer_defects_title(self):
        return self.get_text((By.XPATH, DV.major_trailers_defects_text_xpath))

    def get_minor_trailers_defects_title(self):
        return self.get_text((By.XPATH, DV.minor_trailers_defects_text_xpath))

    def get_trailer_inspection_list_title(self):
        return self.get_text((By.XPATH, DV.trailer_inspection_list_text_xpath))

    def get_mechanic_agent_title(self):
        return self.get_text((By.XPATH, DV.mechanic_agent_text_xpath))

    def get_reviewer_title(self):
        return self.get_text((By.XPATH, DV.reviewer_text_xpath))

    def click_statuses_filter(self):
        self.click((By.XPATH, DV.statuses_filter_text_xpath))

    def click_first_statuses(self):
        self.click((By.XPATH, DV.status_filter_dropdown_xpath))

    def click_date_filter(self):
        self.click((By.XPATH, DV.select_date_range_text_xpath))

    def click_first_date(self):
        self.click((By.XPATH, DV.select_date_filter_date1_xpath))

    def click_second_date(self):
        self.click((By.XPATH, DV.select_date_filter_date2_xpath))

    def click_date_apply_button(self):
        self.click((By.XPATH, DV.date_filter_apply_button_xpath))

    def click_group_filter(self):
        self.click((By.XPATH, DV.select_group_filter_text_xpath))

    def search_group_filter(self, searched_group):
        self.type((By.XPATH, DV.search_group_textbox_xpath), searched_group)

    def click_searched_group(self):
        self.click((By.XPATH, DV.select_searched_group_xpath))

    def click_group_done_button(self):
        self.click((By.XPATH, DV.group_filter_done_button_xpath))

    def click_defect_filter(self):
        self.click((By.XPATH, DV.defects_filter_xpath))

    def click_first_defects(self):
        self.click((By.XPATH, DV.select_defect_filter_dropdown_xpath))

    def click_search_filter(self):
        self.click((By.XPATH, DV.select_search_filter_text_xpath))

    def click_first_search_filter(self):
        self.click((By.XPATH, DV.select_search_dropdown_xpath))

    def clear_search_dvir_id(self):
        self.clear((By.XPATH, DV.search_criteria_filter_textbox_xpath))

    def search_criteria_filter(self, searched_name):
        self.type((By.XPATH, DV.search_criteria_filter_textbox_xpath), searched_name)

    def click_reset_button(self):
        self.click((By.XPATH, DV.reset_button_text_xpath))

    def click_list_settings_tab(self):
        self.click((By.XPATH, DV.list_settings_tab_xpath))

    def click_list_settings_existing_user_tab(self):
        self.click((By.XPATH, DV.list_setting_tab_existing_user_xpath))

    def click_list_management_tab_existing_user(self):
        try:
            self.click((By.XPATH, DV.list_management_tab_existing_user_xpath))
        except (ElementClickInterceptedException, TimeoutException):
            self.click_list_settings_existing_user_tab()
            self.click((By.XPATH, DV.list_management_tab_existing_user_xpath))

    def click_list_management_tab(self):
        self.click((By.XPATH, DV.list_management_tab_xpath))

    def click_list_assignment_tab(self):
        self.click((By.XPATH, DV.list_assignment_tab_xpath))

    def click_download_csv_report(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.click((By.XPATH, DV.download_csv_button_xpath))
        # wait for download complete
        sleep(20)

    def get_current_month_year(self):
        self.click((By.XPATH, DV.select_date_range_text_xpath))
        return self.get_text((By.XPATH, DV.current_month_year_xpath))

    def get_current_day(self):
        return self.get_text((By.CLASS_NAME, DV.current_day_class))

    def get_dvir_report_file_name(self):
        date_now_text = self.get_current_month_year() + ' ' + self.get_current_day()
        date_now = datetime.strptime(date_now_text, "%B %Y %d").strftime("%Y-%m-%d")

        file_name = 'Dvir Full DVIR List' + ' ' + date_now + '.csv'
        return file_name

    def click_schedules_tab(self):
        self.click((By.XPATH, DV.schedules_tab_xpath))

    def click_assignment_tab_existing_user(self):
        self.click((By.XPATH, DV.list_assignment_tab_existing_user_xpath))

    def click_assignment_tab_existing_user_new_ui(self):
        try:
            self.click((By.XPATH, DV.list_assignment_tab_existing_user_new_ui_xpath))
        except (ElementClickInterceptedException, TimeoutException):
            self.click_list_settings_existing_user_tab()
            self.click((By.XPATH, DV.list_assignment_tab_existing_user_new_ui_xpath))

    def click_dvir_tab(self):
        self.click((By.XPATH, DV.dvir_tab_xpath))

    def click_dvir_tab_new_ui(self):
        self.click((By.XPATH, DV.dvir_tab_new_ui_xpath))

    def click_first_report_id_link(self):
        self.wait_for_element_is_clickable((By.XPATH, DV.first_report_id_link_xpath))
        self.click((By.XPATH, DV.first_report_id_link_xpath))

    def click_select_search_report_id(self):
        self.click((By.XPATH, DV.select_search_dropdown_report_id_xpath))
        sleep(3)

    def click_first_report_id_searched_link(self):
        self.wait_for_element_is_clickable((By.XPATH, DV.first_report_id_searched_xpath))
        self.click((By.XPATH, DV.first_report_id_searched_xpath))

    def get_first_status_text(self):
        return self.get_text((By.XPATH, DV.first_row_status_text_xpath))

    def get_first_driver_text(self):
        return self.get_text((By.XPATH, DV.first_row_driver_text_xpath))

    def get_total_page_count(self):
        page_count = int(
            "".join(list(filter(str.isdigit, self.get_text((By.XPATH, DV.total_reports_page_count_xpath))))))
        return page_count

    def total_reports_top_count(self):
        self.wait_till_element_disappear((By.XPATH, DV.loading_icon_xpath))
        return self.wait_for_expected_number((By.XPATH, DV.top_total_count_reports_xpath))

    def close_defect_filter(self):
        self.wait_for_element_is_clickable((By.XPATH, DV.first_report_id_link_xpath))
        self.click((By.XPATH, DV.close_icon_defect_filter_xpath))

    def dvir_tab_new_ui_is_displayed(self):
        return self.element_is_displayed((By.XPATH, DV.dvir_tab_new_ui_xpath))

    def schedules_tab_new_ui_is_displayed(self):
        return self.element_is_displayed((By.XPATH, DV.schedules_tab_xpath))

    def list_settings_tab_new_ui_is_displayed(self):
        return self.element_is_displayed((By.XPATH, DV.list_setting_tab_existing_user_xpath))

    def list_management_tab_existing_user_is_displayed(self):
        return self.element_is_displayed((By.XPATH, DV.list_management_tab_existing_user_xpath))

    def assignment_tab_existing_user_is_displayed(self):
        return self.element_is_displayed((By.XPATH, DV.list_assignment_tab_existing_user_new_ui_xpath))
