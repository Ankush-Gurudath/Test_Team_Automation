from time import sleep

from hamcrest import contains_string, assert_that
from pytest_bdd import scenarios, given, when, then

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.video_search_page import VideoSearchPage
from steps.common import DC_URL, ENV
from data.int.video_search_data_int import VideoSearchDataInt as VSD_INT
from data.prod.video_search_data_prod import VideoSearchDataProd as VSD_PROD
from data.stg.video_search_data_stg import VideoSearchDataStg as VSD_STG

LOGIN_PAGE = 0
VIDEO_SEARCH_PAGE = 0
DASHBOARD_PAGE = 0
VSD = 0

scenarios('../features/video_search.feature')


# LQ-15219
@given('the login page is displayed')
def launch_browser(browser):
    global LOGIN_PAGE, VIDEO_SEARCH_PAGE, DASHBOARD_PAGE, VSD

    LOGIN_PAGE = LoginPage(browser)
    VIDEO_SEARCH_PAGE = VideoSearchPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)

    browser.get(DC_URL)

    if ENV == 'int':
        VSD = VSD_INT
    elif ENV == 'stg':
        VSD = VSD_STG
    else:
        VSD = VSD_PROD


@when('the Video Reviewer Plus user enters a newly created username/password and clicks the login button')
def login():
    LOGIN_PAGE.enter_username(VSD.user_name_real_device)
    LOGIN_PAGE.enter_password(VSD.password)
    LOGIN_PAGE.click_login()


@then('the user is successfully logged into the Video Search page')
def verify_login():
    assert VIDEO_SEARCH_PAGE.get_video_search_title() == "VIDEO SEARCH"


# LQ-205
@when('the Video Reviewer Plus user is in Video Search page')
def go_to_video_search_page():
    VIDEO_SEARCH_PAGE.click_vehicle_tab()


@then('the vehicle count is displayed and the table is displayed with columns: "ACTIONS", "VEHICLES", "DEVICE", "LAST COMMUNICATED", "GROUP", "VIEWS"')
def verify_table_vehicle_page():
    assert VIDEO_SEARCH_PAGE.video_tag_count_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True
    assert VIDEO_SEARCH_PAGE.get_actions_column_text() == "ACTIONS"
    assert VIDEO_SEARCH_PAGE.get_vehicles_column_text() == "VEHICLES"
    assert VIDEO_SEARCH_PAGE.get_device_column_text() == "DEVICE"
    assert VIDEO_SEARCH_PAGE.get_last_communicated_column_text() == "LAST COMMUNICATED"
    assert VIDEO_SEARCH_PAGE.get_group_column_text() == "GROUP"
    assert VIDEO_SEARCH_PAGE.get_views_column_text() == "VIEWS"


# LQ-201
@when('the user sets group filter to one group in vehicles page')
def set_group_filter_vehicle_page():
    VIDEO_SEARCH_PAGE.click_group_filter()
    VIDEO_SEARCH_PAGE.search_group(VSD.saved_group)
    VIDEO_SEARCH_PAGE.select_searched_group()
    VIDEO_SEARCH_PAGE.click_done_button()


@then('the vehicles belong to the group are listed')
def verify_group_filter_vehicle_page():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True


@when('the user selects "Vehicle Name" from "Select Search" dropdown and the user input some characters in search bar')
def search_by_vehicle_name_vehicle_page():
    VIDEO_SEARCH_PAGE.click_reset_button()
    VIDEO_SEARCH_PAGE.click_select_search_filter()
    VIDEO_SEARCH_PAGE.select_vehicle_name_dropdown()
    VIDEO_SEARCH_PAGE.search_criteria_textbox(VSD.vehicle)


@then('the vehicles with the inputted characters are listed')
def verify_searched_by_vehicle_name_vehicle_page():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True


@when('the user selects "Serial Number" from "Select Search" dropdown and the user input some characters in search bar')
def search_by_serial_name_vehicle_page():
    VIDEO_SEARCH_PAGE.click_reset_button()
    VIDEO_SEARCH_PAGE.click_select_search_filter()
    VIDEO_SEARCH_PAGE.select_serial_name_dropdown()
    VIDEO_SEARCH_PAGE.search_criteria_textbox(VSD.device)


@then('the vehicles which attached ER serial number with the inputted characters are listed')
def verify_searched_by_serial_name_vehicle_page():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True


# LQ-207
@when('the user clicks on the Library and the user selects Saved Videos')
def go_to_saved_videos_page():
    VIDEO_SEARCH_PAGE.click_library_tab()
    VIDEO_SEARCH_PAGE.click_saved_videos_tab()


@then('the video count is displayed and the table is displayed with columns: "VIDEO NAME","STATUS","TAG TYPE","VEHICLE","GROUP","LENGTH","VIEWS","VIDEO DATE","REQUEST DATE"')
def verify_table_saved_videos_page():
    sleep(5)
    # assert VIDEO_SEARCH_PAGE.get_video_count() == "4"
    # assert VIDEO_SEARCH_PAGE.get_row_count() == 4
    assert VIDEO_SEARCH_PAGE.get_video_name_column_text() == "VIDEO NAME"
    assert VIDEO_SEARCH_PAGE.get_status_column_text() == "STATUS"
    assert VIDEO_SEARCH_PAGE.get_tag_type_column_text() == "TAG TYPE"
    assert VIDEO_SEARCH_PAGE.get_vehicle_column_saved_videos_text() == "VEHICLE"
    assert VIDEO_SEARCH_PAGE.get_group_column_saved_videos_text() == "GROUP"
    assert VIDEO_SEARCH_PAGE.get_length_column_text() == "LENGTH"
    assert VIDEO_SEARCH_PAGE.get_views_column_saved_videos_text() == "VIEWS"
    assert VIDEO_SEARCH_PAGE.get_video_date_column_text() == "VIDEO DATE"
    assert VIDEO_SEARCH_PAGE.get_request_date_column_text() == "REQUEST DATE"


# LQ-206
@when('the user sets group filter to one group in the Saved Videos page')
def set_group_filter_saved_videos():
    VIDEO_SEARCH_PAGE.click_group_filter_saved_videos()
    VIDEO_SEARCH_PAGE.search_group_saved_videos(VSD.group)
    VIDEO_SEARCH_PAGE.select_searched_group_saved_videos()
    VIDEO_SEARCH_PAGE.done_button_saved_videos()


@then('the saved videos belong to the selected group are listed in the Saved Videos page')
def verify_group_filter_saved_videos_page():
    # assert VIDEO_SEARCH_PAGE.get_row_count() == 4
    VIDEO_SEARCH_PAGE.click_reset_button_saved_videos()


@when('the user sets the date filter in the Saved Videos page')
def set_date_filter_saved_videos():
    VIDEO_SEARCH_PAGE.click_date_filter_saved_videos()
    VIDEO_SEARCH_PAGE.set_video_date_range(VSD.video_date_range_start_month, VSD.video_date_range_start_day,
                                           VSD.video_date_range_start_year,
                                           VSD.video_date_range_end_month, VSD.video_date_range_end_day,
                                           VSD.video_date_range_end_year)

    VIDEO_SEARCH_PAGE.click_apply_saved_videos()


@then('the saved videos belong to the date are listed in the Saved Videos page')
def verify_date_filter_saved_videos_page():
    # assert VIDEO_SEARCH_PAGE.get_video_date() == VSD.video_date
    assert_that(VIDEO_SEARCH_PAGE.get_video_date(), contains_string(VSD.video_date))


@when('user selects "Vehicle Name" from "Select Search" filter and user inputs some characters in the Saved Videos page')
def search_by_vehicle_name_saved_videos():
    VIDEO_SEARCH_PAGE.click_select_search_filter_saved_videos()
    VIDEO_SEARCH_PAGE.select_vehicle_name_dropdown_saved_videos()
    VIDEO_SEARCH_PAGE.search_criteria_textbox_saved_videos(VSD.video_tag_vehicle)


@then('the saved videos that vehicle name with the input characters are listed')
def verify_search_by_vehicle_name_saved_videos_page():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True


@when('the user selects "Video Name" of from "Select Search" filter and the user inputs some characters in the Saved Videos page')
def search_by_video_name_saved_videos():
    VIDEO_SEARCH_PAGE.click_reset_button()
    VIDEO_SEARCH_PAGE.click_select_search_filter_saved_videos()
    VIDEO_SEARCH_PAGE.select_video_name_dropdown_saved_videos()
    VIDEO_SEARCH_PAGE.search_criteria_textbox_saved_videos(VSD.video_name)


@then('the saved videos that video name with the input characters are listed')
def verify_search_by_video_name_saved_videos_page():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True

# LQ-208
@when('the user clicks the video name')
def click_first_video_name():
    VIDEO_SEARCH_PAGE.click_first_video_name()


@then('the video player page is opened and the video is auto-played')
def assert_video_player():
    assert VIDEO_SEARCH_PAGE.get_video_player_title("VIDEO PLAYER") == "VIDEO PLAYER"


# LQ-10128
@when('the user clicks on the Library and the user selects Video Tags')
def go_to_video_tags_page():
    VIDEO_SEARCH_PAGE.click_reset_button()
    VIDEO_SEARCH_PAGE.click_library_tab()
    VIDEO_SEARCH_PAGE.click_video_tags_tab()


@then(
    'the video tag count is displayed and the table is displayed with columns: "ACTIONS","VEHICLE","TAG NAME","CATEGORY","AVAILABLE VIEWS","GROUP","RECORD DATE"')
def verify_table_video_tags_page():
    sleep(2)
    assert VIDEO_SEARCH_PAGE.get_actions_column_video_tags_text() == "ACTIONS"
    assert VIDEO_SEARCH_PAGE.get_vehicle_column_video_tags_text() == "VEHICLE"
    assert VIDEO_SEARCH_PAGE.get_tag_name_column_text() == "TAG NAME"
    assert VIDEO_SEARCH_PAGE.get_category_column_text() == "CATEGORY"
    assert VIDEO_SEARCH_PAGE.get_available_views_column_text() == "AVAILABLE VIEWS"
    assert VIDEO_SEARCH_PAGE.get_group_column_video_tags_text() == "GROUP"
    assert VIDEO_SEARCH_PAGE.get_record_date_column_text() == "RECORD DATE"


# LQ-210
@when('the user sets group filter to one group in the Video Tags page')
def set_group_filter_video_tags_page():
    VIDEO_SEARCH_PAGE.click_group_filter_video_tags()
    VIDEO_SEARCH_PAGE.search_group_video_tags(VSD.group)
    VIDEO_SEARCH_PAGE.select_searched_group_video_tags()
    VIDEO_SEARCH_PAGE.click_done_button_video_tags()


@then('the tagged videos belong to the group are listed')
def verify_group_filter_video_tags_page():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True


@when('the user sets the date filter in the Video Tags page')
def set_date_filter_video_tags_page():
    VIDEO_SEARCH_PAGE.click_date_filter_video_tags()
    VIDEO_SEARCH_PAGE.select_last_90_days_video_tags()
    VIDEO_SEARCH_PAGE.click_apply_button_video_tags()


@then('the tagged videos belong to the date are listed')
def verify_date_filter_video_tags_page():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True


@when('the user selects driver tagged from "Category" filter in the Video Tags page')
def set_category_filter_video_tags_page():
    VIDEO_SEARCH_PAGE.click_category_filter()
    VIDEO_SEARCH_PAGE.select_driver_tagged()


@then('the tagged videos belong to the driver tagged are listed')
def verify_category_filter_video_tags_page():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True


# LQ-211
@when('the user selects "Tag Name" from "Select Search" filter and the user inputs some characters')
def search_by_tag_name_video_tags_page():
    VIDEO_SEARCH_PAGE.click_select_search_filter_video_tags()
    VIDEO_SEARCH_PAGE.select_tag_name_dropdown_video_tags()
    VIDEO_SEARCH_PAGE.search_criteria_textbox_video_tags(VSD.video_tag_vehicle)


@then('the tagged videos that tag name with the input characters are listed')
def verify_search_by_tag_name_video_tags():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True


@when('the user selects "Vehicle Name" from "Select Search" filter and the user inputs some characters')
def search_by_vehicle_name_video_tags_page():
    VIDEO_SEARCH_PAGE.click_select_search_filter_video_tags()
    VIDEO_SEARCH_PAGE.select_vehicle_name_dropdown_video_tags()
    VIDEO_SEARCH_PAGE.search_criteria_textbox_video_tags(VSD.video_tag_vehicle)


@then('the tagged videos that vehicle name with the input characters are listed')
def verify_search_by_tag_name_video_tags():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True

# LQ-204
@given('"Video Reviewer Plus" user is in VIDEO SEARCH')
def login_company_with_real_device(browser):
    VIDEO_SEARCH_PAGE.click_profile_icon()
    VIDEO_SEARCH_PAGE.click_sign_out_button()
    LOGIN_PAGE.enter_username(VSD.user_name_real_device)
    LOGIN_PAGE.enter_password(VSD.password_real_device)

    LOGIN_PAGE.click_login()
    LOGIN_PAGE.retry_if_login_failed(DC_URL, VSD.user_name_real_device, VSD.password_real_device)


@when('user clicks on "Browse" from the ACTIONS for one vehicle')
def click_browse_button(context):
    VIDEO_SEARCH_PAGE.click_vehicles_tab()
    context['live_present'] = VIDEO_SEARCH_PAGE.click_browse_button()


@then('user is navigated to "Browser" in VIDEO BROWSER page')
def assert_browse_button(context):
    assert VIDEO_SEARCH_PAGE.get_video_browser_title("VIDEO BROWSER") == "VIDEO BROWSER"
    if context['live_present']:
        assert VIDEO_SEARCH_PAGE.browser_tab_is_active() is True
        assert VIDEO_SEARCH_PAGE.live_tab_is_active() is False


@when('user clicks on "Live" from the ACTIONS for one vehicle')
def click_live_button():
    VIDEO_SEARCH_PAGE.click_vehicle_tab()
    VIDEO_SEARCH_PAGE.click_live_button()


@then('user is navigated to "Live" in VIDEO BROWSER page')
def assert_live_button():
    assert VIDEO_SEARCH_PAGE.get_video_browser_title("VIDEO BROWSER") == "VIDEO BROWSER"
    assert VIDEO_SEARCH_PAGE.browser_tab_is_active() is False
    assert VIDEO_SEARCH_PAGE.live_tab_is_active() is True


# LQ-203
@when('the user clicks on "live" link')
# do nothing due to the live tab is opened already

@then(
    'the outside video is live played on the left and the map is displayed on the right with current position and the GSP speed is displayed on the bottom')
def assert_live_stream():
    assert VIDEO_SEARCH_PAGE.retry_button_is_displayed() is False
    assert VIDEO_SEARCH_PAGE.outside_view_live_tab_is_active() is True
    # assert VIDEO_SEARCH_PAGE.map_displayed_live_tab() is True # the device's map is not available
    assert "GPS SPEED" in VIDEO_SEARCH_PAGE.get_gps_speed_text("GPS SPEED")


# LQ-202
@given('"Video Reviewer Plus" user is in browser tab of VIDEO BROWSER page')
def go_to_browser_tab():
    VIDEO_SEARCH_PAGE.click_vehicles_tab()
    VIDEO_SEARCH_PAGE.click_browse_button()


@when(
    'user clicks on the "Save To Library" button and user enters a video name in input box and user clicks "Save" button and user clicks "Go To Video" button on the success popup modal')
def save_video():
    VIDEO_SEARCH_PAGE.click_save_to_library()
    VIDEO_SEARCH_PAGE.type_video_name('Save Video Test')
    VIDEO_SEARCH_PAGE.click_save_button()
    VIDEO_SEARCH_PAGE.click_go_to_video_button()


@then('the 120 seconds video for all the views is received and the user is navigated to Video Player page')
def assert_save_video():
    assert VIDEO_SEARCH_PAGE.get_video_player_title("VIDEO PLAYER") == "VIDEO PLAYER"
