from time import sleep

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

import pytest

@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

@pytest.fixture
def dashboard_page(browser):
    return DashboardPage(browser)

@pytest.fixture
def configuration_setting_page(browser):
    return ConfigurationSettingPage(browser)

@pytest.fixture
def user_management_page(browser):
    return UserManagementPage(browser)

@pytest.fixture
def trailer_management_page(browser):
    return TrailerManagementPage(browser)

@pytest.fixture
def add_trailer_page(browser):
    return AddTrailerPage(browser)

@pytest.fixture
def edit_trailer_page(browser):
    return EditTrailerPage(browser)

@pytest.fixture
def ad():
    if ENV == 'int':
        return AD_INT
    elif ENV == 'stg':
        return AD_STG
    else:
        return AD_PROD

@pytest.fixture
def tabn():
    t = AddUserPage(BasePage)
    t.get_random_string()
    t.get_random_name(6)
    return t

scenarios('../features/admin_trailer_workflow.feature')


# LQ-242
@given('Administrator user is in Admin')
def login_as_admin(browser, login_page, dashboard_page, user_management_page, trailer_management_page, configuration_setting_page, add_trailer_page, edit_trailer_page, ad, tabn):
    browser.get(DC_URL)
    login_page.enter_username(ad.autobots_full_access_username)
    login_page.enter_password(ad.password2)
    login_page.click_login()
    dashboard_page.click_admin_tab()


# LQ-12128
@when('the user performs the Trailer Management workflow')
def go_to_trailer_management_page(trailer_management_page):
    trailer_management_page.click_trailer_tab()


@then(
    'a trailer can be added, edited, have inspection lists set, and be filtered by group, and then deleted.')
def verify_trailer_management_page(trailer_management_page, add_trailer_page, edit_trailer_page, ad, tabn):
    assert trailer_management_page.get_trailer_management_text() == "TRAILER MANAGEMENT"
    assert trailer_management_page.get_trailer_column_text() == "TRAILER"
    assert trailer_management_page.get_group_column_text() == "GROUP"
    assert trailer_management_page.get_license_plate_column_text() == "LICENSE PLATE"
    assert trailer_management_page.get_vin_column_text() == "VIN"
    assert trailer_management_page.get_inspection_list_column_text() == "INSPECTION LIST"

    # Add Trailer
    trailer_management_page.click_add_trailer_button()
    add_trailer_page.click_group_trailer_filter()
    add_trailer_page.search_group_trailer_filter(ad.group)
    add_trailer_page.select_searched_group()
    add_trailer_page.click_done_trailer_group_button()
    add_trailer_page.type_trailer_name(tabn.random_name)
    add_trailer_page.type_vin_number(tabn.random_word)
    add_trailer_page.click_create_trailer()

    trailer_management_page.search_trailer_name(tabn.random_name)
    assert trailer_management_page.get_searched_trailer_name(tabn.random_name) == tabn.random_name

    # Edit Trailer
    trailer_management_page.click_added_trailer_name()
    edit_trailer_page.clear_trailer_name()
    edit_trailer_page.edit_first_name_trailer(tabn.random_word)
    edit_trailer_page.click_save_trailer()
    sleep(5)
    trailer_management_page.click_reset_button()
    trailer_management_page.search_trailer_name(tabn.random_word)
    assert trailer_management_page.get_searched_trailer_name(tabn.random_word) == tabn.random_word

    # Delete Trailer
    trailer_management_page.click_added_trailer_name()
    trailer_management_page.click_delete_trailer_button()
    trailer_management_page.click_continue_to_delete_trailer_button()
    assert trailer_management_page.trailer_deleted_message_is_displayed() is True
    assert trailer_management_page.no_trailers_found_message_is_displayed() is True
