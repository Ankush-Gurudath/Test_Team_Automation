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
from steps.common import ENV, NEW_UI_FTM_URL
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

scenarios('../features/admin_user_workflow.feature')


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
    browser.get(NEW_UI_FTM_URL)


@when('the user enters a newly created username/password and clicks the login button')
def login():
    LOGIN_PAGE.enter_username(AUD.autobots_full_access_username)
    LOGIN_PAGE.enter_password(AUD.password2)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()


@then('the user is successfully logged into the Driver Safety dashboard')
def verify_login():
    assert_that(DASHBOARD_PAGE.get_driver_safety_title(), IsEqualIgnoringCase("Driver Safety"))


# LQ-251
@when('the user clicks on Admin tab')
def navigate_to_user_management_page():
    DASHBOARD_PAGE.click_admin_tab()


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
    assert USER_MANAGEMENT_PAGE.get_roles_label() == "ROLES (GROUP)"
    assert USER_MANAGEMENT_PAGE.get_status_label() == "STATUS"
    assert USER_MANAGEMENT_PAGE.get_login_label() == "LOGIN"
    assert USER_MANAGEMENT_PAGE.get_user_name_label() == "USERNAME"


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


@then('the user is added')
def verify_add_user_user_management():
    USER_MANAGEMENT_PAGE.click_reset_button()
    USER_MANAGEMENT_PAGE.search_name_filter(tabn.random_name)
    assert_that(USER_MANAGEMENT_PAGE.get_first_user_text(tabn.random_name), contains_string(tabn.random_name))


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
    USER_MANAGEMENT_PAGE.search_name_filter(tabn.random_name)
    USER_MANAGEMENT_PAGE.click_expected_user(tabn.random_name)


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
    EDIT_USER_PAGE.select_insight_summary_report()
    EDIT_USER_PAGE.click_save_changes()


@then('the notification and report are added for the user & the edited user receives the subscribed '
      'report at the selected date time')
def verify_edit_notifications_reports_user_management():
    USER_MANAGEMENT_PAGE.click_expected_user(tabn.random_name)
    EDIT_USER_PAGE.wait_for_edit_user_page()
    EDIT_USER_PAGE.click_notification_tab()
    assert_that(EDIT_USER_PAGE.get_notification_text(), contains_string("Notifications (1)"))
    assert_that(EDIT_USER_PAGE.get_report_text(), contains_string("Reports (1)"))
    EDIT_USER_PAGE.back_to_previous_page()


@when('the user clicks on the "Delete user" & the user clicks "Confirm" button on the popup message')
def delete_user_user_management():
    USER_MANAGEMENT_PAGE.click_reset_button()
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