from hamcrest import assert_that, contains_string
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then
from data.prod.fleet_telematics_prod import FleetTelematicsDataProd as FTD_PROD
from data.stg.fleet_telematics_stg import FleetTelematicsDataStg as FTD_STG
from data.int.fleet_telematics_int import FleetTelematicsDataInt as FTD_INT
from pages.dashboard_page import DashboardPage
from pages.fleet_telematics_center_page import FleetTelematicsCenterPage
from pages.fleet_telematics_left_panel_page import FleetTelematicsPageLeftPanel
from pages.fleet_telematics_left_panel_page_old_ui import FleetTelematicsPageLeftPanelOldUI
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage
from pages.video_search_page import VideoSearchPage
from steps.common import DC_URL
from steps.common import ENV

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
BASE_PAGE = 0
FLEET_TELEMATICS_PAGE = 0
FLEET_TELEMATICS_CENTER_PAGE = 0
VIDEO_SEARCH_PAGE = 0
FTD = 0
USER_MANAGEMENT_PAGE = 0
FLEET_TELEMATICS_PAGE_OLD_UI = 0

scenarios('../features/sanity_fleet_telematics_left_panel_old_ui.feature')


# LQ-306
@given('the login page is displayed in the browser')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, FTD, FLEET_TELEMATICS_PAGE, VIDEO_SEARCH_PAGE, USER_MANAGEMENT_PAGE, FLEET_TELEMATICS_CENTER_PAGE, FLEET_TELEMATICS_PAGE_OLD_UI

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    FLEET_TELEMATICS_PAGE = FleetTelematicsPageLeftPanel(browser)
    VIDEO_SEARCH_PAGE = VideoSearchPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)
    FLEET_TELEMATICS_CENTER_PAGE = FleetTelematicsCenterPage(browser)
    FLEET_TELEMATICS_PAGE_OLD_UI = FleetTelematicsPageLeftPanelOldUI(browser)

    browser.get(DC_URL)

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
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))
    assert DASHBOARD_PAGE.no_of_unassigned_drivers_is_displayed() is True
    assert DASHBOARD_PAGE.get_unassigned_drivers_text() == "UNASSIGNED DRIVERS"
    assert_that(DASHBOARD_PAGE.get_unassigned_drivers_text(), contains_string("UNASSIGNED DRIVER"))
    assert DASHBOARD_PAGE.get_due_for_coaching_text() == "DUE FOR COACHING"
    assert DASHBOARD_PAGE.get_fyi_notify_text() == "FYI NOTIFY"
    assert_that(DASHBOARD_PAGE.get_collisions_text(), contains_string('COLLISION'))
    assert_that(DASHBOARD_PAGE.get_possible_collisions_text(), contains_string("POSSIBLE COLLISION"))
    # Validate all dashboard details links contain the expected label
    for _name, link_text in DASHBOARD_PAGE.get_all_dashboard_details_links().items():
        assert_that(link_text, contains_string("View Details"))


@when('the user clicks on Tasks > Due For Coaching')
def click_due_for_coaching():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_coaching()


@then('the user should see page header Due For Coaching with tasks count')
def verify_due_for_coaching_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.due_for_coaching_header_is_displayed() is True


@when('the user clicks on Tasks > Assign Drivers')
def click_assign_drivers():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_assign_driver_tab()


@then('the user should see page header Assign Drivers with tasks count')
def verify_assign_drivers_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.assign_driver_header_is_displayed() is True


@when('the user clicks on Tasks > Collision')
def click_collision():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_collisions_tab()


@then('the user should see page header Collision with tasks count')
def verify_collision_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.collisions_header_is_displayed() is True


@when('the user clicks on Tasks > FYI Notify')
def click_fyi_notify():
    DASHBOARD_PAGE.click_tasks()
    DASHBOARD_PAGE.click_fyi_notify_tab()


@then('the user should see page header FYI Notify with tasks count')
def verify_fyi_notify_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.fyinotify_header_is_displayed() is True


@when('the user clicks on Insights > Open Tasks Report')
def click_open_task_report():
    DASHBOARD_PAGE.click_insights_tab()
    DASHBOARD_PAGE.click_open_tasks_report_tab()

@then('the user should see page header Open Tasks Report with drivers count')
def verify_open_task_report_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.opentasksreport_header_is_displayed() is True


@when('the user clicks on Insights > Drivers Report')
def click_driver_report():
    DASHBOARD_PAGE.click_insights_tab()
    DASHBOARD_PAGE.click_drivers_report_tab()


@then('the user should see page header Drivers Report with drivers count')
def verify_driver_report_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.driversreport_header_is_displayed() is True


@when('the user clicks on Insights > Group Report')
def click_group_report():
    DASHBOARD_PAGE.click_insights_tab()
    DASHBOARD_PAGE.click_group_report_tab()


@then('the user should see page header Group Report with subgroups count')
def verify_group_report_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.groupreport_header_is_displayed() is True


@when('the user clicks on Insights > Coaches Report')
def click_coaches_report():
    DASHBOARD_PAGE.click_insights_tab()
    DASHBOARD_PAGE.click_coaches_report_tab()


@then('the user should see page header Coaches Report with coaches count')
def verify_coaches_report_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.coachesreport_header_is_displayed() is True


@when('the user clicks on Insights > Program Status Report')
def click_program_status_report():
    DASHBOARD_PAGE.click_insights_tab()
    DASHBOARD_PAGE.click_program_status_report_tab()


@then('the user should see page header Program Status Report with subgroups count')
def verify_program_status_report_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.programstatusreport_header_is_displayed() is True


@when('the user clicks on Insights > Behaviors Report')
def click_behaviors_report():
    DASHBOARD_PAGE.click_insights_tab()
    DASHBOARD_PAGE.click_behaviors_report_tab()


@then('the user should see page header Behaviors Report with Behaviors count')
def verify_behaviors_report_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.behaviorsreport_header_is_displayed() is True


@when('the user clicks on Library > Events')
def click_library_events():
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_events()


@then('the user should see page header Library with events count')
def verify_library_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.events_header_is_displayed() is True


@when('the user clicks on Library > Coaching History')
def click_coaching_history():
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_coaching_history()


@then('the user should see page header Coaching History with sessions count')
def verify_coaching_history_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.coachinghistory_header_is_displayed() is True


@when('the user clicks on Library > Recognition History')
def click_recognition_history():
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_recognition_history()

@then('the user should see page header Recognition History with recognitions count')
def verify_recognition_history_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.recognitionhistory_header_is_displayed() is True


@when('the user clicks on Library > Data Export')
def click_data_export():
    DASHBOARD_PAGE.click_library_tab()
    DASHBOARD_PAGE.click_data_export()

@then('the user should see page header Data Export')
def verify_data_export_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.dataexport_header_is_displayed() is True


@when('the user clicks on Search menu')
def click_on_search_menu():
    FLEET_TELEMATICS_PAGE_OLD_UI.click_search_submenu_old_ui()


@then('the user should see Search by event ID text box')
def verify_event_id_textbox():
    assert FLEET_TELEMATICS_CENTER_PAGE.search_textbox_is_displayed() is True


@when('the user clicks on video search')
def login_to_video_search():
    DASHBOARD_PAGE.click_video_search_tab()


@then('the user should see the Video Search main page is loaded successfully with all elements')
def verify_video_search_tabs():
    assert_that(VIDEO_SEARCH_PAGE.get_video_search_title(), IsEqualIgnoringCase("Video Search"))
    assert FLEET_TELEMATICS_CENTER_PAGE.vehicles_header_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.video_tag_count_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True
    assert VIDEO_SEARCH_PAGE.get_actions_column_text() == "ACTIONS"
    assert VIDEO_SEARCH_PAGE.get_vehicles_column_text() == "VEHICLES"
    assert VIDEO_SEARCH_PAGE.get_device_column_text() == "DEVICE"
    assert VIDEO_SEARCH_PAGE.get_last_communicated_column_text() == "LAST COMMUNICATED"
    assert VIDEO_SEARCH_PAGE.get_group_column_text() == "GROUP"
    assert VIDEO_SEARCH_PAGE.get_views_column_text() == "VIEWS"


@when('the user clicks on Video Search > Map Search menu')
def navigate_to_map_search_page():
    VIDEO_SEARCH_PAGE.click_map_search_tab()


@then('the user should see page header Map Search with vehicles count')
def verify_map_search_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.map_search_header_is_displayed() is True


@when('the user clicks on Video Search > Library > Saved Videos')
def navigate_to_verify_saved_videos_page():
    VIDEO_SEARCH_PAGE.click_library_tab()
    VIDEO_SEARCH_PAGE.click_saved_videos_tab()


@then('the user should see page header Saved Videos with vehicles count')
def verify_saved_videos_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.saved_videos_header_is_displayed() is True


@when('the user clicks on Video Search > Library > Video Tags')
def navigate_to_video_tags_page():
    VIDEO_SEARCH_PAGE.click_library_tab()
    VIDEO_SEARCH_PAGE.click_video_tags_tab()


@then('the user should see page header Video Tags with video tags count')
def verify_video_tags_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.video_tags_header_is_displayed() is True


@when('the user clicks on Admin tab')
def navigate_to_user_management_page():
    DASHBOARD_PAGE.click_admin_tab()


@then(
    'the page header "USER MANAGEMENT" is displayed and the user count are displayed and the table is displayed with columns: "NAME", "EMPLOYEE ID", "LYTX BADGE", "PRIMARY DRIVER GROUP", "ROLES (GROUP)", "STATUS", "LOGIN", "USERNAME"')
def verify_user_management_tabs():
    assert_that(DASHBOARD_PAGE.get_admin_title(), IsEqualIgnoringCase("Admin"))
    assert FLEET_TELEMATICS_CENTER_PAGE.users_header_is_displayed() is True
    assert USER_MANAGEMENT_PAGE.user_management_label_is_displayed() is True
    assert USER_MANAGEMENT_PAGE.get_user_management_label() == "USER MANAGEMENT"
    assert USER_MANAGEMENT_PAGE.get_name_label() == "NAME"
    assert USER_MANAGEMENT_PAGE.get_employee_id_label() == "EMPLOYEE ID"
    assert USER_MANAGEMENT_PAGE.get_roles_label() == "ROLES (GROUP)"
    assert USER_MANAGEMENT_PAGE.get_status_label() == "STATUS"
    assert USER_MANAGEMENT_PAGE.get_login_label() == "LOGIN"
    assert USER_MANAGEMENT_PAGE.get_user_name_label() == "USERNAME"


@when('the user clicks on Admin > Vehicles menu')
def navigate_to_vehicles_page():
    USER_MANAGEMENT_PAGE.click_vehicle_tab()


@then('the user should see page header Vehicles with vehicles count')
def verify_vehicles_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.admin_vehicles_header_is_displayed() is True


# LQ-148199
@when('the user clicks on Admin > Telematics Assets menu')
def navigate_to_assets_page():
    FLEET_TELEMATICS_PAGE_OLD_UI.click_telematics_assets_menu_old_ui()
    FLEET_TELEMATICS_PAGE_OLD_UI.wait_for_page_to_fully_load()


@then('the user should see page header Assets, assets tab, cameras tab, and all required UI fields')
def verify_assets_page():
    FLEET_TELEMATICS_PAGE_OLD_UI.wait_for_page_to_fully_load()
    assert FLEET_TELEMATICS_CENTER_PAGE.search_bar_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.asset_reports_button_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.telematics_cameras_tab_is_displayed() is True
    assert FLEET_TELEMATICS_CENTER_PAGE.telematics_assets_tab_is_displayed() is True


@when('the user clicks on Admin > Device menu')
def navigate_to_device_management_page():
    USER_MANAGEMENT_PAGE.click_devices_tab()


@then('the user should see page header Device Management with device count')
def verify_device_management_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.devices_header_is_displayed() is True


@when('the user clicks on Admin > Geofence menu')
def navigate_to_geofence_management_page():
    USER_MANAGEMENT_PAGE.click_geofences_tab()


@then('the user should see page header Geofence Management with device count')
def verify_geofence_management_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.geofences_header_is_displayed() is True


@when('the user clicks on Admin > Insights menu > Driver ID Assignment submenu')
def navigate_to_driver_id_assignment_page():
    USER_MANAGEMENT_PAGE.click_insights_tab()
    USER_MANAGEMENT_PAGE.click_driver_id_assignment_tab()


@then('the user should see page header Driver ID Assignment with trips count')
def verify_driver_id_assignment_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.admin_insights_driver_id_header_is_displayed() is True


@when('the user clicks on Admin > Config Settings menu')
def navigate_to_config_settings():
    USER_MANAGEMENT_PAGE.click_config_setting_tab()


@then('the user should see page header Configuration Settings')
def verify_config_setting_page():
    assert FLEET_TELEMATICS_CENTER_PAGE.config_settings_header_is_displayed() is True


# LQ-108840
@when('the user clicks Fleet Telematics tab')
def navigate_to_fleet_telematics():
    DASHBOARD_PAGE.click_fleet_telematics_tab()


@then('the Fleet Telematics main page is loaded successfully')
def verify_user_on_fleet_telematics():
    FLEET_TELEMATICS_PAGE_OLD_UI.switch_ft_iframe()
    assert FLEET_TELEMATICS_PAGE_OLD_UI.more_charts_button_is_displayed() is True
    FLEET_TELEMATICS_PAGE_OLD_UI.switch_to_first_tab(0)


@then('the user should see the tabs in the left Navigation bar such as Dashboard, Map, Productivity, Compliance, Maintenance, Sustainability, Reports, Rules & Exceptions, Messages & Notifications')
def verify_all_menus():
    assert FLEET_TELEMATICS_PAGE_OLD_UI.dashboard_menu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.map_menu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.productivity_menu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.compliance_menu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.maintenance_menu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.sustainability_menu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.reports_menu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.rulesandexceptions_menu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.messages_menu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.notifications_menu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.addins_menu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.marketplace_menu_is_displayed() is True


# LQ-110112
@when('the user clicks map menu')
def refresh_page():
    FLEET_TELEMATICS_PAGE_OLD_UI.click_map_menu()


@then(
    'the user should see the Map page is loaded successfully with all elements')
def verify_user_on_fleet_telematics():
    assert FLEET_TELEMATICS_PAGE_OLD_UI.map_menu_is_displayed() is True


# LQ-110714
@when('the user clicks "Productivity" menu')
def click_productivity_menu_dropdown():
    FLEET_TELEMATICS_PAGE_OLD_UI.click_productivity_menu()


@then(
    'the user should see the sub-menus such as Trip History, Routes, Public Works, Zones, Driver Congregation, Asset Location Sharing, Linked Assets & Risk Management')
def verify_productivity_sub_menus():
    assert FLEET_TELEMATICS_PAGE_OLD_UI.trip_history_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.routes_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.plannedvsactualroutes_subchild_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.routesummary_subchild_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.unmatchedroute_subchild_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.importroutes_subchild_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.routecompletion_subchild_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.materialmanagement_subchild_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.zones_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.zonevisits_subchild_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.zonetypes_subchild_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.importzones_subchild_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.drivercongregation_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.assetlocationsharing_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.linkedassets_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.riskmanagement_submenu_is_displayed() is True


# LQ-110742
@when('the user clicks the "Compliance" menu')
def click_compliance_menu_dropdown():
    FLEET_TELEMATICS_PAGE_OLD_UI.click_compliance_menu()


@then('the user should see the sub-menus HOS, Time Card Report, IFTA Report & Clean Truck Check etc')
def verify_compliance_sub_menus():
    assert FLEET_TELEMATICS_PAGE_OLD_UI.hos_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.unidentified_driving_subchild_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.violations_subchild_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.availability_subchild_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.timecardreport_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.iftareport_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.cleantruckcheck_submenu_is_displayed() is True


@when('the user clicks the dropdown icon present next to "Maintenance" menu')
def click_maintenance_menu_dropdown():
    FLEET_TELEMATICS_PAGE_OLD_UI.click_maintenance_menu()


@then(
    'the user should see the sub-menus Asset Inspection, Diagnostics & Maintenance Center')
def verify_maintenance_sub_menus():
    assert FLEET_TELEMATICS_PAGE_OLD_UI.assetinspection_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.faults_subchild_xpath_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.diagnostics_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.work_order_sub_child_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.schedules_sub_child_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.speed_profile_subchild_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.log_data_and_collisions_subchild_is_displayed() is True

# LQ-111061
@when('the user clicks the dropdown icon present next to "Sustainability" menu')
def click_sustainability_dropdown():
    FLEET_TELEMATICS_PAGE_OLD_UI.click_sustainability_menu()


@then(
    'the user should see the sub-menus such as Sustainability Center, Fuel & Energy Usage, EV Battery Health, EV Charging History & BEV Range Capability')
def verify_sustainability_sub_menus():
    assert FLEET_TELEMATICS_PAGE_OLD_UI.sustainabilitycenter_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.fuel_energy_usage_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.evbatteryhealth_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.evcharginghistory_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.bevrangecapability_submenu_is_displayed() is True


@when('the user clicks "Insights" menu')
def click_reports_menu_dropdown():
    FLEET_TELEMATICS_PAGE_OLD_UI.click_reports_menu_dropdown()


@then(
    'the user should see the sub-menus such as My Reports & Report Setup')
def verify_reports_child_menus():
    assert FLEET_TELEMATICS_PAGE_OLD_UI.myreports_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.reportsetup_submenu_is_displayed() is True


@when('the user clicks to "Rules & Exceptions" menu')
def click_rules_and_exceptions_menu_dropdown():
    FLEET_TELEMATICS_PAGE_OLD_UI.click_rulesandexceptions_menu()


@then(
    'the user should see the "Rules" and "Exceptions" sub-menus')
def verify_rules_and_exceptions_child_menus():
    assert FLEET_TELEMATICS_PAGE_OLD_UI.rules_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.exceptions_submenu_is_displayed() is True


@when('the user clicks to "Config" menu')
def click_config_menu_dropdown():
    FLEET_TELEMATICS_PAGE_OLD_UI.click_config_menu()


@then('the user should see the "Settings", "Work Hours", "Holidays", "Audit log" sub-menus')
def verify_config_child_menus():
    assert FLEET_TELEMATICS_PAGE_OLD_UI.settings_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.work_hours_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.holidays_submenu_is_displayed() is True
    assert FLEET_TELEMATICS_PAGE_OLD_UI.audit_log_submenu_is_displayed() is True
