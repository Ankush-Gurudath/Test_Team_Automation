from selenium.webdriver.common.by import By
from locators.locators_equipment_management_page import LocatorsEquipmentManagement as EQ
from pages.base_page import BasePage


class EquipmentManagementPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.equipment_with_device_count = None
        self.driver = driver

    # Actions
    def click_equipment(self):
        self.click((By.XPATH, EQ.equipment_management_tab_xpath))
        self.wait_for_page_load()

    def click_add_equipment(self):
        self.click((By.XPATH, EQ.add_equipment_button_xpath))

    def click_select_group(self):
        self.click((By.ID, EQ.group_filter_id))

    def click_done_on_select_group(self):
        self.click((By.XPATH, EQ.group_filter_done_button_xpath))

    def enter_equipment_name(self, equipment_name):
        self.type((By.XPATH, EQ.equipment_name_textbox_xpath), equipment_name)

    def click_equipment_status(self):
        self.click((By.XPATH, EQ.equipment_status_xpath))

    def select_in_service_equipment_status(self):
        self.click_element_ignore_exceptions((By.XPATH, EQ.equipment_status_in_service_xpath), 3)

    def click_create_equipment(self):
        self.click((By.ID, EQ.create_equipment_button_id))
        self.wait_till_element_disappear((By.XPATH, EQ.equipment_created_success_message_xpath))

    def click_move_and_continue(self):
        self.wait_for_element_is_clickable((By.ID, EQ.move_and_continue_id))
        self.click((By.ID, EQ.move_and_continue_id))

    def click_change_status(self):
        self.click((By.XPATH, EQ.change_status_button_xpath))

    def click_select_status(self):
        self.click((By.XPATH, EQ.edit_equipment_status_drop_down_xpath))

    def click_first_checkbox(self):
        self.wait_for_expected_number((By.XPATH, EQ.equipment_count_xpath), '1')
        self.click((By.XPATH, EQ.first_checkbox_xpath))

    def select_in_service(self):
        self.click((By.XPATH, EQ.in_service_xpath))

    def select_out_of_service(self):
        self.click((By.XPATH, EQ.out_of_service_xpath))

    def select_spare(self):
        self.click((By.XPATH, EQ.spare_xpath))

    def click_apply(self):
        self.click((By.ID, EQ.set_equipment_status_apply_button_id))

    def click_first_equipment_in_list(self):
        self.click_element_ignore_exceptions((By.XPATH, EQ.first_equipment_in_list_xpath))

    def clear_equipment_name(self):
        self.clear((By.XPATH, EQ.equipment_name_textbox_xpath))

    def click_search_drop_down(self):
        self.click((By.XPATH, EQ.search_drop_down_xpath))

    def click_equipment_in_drop_down(self):
        self.click((By.XPATH, EQ.equipment_in_drop_down_xpath))

    def enter_equipment_name_in_search(self, equipment_name):
        self.type((By.ID, EQ.search_textbox_id), equipment_name)

    def search_and_select_device_equipment(self, device_name):
        self.type_and_auto_search((By.XPATH, EQ.equipment_search_device_xpath), device_name)
        self.click_element_ignore_exceptions((By.XPATH, EQ.equipment_search_device_result_xpath))

    def click_eq_management_status_drop_down(self):
        self.click((By.XPATH, EQ.equipment_management_status_drop_down_xpath))

    def select_eq_management_in_service_status(self):
        self.click((By.XPATH, EQ.equipment_management_in_service_status_drop_down_xpath))

    def select_eq_management_out_of_service_status(self):
        self.click((By.XPATH, EQ.equipment_management_out_of_service_status_drop_down_xpath))

    def select_eq_management_spare_status(self):
        self.click((By.XPATH, EQ.equipment_management_spare_status_drop_down_xpath))

    def select_root_group(self):
        self.click((By.XPATH, EQ.root_group_checkbox_xpath))

    def clear_eq_management_status_drop_down(self):
        self.click((By.XPATH, EQ.equipment_management_status_drop_down_xpath))

    def add_equipment_out_of_service(self, equipment_name):
        self.click((By.XPATH, EQ.add_equipment_button_xpath))
        self.click((By.ID, EQ.group_filter_id))
        self.click((By.XPATH, EQ.group_filter_done_button_xpath))
        self.type((By.XPATH, EQ.equipment_name_textbox_xpath), equipment_name)
        self.click((By.XPATH, EQ.add_equipment_status_dropdown_xpath))
        self.click((By.XPATH, EQ.add_equipment_out_of_service_dropdown_xpath))
        self.click((By.ID, EQ.create_equipment_button_id))

    def add_equipment_in_service(self, equipment_name):
        self.click((By.XPATH, EQ.add_equipment_button_xpath))
        self.click((By.ID, EQ.group_filter_id))
        self.click((By.XPATH, EQ.group_filter_done_button_xpath))
        self.type((By.XPATH, EQ.equipment_name_textbox_xpath), equipment_name)
        self.click((By.XPATH, EQ.add_equipment_status_dropdown_xpath))
        self.click((By.XPATH, EQ.add_equipment_in_service_dropdown_xpath))
        self.click((By.ID, EQ.create_equipment_button_id))

    def add_equipment_spare(self, equipment_name):
        self.click((By.XPATH, EQ.add_equipment_button_xpath))
        self.click((By.ID, EQ.group_filter_id))
        self.click((By.XPATH, EQ.group_filter_done_button_xpath))
        self.type((By.XPATH, EQ.equipment_name_textbox_xpath), equipment_name)
        self.click((By.XPATH, EQ.add_equipment_status_dropdown_xpath))
        self.click((By.XPATH, EQ.add_equipment_spare_dropdown_xpath))
        self.click((By.ID, EQ.create_equipment_button_id))

    def click_reset(self):
        self.wait_for_page_to_fully_load()
        self.click((By.XPATH, EQ.reset_button_xpath))

    def wait_for_page_loaded(self):
        self.wait_for_element_is_clickable((By.XPATH, EQ.reset_button_xpath))

    # Get Text
    def get_equipment_management_title_text(self):
        return self.get_text((By.XPATH, EQ.equipment_management_title_xpath))

    def get_equipment_column_name_text(self):
        return self.get_text((By.ID, EQ.equipment_column_name_id))

    def get_device_column_name_text(self):
        return self.get_text((By.ID, EQ.device_column_name_id))

    def get_group_column_name_text(self):
        return self.get_text((By.ID, EQ.group_column_name_id))

    def get_last_connected_column_name_text(self):
        return self.get_text((By.ID, EQ.last_connected_column_name_id))

    def get_status_column_name_text(self):
        return self.get_text((By.ID, EQ.status_column_name_id))

    def get_new_equipment_text(self, equipment_name):
        self.wait_for_expected_text((By.XPATH, EQ.test_equipment_added_xpath), equipment_name)
        return self.get_text((By.XPATH, EQ.test_equipment_added_xpath))

    def get_status_text(self, status):
        self.wait_for_expected_text((By.XPATH, EQ.status_value_xpath), status)
        return self.get_text((By.XPATH, EQ.status_value_xpath))

    def click_last_connected_filter(self):
        self.click((By.XPATH, EQ.last_connected_filter_xpath))

    def select_last_30_days(self):
        self.click((By.XPATH, EQ.last_30_days_xpath))

    def click_apply_last_connected(self):
        self.click((By.XPATH, EQ.apply_button_last_connected_xpath))

    def select_first_equipment(self):
        self.click((By.XPATH, EQ.select_the_first_equipment_xpath))

    def click_move_group(self):
        self.click((By.XPATH, EQ.move_group_button_xpath))

    def click_detach_device(self):
        self.click((By.XPATH, EQ.detach_button_xpath))

    def click_apply_detach(self):
        self.click((By.ID, EQ.apply_detach_id))

    def get_detach_message(self, expected_text, attempts, wait_time):
        return self.wait_for_expected_text((By.XPATH, EQ.detach_message_xpath), expected_text, attempts, wait_time)

    def search_group(self, group_name):
        self.type((By.XPATH, EQ.search_group_textbox_xpath), group_name)

    def select_searched_group(self):
        self.click((By.XPATH, EQ.select_searched_group_xpath))

    def click_done_button_move_group(self):
        self.click((By.XPATH, EQ.move_group_done_button_xpath))

    def click_continue_button(self):
        self.click((By.XPATH, EQ.move_group_continue_button_xpath))

    def get_the_group_first_equipment(self):
        return self.get_text((By.XPATH, EQ.group_name_of_first_equipment_xpath))

    def click_delete_equipment_button(self):
        self.click((By.XPATH, EQ.delete_equipment_button_xpath))

    def click_confirm_button_delete_equipment(self):
        self.click((By.XPATH, EQ.confirm_button_xpath))
        self.wait_for_page_load()
        self.wait_till_element_disappear((By.XPATH, EQ.equipment_deleted_success_message_xpath))
        self.wait_for_page_load()

    def click_select_all_checkbox(self):
        self.click((By.XPATH, EQ.select_all_equipment_button))

    def get_equipment_group(self):
        self.wait_for_element_displayed((By.XPATH, EQ.group_of_first_equipment_xpath))
        return self.get_text((By.XPATH, EQ.group_of_first_equipment_xpath))

    def click_cancel_button(self):
        self.click((By.XPATH, EQ.cancel_button_xpath))

    def device_1st_equipment(self, expected_text, attempts=5):
        self.wait_for_expected_number((By.XPATH, EQ.equipment_count_xpath), '1')
        return self.wait_for_expected_text((By.XPATH, EQ.device_1st_equipment_xpath), expected_text, attempts)

    # clear / roll back data
    def delete_existing_equipment(self):
        self.click_select_all_checkbox()
        self.click_delete_equipment_button()
        self.click_confirm_button_delete_equipment()

    def move_and_continue_displayed(self):
        return self.element_is_displayed((By.ID, EQ.move_and_continue_id))

    def add_equipment_page_is_displayed(self):
        return self.element_is_displayed((By.XPATH, EQ.add_equip_Page_title_xpath))

    def group_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, EQ.group_filter_xpath))

    def last_connected_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, EQ.last_connected_filter_xpath))

    def status_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, EQ.equipment_management_status_drop_down_xpath))

    def search_name_or_id_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, EQ.search_filter_xpath))

    def reset_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, EQ.reset_button_xpath))

    def move_group_button_displayed(self):
        return self.element_is_displayed((By.XPATH, EQ.move_group_button_xpath))

    def change_status_button_displayed(self):
        return self.element_is_displayed((By.XPATH, EQ.change_status_button_xpath))

    def delete_equipment_button_displayed(self):
        return self.element_is_displayed((By.XPATH, EQ.delete_equipment_button_xpath))

    def more_options_button_displayed(self):
        return self.element_is_displayed((By.XPATH, EQ.more_options_xpath))

    def add_equipment_is_enabled(self):
        return self.element_is_displayed((By.XPATH, EQ.add_equipment_button_xpath))

    def pagination_is_displayed(self):
        return self.element_is_displayed((By.XPATH, EQ.paginator_xpath))

    def detach_device_button_displayed(self):
        return self.element_is_displayed((By.XPATH, EQ.detach_button_xpath))

    def click_device_column_sorting_button(self):
        self.click((By.XPATH, EQ.device_column_sorting_xpath))

    def get_equipment_with_attached_devices_count(self):
        # 1️⃣ Wait until table cells are visible
        self.wait_for_element_displayed((By.XPATH, "//*[@class='cell-value']"))

        # 2️⃣ Locate the Device (SerialNumber) column header
        device_header = self.driver.find_element(By.XPATH, "//*[@data-test-id='sortable-container-SerialNumber']")

        # 3️⃣ Compute the column index by counting preceding siblings
        preceding_headers = self.driver.find_elements(
            By.XPATH, "//*[@data-test-id='sortable-container-SerialNumber']/preceding-sibling::*"
        )
        devices_col_index = len(preceding_headers) + 1  # XPath is 1-based index

        # 4️⃣ Get all rows (skip header)
        rows = self.driver.find_elements(By.XPATH, "//tr[position()>1]")

        # 5️⃣ Collect all non-empty values under the 'Device/SerialNumber' column
        devices_values = []
        for row in rows:
            cells = row.find_elements(By.XPATH, ".//*[@class='cell-value']")
            if devices_col_index <= len(cells):
                cell_value = cells[devices_col_index - 1].text.strip()
                if cell_value:
                    devices_values.append(cell_value)

        # 6️⃣ Store and return count
        self.equipment_with_device_count = len(devices_values)
        return self.equipment_with_device_count



