from datetime import datetime
from time import sleep

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By

from locators.locators_configuration_setting_page import LocatorsConfigurationSetting as CS
from pages.base_page import BasePage


class ConfigurationSettingPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_tier1_label(self):
        self.scroll_page_up()
        return self.get_text((By.XPATH, CS.tier1_label_xpath))

    def get_full_access_tier1_role_text(self):
        return self.get_text((By.XPATH, CS.tier1_full_access_role_text_xpath))

    def click_add_new_tier_button(self):
        self.click((By.XPATH, CS.add_new_tier_button_xpath))

    def click_select_roles_button(self):
        self.click((By.XPATH, CS.select_roles_button_xpath))

    def click_first_role_dropdown_button(self):
        self.click((By.XPATH, CS.select_first_role_dropdown_xpath))

    def click_role_twice_button(self):
        self.click((By.XPATH, CS.select_role_double_click_xpath))

    def click_select_roles_confirm_button(self):
        self.click((By.XPATH, CS.confirm_select_roles_button_xpath))
        self.click_refresh_button()
        self.wait_for_page_load()
        self.element_is_displayed((By.XPATH, CS.add_new_tier_button_xpath))

    def get_new_role_added_text(self):
        try:
            return self.get_text((By.XPATH, CS.new_role_tier2_text_xpath))
        except StaleElementReferenceException:
            sleep(3)
            return self.get_text((By.XPATH, CS.new_role_tier2_text_xpath))

    def click_edit_tier_button(self):
        self.wait_for_page_load()
        self.click((By.XPATH, CS.edit_tier_button_xpath))

    def click_edit_roles_button(self):
        self.click((By.XPATH, CS.edit_role_button_xpath))

    def click_select_roles_edit_button(self):
        self.click((By.XPATH, CS.select_edit_role_option_xpath))

    def click_edit_roles_confirm_button(self):
        self.click((By.XPATH, CS.confirm_edit_role_button_xpath))
        self.wait_for_page_load()

    def click_delete_tier_button(self):
        self.click((By.ID, CS.delete_tier_button_id))

    def click_confirm_delete_tier_button(self):
        self.click((By.XPATH, CS.confirm_delete_tier_button_xpath))

    def get_second_tier2_role_text(self):
        return self.get_text((By.XPATH, CS.second_edited_role_xpath))

    def get_tier2_text(self, expected_tier):
        return self.wait_for_expected_text((By.XPATH, CS.unranked_tier_text_xpath), expected_tier)

    def role_already_selected(self):
        return self.element_is_displayed((By.XPATH, CS.already_selected_role))

    def delete_role_already_selected(self):
        self.click((By.XPATH, CS.already_selected_role))

    def get_config_setting_page_title(self):
        return self.get_text((By.XPATH, CS.config_settings_page_title_xpath))

    def click_coaching_workflow_tab(self):
        self.click((By.XPATH, CS.coaching_workflow_tab_xpath))

    def get_workflows_title(self):
        return self.get_text((By.XPATH, CS.workflows_title))

    def create_workflow_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.create_workflow_button))

    def groups_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.groups_button))

    def duplicate_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.duplicate_button))

    def edit_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.edit_button))

    def download_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.download_button))

    def click_create_workflow_button(self):
        self.click((By.XPATH, CS.create_workflow_button))

    def get_create_workflow_title(self):
        return self.get_text((By.XPATH, CS.create_workflow_title))

    def click_group_filter(self):
        self.click((By.XPATH, CS.group_filter_xpath))

    def search_group(self, group_name):
        self.type((By.XPATH, CS.search_group_textbox_xpath), group_name)

    def select_searched_group(self):
        self.click((By.XPATH, CS.select_searched_group_xpath))

    def click_done_button(self):
        self.click((By.XPATH, CS.search_group_done_button_xpath))

    def click_group_button(self):
        self.click((By.XPATH, CS.groups_button))

    def get_first_group_name(self):
        self.get_text((By.XPATH, CS.first_group_name))

    def click_edit_button(self):
        self.click((By.XPATH, CS.edit_button))

    def get_edit_workflow_title(self):
        return self.get_text((By.XPATH, CS.edit_workflow_title))

    def enter_new_workflow_name(self, workflow_name):
        self.clear((By.XPATH, CS.workflow_name_field_xpath))
        self.type((By.XPATH, CS.workflow_name_field_xpath), workflow_name)

    def enter_existing_workflow_name(self, workflow_name):
        self.clear((By.XPATH, CS.workflow_existing_name_field_xpath))
        self.click((By.XPATH, CS.workflow_existing_name_field_xpath))
        self.click((By.XPATH, CS.workflow_new_name_field_xpath))
        self.type((By.XPATH, CS.workflow_new_name_field_xpath), workflow_name)

    def click_behaviour_dropdown(self):
        self.click((By.XPATH, CS.behaviour_dropdown_xpath))

    def select_the_behaviour_from_dropdown(self):
        self.click((By.XPATH, CS.behaviour_from_dropdown_xpath))

    def click_coaching_status_dropdown(self):
        self.click((By.XPATH, CS.coaching_status_dropdown_xpath))

    def select_the_coaching_status_from_dropdown(self):
        self.click((By.XPATH, CS.coaching_status_from_dropdown_xpath))

    def enter_a_custom_score(self, score):
        self.type((By.XPATH, CS.custom_score_field_xpath), score)

    def click_save_button(self):
        self.click((By.ID, CS.save_button))

    def click_search_filed_in_workflow_page(self):
        self.click((By.ID, CS.search_filed_in_workflow_page))

    def enter_newly_created_workflow_name(self, name):
        self.type((By.ID, CS.search_filed_in_workflow_page), name)

    def get_first_workflow_name(self):
        self.wait_for_page_load()
        return self.get_text((By.XPATH, CS.first_workflow_name_xpath))

    def delete_existing_behaviour(self):
        self.wait_for_element_displayed((By.XPATH, CS.delete_existing_behaviour_xpath))
        self.click((By.XPATH, CS.delete_existing_behaviour_xpath))

    def get_update_popup_message(self):
        self.wait_for_element_displayed((By.XPATH, CS.update_popup_message_xpath))
        return self.get_text((By.XPATH, CS.update_popup_message_xpath))

    def click_duplicate_button_of_a_workflow(self):
        self.click((By.XPATH, CS.duplicate_button))

    def click_behaviour_dropdown_duplicate(self):
        self.click((By.XPATH, CS.behaviour_dropdown_duplicate_xpath))

    def select_the_behaviour_from_dropdown_duplicate(self):
        self.click((By.XPATH, CS.behaviour_from_dropdown_duplicate_xpath))

    def click_coaching_status_dropdown_duplicate(self):
        self.click((By.XPATH, CS.coaching_status_dropdown_duplicate_xpath))

    def select_the_coaching_status_from_dropdown_duplicate(self):
        self.click((By.XPATH, CS.coaching_status_from_dropdown_duplicate_xpath))

    def enter_a_custom_score_duplicate(self, score):
        self.type((By.XPATH, CS.custom_score_field_duplicate_xpath), score)

    def click_delete_button(self):
        self.click((By.XPATH, CS.delete_button))

    def delete_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.delete_button))

    def click_delete_in_popup(self):
        self.click((By.XPATH, CS.delete_in_popup_xpath))

    def get_delete_popup_message(self):
        return self.get_text((By.XPATH, CS.delete_popup_message_xpath))

    def click_add_behavior_button(self):
        self.wait_for_element_displayed((By.XPATH, CS.add_behavior_button_xpath))
        self.click((By.XPATH, CS.add_behavior_button_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, CS.reset_button_xpath))

    def get_first_workflow_name_after_delete(self):
        return self.element_is_displayed((By.XPATH, CS.first_workflow_name_xpath))

    def close_group_page(self):
        self.click((By.ID, CS.close_button))

    def delete_existing_behaviour_is_present(self):
        return self.element_is_displayed((By.XPATH, CS.delete_existing_behaviour_xpath))

    def click_download_button_of_any_workflow(self):
        self.click((By.XPATH, CS.download_button))

    def get_workflow_file_name(self, workflow_name):
        date_now = datetime.now().strftime("%Y-%m-%d")
        file_name = f"{date_now}_Events_Workflow_{workflow_name}.csv"
        return file_name

    def click_cancel_button_edit_workflow_page(self):
        self.click((By.ID, CS.close_button))

    def get_role_label(self):
        return self.get_text((By.XPATH, CS.role_label_xpath))

    def get_description_label(self):
        return self.get_text((By.XPATH, CS.description_label_xpath))

    def get_admin_permission_label(self):
        return self.get_text((By.XPATH, CS.admin_permission_label_xpath))

    def edit_icon_is_displayed(self):
        return self.element_is_displayed((By.ID, CS.first_tier_edit_icon_id))

    def edit_icon_for_second_tier_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.edit_icon_for_second_tier_xpath))

    def delete_icon_for_second_tier_displayed(self):
        return self.element_is_displayed((By.ID, CS.delete_icon_for_second_tier_id))

    def workflow_count_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.workflow_count_xpath))

    def workflow_group_filter_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.group_filter_xpath))

    def search_workflow_button_is_displayed(self):
        return self.element_is_displayed((By.ID, CS.search_filed_in_workflow_page))

    def click_program_configuration_tab(self):
        self.click((By.XPATH, CS.program_configuration_tab_xpath))

    def get_critical_distance_text(self):
        return self.get_text((By.XPATH, CS.critical_distance_text_xpath))

    def get_audio_alerts_text(self):
        return self.get_text((By.XPATH, CS.audio_alerts_text_xpath))

    def get_led_alerts_text(self):
        return self.get_text((By.XPATH, CS.led_alerts_text_xpath))

    def get_events_text(self):
        return self.get_text((By.XPATH, CS.events_text_xpath))

    def get_following_distance_text(self):
        return self.get_text((By.XPATH, CS.following_distance_text_xpath))

    def get_audio_alerts_for_following_distance_text(self):
        return self.get_text((By.XPATH, CS.audio_alerts_for_following_distance_text_xpath))

    def get_led_alerts_for_following_distance_text(self):
        return self.get_text((By.XPATH, CS.led_alerts_for_following_distance_text_xpath))

    def get_events_for_following_distance_text(self):
        return self.get_text((By.XPATH, CS.events_for_following_distance_text_xpath))

    def get_lane_departure_text(self):
        return self.get_text((By.XPATH, CS.lane_departure_text_xpath))

    def get_audio_alerts_for_lane_departure_text(self):
        return self.get_text((By.XPATH, CS.audio_alerts_for_lane_departure_text_xpath))

    def get_led_alerts_for_lane_departure_text(self):
        return self.get_text((By.XPATH, CS.led_alerts_for_lane_departure_text_xpath))

    def get_events_for_lane_departure_text(self):
        return self.get_text((By.XPATH, CS.events_for_lane_departure_text_xpath))

    def get_rolling_stop_text(self):
        return self.get_text((By.XPATH, CS.rolling_stop_text_xpath))

    def get_audio_alerts_for_rolling_stop_text(self):
        return self.get_text((By.XPATH, CS.audio_alerts_for_rolling_stop_text_xpath))

    def get_led_alerts_for_rolling_stop_text(self):
        return self.get_text((By.XPATH, CS.led_alerts_for_rolling_stop_text_xpath))

    def get_events_for_rolling_stop_text(self):
        return self.get_text((By.XPATH, CS.events_for_rolling_stop_text_xpath))

    def click_action_plan_tab(self):
        self.click((By.XPATH, CS.action_plan_tab_xpath))

    def get_name_text(self):
        return self.get_text((By.XPATH, CS.name_text_xpath))

    def get_description_text(self):
        return self.get_text((By.XPATH, CS.description_text_xpath))

    def edit_button_in_action_plan_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.edit_button_in_action_plan_xpath))

    def delete_button_in_action_plan_is_displayed(self):
        return self.element_is_displayed((By.ID, CS.delete_button_id))

    def add_corrective_action_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.add_corrective_action_xpath))

    def click_close_icon_in_create_workflow_page(self):
        self.click((By.XPATH, CS.close_icon_button_xpath))

    def click_groups_button(self):
        self.click((By.XPATH, CS.groups_button))

    def click_modify_groups_button_in_groups_popup(self):
        self.click((By.XPATH, CS.modify_groups_button_in_groups_popup_xpath))

    def select_group_in_groups_popup(self):
        self.click((By.XPATH, CS.select_group_in_groups_popup_xpath))

    def click_done_button_in_groups_popup(self):
        self.click((By.XPATH, CS.done_button_xpath))

    def click_save_button_in_groups_popup(self):
        self.click((By.XPATH, CS.save_button_xpath))

    def close_groups_page(self):
        self.click((By.XPATH, CS.close_button_xpath))

    def click_group_filter_button(self):
        self.click((By.XPATH, CS.group_filter_xpath))

    def click_search_by_group_field(self):
        self.wait_for_element_displayed((By.XPATH, CS.search_by_group_field_xpath))
        self.click((By.XPATH, CS.search_by_group_field_xpath))

    def search_group_filter(self, group_name):
        self.type((By.XPATH, CS.search_by_group_field_xpath), group_name)

    def select_group(self):
        self.click((By.XPATH, CS.select_group_xpath))

    def click_group_done_button(self):
        self.click((By.XPATH, CS.group_done_button_xpath))

    def click_role_hierarchy_tab_xpath(self):
        self.click((By.XPATH, CS.role_hierarchy_tab_xpath))

    def get_duplicate_workflow_name_error_message(self):
        return self.get_text((By.XPATH, CS.duplicate_workflow_name_error_message_xpath))

    def click_discard_changes_popup(self):
        self.click((By.XPATH, CS.discard_changes_popup_xpath))

    def description_text(self):
        return self.get_text((By.XPATH, CS.description_xpath))

    def note_text(self):
        return self.get_text((By.XPATH, CS.note_xpath))

    def remove_existing_behavior(self):
        self.click((By.XPATH, CS.existing_behavior_close_button_xpath))

    def remove_existing_coaching_status(self):
        self.click((By.XPATH, CS.existing_coaching_status_close_button_xpath))

    def click_incab_mvai_tab(self):
        self.click((By.XPATH, CS.incab_mvai_tab_xpath))

    def get_incab_mvai_page_title(self):
        return self.get_text((By.XPATH, CS.incab_mvai_page_title_xpath))

    def incab_mvai_description_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.incab_mvai_description_xpath))

    def verify_feature_checkboxes_clickable(self):
        feature_checkboxes = {
            "smoking_audio_alert": CS.smoking_audio_alerts_checkbox_xpath,
            "smoking_led_alert": CS.smoking_led_alerts_checkbox_xpath,
            "smoking_events": CS.smoking_events_checkbox_xpath,
            "food_drink_audio_alert": CS.food_drink_audio_alerts_checkbox_xpath,
            "food_drink_led_alert": CS.food_drink_led_alerts_checkbox_xpath,
            "food_drink_events": CS.food_drink_events_checkbox_xpath,
            "inattentiveness_audio_alert": CS.inattentiveness_audio_alerts_checkbox_xpath,
            "inattentiveness_led_alert": CS.inattentiveness_led_alerts_checkbox_xpath,
            "inattentiveness_events": CS.inattentiveness_events_checkbox_xpath,
            "lens_obstruction_audio_alert": CS.lens_obstruction_audio_alerts_checkbox_xpath,
            "lens_obstruction_led_alert": CS.lens_obstruction_led_alerts_checkbox_xpath,
            "lens_obstruction_events": CS.lens_obstruction_events_checkbox_xpath,
            "handheld_device_audio_alert": CS.handheld_device_audio_alerts_checkbox_xpath,
            "handheld_device_led_alert": CS.handheld_device_led_alerts_checkbox_xpath,
            "handheld_device_events": CS.handheld_device_events_checkbox_xpath,
            "no_seatbelt_audio_alert": CS.no_seatbelt_audio_alerts_checkbox_xpath,
            "no_seatbelt_led_alert": CS.no_seatbelt_led_alerts_checkbox_xpath,
            "no_seatbelt_events": CS.no_seatbelt_events_checkbox_xpath
        }
        for feature, checkbox_xpath in feature_checkboxes.items():

            if not feature.startswith(("smoking", "food_drink")):
                self.scroll_page_down()

            locator = (By.XPATH, checkbox_xpath)

            if not self.element_is_displayed(locator):
                print("Checkbox not displayed for feature: " + feature)
                return False

            if not self.wait_for_element_is_clickable(locator):
                print("Checkbox not clickable for feature: " + feature)
                return False

        return True

    def click_smoking_audio_alerts_checkbox(self):
        self.click((By.XPATH, CS.smoking_audio_alerts_checkbox_xpath))

    def smoking_description_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.smoking_description_xpath))

    def food_drink_description_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.food_drink_description_xpath))

    def inattentiveness_description_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.inattentiveness_description_xpath))

    def lens_obstruction_description_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.lens_obstruction_description_xpath))

    def no_seatbelt_description_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.no_seatbelt_description_xpath))

    def handheld_device_description_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.handheld_device_description_xpath))

    def click_save_button_incab_mvai(self):
        self.click((By.XPATH, CS.incab_mvai_save_button_xpath))

    def click_confirmation_popup_save_button(self):
        self.click((By.ID, CS.confirmation_popup_save_button_id))

    def alert_success_message_is_displayed(self):
        return self.element_is_displayed((By.XPATH, CS.alert_success_message_xpath))

    def click_edit_button_in_action_plan(self):
        self.click((By.XPATH, CS.edit_button_in_action_plan_xpath))

    def click_add_corrective_action_button(self):
        self.click((By.XPATH, CS.add_corrective_action_button_xpath))

    def type_corrective_action_name(self, action_name):
        self.type((By.XPATH, CS.corrective_action_name_textbox_xpath), action_name)

    def type_corrective_action_description(self, action_description):
        self.type((By.XPATH, CS.corrective_action_description_textbox_xpath), action_description)

    def click_save_corrective_action_button(self):
        self.click((By.XPATH, CS.save_corrective_action_button_xpath))

    def get_added_corrective_action_text(self):
        return self.get_text((By.XPATH, CS.added_corrective_action_text_xpath))

    def click_delete_button_in_action_plan(self):
        self.click((By.XPATH, CS.delete_button_in_action_plan_xpath))

    def click_confirm_delete_corrective_action_button(self):
        self.click((By.XPATH, CS.confirm_delete_corrective_action_button_xpath))

    def get_corrective_action_title_text(self):
        return self.get_text((By.XPATH, CS.corrective_action_title_text_xpath))

    def added_creative_action_plan_is_deleted(self):
        self.wait_till_element_disappear((By.XPATH, CS.save_corrective_action_button_xpath))
        return self.element_is_displayed((By.XPATH, CS.added_corrective_action_text_xpath))
