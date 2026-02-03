from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from locators.locators_admin_groups_page import LocatorAdminGroups as AG
from pages.base_page import BasePage


class AdminGroupsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_groups_tab(self):
        self.click((By.XPATH, AG.groups_tab_xpath))

    def group_management_page_is_displayed(self):
        return self.element_is_displayed((By.XPATH, AG.groups_tab_header_xpath))

    def groups_tab_count_is_displayed(self):
        return self.element_is_displayed((By.XPATH, AG.groups_tab_count_xpath))

    def get_group_count(self):
        self.wait_for_page_load()
        return self.get_text((By.XPATH, AG.group_count_xpath))

    def click_first_group(self):
        self.click((By.XPATH, AG.first_group_xpath))

    def plus_icon_is_displayed(self):
        self.wait_for_element_displayed((By.XPATH, AG.plus_icon_xpath))
        return self.element_is_displayed((By.XPATH, AG.plus_icon_xpath))

    def click_plus_icon(self):
        self.click((By.XPATH, AG.plus_icon_xpath))

    def add_group_is_displayed(self):
        self.wait_for_element_is_clickable((By.XPATH, AG.add_group_pop_up_xpath))
        return self.element_is_displayed((By.XPATH, AG.add_group_pop_up_xpath))

    def get_group_name_field_in_pop_up(self):
        return self.get_text((By.XPATH, AG.group_name_field_in_pop_up_xpath))

    def get_group_path_field_in_pop_up(self):
        return self.get_text((By.XPATH, AG.group_path_field_in_pop_up_xpath))

    def get_group_path_field_in_delete_pop_up(self):
        return self.get_text((By.XPATH, AG.group_path_field_in_pop_up_xpath))

    def get_description_field_in_pop_up(self):
        return self.get_text((By.XPATH, AG.get_description_field_in_pop_up_xpath))

    def create_or_save_button_disabled(self):
        return self.element_is_displayed((By.XPATH, AG.create_or_save_button_disabled_xpath))

    def type_group_name(self, group_name):
        self.clear((By.XPATH, AG.group_name_input_xpath))
        self.type((By.XPATH, AG.group_name_input_xpath), group_name)

    def type_description(self, description):
        self.clear((By.XPATH, AG.description_input_xpath))
        self.type((By.XPATH, AG.description_input_xpath), description)

    def click_create_or_save_changes(self):
        self.click((By.XPATH, AG.create_or_save_group_button_xpath))

    def click_on_cancel(self):
        self.click((By.XPATH, AG.cancel_xpath))
        self.wait_till_element_disappear((By.XPATH, AG.cancel_xpath))

    def cancel_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, AG.cancel_in_delete_pop_up_xpath))

    def get_group_created_alert_msg(self):
        self.wait_for_element_displayed((By.XPATH, AG.group_created_alert_msg_xpath))
        return self.get_text((By.XPATH, AG.group_created_alert_msg_xpath))

    def get_group_already_exists_error_msg(self):
        self.wait_for_element_displayed((By.XPATH, AG.group_already_exists_error_msg_xpath))
        return self.get_text((By.XPATH, AG.group_already_exists_error_msg_xpath))

    def get_group_name_from_group_container(self):
        try:
            self.wait_till_element_disappear((By.XPATH, AG.create_or_save_group_button_xpath))
            return self.get_text((By.XPATH, AG.first_current_level_sibling_group_name_xpath))
        except TimeoutException:
            return None

    def get_second_group_name_from_group_container(self):
        try:
            self.wait_till_element_disappear((By.XPATH, AG.create_or_save_group_button_xpath))
            return self.get_text((By.XPATH, AG.second_current_level_group_name_xpath))
        except TimeoutException:
            return None

    def get_group_description_from_group_container(self):
        return self.get_text((By.XPATH, AG.group_description_from_group_container_xpath))

    def get_number_of_sub_groups(self):
        text = self.get_text((By.XPATH, AG.number_of_subgroups_xpath)).split(" ")[0]
        return text

    def new_group_exists(self):
        return self.element_is_displayed((By.XPATH, AG.new_created_group_name_xpath))

    def click_on_parent_group(self):
        self.click((By.XPATH, AG.parent_group_xpath))

    def is_parent_group_kebab_menu_displayed(self):
        return self.element_is_displayed((By.XPATH, AG.parent_group_kebab_menu_xpath))

    def click_on_kebab(self, group_name):
        xpath = '//*[@title="' + group_name + '"]/parent::div/following-sibling::div'
        self.click((By.XPATH, xpath))

    def edit_option_is_available(self):
        return self.element_is_displayed((By.XPATH, AG.edit_option_xpath))

    def move_option_is_available(self):
        return self.element_is_displayed((By.XPATH, AG.move_option_xpath))

    def delete_option_is_available(self):
        return self.element_is_displayed((By.XPATH, AG.delete_option_xpath))

    def click_delete(self):
        self.click((By.XPATH, AG.delete_option_xpath))

    def delete_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, AG.delete_group_pop_up_xpath))

    def click_delete_group(self):
        self.click((By.XPATH, AG.delete_group_pop_up_xpath))

    def click_cancel_in_delete_pop_up(self):
        self.click((By.XPATH, AG.cancel_in_delete_pop_up_xpath))
        self.wait_till_element_disappear((By.XPATH, AG.cancel_in_delete_pop_up_xpath))

    def get_number_of_sub_groups_for_first_child_group(self):
        text = self.get_text((By.XPATH, AG.number_of_sub_groups_for_first_child_group_xpath)).split(" ")[0]
        return text

    def delete_group(self):
        while self.get_number_of_sub_groups_for_first_child_group() != "0":
            self.click_first_child_group()
            self.click((By.XPATH, AG.kebab_second_tier_child_xpath))
            self.click_delete()
            self.wait_for_element_is_clickable((By.XPATH, AG.delete_group_pop_up_xpath))
            self.click((By.XPATH, AG.delete_group_pop_up_xpath))
            self.wait_till_element_disappear((By.XPATH, AG.delete_group_pop_up_xpath))
        self.click((By.XPATH, AG.kebab_button_child_group_xpath))
        self.click_delete()
        self.wait_for_element_is_clickable((By.XPATH, AG.delete_group_pop_up_xpath))
        self.click((By.XPATH, AG.delete_group_pop_up_xpath))
        self.wait_till_element_disappear((By.XPATH, AG.delete_group_pop_up_xpath))

    def click_edit_option(self):
        self.click((By.XPATH, AG.edit_option_xpath))

    def edit_group_pop_up_title_displayed(self):
        return self.element_is_displayed((By.XPATH, AG.edit_group_pop_up_title_xpath))

    def get_sub_groups_field_in_pop_up(self):
        return self.get_text((By.XPATH, AG.sub_groups_field_in_pop_up_xpath))

    def group_name_is_a_required_field(self):
        return self.element_is_displayed((By.XPATH, AG.group_name_require_xpath))

    def get_current_level_sibling_group_name(self):
        return self.get_text((By.XPATH, AG.first_current_level_sibling_group_name_xpath))

    def click_first_child_group(self):
        self.click((By.XPATH, AG.first_child_group_xpath))

    def click_plus_icon_child(self):
        self.click((By.XPATH, AG.plus_icon_child_xpath))

    def delete_group_pop_up_title_displayed(self):
        return self.element_is_displayed((By.XPATH, AG.delete_group_pop_up_title_xpath))

    def get_confirmation_msg_for_delete_group(self):
        return self.get_text((By.XPATH, AG.confirmation_msg_for_delete_group_xpath))

    def get_group_deleted_alert_msg(self):
        self.wait_for_element_displayed((By.XPATH, AG.group_deleted_alert_msg_xpath))
        return self.get_text((By.XPATH, AG.group_deleted_alert_msg_xpath))

    def cant_delete_group_message_displayed(self):
        return self.element_is_displayed((By.XPATH, AG.cant_delete_group_message_xpath))

    def get_cant_delete_group_suggestion_message(self):
        return self.get_text((By.XPATH, AG.get_cant_delete_group_suggestion_message_xpath))

    def click_close(self):
        self.click((By.XPATH, AG.close_button_xpath))

    def click_delete_edit_page(self):
        self.click((By.XPATH, AG.delete_edit_page_xpath))

    def enter_text_in_search_box(self, group_name):
        self.clear((By.XPATH, AG.search_box_input_xpath))
        self.type((By.XPATH, AG.search_box_input_xpath), group_name)

    def is_dropdown_present_for_search_box(self):
        return self.element_is_displayed((By.XPATH, AG.search_box_drop_down_menu_xpath))

    def click_group_from_suggestion_box(self):
        self.click((By.XPATH, AG.search_box_drop_down_menu_xpath))

    def group_is_focused(self):
        return self.element_is_displayed((By.XPATH, AG.selected_group_xpath))

    def click_on_the_doughnut_peddler_group(self):
        self.click((By.XPATH, AG.doughnut_peddler_group_text_xpath))

    def sub_groups_are_displayed(self):
        self.wait_for_element_displayed((By.XPATH, AG.subgroups_xpath))
        return self.element_is_displayed((By.XPATH, AG.subgroups_xpath))

    def click_distribution_center_group(self):
        self.click((By.XPATH, AG.distribution_centre_group_text_xpath))

    def get_breadcrumb_text(self):
        return self.get_text((By.XPATH, AG.breadcrumb_text_xpath))

    def group_hierarchy_is_present(self):
        return self.element_is_displayed((By.XPATH, AG.group_hierarchy_xpath))

    def group_card_details_is_present(self):
        return self.element_is_displayed((By.XPATH, AG.group_card_details_xpath))

    def search_group_is_displayed(self):
        return self.element_is_displayed((By.XPATH, AG.search_group_box_xpath))

    def download_csv_button_is_present(self):
        return self.element_is_displayed((By.XPATH, AG.download_csv_xpath))

    def import_groups_button_is_present(self):
        return self.element_is_displayed((By.XPATH, AG.import_group_button_xpath))

    def click_view_change_history(self):
        self.click((By.XPATH, AG.view_change_history_xpath))

    def get_name_column_title(self):
        return self.get_text((By.XPATH, AG.name_table_text_xpath))

    def get_groups_column_title(self):
        return self.get_text((By.XPATH, AG.groups_table_text_xpath))

    def get_action_column_title(self):
        return self.get_text((By.XPATH, AG.action_table_text_xpath))

    def get_action_details_column_title(self):
        return self.get_text((By.XPATH, AG.action_details_table_text_xpath))

    def get_editor_column_title(self):
        return self.get_text((By.XPATH, AG.editor_table_text_xpath))

    def get_action_date_column_title(self):
        return self.get_text((By.XPATH, AG.action_date_table_text_xpath))

    def get_group_audit_log_title(self):
        return self.get_text((By.XPATH, AG.group_audit_log_title_xpath))

    def search_group_affected_is_displayed(self):
        return self.element_is_displayed((By.XPATH, AG.search_group_textbox_xpath))

    def select_actions_is_displayed(self):
        return self.element_is_displayed((By.XPATH, AG.select_actions_filter_xpath))

    def download_log_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, AG.download_log_button_xpath))

    def date_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, AG.date_filter_xpath))

    def get_first_group_affected_text(self):
        return self.get_text((By.XPATH, AG.first_group_affected_text_xpath))

    def search_group_affected(self, group_name):
        self.type((By.XPATH, AG.search_group_textbox_xpath), group_name)

    def get_no_audit_logs_message(self):
        self.wait_for_element_displayed((By.XPATH, AG.no_audit_logs_message_xpath))
        return self.get_text((By.XPATH, AG.no_audit_logs_message_xpath))

    def click_reset_in_audit_page(self):
        self.click((By.XPATH, AG.reset_button_audit_page_xpath))

    def click_date_range_dropdown(self):
        self.click((By.XPATH, AG.date_filter_xpath))

    def select_date_range_today(self):
        self.click((By.XPATH, AG.select_date_range_today_xpath))

    def get_action_date(self):
        self.wait_for_element_displayed((By.XPATH, AG.action_date_table_text_xpath))
        return self.get_text((By.XPATH, AG.action_date_table_text_xpath))

    def click_close_group_audit_log(self):
        self.click((By.XPATH, AG.close_view_change_history_xpath))

    def view_change_history_popup_displayed(self):
        self.wait_till_element_disappear((By.XPATH, AG.view_change_history_popup_xpath))
        return self.element_is_displayed((By.XPATH, AG.view_change_history_popup_xpath))

    def click_select_actions_filter(self):
        self.click((By.XPATH, AG.select_actions_filter_xpath))

    def select_action_type_added(self):
        self.click((By.XPATH, AG.select_added_xpath))

    def get_first_action_type_text(self):
        self.wait_for_element_displayed((By.XPATH, AG.action_type_text_xpath))
        return self.get_text((By.XPATH, AG.action_type_text_xpath))

    def select_action_type_edited(self):
        self.click((By.XPATH, AG.select_edited_xpath))

    def select_deleted_action_type(self):
        self.click((By.XPATH, AG.select_deleted_xpath))

    def select_imported_action_type(self):
        self.click((By.XPATH, AG.select_imported_xpath))

    def click_download_log_button(self):
        self.click((By.XPATH, AG.download_log_button_xpath))
        self.click((By.XPATH, AG.download_log_confirm_button_xpath))

    def get_audit_log_file_name(self):
        file_name = 'audit_report.csv'
        return file_name

    def download_log_button_disabled_displayed(self):
        return self.element_is_displayed((By.XPATH, AG.download_log_button_disabled_xpath))

    def get_group_name_from_container(self):
        return self.get_text((By.XPATH, AG.group_name_from_container_xpath))

