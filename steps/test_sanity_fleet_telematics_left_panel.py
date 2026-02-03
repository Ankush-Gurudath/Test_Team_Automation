from hamcrest import assert_that, contains_string
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then
from data.prod.fleet_telematics_prod import FleetTelematicsDataProd as FTD_PROD
from data.stg.fleet_telematics_stg import FleetTelematicsDataStg as FTD_STG
from data.int.fleet_telematics_int import FleetTelematicsDataInt as FTD_INT
from pages.dashboard_page import DashboardPage
from pages.fleet_telematics_center_page import FleetTelematicsCenterPage
from pages.fleet_telematics_left_panel_page import FleetTelematicsPageLeftPanel
from pages.geotab_page_add_ins_page import GeotabPageAddIns
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage
from pages.video_search_page import VideoSearchPage
from steps.common import NEW_UI_FTM_URL
from steps.common import ENV

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
BASE_PAGE = 0
FLEET_TELEMATICS_PAGE = 0
FLEET_TELEMATICS_CENTER_PAGE = 0
VIDEO_SEARCH_PAGE = 0
FTD = 0
USER_MANAGEMENT_PAGE = 0
GEOTAB_PAGE = 0

scenarios('../features/sanity_fleet_telematics_left_panel.feature')


# LQ-306
@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, FTD, FLEET_TELEMATICS_PAGE, VIDEO_SEARCH_PAGE, USER_MANAGEMENT_PAGE, FLEET_TELEMATICS_CENTER_PAGE, GEOTAB_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    FLEET_TELEMATICS_PAGE = FleetTelematicsPageLeftPanel(browser)
    VIDEO_SEARCH_PAGE = VideoSearchPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)
    FLEET_TELEMATICS_CENTER_PAGE = FleetTelematicsCenterPage(browser)
    GEOTAB_PAGE = GeotabPageAddIns(browser)

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
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.enter_username(FTD.username)
    LOGIN_PAGE.enter_password(FTD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_multi_company(FTD.company_name)
    LOGIN_PAGE.click_select_company_button()
    LOGIN_PAGE.wait_for_page_load()


@then('the user is successfully in the Driver Safety dashboard')
def verify_driver_safety_tabs():
    assert DASHBOARD_PAGE.lytx_logo_is_displayed()
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert DASHBOARD_PAGE.no_of_unassigned_drivers_is_displayed()
    assert DASHBOARD_PAGE.get_unassigned_drivers_text() == "UNASSIGNED DRIVERS"
    assert_that(DASHBOARD_PAGE.get_unassigned_drivers_text(), contains_string("UNASSIGNED DRIVER"))
    assert DASHBOARD_PAGE.get_due_for_coaching_text() == "DUE FOR COACHING"
    assert DASHBOARD_PAGE.get_fyi_notify_text() == "FYI NOTIFY"
    assert_that(DASHBOARD_PAGE.get_collisions_text(), contains_string('COLLISION'))
    assert_that(DASHBOARD_PAGE.get_possible_collisions_text(), contains_string("POSSIBLE COLLISION"))
    # Commenting below till MEGA-3698 is resolved
    # # Validate all dashboard details links contain the expected label
    # for _name, link_text in DASHBOARD_PAGE.get_all_dashboard_details_links().items():
    #     assert_that(link_text, contains_string("View Details"))


@when('the user clicks on Tasks > Due For Coaching')
def click_due_for_coaching():
    DASHBOARD_PAGE.click_tasks()
    FLEET_TELEMATICS_PAGE.click_due_for_coaching_submenu()


@then('the user should see page header Due For Coaching with tasks count')
def verify_due_for_coaching_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.due_for_coaching_header_is_displayed()


@when('the user clicks on Tasks > Assign Drivers')
def click_assign_drivers():
    FLEET_TELEMATICS_PAGE.click_assign_drivers_submenu()


@then('the user should see page header Assign Drivers with tasks count')
def verify_assign_drivers_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.assign_driver_header_is_displayed()


@when('the user clicks on Tasks > Collision')
def click_collision():
    FLEET_TELEMATICS_PAGE.click_collisions_submenu()


@then('the user should see page header Collision with tasks count')
def verify_collision_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.collisions_header_is_displayed()


@when('the user clicks on Tasks > FYI Notify')
def click_fyi_notify():
    FLEET_TELEMATICS_PAGE.click_fyinotify_submenu()


@then('the user should see page header FYI Notify with tasks count')
def verify_fyi_notify_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.fyinotify_header_is_displayed()


@when('the user clicks on Insights > Open Tasks Report')
def click_open_task_report():
    FLEET_TELEMATICS_PAGE.click_insights_menu()
    FLEET_TELEMATICS_PAGE.click_open_tasks_report_submenu()


@then('the user should see page header Open Tasks Report with drivers count')
def verify_open_task_report_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.opentasksreport_header_is_displayed()


@when('the user clicks on Insights > Drivers Report')
def click_driver_report():
    FLEET_TELEMATICS_PAGE.click_drivers_report_submenu()


@then('the user should see page header Drivers Report with drivers count')
def verify_driver_report_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.driversreport_header_is_displayed()


@when('the user clicks on Insights > Group Report')
def click_group_report():
    FLEET_TELEMATICS_PAGE.click_group_report_submenu()


@then('the user should see page header Group Report with subgroups count')
def verify_group_report_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.groupreport_header_is_displayed()


@when('the user clicks on Insights > Coaches Report')
def click_coaches_report():
    FLEET_TELEMATICS_PAGE.click_coaches_report_submenu()


@then('the user should see page header Coaches Report with coaches count')
def verify_coaches_report_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.coachesreport_header_is_displayed()


@when('the user clicks on Insights > Program Status Report')
def click_program_status_report():
    FLEET_TELEMATICS_PAGE.click_program_status_report_submenu()


@then('the user should see page header Program Status Report with subgroups count')
def verify_program_status_report_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.programstatusreport_header_is_displayed()


@when('the user clicks on Insights > Behaviors Report')
def click_behaviors_report():
    FLEET_TELEMATICS_PAGE.click_behaviors_report_submenu()


@then('the user should see page header Behaviors Report with Behaviors count')
def verify_behaviors_report_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.behaviorsreport_header_is_displayed()


@when('the user clicks on Library > Events')
def click_library_events():
    FLEET_TELEMATICS_PAGE.click_library_menu()
    FLEET_TELEMATICS_PAGE.click_events_submenu()


@then('the user should see page header Library with events count')
def verify_library_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.events_header_is_displayed()


@when('the user clicks on Library > Coaching History')
def click_coaching_history():
    FLEET_TELEMATICS_PAGE.click_coachinghistory_submenu()


@then('the user should see page header Coaching History with sessions count')
def verify_coaching_history_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.coachinghistory_header_is_displayed()


@when('the user clicks on Library > Recognition History')
def click_recognition_history():
    FLEET_TELEMATICS_PAGE.click_recognitionhistory_submenu()


@then('the user should see page header Recognition History with recognitions count')
def verify_recognition_history_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.recognitionhistory_header_is_displayed()


@when('the user clicks on Library > Data Export')
def click_data_export():
    FLEET_TELEMATICS_PAGE.click_dataexport_submenu()


@then('the user should see page header Data Export')
def verify_data_export_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.dataexport_header_is_displayed()


@when('the user clicks on Search menu')
def click_on_search_menu():
    FLEET_TELEMATICS_PAGE.click_search_submenu()


@then('the user should see Search by event ID text box')
def verify_event_id_textbox():
    assert FLEET_TELEMATICS_CENTER_PAGE.search_textbox_is_displayed()


@when('the user clicks on video search')
def login_to_video_search():
    DASHBOARD_PAGE.click_video_search_tab()


@then(
    'the user is successfully in the Video Search page. The vehicle count is displayed and the table is displayed with columns: "ACTIONS", "VEHICLES", "DEVICE", "LAST COMMUNICATED", "GROUP", "VIEWS"')
def verify_video_search_tabs():
    assert_that(VIDEO_SEARCH_PAGE.get_video_search_title(), IsEqualIgnoringCase("Video Search"))
    assert FLEET_TELEMATICS_CENTER_PAGE.vehicles_header_is_displayed()
    assert VIDEO_SEARCH_PAGE.video_tag_count_is_displayed()
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag()
    assert VIDEO_SEARCH_PAGE.get_actions_column_text() == "ACTIONS"
    assert VIDEO_SEARCH_PAGE.get_vehicles_column_text() == "VEHICLES"
    assert VIDEO_SEARCH_PAGE.get_device_column_text() == "DEVICE"
    assert VIDEO_SEARCH_PAGE.get_last_communicated_column_text() == "LAST COMMUNICATED"
    assert VIDEO_SEARCH_PAGE.get_group_column_text() == "GROUP"
    assert VIDEO_SEARCH_PAGE.get_views_column_text() == "VIEWS"


@when('the user clicks on Video Search > Map Search menu')
def navigate_to_map_search_page():
    FLEET_TELEMATICS_PAGE.click_map_search_menu()


@then('the user should see page header Map Search with vehicles count')
def verify_map_search_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.map_search_header_is_displayed()


@when('the user clicks on Video Search > Library > Saved Videos')
def navigate_to_verify_saved_videos_page():
    FLEET_TELEMATICS_PAGE.click_vs_library_menu()
    FLEET_TELEMATICS_PAGE.click_saved_videos_submenu()


@then('the user should see page header Saved Videos with vehicles count')
def verify_saved_videos_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.saved_videos_header_is_displayed()


@when('the user clicks on Video Search > Library > Video Tags')
def navigate_to_video_tags_page():
    FLEET_TELEMATICS_PAGE.click_video_tags_submenu()


@then('the user should see page header Video Tags with video tags count')
def verify_video_tags_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.video_tags_header_is_displayed()


@when('the user clicks on Admin tab')
def navigate_to_user_management_page():
    DASHBOARD_PAGE.click_admin_tab()


@then(
    'the page header "USER MANAGEMENT" is displayed and the user count are displayed and the table is displayed with columns: "NAME", "EMPLOYEE ID", "LYTX BADGE", "PRIMARY DRIVER GROUP", "ROLES (GROUP)", "STATUS", "LOGIN", "USERNAME"')
def verify_user_management_tabs():
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert FLEET_TELEMATICS_CENTER_PAGE.users_header_is_displayed()
    assert USER_MANAGEMENT_PAGE.user_management_label_is_displayed()
    assert USER_MANAGEMENT_PAGE.get_user_management_label() == "USER MANAGEMENT"
    assert USER_MANAGEMENT_PAGE.get_name_label() == "NAME"
    assert USER_MANAGEMENT_PAGE.get_employee_id_label() == "EMPLOYEE ID"
    assert USER_MANAGEMENT_PAGE.get_roles_label() == "ROLES (GROUP)"
    assert USER_MANAGEMENT_PAGE.get_status_label() == "STATUS"
    assert USER_MANAGEMENT_PAGE.get_login_label() == "LOGIN"
    assert USER_MANAGEMENT_PAGE.get_user_name_label() == "USERNAME"


@when('the user clicks on Admin > Vehicles menu')
def navigate_to_vehicles_page():
    FLEET_TELEMATICS_PAGE.click_admin_vehicles_menu()


@then('the user should see page header Vehicles with vehicles count')
def verify_vehicles_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.admin_vehicles_header_is_displayed()


# LQ-148199
@when('the user clicks on Admin > Telematics Assets menu')
def navigate_to_assets_page():
    FLEET_TELEMATICS_PAGE.click_telematics_assets_menu()
    FLEET_TELEMATICS_PAGE.wait_for_page_to_fully_load()


@then('the user should see page header Assets, assets tab, cameras tab, and all required UI fields')
def verify_assets_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.asset_header_is_displayed()
    assert FLEET_TELEMATICS_CENTER_PAGE.search_bar_displayed()
    assert FLEET_TELEMATICS_CENTER_PAGE.asset_reports_button_is_displayed()
    assert FLEET_TELEMATICS_CENTER_PAGE.telematics_cameras_tab_is_displayed()
    assert FLEET_TELEMATICS_CENTER_PAGE.telematics_assets_tab_is_displayed()


# LQ-119298
@when('the user clicks Admin - Telematics Assets - Linked Assets')
def navigate_to_linkedAssets():
    FLEET_TELEMATICS_CENTER_PAGE.click_linkedassets_title()


@then('the user should be navigated to the "Linked Assets" page')
def verify_linkedassets_header():
    assert FLEET_TELEMATICS_CENTER_PAGE.linkedassets_header_is_displayed()
    assert FLEET_TELEMATICS_CENTER_PAGE.zt_search_name_comment_is_displayed()
    assert FLEET_TELEMATICS_CENTER_PAGE.linkedassets_groups_is_displayed()
    assert FLEET_TELEMATICS_CENTER_PAGE.linkedassets_primary_asset_is_displayed()
    assert FLEET_TELEMATICS_CENTER_PAGE.linkedassets_linked_asset_is_displayed()


@when('the user clicks on Admin > Device menu')
def navigate_to_device_management_page():
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)
    FLEET_TELEMATICS_PAGE.click_devices_menu()


@then('the user should see page header Device Management with device count')
def verify_device_management_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.devices_header_is_displayed()


@when('the user clicks on Admin > Geofence menu')
def navigate_to_geofence_management_page():
    FLEET_TELEMATICS_PAGE.click_geofences_menu()


@then('the user should see page header Geofence Management with device count')
def verify_geofence_management_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.geofences_header_is_displayed()


@when('the user clicks on Admin > Insights menu > Driver ID Assignment submenu')
def navigate_to_driver_id_assignment_page():
    FLEET_TELEMATICS_PAGE.click_admin_insights_menu()
    FLEET_TELEMATICS_PAGE.click_insights_driver_id_menu()


@then('the user should see page header Driver ID Assignment with trips count')
def verify_driver_id_assignment_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.admin_insights_driver_id_header_is_displayed()


@when('the user clicks on Admin > Config Settings menu')
def navigate_to_config_settings():
    FLEET_TELEMATICS_PAGE.click_config_settings_menu()


@then('the user should see page header Configuration Settings')
def verify_config_setting_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.config_settings_header_is_displayed()


# LQ-136400
@when('the user clicks on Config Settings menu > Safe Driving Report')
def navigate_to_safe_driving_report():
    FLEET_TELEMATICS_PAGE.click_config_settings_menu()
    FLEET_TELEMATICS_CENTER_PAGE.click_safe_driving_report_tab()


@then(
    'the user should see page setting, groups and minimum distance driven table headers with only edit icon for root group and edit, delete icons for all other groups')
def verify_safe_driving_report_page():
    assert_that(FLEET_TELEMATICS_CENTER_PAGE.get_setting_header_text(), IsEqualIgnoringCase("SETTING"))
    assert_that(FLEET_TELEMATICS_CENTER_PAGE.get_group_header_text(), IsEqualIgnoringCase("GROUP"))
    assert_that(FLEET_TELEMATICS_CENTER_PAGE.get_minimum_distance_driven_header_text(),
                IsEqualIgnoringCase("MINIMUM DISTANCE DRIVEN"))
    assert FLEET_TELEMATICS_CENTER_PAGE.edit_icon_is_displayed()
    assert FLEET_TELEMATICS_CENTER_PAGE.invisible_delete_icon_only_root_group_is_displayed()
    assert FLEET_TELEMATICS_CENTER_PAGE.delete_icon_is_displayed()


# LQ-172939
@given('the "Administrator" user is in NEW UI HOS Application')
def verify_user_in_hos_application(browser):
    LOGIN_PAGE.click_profile_btn()
    LOGIN_PAGE.click_sign_out_button_newui()
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(FTD.admin_username)
    LOGIN_PAGE.enter_password(FTD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_multi_company(FTD.admin_company_name)
    LOGIN_PAGE.click_select_company_button()
    DASHBOARD_PAGE.wait_for_page_to_fully_load()
    DASHBOARD_PAGE.click_hos_tab()
    DASHBOARD_PAGE.wait_for_page_to_fully_load()


@when('the user clicks the refresh button in the browser')
def refresh_hos_page():
    DASHBOARD_PAGE.click_refresh_button()
    DASHBOARD_PAGE.wait_for_page_to_fully_load()


@then(
    'the user should be able to see the HOS application and when user click on other app "fleet telematics" and click on back button then user should come back to HOS application')
def verify_hos_application_with_refresh_and_back():
    DASHBOARD_PAGE.scroll_page_up()
    DASHBOARD_PAGE.switch_ft_iframe_eld()
    assert GEOTAB_PAGE.dashboard_is_displayed() is True
    hos_url = DASHBOARD_PAGE.get_current_url()
    DASHBOARD_PAGE.click_driver_safety_tab()
    DASHBOARD_PAGE.wait_for_page_to_fully_load()
    DASHBOARD_PAGE.back_to_previous_page()
    DASHBOARD_PAGE.wait_for_page_to_fully_load()
    DASHBOARD_PAGE.switch_ft_iframe_eld()
    DASHBOARD_PAGE.scroll_page_up()
    assert GEOTAB_PAGE.dashboard_is_displayed() is True
    assert DASHBOARD_PAGE.get_current_url() == hos_url


# LQ-108840
@when('the user clicks Fleet Telematics tab')
def navigate_to_fleet_telematics(browser):
    LOGIN_PAGE.click_profile_btn()
    LOGIN_PAGE.click_sign_out_button_newui()
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.enter_username(FTD.username)
    LOGIN_PAGE.enter_password(FTD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_multi_company(FTD.company_name)
    LOGIN_PAGE.click_select_company_button()
    LOGIN_PAGE.wait_for_page_load()
    DASHBOARD_PAGE.click_fleet_telematics_tab()


@then('the Fleet Telematics main page is loaded successfully')
def verify_user_on_fleet_telematics():
    FLEET_TELEMATICS_PAGE.switch_ft_iframe()
    assert FLEET_TELEMATICS_PAGE.more_charts_button_is_displayed()
    FLEET_TELEMATICS_PAGE.switch_to_first_tab(0)


# LQ-110640
@then('the user should be able to see the left navigation in expand mode by default.')
def verify_left_navigation_in_expand_mode():
    assert FLEET_TELEMATICS_PAGE.left_navigation_expand_mode_is_displayed()


@when('the user clicks the left arrow symbol present in the left navigation bar.')
def click_arrow_to_left():
    FLEET_TELEMATICS_PAGE.click_arrow_left_direction()


@then(
    'the user should see the left navigation bar getting collapsed and the user should see the arrow symbol facing towards right side once it gets collapsed.')
def verify_left_navigation_in_collapse_mode():
    assert FLEET_TELEMATICS_PAGE.left_navigation_collapse_mode_is_displayed()
    assert FLEET_TELEMATICS_PAGE.arrow_right_direction_displayed()
    assert DASHBOARD_PAGE.lytx_logo_is_displayed() is False
    FLEET_TELEMATICS_PAGE.click_arrow_left_direction()


@then(
    'the user should see the tabs in the left Navigation bar such as Dashboard, Map, Productivity, Compliance, Maintenance, Sustainability, Reports, Rules & Exceptions, Messages & Notifications')
def verify_all_menus():
    assert FLEET_TELEMATICS_PAGE.dashboard_menu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.map_menu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.productivity_menu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.compliance_menu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.maintenance_menu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.sustainability_menu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.reports_menu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.rulesandexceptions_menu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.messages_menu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.notifications_menu_is_displayed()


# LQ-110112
@when('the user clicks refresh icon in the browser')
def refresh_page():
    FLEET_TELEMATICS_PAGE.click_refresh_button()
    FLEET_TELEMATICS_PAGE.wait_for_page_to_fully_load()


@then(
    'the user should see the page getting refreshed and landed to fleet telematics application, click on any menu and the user click back button in the browser and the user should go to the previous page where the user was.')
def verify_user_on_fleet_telematics():
    assert FLEET_TELEMATICS_PAGE.dashboard_menu_is_displayed()
    dashboard_url = FLEET_TELEMATICS_PAGE.get_current_url()
    FLEET_TELEMATICS_PAGE.click_map_menu()
    FLEET_TELEMATICS_PAGE.wait_for_page_to_fully_load()
    FLEET_TELEMATICS_PAGE.back()
    assert FLEET_TELEMATICS_PAGE.get_current_url() == dashboard_url


# LQ-110714
@when('the user clicks the dropdown icon present next to "Productivity" menu')
def click_productivity_menu_dropdown():
    FLEET_TELEMATICS_PAGE.click_productivity_menu_dropdown()


@then(
    'the user should see the sub-menus such as Trip History, Routes, Zones, Driver Congregation, Asset Location Sharing, Linked Assets & Risk Management')
def verify_productivity_sub_menus():
    assert FLEET_TELEMATICS_PAGE.trip_history_submenu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.routes_submenu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.zones_submenu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.drivercongregation_submenu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.assetlocationsharing_submenu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.riskmanagement_submenu_is_displayed()


@when('the user clicks the dropdown icon present left to "Routes" menu')
def click_routes_dropdown():
    FLEET_TELEMATICS_PAGE.click_routes_submenu_dropdown()


@then(
    'the user should see the child menus of Routes such as Planned vs Actual, Route Summary, Unmatched Route, Import Routes with a vertical line.')
def verify_routes_child_menus():
    assert FLEET_TELEMATICS_PAGE.plannedvsactualroutes_subchild_is_displayed()
    assert FLEET_TELEMATICS_PAGE.routesummary_subchild_is_displayed()
    assert FLEET_TELEMATICS_PAGE.unmatchedroute_subchild_is_displayed()
    assert FLEET_TELEMATICS_PAGE.importroutes_subchild_is_displayed()


@when('the user clicks the dropdown icon present left to "Zones" menu')
def click_zones_menu_dropdown():
    FLEET_TELEMATICS_PAGE.click_zones_submenu_dropdown()


@then(
    'the user should see the child menus of Zones such as Zones, Zone Visits, Zone Types & Import Zones with a vertical line.')
def verify_zones_child_menus():
    assert FLEET_TELEMATICS_PAGE.zones_subchild_is_displayed()
    assert FLEET_TELEMATICS_PAGE.zonevisits_subchild_is_displayed()
    assert FLEET_TELEMATICS_PAGE.zonetypes_subchild_is_displayed()
    assert FLEET_TELEMATICS_PAGE.importzones_subchild_is_displayed()


# LQ-110742
@when('the user clicks the dropdown icon present next to "Compliance" menu')
def click_compliance_menu_dropdown():
    # Click productivity to close the dropdown and click compliance dropdown
    FLEET_TELEMATICS_PAGE.click_productivity_menu()
    FLEET_TELEMATICS_PAGE.click_compliance_menu_dropdown()


@then(
    'the user should see the sub-menus HOS, Time Card Report, IFTA Report & Clean Truck Check')
def verify_compliance_sub_menus():
    assert FLEET_TELEMATICS_PAGE.hos_submenu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.timecardreport_submenu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.iftareport_submenu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.cleantruckcheck_submenu_is_displayed()


@when('the user clicks the dropdown icon present left to "HOS" menu')
def click_hos_dropdown():
    FLEET_TELEMATICS_PAGE.click_hos_submenu_dropdown()


@then(
    'the user should see the child menus of HOS such as Logs, Unidentified Driving, Violations & Availability with a vertical line.')
def verify_hos_child_menus():
    assert FLEET_TELEMATICS_PAGE.logs_is_displayed()
    assert FLEET_TELEMATICS_PAGE.unidentified_driving_subchild_is_displayed()
    assert FLEET_TELEMATICS_PAGE.violations_subchild_is_displayed()
    assert FLEET_TELEMATICS_PAGE.availability_subchild_is_displayed()


@when('the user clicks the dropdown icon present next to "Maintenance" menu')
def click_maintenance_menu_dropdown():
    FLEET_TELEMATICS_PAGE.click_maintenance_menu_dropdown()


@then('the user should see the sub-menus Work Orders, Schedules, Asset Inspection, Faults & Measurements')
def verify_maintenance_sub_menus():
    assert FLEET_TELEMATICS_PAGE.work_order_sub_child_is_displayed()
    assert FLEET_TELEMATICS_PAGE.schedules_sub_child_is_displayed()
    assert FLEET_TELEMATICS_PAGE.assetinspection_submenu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.faults_subchild_xpath_is_displayed()
    assert FLEET_TELEMATICS_PAGE.measurements_subchild_is_displayed()


# LQ-111061
@when('the user clicks the dropdown icon present next to "Sustainability" menu')
def click_sustainability_dropdown():
    FLEET_TELEMATICS_PAGE.click_sustainability_menu_dropdown()


@then(
    'the user should see the sub-menus such as Sustainability Overview, Fuel & Energy Usage, EV Battery Health, EV Charging History & BEV Range Capability')
def verify_sustainability_sub_menus():
    assert FLEET_TELEMATICS_PAGE.sustainabilityoverview_submenu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.fuel_energy_usage_submenu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.evcharginghistory_submenu_is_displayed()


@when('the user clicks the dropdown icon present next to "Reports" menu')
def click_reports_menu_dropdown():
    # Click sustainability to close the dropdown and click reports dropdown
    FLEET_TELEMATICS_PAGE.click_sustainability_menu()
    FLEET_TELEMATICS_PAGE.click_reports_menu_dropdown()


@then(
    'the user should see the sub-menus such as My Reports & Report Setup')
def verify_reports_child_menus():
    assert FLEET_TELEMATICS_PAGE.myreports_submenu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.reportsetup_submenu_is_displayed()


@when('the user clicks the dropdown icon present next to "Rules & Exceptions" menu')
def click_rules_and_exceptions_menu_dropdown():
    FLEET_TELEMATICS_PAGE.click_rulesandexceptions_menu_dropdown()


@then(
    'the user should see the "Rules" and "Exceptions" sub-menus')
def verify_rules_and_exceptions_child_menus():
    assert FLEET_TELEMATICS_PAGE.rules_submenu_is_displayed()
    assert FLEET_TELEMATICS_PAGE.exceptions_submenu_is_displayed()


@when('the user scrolls to the bottom of left panel')
def scroll_down_left_panel():
    FLEET_TELEMATICS_PAGE.scroll_page_down()


@then('the Addins menu should be present')
def verify_addins_menu():
    assert FLEET_TELEMATICS_PAGE.addins_menu_is_displayed()