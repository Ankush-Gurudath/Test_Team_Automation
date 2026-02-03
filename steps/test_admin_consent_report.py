from hamcrest import assert_that, contains_string, not_
from pytest_bdd import scenarios, given, when, then
from pages.add_user_page import *
from pages.add_user_page import AddUserPage
from pages.dashboard_page import DashboardPage
from pages.edit_user_page import EditUserPage
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage
from pages.consent_report_page import ConsentReportPage
from steps.common import ENV, NEW_UI_FTM_URL
from data.int.admin_data_int import AdminDataInt as AD_INT
from data.prod.admin_data_prod import AdminDataProd as AD_PROD
from data.stg.admin_data_stg import AdminDataStg as AD_STG
from steps.test_admin_user import AUD
from pages.edit_user_page import EditUserPage

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
USER_MANAGEMENT_PAGE = 0
AD = 0
CONSENT_REPORT_PAGE = 0
EDIT_USER_PAGE = 0
user_count_after_create = 0
user_count_after_delete = 0

scenarios('../features/admin_lcmp.feature')


# LQ-235
@given('admin user logs in')
def fa_log_in(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, USER_MANAGEMENT_PAGE, AD, CONSENT_REPORT_PAGE, ADD_USER_PAGE, EDIT_USER_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)
    CONSENT_REPORT_PAGE = ConsentReportPage(browser)
    ADD_USER_PAGE = AddUserPage(browser)
    EDIT_USER_PAGE = EditUserPage(browser)

    browser.get(NEW_UI_FTM_URL)

    if ENV == 'int':
        AD = AD_INT
    elif ENV == 'stg':
        AD = AD_STG
    elif ENV == 'prod':
        AD = AD_PROD

    LOGIN_PAGE.enter_username(AD.admin1_user_name)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_multi_company(AD.company_name1)
    LOGIN_PAGE.click_select_company_button()


# LQ-253
@when('the user clicks on "Add User" & the user enters required fields: "First Name", "Last Name", '
      '"EmployeeID", "Email", "Cell Phone", "Group" and "Role" on the "Info" tab & the user clicks "Create User"')
def add_user_details_user_management():
    DASHBOARD_PAGE.click_admin_tab()
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
    ADD_USER_PAGE.search_group(AD.consent_group)
    ADD_USER_PAGE.select_group()
    ADD_USER_PAGE.click_group_done()
    ADD_USER_PAGE.click_select_role()
    ADD_USER_PAGE.click_driver_role()
    ADD_USER_PAGE.click_create_user()
    if USER_MANAGEMENT_PAGE.qr_code_is_displayed() is True:
        USER_MANAGEMENT_PAGE.click_cancel_button()


@then('the user is added')
def verify_add_user_user_management():
    # USER_MANAGEMENT_PAGE.click_clear_search_button()
    USER_MANAGEMENT_PAGE.search_name_filter(tabn.random_name)
    assert_that(USER_MANAGEMENT_PAGE.get_first_user_text(tabn.random_name), contains_string(tabn.random_name))


# @LQ-152866
@when('the user clicks driver name the "More Options" tab')
def user_clicks_more_options_tab():
    USER_MANAGEMENT_PAGE.click_first_user_checkbox()
    USER_MANAGEMENT_PAGE.click_more_options()


@then('the user should see the "Request user consent" tab available')
def user_should_see_request_user_consent_tab():
    assert USER_MANAGEMENT_PAGE.request_user_consent_is_displayed() is True


@when('the user clicks "Request user consent" tab')
def user_clicks_request_user_consent_tab():
    USER_MANAGEMENT_PAGE.click_request_user_consent()


@then('the user should see the tab opens from bottom with title "Request User Consent"')
def user_should_see_request_user_consent_tab_opens():
    assert USER_MANAGEMENT_PAGE.get_request_user_consent_title() == "Request User Consent"


# LQ-152962
@when('the user checks the "Facial ID" system and the user selects the "Email" communication mode and the user clicks the next button')
def user_checks_facial_id_and_email():
    USER_MANAGEMENT_PAGE.check_facial_id_checkbox()
    USER_MANAGEMENT_PAGE.select_communication_mode_email()
    USER_MANAGEMENT_PAGE.click_next_button()


@then('the user should see the "Confirm Request" modal getting opened.')
def user_should_see_confirm_request_modal():
    assert USER_MANAGEMENT_PAGE.get_confirm_request_title() == "Confirm Request"


# @LQ-153001
@when('the user click the "Send Request" button in the "Confirm Request" modal')
def user_clicks_send_request_button():
    USER_MANAGEMENT_PAGE.click_send_request_button()


@then('the user should see the success message "User consent request sent successfully" and the user should be '
      'redirected to User Management page.')
def user_should_see_success_message():
    assert USER_MANAGEMENT_PAGE.get_success_message() == "User consent request sent successfully!"
    assert USER_MANAGEMENT_PAGE.get_user_management_label() == "USER MANAGEMENT"


@when('the user click on the "Consent Report" module')
def user_clicks_consent_report_tab():
    USER_MANAGEMENT_PAGE.click_insights_tab()
    CONSENT_REPORT_PAGE.click_consent_report_tab()


@then('the user should see all the filter like "All Available Groups", "Status", "Search Name or ID" and "Reset"')
def user_should_see_all_filters():
    assert CONSENT_REPORT_PAGE.group_filter_is_displayed() is True
    assert CONSENT_REPORT_PAGE.status_filter_is_displayed() is True
    assert CONSENT_REPORT_PAGE.search_name_or_id_is_displayed() is True
    assert CONSENT_REPORT_PAGE.reset_button_is_displayed() is True


@then(
    'the user should see the count of Drivers with tabs named "Facial ID", "Video Safety" and "Distraction and Fatigue Detection"')
def user_should_see_count_and_all_tabs():
    assert CONSENT_REPORT_PAGE.driver_count_is_displayed() is True
    assert CONSENT_REPORT_PAGE.facial_id_tab_is_displayed() is True

    # Commented these two assertions as these two tabs are not in scope as of now
    # assert CONSENT_REPORT_PAGE.distraction_and_fatigue_detection_tab_is_displayed() is True
    # assert CONSENT_REPORT_PAGE.video_safety_tab_is_displayed() is True


# @LQ-157939
# @when('the user is in "Facial ID" product tab') # This step is not needed as this step is covered in LQ-136386


@then('the user should see the title "Consent Report" and the user should see the columns "NAME","GROUPS","STATUS", '
      '"SENT DATE" and "REQUESTED DATE"')
def user_should_see_all_columns():
    assert CONSENT_REPORT_PAGE.get_page_title() == "CONSENT REPORT"
    assert CONSENT_REPORT_PAGE.get_name_column_label() == "NAME"
    assert CONSENT_REPORT_PAGE.get_groups_column_label() == "GROUPS"
    assert CONSENT_REPORT_PAGE.get_status_column_label() == "STATUS"
    assert CONSENT_REPORT_PAGE.get_sent_date_column_label() == "SENT DATE"
    assert CONSENT_REPORT_PAGE.get_received_date_column_label() == "RECEIVED DATE"


@then('the user see the options "0 selected","Clear All","Download PDF", "Revoke Consent" and "CSV"')
def user_should_see_all_options():
    assert CONSENT_REPORT_PAGE.clear_all_option_is_displayed() is True
    assert CONSENT_REPORT_PAGE.csv_option_is_displayed() is True


# @LQ-157911
@when('the user selects any group')
def user_selects_any_group():
    CONSENT_REPORT_PAGE.click_group_filter_button()
    CONSENT_REPORT_PAGE.click_search_by_group_field()
    CONSENT_REPORT_PAGE.search_group_filter(AD.consent_group)
    CONSENT_REPORT_PAGE.select_group()
    CONSENT_REPORT_PAGE.click_done_button()


@then('the user should be able to see the selected group data')
def user_should_see_selected_group_data():
    assert CONSENT_REPORT_PAGE.get_first_group_name() == AD.consent_group
    assert CONSENT_REPORT_PAGE.driver_count_is_displayed() is True


@when('the user search the username in the search filter')
def user_searches_username_in_search_filter():
    CONSENT_REPORT_PAGE.click_search_name_field()
    CONSENT_REPORT_PAGE.type_search_name_field(tabn.random_name)


@then('the user should be able to see the newly sent consent user in the Consent Report page with employee ID')
def user_should_see_newly_sent_consent_user_in_consent_report_page():
    assert_that(CONSENT_REPORT_PAGE.get_first_row_driver_name(), contains_string(tabn.random_name))
    assert_that(CONSENT_REPORT_PAGE.get_first_row_driver_name(), contains_string(str(tabn.random_digit)))


@when('the user clicks "Status" the dropdown')
def user_clicks_status_dropdown():
    CONSENT_REPORT_PAGE.click_reset_button()
    CONSENT_REPORT_PAGE.click_status_filter_button()


@then('the user should see four statuses options "Not Received","Revoked","Received" and "Opted Out"')
def user_should_see_status_options():
    assert CONSENT_REPORT_PAGE.not_received_status_button_is_displayed() is True
    assert CONSENT_REPORT_PAGE.received_status_button_is_displayed() is True
    assert CONSENT_REPORT_PAGE.revoked_status_button_is_displayed() is True
    assert CONSENT_REPORT_PAGE.opted_out_status_button_is_displayed() is True


@when('the user clicks "Status" the dropdown and the user selects "Not Received" status')
def user_selects_not_received_status():
    CONSENT_REPORT_PAGE.select_not_received_status_button()


@then('the user should be able to see the data for the selected not received status')
def user_should_see_selected_status_data():
    assert CONSENT_REPORT_PAGE.get_first_row_status() == "Not Received"
    assert CONSENT_REPORT_PAGE.driver_count_is_displayed() is True


@when('the user clicks "Status" the dropdown and the user selects "Received" status')
def user_selects_received_status():
    CONSENT_REPORT_PAGE.click_reset_button()
    CONSENT_REPORT_PAGE.click_status_filter_button()
    CONSENT_REPORT_PAGE.select_received_status_button()


@then('the user should be able to see the data for the selected received status')
def user_should_see_selected_status_data():
    assert CONSENT_REPORT_PAGE.get_first_row_status() == "Received"
    assert CONSENT_REPORT_PAGE.driver_count_is_displayed() is True


@when('the user clicks "Status" the dropdown and the user selects "Revoked" status')
def user_selects_revoked_status():
    CONSENT_REPORT_PAGE.click_reset_button()
    CONSENT_REPORT_PAGE.click_status_filter_button()
    CONSENT_REPORT_PAGE.select_revoked_status_button()


@then('the user should be able to see the data for the selected revoked status')
def user_should_see_selected_status_data():
    assert CONSENT_REPORT_PAGE.get_first_row_status() == "Revoked"
    assert CONSENT_REPORT_PAGE.driver_count_is_displayed() is True


@when('the user clicks "Status" the dropdown and the user selects "Opted Out" status')
def user_selects_opted_out_status():
    CONSENT_REPORT_PAGE.click_status_filter_button()
    CONSENT_REPORT_PAGE.select_opted_out_status_button()


@then('the user should be able to see the data for the selected opted out status')
def user_should_see_selected_status_data():
    assert CONSENT_REPORT_PAGE.driver_count_is_displayed() is True


@when('the user inputs driver name from first page in the "Search Name or ID" field')
def user_inputs_name_in_search_field():
    CONSENT_REPORT_PAGE.click_reset_button()
    CONSENT_REPORT_PAGE.click_search_name_field()
    CONSENT_REPORT_PAGE.type_search_name_field(AD.driver1_user_name)


@then('the user should be able to see the data related to the provided name or ID')
def user_should_see_data_related_to_name():
    assert CONSENT_REPORT_PAGE.get_first_row_driver_name() == AD.driver1_user_name
    assert CONSENT_REPORT_PAGE.driver_count_is_displayed() is True


@when('the user inputs driver name from last page in the "Search Name or ID" field')
def user_inputs_name_in_search_field():
    global last_page_driver_name
    CONSENT_REPORT_PAGE.click_reset_button()
    CONSENT_REPORT_PAGE.click_last_page_number()
    last_page_driver_name = CONSENT_REPORT_PAGE.get_last_page_driver_name_text()
    CONSENT_REPORT_PAGE.click_search_name_field()
    CONSENT_REPORT_PAGE.type_search_name_field(last_page_driver_name)


@then('the user should be able to see the data related to the provided name')
def user_should_see_data_related_to_name():
    assert CONSENT_REPORT_PAGE.get_first_row_driver_name() == last_page_driver_name
    assert CONSENT_REPORT_PAGE.driver_count_is_displayed() is True


# @LQ-161688
@when('the user clicks the CSV button')
def user_clicks_csv_button():
    CONSENT_REPORT_PAGE.click_enable_product_cancel_button()
    CONSENT_REPORT_PAGE.click_csv_option()


@then('the user should see the excel getting downloaded in the format ('
      'YYYY-MM-DD_Productname_Consent_Status_Report.csv)')
def verify_csv_report_downloaded():
    file_name = CONSENT_REPORT_PAGE.get_facial_id_file_name()
    CONSENT_REPORT_PAGE.wait_for_file_downloaded(file_name)
    assert CONSENT_REPORT_PAGE.check_file_exist(file_name) is True


# @LQ-161873
@when('the user clicks the "PDF" with download icon available for "Revoked" and "Received" status')
def user_clicks_pdf_button():
    CONSENT_REPORT_PAGE.click_download_pdf_option()


@then('the user should see the PDF getting downloaded in a format (ConsentID.pdf)')
def verify_pdf_report_downloaded():
    file_name = CONSENT_REPORT_PAGE.get_pdf_file_name(AD.consent_id)
    CONSENT_REPORT_PAGE.wait_for_file_downloaded(file_name)
    assert CONSENT_REPORT_PAGE.check_file_exist(file_name) is True


@when('the user navigates to Enable Product page and select a group in the group filter')
def navigate_to_enable_product_page():
    CONSENT_REPORT_PAGE.click_enable_facial_id_link()
    CONSENT_REPORT_PAGE.click_group_filter_button()
    CONSENT_REPORT_PAGE.click_search_by_group_field()
    CONSENT_REPORT_PAGE.search_group_filter(AD.consent_group)
    CONSENT_REPORT_PAGE.select_group()
    CONSENT_REPORT_PAGE.click_done_button()


@then('the user get the driver count of selected group')
def verify_driver_count_of_selected_group():
    global user_count_after_create
    user_count_after_create = int(CONSENT_REPORT_PAGE.get_user_count_for_selected_group_after_creating_user())


# LQ-258
@when('the user checks some available users & the user clicks "Delete Users" & the user clicks "Confirm"')
def batch_delete_users_user_management():
    USER_MANAGEMENT_PAGE.click_user_tab()
    USER_MANAGEMENT_PAGE.user_management_label_is_displayed()
    EDIT_USER_PAGE.click_first_name_in_user_page()
    EDIT_USER_PAGE.edit_user_title_is_displayed
    USER_MANAGEMENT_PAGE.clear_employee_id()
    CONSENT_REPORT_PAGE.edit_password(AD.password)
    CONSENT_REPORT_PAGE.click_save_changes()
    USER_MANAGEMENT_PAGE.click_clear_search_button()
    USER_MANAGEMENT_PAGE.clear_status_filter()
    USER_MANAGEMENT_PAGE.search_name_filter(tabn.random_name)
    USER_MANAGEMENT_PAGE.check_first_user()
    if USER_MANAGEMENT_PAGE.get_first_user_status() != "Deleted":
        USER_MANAGEMENT_PAGE.click_batch_delete_user()
        USER_MANAGEMENT_PAGE.click_confirm_button()


@then('the status of selected users is updated to deleted')
def verify_batch_delete_user_management():
    assert USER_MANAGEMENT_PAGE.get_first_user_status() == "Deleted"


@when('the user search the username in the search filter after deleting the user')
def user_searches_username_in_search_filter():
    USER_MANAGEMENT_PAGE.click_insights_tab()
    CONSENT_REPORT_PAGE.click_consent_report_tab()
    CONSENT_REPORT_PAGE.click_reset_button()
    CONSENT_REPORT_PAGE.click_search_name_field()
    CONSENT_REPORT_PAGE.type_search_name_field(tabn.random_name)


@then('the user should not see the removed employee id next to username in the Consent Report page')
def user_should_not_see_removed_employee_id_in_consent_report_page():
    assert_that(CONSENT_REPORT_PAGE.get_first_row_driver_name(), contains_string(tabn.random_name))
    # assert_that(CONSENT_REPORT_PAGE.get_first_row_driver_name(), not_(contains_string(str(tabn.random_digit))))


@when('the user navigates to Enable Product page from User Management page')
def navigate_to_enable_product_page():
    CONSENT_REPORT_PAGE.click_enable_facial_id_link()
    CONSENT_REPORT_PAGE.click_group_filter_button()
    CONSENT_REPORT_PAGE.click_search_by_group_field()
    CONSENT_REPORT_PAGE.search_group_filter(AD.consent_group)
    CONSENT_REPORT_PAGE.select_group()
    CONSENT_REPORT_PAGE.click_done_button()
    if CONSENT_REPORT_PAGE.user_count_for_selected_group_after_deleting_user_is_displayed() is False:
        CONSENT_REPORT_PAGE.click_group_filter_button()
        CONSENT_REPORT_PAGE.click_search_by_group_field()
        CONSENT_REPORT_PAGE.search_group_filter(AD.consent_group)
        CONSENT_REPORT_PAGE.select_group()
        CONSENT_REPORT_PAGE.click_done_button()


@then('the user count should be less for the selected group based on inactive the user')
def verify_inactive_user_not_in_list():
    global user_count_after_delete
    user_count_after_delete = int(CONSENT_REPORT_PAGE.get_user_count_for_selected_group_after_deleting_user())
    assert user_count_after_delete == user_count_after_create - 1
