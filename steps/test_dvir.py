from time import sleep

from hamcrest import assert_that, contains_string
from pytest_bdd import scenarios, given, when, then

from pages.dashboard_page import DashboardPage
from pages.driver_vehicle_inspection_reports_page import DriverVehicleInspectionReportsPage
from pages.inspection_list_assignment_page import InspectionListAssignmentPage
from pages.inspection_list_management_page import InspectionListManagementPage
from pages.inspection_report_page import InspectionReportPage
from pages.inspection_schedules_page import InspectionSchedulesPage
from pages.login_page import LoginPage
from steps.common import DC_URL, ENV
from data.int.DVIR_data_int import DvirDataInt as DD_INT
from data.prod.DVIR_data_prod import DvirDataProd as DD_PROD
from data.stg.DVIR_data_stg import DvirDataStg as DD_STG

LOGIN_PAGE = 0
DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE = 0
DASHBOARD_PAGE = 0
INSPECTION_LIST_ASSIGNMENT_PAGE = 0
INSPECTION_SCHEDULES_PAGE = 0
INSPECTION_LIST_MANAGEMENT_PAGE = 0
INSPECTION_REPORT_PAGE = 0
DD = 0

scenarios('../features/DVIR.feature')


# LQ-12437
@given('full access user logs in')
def launch_browser(browser):
    global LOGIN_PAGE, DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE, DASHBOARD_PAGE, INSPECTION_LIST_ASSIGNMENT_PAGE, INSPECTION_SCHEDULES_PAGE, INSPECTION_LIST_MANAGEMENT_PAGE, INSPECTION_REPORT_PAGE, DD

    LOGIN_PAGE = LoginPage(browser)
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE = DriverVehicleInspectionReportsPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    INSPECTION_LIST_ASSIGNMENT_PAGE = InspectionListAssignmentPage(browser)
    INSPECTION_SCHEDULES_PAGE = InspectionSchedulesPage(browser)
    INSPECTION_LIST_MANAGEMENT_PAGE = InspectionListManagementPage(browser)
    INSPECTION_REPORT_PAGE = InspectionReportPage(browser)

    browser.get(DC_URL)

    if ENV == 'int':
        DD = DD_INT
    elif ENV == 'stg':
        DD = DD_STG
    else:
        DD = DD_PROD

    LOGIN_PAGE.enter_username(DD.fa_user_name)
    LOGIN_PAGE.enter_password(DD.password)
    LOGIN_PAGE.click_login()
    sleep(5)


@when('the user clicks DVIR')
def go_to_DVIR_page():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_dvir_tab_new_ui()

@then(
    'Total reports count, reset button, group filter, date filter, status filter, defect filter and wild search filter are shown on "DRIVER VEHICLE INSPECTION REPORTS" page and table columns are: "REPORT ID", "TYPE", "STATUS", "REPORT DATE", "DURATION", "DRIVER", "VEHICLE", "MAJOR VEHICLE DEFECTS", "MINOR VEHICLE DEFECTS", "VEHICLE INSPECTION LIST", "TRAILER", "MAJOR TRAILER DEFECTS", "MINOR TRAILER DEFECTS", "TRAILER INSPECTION LIST", "MECHANIC/AGENT", "REVIEWER"')
def verify_driver_vehicle_inspection_report_page():
    sleep(2)
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_total_report_title() == "Reports"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_groups_filter_title() == "Select Group(s)"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_date_range_filter_title() == "Select Date Range"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_statuses_filter_title() == "Status"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_defects_filter_title() == "Defects"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_search_filter_title() == "Select Search"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_reset_button_title() == "Reset"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_report_Id_title() == "REPORT ID"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_type_title() == "TYPE"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_status_title() == "STATUS"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_report_date_title() == "REPORT DATE"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_duration_title() == "DURATION"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_driver_title() == "DRIVER"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_vehicle_title() == "VEHICLE"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_major_vehicle_defects_title() == "MAJOR VEHICLE DEFECTS"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_minor_vehicle_defects_title() == "MINOR VEHICLE DEFECTS"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_vehicle_inspection_list_title() == "VEHICLE INSPECTION LIST"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_trailer_title() == "TRAILER"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_major_trailer_defects_title() == "MAJOR TRAILER DEFECTS"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_minor_trailers_defects_title() == "MINOR TRAILER DEFECTS"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_trailer_inspection_list_title() == "TRAILER INSPECTION LIST"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_mechanic_agent_title() == "MECHANIC/AGENT"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_reviewer_title() == "REVIEWER"


# LQ-12439
@when('the user clicks Statuses and select one or multiple statuses on "DRIVER VEHICLE INSPECTION REPORTS" page')
def navigate_to_statuses_filter():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_statuses_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_first_statuses()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_statuses_filter()
    sleep(5)


@then('"DRIVER VEHICLE INSPECTION" reports with selected status are shown in table')
def verify_statuses_filter():
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_first_status_text() == "Defect"
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_reset_button()


@when('the user clicks Select Date Range and select dates on "DRIVER VEHICLE INSPECTION REPORTS" page')
def navigate_to_date_filter():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_date_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_first_date()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_second_date()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_date_apply_button()
    sleep(5)


@then('"DRIVER VEHICLE INSPECTION" reports within the selected date range are shown in table')
def verify_date_filter():
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_row_count() == 10
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_reset_button()


@when('the user selects a group in Select Group dialog')
def navigate_to_group_filter():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_group_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.search_group_filter(DD.group)
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_searched_group()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_group_done_button()
    sleep(5)


@then('"DRIVER VEHICLE INSPECTION" reports belongs to the group are shown in table')
def verify_group_filter():
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.total_reports_top_count() == str(
        DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_total_page_count())
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_reset_button()


@when('the user clicks Defect and select one or multiple defects on "DRIVER VEHICLE INSPECTION REPORTS" page')
def navigate_to_defect_filter():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_defect_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_first_defects()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.close_defect_filter()


@then('"DRIVER VEHICLE INSPECTION" reports with the defect are shown in table')
def verify_defects_filter():
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_row_count(10) == 0
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_reset_button()


@when(
    'the user clicks Select Search, select a search option and input search criteria on "DRIVER VEHICLE INSPECTION REPORTS" page')
def navigate_to_search_filter():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_search_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_first_search_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.search_criteria_filter(DD.driver)
    sleep(5)


@then('"DRIVER VEHICLE INSPECTION" reports match the search criteria are shown in table')
def verify_search_filter():
    assert_that(DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_first_driver_text(), contains_string(DD.driver))
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_reset_button()


# LQ-27998
@given('there are some defect status reports')
def filter_defect_statue_report():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_search_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_select_search_report_id()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.search_criteria_filter(DD.defect_status_report_id)
    sleep(2)


@when(
    'the user clicks one report id of defect status and the user clicks "Resolve" dropdown and the user selects Repaired')
def select_repaired():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_first_report_id_searched_link()
    INSPECTION_REPORT_PAGE.click_resolve_button()
    INSPECTION_REPORT_PAGE.click_repaired_button()


@then('The "Reopen" button displays with Repaired text')
def assert_repaired():
    assert INSPECTION_REPORT_PAGE.get_repaired_text() == "Repaired"
    assert INSPECTION_REPORT_PAGE.get_reopen_text() == "Reopen"


@when('the user clicks "Reopen" button behind defect')
def click_reopen():
    INSPECTION_REPORT_PAGE.click_reopen_button()


@then('The "Resolve" button displays')
def asser_reopen():
    assert INSPECTION_REPORT_PAGE.get_resolve_text() == "Resolve"


@when('the user clicks "Resolve" dropdown and the user selects No Repair Needed')
def select_no_repair_needed():
    INSPECTION_REPORT_PAGE.click_resolve_button()
    INSPECTION_REPORT_PAGE.click_no_repair_needed_button()


@then('The "Reopen" button displays with No Repair Needed text')
def assert_no_repair_needed():
    assert INSPECTION_REPORT_PAGE.get_no_repair_needed_text() == "No Repair Needed"
    assert INSPECTION_REPORT_PAGE.get_reopen_text() == "Reopen"

    # for next run
    INSPECTION_REPORT_PAGE.click_reopen_button()

    INSPECTION_REPORT_PAGE.click_back_button()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_reset_button()


# @LQ-12444
@when('the user clicks Download Report')
def click_download_report():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_download_csv_report()


@then('the "INSPECTION REPORT" is downloaded')
def verify_csv_report_downloaded():
    file_name = DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_dvir_report_file_name()
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.check_file_exist(file_name) is True


# LQ-12430
@when('the user clicks the "List Settings" tab & the user clicks "List Assignment"')
def navigate_to_list_assignment():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_list_settings_existing_user_tab()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_assignment_tab_existing_user_new_ui()
    sleep(5)


@then(
    'the page header "INSPECTION LIST ASSIGNMENT" is displayed & the vehicle count is displayed & the table is displayed with columns: "VEHICLE", "GROUP", "VEHICLE TYPE" and "INSPECTION LIST"')
def verify_inspection_list_assignment_page():
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_assignment_title() == "INSPECTION LIST ASSIGNMENT"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_vehicle_count_title() == "Vehicles"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_vehicle_table_title() == "VEHICLE"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_group_table_title() == "GROUP"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_vehicle_type_table_title() == "VEHICLE TYPE"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_table_title() == "INSPECTION LIST"


# LQ-12431
@when('the user sets group filter to one group')
def navigate_to_groups_filter():
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_groups_filter()
    INSPECTION_LIST_ASSIGNMENT_PAGE.search_groups_filter(DD.group)
    INSPECTION_LIST_ASSIGNMENT_PAGE.select_first_groups_filter()
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_done_groups_filter()
    sleep(5)


@then('the vehicles belong to the group are listed')
def verify_vehicle_groups_filter():
    assert_that(INSPECTION_LIST_ASSIGNMENT_PAGE.get_first_vehicle_group_text(), contains_string(DD.group))
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_reset_button()


@when('the user clicks on "Vehicle Type" filter & the user selects one or more vehicle type(s)')
def navigate_to_vehicle_type_filter():
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_vehicle_type_filter()
    INSPECTION_LIST_ASSIGNMENT_PAGE.select_vehicle_type_filter()
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_vehicle_type_filter()
    sleep(5)


@then('the vehicles with the selected vehicle type(s) are displayed')
def verify_vehicle_type_filter():
    assert_that(INSPECTION_LIST_ASSIGNMENT_PAGE.get_first_row_vehicle_type_text(), contains_string("Ambulance"))
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_reset_button()


@when(
    'the user clicks on "Inspection List" filter & the user selects one or more inspection list(s) on the Vehicle Assignment page')
def navigate_to_inspection_list_filter():
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_inspection_list_filter()
    INSPECTION_LIST_ASSIGNMENT_PAGE.select_inspection_list_filter()
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_inspection_list_search_button()
    sleep(5)


@then('the vehicles with the selected inspection list are displayed')
def verify_vehicle_inspection_list_filter():
    assert str(INSPECTION_LIST_ASSIGNMENT_PAGE.get_selected_inspection_list()) in INSPECTION_LIST_ASSIGNMENT_PAGE.get_first_row_inspection_list_text()
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_reset_button()


@when('the user enters some characters into "Search Vehicle Name" field')
def navigate_to_search_vehicle_filter():
    INSPECTION_LIST_ASSIGNMENT_PAGE.search_vehicle_name_filter(DD.vehicle)
    sleep(3)


@then('the vehicles names have inputted characters are shown')
def verify_vehicle_search_filter():
    assert_that(INSPECTION_LIST_ASSIGNMENT_PAGE.get_first_row_vehicle_name_text(), contains_string(DD.vehicle))
    sleep(7)


# @LQ-12432
@when(
    'the user checks some available vehicles & the user clicks "Set Inspection List" Button on the Vehicle Assignment page')
def Set_vehicle_inspection_list():
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_reset_button()
    sleep(3)
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_first_vehicle_inspection_list()
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_second_vehicle_inspection_list()
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_set_inspection_vehicle_list_button()
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_inspection_default_checkbox()
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_vehicle_set_popup()
    sleep(10)


@then('the selected inspection list(s) are set to the selected vehicles on the Vehicle Assignment page')
def Verify_vehicle_set_inspection_list():
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_first_vehicle_inspection_list() == "Default"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_second_vehicle_inspection_list() == "Default"
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_reset_button()
    sleep(5)


# LQ-12436
@when('user clicks "SCHEDULE" on left navigation')
def click_schedule_tab():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_schedules_tab()


@then(
    'the page header "INSPECTION SCHEDULES" is displayed & the count of the vehicle schedule report is displayed & the table is displayed with columns')
def verify_inspection_schedules_table():
    sleep(3)
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_schedules_title() == "INSPECTION SCHEDULES"
    assert INSPECTION_SCHEDULES_PAGE.get_reports_title() == "Reports"
    assert INSPECTION_SCHEDULES_PAGE.get_vehicle_name_title() == "VEHICLE NAME"
    assert INSPECTION_SCHEDULES_PAGE.get_vehicle_group_title() == "VEHICLE GROUP"
    assert INSPECTION_SCHEDULES_PAGE.get_status_title() == "STATUS"
    assert INSPECTION_SCHEDULES_PAGE.get_due_date_title() == "DUE DATE"
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_list_title() == "INSPECTION LIST"
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_frequency_title() == "INSPECTION FREQUENCY"
    assert INSPECTION_SCHEDULES_PAGE.get_last_inspected_date_title() == "LAST INSPECTED DATE"
    assert INSPECTION_SCHEDULES_PAGE.get_last_inspected_driver_title() == "LAST INSPECTED DRIVER"


# LQ-12459
@when('the user sets group filter to one group in Vehicle Schedule page')
def set_groups_filter():
    INSPECTION_SCHEDULES_PAGE.click_groups_filter()
    INSPECTION_SCHEDULES_PAGE.search_groups_filter(DD.group)
    INSPECTION_SCHEDULES_PAGE.select_groups_filter()
    INSPECTION_SCHEDULES_PAGE.click_done_button()
    sleep(5)


@then('the vehicles schedule reports vehicle group belong to the group are listed')
def verify_inspection_groups_filter():
    assert_that(INSPECTION_SCHEDULES_PAGE.get_vehicle_group_first_row_text(), contains_string(DD.subgroup))
    INSPECTION_SCHEDULES_PAGE.click_reset_button()
    sleep(2)


@when(
    'the user clicks on "Inspection List" filter & the user selects one or more inspection list(s) on the Vehicle Schedule page')
def set_inspection_lists_filter():
    INSPECTION_SCHEDULES_PAGE.click_inspection_lists_filter()
    INSPECTION_SCHEDULES_PAGE.select_inspection_lists_filter()
    INSPECTION_SCHEDULES_PAGE.close_vehicle_inspection_list()


@then('the vehicle schedule reports with the selected inspection list are displayed')
def verify_inspection_lists_filter():
    assert str(
        INSPECTION_SCHEDULES_PAGE.get_selected_inspection_list()) in INSPECTION_SCHEDULES_PAGE.get_inspection_list_first_row_text()

    INSPECTION_SCHEDULES_PAGE.click_reset_button()
    sleep(2)


@when('the user clicks on "Status" filter & the user selects one or more status')
def set_status_filter():
    INSPECTION_SCHEDULES_PAGE.click_status_filter()
    INSPECTION_SCHEDULES_PAGE.select_status_filter()
    INSPECTION_SCHEDULES_PAGE.click_status_filter()
    sleep(5)


@then('the vehicle schedule reports with the selected status are displayed')
def verify_inspection_status_filter():
    sleep(3)
    assert_that(INSPECTION_SCHEDULES_PAGE.get_status_first_row_text(), contains_string("Overdue"))
    INSPECTION_SCHEDULES_PAGE.click_reset_button()


@when('the user enters some characters into "Search Vehicle Name" field & the user clicks the search icon')
def set_search_vehicle_name_filter():
    INSPECTION_SCHEDULES_PAGE.search_vehicle_name_filter(DD.vehicle)
    sleep(5)


@then('the vehicle schedule reports belong to the filtered vehicles are shown')
def verify_vehicle_name_filter():
    assert_that(INSPECTION_SCHEDULES_PAGE.get_vehicle_name_first_row_text(), contains_string(DD.vehicle))
    sleep(3)


# @LQ-12460
@given('the "Full Access" user is landed in the vehicle schedule page')
def navigate_to_vehicle_schedule_page():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_schedules_tab()


@when('the user clicks Download CSV in vehicle schedule page')
def click_on_vehicle_schedule_download_csv():
    INSPECTION_SCHEDULES_PAGE.click_download_csv_report()


@then('the Vehicle Schedule report is downloaded')
def verify_csv_report_downloaded():
    file_name = INSPECTION_SCHEDULES_PAGE.get_dvir_list_file_name()
    assert INSPECTION_SCHEDULES_PAGE.check_file_exist(file_name) is True


# LQ-12446
@when('the "Full Access" user is in the Vehicle list page')
def navigate_to_vehicle_list_management_page():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_list_settings_existing_user_tab()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_list_management_tab_existing_user()
    sleep(2)


@then(
    'the title "VEHICLE INSPECTION LISTS" is displayed & there is a default vehicle inspection list and named "Default" & there is a duplicate icon behind the list name')
def verify_inspection_management_titles():
    assert INSPECTION_LIST_MANAGEMENT_PAGE.get_vehicle_inspection_list_title() == "VEHICLE INSPECTION LISTS"
    assert INSPECTION_LIST_MANAGEMENT_PAGE.get_default_title() == "Default"
    assert INSPECTION_LIST_MANAGEMENT_PAGE.vehicle_duplicate_icon_displayed() is True


# LQ-12423
@when('the user clicks on Edit icon of one list & the user updates the List name & the user clicks "Save Changes"')
def edit_list_name():
    INSPECTION_LIST_MANAGEMENT_PAGE.click_edit_button()
    INSPECTION_LIST_MANAGEMENT_PAGE.clear_list_name()
    INSPECTION_LIST_MANAGEMENT_PAGE.edit_list_name(DD.updated_list_name)
    sleep(2)
    INSPECTION_LIST_MANAGEMENT_PAGE.click_save_changes_button()
    sleep(2)


@then('the vehicle inspection list is updated')
def verify_edited_inspection_list_name():
    assert_that(INSPECTION_LIST_MANAGEMENT_PAGE.get_all_vehicle_inspection_lists(),
                contains_string(DD.updated_list_name))
    sleep(5)


# LQ-12422
@when(
    'the user clicks on "New List" button & the user enters required fields: "List Name", "Inspection Item Section" and "Inspection Points" & the user clicks Create')
def create_a_new_list():
    INSPECTION_LIST_MANAGEMENT_PAGE.click_new_list_button()
    sleep(3)
    INSPECTION_LIST_MANAGEMENT_PAGE.type_new_list_name(DD.new_list_name)
    INSPECTION_LIST_MANAGEMENT_PAGE.type_new_section_item(DD.session_item)
    INSPECTION_LIST_MANAGEMENT_PAGE.type_list_inspection_points(DD.list_inspection_points)
    INSPECTION_LIST_MANAGEMENT_PAGE.click_create_new_list_button()
    sleep(2)


@then('the vehicle inspection list is added')
def verify_new_added_list():
    assert_that(INSPECTION_LIST_MANAGEMENT_PAGE.get_all_vehicle_inspection_lists(), contains_string(DD.new_list_name))


# @LQ-12424
@when('the user clicks on Duplicate icon of one list')
def click_on_duplicate_list():
    INSPECTION_LIST_MANAGEMENT_PAGE.click_duplicate_icon()
    sleep(2)


@then('the duplicate vehicle inspection list is added & the name of the duplicate vehicle inspection list ends in "Copy1"')
def verify_duplicate_list():
    assert_that(INSPECTION_LIST_MANAGEMENT_PAGE.get_all_vehicle_inspection_lists(), contains_string("Default_Copy"))


# LQ-12425
@when('the user clicks on Delete icon of one list & the user clicks "Delete" button on the pop-up')
def click_on_vehicle_list_delete():
    INSPECTION_LIST_MANAGEMENT_PAGE.click_list_delete_icon()
    INSPECTION_LIST_MANAGEMENT_PAGE.click_inspection_list_delete_button()
    sleep(3)


@then('the vehicle inspection list is deleted')
def verify_vehicle_list_delete():
    assert INSPECTION_LIST_MANAGEMENT_PAGE.get_first_vehicle_inspection_lists() == DD.new_list_name
    sleep(3)


# @LQ-12447
@when('the "Full Access" user is in the Trailer list page')
def navigate_to_trailer_list():
    INSPECTION_LIST_MANAGEMENT_PAGE.click_trailer_list_link()
    sleep(3)


@then(
    'the title "TRAILER INSPECTION LISTS" is displayed & there is a default trailer inspection list and named "Default" & there is a duplicate icon behind the list name')
def verify_trailer_inspection_list():
    assert INSPECTION_LIST_MANAGEMENT_PAGE.get_trailer_inspection_lists_title() == "TRAILER INSPECTION LISTS"
    assert INSPECTION_LIST_MANAGEMENT_PAGE.get_default_inspection_lists_title() == "Default"
    assert INSPECTION_LIST_MANAGEMENT_PAGE.trailer_duplicate_icon_displayed() is True


# @LQ-12427
@when(
    'the user clicks on Edit icon of one list in trailer list & the user update the List name & the user clicks "Save Changes"')
def edit_trailer_list_name():
    global list_name
    list_name = INSPECTION_LIST_MANAGEMENT_PAGE.get_random_name(6)
    INSPECTION_LIST_MANAGEMENT_PAGE.click_trailer_edit_list_button()
    INSPECTION_LIST_MANAGEMENT_PAGE.clear_trailer_list_name()
    INSPECTION_LIST_MANAGEMENT_PAGE.type_new_trailer_list_name(list_name)
    INSPECTION_LIST_MANAGEMENT_PAGE.clear_trailer_inspection_item()
    INSPECTION_LIST_MANAGEMENT_PAGE.type_new_trailer_inspection_item(DD.session_item)
    INSPECTION_LIST_MANAGEMENT_PAGE.clear_trailer_inspection_points()
    INSPECTION_LIST_MANAGEMENT_PAGE.type_new_trailer_inspection_points(DD.list_inspection_points)
    INSPECTION_LIST_MANAGEMENT_PAGE.click_trailer_save_changes_edit_button()
    sleep(3)


@then('the trailer inspection list is update')
def verify_edit_trailer_list_name():
    assert INSPECTION_LIST_MANAGEMENT_PAGE.get_all_trailer_inspection_lists() != DD.updated_trailer_list_name
    # assert DD.updated_trailer_list_name in INSPECTION_LIST_MANAGEMENT_PAGE.get_all_trailer_inspection_lists()
    sleep(2)  # added sleep to load data in page


# @LQ-12426
@when(
    'the user clicks on "New List" button in trailer list & the user enters required fields: "List Name", "Inspection Item Section" and "Inspection Points" & the user clicks "Create"')
def create_new_trailer_list():
    INSPECTION_LIST_MANAGEMENT_PAGE.click_trailer_new_list_button()
    INSPECTION_LIST_MANAGEMENT_PAGE.type_new_trailer_list_name(DD.new_trailer_list_name)
    INSPECTION_LIST_MANAGEMENT_PAGE.type_new_trailer_inspection_item(DD.session_item)
    INSPECTION_LIST_MANAGEMENT_PAGE.type_new_trailer_inspection_points(DD.list_inspection_points)
    INSPECTION_LIST_MANAGEMENT_PAGE.click_trailer_create_new_list_button()
    sleep(3)


@then('the trailer inspection list is added')
def verify_new_trailer_list():
    sleep(15)
    assert DD.new_trailer_list_name in INSPECTION_LIST_MANAGEMENT_PAGE.get_all_trailer_inspection_lists()


# @LQ-12429
@when('the user clicks on Delete icon of one list & the user clicks "Delete" button on the pop-up in trailer list')
def delete_trailer_list():
    INSPECTION_LIST_MANAGEMENT_PAGE.click_trailer_delete_list_button()
    INSPECTION_LIST_MANAGEMENT_PAGE.click_trailer_delete_list_popup_button()
    sleep(3)


@then('the trailer inspection list is deleted')
def verify_delete_trailer_list():
    assert DD.new_trailer_list_name not in INSPECTION_LIST_MANAGEMENT_PAGE.get_all_trailer_inspection_lists()


# LQ-12428
@when('the user clicks on Duplicate icon of one list on trailer list')
def duplicate_trailer_list():
    INSPECTION_LIST_MANAGEMENT_PAGE.click_trailer_list_duplicate_button()
    sleep(3)


@then('the duplicate trailer inspection list is added & the name of the duplicate trailer inspection list ends in "Copy1"')
def verify_duplicate_trailer_list():
    assert_that(INSPECTION_LIST_MANAGEMENT_PAGE.get_all_trailer_inspection_lists(), contains_string("Default_Copy"))


# LQ-12433
@given('the "Full Access" user is in Vehicle Assignment page')
def navigate_to_list_assignment_vehicle_page():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_list_settings_existing_user_tab()
    sleep(2)
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_assignment_tab_existing_user_new_ui()


@when('the user clicks the "Trailer Assignment" tab')
def navigate_to_trailer_list_assignment_page():
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_trailer_assignment_tab()
    sleep(3)


@then(
    'the page header "INSPECTION LIST ASSIGNMENT" is displayed & the trailer count is displayed & the table is displayed with columns: "TRAILER", "GROUP", "TRAILER TYPE" and "INSPECTION LIST"')
def verify_trailer_assignment_titles():
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_assignment_title() == "INSPECTION LIST ASSIGNMENT"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_trailers_count() == "Trailers"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_trailer_column() == "TRAILER"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_group_title() == "GROUP"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_trailer_type_title() == "TRAILER TYPE"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_inspection_list_column_title() == "INSPECTION LIST"


# @LQ-12434
@when('the user sets group filter to one group in trailer assignment page')
def set_trailer_group_filter():
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_trailer_group_filter()
    INSPECTION_LIST_ASSIGNMENT_PAGE.search_trailer_group_name_filter(DD.group)
    INSPECTION_LIST_ASSIGNMENT_PAGE.select_trailer_group_filter()
    sleep(2)
    INSPECTION_LIST_ASSIGNMENT_PAGE.deselect_sub_groups_filter()
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_done_trailer_group_filter()
    sleep(3)


@then('the trailers belong to the group are listed')
def verify_trailer_group_filter():
    assert_that(INSPECTION_LIST_ASSIGNMENT_PAGE.get_first_trailer_group_name(), contains_string(DD.group))
    sleep(5)
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_trailer_reset_button()


@when(
    'the user clicks on "Trailer Type" filter & the user selects one or more trailer type(s) in trailer assignment page')
def set_trailer_type_filter():
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_trailer_assignment_type_filter()
    INSPECTION_LIST_ASSIGNMENT_PAGE.select_trailer_assignment_type_filter()
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_trailer_assignment_type_filter()
    sleep(3)


@then('the trailers with the selected trailer type(s) are displayed')
def verify_trailer_type_filter():
    assert_that(INSPECTION_LIST_ASSIGNMENT_PAGE.get_first_trailer_type_name(),
                contains_string(INSPECTION_LIST_ASSIGNMENT_PAGE.get_selected_trailer_assignment_type()))
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_trailer_reset_button()


@when(
    'the user clicks on "Inspection List" filter & the user selects one or more inspection list(s) in trailer assignment page')
def set_inspection_list_filter():
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_trailer_reset_button()
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_trailer_inspection_list_filter()
    INSPECTION_LIST_ASSIGNMENT_PAGE.select_trailer_inspection_list_filter()
    INSPECTION_LIST_ASSIGNMENT_PAGE.close_trailer_inspection_list_filter()
    sleep(3)


@then('the trailers with the selected inspection list are displayed')
def verify_inspection_list_filter():
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_trailer_inspection_list_filter()
    assert_that(INSPECTION_LIST_ASSIGNMENT_PAGE.get_first_trailer_inspection_list(),
                contains_string(INSPECTION_LIST_ASSIGNMENT_PAGE.get_selected_trailer_inspection_list_text()))

    INSPECTION_LIST_ASSIGNMENT_PAGE.click_trailer_reset_button()
    sleep(3)


@when('the user enters some characters into "Search Trailer Name" field in trailer assignment page')
def set_search_trailer_vehicle_name():
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_trailer_reset_button()
    INSPECTION_LIST_ASSIGNMENT_PAGE.search_trailer_name_filter(DD.trailer)
    sleep(3)


@then('the trailers names have inputted characters are shown')
def verify_trailer_search_vehicle():
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_first_trailer_name_stg() == DD.trailer


# @LQ-12435
@when(
    'the user checks some available trailers & the user clicks "Set Inspection List" Button & the user selects one or more inspection list(s) & the user clicks "Set" button in trailer assignment page')
def set_trailer_inspection_list():
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_trailer_reset_button()
    sleep(2)
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_first_trailer_inspection_list()
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_second_trailer_inspection_list()
    sleep(2)
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_set_inspection_list_button()
    INSPECTION_LIST_ASSIGNMENT_PAGE.select_default_inspection_list_popup()
    INSPECTION_LIST_ASSIGNMENT_PAGE.click_set_inspection_list_popup_button()
    sleep(15)


@then('the selected inspection list(s) are set to the selected trailers')
def verify_trailer_set_inspection_list():
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_trailer_first_inspection_list() == "Default"
    assert INSPECTION_LIST_ASSIGNMENT_PAGE.get_trailer_second_inspection_list() == "Default"


# LQ-12463
@given('the "Full Access" user is in the trailer schedule page')
def landed_on_trailer_schedule_page():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_schedules_tab()
    INSPECTION_SCHEDULES_PAGE.click_trailer_schedules_link()


@when('the user clicks Download CSV in trailer schedule page')
def download_csv_trailer_schedule():
    INSPECTION_SCHEDULES_PAGE.click_download_csv_report()


@then('the Trailer Schedule report is downloaded in trailer schedule page')
def verify_download_csv_trailer_schedule():
    file_name = INSPECTION_SCHEDULES_PAGE.get_dvir_list_file_name()
    assert INSPECTION_SCHEDULES_PAGE.check_file_exist(file_name) is True


# LQ-12461
@when('user clicks "SCHEDULE" on left navigation & user clicks "Trailer Schedule"')
def navigate_to_trailer_schedule_tab():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_schedules_tab()
    INSPECTION_SCHEDULES_PAGE.click_trailer_schedules_link()
    INSPECTION_SCHEDULES_PAGE.click_trailer_reset_button()
    sleep(3)


@then(
    'the page header "INSPECTION SCHEDULES" is displayed & the count of the trailer schedule report is displayed & the table is displayed with columns')
def verify_trailer_schedule_table():
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_schedules_title() == "INSPECTION SCHEDULES"
    assert INSPECTION_SCHEDULES_PAGE.get_trailer_reports_title() == "Reports"
    assert INSPECTION_SCHEDULES_PAGE.get_trailer_name_column_text() == "TRAILER NAME"
    assert INSPECTION_SCHEDULES_PAGE.get_trailer_group_column_text() == "TRAILER GROUP"
    assert INSPECTION_SCHEDULES_PAGE.get_status_column_text() == "STATUS"
    assert INSPECTION_SCHEDULES_PAGE.get_due_date_column_text() == "DUE DATE"
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_list_column_text() == "INSPECTION LIST"
    assert INSPECTION_SCHEDULES_PAGE.get_inspection_frequency_column_text() == "INSPECTION FREQUENCY"
    assert INSPECTION_SCHEDULES_PAGE.get_last_inspected_date_column_text() == "LAST INSPECTED DATE"
    assert INSPECTION_SCHEDULES_PAGE.get_last_inspected_driver_column_text() == "LAST INSPECTED DRIVER"


# @LQ-12462
@when('the user sets group filter to one group in Trailer Schedule page')
def set_trailer_group_filter():
    INSPECTION_SCHEDULES_PAGE.click_trailer_group_filter_button()
    INSPECTION_SCHEDULES_PAGE.search_trailer_groups_filter(DD.group2)
    INSPECTION_SCHEDULES_PAGE.select_trailer_group_filter()
    INSPECTION_SCHEDULES_PAGE.select_groups_root_filter()
    INSPECTION_SCHEDULES_PAGE.click_trailer_schedule_group_done_button()
    sleep(5)


@then('the trailer schedule reports trailer group belong to the group are listed in Trailer Schedule Page')
def verify_trailer_group_filter():
    assert_that(INSPECTION_SCHEDULES_PAGE.get_first_trailer_group_text(), contains_string(DD.group2))
    sleep(5)
    INSPECTION_SCHEDULES_PAGE.click_trailer_reset_button()


@when(
    'the user clicks on "Inspection List" filter & the user selects one or more inspection list(s) in Trailer Schedule page')
def set_trailer_inspection_list_filter():
    INSPECTION_SCHEDULES_PAGE.click_trailer_inspection_list_filter()
    INSPECTION_SCHEDULES_PAGE.select_trailer_inspection_list_filter()
    INSPECTION_SCHEDULES_PAGE.close_trailer_inspection_list()
    INSPECTION_SCHEDULES_PAGE.click_trailer_inspection_list_filter()
    sleep(3)


@then('the trailer schedule reports with the selected inspection list are displayed')
def verify_trailer_inspection_list_filter():
    assert INSPECTION_SCHEDULES_PAGE.get_selected_trailer_inspection_list() in INSPECTION_SCHEDULES_PAGE.get_first_trailer_inspection_list_text()
    INSPECTION_SCHEDULES_PAGE.click_trailer_reset_button()


@when('the user clicks on "Status" filter & the user selects one or more status in Trailer Schedule page')
def set_trailer_status_filter():
    INSPECTION_SCHEDULES_PAGE.click_status_inspection_list_filter()
    INSPECTION_SCHEDULES_PAGE.select_status_inspection_list_filter()
    INSPECTION_SCHEDULES_PAGE.click_status_inspection_list_filter()
    sleep(3)


@then('the trailer schedule reports with the selected status are displayed')
def verify_trailer_status_filter():
    INSPECTION_SCHEDULES_PAGE.click_status_inspection_list_filter()
    assert_that(INSPECTION_SCHEDULES_PAGE.get_first_trailer_status_text(), contains_string("Overdue"))
    sleep(3)
    INSPECTION_SCHEDULES_PAGE.click_trailer_reset_button()
    sleep(3) # added sleep to load data in page


@when('the user enters some characters into "Search Trailer Name" field')
def set_search_trailer_name_filter():
    INSPECTION_SCHEDULES_PAGE.search_trailer_name_filter(DD.trailer)
    sleep(3)


@then('the trailer schedule reports belong to the filtered trailers are shown')
def verify_search_trailer_name_filter():
    assert INSPECTION_SCHEDULES_PAGE.get_first_trailer_name_text_stg(), contains_string(DD.trailer)
    sleep(3)


# LQ-12442
@when('the user clicks an "INSPECTION REPORT"')
def navigate_to_inspection_report_page():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_dvir_tab_new_ui()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_reset_button()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_search_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_select_search_report_id()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.search_criteria_filter(DD.report_id_without_note)
    sleep(5)
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_first_report_id_searched_link()


@then(
    'the "INSPECTION REPORT" is opened with "REPORT ID", "INSPECTION TYPE", "DRIVER", "REPORT DATE", "STATUS" and "LOCATION" & the vehicle info is shown with "LICENSE PLATE", "ODOMETER" and status & the driver signature is shown with name and date')
def verify_inspection_report_labels():
    assert INSPECTION_REPORT_PAGE.get_inspection_report_title() == "INSPECTION REPORT"
    assert INSPECTION_REPORT_PAGE.get_report_id_title() == "REPORT ID"
    assert INSPECTION_REPORT_PAGE.get_inspection_type_title() == "INSPECTION TYPE"
    assert INSPECTION_REPORT_PAGE.get_driver_title() == "DRIVER"
    assert INSPECTION_REPORT_PAGE.get_report_date_title() == "REPORT DATE"
    assert INSPECTION_REPORT_PAGE.get_status_title() == "STATUS"
    assert INSPECTION_REPORT_PAGE.get_location_title() == "LOCATION"
    assert INSPECTION_REPORT_PAGE.get_odometer_title() == "ODOMETER"
    sleep(2)
    assert INSPECTION_REPORT_PAGE.get_driver_signature_name_title() == "DRIVER SIGNATURE"
    assert INSPECTION_REPORT_PAGE.get_mechanic_signature_title() == "MECHANIC/AGENT SIGNATURE"


# @LQ-5410
@when('the user clicks "Add Note" button & the user enters some characters & the user clicks "Save" button')
def add_notes_inspection_report():
    INSPECTION_REPORT_PAGE.click_add_notes_button()
    INSPECTION_REPORT_PAGE.send_notes_text(DD.add_note_text)
    INSPECTION_REPORT_PAGE.click_add_notes_save_button()
    sleep(6)


@then('the entered characters are added & the "Edit" button and "Delete" button will show')
def verify_inspection_report_added_notes():
    INSPECTION_REPORT_PAGE.click_keboo_button()
    sleep(3)
    assert INSPECTION_REPORT_PAGE.get_added_notes_text() == DD.add_note_text
    assert INSPECTION_REPORT_PAGE.get_edit_button_text() == "Edit"
    assert INSPECTION_REPORT_PAGE.get_delete_button_text() == "Delete"


# LQ-5437
@when(
    "the user clicks the keboo & the user clicks 'Edit' button & the user enters some characters & the user clicks 'Save' button")
def edit_notes_inspection_report():
    INSPECTION_REPORT_PAGE.click_edit_button()
    INSPECTION_REPORT_PAGE.clear_added_notes()
    INSPECTION_REPORT_PAGE.send_notes_text(DD.update_note_text)
    INSPECTION_REPORT_PAGE.click_add_notes_save_button()
    sleep(5)


@then('the note updated correctly')
def verify_edit_notes_inspection_report():
    assert INSPECTION_REPORT_PAGE.get_edited_note_text() == DD.update_note_text
    INSPECTION_REPORT_PAGE.click_keboo_button()
    INSPECTION_REPORT_PAGE.click_delete_notes_button()
    sleep(3)


@when(
    "the other user clicks the keboo & the user clicks 'Edit' button & the user enters some characters & the user clicks 'Save' button")
def navigate_to_edit_notes():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_dvir_tab_new_ui()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_reset_button()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_search_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_select_search_report_id()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.clear_search_dvir_id()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.search_criteria_filter(DD.report_id_with_note)
    sleep(5)
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_first_report_id_searched_link()
    INSPECTION_REPORT_PAGE.scroll_down_to_the_end_of_page()
    INSPECTION_REPORT_PAGE.click_keboo_button()
    INSPECTION_REPORT_PAGE.click_edit_button()
    INSPECTION_REPORT_PAGE.clear_added_notes()
    INSPECTION_REPORT_PAGE.send_notes_text(DD.update_note_text)
    INSPECTION_REPORT_PAGE.click_add_notes_save_button()
    sleep(5)


@then('the note updated correctly in the inspection report page')
def verify_other_user_edit_notes():
    assert INSPECTION_REPORT_PAGE.get_added_notes_text() == DD.update_note_text


# LQ-12445
@when('the user clicks Back')
def click_on_back_button():
    INSPECTION_REPORT_PAGE.click_back_button()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_reset_button()


@then(
    'Total reports count, group filter, date filter, status filter, defect filter and wild search filter are shown on "DRIVER VEHICLE INSPECTION REPORTS" page')
def verify_back_button():
    sleep(15)
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_total_report_title() == "Reports"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_groups_filter_title() == "Select Group(s)"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_date_range_filter_title() == "Select Date Range"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_statuses_filter_title() == "Status"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_defects_filter_title() == "Defects"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_search_filter_title() == "Select Search"


# LQ-12441
@when('the user clicks Download CSV on "DRIVER VEHICLE INSPECTION REPORTS" page')
def download_csv_DVIR_page():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_download_csv_report()


@then('"DRIVER VEHICLE INSPECTION" reports are downloaded successfully')
def verify_download_csv_DVIR_page():
    file_name = DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_dvir_report_file_name()
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.check_file_exist(file_name) is True


# LQ-27997
@given('support user logs in dvir page')
def launch_browser(browser):
    browser.get(DC_URL)
    LOGIN_PAGE.enter_username(DD.support_username)
    LOGIN_PAGE.enter_password(DD.support_password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed(DC_URL, DD.support_username, DD.support_password)
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_dvir_tab_new_ui()


@when('the user sets group filter to one group, sets one date range, sets Status filter to one status, sets Defects filter to one defect, searches vehicle by inputting some characters and clicks "Reset"')
def go_to_DVIR_page():
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.wait_for_page_load()
    global count_before_filters, count_after_filters
    count_before_filters = DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.total_reports_top_count()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_group_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.search_group_filter(DD.group)
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_searched_group()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_group_done_button()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_date_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_first_date()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_second_date()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_date_apply_button()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_statuses_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_first_statuses()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_statuses_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_defect_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_first_defects()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_search_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_first_search_filter()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.search_criteria_filter(DD.driver)
    count_after_filters = DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.total_reports_top_count()
    DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.click_reset_button()


@then('all filter back to default, the DVIR list is updated correctly according to default filter and the first page is displayed')
def verify_driver_vehicle_inspection_report_page():
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.total_reports_top_count() == count_before_filters
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.total_reports_top_count() != count_after_filters
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_groups_filter_title() == "Select Group(s)"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_date_range_filter_title() == "Select Date Range"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_statuses_filter_title() == "Status"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_defects_filter_title() == "Defects"
    assert DRIVER_VEHICLE_INSPECTION_REPORTS_PAGE.get_select_search_filter_title() == "Select Search"
