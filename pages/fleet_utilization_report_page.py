from selenium.webdriver.common.by import By

from locators.locators_fleet_utilization_report import FleetUtilizationReport as FUL
from pages.base_page import BasePage


class FleetUtilizationReportPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_fleet_utilization(self):
        self.click((By.XPATH, FUL.fleet_utilization_tab_xpath))

    def utilization_report_displayed(self):
        self.wait_for_element_displayed((By.XPATH, FUL.fleet_utilization_text_xpath))
        return self.element_is_displayed((By.XPATH, FUL.fleet_utilization_text_xpath))

    def get_distance_page_url(self):
        return self.get_current_url()

    def click_distance_tab(self):
        self.click((By.XPATH, FUL.distance_tab_xpath))

    def select_date_filter_group(self):
        self.click((By.XPATH, FUL.date_filter_xpath))

    def set_fleet_utilization_date_range(self, start_month, start_day, start_year, end_month, end_day, end_year):
        self.click((By.XPATH, FUL.fleet_utilization_date_range_start_month_xpath))
        self.type((By.XPATH, FUL.fleet_utilization_date_range_start_month_xpath), start_month)
        self.click((By.XPATH, FUL.fleet_utilization_date_range_start_day_xpath))
        self.type((By.XPATH, FUL.fleet_utilization_date_range_start_day_xpath), start_day)
        self.click((By.XPATH, FUL.fleet_utilization_date_range_start_year_xpath))
        self.type((By.XPATH, FUL.fleet_utilization_date_range_start_year_xpath), start_year)
        self.click((By.XPATH, FUL.fleet_utilization_date_range_end_month_xpath))
        self.type((By.XPATH, FUL.fleet_utilization_date_range_end_month_xpath), end_month)
        self.click((By.XPATH, FUL.fleet_utilization_date_range_end_day_xpath))
        self.type((By.XPATH, FUL.fleet_utilization_date_range_end_day_xpath), end_day)
        self.click((By.XPATH, FUL.fleet_utilization_date_range_end_year_xpath))
        self.type((By.XPATH, FUL.fleet_utilization_date_range_end_year_xpath), end_year)

    def click_apply(self):
        self.click((By.XPATH, FUL.date_filter_apply_button_xpath))

    def get_row_count_for_distance_by_group(self):
        return len(self.find_elements((By.XPATH, FUL.get_group_row_count_xpath)))

    def get_row_count_for_distance_by_vehicle(self):
        return len(self.find_elements((By.XPATH, FUL.get_vehicle_row_count_xpath)))

    def get_distance_trend(self):
        return self.element_is_displayed((By.XPATH, FUL.distance_trend_graph_xpath))

    def click_filter_group(self):
        self.scroll_page_up()
        self.click((By.XPATH, FUL.group_filter_xpath))

    def search_filter_group(self, search_text):
        self.type((By.XPATH, FUL.search_by_group_textbox_xpath), search_text)

    def select_search_filter(self):
        self.click((By.XPATH, FUL.select_search_button_xpath))

    def click_done(self):
        self.click((By.XPATH, FUL.done_button_xpath))

    def get_fleet_utilization_distance_trend_title(self):
        return self.get_text((By.XPATH, FUL.average_distance_text_xpath))

    def get_fleet_utilization_distance_group_title(self):
        return self.get_text((By.XPATH, FUL.distance_group_text_xpath))

    def get_fleet_utilization_distance_vehicle_title(self):
        return self.get_text((By.XPATH, FUL.distance_vehicle_text_xpath))

    def click_reset_button(self):
        self.click((By.XPATH, FUL.reset_button_xpath))

    def click_view_details_of_group_widget(self):
        self.click((By.XPATH, FUL.group_widget_view_details_xpath))

    def get_fleet_operations_title(self):
        return self.get_text((By.ID, FUL.fleet_operations_title_id))

    def click_group_name_in_group_widget(self):
        self.click((By.XPATH, FUL.group_name_xpath))

    def get_group_filter_text(self):
        return self.get_text((By.XPATH, FUL.fleet_operation_group_filter_text_xpath))

    def get_fleet_operations_groups_tab(self):
        return self.get_text((By.XPATH, FUL.groups_tab_text_xpath))

    def click_view_details_of_vehicle_widget(self):
        self.click((By.XPATH, FUL.vehicle_widget_view_details_xpath))

    def get_fleet_operations_vehicle_tab(self):
        return self.get_text((By.XPATH, FUL.vehicle_tab_text_xpath))

    def click_vehicle_name_in_vehicle_widget(self):
        self.click((By.XPATH, FUL.vehicle_name_xpath))

    def get_vehicle_profile_text_title(self):
        return self.get_text((By.XPATH, FUL.vehicle_profile_text_title_xpath))

    def click_engine_hours_tab(self):
        self.wait_for_element_is_clickable((By.XPATH, FUL.engine_hours_tab_xpath))
        self.click((By.XPATH, FUL.engine_hours_tab_xpath))

    def get_average_engine_hours_trend_title(self):
        return self.get_text((By.XPATH, FUL.engine_hours_trend_text_xpath))

    def get_engine_hours_by_group_title(self):
        return self.get_text((By.XPATH, FUL.engine_hours_group_text_xpath))

    def get_engine_hours_by_vehicle_title(self):
        return self.get_text((By.XPATH, FUL.engine_hours_vehicle_text_xpath))

    def set_fleet_utilization_engine_hours_date_range(self, start_month, start_day, start_year, end_month, end_day,
                                                      end_year):
        self.click((By.XPATH, FUL.fleet_utilization_date_range_start_month_xpath))
        self.type((By.XPATH, FUL.fleet_utilization_date_range_start_month_xpath), start_month)
        self.click((By.XPATH, FUL.fleet_utilization_date_range_start_day_xpath))
        self.type((By.XPATH, FUL.fleet_utilization_date_range_start_day_xpath), start_day)
        self.click((By.XPATH, FUL.fleet_utilization_date_range_start_year_xpath))
        self.type((By.XPATH, FUL.fleet_utilization_date_range_start_year_xpath), start_year)
        self.click((By.XPATH, FUL.fleet_utilization_date_range_end_month_xpath))
        self.type((By.XPATH, FUL.fleet_utilization_date_range_end_month_xpath), end_month)
        self.click((By.XPATH, FUL.fleet_utilization_date_range_end_day_xpath))
        self.type((By.XPATH, FUL.fleet_utilization_date_range_end_day_xpath), end_day)
        self.click((By.XPATH, FUL.fleet_utilization_date_range_end_year_xpath))
        self.type((By.XPATH, FUL.fleet_utilization_date_range_end_year_xpath), end_year)

    def get_row_count_for_engine_hours_by_group(self):
        return len((By.XPATH, FUL.engine_hours_group_row_count_xpath))

    def get_row_count_for_engine_hours_by_vehicle(self):
        return len((By.XPATH, FUL.engine_hours_vehicle_row_count_xpath))

    def get_engine_hours_trend(self):
        return self.element_is_displayed((By.XPATH,FUL.engine_hours_trend_graph_xpath))

    def get_engine_group_filter_text(self):
        return self.get_text((By.XPATH, FUL.engine_fleet_operation_group_filter_text_xpath))

    def get_group_column_name_title_of_group_widget(self):
        return self.get_text((By.XPATH, FUL.group_column_name_title_of_group_widget_xpath))

    def get_total_vehicle_column_name_title_of_group_widget(self):
        return self.get_text((By.XPATH, FUL.total_vehicle_column_name_title_of_group_widget_xpath))

    def get_total_column_name_title_of_group_widget(self):
        return self.get_text((By.XPATH, FUL.total_column_name_title_of_group_widget_xpath))

    def get_avg_day_column_name_title_of_group_widget(self):
        return self.get_text((By.XPATH, FUL.avg_day_column_name_title_of_group_widget_xpath))

    def get_vehicle_column_name_title_of_vehicle_widget(self):
        return self.get_text((By.XPATH, FUL.vehicle_column_name_title_of_vehicle_widget_xpath))

    def get_group_column_name_title_of_vehicle_widget(self):
        return self.get_text((By.XPATH, FUL.group_column_name_title_of_vehicle_widget_xpath))

    def get_total_column_name_title_of_vehicle_widget(self):
        return self.get_text((By.XPATH, FUL.total_column_name_title_of_vehicle_widget_xpath))

    def get_avg_day_column_name_title_of_vehicle_widget(self):
        return self.get_text((By.XPATH, FUL.avg_day_column_name_title_of_vehicle_widget_xpath))








