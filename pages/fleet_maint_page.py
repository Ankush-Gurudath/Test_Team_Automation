from time import sleep

from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException
from selenium.webdriver.common.by import By

from locators.locators_fleet_maint_page import LocatorsFleetMaint as FML
from pages.base_page import BasePage


class FleetMaintPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_apply_button(self):
        self.click((By.ID, FML.apply_button_id))

    # Labels
    def get_fleet_tracking_title(self):
        return self.get_text((By.ID, FML.fleet_tracking_title_id))

    def get_preventative_maintenance_title(self):
        return self.get_text((By.XPATH, FML.preventative_maintenance_title_xpath))

    def get_upcoming_services_tab_title(self):
        return self.get_text((By.XPATH, FML.pm_upcoming_service_xpath))

    def click_upcoming_services_tab(self):
        self.click((By.XPATH, FML.pm_upcoming_service_xpath))

    def get_history_tab_title(self):
        return self.get_text((By.XPATH, FML.pm_history_xpath))

    def get_manage_services_title(self):
        return self.get_text((By.XPATH, FML.maint_manage_services_xpath))

    # Maintenance
    def click_maintenance(self):
        i = 0
        while i < 5:
            i += 1
            try:
                self.click((By.XPATH, FML.maintenance_xpath))
                break
            except (StaleElementReferenceException, ElementClickInterceptedException):
                sleep(4)

        if i >= 5:
            self.click((By.XPATH, FML.maintenance_xpath))

    def click_maintenance_new_ui(self):
        i = 0
        while i < 5:
            i += 1
            try:
                self.click((By.XPATH, FML.maintenance_new_ui_xpath))
                break
            except (StaleElementReferenceException, ElementClickInterceptedException):
                sleep(4)

        if i >= 5:
            self.click((By.XPATH, FML.maintenance_new_ui_xpath))

    def click_preventative_maintenance(self):
        self.click((By.XPATH, FML.preventative_maintenance_xpath))

    def click_preventative_maintenance_new_ui(self):
        self.click((By.XPATH, FML.preventative_maintenance_new_ui_xpath))

    def click_dtc(self):
        self.click((By.XPATH, FML.dtc_xpath))

    def click_dtc_new_ui(self):
        self.click((By.XPATH, FML.dtc_new_ui_xpath))

    # Maintenance upcoming service
    def go_to_upcoming_service(self):
        self.click((By.XPATH, FML.pm_upcoming_service_xpath))

    def search_vehicle_upcoming_service(self, vehicle_name):
        self.type((By.XPATH, FML.pm_upcoming_service_search_vehicle_xpath), vehicle_name)

    def select_vehicle_upcoming_service(self, vehicle_name):
        i = 0
        while i < 5:
            i += 1
            try:
                if vehicle_name in str(self.get_text((By.XPATH, FML.pm_upcoming_service_select_vehicle_xpath))):
                    break

                sleep(5)
            except TimeoutException:
                sleep(1)

        self.click((By.XPATH, FML.pm_upcoming_service_select_vehicle_xpath))

    def get_pm_upcoming_service_count(self):
        n = 0
        while n < 5:
            try:
                n += 1
                count = self.get_text((By.XPATH, FML.pm_upcoming_service_count_xpath))
                if count.isdigit():
                    break
                else:
                    sleep(2)
            except (TimeoutException, StaleElementReferenceException):
                sleep(2)

        return self.get_text((By.XPATH, FML.pm_upcoming_service_count_xpath))

    def get_pm_upcoming_service_1st_vehicle(self):
        return self.get_text((By.XPATH, FML.pm_upcoming_service_1st_vehicle_xpath))

    def get_pm_upcoming_service_1st_group(self):
        return self.get_text((By.XPATH, FML.pm_upcoming_service_1st_group_xpath))

    def get_pm_upcoming_service_1st_service(self):
        return self.get_text((By.XPATH, FML.pm_upcoming_service_1st_service_xpath))

    def get_pm_upcoming_service_1st_interval(self):
        return self.get_text((By.XPATH, FML.pm_upcoming_service_1st_interval_xpath))

    def get_pm_upcoming_service_1st_status(self, status):
        self.wait_for_expected_text((By.XPATH, FML.pm_upcoming_service_1st_status_xpath), status)
        return self.get_text((By.XPATH, FML.pm_upcoming_service_1st_status_xpath))

    def get_pm_upcoming_service_1st_action(self):
        return self.get_text((By.XPATH, FML.pm_upcoming_service_1st_action_xpath))

    def click_pm_upcoming_service_1st_action(self):
        self.click((By.XPATH, FML.pm_upcoming_service_1st_action_xpath))

    def click_pm_complete_service_dialog_complete(self):
        self.wait_for_element_is_clickable((By.ID, FML.pm_complete_service_dialog_complete_id))
        self.click((By.ID, FML.pm_complete_service_dialog_complete_id))

    # maint. PM manage service
    def click_manage_services(self):
        self.click((By.XPATH, FML.maint_manage_services_xpath))

    def get_manage_service_services_count(self):
        n = 0
        while n < 5:
            try:
                n += 1
                count = self.element_is_displayed((By.XPATH, FML.manage_service_count_xpath))
                if count is True:
                    break
                else:
                    sleep(2)
            except (TimeoutException, StaleElementReferenceException):
                sleep(2)

        return self.element_is_displayed((By.XPATH, FML.manage_service_count_xpath))

    def click_create_service(self):
        self.click((By.XPATH, FML.maint_create_service_xpath))

    def set_service_parameters(self, service_name, miles_due, miles_overdue):
        self.type((By.XPATH, FML.maint_service_name_xpath), service_name)
        sleep(1)
        self.click((By.XPATH, FML.maint_service_check_mile_xpath))
        sleep(1)
        self.type((By.XPATH, FML.maint_service_mile_due_xpath), miles_due)
        sleep(1)
        self.type((By.XPATH, FML.maint_service_mile_due_soon_xpath), miles_overdue)

    def update_service_parameters(self, service_name, miles_due, miles_overdue):
        self.clear((By.XPATH, FML.maint_service_name_xpath))
        self.type((By.XPATH, FML.maint_service_name_xpath), service_name)

        self.clear((By.XPATH, FML.maint_service_mile_due_xpath))
        self.type((By.XPATH, FML.maint_service_mile_due_xpath), miles_due)

        self.clear((By.XPATH, FML.maint_service_mile_due_soon_xpath))
        self.type((By.XPATH, FML.maint_service_mile_due_soon_xpath), miles_overdue)

    def add_vehicle_to_pm_service(self):
        self.wait_for_element_is_clickable((By.XPATH, FML.maint_service_vehicle_dropdown_xpath))
        self.click((By.XPATH, FML.maint_service_vehicle_dropdown_xpath))
        self.wait_for_element_is_clickable((By.XPATH, FML.maint_service_select_vehicle_xpath))
        self.click((By.XPATH, FML.maint_service_select_vehicle_xpath))
        self.wait_for_element_is_clickable((By.XPATH, FML.click_on_service_interval_xpath))
        self.click((By.XPATH, FML.click_on_service_interval_xpath))
        self.wait_for_element_displayed((By.XPATH, FML.vehicle_name_xpath))

    def click_save_service(self):
        self.wait_for_element_is_clickable((By.XPATH, FML.maint_service_save_xpath))
        self.click((By.XPATH, FML.maint_service_save_xpath))

    def click_service_name(self):
        self.click((By.XPATH, FML.maint_service_list_service_name_xpath))

    def get_updated_service_name(self):
        return self.get_text((By.XPATH, FML.updated_service_list_service_name_xpath))

    # pm maint - history
    def click_history_tab(self):
        self.wait_for_element_is_clickable((By.XPATH, FML.pm_history_xpath))
        i = 0
        while i < 10:
            i += 1
            try:
                self.click((By.XPATH, FML.pm_history_xpath))
                break
            except ElementClickInterceptedException:
                sleep(1)

        if i == 10:
            self.click((By.XPATH, FML.pm_history_xpath))

    def get_pm_history_service_count(self):
        for _ in range(5):
            try:
                count_text = self.get_text(
                    (By.XPATH, FML.pm_history_count_xpath)
                ).strip()

                # Remove commas if present
                normalized_text = count_text.replace(",", "")

                if normalized_text.isdigit():
                    return int(normalized_text)

                sleep(2)

            except (TimeoutException, StaleElementReferenceException):
                sleep(2)

        # Final attempt
        count_text = self.get_text((By.XPATH, FML.pm_history_count_xpath)).strip()
        normalized_text = count_text.replace(",", "")

        return int(normalized_text) if normalized_text.isdigit() else 0

    def click_date_filter_history(self):
        self.click((By.XPATH, FML.pm_history_date_filter_xpath))

    def select_last_60_days_history(self):
        self.click((By.XPATH, FML.pm_history_last_60_days_xpath))

    def click_apply_button_history(self):
        self.click((By.ID, FML.apply_button_id))

    def get_vehicle_preventative_maintenance(self):
        return self.get_text((By.XPATH, FML.pm_history_vehicle_label_xpath))

    def get_group_preventative_maintenance(self):
        return self.get_text((By.XPATH, FML.pm_history_group_label_xpath))

    def get_service_preventative_maintenance(self):
        return self.get_text((By.XPATH, FML.pm_history_service_label_xpath))

    def get_interval_preventative_maintenance(self):
        return self.get_text((By.XPATH, FML.pm_history_interval_label_xpath))

    def get_date_serviced_preventative_maintenance(self):
        return self.get_text((By.XPATH, FML.pm_history_date_serviced_label_xpath))

    def get_odometer_preventative_maintenance(self):
        return self.get_text((By.XPATH, FML.pm_history_odometer_label_xpath))

    def get_engine_hours_preventative_maintenance(self):
        return self.get_text((By.XPATH, FML.pm_history_engine_hours_label_xpath))

    def get_notes_preventative_maintenance(self):
        return self.get_text((By.XPATH, FML.pm_history_notes_label_xpath))

    def get_action_preventative_maintenance(self):
        return self.get_text((By.XPATH, FML.pm_history_action_label_xpath))

    def get_pm_history_1st_vehicle(self):
        return self.get_text((By.XPATH, FML.pm_history_1st_vehicle_xpath))

    def get_pm_history_1st_group(self):
        return self.get_text((By.XPATH, FML.pm_history_1st_group_xpath))

    def get_pm_history_1st_service(self):
        return self.get_text((By.XPATH, FML.pm_history_1st_service_xpath))

    def get_pm_history_1st_interval(self):
        return self.get_text((By.XPATH, FML.pm_history_1st_interval_xpath))

    def get_pm_history_1st_date_serviced(self):
        return self.get_text((By.XPATH, FML.pm_history_1st_date_serviced_xpath))

    def get_pm_history_1st_odometer(self):
        return self.get_text((By.XPATH, FML.pm_history_1st_odometer_xpath))

    def get_pm_history_1st_engine_hours(self):
        return self.get_text((By.XPATH, FML.pm_history_1st_engine_hours_xpath))

    def get_pm_history_1st_notes(self):
        return self.get_text((By.XPATH, FML.pm_history_1st_notes_xpath))

    def click_pm_history_1st_edit(self):
        self.wait_for_element_displayed((By.XPATH, FML.pm_history_1st_edit_xpath))
        self.click_element_ignore_exceptions((By.XPATH, FML.pm_history_1st_edit_xpath))

    def click_pm_history_1st_only_edit(self):
        self.wait_for_element_displayed((By.XPATH, FML.pm_history_1st_only_edit_xpath))
        self.click_element_ignore_exceptions((By.XPATH, FML.pm_history_1st_only_edit_xpath))

    # pm maint - history - edit service
    def click_date_selector_pm_history_edit_service(self):
        self.click((By.XPATH, FML.pm_history_edit_service_date_selector_xpath))

    def select_1st_day_pm_history_edit_service(self):
        self.click_element_ignore_exceptions((By.XPATH, FML.pm_history_edit_service_1st_day_xpath))

    def set_hour_pm_history_edit_service(self, hour):
        self.click((By.XPATH, FML.pm_history_edit_service_hour_xpath))
        self.type((By.XPATH, FML.pm_history_edit_service_hour_xpath), hour)

    def set_minute_pm_history_edit_service(self, minute):
        self.click((By.XPATH, FML.pm_history_edit_service_minute_xpath))
        self.type((By.XPATH, FML.pm_history_edit_service_minute_xpath), minute)

    def set_period_pm_history_edit_service(self, period):
        self.click((By.XPATH, FML.pm_history_edit_service_period_xpath))
        self.type((By.XPATH, FML.pm_history_edit_service_period_xpath), period)

    def open_time_selector_pm_history_edit_service(self):
        self.click((By.XPATH, FML.pm_history_edit_service_hour_xpath))

    def click_save_pm_history_edit_service(self):
        self.wait_for_element_is_clickable((By.ID, FML.pm_history_edit_service_save_id))
        self.click((By.ID, FML.pm_history_edit_service_save_id))

    def get_time_pm_history_edit_service(self):
        time = self.find_elements((By.CSS_SELECTOR, '.selection.active'))
        return [time[0].text, time[1].text, time[2].text]

    def set_months_ago_history_edit_service(self, months_ago):
        i = 0
        while i < months_ago:
            i += 1
            self.click((By.XPATH, FML.pm_history_previous_month_xpath))
            sleep(0.2)

    # maint DTC page
    def get_dtc_title(self):
        return self.get_text((By.XPATH, FML.dtc_title_xpath))

    def click_group_filter_dtc_page(self):
        self.click((By.XPATH, FML.group_filter_dtc_page_xpath))

    def search_by_group_dtc_page(self, groupname):
        self.type((By.XPATH, FML.search_by_group_textbox_dtc_page_xpath), groupname)

    def select_search_group_dct_page(self):
        self.click((By.XPATH, FML.select_search_button_dtc_page_xpath))

    def click_done_button_dtc_page(self):
        self.click((By.XPATH, FML.done_button_dtc_page_xpath))

    def group_filter_displayed_dtc_page(self):
        return self.element_is_displayed((By.XPATH, FML.group_filter_dtc_page_xpath))

    def get_code_count_dtc_page(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, FML.code_count_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, FML.code_count_xpath))

    def get_vehicle_column_text_dtc_page(self):
        return self.get_text((By.XPATH, FML.vehicle_column_text_dtc_page_xpath))

    def get_group_column_text_dtc_page(self):
        return self.get_text((By.XPATH, FML.group_column_text_dtc_page_xpath))

    def get_date_column_text_dtc_page(self):
        return self.get_text((By.XPATH, FML.date_column_text_dtc_page_xpath))

    def get_code_column_text_dtc_page(self):
        return self.get_text((By.XPATH, FML.code_column_text_dtc_page_xpath))

    def get_total_page_count(self):
        page_count = int(
            "".join(list(filter(str.isdigit, self.get_text((By.XPATH, FML.pm_history_service_page_count))))))
        return page_count

    # clear / roll back data
    def delete_existing_service(self):
        count = self.get_row_count()

        n = 0
        while n < count:
            self.click_service_name()
            self.click((By.ID, FML.maint_service_delete_id))
            self.click((By.ID, FML.maint_service_confirm_delete_id))
            n += 1

    def get_manage_service_name(self):
        return self.get_text((By.XPATH, FML.maint_service_list_service_name_xpath))

    def newly_created_service_is_displayed(self):
        return self.element_is_displayed((By.XPATH, FML.maint_service_list_service_name_xpath))

    def updated_service_list_service_name_is_displayed(self):
        return self.element_is_displayed((By.XPATH, FML.updated_service_list_service_name_xpath))

    def get_pm_upcoming_service_count_is_displayed(self):
        return self.element_is_displayed((By.XPATH, FML.pm_upcoming_service_count_xpath))

    def click_newly_created_service_name(self):
        self.click((By.XPATH, FML.updated_service_list_service_name_xpath))

    def click_delete_service(self):
        self.click((By.ID, FML.maint_service_delete_id))

    def get_manage_services_title(self):
        return self.get_text((By.XPATH, FML.maint_manage_services_xpath))

    def dtc_count_is_displayed(self):
        return self.element_is_displayed((By.XPATH, FML.code_count_xpath))

    def click_cancel_button(self):
        self.click((By.XPATH, FML.cancel_button_xpath))

    def get_newly_created_service_in_pm_upcoming_service_list(self):
        return self.get_text((By.XPATH, FML.newly_created_service_in_pm_upcoming_service_list_xpath))

    def click_confirm_delete_service(self):
        self.click((By.ID, FML.maint_service_confirm_delete_id))

    def preventative_maintenance_menu_text(self):
        return self.get_text((By.XPATH, FML.preventative_maintenance_new_ui_xpath))

    def diagnostic_trouble_codes_menu_text(self):
        return self.get_text((By.XPATH, FML.dtc_new_ui_xpath))

