from hamcrest import assert_that, contains_string
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then, parsers
from data.prod.fleet_telematics_prod import FleetTelematicsDataProd as FTD_PROD
from data.stg.fleet_telematics_stg import FleetTelematicsDataStg as FTD_STG
from data.int.fleet_telematics_int import FleetTelematicsDataInt as FTD_INT
from pages.dashboard_page import DashboardPage
from pages.fleet_telematics_left_panel_page import FleetTelematicsPageLeftPanel
from pages.fleet_telematics_center_page import FleetTelematicsCenterPage
from pages.login_page import LoginPage
from steps.common import ENV, NEW_UI_FTM_URL

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
BASE_PAGE = 0
FLEET_TELEMATICS_PAGE = 0
FLEET_TELEMATICS_CENTER_PAGE = 0
FTD = 0

scenarios('../features/sanity_fleet_telematics_center_page.feature')


# LQ-306
@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, FTD, FLEET_TELEMATICS_PAGE, FLEET_TELEMATICS_CENTER_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    FLEET_TELEMATICS_PAGE = FleetTelematicsPageLeftPanel(browser)
    FLEET_TELEMATICS_CENTER_PAGE = FleetTelematicsCenterPage(browser)

    browser.get(NEW_UI_FTM_URL)

    if ENV == 'stg':
        FTD = FTD_STG
    elif ENV == 'int':
        FTD = FTD_INT
    elif ENV == 'prod':
        FTD = FTD_PROD
    else:
        raise ValueError(f"Unsupported ENV value: '{ENV}'. Valid options are 'stg', 'int', or 'prod'.")


@when('the user enters username/password, clicks the login button in the page and select company from the list')
def login():
    LOGIN_PAGE.enter_username(FTD.username)
    LOGIN_PAGE.enter_password(FTD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_multi_company(FTD.company_name)
    LOGIN_PAGE.click_select_company_button()
    LOGIN_PAGE.wait_for_page_load()


@then('the user is successfully logged into the Driver Safety dashboard')
def verify_login():
    assert DASHBOARD_PAGE.lytx_logo_is_displayed() is True
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert DASHBOARD_PAGE.no_of_unassigned_drivers_is_displayed() is True
    assert DASHBOARD_PAGE.get_unassigned_drivers_text() == "UNASSIGNED DRIVERS"
    assert_that(DASHBOARD_PAGE.get_unassigned_drivers_text(), contains_string("UNASSIGNED DRIVER"))
    assert DASHBOARD_PAGE.get_due_for_coaching_text() == "DUE FOR COACHING"
    assert DASHBOARD_PAGE.get_fyi_notify_text() == "FYI NOTIFY"
    assert_that(DASHBOARD_PAGE.get_collisions_text(), contains_string("COLLISION"))
    assert_that(DASHBOARD_PAGE.get_possible_collisions_text(), contains_string("POSSIBLE COLLISION"))


# LQ-108840
@when('the user clicks Fleet Telematics tab')
def navigate_to_fleet_telematics():
    DASHBOARD_PAGE.click_fleet_telematics_tab()


@then('the Fleet Telematics main page is loaded successfully')
def verify_user_on_fleet_telematics():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_PAGE.more_charts_button_is_displayed() is True


# LQ-117225
@when('the user clicks on MAP menu in the left navigation bar')
def click_map_menu():
    FLEET_TELEMATICS_PAGE.scroll_page_up()
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_map_menu()
    FLEET_TELEMATICS_CENTER_PAGE.switch_ft_iframe()


@then(
    'the user should be navigated to the Map page with the headers such as Search asset,VIN or serial number, Status, Saved Views, Map Options and Add Zone and the icons such as Zoom in, Zoom out present inside the map')
def verify_map_page_headers_icons():
    assert FLEET_TELEMATICS_CENTER_PAGE.search_asset_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.status_dropdown_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.nearest_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.find_asset_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.status_change_sort_direction_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.update_list_with_map_checkbox_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.mc_refresh_icon_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.mc_zoom_in_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.mc_zoom_out_is_displayed() is True


# LQ-118189
@when('the user clicks Productivity menu - Trips History submenu')
def navigate_to_tripHistory():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_productivity_menu()
    FLEET_TELEMATICS_PAGE.click_triphistory_submenu()


@then(
    'the user should be navigated to the Trips History Page and the user should be able to see the Headers such as Search, Options, Summary, Live Positions, Report, Map Options present in the Trips History page')
def verify_tripHistory_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.trip_history_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.search_bar_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.select_different_options_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.live_positions_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.reports_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.show_all_trips_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.date_is_displayed() is True


@when('the user clicks Productivity menu - Routes submenu- Routes subchild')
def navigate_to_routes():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_routes_submenu_dropdown()
    FLEET_TELEMATICS_PAGE.click_routes_subchild()


@then(
    'the user should be navigated to the "Routes" page and options such as "Search name","Add route","Filter" and "Columns"')
def verify_routes_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.routes_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.routes_search_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.routes_addnewroute_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.routes_filters_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.routes_columns_is_displayed() is True


@when('the user clicks the dropdown icon present near the "Columns"')
def click_routes_columns_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.click_routes_columns()


@then(
    'the user should be able to see the Options such as "Reset to default","Name","Assigned Asset","Scheduled Start Time" and "Status" available')
def verify_routes_columns_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.routes_reset_to_default_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.routes_name_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.routes_assigned_asset_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.routes_scheduled_start_time_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.routes_status_is_displayed() is True


# LQ-118200
@when('the user clicks Productivity menu - Routes submenu- Planned vs actual routes subchild')
def navigate_to_plannedVsActualRoutes():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_plannedvsactualroutes_subchild()


@then(
    'the user should be navigated to the "Planned vs actual route report" page and the user should be able to see the headers such as search assets, options and report present in the page')
def verify_plannedVsActualRoutes_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.plannedvsactual_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.pa_search_assets_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.pa_options_dropdown_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.pa_report_dropdown_is_displayed() is True


# LQ-118210
@when('the user clicks Productivity menu - Routes submenu- Route Summary subchild')
def navigate_to_routeSummary():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_routesummary_subchild()


@then(
    'the user should be navigated to the "Route Summary Report" page and the user should be able to see the headers such as options, stop processing and report present in the page')
def verify_routeSummary_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.route_summary_report_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.rs_stop_processing_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.rs_reports_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.asset_xpath_is_displayed() is True


# LQ-97664
@when('the user clicks Productivity menu - Routes submenu- Unmatched Route subchild')
def navigate_to_unmatchedRoutes():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_unmatchedroute_subchild_dropdown()


@then(
    'the user should be navigated to the "Unmatched Route Report" page and the user should be able to see the headers such as options and report present in the page')
def verify_unmatchedRoutes_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.unmatched_route_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.ur_reports_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.asset_xpath_is_displayed() is True


# LQ-118220
@when('the user clicks Productivity menu - Routes submenu- Import Routes subchild')
def navigate_to_importRoutes():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_importroutes_subchild()


@then(
    'the user should be navigated to the "Import Routes Report" page and the user should be able to see the headers such as import routes title, drop area, and sample table present in the page')
def verify_importRoutes_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.import_routes_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.drop_file_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.import_file_table_is_displayed() is True


# LQ-118722
@when('the user clicks Productivity menu - Zones - Zones subchild')
def navigate_to_zones():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_zones_submenu()
    FLEET_TELEMATICS_PAGE.click_zones_subchild()


@then(
    'the user should be navigated to the "Zones" page and the user should be able to see the headers such as search name, filter, add, sort by, types, report, select none, columns present in the page')
def verify_zones_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.zones_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zones_search_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.filters_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zones_addnewzone_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.reports_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zones_types_is_displayed() is True


# LQ-118724
@when('the user clicks Productivity menu - Zones - Zone Visits subchild')
def navigate_to_zoneVisits():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_zonevisits_subchild()


@then(
    'the user should be navigated to the "Zone Visits" page and the user should be able to see the headers such as search assets, options, sort by, report, columns present in the page')
def verify_zoneVisits_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.zonevisits_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zv_search_assets_dropdown_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zv_sort_dropdown_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zv_summary_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zv_options_dropdown_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.reports_button_is_displayed() is True


# LQ-118733
@when('the user clicks Productivity menu - Zones - Zone Types subchild')
def navigate_to_zoneTypes():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_zonetypes_subchild()


@then(
    'the user should be navigated to the "Zone Types" page and the user should be able to see the headers such as search name or comment, add zone type present in the page')
def verify_zoneTypes_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.zone_types_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zt_add_zone_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zt_search_name_comment_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zone_types_customer_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zone_types_home_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zone_types_inhouse_service_center_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zone_types_office_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zone_types_vendor_service_center_is_displayed() is True


# LQ-118734
@when('the user clicks Productivity menu - Zones - Import Zones subchild')
def navigate_to_importZones():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_importzones_subchild()


@then(
    'the user should be navigated to the "Import Zones" page and the user should be able to see the headers such as options, drop files area, sample table present in the page')
def verify_importZones_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.importzones_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.importzones_options_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.importzones_upload_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.importzones_table_is_displayed() is True


# LQ-118743
@when('the user clicks Productivity menu - Driver Congregation submenu')
def navigate_to_driverCongregation():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_zones_submenu()
    FLEET_TELEMATICS_PAGE.click_drivercongregation_submenu()


@then('the user should be navigated to the "Driver Congregation" page')
def verify_driverCongregation_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.drivercongregation_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.reports_button_is_displayed() is True


# LQ-118745
@when('the user clicks Productivity menu - Asset Location Sharing submenu')
def navigate_to_assetLocationSharing():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_assetlocationsharing_submenu()


@then('the user should be navigated to the "Asset Location Sharing" page')
def verify_assetLocationSharing_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.assetlocationsharing_header_is_displayed() is True
    # assert FLEET_TELEMATICS_CENTER_PAGE.zones_filter_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zt_search_name_comment_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.assetlocationsharing_sort_by_asset_is_displayed() is True


# LQ-118200
@when('the user clicks Productivity menu - Risk Management submenu')
def navigate_to_riskmanagement():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_riskmanagement_submenu()


@then('the user should be navigated to the "Risk Management" page')
def verify_riskmanagement_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.riskmanagement_header_is_displayed() is True


# LQ-119240
@when('the user clicks Compliance menu - HOS submenu - Logs subchild')
def navigate_to_hoslogs():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_compliance_menu()
    FLEET_TELEMATICS_PAGE.click_hos_submenu_dropdown()
    FLEET_TELEMATICS_PAGE.click_hoslogs_subchild()


@then('the user should be navigated to the "HOS Logs" page')
def verify_hoslogs_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.hoslogs_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.filters_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.status_change_sort_direction_is_displayed() is True


# LQ-119241
@when('the user clicks Compliance menu - HOS submenu - Unidentified Driving subchild')
def navigate_to_unidentifiedDriving():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_unidentified_driving_subchild()


@then('the user should be navigated to the "Unidentified Driving" page')
def verify_unidentifiedDriving_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.unidentifieddriving_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.filters_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.status_change_sort_direction_is_displayed() is True


# LQ-119242
@when('the user clicks Compliance menu - HOS submenu - Violations subchild')
def navigate_to_violations():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_violations_subchild()


@then('the user should be navigated to the "Violations" page')
def verify_violations_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.hosviolations_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.pa_search_assets_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.status_change_sort_direction_is_displayed() is True


# LQ-119243
@when('the user clicks Compliance menu - HOS submenu - Availability subchild')
def navigate_to_availability():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_availability_subchild()


@then('the user should be navigated to the "Availability" page')
def verify_availability_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.hosavailability_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.pa_search_assets_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.status_change_sort_direction_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.reports_button_is_displayed() is True


# @LQ-119271
@when('the user clicks Compliance menu - Time Card Report submenu')
def navigate_to_timeCardReport():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_hos_submenu()
    FLEET_TELEMATICS_PAGE.click_timecardreport_submenu()


@then('the user should be navigated to the "Time Card Report" page')
def verify_timeCardReport_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.timecardreport_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.status_change_sort_direction_is_displayed() is True


# LQ-119273
@when('the user clicks Compliance menu - IFTA Report submenu')
def navigate_to_IFTAReport():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_iftareport_submenu()


@then('the user should be navigated to the "IFTA Report" page')
def verify_IFTAReport_headers():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.iftareport_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.reports_button_is_displayed() is True


# LQ-119282
@when('the user clicks Compliance menu - Clean Truck Check submenu')
def navigate_to_cleanTruckCheck():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_cleantruckcheck_submenu()


@then('the user should be navigated to the "Clean Truck Check" page')
def verify_cleanTruckCheck_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.cleantruckcheckprogram_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.enrollAssets_is_displayed() is True


# LQ-146480
@given('the user clicks Maintenance menu')
def click_maintenance_tab():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_maintenance_menu()


@when('the user clicks the "Work Order" submenu')
def navigate_to_work_order():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_work_order_sub_menu()


@then('the user should be navigated to the "Work Order Management" page with sub-tabs "Requests","Orders" and "Jobs"')
def verify_work_order_management():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    FLEET_TELEMATICS_CENTER_PAGE.wait_for_page_to_fully_load()
    assert FLEET_TELEMATICS_CENTER_PAGE.get_work_order_management_page_title() == "Work Order Management"
    assert FLEET_TELEMATICS_CENTER_PAGE.requests_tab_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.orders_tab_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.jobs_tab_is_displayed() is True


# LQ-146663
@then('the user is in "Request" tab by default with "Schedules","Reports" and "Work Request" in the header')
def verify_request_tab_is_opened():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.schedules_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.work_request_is_displayed() is True


@then('the user should see the options "Groups","Assets" and "Filters" under the tab')
def verify_filters():
    assert FLEET_TELEMATICS_CENTER_PAGE.groups_filter_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.assets_filter_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.filters_option_is_displayed() is True


@then(
    'the user should see columns "Asset","Source","Maintenance Type","Categories","Severity","Triggered date","Status" and "Description" present by default in the tabular form')
def verify_columns_for_requests_tab():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_asset_column_name() == "Asset"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_source_column_name() == "Source"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_maintenance_type_column_name() == "Maintenance type"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_categories_column_name() == "Categories"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_severity_column_name() == "Severity"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_triggered_date_column_name() == "Triggered date"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_status_column_name() == "Status"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_description_column_name() == "Description"


# LQ-146688
@when('the user clicks the Setting icon present above the tabular column')
def click_setting_icon():
    FLEET_TELEMATICS_CENTER_PAGE.click_setting_icon()


@then('all the setting names should be present for requests tab')
def verify_setting_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_asset_setting_name() == "Asset"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_source_setting_name() == "Source"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_maintenance_type_setting_name() == "Maintenance type"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_categories_setting_name() == "Categories"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_severity_setting_name() == "Severity"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_triggered_date_setting_name() == "Triggered date"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_status_setting_name() == "Status"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_description_setting_name() == "Description"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_is_overdue_setting_name() == "Is overdue"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_service_due_on_odometer_setting_name() == "Service due on odometer"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_service_due_on_engine_hours_setting_name() == "Service due on engine hours"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_current_engine_hours_setting_name() == "Current engine hours"


@when('the user clicks the "Filters" options')
def user_clicks_filters_options():
    FLEET_TELEMATICS_CENTER_PAGE.click_filters_button()


@then('the user should see an pop-up having a header named " All Filters" and all the filter options')
def verify_filter_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_filters_pop_up_title() == "All Filters"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_groups_filter_option_in_pop_up() == "Groups"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_assets_filter_option_in_pop_up() == "Assets"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_maintenance_types_filter_option_in_pop_up() == "Maintenance types"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_sources_filter_option_in_pop_up() == "Sources"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_severity_filter_option_in_pop_up() == "Severity"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_show_snoozed_requests_filter_option_in_pop_up() == "Show snoozed requests"


@when('the user clicks on the "Groups" dropdown and selects a group option')
def user_clicks_group_drop_down_in_pop_up():
    FLEET_TELEMATICS_CENTER_PAGE.click_group_filter_in_filter_pop_up()
    FLEET_TELEMATICS_CENTER_PAGE.select_asset_information_check_box()
    FLEET_TELEMATICS_CENTER_PAGE.click_apply_button()


@then('the selected group should be applied to the filter')
def verify_group_filter_in_filters_pop_up():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_selected_group_filter_in_filters_pop_up() == "Asset Information"


@when('the user clicks on the "Assets" dropdown and selects an asset option')
def click_assets_drop_down():
    FLEET_TELEMATICS_CENTER_PAGE.click_assets_filter_in_filter_pop_up()
    FLEET_TELEMATICS_CENTER_PAGE.select_asset_check_box()
    FLEET_TELEMATICS_CENTER_PAGE.close_asset_drop_down()


@then('the selected asset should be applied to the filter')
def verify_assets_filter():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_selected_asset_filter_in_filters_pop_up() is True


@when('the user clicks on the "Maintenance types" dropdown and selects a maintenance type')
def click_on_maintenance_filter():
    FLEET_TELEMATICS_CENTER_PAGE.click_maintenance_filter_in_filter_pop_up()
    FLEET_TELEMATICS_CENTER_PAGE.select_maintenance_check_box()
    FLEET_TELEMATICS_CENTER_PAGE.close_maintenance_drop_down()


@then('the selected maintenance type should be applied to the filter')
def verify_maintenance_filter():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_selected_maintenance_filter_in_filters_pop_up() != "Maintenance types"


@when('the user clicks on the "Sources" dropdown')
def click_sources_filter():
    FLEET_TELEMATICS_CENTER_PAGE.click_sources_filter_in_filter_pop_up()


@then(
    'the user should see the types "Manual","Data Insight","Scheduled","Driver reported","Faults" with "Select All" option')
def verify_sources_drop_down_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_select_all_text() == "Select all"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_manual_checkbox() == "Manual"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_data_insight_checkbox() == "Data insight"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_scheduled_checkbox() == "Scheduled"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_driver_reported_checkbox() == "Driver reported"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_faults_checkbox() == "Faults"


@when('the user selects any source type')
def select_source_type():
    FLEET_TELEMATICS_CENTER_PAGE.click_manual_checkbox()
    FLEET_TELEMATICS_CENTER_PAGE.close_sources_drop_down()


@then('the selected source type should be applied to the filter')
def verify_source_type_applied():
    assert FLEET_TELEMATICS_CENTER_PAGE.is_manual_filter_applied() is True


@when('the user clicks on the "Severity" dropdown')
def click_severity_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.click_severity_dropdown()


@then('the user should see the types "Unknown","Low","Medium","High","Critical" with "Select All" option')
def verify_severity_dropdown_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_select_all_severity() == "Select all"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_unknown_severity() == "Unknown"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_low_severity() == "Low"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_medium_severity() == "Medium"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_high_severity() == "High"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_critical_severity() == "Critical"


@when('the user selects a severity')
def select_severity():
    FLEET_TELEMATICS_CENTER_PAGE.click_high_severity()  # example: selecting "High"


@then('the user selected severity type should be applied to the filter')
def verify_selected_severity_applied():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_applied_severity_filter() == "High"


@when('the user clicks the "Orders" sub-tab')
def click_orders_tab():
    if FLEET_TELEMATICS_CENTER_PAGE.close_button_is_displayed() is True:
        FLEET_TELEMATICS_CENTER_PAGE.click_close_button()
    FLEET_TELEMATICS_CENTER_PAGE.click_orders_tab()


@then('the "Orders" tab should be displayed with buttons "Reports", "Bulk upload" and "Work Order" in the header')
def verify_headers_in_orders_tab():
    assert FLEET_TELEMATICS_CENTER_PAGE.work_order_is_displayed() is True


@then('the user should see the options "Groups","Assets","Status" and "Filters" under the tab')
def verify_filter_options_in_orders():
    assert FLEET_TELEMATICS_CENTER_PAGE.groups_filter_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.assets_filter_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.status_filter_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.filters_option_is_displayed() is True


@when('the user clicks the dropdown present near "Status" field')
def click_drop_down_for_status_filter():
    FLEET_TELEMATICS_CENTER_PAGE.click_status_filter()


@then(
    'the user should be able to see the types "Open","Assigned","In progress","On hold","Completed" and "Cancelled" available and buttons "Clear","Cancel" and "Apply"')
def verify_drop_down_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_open_dropdown_value() == "Open"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_assigned_dropdown_value() == "Assigned"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_in_progress_dropdown_value() == "In progress"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_on_hold_dropdown_value() == "On hold"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_completed_dropdown_value() == "Completed"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_canceled_dropdown_value() == "Canceled"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_clear_dropdown_value() == "Clear"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_cancel_dropdown_value() == "Cancel"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_apply_dropdown_value() == "Apply"


@then('the user should see the columns Asset, Order reference, Date created, Date completed, Priority, status')
def verify_table_columns():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_asset_column_name() == "Asset"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_order_reference_column_name() == "Order reference"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_created_column_name() == "Date created"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_completed_column_name() == "Date completed"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_priority_column_name() == "Priority"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_status_column_name() == "Status"


@then('all the setting names should be present for orders tab')
def verify_setting_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_asset_setting_name_in_order_page() == "Asset"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_order_reference_setting_name() == "Order reference"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_created_setting_name() == "Date created"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_completed_setting_name() == "Date completed"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_priority_setting_name() == "Priority"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_status_setting_name_order_page() == "Status"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_engine_hours_reading_setting_name() == "Engine hours reading"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_odometer_reading_setting_name() == "Odometer reading"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_assigned_to_setting_name() == "Assigned to"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_due_on_date_setting_name() == "Due on date"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_labor_costs_setting_name() == "Labor costs"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_notes_setting_name() == "Notes"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_opened_by_setting_name() == "Opened by"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_parts_cost_setting_name() == "Parts cost"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_reason_for_repair_setting_name() == "Reason for repair"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_repair_class_setting_name() == "Repair class"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_shipping_cost_setting_name() == "Shipping cost"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_tax_cost_setting_name() == "Tax cost"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_total_cost_setting_name() == "Total cost"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_last_updated_setting_name() == "Last updated"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_repair_site_setting_name() == "Repair site"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_job_count_setting_name() == "Job count"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_reset_setting_name() == "Reset"


@when('the user clicks the "Filters" option in Orders tab')
def click_filters_in_orders_tab():
    FLEET_TELEMATICS_CENTER_PAGE.click_filters_button()


@then('user should see all filter options')
def verify_orders_filters():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_filters_pop_up_title() == "All Filters"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_groups_filter_option_in_pop_up() == "Groups"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_assets_filter_option_in_pop_up() == "Assets"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_status_filter_option_in_pop_up() == "Status"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_created_filter_option_in_pop_up() == "Date created"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_references_filter_option_in_pop_up() == "References"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_priority_filter_option_in_pop_up() == "Priority"


@when('the user clicks on the "Groups" dropdown and selects a group option - orders tab')
def user_selects_one_group():
    FLEET_TELEMATICS_CENTER_PAGE.click_group_filter_in_filter_pop_up()
    FLEET_TELEMATICS_CENTER_PAGE.select_asset_information_check_box()
    FLEET_TELEMATICS_CENTER_PAGE.click_apply_button()


@then('the selected group should be applied to the filter in orders tab')
def verify_group_filter():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_selected_group_filter_in_filters_pop_up() == "Asset Information"


@when('the user clicks on the "Assets" dropdown and selects an asset option - orders tab')
def click_assets_drop_down_orders_tab():
    FLEET_TELEMATICS_CENTER_PAGE.click_assets_filter_in_filter_pop_up()
    FLEET_TELEMATICS_CENTER_PAGE.select_asset_check_box()
    FLEET_TELEMATICS_CENTER_PAGE.close_asset_drop_down()


@then('the selected asset should be applied to the filter in orders tab')
def verify_assets_filter():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_selected_asset_filter_in_filters_pop_up() is True


@when('the user clicks on the "Status" dropdown')
def click_status_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.click_status_dropdown()


@then(
    'the user should see the types "Open","Assigned","In progress","On hold","Completed" and "Cancelled" available with a "Clear" button disabled')
def verify_status_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_open_dropdown_value() == "Open"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_assigned_dropdown_value() == "Assigned"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_in_progress_dropdown_value() == "In progress"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_on_hold_dropdown_value() == "On hold"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_completed_dropdown_value() == "Completed"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_canceled_dropdown_value() == "Canceled"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_clear_dropdown_value() == "Clear"
    assert FLEET_TELEMATICS_CENTER_PAGE.clear_button_is_present_and_disabled() is True


@when('the user selects any status')
def select_any_status():
    FLEET_TELEMATICS_CENTER_PAGE.click_open_status()
    FLEET_TELEMATICS_CENTER_PAGE.close_status_drop_down()


@then('the selected status should be applied to the filter')
def verify_status_filter():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_applied_status_text() == "Open"


@when('the user clicks the "Select Date" button')
def click_select_date_button():
    FLEET_TELEMATICS_CENTER_PAGE.click_select_date_button()


@then(
    'the user should see the header "Date created" with options like "Today","Yesterday","This week","Last week","This month","Last month","Last 3 months" and "Custom"')
def verify_select_date_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_created_header() == "Date created"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_today_text() == "Today"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_yesterday_text() == "Yesterday"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_this_week_text() == "This week"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_last_week_text() == "Last week"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_this_month_text() == "This month"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_last_month_text() == "Last month"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_last_3_months_text() == "Last 3 months"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_custom_text() == "Custom"


@when('selects any date option')
def select_any_date_option():
    FLEET_TELEMATICS_CENTER_PAGE.click_today_option()  # picking "Today" as the selected option


@then('the selected date should be applied to the filter')
def verify_selected_date_applied():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_applied_date_filter_text() == "Today"


@then('the user should see "Low","Medium", "High" and "Critical" options')
def verify_priority_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.is_priority_low_visible()
    assert FLEET_TELEMATICS_CENTER_PAGE.is_priority_medium_visible()
    assert FLEET_TELEMATICS_CENTER_PAGE.is_priority_high_visible()
    assert FLEET_TELEMATICS_CENTER_PAGE.is_priority_critical_visible()


@when('the user clicks any of the priority')
def click_priority():
    FLEET_TELEMATICS_CENTER_PAGE.click_priority_low()


@then('the user should see the selected priority checked')
def verify_priority_checked():
    assert FLEET_TELEMATICS_CENTER_PAGE.is_priority_low_checked()


@when('the user clicks the "Jobs" sub-tab')
def user_click_jobs_sub_tab():
    FLEET_TELEMATICS_CENTER_PAGE.click_jobs_sub_tab()


@then('the user should see the options "Groups","Assets","This month","Status" and "Filters" under the tab')
def verify_filters_in_jobs_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.groups_filter_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.assets_filter_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.date_filter_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.status_filter_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.filters_option_is_displayed() is True


@then(
    'the user should see the columns "Asset","Order reference","Source","Maintenance type","Categories","Status","Date started","Date completed" and "Date created"')
def verify_table_columns_in_jobs_tab():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_asset_column_name() == "Asset"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_order_reference_column_name() == "Order reference"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_source_column_name() == "Source"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_maintenance_type_column_name() == "Maintenance type"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_categories_column_name() == "Categories"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_status_column_name() == "Status"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_started_column_name() == "Date started"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_completed_column_name() == "Date completed"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_created_column_name() == "Date created"


@then(
    'the user should be able to see the types "Open","Assigned","In progress","On hold","Completed" and "Cancelled" available with "Select all" option and "Clear" displayed')
def verify_status_filter_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_select_all_dropdown_value() == "Select all"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_open_dropdown_value() == "Open"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_assigned_dropdown_value() == "Assigned"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_in_progress_dropdown_value() == "In progress"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_on_hold_dropdown_value() == "On hold"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_completed_dropdown_value() == "Completed"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_canceled_dropdown_value() == "Canceled"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_clear_dropdown_value() == "Clear"


@when('the user clicks the "This month" option')
def user_click_calender_option():
    FLEET_TELEMATICS_CENTER_PAGE.click_calender_filter()


@then(
    'the user should see the "Dates" with a header "Date completed" and other options "Today","Yesterday","This week","Last week","This month","Last month","Last 3 months" and "Custom" available')
def verify_options_for_date_filter():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_completed_text() == "Date completed"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_today_text() == "Today"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_yesterday_text() == "Yesterday"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_this_week_text() == "This week"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_last_week_text() == "Last week"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_this_month_text() == "This month"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_last_month_text() == "Last month"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_last_3_months_text() == "Last 3 months"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_custom_text() == "Custom"


@then('the user should see the "Clear" button disabled')
def verify_clear_button_in_date_filter():
    assert FLEET_TELEMATICS_CENTER_PAGE.clear_button_is_present_and_disabled() is True


@then('the user should see all the options with reset button')
def verify_setting_options_in_jobs_tab():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_asset_setting_name_in_jobs_page() == "Asset"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_order_reference_setting_name_in_jobs_page() == "Order reference"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_source_setting_name_in_jobs_page() == "Source"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_maintenance_type_setting_name_in_jobs_page() == "Maintenance type"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_categories_setting_name_in_jobs_page() == "Categories"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_status_setting_name_in_jobs_page() == "Status"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_started_setting_name() == "Date started"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_completed_setting_name_in_jobs_page() == "Date completed"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_created_setting_name_in_jobs_page() == "Date created"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_triggered_date_setting_in_jobs_page_name() == "Triggered date"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_engine_hours_reading_setting_name_in_jobs_page() == "Engine hours reading"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_odometer_reading_setting_name_in_jobs_page() == "Odometer reading"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_hours_setting_name() == "Hours"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_labor_costs_setting_name_in_jobs_page() == "Labor costs"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_parts_cost_setting_name_in_jobs_page() == "Parts cost"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_shipping_cost_setting_name_in_jobs_page() == "Shipping costs"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_tax_cost_setting_name_in_jobs_page() == "Taxes"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_total_cost_setting_name_in_jobs_page() == "Total cost"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_priority_setting_name_in_jobs_page() == "Priority"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_reset_setting_name_in_jobs_page() == "Reset"


@when('the user clicks the "Schedules" submenu')
def click_schedules_child_menu():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_schedules_child_menu()


@then(
    'the "Maintenance Schedules" page is displayed with Headers such as "Reports","Work requests" "Bulk upload" and "Schedule"')
def verify_headers_in_schedules_page():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.work_request_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.schedule_button_is_displayed() is True


@then(
    'the user should be able to see the filter options such as "Groups", "Search", "Frequency","Repeats" and a settings icon')
def verify_filter_options_in_schedules_tab():
    assert FLEET_TELEMATICS_CENTER_PAGE.groups_filter_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.search_filter_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.frequency_filter_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.repeats_filter_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.setting_icon_is_displayed() is True


@then(
    'the user should be able to see the list of schedules such as "Name","Categories","Repeats","Frequency" and "Assets added" present in the page')
def verify_table_columns_in_schedules_tab():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_name_column_text() == "Name"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_categories_column_text() == "Categories"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_repeats_column_text() == "Repeats"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_frequency_column_text() == "Frequency"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_assets_added_column_text() == "Assets added"


@when('the user clicks the dropdown icon present near the "Frequency" textbox')
def click_drop_down_for_frequency_filter():
    FLEET_TELEMATICS_CENTER_PAGE.click_frequency_drop_down()


@then(
    'the user should be able to see the frequencies such as "Frequency based on distance", "Frequency based on months", "Frequency based on weeks", "Frequency based on days" and "Frequency based on engine hours"')
def verify_freq_filter_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_frequency_based_on_distance_text() == "Frequency based on distance"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_frequency_based_on_months_text() == "Frequency based on months"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_frequency_based_on_weeks_text() == "Frequency based on weeks"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_frequency_based_on_days_text() == "Frequency based on days"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_frequency_based_on_engine_hours_text() == "Frequency based on engine hours"


@then(
    'the user should be able to see the "Clear" and "Apply" buttons which is disabled and "Cancel" button which is enabled')
def verify_clear_option_freq_filter():
    assert FLEET_TELEMATICS_CENTER_PAGE.clear_button_is_present_and_disabled() is True


@when('the user clicks the dropdown icon present near the "Repeats" textbox')
def click_repeats_filter():
    FLEET_TELEMATICS_CENTER_PAGE.click_repeats_filter()


@then('the user should be able to see "Yes" and "No" options available')
def verify_repeats_filter_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_yes_option_text() == "Yes"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_no_option_text() == "No"


@then('the user should be able to see the "Clear" button disabled')
def verify_clear_button_in_repeats_filter():
    assert FLEET_TELEMATICS_CENTER_PAGE.clear_button_is_present_and_disabled() is True


@then(
    'the user should be able to see the options "Name","Categories","Repeats","Frequency","Asset added","Days","Weeks","Months","Day of week","Day of month","Engine hours","Distance","Event date" and "Source" available with scroll bar under the settings icon and Reset button is available')
def verify_setting_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_name_setting_text() == "Name"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_categories_setting_text() == "Categories"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_repeats_setting_text() == "Repeats"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_frequency_setting_text() == "Frequency"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_assets_added_setting_text() == "Assets added"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_days_setting_text() == "Days"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_weeks_setting_text() == "Weeks"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_months_setting_text() == "Months"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_day_of_week_setting_text() == "Day of week"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_day_of_month_setting_text() == "Day of month"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_engine_hours_setting_text() == "Engine hours"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_distance_setting_text() == "Distance"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_event_date_setting_text() == "Event date"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_source_setting_text() == "Source"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_reset_setting_name() == "Reset"


# LQ-171273
@when('the user click the "Asset Inspection" sub-menu under Maintenance menu')
def click_asset_inspection_sub_menu():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_assetinspection_submenu()
    FLEET_TELEMATICS_PAGE.scroll_page_up()


@then('the user should be navigated to the "Asset Inspection" page and all the UI components should be loaded')
def verify_asset_inspection_page():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.assetinspection_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.search_bar_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.filters_option_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.defect_lists_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.inspection_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.sort_by_asset_is_displayed() is True


# LQ-171276
@when('the user clicks the dropdown icon present near the "Sort by: Asset" button')
def click_sort_by_asset_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.click_sort_by_asset_dropdown()


@then('the user should be able to see the options such as "Asset","Date" and "Duration"')
def verify_sort_by_asset_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_asset_option_text() == "Asset"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_option_text() == "Date"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_duration_option_text() == "Duration"


@when('the user clicks the Settings icon box present in the left-side top corner')
def click_settings_icon():
    FLEET_TELEMATICS_CENTER_PAGE.click_settings_icon()


@then('the user should be able to see all the options')
def verify_settings_icon_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_reset_to_default_text() == "Reset to default"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_and_time_text() == "Date & Time"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_asset_name_text() == "Asset Name"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_driver_text() == "Driver"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_status_text() == "Status"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_defects_text() == "Defects"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_comments_text() == "Comments"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_inspection_type_text() == "Inspection Type"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_asset_type_text() == "Asset Type"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_certification_text() == "Certification"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_duration_text() == "Duration"


# LQ-146436
@when('the user clicks the Faults submenu under Maintenance menu')
def click_faults_under_maintenance():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_faults_subchild()


@then(
    'the user should be navigated to the "Faults" page with elements such as "Filter", "Sort by: Fault Code", "Report", "Dismiss faults" and "Columns" present in the page')
def verify_faults_page():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.faults_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.filter_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.sort_by_fault_code_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.report_button_in_fault_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.dismiss_faults_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.columns_button_is_displayed() is True


# LQ-146437
@when('the user clicks the dropdown icon present near the "Sort by: Fault Code" button')
def click_sort_by_fault_code_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.click_sort_by_fault_code_dropdown()


@then(
    'the user should be able to see the options such as "Fault Code","Description","Times Logged","Source" and "Severity" available')
def verify_sort_by_fault_code_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_fault_code_option_text() == "Fault Code"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_description_option_text() == "Description"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_times_logged_option_text() == "Times Logged"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_source_option_text() == "Source"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_severity_option_text() == "Severity"


@when('the user clicks the "Columns" drop down box present in the left-side top corner')
def click_columns_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.click_columns_dropdown()


@then(
    'the user should be able to see the columns such as "Reset to default", "Fault Code", "Description", "Current Status", "Times Logged", "Source", "Protocol", "Advanced Details", "Selection", "Severity" and "Controller"  available')
def verify_columns_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_reset_to_default_text() == "Reset to default"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_fault_code_text() == "Fault Code"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_description_text() == "Description"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_current_status_text() == "Current Status"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_times_logged_text() == "Times Logged"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_source_text() == "Source"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_protocol_text() == "Protocol"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_advanced_details_text() == "Advanced Details"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_selection_text() == "Selection"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_severity_text() == "Severity"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_controller_text() == "Controller"


# LQ-146446
@when('the user clicks the "Measurements" submenu')
def click_measurements_under_maintenance():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_measurements_subchild()


@then(
    'the user should be navigated to the "Measurements" page with elements such as "Filters", "Group by: Diagnostic" and "Report" present in the page')
def verify_measurements_page():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.measurements_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.filter_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.group_by_diagnostic_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.report_button_in_measurement_page_is_displayed() is True


@when('the user clicks the dropdown icon present near the "Group by: Diagnostic" textbox')
def click_group_by_diagnostic_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.click_group_by_diagnostic_dropdown()


@then('the user should be able to see the options "Diagnostic","Date" options')
def verify_group_by_diagnostic_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_diagnostic_option_text() == "Diagnostic"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_date_option_text() == "Date"


# LQ-147534
@when('the user clicks the "Speed Profile" child-menu')
def click_speed_profile_under_maintenance():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_speed_profile_subchild()


@then(
    'the user should be navigated to the "Speed Profile" page and user see "Filters" and "View trips" buttons in the headers')
def verify_speed_profile_page():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.speed_profile_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.filter_button_in_speed_profile_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.view_trips_button_is_displayed() is True


# LQ-147545
@when('the user clicks the "Log Data and Collisions" child-menu')
def click_log_data_and_collisions():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_log_data_and_collisions_subchild()


@then(
    'the user should be navigated to the "Log Data and Collisions" page and the user see "Reports","Search", "Filters", and "Sort by: Vehicle and date/time" menu')
def verify_log_data_and_collisions_page():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.log_data_and_collisions_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.reports_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.search_bar_log_data_and_collisions_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.filters_menu_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.sort_by_vehicle_and_date_time_is_displayed() is True


@when('the user clicks the "Sort by: Vehicle and date/time" dropdown')
def click_sort_by_vehicle_and_date_time_dropdown():
    if FLEET_TELEMATICS_CENTER_PAGE.apply_changes_button_is_displayed():
        FLEET_TELEMATICS_CENTER_PAGE.click_filter_menu()
    FLEET_TELEMATICS_CENTER_PAGE.click_sort_by_vehicle_and_date_time_dropdown()


@then(
    'the user should see options "Vehicle and date/time", "Reason and date/time" and "Record type and date/time" available')
def verify_sort_by_vehicle_and_date_time_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_vehicle_and_date_time_option_text() == "Vehicle and date/time"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_reason_and_date_time_option_text() == "Reason and date/time"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_record_type_and_date_time_option_text() == "Record type and date/time"


@when('the user clicks Maintenance menu - Asset Inspection submenu')
def navigate_to_assetInspection():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_maintenance_menu()
    FLEET_TELEMATICS_PAGE.click_assetinspection_submenu()


@then('the user should be navigated to the "Asset Inspection" page')
def verify_assetInspection_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.assetinspection_header_is_displayed() is True


# LQ-
@when('the user clicks Maintenance menu - Diagnostics submenu - Faults subchild')
def navigate_to_diagnostics():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_diagnostics_submenu_dropdown()
    FLEET_TELEMATICS_PAGE.click_faults_subchild()


@then('the user should be navigated to the "Faults" page')
def verify_diagnostics_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.faults_header_is_displayed() is True


# LQ-
@when('the user clicks Maintenance menu - Diagnostics submenu - Measurements subchild')
def navigate_to_measurements():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_measurements_subchild()


@then('the user should be navigated to the "Measurements" page')
def verify_measurements_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.measurements_header_is_displayed() is True


# LQ-
@when('the user clicks Maintenance menu - Reminders submenu')
def navigate_to_reminders():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_reminders_submenu()


@then('the user should be navigated to the "Reminders" page')
def verify_reminders_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.maintenanceschedules_header_is_displayed() is True


# LQ-
@when('the user clicks Sustainability menu - Sustainability Overview submenu')
def navigate_to_sustainabilityOverview():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_sustainability_menu()
    FLEET_TELEMATICS_PAGE.click_sustainabilityoverview_submenu()


@then('the user should be navigated to the "Sustainability Overview" page')
def verify_sustainabilityOverview_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.sustainabilityoverview_header_is_displayed() is True


# LQ-
@when('the user clicks Sustainability menu - Fuel & EV energy usage submenu')
def navigate_to_fuelEVenergyUsage():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_fuel_energy_usage_submenu()


@then('the user should be navigated to the "Fuel & EV energy usage" page')
def verify_fuelEVenergyUsage_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.mfuel_and_ev_energyusage_header_is_displayed() is True


# LQ-
@when('the user clicks Sustainability menu - EV Battery Health submenu')
def navigate_to_eVBatteryHealth():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_evbatteryhealth_submenu()


@then('the user should be navigated to the "EV Battery Health" page')
def verify_eVBatteryHealth_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.ev_batteryhealth_header_is_displayed() is True


# LQ-
@when('the user clicks Sustainability menu - EV Charging History submenu')
def navigate_to_eVChargingHistory():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_evcharginghistory_submenu()


@then('the user should be navigated to the "EV Charging History" page')
def verify_eVChargingHistory_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.ev_charginghistory_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.reports_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.status_change_sort_direction_is_displayed() is True


# LQ-
@when('the user clicks Sustainability menu - BEV Range Capability submenu')
def navigate_to_bEVRangeCapability():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_bevrangecapability_submenu()


@then('the user should be navigated to the "BEV Range Capability" page')
def verify_bEVRangeCapability_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.bev_rangecapability_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.rc_report_dropdown_is_displayed() is True


# LQ-
@when('the user clicks Reports menu - My Reports submenu')
def navigate_to_myReports():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_reports_menu()
    FLEET_TELEMATICS_PAGE.click_myreports_submenu()


@then('the user should be navigated to the "My Reports" page')
def verify_myReports_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    FLEET_TELEMATICS_PAGE.wait_for_page_to_fully_load()
    assert FLEET_TELEMATICS_CENTER_PAGE.myreports_header_is_displayed() is True


# LQ-
@when('the user clicks Reports menu - Report Setup submenu')
def navigate_to_myReports():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_report_setup_submenu()


@then('the user should be navigated to the "Report Setup" page')
def verify_myReports_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.report_setup_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zt_search_name_comment_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.type_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.custom_report_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.upload_file_is_displayed() is True


# LQ-136768
@when('the user clicks Rules & Exceptions menu - Rules submenu')
def navigate_to_rulesExceptions():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_rulesandexceptions_menu()
    FLEET_TELEMATICS_PAGE.click_rules_submenu()


@then('the user should be navigated to the "Rules" page, header and safety section should be displayed')
def verify_rulesExceptions_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.rules_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.safetysection_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.zt_search_name_comment_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.addrules_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.reprocessdata_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.notification_template_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.distribution_lists_is_displayed() is True


# LQ-94886
@when('the user clicks on the "Add" button in the Rules page')
def click_add_rules():
    FLEET_TELEMATICS_CENTER_PAGE.click_addrules_button()


@then(
    'the user should be navigated to the "Exception Rule Edit" page and should be able to see tabs such as name, condition, notifications and media upload tab, save and cancel buttons and 7 colors')
def verify_exception_rule_edit_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.exception_rule_edit_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.name_tab_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.comment_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.condition_tab_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.notifications_tab_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.media_tab_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.save_button_is_displayed() is True


@then('the user should be able to see fields such as "name", "color", "Publish to groups", "Comment"')
def verify_fields_in_name_tab():
    assert FLEET_TELEMATICS_CENTER_PAGE.name_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.color_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.publish_to_groups_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.comment_field_is_displayed() is True


@given('the user clicks on the "Publish to groups" dropdown field')
def click_publish_to_groups_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.click_publish_to_groups_drop_down()


@when('the user selects any group from the dropdown')
def select_group_from_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.select_first_group_from_dropdown()


@then('the user should be able to see selected groups')
def verify_groups_in_dropdown():
    assert FLEET_TELEMATICS_CENTER_PAGE.all_groups_displayed_in_dropdown() == "Asset Information"


@when('the user click the cross mark symbol present next to the selected groups')
def click_cross_mark_next_to_selected_groups():
    FLEET_TELEMATICS_CENTER_PAGE.click_cross_mark_next_to_selected_groups()


@then('the user should not see the groups that was selected')
def verify_groups_are_removed():
    assert FLEET_TELEMATICS_CENTER_PAGE.all_groups_removed() is False


@when('the user clicks on the "Condition" tab')
def click_condition_tab():
    FLEET_TELEMATICS_CENTER_PAGE.click_condition_tab()


@then('the user should be navigated to Conditions page and the user should see "Engine data"')
def verify_conditions_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.condition_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.engine_data_condition_is_displayed() is True


@when('the user clicks on the "Engine data" condition box')
def click_engine_data_condition():
    FLEET_TELEMATICS_CENTER_PAGE.click_engine_data_condition()


@then('the user should see options such as "Active Fault", "Any Fault" and "Measurement or Data"')
def verify_engine_data_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_active_fault_option_text() == "Active Fault"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_any_fault_option_text() == "Any Fault"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_measurement_or_data_option_text() == "Measurement or Data"


@then('the user should see all the components under "Engine data"')
def verify_engine_data_components():
    assert FLEET_TELEMATICS_CENTER_PAGE.engine_data_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.type_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.diagnostic_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.add_a_condition_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.display_all_diagnostic_field_is_displayed() is True


@when('the user clicks "Zone or Zone Type" text box')
def click_zone_or_zone_type_textbox():
    FLEET_TELEMATICS_CENTER_PAGE.click_zone_or_zone_type_textbox()


@then('the user should navigate to the "Zone or Zone Type" page')
def verify_zone_or_zone_type_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.zone_header_is_displayed() is True


@then('the user should be able to see options named "Type", "Zone" and "Event"')
def verify_zone_or_zone_type_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_type_option_text() == "Type"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_zone_option_text() == "Zone"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_event_option_text() == "Event"


@then(
    'the user should see all the Event types names "Entering", "Exiting", "Outside", "inside" and "Inside", "add" and "cancel" button and "add a Condition" input box')
def verify_event_types_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_entering_option_text() == "Entering"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_exiting_option_text() == "Exiting"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_outside_option_text() == "Outside"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_inside_option_text() == "Inside"
    assert FLEET_TELEMATICS_CENTER_PAGE.add_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.add_a_condition_field_is_displayed() is True


#   LQ-144502
@when('the user clicks "Roads with speed limit" text box')
def click_roads_with_speed_limit_textbox():
    FLEET_TELEMATICS_CENTER_PAGE.click_roads_with_speed_limit_textbox()


@then(
    'the user should be able to see the Dialog box named "Roads with speed limit" and "Over" and "Under" and an empty text box under that with unit "mph"')
def verify_roads_with_speed_limit_dialog_box():
    assert FLEET_TELEMATICS_CENTER_PAGE.roads_with_speed_limit_dialog_box_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.get_over_option_text() == "Over"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_under_option_text() == "Under"
    assert FLEET_TELEMATICS_CENTER_PAGE.empty_text_box_under_over_and_under_is_displayed() is True


#  LQ-144503
@then('the user should see "Add" and "Cancel" button and input box "Add a condition..."')
def verify_add_and_cancel_button_in_roads_with_speed_limit():
    assert FLEET_TELEMATICS_CENTER_PAGE.add_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.add_a_condition_field_is_displayed() is True


@when('the user clicks "Speed" text box')
def click_speed_textbox():
    FLEET_TELEMATICS_CENTER_PAGE.click_speed_textbox()


@then(
    'the user should be able to see the Dialog box named "Speed" with "Over" and "Under" and an empty text box under that with unit "mph"')
def verify_speed_dialog_box():
    assert FLEET_TELEMATICS_CENTER_PAGE.speed_dialog_box_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.get_over_option_text() == "Over"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_under_option_text() == "Under"
    assert FLEET_TELEMATICS_CENTER_PAGE.empty_text_box_under_over_and_under_is_displayed() is True


# LQ-144512
@when('the user clicks "Speed limit" text box')
def click_speed_limit_textbox():
    FLEET_TELEMATICS_CENTER_PAGE.click_speed_limit_textbox()


@then(
    'the user should be able to see the Dialog box named "Speed limit" with the field named "Truck speed limit" with "Yes" and "No" buttons')
def verify_speed_limit_dialog_box():
    assert FLEET_TELEMATICS_CENTER_PAGE.speed_limit_dialog_box_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.truck_speed_limit_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.yes_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.no_button_is_displayed() is True


@then(
    'the user should see the field named "Over the limit by" and an empty textbox and field named "Exclude estimated speed limits" with "On", "Off" buttons')
def verify_fields_in_speed_limit_dialog_box():
    assert FLEET_TELEMATICS_CENTER_PAGE.over_the_limit_by_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.exclude_estimated_speed_limits_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.on_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.off_button_is_displayed() is True


# LQ-144513
@when('the user clicks the dropdown present near to "More" in condition tab')
def click_more_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.click_more_dropdown()


@then(
    'the user should see a header named "Device" and the options "Ignition", "Asset", "Driver", "Group", "Asset Inspection Defect"')
def verify_more_dropdown_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_device_header_text() == "Device"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_ignition_option_text() == "Ignition"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_asset_option_text() == "Asset"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_driver_option_text() == "Driver"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_group_option_text() == "Group"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_asset_inspection_defect_option_text() == "Asset Inspection defect"


# LQ-144514
@then('the user should see a header named "Trip" and the options "Driving", "Stop", "Trip distance", "Trip duration"')
def verify_more_dropdown_trip_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_trip_header_text() == "Trip"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_driving_option_text() == "Driving"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_stop_option_text() == "Stop"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_trip_distance_option_text() == "Trip distance"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_trip_duration_option_text() == "Trip duration"


# LQ-144516
@then(
    'the user should see a header named "Auxiliaries" and the options "Aux 1", "Aux 2", "Aux 3", "Aux 4", "Aux 5", "Aux 6", "Aux 7", "Aux 8"')
def verify_more_dropdown_auxiliaries_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_auxiliaries_header_text() == "Auxiliaries"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_aux_1_option_text() == "Aux 1"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_aux_2_option_text() == "Aux 2"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_aux_3_option_text() == "Aux 3"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_aux_4_option_text() == "Aux 4"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_aux_5_option_text() == "Aux 5"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_aux_6_option_text() == "Aux 6"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_aux_7_option_text() == "Aux 7"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_aux_8_option_text() == "Aux 8"


# LQ-144589
@then(
    'the user should see a header named "Work Hours" and the options "After work hours rule", "Work hours rule", "After work hours device", "Device work hours"')
def verify_more_dropdown_work_hours_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_work_hours_header_text() == "Work Hours"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_after_work_hours_rule_option_text() == "After work hours rule"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_work_hours_rule_option_text() == "Work hours rule"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_after_work_hours_device_option_text() == "After work hours device"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_device_work_hours_option_text() == "Device work hours"


# LQ-144566
@then(
    'the user should see a header named "Wrappers" and the options "Is value more than", "Is value less than", "Is value equal to"')
def verify_more_dropdown_wrappers_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_wrappers_header_text() == "Wrappers"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_is_value_more_than_option_text() == "Is value more than"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_is_value_less_than_option_text() == "Is value less than"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_is_value_equal_to_option_text() == "Is value equal to"


@then('user should see header named "Logic" with the options "And", "Or" available')
def verify_more_dropdown_logic_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_logic_header_text() == "Logic"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_and_option_text() == "And"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_or_option_text() == "Or"


# LQ-144567
@when('the user clicks Notifications tab')
def click_notifications_tab():
    FLEET_TELEMATICS_CENTER_PAGE.click_notifications_tab()


@then(
    'the user should be navigated to Notifications page with header "NOTIFICATION RECIPIENTS" and "Add email", "Add alert", "Add driver feedback", "More" options')
def verify_notifications_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.notifications_recipients_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.add_email_option_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.add_alert_option_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.add_driver_feedback_option_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.more_option_is_displayed() is True


@then('user should see Summary under "HELP" Section')
def verify_help_section_in_notifications_tab():
    assert FLEET_TELEMATICS_CENTER_PAGE.help_section_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.summary_in_help_section_is_displayed() is True


# LQ-144568
@when('the user clicks "AddEmail" Button')
def click_add_email_button():
    FLEET_TELEMATICS_CENTER_PAGE.click_add_email_option()


@then('the user should see the Fields Template and Email')
def verify_add_email_fields():
    assert FLEET_TELEMATICS_CENTER_PAGE.template_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.email_field_is_displayed() is True


# LQ-144568
@when('the user clicks the dropdown of the Template field')
def click_template_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.click_template_dropdown()


@then('the user should see the "Default email template" and "Add new template"')
def verify_template_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_default_email_template_option_text() == "Default email template"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_add_new_template_option_text() == "Add new template"


# LQ-144568
@when('the user clicks the Add new template')
def click_add_new_template_option():
    FLEET_TELEMATICS_CENTER_PAGE.click_add_new_template_option()


@then('the user should see pop-up')
def verify_add_new_template_popup():
    assert FLEET_TELEMATICS_CENTER_PAGE.warning_popup_is_displayed() is True


# LQ-144568
@when('the user clicks the textbox of the email')
def click_email_textbox():
    FLEET_TELEMATICS_CENTER_PAGE.click_email_textbox()


@then('the user should see the dropdown with valid and invalid email IDs')
def verify_email_dropdown():
    assert FLEET_TELEMATICS_CENTER_PAGE.email_dropdown_is_displayed() is True


# LQ-144590
@when('the user clicks the dropdown present near the Option "Add alert"')
def click_add_alert_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.click_add_alert_dropdown()


@then('the user should see the "Popup" alert and the "Description"')
def verify_add_alert_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_popup_option_text() == "Popup"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_popup_description_option_text() == "Display a yellow, low-priority popup alert at the top of the screen"


@then('the user should see the "Urgent popup" alert and the "Description"')
def verify_urgent_popup_option():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_urgent_popup_option_text() == "Urgent popup"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_urgent_popup_description_text() == "Display a red popup for each instance of an alert. Note: This can produce excessive notifications for easily-triggered rules."


@then('the user should see the "Log only" alert and the "Description"')
def verify_log_only_option():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_log_only_option_text() == "Log only"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_log_only_description_text() == 'Log a notification in "My Notifications"'


# LQ-144591
@when('the user clicks the dropdown present near the Option "Add driver feedback"')
def click_add_driver_feedback_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.click_add_driver_feedback_dropdown()


@then('the user should see the "Beep three times" and the respective "Description"')
def verify_beep_three_times_option():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_beep_three_times_text() == "Beep three times"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_beep_three_times_description_text() == "Beep the device three times"


@then('the user should see the "Beep three times rapidly" and the respective "Description"')
def verify_beep_three_times_rapidly_option():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_beep_three_times_rapidly_text() == "Beep three times rapidly"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_beep_three_times_rapidly_description_text() == "Rapidly beep the device three times"


@then('the user should see the "Beep ten times rapidly" and the respective "Description"')
def verify_beep_ten_times_rapidly_option():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_beep_ten_times_rapidly_text() == "Beep ten times rapidly"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_beep_ten_times_rapidly_description_text() == "Rapidly beep the device ten times"


@then('the user should see the "Text message" and the respective "Description"')
def verify_text_message_option():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_text_message_option_text() == "Text message"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_text_message_description_text() == "Send a text notification to a compatible device. This will be spoken aloud on the driver's application if the asset is in motion."


@then('the user should see the "GO TALK" and the respective "Description"')
def verify_go_talk_option():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_go_talk_option_text() == "GO TALK"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_go_talk_description_text() == "Send a message that will be spoken to the driver (requires an IOX-GOTALK)"


@then('the user should see the "Change status" and the respective "Description"')
def verify_change_status_option():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_change_status_option_text() == "Change status"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_change_status_description_text() == "Prompt the driver to change their status on a connected compatible device"


# LQ-144592
@when('the user clicks the dropdown present near the "More" options')
def click_more_options_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.click_more_options_dropdown()


@then('the user should see the "Web request" and the respective "Description"')
def verify_more_options_web_request_option():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_web_request_option_text() == "Web request"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_web_request_description_text() == "Make an HTTP GET or POST web request."


@then('the user should see the "Assign to group" and the respective "Description"')
def verify_more_options_assign_to_group_option():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_assign_to_group_option_text() == "Assign to group"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_assign_to_group_description_text() == "Assign asset to specified group."


@then('the user should see the "Email to group" and the respective "Description"')
def verify_more_options_email_to_group_option():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_email_to_group_option_text() == "Email to group"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_email_to_group_description_text() == "Email to users in selected group"


@then('the user should see the "Distribution list" and the respective "Description"')
def verify_more_options_distribution_list_option():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_distribution_list_option_text() == "Distribution list"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_distribution_list_description_text() == "Send notification to distribution list"


@then('the user should see the "Assign as Personal/Business" and the respective "Description"')
def verify_more_options_assign_as_personal_business_option():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_assign_as_personal_business_option_text() == "Assign as Personal/Business"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_assign_as_personal_business_description_text() == "Put asset(s) into Personal Mode (no GPS tracking) or Business Mode."


# LQ-144593
@when('the user clicks Media Upload tab')
def click_media_upload_tab():
    FLEET_TELEMATICS_CENTER_PAGE.click_media_upload_tab()


@then('the user should see "MEDIA UPLOAD SETTINGS" with "Media type" with an information symbol')
def verify_media_upload_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.media_upload_settings_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.media_type_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.information_symbol_is_displayed() is True


# LQ-144593
@when('the user hovers on to the symbol')
def hover_on_information_symbol():
    FLEET_TELEMATICS_CENTER_PAGE.hover_on_information_symbol()


@then('the user should see the message "The type of media when a rule is triggered."')
def verify_information_symbol_message():
    assert FLEET_TELEMATICS_CENTER_PAGE.information_symbol_message_is_displayed() is True


@then('the user sees three buttons "Video", "Snapshot" and "None"')
def verify_media_type_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.video_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.snapshot_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.none_button_is_displayed() is True


# LQ-144602
@given('user clicks back button in the Exception Rule Edit page')
def click_back_button_in_exception_rule_edit_page():
    FLEET_TELEMATICS_CENTER_PAGE.click_back_button()


@when('the user clicks on the "Notification Templates" button in the header')
def click_notification_templates_button():
    FLEET_TELEMATICS_CENTER_PAGE.click_notification_template_button()


@then(
    'the user should be redirected to the "Notifications Templates" page and user should see the Options "Search","Sort by : Name", "Add email template", "Add web template", "Add text template"')
def verify_notification_templates_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.notification_templates_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.search_option_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.sort_by_name_option_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.add_email_template_option_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.add_web_template_option_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.add_text_template_option_is_displayed() is True


# LQ-146703
@when('the user clicks "Add email template" button')
def click_add_email_template_button():
    FLEET_TELEMATICS_CENTER_PAGE.click_add_email_template_button()
    FLEET_TELEMATICS_CENTER_PAGE.wait_for_page_to_fully_load()


@then(
    'the "Email Template Edit" page is displayed with parameters such as "Name", "Subject", "Body", "Exception Report"')
def verify_email_template_edit_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.email_template_edit_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.name_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.subject_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.body_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.exception_report_field_is_displayed() is True


# LQ-146703
@when('the user clicks the dropdown present next to "Do not attach Exceptions Detail Report" textbox')
def click_do_not_attach_exceptions_detail_report_dropdown():
    FLEET_TELEMATICS_CENTER_PAGE.click_do_not_attach_exceptions_detail_report_dropdown()


@then(
    'the user should be able to see the dropdown options "Do not attach Exceptions Detail Report", "Default Exceptions Detail Report", "Possible Collisions" and "Advanced Exceptions Detail Report"')
def verify_exceptions_detail_report_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_do_not_attach_exceptions_detail_report_option_text() == "Do not attach Exceptions Detail report"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_default_exceptions_detail_report_option_text() == "Default Exceptions Detail Report"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_possible_collisions_option_text() == "Possible Collisions"
    assert FLEET_TELEMATICS_CENTER_PAGE.get_advanced_exceptions_detail_report_option_text() == "Advanced Exceptions Detail Report"


@then(parsers.parse(
    'the user should be able to see Available Tokens {S__No}, {Token_Name} and {Description} in a tabular format'))
def verify_available_tokens_section(S__No, Token_Name, Description):
    index = int(S__No)
    token_name = FLEET_TELEMATICS_CENTER_PAGE.get_tokens_name(index)
    token_desc = FLEET_TELEMATICS_CENTER_PAGE.get_token_description(index)

    assert token_name == Token_Name
    assert token_desc == Description


# LQ-144747
@given('user closes "Add Email Template" page')
def close_add_email_template_page():
    FLEET_TELEMATICS_CENTER_PAGE.click_cancel_button_in_email_template_edit_page()


@when('the user clicks "Add web template" button')
def click_add_web_template_button():
    FLEET_TELEMATICS_CENTER_PAGE.click_add_web_template_button()


@then(
    'the "Web Request Template Edit" page is displayed with parameters "Template Name", "URL", "HTTP request type" and "Available Tokens"')
def verify_web_request_template_edit_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.web_request_template_edit_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.template_name_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.url_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.http_request_type_field_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.available_tokens_section_is_displayed() is True


@then('the user should see 2 toggle buttons "GET" & "POST" for "HTTP request type"')
def verify_http_request_type_options():
    assert FLEET_TELEMATICS_CENTER_PAGE.get_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.post_button_is_displayed() is True


# LQ-
@when('the user clicks Rules & Exceptions menu - Exceptions submenu')
def navigate_to_Exceptions():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_exceptions_submenu()


@then('the user should be navigated to the "Exceptions" page')
def verify_exceptions_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.exceptions_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.reports_button_is_displayed() is True


# LQ-
@when('the user clicks Messages menu')
def navigate_to_messages():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_messages_menu()


@then('the user should be navigated to the "Messages" page')
def verify_messages_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_CENTER_PAGE.message_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.new_message_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.pa_search_assets_is_displayed() is True


# LQ-165571
@when('the user clicks the "Message" button present with plus symbol')
def click_message_button():
    FLEET_TELEMATICS_CENTER_PAGE.click_new_message_button()


@then('the user should see a pop up opening with a title "New Message" with a description "Messages can be sent '
      'to multiple assets and users. Select all that apply. Replies are only visible to you", search filter with a '
      'water mark "Search for asset or user" and the user sees "Compose message" button is disabled.')
def verify_new_message_popup():
    assert FLEET_TELEMATICS_CENTER_PAGE.new_message_popup_header_title() == "New message"
    assert FLEET_TELEMATICS_CENTER_PAGE.new_message_popup_description() == "Messages can be sent to multiple assets and users. Select all that apply. Replies are only visible to you."
    assert FLEET_TELEMATICS_CENTER_PAGE.search_filter_is_displayed_in_message_popup() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.compose_message_button_is_disabled() is True


@then('the user should see list of assets under "Assets" sub-tab with checkboxes.')
def verify_assets_list_in_message_popup():
    assert FLEET_TELEMATICS_CENTER_PAGE.assets_subtab_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.assets_list_with_checkboxes_is_displayed() is True


@when('the user clicks the "Users" sub-tab')
def click_users_subtab_in_message_popup():
    FLEET_TELEMATICS_CENTER_PAGE.click_users_subtab_in_message_popup()


@then('the user should see the list of users with checkboxes.')
def verify_users_list_in_message_popup():
    assert FLEET_TELEMATICS_CENTER_PAGE.users_list_with_checkboxes_is_displayed() is True


# @LQ-165575
@when(
    'the user selects any user under "Users" tab and the user should see the "Compose message" button enabled and the user clicks the "Compose message" button')
def select_user_in_message_popup():
    FLEET_TELEMATICS_CENTER_PAGE.select_any_user_in_message_popup()
    FLEET_TELEMATICS_CENTER_PAGE.click_compose_message_button()


@then(
    'the user should see a dialog box with the options "back to asset selection" , user name , search icon and cross mark symbol')
def verify_compose_message_dialog_box():
    assert FLEET_TELEMATICS_CENTER_PAGE.back_to_asset_selection_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.user_name_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.search_icon_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.cross_mark_symbol_is_displayed() is True


# LQ-
@when('the user clicks Notifications menu')
def navigate_to_notifications():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_notifications_menu()


@then('the user should be navigated to the "Notifications" page, header and notification types should be displayed')
def verify_notifications_header():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    FLEET_TELEMATICS_PAGE.scroll_page_up()
    assert FLEET_TELEMATICS_CENTER_PAGE.notifications_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.notifications_types_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.pa_search_assets_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.reload_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.status_change_sort_direction_is_displayed() is True


# LQ-146401
@when('the user clicks the dropdown present near "Config" menu')
def navigate_to_config_menu():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_config_menu()


@then('the user should see of all the submenus under Config')
def verify_submenus():
    assert FLEET_TELEMATICS_PAGE.fleet_settings_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE.work_hours_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE.holidays_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE.audit_log_submenu_is_displayed() is True


# LQ-151000
@when('the user clicks the "Fleet Settings" sub-menu and navigates to System Settings page')
def navigate_to_fleet_settings():
    FLEET_TELEMATICS_PAGE.click_fleet_settings_submenu()


@then('the user should be able to see all of the headers in the System Settings page')
def verify_system_settings():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    FLEET_TELEMATICS_PAGE.scroll_page_up()
    assert FLEET_TELEMATICS_CENTER_PAGE.system_settings_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.general_tab_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.maps_tab_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.hos_tab_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.user_account_tab_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.communications_tab_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.data_purge_tab_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.addins_tab_is_displayed() is True


# LQ-151090
@when('the user clicks the "Work Hours" sub-menu')
def navigate_to_work_hours():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_work_hours_submenu()


@then(
    'the user should be navigated to "Work Hours" page with a "Work Hours" button, fields like "Search", "Sort by: Name" and "Total items", and see all of the work hours available')
def verify_work_hours():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    FLEET_TELEMATICS_PAGE.scroll_page_up()
    assert FLEET_TELEMATICS_CENTER_PAGE.work_hours_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.work_hours_search_box_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.sort_by_name_button_is_displayed() is True
    assert_that(FLEET_TELEMATICS_CENTER_PAGE.all_hours_text_is_displayed(), contains_string("All hours"))
    assert_that(FLEET_TELEMATICS_CENTER_PAGE.early_departure_hours_text_is_displayed(),
                contains_string("Early departure hours"))
    assert_that(FLEET_TELEMATICS_CENTER_PAGE.late_arrival_text_hours_is_displayed(),
                contains_string("Late arrival hours"))
    assert_that(FLEET_TELEMATICS_CENTER_PAGE.lunch_hours_text_is_displayed(), contains_string("Lunch hours"))
    assert_that(FLEET_TELEMATICS_CENTER_PAGE.standard_hours_text_is_displayed(), contains_string("Standard hours"))


# LQ-151111
@when('the user clicks the "Audit Log" menu')
def navigate_to_audit_log():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_audit_log_submenu()


@then(
    'the user should be redirected to "Audit Log" page with "Search","Options" and "Reports" fields, and user login details with the email id and Time')
def verify_audit_log():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    FLEET_TELEMATICS_PAGE.scroll_page_up()
    assert FLEET_TELEMATICS_CENTER_PAGE.audit_log_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.audit_log_search_box_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.options_drop_down_is_displayed() is True
    assert_that(FLEET_TELEMATICS_CENTER_PAGE.user_login_text_is_displayed(), contains_string("User login"))


@when('the user clicks the "Holidays" menu')
def navigate_to_audit_log():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_holidays_submenu()


@then(
    'the user should be redirected to "Holidays" page and should have Holidays header, search, add holiday and table consisting of name, date and group')
def verify_audit_log():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    FLEET_TELEMATICS_PAGE.scroll_page_up()
    assert FLEET_TELEMATICS_CENTER_PAGE.holidays_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.search_bar_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.add_holiday_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.name_column_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.date_column_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.group_column_header_is_displayed() is True


@when('the user clicks on Add Holiday button')
def click_add_holiday_button():
    FLEET_TELEMATICS_CENTER_PAGE.click_add_holiday_button()


@then(
    'add holiday page should be opened with fields like name, date, holiday group id with default value as 1, enabled cancel and disabled save button')
def verify_add_holiday_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.add_holiday_page_header_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.holiday_name_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.holiday_date_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.holiday_group_id_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.cancel_holiday_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.save_holiday_button_is_displayed() is False
    assert FLEET_TELEMATICS_CENTER_PAGE.default_group_id_value_1_is_displayed() is True
