from datetime import datetime

from hamcrest import assert_that, contains_string
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then
from pages.add_user_page import *
from pages.dashboard_page import DashboardPage
from pages.device_management_page import DeviceManagementPage
from pages.edit_user_page import *
from pages.edit_vehicle_page import EditVehiclePage
from pages.login_page import LoginPage
from pages.my_account_page import MyAccountPage
from pages.user_management_page import UserManagementPage
from pages.vehicle_management_page import VehicleManagementPage
from steps.common import DC_URL, ENV
from data.int.admin_user_data_int import AdminUserDataInt as AUD_INT
from data.prod.admin_user_data_prod import AdminUserDataProd as AUD_PROD
from data.stg.admin_user_data_stg import AdminUserDataStg as AUD_STG

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
USER_MANAGEMENT_PAGE = 0
ADD_USER_PAGE = 0
EDIT_USER_PAGE = 0
DEVICE_MANAGEMENT_PAGE = 0
VEHICLE_MANAGEMENT_PAGE = 0
EDIT_VEHICLE_PAGE = 0
MY_ACCOUNT_PAGE = 0
AUD = 0

scenarios('../features/admin_user.feature')


# LQ-304
@given('the login page is displayed')
def launch_browser(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, USER_MANAGEMENT_PAGE, ADD_USER_PAGE, EDIT_USER_PAGE, DEVICE_MANAGEMENT_PAGE, \
        MY_ACCOUNT_PAGE, VEHICLE_MANAGEMENT_PAGE, EDIT_VEHICLE_PAGE, AUD

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)
    ADD_USER_PAGE = AddUserPage(browser)
    EDIT_USER_PAGE = EditUserPage(browser)
    MY_ACCOUNT_PAGE = MyAccountPage(browser)
    DEVICE_MANAGEMENT_PAGE = DeviceManagementPage(browser)
    VEHICLE_MANAGEMENT_PAGE = VehicleManagementPage(browser)
    EDIT_VEHICLE_PAGE = EditVehiclePage(browser)

    if ENV == 'int':
        AUD = AUD_INT
    elif ENV == 'stg':
        AUD = AUD_STG
    else:
        AUD = AUD_PROD
    browser.get(DC_URL)


@when('the user enters a newly created username/password and clicks the login button')
def login():
    LOGIN_PAGE.enter_username(AUD.pm_only_user_name)
    LOGIN_PAGE.enter_password(AUD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.url_change(AUD.dashboard_url)


@then('the user is successfully logged into the Driver Safety dashboard')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))


# LQ-251
@given('the "Program Manager" user is in the Driver Safety page')
def navigate_to_dashboard_page():
    DASHBOARD_PAGE.click_home_tab()


@when('the user clicks on Admin tab')
def navigate_to_user_management_page():
    DASHBOARD_PAGE.click_admin_tab()


# LQ-136209
@when('the user clicks on the "Users" menu')
def user_clicks_users_tab():
    USER_MANAGEMENT_PAGE.click_users_tab()


@then(
    'the user should be able to see all the filters like "Select Group(s)","Roles","Login" ,"Status", "Reset" and "Search Name or ID"')
def user_should_see_all_filter_options():
    assert USER_MANAGEMENT_PAGE.group_filter_is_displayed()
    assert USER_MANAGEMENT_PAGE.role_filter_is_displayed()
    assert USER_MANAGEMENT_PAGE.login_filter_is_displayed()
    assert USER_MANAGEMENT_PAGE.status_filter_is_displayed()
    assert USER_MANAGEMENT_PAGE.search_name_or_id_filter_is_displayed()
    assert USER_MANAGEMENT_PAGE.reset_button_is_displayed()


@then('the user should see the buttons "Import Users" and "Add Users"')
def user_should_see_buttons_import_users_and_add_users():
    assert USER_MANAGEMENT_PAGE.add_users_button_is_displayed()


@then('the user should see the pagination and download CSV in the bottom of the page')
def user_should_see_pagination_and_download_csv_option():
    assert USER_MANAGEMENT_PAGE.pagination_is_displayed()
    assert USER_MANAGEMENT_PAGE.download_csv_is_displayed()


@then('the page header "USER MANAGEMENT" is displayed and the user count are displayed and the table'
      ' is displayed with columns: "NAME", "EMPLOYEE ID", "LYTX BADGE", "PRIMARY DRIVER GROUP", '
      '"ROLES (GROUP)", "STATUS", "LOGIN", "USERNAME"')
def verify_user_management_tabs():
    assert USER_MANAGEMENT_PAGE.user_management_label_is_displayed() is True
    assert USER_MANAGEMENT_PAGE.get_user_count() == str(USER_MANAGEMENT_PAGE.get_total_page_count())
    assert USER_MANAGEMENT_PAGE.get_user_management_label() == "USER MANAGEMENT"
    assert USER_MANAGEMENT_PAGE.get_name_label() == "NAME"
    assert USER_MANAGEMENT_PAGE.get_employee_id_label() == "EMPLOYEE ID"
    assert USER_MANAGEMENT_PAGE.get_lytx_badge_label() == "LYTX BADGE"
    assert USER_MANAGEMENT_PAGE.get_primary_driver_group_label() == "PRIMARY DRIVER GROUP"
    assert USER_MANAGEMENT_PAGE.get_roles_label() == "ROLES (GROUP)"
    assert USER_MANAGEMENT_PAGE.get_status_label() == "STATUS"
    assert USER_MANAGEMENT_PAGE.get_login_label() == "LOGIN"
    assert USER_MANAGEMENT_PAGE.get_user_name_label() == "USERNAME"


# LQ-252
@when('the user sets group filter to one group')
def apply_group_filter_user_management():
    USER_MANAGEMENT_PAGE.click_select_group_filter()
    USER_MANAGEMENT_PAGE.search_group_filter(AUD.group)
    USER_MANAGEMENT_PAGE.select_searched_group()
    USER_MANAGEMENT_PAGE.click_done_group_filter()


@then('the users belong to the group are listed')
def verify_group_filter_user_management():
    assert_that(USER_MANAGEMENT_PAGE.get_user_group_label(), contains_string(AUD.group))


@when('the user clicks on "Roles" filter & the user selects one role')
def set_roles_filter_user_management():
    USER_MANAGEMENT_PAGE.click_reset_button()
    USER_MANAGEMENT_PAGE.click_roles_filter()
    # Select Driver role
    USER_MANAGEMENT_PAGE.select_roles_filter()
    USER_MANAGEMENT_PAGE.apply_select_role()


@then('the users with the selected role are displayed on the table')
def verify_role_filter_user_management():
    assert_that(USER_MANAGEMENT_PAGE.get_user_group_label(), contains_string(AUD.filter_role))


@when('the user clicks on "Login" filter & the user selects "Enable"')
def set_login_filter_user_management():
    USER_MANAGEMENT_PAGE.click_login_filter()
    # Select Login as Enabled
    USER_MANAGEMENT_PAGE.select_login_filter()


@then('the users with Login enabled are displayed on the table')
def verify_login_filter_user_management():
    assert USER_MANAGEMENT_PAGE.get_filtered_user_login() == "Enabled"
    USER_MANAGEMENT_PAGE.click_reset_button()


@when('the user clicks on "Status" filter & the user selects "Inactive"')
def set_status_filter_user_management():
    USER_MANAGEMENT_PAGE.click_status_filter()
    # Select Inactive status filter
    USER_MANAGEMENT_PAGE.select_status_filter()


@then('the inactive users are displayed on the table')
def verify_status_filter_user_management():
    assert USER_MANAGEMENT_PAGE.get_first_user_status() == "Inactive"
    USER_MANAGEMENT_PAGE.click_reset_button()


@when('the user enters some characters into "Search Name or ID" field')
def search_name_filter_user_management():
    USER_MANAGEMENT_PAGE.search_name_filter(AUD.pm_only_user_name)


@then('the users that have the inputted characters in their name or employeeid are shown')
def verify_search_filter_user_management():
    assert_that(USER_MANAGEMENT_PAGE.searched_user_is_displayed('pm_only'), contains_string("pm_only"))


# LQ-12783
@when('the user clicks Driver ID of one driver')
def click_driver_id():
    USER_MANAGEMENT_PAGE.click_driver_id()


@then('Preview badge page appeared and three buttons "Cancel","Download Badge","Email Badge" displayed on the bottom')
def verify_lytx_badge_model():
    assert DASHBOARD_PAGE.lytx_logo_is_displayed_old_ui() is True
    assert USER_MANAGEMENT_PAGE.get_cancel_button_text() == "Cancel"
    assert USER_MANAGEMENT_PAGE.get_download_badge_button_text() == "Download Badge"
    assert USER_MANAGEMENT_PAGE.get_email_badge_button_text() == "Email Badge"
    USER_MANAGEMENT_PAGE.click_cancel_button()


# LQ-2593
@given('the "Program Manager" user is in the Add User Page')
def go_to_add_user_page():
    USER_MANAGEMENT_PAGE.click_add_user()


@when('the user adds one driver role')
def add_driver_role():
    ADD_USER_PAGE.add_user_title_is_displayed()
    ADD_USER_PAGE.click_group()
    ADD_USER_PAGE.search_group(AUD.group)
    ADD_USER_PAGE.select_group()
    ADD_USER_PAGE.click_group_done()
    ADD_USER_PAGE.click_select_role()
    ADD_USER_PAGE.click_driver_role()


@then('the LYTX BADGE section will display a Lytx icon without QR code and a message '
      'on the right: "Will be created once the user is added."')
def verify_lytx_badge_message():
    assert ADD_USER_PAGE.get_lytx_badge_message() == "Will be created once user is added."
    ADD_USER_PAGE.click_cancel_button()


# CODE-2045
@when('the user add firstname, lastname, select group, role as driver and click on create button')
def add_driver_user():
    USER_MANAGEMENT_PAGE.click_add_user()
    ADD_USER_PAGE.add_user_title_is_displayed()
    global randriver
    randriver = AddUserPage(BasePage)
    randriver.get_random_name(4)
    ADD_USER_PAGE.add_first_name(randriver.random_name)
    ADD_USER_PAGE.add_last_name(randriver.random_name)
    ADD_USER_PAGE.add_email_address(randriver.random_name + "." + randriver.random_name + "@gmail.com")
    ADD_USER_PAGE.click_group()
    ADD_USER_PAGE.search_group(AUD.group)
    ADD_USER_PAGE.select_group()
    ADD_USER_PAGE.click_group_done()
    ADD_USER_PAGE.click_select_role()
    ADD_USER_PAGE.click_driver_role()
    ADD_USER_PAGE.click_create_user()


@then('the driver user is added successfully and qr_code is displayed')
def verify_lytx_badge_model():
    assert DASHBOARD_PAGE.lytx_logo_is_displayed_old_ui() is True
    assert USER_MANAGEMENT_PAGE.get_cancel_button_text() == "Cancel"
    assert USER_MANAGEMENT_PAGE.qr_code_is_displayed() is True
    USER_MANAGEMENT_PAGE.click_cancel_button()


# LQ-253
@when('the user clicks on "Add User" & the user enters required fields: "First Name", "Last Name", '
      '"EmployeeID", "Email", "Cell Phone", "Group" and "Role" on the "Info" tab & the user clicks "Create User"')
def add_user_details_user_management():
    USER_MANAGEMENT_PAGE.click_add_user()
    ADD_USER_PAGE.add_user_title_is_displayed()
    global tabn
    tabn = AddUserPage(BasePage)
    tabn.get_random_string()
    tabn.get_random_name(6)
    tabn.get_random_with_N_digits(10)
    ADD_USER_PAGE.add_first_name(tabn.random_name)
    ADD_USER_PAGE.add_last_name(tabn.random_name)
    ADD_USER_PAGE.add_employee_id(tabn.random_digit)
    ADD_USER_PAGE.add_email_address(tabn.random_name + "." + tabn.random_name + "@gmail.com")
    ADD_USER_PAGE.add_cell_phone()
    ADD_USER_PAGE.click_login_enabled("enabled")
    ADD_USER_PAGE.add_user_name("autobots" + tabn.random_name)
    ADD_USER_PAGE.add_password('Login123!')
    ADD_USER_PAGE.click_group()
    ADD_USER_PAGE.search_group(AUD.group)
    ADD_USER_PAGE.select_group()
    ADD_USER_PAGE.click_group_done()
    ADD_USER_PAGE.click_select_role()
    ADD_USER_PAGE.click_coach_role()
    ADD_USER_PAGE.click_create_user()
    if USER_MANAGEMENT_PAGE.qr_code_is_displayed() is True:
        USER_MANAGEMENT_PAGE.click_cancel_button()


@then('the user is added')
def verify_add_user_user_management():
    USER_MANAGEMENT_PAGE.click_clear_search_button()
    USER_MANAGEMENT_PAGE.search_name_filter(tabn.random_name)
    assert_that(USER_MANAGEMENT_PAGE.get_first_user_text(tabn.random_name), contains_string(tabn.random_name))


# LQ-257
@when('the user checks some available users & And the user clicks "Edit Group" & the user selects '
      'a group & the user selects a role & the user clicks Apply')
def batch_edit_group_user_user_management():
    USER_MANAGEMENT_PAGE.check_first_user()
    USER_MANAGEMENT_PAGE.click_edit_group_button()
    USER_MANAGEMENT_PAGE.click_group_filter_on_edit_group_dialog()
    USER_MANAGEMENT_PAGE.search_group_on_edit_group_dialog(AUD.group)
    USER_MANAGEMENT_PAGE.select_searched_group_on_edit_group_dialog()
    USER_MANAGEMENT_PAGE.click_done_on_edit_group_dialog()
    USER_MANAGEMENT_PAGE.click_role_filter_on_edit_group_dialog()
    USER_MANAGEMENT_PAGE.select_driver_role_on_edit_group_dialog()
    USER_MANAGEMENT_PAGE.click_apply_on_edit_group_dialog()


@then('the new role-group is added to the selected users')
def verify_edit_group_role_user_management():
    assert_that(USER_MANAGEMENT_PAGE.get_user_group_label(), contains_string(AUD.group))


# LQ-254
@given('the "Program Manager" user is in the Edit User page')
def navigate_to_edit_other_user_page():
    USER_MANAGEMENT_PAGE.search_name_filter(tabn.random_name)
    USER_MANAGEMENT_PAGE.click_expected_user(tabn.random_name)


@when('the user clicks on the name of a user & the user changes "First Name" on Edit '
      'User page & the user clicks Save Changes')
def edit_user_user_management():
    EDIT_USER_PAGE.wait_for_edit_user_page()
    EDIT_USER_PAGE.click_first_name()
    EDIT_USER_PAGE.clear_first_name()
    EDIT_USER_PAGE.edit_first_name(AUD.updated_username)
    EDIT_USER_PAGE.click_save_changes()


@then('the First Name of the edited user is updated')
def verify_edit_user_user_management():
    USER_MANAGEMENT_PAGE.search_name_filter(tabn.random_name)
    assert_that(USER_MANAGEMENT_PAGE.get_first_user_text(AUD.updated_username), contains_string(AUD.updated_username))


@given('the "Program Manager" user is in the Edit self page')
def navigate_to_edit_self_page():
    USER_MANAGEMENT_PAGE.click_clear_search_button()
    USER_MANAGEMENT_PAGE.search_name_filter(AUD.pm_only_user_name)
    USER_MANAGEMENT_PAGE.click_expected_user(AUD.pm_only_user_name)


@when('the user adds a notification on the "Notification" tab & the user adds a report on '
      'the "Report" tab & the user clicks Save Changes')
def edit_notification_report_user_management():
    EDIT_USER_PAGE.wait_for_edit_user_page()
    EDIT_USER_PAGE.click_notification_tab()

    # Clear data - Delete the notifications if already present
    if EDIT_USER_PAGE.delete_notifications_button_displayed() is True:
        EDIT_USER_PAGE.click_delete_notifications()

    # Steps to add notification and save changes
    EDIT_USER_PAGE.click_notification_tab()
    EDIT_USER_PAGE.click_add_notification()
    EDIT_USER_PAGE.click_notification_type()
    EDIT_USER_PAGE.select_event_status()
    EDIT_USER_PAGE.click_status_tab()
    EDIT_USER_PAGE.select_f2f_status()
    EDIT_USER_PAGE.click_arrow_tab()
    EDIT_USER_PAGE.conditions_group_tab()
    EDIT_USER_PAGE.search_group_condition(AUD.group)
    EDIT_USER_PAGE.select_group_dropdown()
    EDIT_USER_PAGE.done_group_button()
    # Clear data - Delete the reports if already present
    EDIT_USER_PAGE.click_reports_tab()
    if EDIT_USER_PAGE.delete_reports_button_displayed() is True:
        EDIT_USER_PAGE.click_delete_reports()

    # Steps to add reports and save changes
    EDIT_USER_PAGE.click_add_subscription()
    EDIT_USER_PAGE.click_select_report()
    EDIT_USER_PAGE.select_driving_summary()
    EDIT_USER_PAGE.click_save_changes()


@then('the notification and report are added for the user & the edited user receives the subscribed '
      'report at the selected date time')
def verify_edit_notifications_reports_user_management():
    USER_MANAGEMENT_PAGE.click_expected_user(AUD.pm_only_user_name)
    EDIT_USER_PAGE.wait_for_edit_user_page()
    EDIT_USER_PAGE.click_notification_tab()
    assert_that(EDIT_USER_PAGE.get_notification_text(), contains_string("Notifications (1)"))
    assert_that(EDIT_USER_PAGE.get_report_text(), contains_string("Reports (1)"))
    EDIT_USER_PAGE.back_to_previous_page()


@when('the user clicks on the "Delete user" & the user clicks "Confirm" button on the popup message')
def delete_user_user_management():
    USER_MANAGEMENT_PAGE.click_clear_search_button()
    USER_MANAGEMENT_PAGE.search_name_filter(tabn.random_name)
    USER_MANAGEMENT_PAGE.click_expected_user(tabn.random_name)
    EDIT_USER_PAGE.wait_for_edit_user_page()
    EDIT_USER_PAGE.click_delete_name()
    EDIT_USER_PAGE.confirm_delete_name()


@then('the selected user is deleted')
def verify_delete_user_user_management():
    USER_MANAGEMENT_PAGE.click_reset_button()
    USER_MANAGEMENT_PAGE.click_status_filter()
    USER_MANAGEMENT_PAGE.select_delete_status()
    assert USER_MANAGEMENT_PAGE.get_first_user_status() == "Deleted"


# LQ-259
@when('the user checks some available users & the user clicks "Change Status" & the user '
      'selects "Inactive" & the user clicks Apply')
def batch_edit_inactive_status_user_management():
    USER_MANAGEMENT_PAGE.clear_status_filter()
    USER_MANAGEMENT_PAGE.click_reset_button()
    USER_MANAGEMENT_PAGE.click_status_filter()
    USER_MANAGEMENT_PAGE.select_delete_status()
    USER_MANAGEMENT_PAGE.search_name_filter(tabn.random_name)
    USER_MANAGEMENT_PAGE.check_first_user()
    USER_MANAGEMENT_PAGE.click_more_action()
    USER_MANAGEMENT_PAGE.click_change_status_button()
    USER_MANAGEMENT_PAGE.select_inactive_status()
    USER_MANAGEMENT_PAGE.click_apply_set_user_status()


@then('the status of selected users is updated to Inactive')
def verify_inactive_status_user_management():
    assert USER_MANAGEMENT_PAGE.get_first_user_status() == "Inactive"


# LQ-261
@when('the user checks some available users & the user clicks "Edit Login" & the user '
      'selects "Enable" & the user clicks Apply')
def edit_enable_login_user_management():
    USER_MANAGEMENT_PAGE.clear_status_filter()
    USER_MANAGEMENT_PAGE.search_name_filter(AUD.pm_only_user_name)
    USER_MANAGEMENT_PAGE.check_first_user()
    USER_MANAGEMENT_PAGE.click_more_action()
    USER_MANAGEMENT_PAGE.click_change_status_button()
    USER_MANAGEMENT_PAGE.click_apply_set_user_status()
    USER_MANAGEMENT_PAGE.click_status_filter()
    USER_MANAGEMENT_PAGE.click_active_filter()
    USER_MANAGEMENT_PAGE.check_first_user()
    USER_MANAGEMENT_PAGE.click_more_action()
    USER_MANAGEMENT_PAGE.click_edit_login()
    USER_MANAGEMENT_PAGE.click_apply_on_edit_login()


@then('the login status of selected users is updated to Enable')
def verify_enabled_login_user_management():
    assert USER_MANAGEMENT_PAGE.get_filtered_user_login() == "Enabled"


# LQ-248
@when('the user clicks humanoid icon & the user clicks MY ACCOUNT')
def open_info_tab_my_account():
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_my_account_button()


@then('the user info is displayed in Info tab with: "FIRST NAME", "LAST NAME", "EMPLOYEE ID" & the contact Information '
      'is displayed in contact Info tab with: "EMAIL ADDRESS", "CELL PHONE" &  the group role assignment is displayed '
      'in Info tab with: "GROUP ROLE ASSIGNMENT" & the username and password is displayed in Info tab with: "USERNAME",'
      '"PASSWORD" and Lytx Badge')
def verify_my_account_info():
    assert MY_ACCOUNT_PAGE.my_account_title_is_displayed() is True
    assert MY_ACCOUNT_PAGE.get_first_name_text() == "FIRST NAME"
    assert MY_ACCOUNT_PAGE.get_last_name_text() == "LAST NAME"
    assert MY_ACCOUNT_PAGE.get_employee_id_text() == "EMPLOYEE ID"
    assert MY_ACCOUNT_PAGE.get_contact_information_text() == "Contact Information"
    assert MY_ACCOUNT_PAGE.get_email_address_text() == "EMAIL ADDRESS"
    assert MY_ACCOUNT_PAGE.get_cellphone_text() == "CELL PHONE"
    assert MY_ACCOUNT_PAGE.get_lytx_badge_text() == "Lytx Badge"
    assert MY_ACCOUNT_PAGE.get_group_role_assignment_text() == "Group Role Assignment"
    assert MY_ACCOUNT_PAGE.get_login_text() == "Login"
    assert MY_ACCOUNT_PAGE.get_username_text() == "USERNAME"
    assert MY_ACCOUNT_PAGE.get_password_text() == "PASSWORD"


@when(
    'the user clicks the "Edit" icon on contact section & the user edits the email address with valid value &  '
    'the user clicks "Save" button')
def edit_email_my_account():
    MY_ACCOUNT_PAGE.click_edit_email_button()
    MY_ACCOUNT_PAGE.clear_email_address()
    MY_ACCOUNT_PAGE.edit_email_address(tabn.random_name + "." + tabn.random_name + "@gmail.com")
    MY_ACCOUNT_PAGE.click_save_edit_email_button()


@then('the info is updated')
def verify_updated_email_address():
    assert_that(MY_ACCOUNT_PAGE.get_updated_email_address_text(),
                contains_string(tabn.random_name + '.' + tabn.random_name + "@gmail.com"))


# LQ-250
@when('the user opens reports tab in My account page')
def open_reports_tab_my_account():
    MY_ACCOUNT_PAGE.click_report_tab()


@then('reports are displayed')
def verify_reports_my_account():
    assert_that(MY_ACCOUNT_PAGE.get_report_subscription_text(), contains_string("Driving Summary"))


# LQ-249
@when('the user navigates to notification tab in my account page')
def open_notification_tab_my_account():
    MY_ACCOUNT_PAGE.click_notification_tab()


@then('the subscribed notifications are listed')
def verify_notification_my_account():
    assert MY_ACCOUNT_PAGE.notification_subscription_displayed() is True

    # Clear test data - Unsubscribing from alerts and deleting the reports for next run
    DASHBOARD_PAGE.click_admin_tab()
    USER_MANAGEMENT_PAGE.user_management_label_is_displayed()
    USER_MANAGEMENT_PAGE.click_clear_search_button()
    USER_MANAGEMENT_PAGE.clear_status_filter()
    USER_MANAGEMENT_PAGE.search_name_filter(AUD.pm_only_user_name)
    USER_MANAGEMENT_PAGE.click_expected_user(AUD.pm_only_user_name)
    EDIT_USER_PAGE.wait_for_edit_user_page()
    EDIT_USER_PAGE.click_notification_tab()
    if EDIT_USER_PAGE.delete_notifications_button_displayed() is True:
        EDIT_USER_PAGE.click_delete_notifications()
    EDIT_USER_PAGE.click_reports_tab()
    EDIT_USER_PAGE.click_delete_reports()
    EDIT_USER_PAGE.click_save_changes()


# LQ-258
@when('the user checks some available users & the user clicks "Delete Users" & the user clicks "Confirm"')
def batch_delete_users_user_management():
    USER_MANAGEMENT_PAGE.user_management_label_is_displayed()
    USER_MANAGEMENT_PAGE.click_clear_search_button()
    USER_MANAGEMENT_PAGE.clear_status_filter()
    user_list = [tabn.random_name, randriver.random_name]
    for name in user_list:
        USER_MANAGEMENT_PAGE.search_name_filter(name)
        USER_MANAGEMENT_PAGE.check_first_user()
        if USER_MANAGEMENT_PAGE.get_first_user_status() != "Deleted":
            USER_MANAGEMENT_PAGE.click_batch_delete_user()
            USER_MANAGEMENT_PAGE.click_confirm_button()


@then('the status of selected users is updated to deleted')
def verify_batch_delete_user_management():
    assert USER_MANAGEMENT_PAGE.get_first_user_status() == "Deleted"


@given('internal FA user login to the application')
def internal_fa_user_login():
    LOGIN_PAGE.navigate_to(DC_URL)
    LOGIN_PAGE.enter_username(AUD.FA_internal_user)
    LOGIN_PAGE.enter_password(AUD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_company()
    LOGIN_PAGE.click_select_company_button()


@when('the user click on "Change View History" in the header of User Management Page')
def click_change_view_history_user_management():
    DASHBOARD_PAGE.click_admin_tab()
    USER_MANAGEMENT_PAGE.click_change_view_history()


@then('the user should be able to see the table columns: "USER AFFECTED", "ACTION", "ACTION DETAILS","EDITOR", "ACTION DATE"')
def verify_user_audit_log_table_columns():
    assert USER_MANAGEMENT_PAGE.get_user_affected_label() == "USER AFFECTED"
    assert USER_MANAGEMENT_PAGE.get_action_label() == "ACTION"
    assert USER_MANAGEMENT_PAGE.get_action_details_label() == "ACTION DETAILS"
    assert USER_MANAGEMENT_PAGE.get_editor_label() == "EDITOR"
    assert USER_MANAGEMENT_PAGE.get_action_date_label() == "ACTION DATE"


@then('the user should see the User Audit log count along with the filters "Search User Affected" and "Select Action(s)" in the header')
def verify_user_audit_log_filters_and_count():
    assert USER_MANAGEMENT_PAGE.user_audit_log_header_is_displayed() is True
    assert USER_MANAGEMENT_PAGE.search_user_affected_filter_is_displayed() is True
    assert USER_MANAGEMENT_PAGE.action_type_dropdown_is_displayed() is True
    assert USER_MANAGEMENT_PAGE.date_filter_is_displayed() is True
    assert USER_MANAGEMENT_PAGE.reset_button_audit_page_is_displayed() is True


@then('the user should see the buttons "Download Log"')
def verify_download_log_button_in_user_audit_log():
    assert USER_MANAGEMENT_PAGE.download_log_is_displayed() is True



@when('user input a valid value in the "Search User Affected" field')
def search_user_affected_in_view_history():
    global AFFECTED_USER
    AFFECTED_USER = USER_MANAGEMENT_PAGE.get_first_user_affected_text()
    USER_MANAGEMENT_PAGE.search_user_affected(AFFECTED_USER)


@then('the searched user should be able to see in the User Audit Log')
def verify_searched_user_in_view_history():
    assert_that(USER_MANAGEMENT_PAGE.get_first_user_affected_text(), contains_string(AFFECTED_USER))


@when('user input an invalid value in the "Search User Affected" field')
def search_invalid_user_affected_in_view_history():
    USER_MANAGEMENT_PAGE.search_user_affected('invalid user aaaa')


@then('it should display a message "No audit logs available for the selected user/date range" with empty table')
def verify_no_audit_logs_message_in_view_history():
    assert USER_MANAGEMENT_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected user/date range"


@when('user select an action type from "Action Type" dropdown')
def select_action_type_in_view_history():
    USER_MANAGEMENT_PAGE.click_reset_in_audit_page()
    USER_MANAGEMENT_PAGE.click_action_type_dropdown()
    USER_MANAGEMENT_PAGE.select_action_type()


@then('the user should be able to see the logs based on selected action type in the User Audit Log')
def verify_action_type_in_view_history():
    assert_that(USER_MANAGEMENT_PAGE.get_action_type_text(), contains_string("Added"))


@when('the user select a date range from "Date Range" dropdown')
def select_date_range_in_view_history():
    USER_MANAGEMENT_PAGE.click_date_range_dropdown()
    USER_MANAGEMENT_PAGE.select_date_range_today()



@then('the user should be able to see the logs based on selected date range in the User Audit Log')
def verify_date_range_in_view_history():
    assert_that(USER_MANAGEMENT_PAGE.get_action_date(), contains_string(USER_MANAGEMENT_PAGE.get_time_today()))


@when('the user click on the "Close" button for the User Audit Log tab')
def close_user_audit_log_tab():
    USER_MANAGEMENT_PAGE.click_close_user_audit_log()


@then('the user Audit Log tab should be closed successfully')
def verify_close_user_audit_log_tab():
    assert USER_MANAGEMENT_PAGE.user_audit_log_tab_displayed() is False


@then('verify it should be redirected back to the User Management page')
def verify_redirected_back_to_user_management_page():
    assert USER_MANAGEMENT_PAGE.user_management_label_is_displayed() is True


@when('the user clicks on the "View Change History" icon in the header')
def click_view_change_history_vehicle_management():
    USER_MANAGEMENT_PAGE.click_change_view_history()


@when('the user clicks "Download Log" in the User audit log tab')
def click_download_log_vehicle_management():
    USER_MANAGEMENT_PAGE.click_download_log()


@then('it should download the audit logs in the .CSV file format')
def verify_downloaded_audit_logs_vehicle_management():
    file_name = USER_MANAGEMENT_PAGE.get_audit_log_file_name()
    USER_MANAGEMENT_PAGE.wait_for_file_downloaded(file_name)
    # assert USER_MANAGEMENT_PAGE.check_file_exist(file_name) is True


@when('search the specific name of any User in "Search User Affected" filter')
def search_user_affected_in_view_history_device_management():
    global AFFECTED_USER
    USER_MANAGEMENT_PAGE.click_reset_in_audit_page()
    AFFECTED_USER = USER_MANAGEMENT_PAGE.get_first_user_affected_text()
    USER_MANAGEMENT_PAGE.search_user_affected(AFFECTED_USER)


@then('the "Download Log" in the User audit log tab is displayed')
def click_download_log_device_management():
    assert USER_MANAGEMENT_PAGE.download_log_is_displayed()


@when('the user select any date from the calendar and select any Action from the dropdown filter')
def filter_date_action_type_in_view_history_vehicle_management():
    USER_MANAGEMENT_PAGE.click_date_range_dropdown()
    USER_MANAGEMENT_PAGE.select_date_range_today()
    USER_MANAGEMENT_PAGE.click_action_type_dropdown()
    USER_MANAGEMENT_PAGE.select_imported()


@then('the "Download Log" functionality should be disabled')
def verify_download_log_disabled_vehicle_management():
    assert USER_MANAGEMENT_PAGE.download_log_disabled() is True


# LQ-252
@when('the user selects multiple groups from the "Select Group(s)" filter')
def apply_group_filter_user_management():
    USER_MANAGEMENT_PAGE.click_reset_button()
    USER_MANAGEMENT_PAGE.click_select_group_filter()
    USER_MANAGEMENT_PAGE.search_group_filter(AUD.Automation_group1)
    USER_MANAGEMENT_PAGE.select_searched_group()
    USER_MANAGEMENT_PAGE.click_done_group_filter()


@then('the users belong to the selected groups are listed')
def verify_group_filter_user_management():
    assert USER_MANAGEMENT_PAGE.get_user_count() == '7'
    for i in range(1, 8):
        assert_that(USER_MANAGEMENT_PAGE.get_users_groups_label(i),contains_string(getattr(AUD, f"Automation_group{i}")))




