from selenium.webdriver.common.by import By

from locators.locators_edit_user import LocatorsEditUser as EU
from pages.base_page import BasePage


class EditUserPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def wait_for_edit_user_page(self):
        self.wait_for_element_displayed((By.XPATH, EU.edit_user_title_xpath))
        self.wait_for_page_load()

    def edit_group_filter(self):
        self.click((By.XPATH, EU.edit_group_button_xpath))

    def search_role_group(self, new_group):
        self.type((By.XPATH, EU.search_group_textbox_xpath), new_group)

    def select_role_group(self):
        self.click((By.XPATH, EU.select_searched_group_button_xpath))

    def click_group_done(self):
        self.click((By.XPATH, EU.done_button_xpath))

    def edit_role_filter(self):
        self.click((By.XPATH, EU.select_role_xpath))

    def select_role_filter(self):
        self.click((By.XPATH, EU.role_dropdown_xpath))

    def click_save_changes(self):
        self.wait_for_element_is_clickable((By.XPATH, EU.save_changes_button_xpath))
        self.click((By.XPATH, EU.save_changes_button_xpath))
        self.wait_for_page_load()
        self.wait_till_element_disappear((By.XPATH, EU.updated_user_success_message_xpath))

    def click_first_name(self):
        self.wait_for_element_displayed((By.XPATH, EU.first_id_textbox_xpath))
        self.click((By.XPATH, EU.first_id_textbox_xpath))

    def clear_first_name(self):
        self.clear((By.XPATH, EU.first_id_textbox_xpath))

    def edit_first_name(self, edit_name):
        self.type((By.XPATH, EU.first_id_textbox_xpath), edit_name)

    def click_delete_name(self):
        self.click((By.XPATH, EU.delete_user_button_xpath))

    def confirm_delete_name(self):
        self.click((By.XPATH, EU.confirm_delete_user_xpath))
        self.wait_for_page_load()
        self.wait_till_element_disappear((By.XPATH, EU.deleted_user_success_message_xpath))

    def click_notification_tab(self):
        self.click((By.XPATH, EU.notification_tab_xpath))

    def click_add_notification(self):
        self.wait_for_element_displayed((By.XPATH, EU.add_notification_button_xpath))
        self.click((By.XPATH, EU.add_notification_button_xpath))

    def click_notification_type(self):
        self.click((By.XPATH, EU.notification_type_xpath))

    def select_event_status(self):
        self.click((By.XPATH, EU.select_event_status_xpath))

    def click_status_tab(self):
        self.click((By.XPATH, EU.select_status_button_xpath))

    def select_f2f_status(self):
        self.click((By.XPATH, EU.select_status_f2f_xpath))

    def click_arrow_tab(self):
        self.click((By.XPATH, EU.dropdown_arrow_xpath))

    def conditions_group_tab(self):
        self.click((By.XPATH, EU.conditions_group_button_xpath))

    def search_group_condition(self, group):
        self.type((By.XPATH, EU.conditions_search_group_textbox_xpath), group)

    def select_group_dropdown(self):
        self.click((By.XPATH, EU.conditions_select_group_dropdown_xpath))

    def done_group_button(self):
        self.click((By.XPATH, EU.conditions_done_button_xpath))

    def click_reports_tab(self):
        self.click((By.XPATH, EU.reports_tab_xpath))

    def click_add_subscription(self):
        self.click((By.XPATH, EU.add_subscription_button_xpath))

    def click_select_report(self):
        self.click((By.XPATH, EU.select_report_xpath))

    def select_driving_summary(self):
        self.click((By.XPATH, EU.select_driving_summary_xpath))

    def select_insight_summary_report(self):
        self.click((By.XPATH, EU.select_insight_summary_report_xpath))

    def get_notification_text(self):
        return self.get_text((By.XPATH, EU.notification_tab_xpath))

    def get_report_text(self):
        return self.get_text((By.XPATH, EU.reports_tab_xpath))

    def click_delete_notifications(self):
        self.click((By.XPATH, EU.delete_notifications_xpath))

    def delete_notifications_button_displayed(self):
        return self.element_is_displayed((By.XPATH, EU.delete_notifications_xpath))

    def delete_reports_button_displayed(self):
        return self.element_is_displayed((By.XPATH, EU.delete_reports_xpath))

    def click_delete_reports(self):
        self.click((By.XPATH, EU.delete_reports_xpath))

    def click_inactive_status(self):
        self.click((By.XPATH, EU.inactive_status_checkbox_xpath))

    def click_continue_inactive_button(self):
        self.click((By.XPATH, EU.continue_status_button_xpath))

    def click_active_label(self):
        self.click((By.XPATH, EU.active_status_checkbox_xpath))

    def click_login_enabled(self):
        self.click((By.XPATH, EU.login_enabled_checkbox_xpath))

    def click_login_disabled(self):
        self.click((By.XPATH, EU.login_disabled_checkbox_xpath))

    def add_username_login(self, username):
        self.type((By.XPATH, EU.username_textbox_xpath), username)

    def add_password_login(self, password):
        self.type((By.XPATH, EU.password_textbox_xpath), password)

    def back_to_previous_page(self):
        self.back()

    def edit_user_title_is_displayed(self):
        self.wait_for_element_displayed((By.XPATH, EU.edit_user_title_xpath))
        return self.element_is_displayed((By.XPATH, EU.edit_user_title_xpath))

    def click_first_name_in_user_page(self):
        self.click((By.XPATH, EU.first_row_driver_name_xpath))
