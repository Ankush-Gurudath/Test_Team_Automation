from datetime import datetime, timedelta
from time import sleep

import pytz
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By

from locators.locators_video_search_page import LocatorsVideoSearchPage as VS
from pages.base_page import BasePage


class VideoSearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Labels
    def get_video_search_title(self):
        self.wait_for_element_displayed((By.ID, VS.video_search_page_title_id))
        return self.get_text((By.ID, VS.video_search_page_title_id))

    def click_vehicle_tab(self):
        self.click((By.XPATH, VS.vehicle_tab_xpath))

    def click_library_tab(self):
        self.click((By.XPATH, VS.library_tab_xpath))

    def click_saved_videos_tab(self):
        self.click((By.XPATH, VS.saved_videos_tab_xpath))

    def click_video_tags_tab(self):
        self.click((By.XPATH, VS.video_tags_tab_xpath))

    # table columns in vehicle page
    def get_vehicle_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, VS.vehicle_count_text_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, VS.vehicle_count_text_xpath))

    def get_actions_column_text(self):
        return self.get_text((By.XPATH, VS.actions_column_text_xpath))

    def get_vehicles_column_text(self):
        return self.get_text((By.XPATH, VS.vehicles_column_text_xpath))

    def get_device_column_text(self):
        return self.get_text((By.XPATH, VS.device_column_text_xpath))

    def get_last_communicated_column_text(self):
        return self.get_text((By.XPATH, VS.last_communicated_column_text_xpath))

    def get_group_column_text(self):
        return self.get_text((By.XPATH, VS.group_column_text_xpath))

    def get_views_column_text(self):
        return self.get_text((By.XPATH, VS.views_column_text_xpath))

    # Filters and select search criteria in Vehicle page
    def click_group_filter(self):
        self.click((By.XPATH, VS.group_filter_xpath))

    def search_group(self, group_name):
        self.type((By.XPATH, VS.search_group_textbox_xpath), group_name)

    def select_searched_group(self):
        self.click((By.XPATH, VS.select_searched_group_xpath))

    def click_done_button(self):
        self.click((By.XPATH, VS.done_button_group_filter_xpath))

    def click_select_search_filter(self):
        self.click((By.XPATH, VS.select_search_filter_xpath))

    def select_vehicle_name_dropdown(self):
        self.click((By.XPATH, VS.select_vehicle_name_dropdown_xpath))

    def select_serial_name_dropdown(self):
        self.click((By.XPATH, VS.select_serial_number_dropdown_xpath))

    def search_criteria_textbox(self, searched_name):
        self.type((By.XPATH, VS.search_criteria_textbox_xpath), searched_name)

    def click_reset_button(self):
        self.click((By.XPATH, VS.reset_button_xpath))

    # table columns in saved videos page
    def get_video_name_column_text(self):
        return self.get_text((By.XPATH, VS.video_name_column_text_xpath))

    def get_status_column_text(self):
        return self.get_text((By.XPATH, VS.status_column_text_xpath))

    def get_tag_type_column_text(self):
        return self.get_text((By.XPATH, VS.tag_type_column_text_xpath))

    def get_vehicle_column_saved_videos_text(self):
        return self.get_text((By.XPATH, VS.vehicle_column_saved_videos_text_xpath))

    def get_group_column_saved_videos_text(self):
        return self.get_text((By.XPATH, VS.group_column_saved_videos_text_xpath))

    def get_length_column_text(self):
        return self.get_text((By.XPATH, VS.length_column_text_xpath))

    def get_views_column_saved_videos_text(self):
        return self.get_text((By.XPATH, VS.views_column_saved_videos_text_xpath))

    def get_video_date_column_text(self):
        return self.get_text((By.XPATH, VS.video_date_column_text_xpath))

    def get_request_date_column_text(self):
        return self.get_text((By.XPATH, VS.request_date_column_text_xpath))

    def get_video_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, VS.video_count_text_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, VS.video_count_text_xpath))

    # Filters and select search criteria in video tags page
    def click_group_filter_saved_videos(self):
        self.click((By.XPATH, VS.group_filter_saved_videos_xpath))

    def search_group_saved_videos(self, group_name):
        self.type((By.XPATH, VS.search_group_textbox_saved_videos_xpath), group_name)

    def select_searched_group_saved_videos(self):
        self.click((By.XPATH, VS.select_searched_group_saved_videos_xpath))

    def done_button_saved_videos(self):
        self.click((By.XPATH, VS.done_button_group_filter_saved_videos_xpath))

    def click_date_filter_saved_videos(self):
        self.click((By.XPATH, VS.date_filter_saved_videos_xpath))

    def set_video_date_range(self, start_month, start_day, start_year, end_month, end_day, end_year):
        self.click((By.XPATH, VS.date_range_start_month_xpath))
        self.type((By.XPATH, VS.date_range_start_month_xpath), start_month)
        self.click((By.XPATH, VS.date_range_start_day_xpath))
        self.type((By.XPATH, VS.date_range_start_day_xpath), start_day)
        self.click((By.XPATH, VS.date_range_start_year_xpath))
        self.type((By.XPATH, VS.date_range_start_year_xpath), start_year)
        self.click((By.XPATH, VS.date_range_end_month_xpath))
        self.type((By.XPATH, VS.date_range_end_month_xpath), end_month)
        self.click((By.XPATH, VS.date_range_end_day_xpath))
        self.type((By.XPATH, VS.date_range_end_day_xpath), end_day)
        self.click((By.XPATH, VS.date_range_end_year_xpath))
        self.type((By.XPATH, VS.date_range_end_year_xpath), end_year)

    def click_apply_saved_videos(self):
        self.click((By.XPATH, VS.apply_button_saved_videos_xpath))

    def click_select_search_filter_saved_videos(self):
        self.click((By.XPATH, VS.select_search_filter_saved_videos_xpath))

    def select_video_name_dropdown_saved_videos(self):
        self.click((By.XPATH, VS.video_name_dropdown_saved_videos_xpath))

    def select_vehicle_name_dropdown_saved_videos(self):
        self.click((By.XPATH, VS.vehicle_name_dropdown_saved_videos_xpath))

    def search_criteria_textbox_saved_videos(self, searched_name):
        self.type((By.XPATH, VS.search_criteria_textbox_saved_videos_xpath), searched_name)

    def click_reset_button_saved_videos(self):
        self.click((By.XPATH, VS.reset_button_saved_videos_xpath))

    # table columns in video tags page
    def get_actions_column_video_tags_text(self):
        return self.get_text((By.XPATH, VS.actions_column_text_video_tags_xpath))

    def get_vehicle_column_video_tags_text(self):
        return self.get_text((By.XPATH, VS.vehicle_column_video_tags_text_xpath))

    def get_tag_name_column_text(self):
        return self.get_text((By.XPATH, VS.tag_name_column_text_xpath))

    def get_category_column_text(self):
        return self.get_text((By.XPATH, VS.category_column_text_xpath))

    def get_available_views_column_text(self):
        return self.get_text((By.XPATH, VS.available_views_column_text_xpath))

    def get_group_column_video_tags_text(self):
        return self.get_text((By.XPATH, VS.group_column_video_tag_text_xpath))

    def get_record_date_column_text(self):
        return self.get_text((By.XPATH, VS.record_date_column_text_xpath))

    def get_video_tags_count(self):
        i = 0
        while i < 5:
            i += 1
            sleep(2)
            try:
                count = self.get_text((By.XPATH, VS.video_tags_count_text_xpath))
                if count.isdigit():
                    sleep(1)
                    break
            except (TimeoutException, StaleElementReferenceException):
                sleep(1)

        return self.get_text((By.XPATH, VS.video_tags_count_text_xpath))

    # Filters and select search criteria in video tags page
    def click_group_filter_video_tags(self):
        self.click((By.XPATH, VS.group_filter_video_tags_xpath))

    def search_group_video_tags(self, group_name):
        self.type((By.XPATH, VS.search_group_textbox_video_tags_xpath), group_name)

    def select_searched_group_video_tags(self):
        self.click((By.XPATH, VS.select_searched_group_video_tags_xpath))

    def click_done_button_video_tags(self):
        self.click((By.XPATH, VS.done_button_group_filter_video_tags_xpath))

    def click_date_filter_video_tags(self):
        self.click((By.XPATH, VS.date_filter_video_tags_xpath))

    def select_last_30_days_video_tags(self):
        self.click((By.XPATH, VS.last_30_days_video_tags_xpath))

    def select_last_90_days_video_tags(self):
        self.click((By.XPATH, VS.last_90_days_video_tags_xpath))

    def click_apply_button_video_tags(self):
        self.click((By.XPATH, VS.apply_date_button_video_tags_xpath))

    def click_category_filter(self):
        self.click((By.XPATH, VS.category_filter_xpath))

    def select_driver_tagged(self):
        self.click((By.XPATH, VS.driver_tagged_xpath))

    def click_reset_button_video_tags(self):
        self.click((By.XPATH, VS.reset_button_video_tags_xpath))

    def click_select_search_filter_video_tags(self):
        self.click((By.XPATH, VS.select_search_filter_video_tags_xpath))

    def select_tag_name_dropdown_video_tags(self):
        self.click((By.XPATH, VS.select_tag_name_dropdown_video_tags_xpath))

    def select_vehicle_name_dropdown_video_tags(self):
        self.click((By.XPATH, VS.select_vehicle_name_dropdown_video_tags_xpath))

    def search_criteria_textbox_video_tags(self, searched_name):
        self.type((By.XPATH, VS.search_criteria_textbox_video_tags_xpath), searched_name)

    def wake_button_is_displayed(self):
        return self.element_is_displayed((By.ID, VS.wake_button_id))

    def click_wake_button(self):
        self.click((By.ID, VS.wake_button_id))

    def get_number_of_vehicles_awake(self):
        elements = self.find_elements((By.XPATH, VS.browse_button_xpath))
        return len(elements)

    def click_browse_button(self, max_attempts=5):
        if self.get_number_of_vehicles_awake() < max_attempts:
            max_attempts = self.get_number_of_vehicles_awake()
        self.wait_for_element_displayed((By.XPATH, VS.browse_button_xpath))
        live_xpath = "(" + VS.browse_button_xpath + "[1]" + VS.live_button_additional_xpath
        live_button_visible = self.element_is_displayed((By.XPATH, live_xpath))
        self.click((By.XPATH, VS.browse_button_xpath))
        if self.video_expired_popup_is_displayed():
            self.click_video_expired_popup_ok_button()

        if self.wait_for_element_displayed((By.ID, VS.back_to_vehicles_button_id), 8):
            self.click((By.ID, VS.back_to_vehicles_button_id))
            attempts = 1
            while attempts <= max_attempts:
                self.wait_for_element_displayed((By.XPATH, VS.browse_button_xpath + f"[{attempts}]"))
                live_button_visible = self.element_is_displayed((By.XPATH, "(" + VS.browse_button_xpath + f"[{attempts}]" + VS.live_button_additional_xpath))
                self.click((By.XPATH, VS.browse_button_xpath + f"[{attempts}]"))
                if self.video_expired_popup_is_displayed():
                    self.click_video_expired_popup_ok_button()
                if self.wait_for_element_displayed((By.ID, VS.back_to_vehicles_button_id), 8):
                    self.click((By.ID, VS.back_to_vehicles_button_id))
                    attempts += 1
                    if attempts > max_attempts:
                        self.click((By.XPATH, VS.browse_button_xpath + f"[{attempts - 1}]"))
                        if self.video_expired_popup_is_displayed():
                            self.click_video_expired_popup_ok_button()
                        if self.wait_for_element_displayed((By.ID, VS.back_to_vehicles_button_id), 8):
                            raise TimeoutException(f"Connection issue persists after {max_attempts} attempts to click browse button.")
                else:
                    break
            else:
                # If we exit the loop without breaking, connection issue persists
                raise TimeoutException(f"Connection issue persists after {max_attempts} attempts to click browse button.")
        return live_button_visible

    def click_live_button(self, max_attempts=5):
        """
        Clicks the live button, retrying up to max_attempts if a connection issue is detected.
        """
        self.wait_for_element_displayed((By.XPATH, VS.live_button_xpath))
        self.click((By.XPATH, VS.live_button_xpath))

        if self.wait_for_element_displayed((By.ID, VS.back_to_vehicles_button_id), 8):
            self.click((By.ID, VS.back_to_vehicles_button_id))
            attempts = 1
            while attempts <= max_attempts:
                self.wait_for_element_displayed((By.XPATH, VS.live_button_xpath + f"[{attempts}]"))
                self.click((By.XPATH, VS.live_button_xpath + f"[{attempts}]"))
                if self.wait_for_element_displayed((By.ID, VS.back_to_vehicles_button_id), 8):
                    self.click((By.ID, VS.back_to_vehicles_button_id))
                    attempts += 1
                    if attempts > max_attempts:
                        self.click((By.XPATH, VS.live_button_xpath + f"[{attempts - 1}]"))
                        if self.wait_for_element_displayed((By.ID, VS.back_to_vehicles_button_id), 8):
                            break
                else:
                    break
            else:
                # If we exit the loop without breaking, connection issue persists
                raise TimeoutException(f"Connection issue persists after {max_attempts} attempts to click live button.")

    def browse_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, VS.browse_button_xpath))

    def browser_tab_is_active(self):
        self.wait_for_element_displayed((By.XPATH, VS.browser_tab_xpath))
        return 'active' in self.get_attribute((By.XPATH, VS.browser_tab_xpath), "class")

    def live_tab_is_active(self):
        self.wait_for_element_displayed((By.XPATH, VS.live_tab_xpath))
        return 'active' in self.get_attribute((By.XPATH, VS.live_tab_xpath), "class")

    def get_video_browser_title(self, video_browser):
        return self.wait_for_expected_text((By.XPATH, VS.video_browser_title_text_xpath), video_browser)

    def outside_view_live_tab_is_active(self):
        return 'selected' in self.get_attribute((By.XPATH, VS.outside_view_tab_xpath), "class")

    def map_displayed_live_tab(self):
        return self.element_is_displayed((By.XPATH, VS.map_live_tab_xpath))

    def get_gps_speed_text(self, gps_speed):
        return self.wait_for_expected_text((By.XPATH, VS.gps_speed_text_xpath), gps_speed)

    def click_first_video_name(self):
        self.click((By.XPATH, VS.first_video_name_xpath))

    def click_saved_video_name(self):
        self.click((By.XPATH, VS.saved_video_name_xpath))

    def click_completed_status_video(self):
        if self.get_text((By.XPATH, VS.first_video_status_xpath)) == 'In Progress':  # video download has not been completed (device went offline/etc)
            self.click((By.XPATH, VS.tenth_video_name_xpath))
        else:
            self.click((By.XPATH, VS.first_video_name_xpath))

    def get_video_player_title(self, expected_text):
        return self.wait_for_expected_text((By.XPATH, VS.video_player_title_xpath), expected_text)

    def video_play_time(self):
        return self.get_text((By.XPATH, VS.video_play_time_xpath))

    def video_play_time_changed(self, play_time):
        return self.wait_for_expected_text_change((By.XPATH, VS.video_play_time_xpath), play_time)

    def click_browser_tab(self):
        self.click((By.XPATH, VS.browser_tab_xpath))

    def click_save_to_library(self):
        self.click((By.XPATH, VS.save_to_library_xpath))

    def type_video_name(self, video_name):
        self.type((By.XPATH, VS.video_name_input_box_xpath), video_name)

    def click_save_button(self):
        self.click((By.ID, VS.save_button_id))

    def click_go_to_video_button(self):
        self.wait_for_element_displayed((By.XPATH, VS.go_to_video_button_xpath))
        self.click((By.XPATH, VS.go_to_video_button_xpath))

    def video_length_duration_is_displayed(self):
        self.wait_for_element_displayed((By.ID, VS.length_value_id))
        return self.element_is_displayed((By.ID, VS.length_value_id))

    def click_profile_icon(self):
        self.click((By.XPATH, VS.profile_xpath))

    def click_sign_out_button(self):
        self.click((By.XPATH, VS.sign_out_button_xpath))
        sleep(3)

    def vehicle_count_displayed(self):
        return self.element_is_displayed((By.XPATH, VS.vehicle_count_text_xpath))

    def get_vehicle_count_is_displayed(self):
        result = self.element_is_displayed((By.XPATH, VS.video_tags_count_text_xpath))
        return result

    def video_tag_count_is_displayed(self):
        self.wait_for_element_displayed((By.XPATH, VS.vehicle_count_text_xpath))
        result = self.element_is_displayed((By.XPATH, VS.vehicle_count_text_xpath))
        return result

    def get_row_count_for_video_tag(self):
        self.wait_for_element_displayed((By.TAG_NAME, "cdk-row"))
        result = self.element_is_displayed((By.TAG_NAME, "cdk-row"))
        if result is False:
            return self.get_text((By.XPATH, VS.no_vehicles_found_xpath)) == "No vehicles found."
        return result

    def click_vehicles_tab(self):
        self.click((By.XPATH, VS.vehicles_tab_xpath))

    def get_video_date(self):
        self.wait_for_element_displayed((By.XPATH, VS.video_date_xpath))
        return self.get_text((By.XPATH, VS.video_date_xpath))

    def retry_button_is_displayed(self):
        """
        Check if the retry button is displayed and attempt to click it up to 3 times.
        If after 3 attempts the button is still displayed, raise a TimeoutException.
        Returns False immediately if the button is not displayed at any check.
        """
        attempts = 0
        while attempts < 3:
            is_displayed = self.element_is_displayed((By.ID, VS.retry_button_id))
            if not is_displayed:
                return False
            # If displayed, click and wait briefly before re-checking
            self.click((By.ID, VS.retry_button_id))
            sleep(2)
            attempts += 1
            # If it disappears after click, consider it handled
            if not self.element_is_displayed((By.ID, VS.retry_button_id)):
                return False
        # Still displayed after 3 attempts
        raise TimeoutException("Retry button still displayed after 3 attempts.")

    def click_vehicle_tab_new(self):
        self.click((By.XPATH, VS.vehicles_menu_xpath))

    def click_library_tab_new(self):
        self.click((By.XPATH, VS.vs_library_menu_xpath))

    def click_saved_videos_tab_new(self):
        self.click((By.XPATH, VS.saved_videos_submenu_xpath))

    def click_video_tags_tab_new(self):
        self.click((By.XPATH, VS.video_tags_submenu_xpath))

    def saved_video_count_is_displayed(self):
        result = self.element_is_displayed((By.XPATH, VS.video_count_text_xpath))
        return result

    def get_row_count_for_saved_video(self):
        result = self.element_is_displayed((By.TAG_NAME, "cdk-row"))
        return result

    def get_count_of_rows_in_vehicles_pages(self):
        count = len(self.find_elements((By.XPATH, "//cdk-row[@class='cdk-row lytx-table-row']")))
        return count

    def click_pagination_dropdown(self):
        self.click((By.XPATH, VS.pagination_dropdown_xpath))

    def select_pagination_from_dropdown(self):
        self.click((By.XPATH, VS.select_pagination_xpath))

    def click_right_arrow_button(self):
        self.click((By.XPATH, VS.right_arrow_button_xpath))

    def click_left_arrow_button(self):
        self.click((By.XPATH, VS.left_arrow_button_xpath))

    def get_page_result(self):
        self.wait_for_element_displayed((By.XPATH, VS.page_result_xpath))
        return self.get_text((By.XPATH, VS.page_result_xpath))

    def edit_name_option_is_displayed(self):
        return self.element_is_displayed((By.XPATH, VS.edit_name_option_xpath))

    def get_video_name_text(self):
        return self.get_text((By.ID, VS.video_name_text_id))

    def get_vehicle_name_text(self):
        return self.get_text((By.ID, VS.vehicle_name_text_id))

    def get_view_text(self):
        return self.get_text((By.ID, VS.view_text_id))

    def get_video_length_text(self):
        return self.get_text((By.ID, VS.video_length_text_id))

    def get_video_date_text(self):
        return self.get_text((By.ID, VS.video_date_text_id))

    def get_request_date_text(self):
        return self.get_text((By.ID, VS.request_date_text_id))

    def click_last_7_days(self):
        self.click((By.XPATH, VS.last_7_days_xpath))

    def click_download_csv_button_in_vehicles_page(self):
        self.click((By.XPATH, VS.download_csv_button_in_vehicles_page_xpath))

    def get_vehicles_list_file_name(self):
        date_now = datetime.now(tz=pytz.timezone("US/Pacific")).strftime("%Y-%m-%d %H%M%S")
        file_name = 'Vehicles' + ' ' + date_now + '.csv'
        sleep(5)  # there is a 1–2sec delay in completing the download, so added a 5-sec sleep as a precaution
        return file_name

    def click_tooltip_icon(self):
        self.click((By.XPATH, VS.tooltip_icon_xpath))

    def device_information_title_is_displayed(self):
        return self.element_is_displayed((By.XPATH, VS.device_information_title_xpath))

    def device_serial_number_with_device_status_is_displayed(self):
        return self.element_is_displayed((By.ID, VS.device_serial_number_with_device_status_id))

    def last_communication_is_displayed(self):
        return self.element_is_displayed((By.ID, VS.last_communication_id))

    def date_filter_is_present(self):
        return self.element_is_displayed((By.XPATH, VS.date_filter_xpath))

    def save_video_button_is_present(self):
        self.scroll_page_down()
        return self.element_is_displayed((By.XPATH, VS.save_video_button_xpath))

    def vehicle_name_is_present(self):
        return self.element_is_displayed((By.XPATH, VS.vehicle_name_xpath))

    def play_pause_button_is_present(self):
        return self.element_is_displayed((By.XPATH, VS.play_pause_button_xpath))

    def playback_speed_option_is_present(self):
        return self.element_is_displayed((By.XPATH, VS.playback_speed_option_xpath))

    def time_dropdown_is_present(self):
        return self.element_is_displayed((By.XPATH, VS.time_dropdown_xpath))

    def trip_inprogress_markers_on_timeline_is_present(self):
        return self.element_is_displayed((By.XPATH, VS.trip_inprogress_markers_on_timeline_xpath))

    def alerts_on_timeline_is_present(self):
        return self.element_is_displayed((By.XPATH, VS.alerts_on_timeline_xpath))

    def events_on_timeline_is_present(self):
        return self.element_is_displayed((By.XPATH, VS.events_on_timeline_xpath))

    def select_the_vehicle_from_the_list(self):
        self.click((By.XPATH, VS.select_the_vehicle_xpath))

    def click_delete_button(self):
        self.click((By.XPATH, VS.delete_button_xpath))

    def click_confirm_button(self):
        self.click((By.ID, VS.confirm_button_id))

    def video_deleted_popup_is_displayed(self):
        self.wait_for_element_displayed((By.XPATH, VS.video_deleted_popup_xpath))
        return self.element_is_displayed((By.XPATH, VS.video_deleted_popup_xpath))

    def click_download_icon(self):
        self.wait_for_element_displayed((By.XPATH, VS.download_icon_xpath))
        self.click((By.XPATH, VS.download_icon_xpath))

    def click_download_dce_button(self):
        self.click((By.XPATH, VS.download_dce_button_xpath))

    def click_download_button(self):
        self.click((By.XPATH, VS.download_button_xpath))
        sleep(5)  # there is a delay in start downloading, so added a 40sec sleep as a precaution

    def get_downloaded_dce_file_name(self):
        date_now = (datetime.now(tz=pytz.timezone("US/Pacific")) - timedelta(days=1)).strftime("%Y-%m-%d")
        file_name = date_now + ' ' + 'Save Video Test' + '.zip'
        sleep(5)  # there is a 1–2sec delay in completing the download, so added a 5-sec sleep as a precaution
        return file_name

    def get_downloaded_mp4_file_name(self):
        date_now = (datetime.now(tz=pytz.timezone("US/Pacific")) - timedelta(days=1)).strftime("%Y-%m-%d")
        file_name = date_now + ' ' + 'Save Video Test(1)' + '.zip'
        sleep(5)  # there is a 1–2sec delay in completing the download, so added a 5-sec sleep as a precaution
        return file_name

    def get_downloaded_mp4_file_name_for_video_stitching(self):
        return "Save Video Test 1 View - INSIDE_OUTSIDE.mp4"
        # date_now = datetime.now(tz=pytz.timezone("US/Pacific")).strftime("%Y-%m-%d")
        # return f"{date_now} Save Video Test 1 View - INSIDE_OUTSIDE.mp4"


    def get_error_message_text(self):
        return self.get_text((By.XPATH, VS.error_message_xpath))

    def click_map_search_tab(self):
        self.click((By.XPATH, VS.map_search_tab_xpath))

    def click_date_filter(self):
        self.click((By.XPATH, VS.date_filter_xpath))

    def select_date(self):
        self.click((By.XPATH, VS.select_date_xpath))

    def click_time_filter(self):
        self.click((By.XPATH, VS.time_filter_xpath))

    def select_time_in_filter(self):
        self.click((By.XPATH, VS.select_time_in_filter_xpath))

    def click_search_address_box_map_search(self):
        self.click((By.XPATH, VS.search_address_box_map_search_xpath))

    def enter_address_in_search_box_map_search(self, address):
        self.type((By.XPATH, VS.search_address_box_map_search_xpath), address)
        self.click((By.XPATH, VS.time_filter_xpath))
        self.click((By.XPATH, VS.search_address_box_map_search_xpath))

    def select_searched_address_map_search(self):
        self.click((By.XPATH, VS.search_address_box_map_search_xpath))
        try:
            self.wait_for_element_displayed((By.XPATH, VS.select_searched_address_map_search_xpath))
            self.click((By.XPATH, VS.select_searched_address_map_search_xpath))
        except (StaleElementReferenceException, TimeoutException):
            self.click((By.XPATH, VS.select_searched_address_map_search_xpath))

    def get_selected_time_range(self):
        self.wait_for_element_displayed((By.XPATH, VS.selected_time_range_xpath))
        return self.get_text((By.XPATH, VS.selected_time_range_xpath))

    def video_expired_popup_is_displayed(self):
        return self.element_is_displayed((By.XPATH, VS.video_expired_popup_xpath))

    def click_video_expired_popup_ok_button(self):
        self.click((By.ID, VS.video_expired_popup_ok_button_id))

    def select_1_view_from_available_views_dropdown(self):
        self.click((By.XPATH, VS.available_views_dropdown_xpath))
        self.click((By.XPATH, VS.select_1_view_from_available_views_xpath))

    def map_is_displayed(self):
        self.wait_for_element_displayed((By.XPATH, VS.map_tab_xpath))
        return self.element_is_displayed((By.XPATH, VS.map_tab_xpath))

    def map_zoom_in_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, VS.map_zoom_in_button_xpath))

    def map_zoom_out_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, VS.map_zoom_out_button_xpath))

    def map_camera_control_button_is_displayed(self):
        return self.element_is_displayed((By.XPATH, VS.map_camera_control_button_xpath))

    def click_view_icon(self):
        self.click((By.XPATH, VS.view_on_icon_xpath))

    def select_1st_view(self):
        self.click((By.XPATH, VS.select_1st_view_xpath))

    def view_1_is_displayed(self):
        return self.element_is_displayed((By.XPATH, VS.view_1_displayed_xpath))

    def view_2_is_displayed(self):
        return self.element_is_displayed((By.XPATH, VS.view_2_displayed_xpath))

    def click_vehicle_dropdown(self):
        self.click((By.XPATH, VS.vehicle_dropdown_xpath))

    def click_map_browse_button(self):
        self.click((By.XPATH, VS.map_browse_button_xpath))

    def enable_video_stitching_section_is_displayed(self):
        return self.element_is_displayed((By.XPATH, VS.enable_video_stitching_section_xpath))

    def click_views_dropdown(self):
        self.click((By.XPATH, VS.views_dropdown_xpath))

    def select_inside_view(self):
        self.click((By.XPATH, VS.select_outside_view_xpath))

    def select_outside_view(self):
        self.click((By.XPATH, VS.select_inside_view_xpath))

    def deselect_inside_view(self):
        self.click((By.XPATH, VS.deselect_inside_view_xpath))

    def select_media_type_dce(self):
        self.click((By.XPATH, VS.media_type_dce_xpath))

    def enable_stitching_toggle(self):
        self.click((By.XPATH, VS.enable_stitching_toggle_xpath))

    def click_download_button(self):
        self.click((By.XPATH, VS.download_button_xpath))
        sleep(5)  # there is a delay in start downloading, so added a 60-sec sleep as a precaution

    def get_error_message_text_download_hd_video_longer_than_3_minutes(self):
        return self.get_text((By.XPATH, VS.error_message_download_hd_video_longer_than_3_minutes_xpath))

    def click_cancel_button(self):
        self.click((By.XPATH, VS.cancel_button_xpath))

    def cross_button_is_present(self):
        return self.element_is_displayed((By.XPATH, VS.cross_button_xpath))

    def click_download_mp4_button(self):
        self.click((By.XPATH, VS.download_mp4_button_xpath))

    def click_cross_button(self):
        self.click((By.XPATH, VS.cross_button_xpath))