from hamcrest import contains_string, assert_that
from pytest_bdd import scenarios, given, when, then
from pages.dashboard_page import DashboardPage
from pages.equipment_management_page import EquipmentManagementPage
from pages.login_page import LoginPage
from pages.user_management_page import UserManagementPage
from steps.common import DC_URL, ENV, NEW_UI_FTM_URL
from data.int.admin_data_int import AdminDataInt as AD_INT
from data.prod.admin_data_prod import AdminDataProd as AD_PROD
from data.stg.admin_data_stg import AdminDataStg as AD_STG

LOGIN_PAGE = 0
DASHBOARD_PAGE = 0
EQUIPMENT_MANAGEMENT_PAGE = 0
USER_MANAGEMENT_PAGE = 0
AD = 0

scenarios('../features/admin_equipment_management_new_ui_shell.feature')


# LQ-7126
@given('the "Program Manager" user is in Admin')
def navigate_to_admin_page(browser):
    global LOGIN_PAGE, DASHBOARD_PAGE, USER_MANAGEMENT_PAGE, EQUIPMENT_MANAGEMENT_PAGE, AD

    LOGIN_PAGE = LoginPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)
    EQUIPMENT_MANAGEMENT_PAGE = EquipmentManagementPage(browser)
    USER_MANAGEMENT_PAGE = UserManagementPage(browser)

    browser.get(NEW_UI_FTM_URL)

    if ENV == 'int':
        AD = AD_INT
    elif ENV == 'stg':
        AD = AD_STG
    elif ENV == 'prod':
        AD = AD_PROD

    LOGIN_PAGE.wait_for_page_to_fully_load()
    LOGIN_PAGE.enter_username(AD.pm_fa_user_name)
    LOGIN_PAGE.enter_password(AD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    DASHBOARD_PAGE.click_admin_tab()


@when('the user clicks the "EQUIPMENT" tab')
def navigate_to_equipment_management_page():
    EQUIPMENT_MANAGEMENT_PAGE.click_equipment()


@then(
    'the page header "EQUIPMENT MANAGEMENT" is displayed and the table is displayed with columns: "EQUIPMENT", "DEVICE", "GROUP", "LAST CONNECTED", "STATUS"')
def verify_user_management_tabs():
    assert EQUIPMENT_MANAGEMENT_PAGE.get_equipment_management_title_text() == "EQUIPMENT MANAGEMENT"
    assert EQUIPMENT_MANAGEMENT_PAGE.get_equipment_column_name_text() == "EQUIPMENT"
    assert EQUIPMENT_MANAGEMENT_PAGE.get_device_column_name_text() == "DEVICE"
    assert EQUIPMENT_MANAGEMENT_PAGE.get_group_column_name_text() == "GROUP"
    assert EQUIPMENT_MANAGEMENT_PAGE.get_last_connected_column_name_text() == "LAST CONNECTED"
    assert EQUIPMENT_MANAGEMENT_PAGE.get_status_column_name_text() == "STATUS"


@then('the user should be able to see the filters like "Select Group(s)","Last Connected","Status", "Select Search" and "Reset"')
def user_should_see_all_filters():
    assert EQUIPMENT_MANAGEMENT_PAGE.group_filter_is_displayed()
    assert EQUIPMENT_MANAGEMENT_PAGE.last_connected_filter_is_displayed()
    assert EQUIPMENT_MANAGEMENT_PAGE.status_filter_is_displayed()
    assert EQUIPMENT_MANAGEMENT_PAGE.search_name_or_id_filter_is_displayed()
    assert EQUIPMENT_MANAGEMENT_PAGE.reset_button_is_displayed()


@then('the user should see the buttons "Move group", "Change Status", "Delete Equipment" and "More Options" disabled')
def move_group_change_status_and_other_button_displayed():
    assert EQUIPMENT_MANAGEMENT_PAGE.move_group_button_displayed()
    assert EQUIPMENT_MANAGEMENT_PAGE.change_status_button_displayed()
    assert EQUIPMENT_MANAGEMENT_PAGE.delete_equipment_button_displayed()
    assert EQUIPMENT_MANAGEMENT_PAGE.detach_device_button_displayed()


@then('the button "Add Equipment" enabled')
def add_equipment_button_is_enabled():
    assert EQUIPMENT_MANAGEMENT_PAGE.add_equipment_is_enabled()


@then('the user should see the pagination and "Download CSV" in the bottom of the page')
def pagination_is_displayed():
    assert EQUIPMENT_MANAGEMENT_PAGE.pagination_is_displayed()


# LQ-7125
@when(
    'the user clicks on "Add Equipment" and the user enters required fields: "Group" and "Equipment Name" and the user clicks "Create Equipment"')
def click_add_equipment():
    if EQUIPMENT_MANAGEMENT_PAGE.get_row_count() != 0:
        EQUIPMENT_MANAGEMENT_PAGE.delete_existing_equipment()

    EQUIPMENT_MANAGEMENT_PAGE.add_equipment_out_of_service("bot1")
    EQUIPMENT_MANAGEMENT_PAGE.add_equipment_out_of_service("bot3")
    EQUIPMENT_MANAGEMENT_PAGE.add_equipment_in_service("bot4")
    EQUIPMENT_MANAGEMENT_PAGE.add_equipment_spare("bot5")
    EQUIPMENT_MANAGEMENT_PAGE.add_equipment_in_service("bot6")
    EQUIPMENT_MANAGEMENT_PAGE.add_equipment_out_of_service("bot7")
    EQUIPMENT_MANAGEMENT_PAGE.click_reset()


@then('the equipment is added')
def verify_equipment_is_added():
    assert_that(EQUIPMENT_MANAGEMENT_PAGE.get_new_equipment_text('bot1'), contains_string('bot1'))


# LQ-7127
@when('the user clicks a created equipment, modifies required fields: “Group” and “Equipment Name”, and clicks “Save”')
def edit_equipment():
    EQUIPMENT_MANAGEMENT_PAGE.click_first_equipment_in_list()
    EQUIPMENT_MANAGEMENT_PAGE.clear_equipment_name()
    EQUIPMENT_MANAGEMENT_PAGE.enter_equipment_name("bot2")
    EQUIPMENT_MANAGEMENT_PAGE.click_create_equipment()
    EQUIPMENT_MANAGEMENT_PAGE.click_reset()


@then('the equipment is modified and saved')
def verify_equipment_is_modified():
    assert_that(EQUIPMENT_MANAGEMENT_PAGE.get_new_equipment_text('bot2'), contains_string('bot2'))


# LQ-7136
@when(
    'the user selects a created equipment, selects “Change Status” button, clicks the "Select Status" dropdown button, selects "In Service", and clicks "Apply" button')
def select_in_service():
    EQUIPMENT_MANAGEMENT_PAGE.click_first_checkbox()
    EQUIPMENT_MANAGEMENT_PAGE.click_change_status()
    EQUIPMENT_MANAGEMENT_PAGE.click_select_status()
    EQUIPMENT_MANAGEMENT_PAGE.select_in_service()
    EQUIPMENT_MANAGEMENT_PAGE.click_apply()
    EQUIPMENT_MANAGEMENT_PAGE.click_reset()
    EQUIPMENT_MANAGEMENT_PAGE.click_search_drop_down()
    EQUIPMENT_MANAGEMENT_PAGE.click_equipment_in_drop_down()
    EQUIPMENT_MANAGEMENT_PAGE.enter_equipment_name_in_search("bot2")


@then('the selected equipment is changed to "In Service" status')
def verify_in_service():
    assert_that(EQUIPMENT_MANAGEMENT_PAGE.get_status_text('In Service'), contains_string('In Service'))


@when(
    'the user selects a created equipment, selects “Change Status” button, clicks the "Select Status" dropdown button, selects "Out of Service", and clicks "Apply" button')
def select_out_of_service():
    EQUIPMENT_MANAGEMENT_PAGE.click_first_checkbox()
    EQUIPMENT_MANAGEMENT_PAGE.click_change_status()
    EQUIPMENT_MANAGEMENT_PAGE.click_select_status()
    EQUIPMENT_MANAGEMENT_PAGE.select_out_of_service()
    EQUIPMENT_MANAGEMENT_PAGE.click_apply()
    EQUIPMENT_MANAGEMENT_PAGE.click_reset()
    EQUIPMENT_MANAGEMENT_PAGE.click_refresh_button()
    EQUIPMENT_MANAGEMENT_PAGE.wait_for_page_to_fully_load()


@then('the selected equipment is changed to "Out of Service" status')
def verify_out_of_service():
    assert_that(EQUIPMENT_MANAGEMENT_PAGE.get_status_text('Out Of Service'), contains_string('Out Of Service'))


@when(
    'the user selects a created equipment, selects “Change Status” button, clicks the "Select Status" dropdown button, selects "Spare", and clicks "Apply" button')
def select_spare():
    EQUIPMENT_MANAGEMENT_PAGE.click_first_checkbox()
    EQUIPMENT_MANAGEMENT_PAGE.click_change_status()
    EQUIPMENT_MANAGEMENT_PAGE.click_select_status()
    EQUIPMENT_MANAGEMENT_PAGE.select_spare()
    EQUIPMENT_MANAGEMENT_PAGE.click_apply()
    EQUIPMENT_MANAGEMENT_PAGE.click_search_drop_down()
    EQUIPMENT_MANAGEMENT_PAGE.click_equipment_in_drop_down()
    EQUIPMENT_MANAGEMENT_PAGE.enter_equipment_name_in_search("bot2")


@then('the searched equipment will be displayed on the page and has status Spare')
def verify_searched_equipment_with_status_spare():
    assert_that(EQUIPMENT_MANAGEMENT_PAGE.get_new_equipment_text('bot2'), contains_string('bot2'))
    assert_that(EQUIPMENT_MANAGEMENT_PAGE.get_status_text('Spare'), contains_string('Spare'))
    EQUIPMENT_MANAGEMENT_PAGE.click_reset()


# LQ-7129
@when('the user clicks the filter “Select Group(s)” and the user selects groups')
def select_group():
    EQUIPMENT_MANAGEMENT_PAGE.click_select_group()
    EQUIPMENT_MANAGEMENT_PAGE.select_root_group()
    EQUIPMENT_MANAGEMENT_PAGE.click_done_on_select_group()


@then(
    'the equipment list will be updated by the selected group and Equipment column values should be in ascending order')
def verify_equipment_by_group():
    assert_that(EQUIPMENT_MANAGEMENT_PAGE.get_new_equipment_text('bot2'), contains_string('bot2'))
    EQUIPMENT_MANAGEMENT_PAGE.click_reset()


# LQ-7130
@when('the user clicks the filter Status and the user selects "In Service"')
def filter_status_select_in_service():
    EQUIPMENT_MANAGEMENT_PAGE.click_eq_management_status_drop_down()
    EQUIPMENT_MANAGEMENT_PAGE.select_eq_management_in_service_status()


@then('the equipment list will be updated by the "In Service" and Equipment column values should be in ascending order')
def verify_equipment_by_in_service():
    assert EQUIPMENT_MANAGEMENT_PAGE.get_row_count() == 2
    assert_that(EQUIPMENT_MANAGEMENT_PAGE.get_new_equipment_text('bot4'), contains_string('bot4'))
    EQUIPMENT_MANAGEMENT_PAGE.click_reset()


@when('the user clicks the filter Status and the user selects "Out of Service"')
def filter_status_select_out_of_service():
    EQUIPMENT_MANAGEMENT_PAGE.click_eq_management_status_drop_down()
    EQUIPMENT_MANAGEMENT_PAGE.clear_eq_management_status_drop_down()
    EQUIPMENT_MANAGEMENT_PAGE.click_eq_management_status_drop_down()
    EQUIPMENT_MANAGEMENT_PAGE.select_eq_management_out_of_service_status()


@then(
    'the equipment list will be updated by the "Out of Service" and Equipment column values should be in ascending order')
def verify_equipment_by_out_of_service():
    assert EQUIPMENT_MANAGEMENT_PAGE.get_row_count() == 2
    assert_that(EQUIPMENT_MANAGEMENT_PAGE.get_new_equipment_text('bot3'), contains_string('bot3'))
    EQUIPMENT_MANAGEMENT_PAGE.click_reset()


@when('the user clicks the filter Status and the user selects "Spare"')
def filter_status_select_spare():
    EQUIPMENT_MANAGEMENT_PAGE.click_eq_management_status_drop_down()
    EQUIPMENT_MANAGEMENT_PAGE.select_eq_management_spare_status()


@then('the equipment list will be updated by the "Spare" and Equipment column values should be in ascending order')
def verify_equipment_by_spare():
    assert EQUIPMENT_MANAGEMENT_PAGE.get_row_count() == 2
    assert_that(EQUIPMENT_MANAGEMENT_PAGE.get_status_text('Spare'), contains_string('Spare'))
    assert_that(EQUIPMENT_MANAGEMENT_PAGE.get_new_equipment_text('bot2'), contains_string('bot2'))
    EQUIPMENT_MANAGEMENT_PAGE.click_reset()


# LQ-7133
@when('the user clicks the filter "Last Connected" and the user selects date range and the user clicks Apply button')
def filter_last_connected_filter():
    EQUIPMENT_MANAGEMENT_PAGE.click_last_connected_filter()
    EQUIPMENT_MANAGEMENT_PAGE.select_last_30_days()
    EQUIPMENT_MANAGEMENT_PAGE.click_apply_last_connected()


@then('the equipment list will be updated by the selected last connected date')
def verify_equipment_by_last_connected():
    assert EQUIPMENT_MANAGEMENT_PAGE.get_row_count() == 0
    EQUIPMENT_MANAGEMENT_PAGE.click_reset()


# LQ-7132
@when(
    'the user selects a created equipment and the user selects “Move Group” and the user selects a group and the user clicks Done on pop up window and the user clicks Continue button')
def move_group_equipment():
    EQUIPMENT_MANAGEMENT_PAGE.select_first_equipment()
    EQUIPMENT_MANAGEMENT_PAGE.click_move_group()
    EQUIPMENT_MANAGEMENT_PAGE.search_group(AD.group)
    EQUIPMENT_MANAGEMENT_PAGE.select_searched_group()
    EQUIPMENT_MANAGEMENT_PAGE.click_done_button_move_group()
    EQUIPMENT_MANAGEMENT_PAGE.click_continue_button()


@then('the equipment group is moved to the selected group')
def verify_move_group():
    EQUIPMENT_MANAGEMENT_PAGE.click_first_equipment_in_list()
    assert_that(EQUIPMENT_MANAGEMENT_PAGE.get_equipment_group(), contains_string(AD.group))
    EQUIPMENT_MANAGEMENT_PAGE.click_cancel_button()


# LQ-7682
@when('the user checks some available equipment and the user clicks "Delete Equipment" and the user clicks "Confirm"')
def delete_equipment():
    # delete all added equipment for next run
    EQUIPMENT_MANAGEMENT_PAGE.click_reset()
    EQUIPMENT_MANAGEMENT_PAGE.click_select_all_checkbox()
    EQUIPMENT_MANAGEMENT_PAGE.click_delete_equipment_button()
    EQUIPMENT_MANAGEMENT_PAGE.click_confirm_button_delete_equipment()
    EQUIPMENT_MANAGEMENT_PAGE.click_reset()


@then('the selected equipment are deleted')
def verify_equipment_deleted():
    assert EQUIPMENT_MANAGEMENT_PAGE.get_row_count() == 0


# LQ-7131
@given('the "Program Manager" user is in the Equipment Management page')
def login_and_go_to_equipment_page(browser):
    browser.get(DC_URL)
    LOGIN_PAGE.enter_username(AD.user_name_equipment)
    LOGIN_PAGE.enter_password(AD.password_equipment)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed_new_ui(DC_URL, AD.user_name_equipment, AD.password_equipment, AD.company_name)
    DASHBOARD_PAGE.click_admin_tab()
    EQUIPMENT_MANAGEMENT_PAGE.click_equipment()


@when(
    'the user selects a device that is bound to an equipment and the user selects “Detach Device” and the user clicks the Apply button')
def detach_equipment():
    EQUIPMENT_MANAGEMENT_PAGE.click_search_drop_down()
    EQUIPMENT_MANAGEMENT_PAGE.click_equipment_in_drop_down()
    EQUIPMENT_MANAGEMENT_PAGE.enter_equipment_name_in_search(AD.equipment)

    # clear dirty data if any
    if EQUIPMENT_MANAGEMENT_PAGE.device_1st_equipment(AD.equipment_device) == '':
        EQUIPMENT_MANAGEMENT_PAGE.click_first_equipment_in_list()
        EQUIPMENT_MANAGEMENT_PAGE.click_equipment_status()
        EQUIPMENT_MANAGEMENT_PAGE.select_in_service_equipment_status()
        EQUIPMENT_MANAGEMENT_PAGE.search_and_select_device_equipment(AD.equipment_device)
        EQUIPMENT_MANAGEMENT_PAGE.click_create_equipment()
        if EQUIPMENT_MANAGEMENT_PAGE.click_move_and_continue() is True:
            EQUIPMENT_MANAGEMENT_PAGE.click_move_and_continue()

    EQUIPMENT_MANAGEMENT_PAGE.click_first_checkbox()
    EQUIPMENT_MANAGEMENT_PAGE.click_detach_device()
    EQUIPMENT_MANAGEMENT_PAGE.click_apply_detach()


@then(
    'the "Success - x Equipment detached from the device" confirmation popup should come and the equipment is in Out of Service status and the device is not bound to this equipment')
def verify_detach_equipment():
    assert EQUIPMENT_MANAGEMENT_PAGE.get_detach_message('Success', 20,
                                                        1) == 'Success - 1 equipment detached from a device.'
    assert EQUIPMENT_MANAGEMENT_PAGE.get_status_text('Out Of Service') == 'Out Of Service'
    assert EQUIPMENT_MANAGEMENT_PAGE.device_1st_equipment('', 1) == ''

# LQ-290195
@given('FA user login to the application')
def internal_fa_user_login(browser):
    LOGIN_PAGE.click_humanoid()
    LOGIN_PAGE.click_sign_out_new_ui()
    browser.get(NEW_UI_FTM_URL)
    LOGIN_PAGE.enter_username(AD.fa_user_drivecam)
    LOGIN_PAGE.enter_password(AD.fa_password_drivecam)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.wait_for_page_to_fully_load()
    DASHBOARD_PAGE.click_admin_tab()
    EQUIPMENT_MANAGEMENT_PAGE.click_equipment()


@when('the user is on the first page of equipment management list')
def navigate_to_first_page_equipment_management():
    USER_MANAGEMENT_PAGE.scroll_page_down()

@then('the Previous button in the pagination section is disabled and 1st page is selected by default')
def verify_first_page_equipment_management():
    assert USER_MANAGEMENT_PAGE.previous_page_button_is_disabled()

@when('the user clicks on the Next button in the pagination section')
def click_next_page_equipment_management():
    USER_MANAGEMENT_PAGE.click_next_page_button()

@then('the next page of equipment management list is displayed and page 2 is selected')
def verify_next_page_equipment_management():
    assert USER_MANAGEMENT_PAGE.get_current_page_number() == 2

@when('the user clicks on the Previous button in the pagination section')
def click_previous_page_equipment_management():
    USER_MANAGEMENT_PAGE.click_previous_page_button()

@then('the previous page of equipment management list is displayed and page 1 is selected')
def verify_previous_page_equipment_management():
    assert USER_MANAGEMENT_PAGE.get_current_page_number() == 1

@when('the user clicks last page number in the pagination section')
def enter_last_page_number_equipment_management():
    USER_MANAGEMENT_PAGE.click_last_page_button()

@then('the equipment management list navigates to last page and the Next button in the pagination section is disabled')
def verify_last_page_equipment_management():
    assert USER_MANAGEMENT_PAGE.next_page_button_is_disabled()
