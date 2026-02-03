from hamcrest import assert_that, contains_string
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase
from pytest_bdd import scenarios, given, when, then, parsers
from selenium.common import TimeoutException

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.admin_groups_page import AdminGroupsPage
from steps.common import DC_URL, ENV, NEW_UI_FTM_URL
from data.prod.admin_data_prod import AdminDataProd as AD_PROD
from data.stg.admin_data_stg import AdminDataStg as AD_STG
from data.int.admin_data_int import AdminDataInt as AD_INT

scenarios('../features/admin_groups_new_ui_shell.feature')

ADMIN_GROUPS_PAGE = 0
LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
GROUP_COUNT_BEFORE_ADDING_GROUP = 0
SIBLING_GROUP = 0
AD = 0


@given('admin user logs in')
def pm_log_in(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, ADMIN_GROUPS_PAGE, AD

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    ADMIN_GROUPS_PAGE = AdminGroupsPage(browser)

    browser.get(NEW_UI_FTM_URL)

    if ENV == 'int':
        AD = AD_INT
    elif ENV == 'stg':
        AD = AD_STG
    elif ENV == 'PROD':
        AD = AD_PROD

    LOGIN_PAGE.enter_username(AD.fa_gm_user_name)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()


@when('user clicks groups tab')
def user_clicks_groups_tab():
    DASHBOARD_PAGE.click_admin_tab()
    ADMIN_GROUPS_PAGE.click_groups_tab()


@then('groups management page is displayed')
def groups_management_page_is_displayed():
    assert ADMIN_GROUPS_PAGE.group_management_page_is_displayed() is True


@then('the user should be able to see the group hierarchy with hyperlinks present for each group like "Devices","Vehicles","Events" and "Users"')
def user_should_be_able_to_see_group_hierarchy():
    assert ADMIN_GROUPS_PAGE.group_hierarchy_is_present() is True
    assert ADMIN_GROUPS_PAGE.group_card_details_is_present() is True


@then('the user should be able to see the groups count and "Search Groups" filter in the header')
def group_count_and_group_filter_should_be_present():
    assert ADMIN_GROUPS_PAGE.groups_tab_count_is_displayed() is True
    assert ADMIN_GROUPS_PAGE.search_group_is_displayed() is True


@then('the user should see the buttons download "CSV" and "Import Groups"')
def user_should_see_download_csv_and_import_buttons():
    assert ADMIN_GROUPS_PAGE.download_csv_button_is_present() is True
    assert ADMIN_GROUPS_PAGE.import_groups_button_is_present() is True


@when('user clicks on parent group')
def user_clicks_parent_group():
    ADMIN_GROUPS_PAGE.click_on_parent_group()


@then('kebab menu should not be present for Parent group')
def kebab_menu_should_not_present_for_parent_group():
    assert ADMIN_GROUPS_PAGE.is_parent_group_kebab_menu_displayed() is False


@when('user tap on first group')
def user_tap_on_first_group():
    ADMIN_GROUPS_PAGE.click_first_group()


@then('plus "+" icon should be displayed')
def plus_icon_is_displayed():
    assert ADMIN_GROUPS_PAGE.plus_icon_is_displayed() is True


@given('user clicks on plus icon')
@when('user clicks on Add group "+" icon')
def user_clicks_plus_icon():
    ADMIN_GROUPS_PAGE.click_plus_icon()


@then('add group pop-up should be displayed with "Group name", "Group path" and "Description"')
def add_group_pop_up_is_displayed():
    assert ADMIN_GROUPS_PAGE.add_group_is_displayed() is True
    assert ADMIN_GROUPS_PAGE.get_group_name_field_in_pop_up() == "GROUP NAME"
    assert ADMIN_GROUPS_PAGE.get_group_path_field_in_pop_up() == "Group Path"
    assert ADMIN_GROUPS_PAGE.get_description_field_in_pop_up() == "DESCRIPTION"


@then('create button should be disabled with empty fields')
def verify_create_button_should_be_disabled():
    assert ADMIN_GROUPS_PAGE.create_or_save_button_disabled() is True


@when('user fills all required fields in add group pop-up "Group name" and "Description"')
def user_fills_required_fields(context):
    ADMIN_GROUPS_PAGE.click_on_cancel()
    while ADMIN_GROUPS_PAGE.get_number_of_sub_groups() != "0":
        ADMIN_GROUPS_PAGE.delete_group()
    ADMIN_GROUPS_PAGE.click_plus_icon()
    context['GROUP_COUNT'] = ADMIN_GROUPS_PAGE.get_group_count()
    ADMIN_GROUPS_PAGE.type_group_name("Automation_Group1")
    ADMIN_GROUPS_PAGE.type_description("Group added for automation testing purpose, do not edit or delete please")
    ADMIN_GROUPS_PAGE.click_create_or_save_changes()


@then(
    'new group should be created and pop-up message should appear, group name and description is present in the group container')
def verify_new_group_added(context):
    assert ADMIN_GROUPS_PAGE.get_group_count() != context['GROUP_COUNT']
    assert ADMIN_GROUPS_PAGE.get_group_name_from_group_container() == "Automation_Group1"
    assert ADMIN_GROUPS_PAGE.get_group_description_from_group_container() == "Group added for automation testing purpose, do not edit or delete please"


@when('the user tries to add a group with an existing "Group name"')
def user_fills_required_data():
    ADMIN_GROUPS_PAGE.click_plus_icon()
    ADMIN_GROUPS_PAGE.type_group_name("Automation_Group1")
    ADMIN_GROUPS_PAGE.type_description("Group added for automation testing purpose, do not edit or delete please")
    ADMIN_GROUPS_PAGE.click_create_or_save_changes()


@then('an error message should appear indicating the group already exists')
def verify_add_existing_group():
    assert ADMIN_GROUPS_PAGE.get_group_already_exists_error_msg() == "Error! Group already exists with same Name and ParentId."


@given(parsers.parse('user clicks on the kebab for one group "{group_name}"'))
@when(parsers.parse('user clicks on the kebab for one group "{group_name}"'))
def user_clicks_the_kebab_for_newly_created_group(group_name):
    ADMIN_GROUPS_PAGE.click_on_kebab(group_name)


@then('"Edit", "Move" and "Delete" options will be displayed')
def verify_edit_move_delete_options_on_kebab():
    assert ADMIN_GROUPS_PAGE.edit_option_is_available() is True
    assert ADMIN_GROUPS_PAGE.move_option_is_available() is True
    assert ADMIN_GROUPS_PAGE.delete_option_is_available() is True


@when('user clicks on edit option')
def user_clicks_on_edit_option():
    ADMIN_GROUPS_PAGE.click_edit_option()


@then('edit group pop-up should be displayed with "Group Name", "Group Path", "Subgroups" and "description"')
def edit_group_id_displayed():
    assert ADMIN_GROUPS_PAGE.edit_group_pop_up_title_displayed() is True
    assert ADMIN_GROUPS_PAGE.get_group_name_field_in_pop_up() == "GROUP NAME"
    assert ADMIN_GROUPS_PAGE.get_group_path_field_in_pop_up() == "Group Path"
    assert ADMIN_GROUPS_PAGE.get_sub_groups_field_in_pop_up() == "Subgroups"
    assert ADMIN_GROUPS_PAGE.get_description_field_in_pop_up() == "DESCRIPTION"


@then('group name should be a required field')
def group_name_should_be_required_field():
    assert ADMIN_GROUPS_PAGE.group_name_is_a_required_field() is True


@then('save changes button is disabled')
def save_button_is_disabled():
    assert ADMIN_GROUPS_PAGE.create_or_save_button_disabled() is True


@given('user clicks on cancel button')
@when('user clicks on cancel button')
def user_clicks_on_cancel_button():
    ADMIN_GROUPS_PAGE.click_on_cancel()


@then('edit group pop up should disappear')
def verify_edit_group_pop_up_disappeared():
    assert ADMIN_GROUPS_PAGE.edit_group_pop_up_title_displayed() is False


@when('user modifies group name and description')
def user_modifies_group_name():
    ADMIN_GROUPS_PAGE.type_group_name("Auto_modified_group")
    ADMIN_GROUPS_PAGE.type_description("auto_modified_description")


@then('the save changes button is enabled')
def save_changes_button_is_displayed():
    assert ADMIN_GROUPS_PAGE.create_or_save_button_disabled() is not True


@when('user clicks save changes button')
def user_clicks_save_changes_button():
    ADMIN_GROUPS_PAGE.click_create_or_save_changes()


@then('group name and description should be changed for the same group')
def group_name_and_description_should_be_changed_for_group():
    assert ADMIN_GROUPS_PAGE.get_group_name_from_group_container() == "Auto_modified_group"
    assert ADMIN_GROUPS_PAGE.get_group_description_from_group_container() == "auto_modified_description"


@given('create a new group under parent group')
def create_new_group():
    ADMIN_GROUPS_PAGE.click_plus_icon()
    ADMIN_GROUPS_PAGE.type_group_name("Automation_Group2")
    ADMIN_GROUPS_PAGE.type_description(
        "Second group added for automation testing purpose, do not edit or delete please")
    ADMIN_GROUPS_PAGE.click_create_or_save_changes()


@when('user notes down sibling group name')
def user_notes_down_sibling_group_name():
    global SIBLING_GROUP
    SIBLING_GROUP = ADMIN_GROUPS_PAGE.get_current_level_sibling_group_name()


@when('rename the group as same as sibling group')
def rename_the_group_from_edit_group_page():
    ADMIN_GROUPS_PAGE.type_group_name(SIBLING_GROUP)
    ADMIN_GROUPS_PAGE.click_create_or_save_changes()


@then(
    'group name should not be changed, there should be an error "Error! Group already exists with same Name and ParentId."')
def group_name_should_not_be_changed():
    assert ADMIN_GROUPS_PAGE.get_group_already_exists_error_msg() == "Error! Group already exists with same Name and ParentId."


@when('user clicks on delete option from kebab')
def user_clicks_delete_button():
    ADMIN_GROUPS_PAGE.click_delete()


@then('delete group confirmation pop-up should be displayed with "Cancel" and "Delete"')
def delete_group_pop_up_is_present():
    assert ADMIN_GROUPS_PAGE.delete_group_pop_up_title_displayed() is True
    assert ADMIN_GROUPS_PAGE.get_group_path_field_in_delete_pop_up() == "Group Path"
    assert ADMIN_GROUPS_PAGE.cancel_button_is_displayed() is True
    assert ADMIN_GROUPS_PAGE.delete_button_is_displayed() is True
    assert ADMIN_GROUPS_PAGE.get_confirmation_msg_for_delete_group() == "Are you sure you want to permanently delete this group?"


@then('delete-group pop up should be disappear')
def pop_up_disappear():
    assert ADMIN_GROUPS_PAGE.delete_group_pop_up_title_displayed() is False


@when('user deletes the group')
def user_deletes_the_group(context):
    context['GROUP_COUNT'] = ADMIN_GROUPS_PAGE.get_group_count()
    ADMIN_GROUPS_PAGE.click_delete_group()


@then('group should be deleted')
def group_is_deleted(context):
    assert ADMIN_GROUPS_PAGE.get_group_count() != context['GROUP_COUNT']


@when('click delete from edit group pop_up')
def click_delete_in_pop_up():
    ADMIN_GROUPS_PAGE.click_delete_edit_page()


@when('user clicks on cancel button in delete pop up')
def click_cancel_in_delete_pop_up():
    ADMIN_GROUPS_PAGE.click_cancel_in_delete_pop_up()


@when('user deletes the group from edit page')
def user_deletes_the_group_from_edit_page(context):
    context['GROUP_COUNT'] = ADMIN_GROUPS_PAGE.get_group_count()
    ADMIN_GROUPS_PAGE.click_delete_edit_page()
    ADMIN_GROUPS_PAGE.click_delete_group()


@given(parsers.parse('user creates child group with name "{group_name}" and description "{desc}"'))
def create_group_for_child_group(group_name, desc):
    ADMIN_GROUPS_PAGE.click_first_child_group()
    ADMIN_GROUPS_PAGE.click_plus_icon_child()
    ADMIN_GROUPS_PAGE.type_group_name(group_name)
    ADMIN_GROUPS_PAGE.type_description(desc)
    ADMIN_GROUPS_PAGE.click_create_or_save_changes()


@then(
    'cannot delete group pop up should be displayed and "All subgroups within the group must be moved or deleted prior to group deletion", "Close" button is displayed')
def cannot_delete_group():
    assert ADMIN_GROUPS_PAGE.cant_delete_group_message_displayed() is True
    assert ADMIN_GROUPS_PAGE.get_cant_delete_group_suggestion_message() == "All subgroups within the group must be moved or deleted prior to group deletion."


@when('user clicks on close button')
def user_click_close_button():
    ADMIN_GROUPS_PAGE.click_close()


@then('group should not be deleted')
def group_should_not_be_deleted():
    assert ADMIN_GROUPS_PAGE.get_current_level_sibling_group_name() == "Auto_modified_group"


@when(parsers.parse('delete child group "{group_name}"'))
def delete_child_group(group_name, context):
    context['GROUP_COUNT'] = ADMIN_GROUPS_PAGE.get_group_count()
    ADMIN_GROUPS_PAGE.click_on_kebab(group_name)
    ADMIN_GROUPS_PAGE.click_delete()
    ADMIN_GROUPS_PAGE.click_delete_group()


@then('child group "Child_Automation_Group1" should be deleted')
def child_group_is_deleted(context):
    assert ADMIN_GROUPS_PAGE.get_group_count() != context['GROUP_COUNT']


@given('user clicks on Search box')
def user_click_on_search_box():
    ADMIN_GROUPS_PAGE.click_on_search_box()


@when(parsers.parse('user enters group name in search box "{group_name}"'))
def enter_group_name(group_name):
    ADMIN_GROUPS_PAGE.enter_text_in_search_box(group_name)


@then(parsers.parse('drop down should not be present'))
def verify_dropdown_present():
    assert ADMIN_GROUPS_PAGE.is_dropdown_present_for_search_box() is False


@when('user enters group name in search box')
def user_enters_group_name_in_search_box():
    ADMIN_GROUPS_PAGE.enter_text_in_search_box(AD.group1)


@then('drop down should be present')
def drop_down_should_be_present():
    assert ADMIN_GROUPS_PAGE.is_dropdown_present_for_search_box() is True


@when('user clicks group name from suggestion')
def user_clicks_group_name_from_suggestion():
    ADMIN_GROUPS_PAGE.click_group_from_suggestion_box()


@then('same group should be focused')
def same_group_should_be_focused():
    assert ADMIN_GROUPS_PAGE.group_is_focused() is True


@when('user tap on "The Doughnut Peddler, LLC- Main" group')
def click_on_the_doughnut_peddler_group():
    ADMIN_GROUPS_PAGE.click_on_the_doughnut_peddler_group()


@then('subgroups are displayed')
def subgroups_are_displayed():
    assert ADMIN_GROUPS_PAGE.sub_groups_are_displayed() is True


@when('the user clicks on child group "Distribution Centers"')
def click_on_distribution_center_group():
    ADMIN_GROUPS_PAGE.click_distribution_center_group()


@then('the breadcrumb should display with opened group names')
def the_breadcrumb_should_display():
    assert_that(ADMIN_GROUPS_PAGE.get_breadcrumb_text(), contains_string("The Doughnut Peddler, LLC"))
    assert_that(ADMIN_GROUPS_PAGE.get_breadcrumb_text(), contains_string("The Doughnut Peddler, LLC- Main"))
    assert_that(ADMIN_GROUPS_PAGE.get_breadcrumb_text(), contains_string("Distribution Centers"))


@given('the "Administrator/FA" user is in Group Page')
def admin_fa_in_groups_page():
    LOGIN_PAGE.navigate_to(DC_URL)
    LOGIN_PAGE.enter_username(AD.FA_internal_user)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_company()
    LOGIN_PAGE.click_select_company_button()


@when('the user clicks on the "View Change History" in Group Management page')
def click_view_change_history_group_management():
    DASHBOARD_PAGE.click_admin_tab()
    ADMIN_GROUPS_PAGE.click_groups_tab()
    ADMIN_GROUPS_PAGE.click_view_change_history()


@then('the user should be able to see the table columns: "GROUP AFFECTED", "ACTION", "ACTION DETAILS","EDITOR", "ACTION DATE" and page header "Group Audit Log"')
def verify_table_columns():
    assert ADMIN_GROUPS_PAGE.get_name_column_title() == "NAME"
    assert ADMIN_GROUPS_PAGE.get_groups_column_title() == "GROUP(S)"
    assert ADMIN_GROUPS_PAGE.get_action_column_title() == "ACTION"
    assert ADMIN_GROUPS_PAGE.get_action_details_column_title() == "ACTION DETAILS"
    assert ADMIN_GROUPS_PAGE.get_action_date_column_title() == "ACTION DATE"
    assert_that(ADMIN_GROUPS_PAGE.get_group_audit_log_title(), contains_string("Group Audit Log"))


@then('The user should be see the filters ‘Search Group Affected’, Date filter and ‘Select Action(s)’ in the header, and the ‘Download Log’ button')
def verify_filters_and_download_button():
    assert ADMIN_GROUPS_PAGE.search_group_affected_is_displayed() is True
    assert ADMIN_GROUPS_PAGE.select_actions_is_displayed() is True
    assert ADMIN_GROUPS_PAGE.download_log_button_is_displayed() is True
    assert ADMIN_GROUPS_PAGE.date_filter_is_displayed() is True


@when('the user enters a valid Group in "Search Group Affected"')
def search_group_affected():
    global AFFECTED_GROUP
    AFFECTED_GROUP = ADMIN_GROUPS_PAGE.get_first_group_affected_text()
    ADMIN_GROUPS_PAGE.search_group_affected(AFFECTED_GROUP)


@then('the system should display only matching logs')
def verify_search_group_affected():
    assert_that(ADMIN_GROUPS_PAGE.get_first_group_affected_text(), IsEqualIgnoringCase(AFFECTED_GROUP))


@when('the user enters an invalid group number in "Search Group Affected"')
def search_invalid_group_affected():
    ADMIN_GROUPS_PAGE.click_reset_in_audit_page()
    ADMIN_GROUPS_PAGE.search_group_affected("InvalidGroup123")


@then('the system should show no results message')
def verify_no_results_message():
    assert ADMIN_GROUPS_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected date range"


@when('the user selects a date range in the Date filter')
def select_date_range_group_audit_log():
    ADMIN_GROUPS_PAGE.click_reset_in_audit_page()
    ADMIN_GROUPS_PAGE.click_date_range_dropdown()
    ADMIN_GROUPS_PAGE.select_date_range_today()


@then('the system should display logs within the selected date range')
def verify_date_range_logs_group_audit_log():
    assert_that(ADMIN_GROUPS_PAGE.get_action_date(), contains_string(ADMIN_GROUPS_PAGE.get_time_today()))


@when('the user clicks on the "Close" button')
def click_close_button_group_audit_log():
    ADMIN_GROUPS_PAGE.click_close_group_audit_log()


@then('the group Audit Log tab should be closed successfully')
def verify_close_group_audit_log():
    assert ADMIN_GROUPS_PAGE.view_change_history_popup_displayed() is False


# LQ-249538
@given('user clicks on "View Change History" in Group Management page')
def user_clicks_view_change_history_group_management():
    ADMIN_GROUPS_PAGE.click_view_change_history()


@when('the user selects the Action "Added" from the "Select Action(s)" filter dropdown')
def select_action_added_group_audit_log():
    ADMIN_GROUPS_PAGE.click_select_actions_filter()
    ADMIN_GROUPS_PAGE.select_action_type_added()


@then('the group Audit Log should display logs with the Action type as "Added"')
def verify_action_type_filter():
    try:
        assert ADMIN_GROUPS_PAGE.get_first_action_type_text() == "Added"
    except TimeoutException:
        assert ADMIN_GROUPS_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected date range"


@when('the user selects the Action "Edited" from the "Select Action(s)" filter dropdown')
def select_action_edited_group_audit_log():
    ADMIN_GROUPS_PAGE.click_reset_in_audit_page()
    ADMIN_GROUPS_PAGE.click_select_actions_filter()
    ADMIN_GROUPS_PAGE.select_action_type_edited()


@then('the Group Audit Log should display logs with the Action type as "Edited"')
def verify_action_type_edited_filter():
    try:
        assert ADMIN_GROUPS_PAGE.get_first_action_type_text() == "Edited"
    except TimeoutException:
        assert ADMIN_GROUPS_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected date range"


@when('the user selects the Action "Deleted" from the "Select Action(s)" filter dropdown')
def select_action_deleted_group_audit_log():
    ADMIN_GROUPS_PAGE.click_reset_in_audit_page()
    ADMIN_GROUPS_PAGE.click_select_actions_filter()
    ADMIN_GROUPS_PAGE.select_deleted_action_type()


@then('the Group Audit Log should display logs with the Action type as "Deleted"')
def verify_action_type_deleted_filter():
    try:
        assert ADMIN_GROUPS_PAGE.get_first_action_type_text() == "Deleted"
    except TimeoutException:
        assert ADMIN_GROUPS_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected date range"



@when('the user selects the Action "Imported" from the "Select Action(s)" filter dropdown')
def select_action_imported_group_audit_log():
    ADMIN_GROUPS_PAGE.click_reset_in_audit_page()
    ADMIN_GROUPS_PAGE.click_select_actions_filter()
    ADMIN_GROUPS_PAGE.select_imported_action_type()


@then('the Group Audit Log should display logs with the Action type as "Imported"')
def verify_action_type_imported_filter():
    try:
        assert ADMIN_GROUPS_PAGE.get_first_action_type_text() == "Imported"
    except TimeoutException:
        assert ADMIN_GROUPS_PAGE.get_no_audit_logs_message() == "No audit logs available for the selected date range"


# LQ-249600
@when('the user clicks "Download Log" in the Group audit log tab')
def click_download_log_group_audit_log():
    ADMIN_GROUPS_PAGE.click_reset_in_audit_page()
    ADMIN_GROUPS_PAGE.click_download_log_button()


@then('the Group audit log is downloaded successfully')
def verify_download_log_group_audit_log():
    file_name = ADMIN_GROUPS_PAGE.get_audit_log_file_name()
    ADMIN_GROUPS_PAGE.wait_for_file_downloaded(file_name)


@when('search an invalid group in "Search group Affected" filter')
def search_invalid_group_audit_log():
    ADMIN_GROUPS_PAGE.search_group_affected("NoSuchGroup123")


@then('the "Download Log" button is disabled in group Audit Log')
def verify_download_log_button_disabled():
    assert ADMIN_GROUPS_PAGE.download_log_button_disabled_displayed() is True


@given('admin user logs in with FA/SM user')
def fa_sm_log_in():
    LOGIN_PAGE.navigate_to(DC_URL)
    LOGIN_PAGE.enter_username(AD.FA_GM_SM_user)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()


@when('user navigates to Groups management page')
def navigate_to_groups_management_page():
    DASHBOARD_PAGE.click_admin_tab()
    ADMIN_GROUPS_PAGE.click_groups_tab()


@then('user should be able to view Groups belongs to Full access user only')
def verify_groups_belongs_to_full_access_user():
    assert ADMIN_GROUPS_PAGE.group_management_page_is_displayed() is True
    assert ADMIN_GROUPS_PAGE.get_group_name_from_container() == "*** Corrupt Events ***"