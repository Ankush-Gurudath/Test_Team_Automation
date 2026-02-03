from pytest_bdd import scenarios, given, when, then
from pages.add_user_page import AddUserPage
from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from pages.configuration_setting_page import ConfigurationSettingPage
from pages.login_page import LoginPage
from steps.common import DC_URL, ENV
from pages.user_management_page import UserManagementPage
from pages.trailer_management_page import TrailerManagementPage
from pages.edit_trailer_page import EditTrailerPage
from pages.add_trailer_page import AddTrailerPage
from data.prod.admin_data_prod import AdminDataProd as AD_PROD
from data.stg.admin_data_stg import AdminDataStg as AD_STG
from data.int.admin_data_int import AdminDataInt as AD_INT

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
CONFIGURATION_SETTING_PAGE = 0
USER_MANAGEMENT_PAGE = 0
TRAILER_MANAGEMENT_PAGE = 0
AD = 0
ADD_TRAILER_PAGE = 0
ADD_USER_PAGE = 0
EDIT_TRAILER_PAGE = 0

scenarios('../features/admin_config_trailer.feature')


# LQ-242
@given('Administrator user is in Admin')
def login_as_admin(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, CONFIGURATION_SETTING_PAGE, TRAILER_MANAGEMENT_PAGE, USER_MANAGEMENT_PAGE, AD, ADD_TRAILER_PAGE, EDIT_TRAILER_PAGE

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)
    TRAILER_MANAGEMENT_PAGE = TrailerManagementPage(browser)
    CONFIGURATION_SETTING_PAGE = ConfigurationSettingPage(browser)
    ADD_TRAILER_PAGE = AddTrailerPage(browser)
    EDIT_TRAILER_PAGE = EditTrailerPage(browser)

    browser.get(DC_URL)

    if ENV == 'int':
        AD = AD_INT
    elif ENV == 'stg':
        AD = AD_STG
    else:
        AD = AD_PROD
    LOGIN_PAGE.enter_username(AD.admin_user_name)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_company()
    LOGIN_PAGE.click_select_company_button()
    LOGIN_PAGE.retry_if_login_failed(DC_URL, AD.admin_user_name, AD.password, AD.company_name)
    DASHBOARD_PAGE.click_admin_tab()


@when('the user clicks CONFIG SETTING')
def navigate_to_config_setting_page():
    USER_MANAGEMENT_PAGE.click_config_setting_tab()


@then('Full access role is in tier 1 by default')
def verify_tier_1_full_access_role():
    assert CONFIGURATION_SETTING_PAGE.get_tier1_label() == "Tier 1"
    assert CONFIGURATION_SETTING_PAGE.get_full_access_tier1_role_text() == "Full Access"


# LQ-244
@when('the user click the "Add New Tier" button & the user selects some roles & the user clicks "Confirm" on the popup')
def add_new_tier():
    CONFIGURATION_SETTING_PAGE.click_add_new_tier_button()
    CONFIGURATION_SETTING_PAGE.click_select_roles_button()
    CONFIGURATION_SETTING_PAGE.click_first_role_dropdown_button()
    CONFIGURATION_SETTING_PAGE.click_role_twice_button()
    CONFIGURATION_SETTING_PAGE.click_select_roles_confirm_button()


@then('the selected roles are listed under the newly added tier')
def verify_new_role_tier():
    assert CONFIGURATION_SETTING_PAGE.get_new_role_added_text() == "API Developer"


# LQ-5557
@when(
    'the user clicks "Edit Tier" icon for tier 1 & the user checks some roles & the user clicks "Confirm" on the popup')
def edit_tier():
    CONFIGURATION_SETTING_PAGE.click_edit_tier_button()
    CONFIGURATION_SETTING_PAGE.click_edit_roles_button()
    if CONFIGURATION_SETTING_PAGE.role_already_selected() is True:
        CONFIGURATION_SETTING_PAGE.delete_role_already_selected()
        CONFIGURATION_SETTING_PAGE.click_role_twice_button()
        CONFIGURATION_SETTING_PAGE.click_edit_roles_confirm_button()
        CONFIGURATION_SETTING_PAGE.click_refresh_button()
        CONFIGURATION_SETTING_PAGE.click_edit_tier_button()
        CONFIGURATION_SETTING_PAGE.click_edit_roles_button()
    CONFIGURATION_SETTING_PAGE.click_select_roles_edit_button()
    CONFIGURATION_SETTING_PAGE.click_role_twice_button()
    CONFIGURATION_SETTING_PAGE.click_edit_roles_confirm_button()


@then('the checked roles are updated')
def verify_edit_tier_roles():
    assert CONFIGURATION_SETTING_PAGE.get_second_tier2_role_text() == "API Developer Read Only"


@when('the user clicks on the "Delete Tier" button & the user clicks "Confirm" button on the popup')
def delete_tier():
    CONFIGURATION_SETTING_PAGE.click_delete_tier_button()
    CONFIGURATION_SETTING_PAGE.click_confirm_delete_tier_button()


@then('the tier is deleted')
def verify_delete_tier():
    assert CONFIGURATION_SETTING_PAGE.get_tier2_text("Unranked Tier") == "Unranked Tier"


# LQ-12128
@when('the user clicks the "TRAILER" tab')
def go_to_trailer_management_page():
    TRAILER_MANAGEMENT_PAGE.click_trailer_tab()


@then(
    'the page header "TRAILER MANAGEMENT" is displayed and the table is displayed with columns: "TRAILER", "GROUP", "LICENSE PLATE", "VIN", "INSPECTION LIST"')
def verify_trailer_management_page():
    assert TRAILER_MANAGEMENT_PAGE.get_trailer_management_text() == "TRAILER MANAGEMENT"
    assert TRAILER_MANAGEMENT_PAGE.get_trailer_column_text() == "TRAILER"
    assert TRAILER_MANAGEMENT_PAGE.get_group_column_text() == "GROUP"
    assert TRAILER_MANAGEMENT_PAGE.get_license_plate_column_text() == "LICENSE PLATE"
    assert TRAILER_MANAGEMENT_PAGE.get_vin_column_text() == "VIN"
    assert TRAILER_MANAGEMENT_PAGE.get_inspection_list_column_text() == "INSPECTION LIST"


# LQ-12129
@when('the user sets group filter to one group on the Trailer Management page')
def set_group_filter_trailer_management_page():
    TRAILER_MANAGEMENT_PAGE.click_group_filter()
    TRAILER_MANAGEMENT_PAGE.search_group(AD.group)
    TRAILER_MANAGEMENT_PAGE.select_searched_group()
    TRAILER_MANAGEMENT_PAGE.click_done_button()


@then('the Trailer belong to the group are listed')
def verify_group_filter_trailer_management_page():
    assert TRAILER_MANAGEMENT_PAGE.get_first_trailer_group(AD.group) == AD.group


@when('the user enters some characters into "Search Trailer" field on the Trailer Management page')
def search_trailer():
    TRAILER_MANAGEMENT_PAGE.type_trailer_name("TestTrailer")


@then('the Trailers that contained the inputted characters are shown')
def verify_search_trailer_trailer_management_page():
    assert TRAILER_MANAGEMENT_PAGE.get_row_count(10) == 0
    TRAILER_MANAGEMENT_PAGE.click_reset_button()


# LQ-12159
@when(
    'the user clicks on "Add Trailer" & the user enters required fields: "Group" and "Trailer Name" & the user enters required fields: "Group" and "Trailer Name"')
def add_new_trailer():
    global tabn
    tabn = AddUserPage(BasePage)
    tabn.get_random_string()
    tabn.get_random_name(6)
    TRAILER_MANAGEMENT_PAGE.click_add_trailer_button()
    ADD_TRAILER_PAGE.click_group_trailer_filter()
    ADD_TRAILER_PAGE.search_group_trailer_filter(AD.group)
    ADD_TRAILER_PAGE.select_searched_group()
    ADD_TRAILER_PAGE.click_done_trailer_group_button()
    ADD_TRAILER_PAGE.type_trailer_name(tabn.random_name)
    ADD_TRAILER_PAGE.type_vin_number(tabn.random_word)
    ADD_TRAILER_PAGE.click_create_trailer()


@then('the Trailer is added')
def verify_added_new_trailer():
    TRAILER_MANAGEMENT_PAGE.search_trailer_name(tabn.random_name)
    assert TRAILER_MANAGEMENT_PAGE.get_searched_trailer_name(tabn.random_name) == tabn.random_name


# LQ-17331
@when(
    'the user clicks on the name of a trailer & the user changes "Trailer Name" on Edit Trailer page & the user sets one group & the user clicks "Save Changes"')
def edit_trailer_name():
    TRAILER_MANAGEMENT_PAGE.click_added_trailer_name()
    EDIT_TRAILER_PAGE.clear_trailer_name()
    EDIT_TRAILER_PAGE.edit_first_name_trailer(tabn.random_word)
    EDIT_TRAILER_PAGE.click_save_trailer()
    TRAILER_MANAGEMENT_PAGE.click_reset_button()


@then('the First Name of the edited trailer is updated')
def verify_edit_trailer_name():
    TRAILER_MANAGEMENT_PAGE.search_trailer_name(tabn.random_word)
    assert TRAILER_MANAGEMENT_PAGE.get_searched_trailer_name(tabn.random_word) == tabn.random_word


# LQ-15957
@when('the "users" checks one trailer and the "users" clicks "Set Inspection List"')
def set_single_inspection_list_for_trailer():
    TRAILER_MANAGEMENT_PAGE.click_reset_button()
    TRAILER_MANAGEMENT_PAGE.select_first_trailer()
    TRAILER_MANAGEMENT_PAGE.click_set_inspection_list_button()
    TRAILER_MANAGEMENT_PAGE.select_second_inspection_list_dialog()
    TRAILER_MANAGEMENT_PAGE.click_set_inspection_list_dialog()


@then('the inspection list is assigned to the selected trailer')
def verify_single_inspection_list_for_trailer():
    assert TRAILER_MANAGEMENT_PAGE.get_first_inspection_list_text(
        AD.second_trailer_inspection_list) == AD.second_trailer_inspection_list


@when('the "users" checks one or more trailers & the "users" clicks "Set Inspection List"')
def set_multiple_inspection_list_for_trailer():
    TRAILER_MANAGEMENT_PAGE.select_first_trailer()
    TRAILER_MANAGEMENT_PAGE.select_second_trailer()
    TRAILER_MANAGEMENT_PAGE.click_set_inspection_list_button()
    TRAILER_MANAGEMENT_PAGE.select_first_inspection_list_dialog()
    TRAILER_MANAGEMENT_PAGE.select_second_inspection_list_dialog()
    TRAILER_MANAGEMENT_PAGE.click_set_inspection_list_dialog()


@then('the inspection lists are assigned to the selected trailers')
def assert_multiple_inspection_list_for_trailer():
    second_list = AD.second_trailer_inspection_list + ", " + AD.first_trailer_inspection_list
    assert TRAILER_MANAGEMENT_PAGE.get_first_inspection_list_text(second_list) == second_list
    assert TRAILER_MANAGEMENT_PAGE.get_second_inspection_list_text() == second_list


# @LQ-101422
@when('the user clicks the "Coaching Workflows" tab')
def navigate_to_coaching_workflow_page():
    CONFIGURATION_SETTING_PAGE.click_coaching_workflow_tab()


@then(
    'the user should be able to see the page with the header "Workflows" and all the available workflows listed below.')
def verify_coaching_workflow_page_is_displayed():
    assert CONFIGURATION_SETTING_PAGE.get_workflows_title() == "Workflows"


@then('the user should be able to see a button "Create Workflow" filled with blue color in the right top corner.')
def verify_create_workflow_button_is_present():
    assert CONFIGURATION_SETTING_PAGE.create_workflow_button_is_displayed() is True


# @LQ-101424
# (When part is covered in LQ-101422)

@then(
    'the user should be able to see all the workflows with the "Groups", "Duplicate", "Edit", "Delete", "Download" present straight to it in hyperlink format.')
def verify_the_list_of_buttons_present_in_workflw_cloumn():
    assert CONFIGURATION_SETTING_PAGE.groups_button_is_displayed() is True
    assert CONFIGURATION_SETTING_PAGE.duplicate_button_is_displayed() is True
    assert CONFIGURATION_SETTING_PAGE.download_button_is_displayed() is True


# @LQ-106871
@when('the user sets group filter to one group on the coaching workflow page')
def set_group_filter_in_coaching_workflow_page():
    CONFIGURATION_SETTING_PAGE.click_group_filter()
    CONFIGURATION_SETTING_PAGE.search_group(AD.group)
    CONFIGURATION_SETTING_PAGE.select_searched_group()
    CONFIGURATION_SETTING_PAGE.click_done_button()


@then('the workflows belong to the group are listed')
def verify_group_filter_trailer_management_page():
    CONFIGURATION_SETTING_PAGE.click_group_button()
    assert CONFIGURATION_SETTING_PAGE.get_first_group_name() == AD.group
    CONFIGURATION_SETTING_PAGE.close_group_page()
    CONFIGURATION_SETTING_PAGE.click_reset_button()


# @LQ-101427
@when('the user clicks the "Create Workflow" button.')
def navigate_to_create_workflow_page():
    CONFIGURATION_SETTING_PAGE.click_create_workflow_button()


@then('the user should see "Create Workflow" page coming from the bottom.')
def verify_create_workflow_page_is_displayed():
    assert CONFIGURATION_SETTING_PAGE.get_create_workflow_title() == "Create Workflow"


# @LA-103680
@when('the user clicks the "Create Workflow" button & enters the workflow name')
def add_required_details():
    CONFIGURATION_SETTING_PAGE.enter_new_workflow_name(AD.workflow_name)


@when(
    'the user selects the the behaviour, coaching status from the dropdowns and the user gives a custom score & the user clicks on save button')
def select_required_fields_in_create_workflow_page():
    CONFIGURATION_SETTING_PAGE.click_behaviour_dropdown()
    CONFIGURATION_SETTING_PAGE.select_the_behaviour_from_dropdown()
    CONFIGURATION_SETTING_PAGE.click_coaching_status_dropdown()
    CONFIGURATION_SETTING_PAGE.select_the_coaching_status_from_dropdown()
    CONFIGURATION_SETTING_PAGE.enter_a_custom_score(AD.custom_score)
    CONFIGURATION_SETTING_PAGE.click_save_button()


@then('new coaching workflow is created')
def verify_new_created_workflow():
    CONFIGURATION_SETTING_PAGE.click_search_filed_in_workflow_page()
    CONFIGURATION_SETTING_PAGE.enter_newly_created_workflow_name(AD.workflow_name)
    assert CONFIGURATION_SETTING_PAGE.get_first_workflow_name() == AD.workflow_name
    # Script to verify PHNX-4286
    CONFIGURATION_SETTING_PAGE.click_role_hierarchy_tab_xpath()
    CONFIGURATION_SETTING_PAGE.click_coaching_workflow_tab()
    assert CONFIGURATION_SETTING_PAGE.get_first_workflow_name() == AD.workflow_name



# LQ-104058
@when('the user clicks the download button of any workflow')
def click_download_button():
    CONFIGURATION_SETTING_PAGE.click_download_button_of_any_workflow()


@then('the user should see the workflow downloaded in the CSV Format "YYYY-MM-DD_Events_Workflow_Workflow name.csv"')
def verify_csv_report_downloaded():
    file_name = CONFIGURATION_SETTING_PAGE.get_workflow_file_name(AD.workflow_name)
    CONFIGURATION_SETTING_PAGE.wait_for_file_downloaded(file_name)
    assert CONFIGURATION_SETTING_PAGE.check_file_exist(file_name) is True


# @LQ-104000
@when('the user clicks the edit button')
def navigate_to_edit_workflow_page():
    CONFIGURATION_SETTING_PAGE.click_edit_button()


@then('the user should see "Edit Workflow" page coming from the bottom')
def verify_edit_workflow_page():
    assert CONFIGURATION_SETTING_PAGE.get_edit_workflow_title() == "Edit Workflow"


# @LQ-104043
@when('the user clicks the "Cancel" button without doing any changes')
def click_cancel_button():
    CONFIGURATION_SETTING_PAGE.click_cancel_button_edit_workflow_page()


@then('the user should be redirected to the Workflows page without any pop-up message.')
def verify_workflow_page():
    assert CONFIGURATION_SETTING_PAGE.get_workflows_title() == "Workflows"


# @LQ-105094
@when('the user is on edit workflow page')
def navigate_to_edit_workflow_page():
    CONFIGURATION_SETTING_PAGE.click_edit_button()


@then('the user should be able to see the workflow rules of the workflow and the user should be able to see delete '
      'icon present at the end of every rule of the workflow.')
def verify_delete_icon_in_edit_workflow_page():
    assert CONFIGURATION_SETTING_PAGE.delete_existing_behaviour_is_present() is True


# @LQ-104032
@when('the user edit behavior, or Coaching status or custom score')
def edit_existing_workflow():
    CONFIGURATION_SETTING_PAGE.delete_existing_behaviour()
    CONFIGURATION_SETTING_PAGE.click_add_button()
    CONFIGURATION_SETTING_PAGE.click_behaviour_dropdown()
    CONFIGURATION_SETTING_PAGE.select_the_behaviour_from_dropdown()
    CONFIGURATION_SETTING_PAGE.click_coaching_status_dropdown()
    CONFIGURATION_SETTING_PAGE.select_the_coaching_status_from_dropdown()
    CONFIGURATION_SETTING_PAGE.enter_a_custom_score(AD.custom_score)


@then('the user should able save the changes')
def save_the_new_changes():
    CONFIGURATION_SETTING_PAGE.click_save_button()


@then('user should be navigated to the Workflows page with the success pop-up message "Sucessfully updated the '
      'workflow"')
def verify_the_popup_message():
    assert CONFIGURATION_SETTING_PAGE.get_workflows_title() == "Workflows"
    assert CONFIGURATION_SETTING_PAGE.get_update_popup_message() == "Successfully updated the workflow"


# @lQ-105045
@when('the user clicks the Duplicate icon of any workflow which is present next to Groups icon.')
def duplicate_the_workflow():
    CONFIGURATION_SETTING_PAGE.click_duplicate_button_of_a_workflow()


@then('the user should be navigated to "Create Worflow" page with the respective rules of the selected workflow')
def verify_create_workflow_page_is_displayed():
    assert CONFIGURATION_SETTING_PAGE.get_create_workflow_title() == "Create Workflow"


@then('the user inputs a unique workflow name and the user should be able to change any behaviors,coaching status or '
      'custom score.')
def enter_unique_workflow_name():
    CONFIGURATION_SETTING_PAGE.enter_new_workflow_name(AD.duplicate_workflow_name)


@then('the user should be able to add new rule using "+Add" button and the user clicks "Save" button.')
def add_new_rule():
    CONFIGURATION_SETTING_PAGE.click_add_button()
    CONFIGURATION_SETTING_PAGE.click_behaviour_dropdown_duplicate()
    CONFIGURATION_SETTING_PAGE.select_the_behaviour_from_dropdown_duplicate()
    CONFIGURATION_SETTING_PAGE.click_coaching_status_dropdown_duplicate()
    CONFIGURATION_SETTING_PAGE.select_the_coaching_status_from_dropdown_duplicate()
    CONFIGURATION_SETTING_PAGE.enter_a_custom_score_duplicate(AD.custom_score)
    CONFIGURATION_SETTING_PAGE.click_save_button()


@then('the user should be redirected to Workflows page and see the created workflow with the respective rules.')
def verify_duplicated_workflow():
    assert CONFIGURATION_SETTING_PAGE.get_workflows_title() == "Workflows"
    CONFIGURATION_SETTING_PAGE.click_reset_button()
    CONFIGURATION_SETTING_PAGE.click_search_filed_in_workflow_page()
    CONFIGURATION_SETTING_PAGE.enter_newly_created_workflow_name(AD.duplicate_workflow_name)
    assert CONFIGURATION_SETTING_PAGE.get_first_workflow_name() == AD.duplicate_workflow_name


# @LQ-103684
@when('the user clicks the delete icon present straight to the workflow name.')
def delete_workflow():
    CONFIGURATION_SETTING_PAGE.click_delete_button()
    CONFIGURATION_SETTING_PAGE.click_delete_in_popup()


@then('the user should be able to see a success pop-up message "Workflows deleted successfully".')
def verify_delete_message():
    assert CONFIGURATION_SETTING_PAGE.get_delete_popup_message() == "Workflow deleted successfully."


@then('the user should not be able see the delete workflow in the Workflows page.')
def verify_deleted_workflow_is_not_present():
    assert CONFIGURATION_SETTING_PAGE.get_first_workflow_name_after_delete() is False
    CONFIGURATION_SETTING_PAGE.click_reset_button()
    CONFIGURATION_SETTING_PAGE.click_search_filed_in_workflow_page()
    CONFIGURATION_SETTING_PAGE.enter_newly_created_workflow_name(AD.workflow_name)
    assert CONFIGURATION_SETTING_PAGE.get_first_workflow_name() == AD.workflow_name
    CONFIGURATION_SETTING_PAGE.click_delete_button()
    CONFIGURATION_SETTING_PAGE.click_delete_in_popup()
