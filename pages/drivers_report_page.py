from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from selenium.webdriver.common.by import By

from locators.locators_drivers_report_page import LocatorsDriversReportPage as DR
from pages.base_page import BasePage


def parse_event_date(raw_text):
    """
    Parses a date string like 'Dec 2, 2025, 2:03:58 AM PST'
    Returns a datetime object.
    """
    if not raw_text:
        return None

    # Split the string by spaces and remove the last token (timezone)
    parts = raw_text.split(" ")
    cleaned_text = " ".join(parts[:-1])  # removes 'PST'

    # Now parse without timezone
    parsed_date = datetime.strptime(cleaned_text, "%b %d, %Y, %I:%M:%S %p")
    return parsed_date


class DriversReportPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_driver_text(self):
        return self.get_text((By.XPATH, DR.driver_text_xpath))

    def get_group_text(self):
        return self.get_text((By.XPATH, DR.group_text_xpath))

    def get_coachable_score_text(self):
        return self.get_text((By.XPATH, DR.coachable_score_text_xpath))

    def get_coachable_events_text(self):
        return self.get_text((By.XPATH, DR.coachable_events_text_xpath))

    def get_total_score_text(self):
        return self.get_text((By.XPATH, DR.total_score_text_xpath))

    def get_total_events_text(self):
        return self.get_text((By.XPATH, DR.total_events_text_xpath))

    def click_filter_group(self):
        self.click((By.XPATH, DR.filter_by_group_button_xpath))

    def search_filter_group(self, search_text):
        self.type((By.XPATH, DR.search_by_group_textbox_xpath), search_text)

    def select_search_filter(self):
        self.click((By.XPATH, DR.select_search_button_xpath))

    def click_done(self):
        self.click((By.XPATH, DR.done_button_xpath))

    def select_date_filter(self):
        self.click((By.XPATH, DR.date_filter_textbox_xpath))

    def select_from_date(self):
        self.click((By.XPATH, DR.from_date_textbox_xpath))

    def select_end_date(self):
        self.click((By.XPATH, DR.end_date_textbox_xpath))

    def click_apply(self):
        self.click((By.XPATH, DR.apply_button_xpath))

    def click_behavior(self):
        self.click((By.XPATH, DR.behavior_textbox_xpath))

    def select_behavior(self):
        self.click((By.XPATH, DR.behavior_textbox_xpath))
        self.click((By.XPATH, DR.select_behavior_dropdown_xpath))
        self.click((By.XPATH, DR.close_behavior_list))

    def search_by_name(self, search_id):
        self.type((By.XPATH, DR.search_name_textbox_xpath), search_id)

    def select_search_name(self):
        self.wait_for_element_displayed((By.XPATH, DR.select_search_name_dropdown_xpath))
        self.click((By.XPATH, DR.select_search_name_dropdown_xpath))

    def click_reset_driver_score(self):
        self.click((By.XPATH, DR.reset_button_driver_score_xpath))

    def back_to_previous_page(self):
        self.back()

    def click_continual(self):
        self.click((By.XPATH, DR.continual_behavior_link_xpath))

    def get_continual_behaviors_text(self):
        return self.get_text((By.XPATH, DR.continual_behavior_link_xpath))

    def get_driver_behave_text(self):
        return self.get_text((By.XPATH, DR.driver_behave_text_xpath))

    def get_driver_name_behave(self):
        return self.get_text((By.XPATH, DR.driver_name_behave_xpath))

    def get_group_behave_text(self):
        return self.get_text((By.XPATH, DR.group_behave_text_xpath))

    def get_continual_behavior_1st(self):
        return self.get_text((By.XPATH, DR.continual_1st_behavior_xpath))

    def get_driver_behave_num(self):
        return self.get_text((By.XPATH, DR.driver_behave_num_text_xpath))

    def click_filter_group_behave(self):
        self.click((By.XPATH, DR.filter_group_behave_button_xpath))

    def search_group_behave(self, search_text_behave):
        self.type((By.XPATH, DR.search_filter_group_behave_textbox_xpath), search_text_behave)

    def select_search_filter_behave(self):
        self.click((By.XPATH, DR.select_search_filter_behave_button_xpath))

    def click_done_search_behave(self):
        self.click((By.XPATH, DR.done_search_filter_behave_button_xpath))

    def click_date_filter_behave(self):
        self.click((By.XPATH, DR.date_filter_behave_button_xpath))

    def select_from_date_behave(self):
        self.click((By.XPATH, DR.from_date_filter_behave_button_xpath))

    def select_end_date_behave(self):
        self.click((By.XPATH, DR.end_date_filter_behave_button_xpath))

    def click_apply_date_behave(self):
        self.click((By.XPATH, DR.date_behave_apply_button_xpath))

    def clear_search_name_behave(self):
        self.clear((By.XPATH, DR.search_name_behave_textbox_xpath))

    def search_name_behave(self, search_name_text_behave):
        self.type((By.XPATH, DR.search_name_behave_textbox_xpath), search_name_text_behave)

    def select_search_name_behave(self):
        self.wait_for_element_displayed((By.XPATH, DR.select_search_behave_button_xpath))
        self.click((By.XPATH, DR.select_search_behave_button_xpath))

    def click_driver_name(self):
        self.click((By.XPATH, DR.driver_name_link_xpath))

    # Alert
    def click_alert_link(self):
        self.click((By.XPATH, DR.alert_link_text_xpath))

    def get_alerts_text(self):
        return self.get_text((By.XPATH, DR.driver_alert_text_xpath))

    def get_driver_alert_text(self):
        return self.get_text((By.XPATH, DR.driver_alert_text_xpath))

    def get_group_alert_text(self):
        return self.get_text((By.XPATH, DR.group_alert_text_xpath))

    def get_total_alerts_text(self):
        return self.get_text((By.XPATH, DR.total_alerts_text_xpath))

    def get_handheld_alert_text(self):
        return self.get_text((By.XPATH, DR.handheld_alert_text_xpath))

    def get_inattentive_alert_text(self):
        return self.get_text((By.XPATH, DR.inattentive_alert_text_xpath))

    def get_food_or_drink_alert_text(self):
        return self.get_text((By.XPATH, DR.food_or_drink_alert_text_xpath))

    def get_driver_smoking_alert_text(self):
        return self.get_text((By.XPATH, DR.driver_smoking_alert_text_xpath))

    def get_policy_speed_alert_text(self):
        return self.get_text((By.XPATH, DR.policy_speed_alert_text_xpath))

    def get_posted_speed_alert_text(self):
        return self.get_text((By.XPATH, DR.posted_speed_alert_text_xpath))

    def get_no_seat_belt_alert_text(self):
        return self.get_text((By.XPATH, DR.no_seat_belt_alert_text_xpath))

    def get_lens_obstruct_alert_text(self):
        return self.get_text((By.XPATH, DR.lensobst_alert_text_xpath))

    def get_lane_departed_alert_text(self):
        return self.get_text((By.XPATH, DR.lane_depart_alert_text_xpath))

    def get_rolling_alert_text(self):
        return self.get_text((By.XPATH, DR.rolling_alert_text_xpath))

    def get_follow_dist_alert(self):
        return self.get_text((By.XPATH, DR.following_distance_alert_text_xpath))

    def get_critical_dist_alert(self):
        return self.get_text((By.XPATH, DR.critical_distance_alert_text_xpath))

    def get_num_driver_alert(self):
        return self.get_text((By.XPATH, DR.num_driver_alert_text_xpath))

    # Filtergroupalert
    def click_filter_alert_group(self):
        self.click((By.XPATH, DR.filter_group_alert_button_xpath))

    def search_filter_group_alert(self, search_group_alert):
        self.type((By.XPATH, DR.search_filter_group_alert_textbox_xpath), search_group_alert)

    def select_search_filter_group_alert(self):
        self.click((By.XPATH, DR.select_search_filter_group_alert_button_xpath))

    def click_done_filter_group_alert(self):
        self.click((By.XPATH, DR.done_button_alert_button_xpath))

    # Datefilteralert
    def click_filter_date_alert(self):
        self.click((By.XPATH, DR.date_filter_alert_textbox_xpath))

    def select_from_date_alert(self):
        self.click((By.XPATH, DR.from_date_alert_textbox_xpath))

    def select_end_date_alert(self):
        self.click((By.XPATH, DR.end_date_alert_textbox_xpath))

    def click_apply_date_alert(self):
        self.click((By.XPATH, DR.apply_date_alert_button_xpath))

    # behavioralert
    def click_behave_alert(self):
        self.click((By.XPATH, DR.behavior_alert_textbox_xpath))

    def select_behave_alert(self):
        self.click((By.XPATH, DR.select_behavior_alert_button_xpath))
        self.click((By.XPATH, DR.close_behavior_alert_list))

    # Searchname
    def clear_search_name_alert(self):
        self.clear((By.XPATH, DR.search_name_alert_textbox_xpath))

    def search_name_alert(self, search_name_alert):
        self.type((By.XPATH, DR.search_name_alert_textbox_xpath), search_name_alert)

    def select_search_name_alert(self):
        self.wait_for_element_displayed((By.XPATH, DR.select_search_name_alert_button_xpath))
        self.click((By.XPATH, DR.select_search_name_alert_button_xpath))

    def click_reset_alert(self):
        self.click((By.XPATH, DR.reset_button_alert_xpath))

    # DriverProfile
    def click_profile_link_behave(self):
        self.click((By.XPATH, DR.driver_link_text_xpath))

    def get_driver_profile_behave_text(self):
        return self.get_text((By.XPATH, DR.driver_profile_text_xpath))

    def click_profile_link_alert(self):
        self.click((By.XPATH, DR.driver_link_alert_text_xpath))

    def get_driver_profile_alert_text(self):
        return self.get_text((By.XPATH, DR.driver_profile_alert_text_xpath))

    def click_driver_scores_link(self):
        self.click((By.XPATH, DR.driver_score_link_text_xpath))

    def get_driver_scores_text(self):
        return self.get_text((By.XPATH, DR.driver_score_profile_text_xpath))

    def get_driver_profile_driver_scores(self):
        return self.get_text((By.XPATH, DR.driver_score_profile_text_xpath))

    def task_count_displayed(self):
        self.wait_for_element_displayed((By.XPATH, DR.total_count))
        elements = self.find_elements((By.XPATH, DR.total_count))
        return len(elements) > 0

    def get_first_group_name(self):
        return self.get_text((By.XPATH, DR.first_group_name_xpath))

    def get_length_of_columns(self):
        count = self.find_elements((By.XPATH, DR.length_of_columns_xpath))
        return len(count)

    def get_first_driver_name(self):
        driver_full_name = self.get_text((By.XPATH, DR.driver_name_behave_xpath))
        driver = driver_full_name.split(' ')
        if len(driver) > 2:
            driver_full_name = driver[0] + ' ' + driver[1]
        return driver_full_name

    def click_reset(self):
        self.click((By.XPATH, DR.reset_button_xpath))

    def click_download(self):
        self.click((By.XPATH, DR.download_button_xpath))

    def dropdown_is_displayed(self):
        return self.element_is_displayed((By.XPATH, DR.download_button_xpath))

    def click_download_csv(self):
        self.click((By.XPATH, DR.driver_event_history_csv_xpath))

    def click_driver_event_history_report(self):
        self.click((By.XPATH, DR.driver_event_history_report_xpath))

    def get_driver_event_history_file_name(self, driver2):
        file_name = f"{driver2} Driver Event History.pdf"
        return file_name

    def get_driver_name_file_name(self, driver2):
        pst_now = datetime.now(ZoneInfo("America/Los_Angeles"))
        today = pst_now.strftime("%Y-%m-%d")
        date_90_days_ago = (pst_now - timedelta(days=89)).strftime("%Y-%m-%d")
        file_name = f"{driver2} Events {date_90_days_ago}_{today}.csv"
        return file_name

    def click_continual_behave_tab_in_driver_profile(self):
        self.click((By.XPATH, DR.continual_behave_tab_in_driver_profile_xpath))

    def browse_or_wake_link_is_displayed(self):
        return self.element_is_displayed((By.XPATH, DR.browse_or_wake_link_xpath))

    def click_first_driver_name(self):
        self.click((By.XPATH, DR.driver_name_link_xpath))
        self.wait_for_element_displayed((By.XPATH, DR.event_id_text_xpath))
        self.scroll_page_down()
        return self.get_text((By.XPATH, DR.event_id_text_xpath))
    def get_event_dates(self):
        elements = self.driver.find_elements(By.XPATH, DR.event_dates_xpath)

        dates = []
        for e in elements:
            raw_text = e.text.strip()
            if not raw_text:
                continue
            try:
                parsed_date = parse_event_date(raw_text)
                dates.append(parsed_date)
            except Exception as ex:
                print(f"Failed to parse date '{raw_text}': {ex}")
                continue  # skip invalid rows

        return dates

    def are_event_dates_descending(self):
        dates = self.get_event_dates()
        return dates == sorted(dates, reverse=True)

