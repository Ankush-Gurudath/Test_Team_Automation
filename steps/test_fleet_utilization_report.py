from time import sleep
from pytest_bdd import scenarios, when, then, given
from pages.fleet_utilization_report_page import FleetUtilizationReportPage
from pages.fleet_insights_page import FleetInsightsPage
from pages.fleet_insights_page import FleetInsightEquipmentStatusAssetType as AssetType
from pages.login_page import LoginPage
from steps.common import FLEET_URL, ENV
from data.int.fleet_utilization_report_data_int import FleetUtilizationReportDataInt as FUR_INT
from data.stg.fleet_utilization_report_data_stg import FleetUtilizationReportDataSTG as FUR_STG
from data.prod.fleet_utilization_report_data_prod import FleetUtilizationReportDataProd as FUR_PROD

LOGIN_PAGE = 0
FUR = 0
FLEET_UTILIZATION_REPORT_PAGE = 0
FLEET_INSIGHTS_PAGE = 0

scenarios('../features/fleet_utilization_report.feature')


# LQ-52158
@given('the user is login with "Fleet Dispatcher"')
def login_to_fleet_page(browser):
    global LOGIN_PAGE, FLEET_UTILIZATION_REPORT_PAGE, FUR, FLEET_INSIGHTS_PAGE

    LOGIN_PAGE = LoginPage(browser)
    FLEET_INSIGHTS_PAGE = FleetInsightsPage(browser)
    FLEET_UTILIZATION_REPORT_PAGE = FleetUtilizationReportPage(browser)

    browser.get(FLEET_URL)

    if ENV == 'int':
        FUR = FUR_INT
    elif ENV == 'stg':
        FUR = FUR_STG
    else:
        FUR = FUR_PROD

    LOGIN_PAGE.enter_username(FUR.username)
    LOGIN_PAGE.enter_password(FUR.password)

    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed(FLEET_URL, FUR.username, FUR.password)


# LQ-52518
@when('the user clicks "Insights" and the user clicks "Fleet Utilization"')
def navigate_to_insights_and_utilization_report():
    FLEET_INSIGHTS_PAGE.click_insights()
    FLEET_UTILIZATION_REPORT_PAGE.click_fleet_utilization()


@then('the Distance tab of Fleet Utilization is displayed')
def utilization_report_displayed():
    FLEET_UTILIZATION_REPORT_PAGE.click_distance_tab()
    assert FLEET_UTILIZATION_REPORT_PAGE.get_distance_page_url() == FUR.distance_page_url


# LQ-47531
@when('the user sets date in the date filter')
def set_date_filter_in_distance_tab():
    FLEET_UTILIZATION_REPORT_PAGE.select_date_filter_group()
    FLEET_UTILIZATION_REPORT_PAGE.set_fleet_utilization_date_range(FUR.fleet_utilization_date_range_start_month,
                                                                   FUR.fleet_utilization_date_range_start_day,
                                                                   FUR.fleet_utilization_date_range_start_year,
                                                                   FUR.fleet_utilization_date_range_end_month,
                                                                   FUR.fleet_utilization_date_range_end_day,
                                                                   FUR.fleet_utilization_date_range_end_year)
    sleep(2)
    FLEET_UTILIZATION_REPORT_PAGE.click_apply()


@then('the data with selected filters are displayed on the "Average Distance" trend, "Distance by Group", "Distance '
      'by Vehicle"')
def fleet_utilization_filter_distance_tab():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_row_count_for_distance_by_group() <= 10
    assert FLEET_UTILIZATION_REPORT_PAGE.get_row_count_for_distance_by_vehicle() <= 10
    assert FLEET_UTILIZATION_REPORT_PAGE.get_distance_trend() == True

# LQ-47527
@when('the user sets group filter to one group')
def set_group_filter():
    FLEET_UTILIZATION_REPORT_PAGE.click_filter_group()
    FLEET_UTILIZATION_REPORT_PAGE.search_filter_group(FUR.group)
    FLEET_UTILIZATION_REPORT_PAGE.select_search_filter()
    FLEET_UTILIZATION_REPORT_PAGE.click_done()


@then('the data with selected filters are displayed on the "Average Distance" trend, "Distance by Group", "Distance '
      'by Vehicle"')
def data_with_selected_filter_displayed():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_utilization_distance_trend_title() == 'Average Distance (mi)'
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_utilization_distance_group_title() == 'Distance By Group'
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_utilization_distance_vehicle_title() == 'Distance By Vehicle'
    assert FLEET_UTILIZATION_REPORT_PAGE.get_row_count_for_distance_by_group() <= 10
    assert FLEET_UTILIZATION_REPORT_PAGE.get_row_count_for_distance_by_vehicle() <= 10


# LQ-47538
@when('the user clicks "Fleet Utilization"')
def distance_by_group_widget_is_displayed():
    # when part of LQ-47538 is covered in LQ-47527 testcase
    print("no action needed here")


@then('Distance by Group table  is displayed with columns "GROUP", "TOTAL VEHICLE", "TOTAL", "AVG/DAY"')
def assert_distance_by_group_widget():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_group_column_name_title_of_group_widget() == "GROUP"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_total_vehicle_column_name_title_of_group_widget() == "TOTAL VEHICLES"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_total_column_name_title_of_group_widget() == "TOTAL"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_avg_day_column_name_title_of_group_widget() == "AVG/DAY"


# LQ-47540
@when('the user clicks "Fleet Utilization" in Insights')
def distance_by_vehicle_widget_is_displayed():
    # when part of LQ-47540 is covered in LQ-47527 testcase
    print("no action needed here")

@then('Distance by Vehicle table is displayed with columns "VEHICLE", "GROUP", "TOTAL", "AVG/DAY"')
def assert_distance_by_vehicle_widget():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_vehicle_column_name_title_of_vehicle_widget() == "VEHICLE"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_group_column_name_title_of_vehicle_widget() == "GROUP"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_total_column_name_title_of_vehicle_widget() == "TOTAL"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_avg_day_column_name_title_of_vehicle_widget() == "AVG/DAY"


# LQ-52160
@when('the user clicks "view details" in Distance by Group widget')
def click_distance_by_group_hyper_link():
    FLEET_UTILIZATION_REPORT_PAGE.click_view_details_of_group_widget()


@then('the "fleet operation group tab" page is displayed')
def fleet_operation_group_tab_displayed():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_operations_title() == "FLEET OPERATIONS"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_operations_groups_tab() == "Groups"


# LQ-74987
@when('the user clicks "group name" from group column in Distance by Group table')
def click_distance_by_group_group_name_link():
    FLEET_INSIGHTS_PAGE.click_insights()
    FLEET_UTILIZATION_REPORT_PAGE.click_fleet_utilization()
    FLEET_UTILIZATION_REPORT_PAGE.click_group_name_in_group_widget()


@then('the fleet operation group page is displayed with same group filter')
def fleet_operation_page_displayed():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_operations_title() == "FLEET OPERATIONS"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_operations_groups_tab() == "Groups"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_group_filter_text() == "SF400 Kam-Way Alpha Trial"


# LQ-47532
@when('the user clicks "view details" in Distance by Vehicle widget')
def click_distance_by_vehicle_view_details_hyper_link():
    FLEET_INSIGHTS_PAGE.click_insights()
    FLEET_UTILIZATION_REPORT_PAGE.click_fleet_utilization()
    FLEET_UTILIZATION_REPORT_PAGE.click_view_details_of_vehicle_widget()


@then('the "fleet operation vehicle tab" page is displayed')
def fleet_operation_vehicle_tab_displayed():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_operations_title() == "FLEET OPERATIONS"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_operations_vehicle_tab() == "Vehicles"


# LQ-47532
@when('the user clicks "vehicle name" in Distance by Vehicle widget')
def click_distance_by_vehicle_vehicle_name_link():
    FLEET_INSIGHTS_PAGE.click_insights()
    FLEET_UTILIZATION_REPORT_PAGE.click_fleet_utilization()
    FLEET_UTILIZATION_REPORT_PAGE.click_vehicle_name_in_vehicle_widget()


@then('the "vehicle profile" page is displayed')
def vehicle_profile_page_displayed():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_vehicle_profile_text_title() == "VEHICLE PROFILE"


# LQ-52171
@when('the user clicks "Engine Hours"')
def click_fleet_utilization_engine_hours_tab():
    FLEET_INSIGHTS_PAGE.click_insights()
    FLEET_UTILIZATION_REPORT_PAGE.click_fleet_utilization()
    FLEET_UTILIZATION_REPORT_PAGE.click_reset_button()
    FLEET_UTILIZATION_REPORT_PAGE.click_engine_hours_tab()


@then('the Engine Hours tab of Fleet Utilization is displayed')
def fleet_utilization_engine_hours_displayed():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_average_engine_hours_trend_title() == "Average Engine Hours (hrs)"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_engine_hours_by_group_title() == "Engine Hours by Group"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_engine_hours_by_vehicle_title() == "Engine Hours by Vehicle"


# LQ-47543
@when('the user sets date in the date filter in engine hours page')
def set_date_filter_in_engine_hours_tab():
    FLEET_UTILIZATION_REPORT_PAGE.select_date_filter_group()
    FLEET_UTILIZATION_REPORT_PAGE.set_fleet_utilization_engine_hours_date_range(
        FUR.fleet_utilization_engine_hours_date_range_start_month,
        FUR.fleet_utilization_engine_hours_date_range_start_day,
        FUR.fleet_utilization_engine_hours_date_range_start_year,
        FUR.fleet_utilization_engine_hours_date_range_end_month,
        FUR.fleet_utilization_engine_hours_date_range_end_day,
        FUR.fleet_utilization_engine_hours_date_range_end_year)
    sleep(2)
    FLEET_UTILIZATION_REPORT_PAGE.click_apply()


@then(
    'the data with selected filters are displayed on the "Average Engine Hours" trend, "Engine Hours by Group", "Engine Hours by Vehicle"')
def fleet_utilization_filter_engine_hours_tab():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_row_count_for_engine_hours_by_group() <= 10
    assert FLEET_UTILIZATION_REPORT_PAGE.get_row_count_for_engine_hours_by_vehicle() <= 10
    assert FLEET_UTILIZATION_REPORT_PAGE.get_engine_hours_trend() == True


# LQ-47541
@when('the user sets group filter to one group in engine hours tab')
def set_group_in_engine_hours_tab_group_filter():
    FLEET_UTILIZATION_REPORT_PAGE.click_filter_group()
    FLEET_UTILIZATION_REPORT_PAGE.search_filter_group(FUR.group1)
    FLEET_UTILIZATION_REPORT_PAGE.select_search_filter()
    FLEET_UTILIZATION_REPORT_PAGE.click_done()


@then(
    'the data with selected filters are displayed on the "Average Engine Hours" trend, "Engine Hours by Group", "Engine Hours by Vehicle"')
def engine_hours_data_with_selected_filter_displayed():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_row_count_for_engine_hours_by_group() <= 10
    assert FLEET_UTILIZATION_REPORT_PAGE.get_row_count_for_engine_hours_by_vehicle() <= 10

# LQ-47544
@when('the user clicks "Engine Hours" tab in Fleet Utilization')
def engine_hours_by_group_widget_is_displayed():
    # when part of LQ-47544 is covered in LQ-47541 testcase
    print("no action needed here")

@then('Engine Hours by Group table  is displayed with columns "GROUP", "TOTAL VEHICLE", "TOTAL", "AVG/DAY"')
def assert_engine_hours_by_group_widget():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_group_column_name_title_of_group_widget() == "GROUP"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_total_vehicle_column_name_title_of_group_widget() == "TOTAL VEHICLES"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_total_column_name_title_of_group_widget() == "TOTAL"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_avg_day_column_name_title_of_group_widget() == "AVG/DAY"

# LQ-47545
@when('the user clicks "Engine Hours" tab in Insights-Fleet Utilization')
def engine_hours_by_vehicle_widget_is_displayed():
    # when part of LQ-47545 is covered in LQ-57541 testcase
    print("no action needed here")

@then('Engine Hours by Vehicle table is displayed with columns "VEHICLE", "GROUP", "TOTAL", "AVG/DAY"')
def assert_engine_hours_by_vehicle_widget():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_vehicle_column_name_title_of_vehicle_widget() == "VEHICLE"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_group_column_name_title_of_vehicle_widget() == "GROUP"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_total_column_name_title_of_vehicle_widget() == "TOTAL"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_avg_day_column_name_title_of_vehicle_widget() == "AVG/DAY"


# LQ-52170
@when('the user clicks "view details" in Engine Hours by Group widget')
def click_engine_hours_by_group_hyper_link():
    FLEET_UTILIZATION_REPORT_PAGE.click_view_details_of_group_widget()


@then('the "fleet operation group tab" of Engine Hours is displayed')
def fleet_operation_group_tab_displayed():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_operations_title() == "FLEET OPERATIONS"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_operations_groups_tab() == "Groups"


# LQ-75141
@when('the user clicks "group name" from group column in Engine Hours by Group widget')
def click_engine_hours_by_group_group_name_link():
    FLEET_INSIGHTS_PAGE.click_insights()
    FLEET_UTILIZATION_REPORT_PAGE.click_fleet_utilization()
    FLEET_UTILIZATION_REPORT_PAGE.click_engine_hours_tab()
    FLEET_UTILIZATION_REPORT_PAGE.click_group_name_in_group_widget()


@then('the fleet operation group page of Engine Hours is displayed with same group filter')
def fleet_operation_page_displayed():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_operations_title() == "FLEET OPERATIONS"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_operations_groups_tab() == "Groups"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_engine_group_filter_text() == "SF500 Alpha Trial"


# LQ-47547
@when('the user clicks "view details" in Engine Hours by Vehicle widget')
def click_engine_hours_by_vehicle_view_details_hyper_link():
    FLEET_INSIGHTS_PAGE.click_insights()
    FLEET_UTILIZATION_REPORT_PAGE.click_fleet_utilization()
    FLEET_UTILIZATION_REPORT_PAGE.click_engine_hours_tab()
    FLEET_UTILIZATION_REPORT_PAGE.click_view_details_of_vehicle_widget()


@then('the "fleet operation vehicle tab" Engine Hours is displayed')
def fleet_operation_vehicle_tab_displayed():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_operations_title() == "FLEET OPERATIONS"
    assert FLEET_UTILIZATION_REPORT_PAGE.get_fleet_operations_vehicle_tab() == "Vehicles"


@when('the user clicks "vehicle name" in Engine Hours by Vehicle widget')
def click_engine_hours_by_vehicle_vehicle_name_link():
    FLEET_INSIGHTS_PAGE.click_insights()
    FLEET_UTILIZATION_REPORT_PAGE.click_fleet_utilization()
    FLEET_UTILIZATION_REPORT_PAGE.click_engine_hours_tab()
    FLEET_UTILIZATION_REPORT_PAGE.click_vehicle_name_in_vehicle_widget()


@then('the "vehicle profile" page of Engine Hours is displayed')
def vehicle_profile_page_displayed():
    assert FLEET_UTILIZATION_REPORT_PAGE.get_vehicle_profile_text_title() == "VEHICLE PROFILE"
