from time import sleep

from hamcrest import assert_that
from hamcrest.library.text.isequal_ignoring_case import IsEqualIgnoringCase, equal_to_ignoring_case
from pytest_bdd import scenarios, given, when, then
from pages.add_user_page import AddUserPage
from pages.base_page import BasePage
from pages.dashboard_page import DashboardPage
from pages.configuration_setting_page import ConfigurationSettingPage
from pages.login_page import LoginPage
from steps.common import ENV, NEW_UI_FTM_URL
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

scenarios('../features/admin_coaching_workflow.feature')


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

    browser.get(NEW_UI_FTM_URL)

    if ENV == 'int':
        AD = AD_INT
    elif ENV == 'stg':
        AD = AD_STG
    elif ENV == 'prod':
        AD = AD_PROD
    else:
        raise ValueError(f"Unsupported ENV value: {ENV!r}. Must be one of 'int', 'stg', or 'prod'.")

    LOGIN_PAGE.enter_username(AD.admin_user_name1)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.open_company_list()
    LOGIN_PAGE.select_multi_company('DriveCam DC4DC Test Co')
    LOGIN_PAGE.click_select_company_button()


# @LQ-101422
@when('the user clicks the "Coaching Workflows" tab')
def navigate_to_coaching_workflow_page():
    DASHBOARD_PAGE.click_admin_tab()
    USER_MANAGEMENT_PAGE.click_config_setting_tab()
    CONFIGURATION_SETTING_PAGE.click_coaching_workflow_tab()


@then(
    'the user should be able to see the page with the header "Workflows" and all the available workflows listed below.')
def verify_coaching_workflow_page_is_displayed():
    assert CONFIGURATION_SETTING_PAGE.get_workflows_title() == "Workflows"


@then('the user should be able to see a button "Create Workflow" filled with blue color in the right top corner.')
def verify_create_workflow_button_is_present():
    assert CONFIGURATION_SETTING_PAGE.create_workflow_button_is_displayed() is True


@then('the user should see the count of Workflow and filters like "Select Group", "Search Workflow" and "Reset"')
def verify_user_should_see_workflow_count_and_filters():
    assert CONFIGURATION_SETTING_PAGE.workflow_count_is_displayed() is True
    assert CONFIGURATION_SETTING_PAGE.workflow_group_filter_is_displayed() is True
    assert CONFIGURATION_SETTING_PAGE.search_workflow_button_is_displayed() is True


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
    CONFIGURATION_SETTING_PAGE.search_group(AD.group1)
    CONFIGURATION_SETTING_PAGE.select_searched_group()
    CONFIGURATION_SETTING_PAGE.click_done_button()


@then('the workflows belong to the group are listed')
def verify_group_filter_trailer_management_page():
    CONFIGURATION_SETTING_PAGE.click_group_button()
    assert CONFIGURATION_SETTING_PAGE.get_first_group_name() == AD.group1
    CONFIGURATION_SETTING_PAGE.close_group_page()
    CONFIGURATION_SETTING_PAGE.click_reset_button()


# @LQ-101427
@when('the user clicks the "Create Workflow" button.')
def navigate_to_create_workflow_page():
    CONFIGURATION_SETTING_PAGE.click_create_workflow_button()


@then('the user should see "Create Workflow" page coming from the bottom.')
def verify_create_workflow_page_is_displayed():
    assert CONFIGURATION_SETTING_PAGE.get_create_workflow_title() == "Create Workflow"


# LQ-161146
@when('the user clicks the "X" icon present at the top right corner of the create Workflow modal')
def click_close_icon_in_create_workflow_page():
    CONFIGURATION_SETTING_PAGE.click_close_icon_in_create_workflow_page()


@then('the user should be redirected to the Workflows page.')
def verify_workflow_page_after_closing_create_workflow_page():
    assert CONFIGURATION_SETTING_PAGE.get_workflows_title() == "Workflows"


# @LA-103680
@when('the user clicks the "Create Workflow" button & enters the workflow name')
def add_required_details():
    CONFIGURATION_SETTING_PAGE.click_create_workflow_button()
    CONFIGURATION_SETTING_PAGE.enter_new_workflow_name(AD.workflow_name)


@then(
    'the user selects the the behaviour, coaching status from the dropdowns and the user gives a custom score & the user clicks on save button')
def select_required_fields_in_create_workflow_page():
    CONFIGURATION_SETTING_PAGE.click_behaviour_dropdown()
    CONFIGURATION_SETTING_PAGE.select_the_behaviour_from_dropdown()
    CONFIGURATION_SETTING_PAGE.click_coaching_status_dropdown()
    CONFIGURATION_SETTING_PAGE.select_the_coaching_status_from_dropdown()
    CONFIGURATION_SETTING_PAGE.enter_a_custom_score(AD.custom_score)
    CONFIGURATION_SETTING_PAGE.click_add_behavior_button()
    CONFIGURATION_SETTING_PAGE.click_behaviour_dropdown_duplicate()
    CONFIGURATION_SETTING_PAGE.select_the_behaviour_from_dropdown_duplicate()
    CONFIGURATION_SETTING_PAGE.click_coaching_status_dropdown_duplicate()
    CONFIGURATION_SETTING_PAGE.select_the_coaching_status_from_dropdown_duplicate()
    CONFIGURATION_SETTING_PAGE.enter_a_custom_score_duplicate(AD.custom_score)
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


# @PHNX-4284
@when('the user clicks the "Create Workflow" button & enters the existing workflow name')
def add_existing_workflow_name():
    CONFIGURATION_SETTING_PAGE.click_create_workflow_button()
    CONFIGURATION_SETTING_PAGE.enter_new_workflow_name(AD.workflow_name)
    CONFIGURATION_SETTING_PAGE.click_behaviour_dropdown()
    CONFIGURATION_SETTING_PAGE.select_the_behaviour_from_dropdown()
    CONFIGURATION_SETTING_PAGE.click_coaching_status_dropdown()
    CONFIGURATION_SETTING_PAGE.select_the_coaching_status_from_dropdown()
    CONFIGURATION_SETTING_PAGE.enter_a_custom_score(AD.custom_score)
    CONFIGURATION_SETTING_PAGE.click_save_button()


@then('the user should be able to see an error message "Duplicate workflow name. Please enter a unique name."')
def verify_duplicate_workflow_name_error_message():
    assert CONFIGURATION_SETTING_PAGE.get_duplicate_workflow_name_error_message() == "Duplicate workflow name. Please enter a unique name."


# @LQ-101429
@when('the user clicks on the "Groups" icon present next to the newly created workflow and select group and clicks on "Save" button')
def click_groups_icon():
    CONFIGURATION_SETTING_PAGE.click_cancel_button_edit_workflow_page()
    CONFIGURATION_SETTING_PAGE.click_groups_button()
    CONFIGURATION_SETTING_PAGE.click_modify_groups_button_in_groups_popup()
    CONFIGURATION_SETTING_PAGE.click_search_by_group_field()
    CONFIGURATION_SETTING_PAGE.search_group_filter(AD.coaching_workflow_group)
    CONFIGURATION_SETTING_PAGE.select_group()
    CONFIGURATION_SETTING_PAGE.click_done_button_in_groups_popup()
    CONFIGURATION_SETTING_PAGE.click_save_button_in_groups_popup()
    CONFIGURATION_SETTING_PAGE.close_groups_page()


@then('the selected groups should be listed under the respective workflow.')
def verify_selected_group_in_workflow_page():
    CONFIGURATION_SETTING_PAGE.click_group_filter_button()
    CONFIGURATION_SETTING_PAGE.click_search_by_group_field()
    CONFIGURATION_SETTING_PAGE.search_group_filter(AD.coaching_workflow_group)
    CONFIGURATION_SETTING_PAGE.select_group()
    CONFIGURATION_SETTING_PAGE.click_group_done_button()
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


@then('the user should see "Edit Workflow" page coming from the bottom and a Description & Note text')
def verify_edit_workflow_page():
    assert CONFIGURATION_SETTING_PAGE.get_edit_workflow_title() == "Edit Workflow"
    assert CONFIGURATION_SETTING_PAGE.description_text() == "Manage your company’s event handling rules, enabled behaviors, their respective scores, and how these settings impact coaching and driver safety program."
    assert CONFIGURATION_SETTING_PAGE.note_text() == "Note: Some fields are locked and can’t be edited directly. For updates or questions, please contact your Customer Success Manager or"


# @LQ-104043
@when('the user clicks the "Cancel" button without doing any changes')
def click_cancel_button():
    CONFIGURATION_SETTING_PAGE.click_cancel_button_edit_workflow_page()


@then('the user should be redirected to the Workflows page without any pop-up message.')
def verify_workflow_page():
    assert CONFIGURATION_SETTING_PAGE.get_workflows_title() == "Workflows"


# LQ-161146
@when('the user clicks the "X" icon present at the top right corner of the Edit Workflow modal')
def click_close_icon_in_create_workflow_page():
    CONFIGURATION_SETTING_PAGE.click_edit_button()
    CONFIGURATION_SETTING_PAGE.click_close_icon_in_create_workflow_page()


@then('the user should be redirected to the Workflows page.')
def verify_workflow_page_after_closing_edit_workflow_page():
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
@when('the user edit behavior, or Coaching status or custom score and remove the behaviour & coaching status')
def edit_existing_workflow():
    CONFIGURATION_SETTING_PAGE.click_edit_button()
    CONFIGURATION_SETTING_PAGE.delete_existing_behaviour()
    CONFIGURATION_SETTING_PAGE.remove_existing_behavior()
    CONFIGURATION_SETTING_PAGE.remove_existing_coaching_status()
    CONFIGURATION_SETTING_PAGE.click_behaviour_dropdown()
    CONFIGURATION_SETTING_PAGE.select_the_behaviour_from_dropdown()
    CONFIGURATION_SETTING_PAGE.click_coaching_status_dropdown()
    CONFIGURATION_SETTING_PAGE.select_the_coaching_status_from_dropdown()
    CONFIGURATION_SETTING_PAGE.enter_a_custom_score(AD.custom_score)


@then('the user should able save the changes')
def save_the_new_changes():
    CONFIGURATION_SETTING_PAGE.click_save_button()


@then('user should be navigated to the Workflows page with the success pop-up message "Successfully updated the '
      'workflow"')
def verify_the_popup_message():
    assert CONFIGURATION_SETTING_PAGE.get_workflows_title() == "Workflows"
    assert CONFIGURATION_SETTING_PAGE.get_update_popup_message() == "Successfully updated the workflow"


# @PHNX-4284
@when('the user clicks the "Edit Workflow" button & enters the existing workflow name')
def edit_existing_workflow_name():
    CONFIGURATION_SETTING_PAGE.click_cancel_button_edit_workflow_page()
    CONFIGURATION_SETTING_PAGE.click_reset_button()
    CONFIGURATION_SETTING_PAGE.click_search_filed_in_workflow_page()
    CONFIGURATION_SETTING_PAGE.enter_newly_created_workflow_name(AD.existing_workflow_name)
    assert CONFIGURATION_SETTING_PAGE.get_first_workflow_name() == AD.existing_workflow_name
    CONFIGURATION_SETTING_PAGE.click_edit_button()
    CONFIGURATION_SETTING_PAGE.enter_existing_workflow_name(AD.workflow_name)
    CONFIGURATION_SETTING_PAGE.click_save_button()


@then('the user should be able to see an error message "Duplicate workflow name. Please enter a unique name."')
def verify_duplicate_workflow_name_error_message():
    assert CONFIGURATION_SETTING_PAGE.get_duplicate_workflow_name_error_message() == "Duplicate workflow name. Please enter a unique name."


# @PHNX-4284
@when('the user clicks the "Duplicate Workflow" button & enters the existing workflow name')
def add_existing_workflow_name_in_duplicate_workflow_page():
    CONFIGURATION_SETTING_PAGE.click_cancel_button_edit_workflow_page()
    CONFIGURATION_SETTING_PAGE.click_discard_changes_popup()
    CONFIGURATION_SETTING_PAGE.click_duplicate_button_of_a_workflow()
    CONFIGURATION_SETTING_PAGE.enter_new_workflow_name(AD.workflow_name)
    CONFIGURATION_SETTING_PAGE.click_save_button()


@then('the user should be able to see an error message "Duplicate workflow name. Please enter a unique name."')
def verify_duplicate_workflow_name_error_message_in_duplicate_workflow_page():
    assert CONFIGURATION_SETTING_PAGE.get_duplicate_workflow_name_error_message() == "Duplicate workflow name. Please enter a unique name."


# @lQ-105045
@when('the user clicks the Duplicate icon of any workflow which is present next to Groups icon.')
def duplicate_the_workflow():
    CONFIGURATION_SETTING_PAGE.click_cancel_button_edit_workflow_page()
    CONFIGURATION_SETTING_PAGE.click_reset_button()
    CONFIGURATION_SETTING_PAGE.click_search_filed_in_workflow_page()
    CONFIGURATION_SETTING_PAGE.enter_newly_created_workflow_name(AD.workflow_name)
    assert CONFIGURATION_SETTING_PAGE.get_first_workflow_name() == AD.workflow_name
    CONFIGURATION_SETTING_PAGE.click_duplicate_button_of_a_workflow()


@then('the user should be navigated to "Create Workflow" page with the respective rules of the selected workflow')
def verify_create_workflow_page_is_displayed():
    assert CONFIGURATION_SETTING_PAGE.get_create_workflow_title() == "Create Workflow"



@then('the user inputs a unique workflow name and the user should be able to change any behaviors,coaching status or '
      'custom score.')
def enter_unique_workflow_name():
    CONFIGURATION_SETTING_PAGE.enter_new_workflow_name(AD.duplicate_workflow_name)


@then('the user should be able to add new rule using "+Add" button and the user clicks "Save" button.')
def add_new_rule():
    CONFIGURATION_SETTING_PAGE.click_add_behavior_button()
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


#@PHNX-4054
@when('the user clicks the "Create Workflow" button & enters the workflow name')
def add_required_details_phnx_5054():
    CONFIGURATION_SETTING_PAGE.click_create_workflow_button()
    CONFIGURATION_SETTING_PAGE.enter_new_workflow_name(AD.workflow_name)


@then('the user selects the behaviour from the dropdown and sets the score less than the default value')
def select_required_fields_in_create_workflow_page_phnx_5054():
    CONFIGURATION_SETTING_PAGE.click_behaviour_dropdown()
    CONFIGURATION_SETTING_PAGE.select_the_behaviour_from_dropdown()
    CONFIGURATION_SETTING_PAGE.click_coaching_status_dropdown()
    CONFIGURATION_SETTING_PAGE.select_the_coaching_status_from_dropdown()
    CONFIGURATION_SETTING_PAGE.enter_a_custom_score(AD.negative_custom_score)
    CONFIGURATION_SETTING_PAGE.click_save_button()


@then('the user should be able to save the changes without any loading issue')
def verify_coaching_workflow_page_is_displayed():
    assert CONFIGURATION_SETTING_PAGE.get_workflows_title() == "Workflows"
    assert CONFIGURATION_SETTING_PAGE.get_first_workflow_name() == AD.workflow_name
    CONFIGURATION_SETTING_PAGE.click_delete_button()
    CONFIGURATION_SETTING_PAGE.click_delete_in_popup()