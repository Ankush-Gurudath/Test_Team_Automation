from pytest_bdd import scenarios, given, when, then

from pages.base_page import BasePage
from pages.behaviors_report_page import BehaviorsReportPage
from pages.login_page import LoginPage
from pages.risk_company import RiskCompanyPage
from steps.common import DC_URL, ENV
from data.int.risk_company_data_int import RiskCompanyDataInt as RCD_INT
from data.prod.risk_company_data_prod import RiskCompanyDataProd as RCD_PROD
from data.stg.risk_company_data_stg import RiskCompanyDataStg as RCD_STG

LOGIN_PAGE = 0
RISK_COMPANY_PAGE = 0
BEHAVIORS_REPORT_PAGE = 0
BASE_PAGE = 0
RCD = 0

scenarios('../features/ws_rds.feature')


# LQ-373
@given('the welcome login page is displayed')
def launch_welcome_login_page(browser):
    global LOGIN_PAGE, RISK_COMPANY_PAGE, BEHAVIORS_REPORT_PAGE, RCD, BASE_PAGE

    LOGIN_PAGE = LoginPage(browser)
    RISK_COMPANY_PAGE = RiskCompanyPage(browser)
    BEHAVIORS_REPORT_PAGE = BehaviorsReportPage(browser)
    BASE_PAGE = BasePage(browser)

    browser.get(DC_URL)

    if ENV == 'int':
        RCD = RCD_INT
    elif ENV == 'stg':
        RCD = RCD_STG
    else:
        RCD = RCD_PROD


@when('the user login WS for a risk company')
def login_risk_company():
    LOGIN_PAGE.enter_username(RCD.risk_fa_user)
    LOGIN_PAGE.enter_password(RCD.password)
    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed(DC_URL, RCD.risk_fa_user, RCD.password)


@then('the Dashboard page is displayed and the Dashboard page includes "Drivers by Highest Score","Categories by Highest Frequency" and And the Dashboard page includes a driver counts, Group filter, Date filter')
def assert_dashboard_page():
    assert RISK_COMPANY_PAGE.get_dashboard_text() == "DASHBOARD"
    assert RISK_COMPANY_PAGE.get_drivers_by_highest_score_text() == "Drivers by Highest Score"
    assert RISK_COMPANY_PAGE.get_categories_by_highest_frequency_text() == "Categories by Highest Frequency"
    assert RISK_COMPANY_PAGE.driver_count_displayed() is True
    assert RISK_COMPANY_PAGE.group_filter_displayed() is True
    assert RISK_COMPANY_PAGE.date_filter_displayed() is True


# LQ-375
@when('the user clicks "View Details"')
def click_view_detail():
    RISK_COMPANY_PAGE.click_view_details()


@then('the Driver Report page is opened')
def verify_rds_page_title():
    assert BEHAVIORS_REPORT_PAGE.get_driver_report_text() == "DRIVERS REPORT"


# LQ-376

@given(
    'the "Safety Manager" user is on Dashboard page of company A & the dcops key "DC_EnableCoaching" is false of company A')
def navigate_to_dashboard_page():
    RISK_COMPANY_PAGE.click_home_tab_new_ui()


@when('the user sets group filter to one group in dashboard page')
def set_group_filter_dashboard():
    RISK_COMPANY_PAGE.click_filter_group_dashboard()
    RISK_COMPANY_PAGE.search_group_filter_dashboard("Vehicle")
    RISK_COMPANY_PAGE.click_searched_group_filter()
    RISK_COMPANY_PAGE.click_done_group_filter()


@then('the data belong to the selected group are displayed in dashboard page')
def verify_group_filter_dashboard():
    RISK_COMPANY_PAGE.click_view_details()
    assert BEHAVIORS_REPORT_PAGE.get_row_count() == 0


@when('the user sets date filter in dashboard page')
def set_date_filter_dashboard():
    RISK_COMPANY_PAGE.click_home_tab_new_ui()
    RISK_COMPANY_PAGE.click_date_filter()
    RISK_COMPANY_PAGE.click_date1_filter()
    RISK_COMPANY_PAGE.click_date2_filter()
    RISK_COMPANY_PAGE.click_apply_date_filter()


@then('the data belong to the selected date range are displayed in dashboard page')
def verify_date_filter_dashboard():
    RISK_COMPANY_PAGE.click_view_details()
    assert BEHAVIORS_REPORT_PAGE.get_row_count() == 0


# LQ-378
@when('the user clicks "INSIGHTS" & the user clicks "DRIVERS REPORT"')
def navigate_to_drivers_report_page():
    RISK_COMPANY_PAGE.click_drivers_report_new_ui()


@then('the drivers report page is opened & there are 3 tabs： "Drivers Scores","Continual Behaviors", "Alerts" & the table of "Driver Scores" is displayed')
def verify_drivers_report_titles():
    assert RISK_COMPANY_PAGE.get_drivers_report_text() == "DRIVERS REPORT"
    assert RISK_COMPANY_PAGE.get_driver_scors_text() == "Driver Scores"
    assert RISK_COMPANY_PAGE.get_continual_behaviors_text() == "Continual Behaviors"
    assert RISK_COMPANY_PAGE.get_alerts_text() == "Alerts"
    assert RISK_COMPANY_PAGE.get_driver_text() == "DRIVER"
    assert RISK_COMPANY_PAGE.get_group_text() == "GROUP"
    assert RISK_COMPANY_PAGE.get_score_text() == "SCORE"
    assert RISK_COMPANY_PAGE.get_events_text() == "EVENTS"
    assert RISK_COMPANY_PAGE.get_recent_notes_text() == "RECENT NOTES"


# LQ-380
@when('the user selects some categories')
def select_categories_filter():
    RISK_COMPANY_PAGE.click_categories_filter()
    RISK_COMPANY_PAGE.select_categories_filter()


@then('the data belong to the selected categories are displayed')
def verify_categories_filter():
    assert RISK_COMPANY_PAGE.get_row_count() == 0
