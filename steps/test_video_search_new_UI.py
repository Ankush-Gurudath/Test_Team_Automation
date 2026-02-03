from time import sleep

from hamcrest import contains_string, assert_that
from pytest_bdd import scenarios, given, when, then

from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.video_search_page import VideoSearchPage
from steps.common import DC_URL, ENV, NEW_UI_FTM_URL
from data.int.video_search_data_int import VideoSearchDataInt as VSD_INT
from data.prod.video_search_data_prod import VideoSearchDataProd as VSD_PROD
from data.stg.video_search_data_stg import VideoSearchDataStg as VSD_STG

LOGIN_PAGE = 0
VIDEO_SEARCH_PAGE = 0
DASHBOARD_PAGE = 0
VSD = 0

scenarios('../features/video_search_new_ui.feature')


# LQ-15219
@given('the login page is displayed')
def launch_browser(browser):
    global LOGIN_PAGE, VIDEO_SEARCH_PAGE, DASHBOARD_PAGE, VSD

    LOGIN_PAGE = LoginPage(browser)
    VIDEO_SEARCH_PAGE = VideoSearchPage(browser)
    DASHBOARD_PAGE = DashboardPage(browser)

    browser.get(NEW_UI_FTM_URL)

    if ENV == 'int':
        VSD = VSD_INT
    elif ENV == 'stg':
        VSD = VSD_STG
    elif ENV == 'prod':
        VSD = VSD_PROD


@when('the Video Reviewer Plus user enters a newly created username/password and clicks the login button')
def login():
    LOGIN_PAGE.enter_username(VSD.user_name_real_device)
    LOGIN_PAGE.enter_password(VSD.password)
    LOGIN_PAGE.click_login()


@then('the user is successfully logged into the Video Search page')
def verify_login():
    assert VIDEO_SEARCH_PAGE.get_video_search_title() == "Video Search"


# LQ-205
@when('the Video Reviewer Plus user is in Video Search page')
def go_to_video_search_page():
    VIDEO_SEARCH_PAGE.click_vehicle_tab_new()


@then(
    'the vehicle count is displayed and the table is displayed with columns: "ACTIONS", "VEHICLES", "DEVICE", "LAST COMMUNICATED", "GROUP", "VIEWS"')
def verify_table_vehicle_page():
    assert VIDEO_SEARCH_PAGE.video_tag_count_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True
    assert VIDEO_SEARCH_PAGE.get_actions_column_text() == "ACTIONS"
    assert VIDEO_SEARCH_PAGE.get_vehicles_column_text() == "VEHICLES"
    assert VIDEO_SEARCH_PAGE.get_device_column_text() == "DEVICE"
    assert VIDEO_SEARCH_PAGE.get_last_communicated_column_text() == "LAST COMMUNICATED"
    assert VIDEO_SEARCH_PAGE.get_group_column_text() == "GROUP"
    assert VIDEO_SEARCH_PAGE.get_views_column_text() == "VIEWS"


# LQ-136862
@when('the user sets group filter to one group in vehicles page')
def set_group_filter_vehicle_page():
    VIDEO_SEARCH_PAGE.click_group_filter()
    VIDEO_SEARCH_PAGE.search_group(VSD.saved_group)
    VIDEO_SEARCH_PAGE.select_searched_group()
    VIDEO_SEARCH_PAGE.click_done_button()


@then('the vehicles belong to the group are listed')
def verify_group_filter_vehicle_page():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True
    VIDEO_SEARCH_PAGE.click_reset_button()


@when('the user selects "Vehicle Name" from "Select Search" dropdown and the user input some characters in search bar')
def search_by_vehicle_name_vehicle_page():
    VIDEO_SEARCH_PAGE.click_select_search_filter()
    VIDEO_SEARCH_PAGE.select_vehicle_name_dropdown()
    VIDEO_SEARCH_PAGE.search_criteria_textbox(VSD.vehicle)


@then('the vehicles with the inputted characters are listed')
def verify_searched_by_vehicle_name_vehicle_page():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True
    VIDEO_SEARCH_PAGE.click_reset_button()


@when('the user selects "Serial Number" from "Select Search" dropdown and the user input some characters in search bar')
def search_by_serial_name_vehicle_page():
    VIDEO_SEARCH_PAGE.click_select_search_filter()
    VIDEO_SEARCH_PAGE.select_serial_name_dropdown()
    VIDEO_SEARCH_PAGE.search_criteria_textbox(VSD.device)


@then('the vehicles which attached ER serial number with the inputted characters are listed')
def verify_searched_by_serial_name_vehicle_page():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True
    VIDEO_SEARCH_PAGE.click_reset_button()


# @LQ-136867
@when('the user clicks on the "Download CSV" button on the bottom right corner in vehicles page')
def click_download_button_vehicles_page():
    VIDEO_SEARCH_PAGE.click_download_csv_button_in_vehicles_page()


@then('CSV file should be downloaded containing all the available data')
def verify_csv_report_downloaded():
    file_name = VIDEO_SEARCH_PAGE.get_vehicles_list_file_name()
    assert VIDEO_SEARCH_PAGE.check_file_exist(file_name) is True


# @LQ-136875
@when('the user hovers the mouse over the tooltip before the vehicle name')
def click_on_tooltip_of_vehicle():
    VIDEO_SEARCH_PAGE.click_tooltip_icon()


@then('the tooltip should display the device information including Serial Number, Active/Inactive status and Last '
      'Communication Date and Time')
def verify_tooltip_content():
    assert VIDEO_SEARCH_PAGE.device_information_title_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.device_serial_number_with_device_status_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.last_communication_is_displayed() is True


# @LQ-136865
@when('the user clicks the arrow button in the page number section')
def click_arrow_button_in_page_section():
    VIDEO_SEARCH_PAGE.click_right_arrow_button()


@then('the user should be navigated to the next page of results')
def verify_next_page_is_displayed():
    assert_that(VIDEO_SEARCH_PAGE.get_page_result(), contains_string("2"))


@when('the user selects a value from the pagination dropdown 10 vehicles, 50 vehicles, 100 vehicles')
def select_pagination_from_dropdown():
    VIDEO_SEARCH_PAGE.click_pagination_dropdown()
    VIDEO_SEARCH_PAGE.select_pagination_from_dropdown()


@then('the page should display the selected number of vehicles accordingly')
def verify_selected_pagination_is_displayed():
    assert VIDEO_SEARCH_PAGE.get_count_of_rows_in_vehicles_pages() <= 50


# LQ-136890
@when('the user clicks on the Library and the user selects Saved Videos')
def go_to_saved_videos_page():
    VIDEO_SEARCH_PAGE.click_library_tab_new()
    VIDEO_SEARCH_PAGE.click_saved_videos_tab_new()


@then(
    'the video count is displayed and the table is displayed with columns: "VIDEO NAME","STATUS","TAG TYPE","VEHICLE","GROUP","LENGTH","VIEWS","VIDEO DATE","REQUEST DATE"')
def verify_table_saved_videos_page():
    assert VIDEO_SEARCH_PAGE.saved_video_count_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True
    assert VIDEO_SEARCH_PAGE.get_video_name_column_text() == "VIDEO NAME"
    assert VIDEO_SEARCH_PAGE.get_status_column_text() == "STATUS"
    assert VIDEO_SEARCH_PAGE.get_tag_type_column_text() == "TAG TYPE"
    assert VIDEO_SEARCH_PAGE.get_vehicle_column_saved_videos_text() == "VEHICLE"
    assert VIDEO_SEARCH_PAGE.get_group_column_saved_videos_text() == "GROUP"
    assert VIDEO_SEARCH_PAGE.get_length_column_text() == "LENGTH"
    assert VIDEO_SEARCH_PAGE.get_views_column_saved_videos_text() == "VIEWS"
    assert VIDEO_SEARCH_PAGE.get_video_date_column_text() == "VIDEO DATE"
    assert VIDEO_SEARCH_PAGE.get_request_date_column_text() == "REQUEST DATE"


# LQ-136890
@when('the user sets group filter to one group in the Saved Videos page')
def set_group_filter_saved_videos():
    VIDEO_SEARCH_PAGE.click_group_filter_saved_videos()
    VIDEO_SEARCH_PAGE.search_group_saved_videos(VSD.saved_group)
    VIDEO_SEARCH_PAGE.select_searched_group_saved_videos()
    VIDEO_SEARCH_PAGE.done_button_saved_videos()


@then('the saved videos belong to the selected group are listed in the Saved Videos page')
def verify_group_filter_saved_videos_page():
    assert VIDEO_SEARCH_PAGE.saved_video_count_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True
    VIDEO_SEARCH_PAGE.click_reset_button_saved_videos()


@when('the user sets the date filter in the Saved Videos page')
def set_date_filter_saved_videos():
    VIDEO_SEARCH_PAGE.click_date_filter_saved_videos()
    VIDEO_SEARCH_PAGE.click_last_7_days()
    VIDEO_SEARCH_PAGE.click_apply_saved_videos()


@then('the saved videos belong to the date are listed in the Saved Videos page')
def verify_date_filter_saved_videos_page():
    assert VIDEO_SEARCH_PAGE.saved_video_count_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True


@when(
    'user selects "Vehicle Name" from "Select Search" filter and user inputs some characters in the Saved Videos page')
def search_by_vehicle_name_saved_videos():
    VIDEO_SEARCH_PAGE.click_reset_button()
    VIDEO_SEARCH_PAGE.click_select_search_filter_saved_videos()
    VIDEO_SEARCH_PAGE.select_vehicle_name_dropdown_saved_videos()
    VIDEO_SEARCH_PAGE.search_criteria_textbox_saved_videos(VSD.vehicle)


@then('the saved videos that vehicle name with the input characters are listed')
def verify_search_by_vehicle_name_saved_videos_page():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True


@when(
    'the user selects "Video Name" of from "Select Search" filter and the user inputs some characters in the Saved Videos page')
def search_by_video_name_saved_videos():
    VIDEO_SEARCH_PAGE.click_reset_button()
    VIDEO_SEARCH_PAGE.click_select_search_filter_saved_videos()
    VIDEO_SEARCH_PAGE.select_video_name_dropdown_saved_videos()
    VIDEO_SEARCH_PAGE.search_criteria_textbox_saved_videos(VSD.video_name)


@then('the saved videos that video name with the input characters are listed')
def verify_search_by_video_name_saved_videos_page():
    assert VIDEO_SEARCH_PAGE.get_row_count_for_video_tag() is True


# @LQ-136890
@when('the user clicks on the left or right navigation arrows at the bottom of the page')
def click_arrow_button_in_page_section_in_saved_video_page():
    VIDEO_SEARCH_PAGE.click_reset_button()
    VIDEO_SEARCH_PAGE.click_date_filter_video_tags()
    VIDEO_SEARCH_PAGE.select_last_90_days_video_tags()
    VIDEO_SEARCH_PAGE.click_apply_button_video_tags()
    VIDEO_SEARCH_PAGE.click_right_arrow_button()


@then('the page should navigate as per the direction of the arrow clicked')
def verify_next_page_is_displayed_in_saved_video_page():
    assert_that(VIDEO_SEARCH_PAGE.get_page_result(), contains_string("2"))


@when('the user selects pagination options 10, 50, 100 videos from the bottom left corner')
def select_pagination_from_dropdown_in_saved_video_page():
    # VIDEO_SEARCH_PAGE.click_left_arrow_button()
    VIDEO_SEARCH_PAGE.click_pagination_dropdown()
    VIDEO_SEARCH_PAGE.select_pagination_from_dropdown()


@then('the page should display the videos according to the selected pagination option')
def verify_selected_pagination_is_displayed_in_saved_video_page():
    assert VIDEO_SEARCH_PAGE.get_count_of_rows_in_vehicles_pages() <= 50


# LQ-136890
@when('the user clicks the video name')
def click_first_video_name():
    VIDEO_SEARCH_PAGE.click_saved_video_name()


@then('the video player page is opened and the video is auto-played')
def assert_video_player():
    assert VIDEO_SEARCH_PAGE.get_video_player_title("VIDEO PLAYER") == "VIDEO PLAYER"
    assert VIDEO_SEARCH_PAGE.video_play_time() != VIDEO_SEARCH_PAGE.video_play_time_changed(
        VIDEO_SEARCH_PAGE.video_play_time())


# @LQ-150991
# @when('the user navigates to Saved Video page and opens a saved video')
# covered in LQ-208 test


@then('the map should be displayed on the video player page')
def verify_map_is_displayed_in_video_player_page():
    VIDEO_SEARCH_PAGE.scroll_page_down()
    assert VIDEO_SEARCH_PAGE.map_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.map_zoom_in_button_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.map_zoom_out_button_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.map_camera_control_button_is_displayed() is True


# @LQ-151021
@when('the user navigates to Saved Video page and clicks on displayed views in the timeline')
def click_displayed_views_in_timeline():
    VIDEO_SEARCH_PAGE.click_view_icon()
    VIDEO_SEARCH_PAGE.select_1st_view()


@then('the user should be able to select and switch between the available views')
def verify_switch_between_views():
    assert VIDEO_SEARCH_PAGE.view_1_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.view_2_is_displayed() is False


# @LQ-136890
# @when('the user clicks the video name')
# covered in LQ-208 test


@then('the video player page should display video name (with edit option), vehicle name, length, views, video date, '
      'and request date')
def verify_elements_in_video_player_page():
    assert VIDEO_SEARCH_PAGE.edit_name_option_is_displayed() is True
    assert VIDEO_SEARCH_PAGE.get_video_name_text() == "NAME"
    assert VIDEO_SEARCH_PAGE.get_vehicle_name_text() == "VEHICLE"
    assert VIDEO_SEARCH_PAGE.get_video_length_text() == "LENGTH"
    assert VIDEO_SEARCH_PAGE.get_view_text() == "VIEWS"
    assert VIDEO_SEARCH_PAGE.get_video_date_text() == "VIDEO DATE"
    assert VIDEO_SEARCH_PAGE.get_request_date_text() == "REQUEST DATE"


# LQ-278664
@when('the user opens the saved video and opens the Download modal')
def open_download_modal_saved_video_page():
    VIDEO_SEARCH_PAGE.click_download_icon()


@then('the "Enable Video Stitching" section is visible')
def verify_enable_video_stitching_section():
    assert VIDEO_SEARCH_PAGE.enable_video_stitching_section_is_displayed() is True


@when('the user opens the Download modal for that video and selects media type "MP4" And selects view "Inside only"')
def download_mp4_inside_only():
    VIDEO_SEARCH_PAGE.click_views_dropdown()
    VIDEO_SEARCH_PAGE.select_inside_view()
    VIDEO_SEARCH_PAGE.click_views_dropdown()


@then('the "Enable Video Stitching" section is not visible')
def verify_enable_video_stitching_section_not_visible():
    assert VIDEO_SEARCH_PAGE.enable_video_stitching_section_is_displayed() is False


@when('the user selects view "Outside only"')
def download_mp4_outside_only():
    VIDEO_SEARCH_PAGE.click_cancel_button()
    VIDEO_SEARCH_PAGE.click_download_icon()
    VIDEO_SEARCH_PAGE.click_views_dropdown()
    VIDEO_SEARCH_PAGE.select_outside_view()
    VIDEO_SEARCH_PAGE.click_views_dropdown()


@then('the "Enable Video Stitching" section should not be visible')
def verify_enable_video_stitching_section_not_visible_outside_only():
    assert VIDEO_SEARCH_PAGE.enable_video_stitching_section_is_displayed() is False


@when('the user selects view "Inside + Outside"')
def download_mp4_inside_outside():
    VIDEO_SEARCH_PAGE.click_views_dropdown()
    VIDEO_SEARCH_PAGE.deselect_inside_view()
    VIDEO_SEARCH_PAGE.click_views_dropdown()


@then('"Enable Video Stitching" section is visible')
def verify_enable_video_stitching_section_visible_inside_outside():
    assert VIDEO_SEARCH_PAGE.enable_video_stitching_section_is_displayed() is True


#LQ-278669
@when('the user selects media type "DCE" and selects view "Inside + Outside"')
def select_download_DCE():
    VIDEO_SEARCH_PAGE.select_media_type_dce()


@then('the "Enable Video Stitching" section is not visible for Download DCE option')
def verify_enable_video_stitching_section_not_visible_dce():
    assert VIDEO_SEARCH_PAGE.enable_video_stitching_section_is_displayed() is False


#LQ-278671
@when('the user enables the stitching toggle and clicks Download button')
def enable_stitching_and_download():
    VIDEO_SEARCH_PAGE.click_download_mp4_button()
    VIDEO_SEARCH_PAGE.enable_stitching_toggle()
    VIDEO_SEARCH_PAGE.click_download_button()


@then('the stitched video is downloaded successfully')
def verify_stitched_video_downloaded(context):
    expected_file_name = VIDEO_SEARCH_PAGE.get_downloaded_mp4_file_name_for_video_stitching()
    file_downloaded = VIDEO_SEARCH_PAGE.wait_for_download_file(expected_file_name, timeout=30)
    assert file_downloaded, f"Stitched video '{expected_file_name}' was not downloaded."


# LQ-278687
@when('the user selects a saved video longer than 3 minutes and clicks Download button')
def download_video_longer_than_3_minutes():
    VIDEO_SEARCH_PAGE.click_saved_videos_tab_new()
    VIDEO_SEARCH_PAGE.click_reset_button_saved_videos()
    VIDEO_SEARCH_PAGE.click_select_search_filter_saved_videos()
    VIDEO_SEARCH_PAGE.select_video_name_dropdown_saved_videos()
    VIDEO_SEARCH_PAGE.search_criteria_textbox_saved_videos(VSD.video_name_HD)
    VIDEO_SEARCH_PAGE.click_first_video_name()
    VIDEO_SEARCH_PAGE.click_download_icon()


@then('the user should see an error message indicating "Unavailable for HD videos longer than 3 minutes"')
def verify_error_message_for_hd_video_longer_than_3_minutes():
    assert VIDEO_SEARCH_PAGE.get_error_message_text_download_hd_video_longer_than_3_minutes() == "Unavailable for HD videos longer than 3 minutes"


# @LQ-151020
@when('the user navigates to Saved Video page and clicks the delete button on the timeline')
def delete_saved_video():
    VIDEO_SEARCH_PAGE.click_saved_videos_tab_new()
    VIDEO_SEARCH_PAGE.select_the_vehicle_from_the_list()
    VIDEO_SEARCH_PAGE.click_delete_button()
    VIDEO_SEARCH_PAGE.click_confirm_button()


@then('the video should be deleted')
def verify_saved_deleted():
    assert VIDEO_SEARCH_PAGE.video_deleted_popup_is_displayed() is True


# LQ-136887
@when('the user clicks on the Library and the user selects Video Tags')
def go_to_video_tags_page():
    VIDEO_SEARCH_PAGE.click_library_tab_new()
    VIDEO_SEARCH_PAGE.click_video_tags_tab_new()


@then(
    'the video tag count is displayed and the table is displayed with columns: "ACTIONS","VEHICLE","TAG NAME","CATEGORY","AVAILABLE VIEWS","GROUP","RECORD DATE"')
def verify_table_video_tags_page():
    assert VIDEO_SEARCH_PAGE.get_actions_column_video_tags_text() == "ACTIONS"
    assert VIDEO_SEARCH_PAGE.get_vehicle_column_video_tags_text() == "VEHICLE"
    assert VIDEO_SEARCH_PAGE.get_tag_name_column_text() == "TAG NAME"
    assert VIDEO_SEARCH_PAGE.get_category_column_text() == "CATEGORY"
    assert VIDEO_SEARCH_PAGE.get_available_views_column_text() == "AVAILABLE VIEWS"
    assert VIDEO_SEARCH_PAGE.get_group_column_video_tags_text() == "GROUP"
    assert VIDEO_SEARCH_PAGE.get_record_date_column_text() == "RECORD DATE"


# LQ-136887
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


# LQ-136887
@when('the user selects "Tag Name" from "Select Search" filter and the user inputs some characters')
def search_by_tag_name_video_tags_page():
    VIDEO_SEARCH_PAGE.click_select_search_filter_video_tags()
    VIDEO_SEARCH_PAGE.select_tag_name_dropdown_video_tags()
    VIDEO_SEARCH_PAGE.search_criteria_textbox_video_tags(VSD.tag_name)


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


# @LQ-150975
@when('clicks on the Browse button')
def navigate_to_browse_page():
    VIDEO_SEARCH_PAGE.click_browse_button()
    if VIDEO_SEARCH_PAGE.video_expired_popup_is_displayed():
        VIDEO_SEARCH_PAGE.click_video_expired_popup_ok_button()


@then('user should be navigated to the Browse page')
def verify_navigate_to_browse_page():
    assert VIDEO_SEARCH_PAGE.get_video_browser_title("VIDEO BROWSER") == "VIDEO BROWSER"
    assert VIDEO_SEARCH_PAGE.browser_tab_is_active() is True
    assert VIDEO_SEARCH_PAGE.live_tab_is_active() is False


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
    VIDEO_SEARCH_PAGE.click_vehicle_tab_new()
    context['live_present'] = VIDEO_SEARCH_PAGE.click_browse_button()


@then('user is navigated to "Browser" in VIDEO BROWSER page')
def assert_browse_button(context):
    assert VIDEO_SEARCH_PAGE.get_video_browser_title("VIDEO BROWSER") == "VIDEO BROWSER"
    if context['live_present']:
        assert VIDEO_SEARCH_PAGE.browser_tab_is_active() is True
        assert VIDEO_SEARCH_PAGE.live_tab_is_active() is False
    # These properties are not always available if the video is not there
    # assert VIDEO_SEARCH_PAGE.map_is_displayed() is True
    # assert VIDEO_SEARCH_PAGE.map_zoom_in_button_is_displayed() is True
    # assert VIDEO_SEARCH_PAGE.map_zoom_out_button_is_displayed() is True
    # assert VIDEO_SEARCH_PAGE.map_camera_control_button_is_displayed() is True



# @LQ-136880
# @when('the user clicks on the Browse button for a vehicle') when is covered in LQ-204


@then('the Browse page should open with the following elements should be visible "date filter","save video button", '
      '"vehicle name", "play/pause button", "playback speed option", "time dropdown", "Trip In-Progress markers on '
      'timeline", "Alerts on timeline", "Events on timeline"')
def verify_the_elements_present_in_video_browser_page():
    assert VIDEO_SEARCH_PAGE.date_filter_is_present() is True
    assert VIDEO_SEARCH_PAGE.vehicle_name_is_present() is True
    assert VIDEO_SEARCH_PAGE.save_video_button_is_present() is True
    assert VIDEO_SEARCH_PAGE.play_pause_button_is_present() is True
    assert VIDEO_SEARCH_PAGE.playback_speed_option_is_present() is True
    assert VIDEO_SEARCH_PAGE.time_dropdown_is_present() is True
    assert VIDEO_SEARCH_PAGE.trip_inprogress_markers_on_timeline_is_present() is True
    assert VIDEO_SEARCH_PAGE.alerts_on_timeline_is_present() is True
    assert VIDEO_SEARCH_PAGE.events_on_timeline_is_present() is True


# @LQ-1368884
@when('user clicks on "Live" from the ACTIONS for one vehicle')
def click_live_button():
    VIDEO_SEARCH_PAGE.click_vehicle_tab_new()
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


# LQ-151039
@given('"Video Reviewer Plus" user is in browser tab of VIDEO BROWSER page')
def go_to_browser_tab():
    VIDEO_SEARCH_PAGE.click_vehicle_tab_new()
    VIDEO_SEARCH_PAGE.click_browse_button()


@when(
    'user clicks on the "Save To Library" button and user enters a video name in input box and user clicks "Save" '
    'button and user clicks "Go To Video" button on the success popup modal')
def save_video():
    VIDEO_SEARCH_PAGE.click_save_to_library()
    VIDEO_SEARCH_PAGE.type_video_name('Save Video Test')
    VIDEO_SEARCH_PAGE.click_save_button()
    VIDEO_SEARCH_PAGE.click_go_to_video_button()


@then('the 120 seconds video for all the views is received and the user is navigated to Video Player page')
def assert_save_video():
    assert VIDEO_SEARCH_PAGE.get_video_player_title("VIDEO PLAYER") == "VIDEO PLAYER"


# @LQ-151018
@when('clicks on the download button and selects Download DCE')
def download_dce():
    VIDEO_SEARCH_PAGE.click_download_icon()
    VIDEO_SEARCH_PAGE.click_download_dce_button()
    VIDEO_SEARCH_PAGE.click_download_button()


@then('the DCE file should be downloaded')
def verify_dce_file_downloaded():
    file_name = VIDEO_SEARCH_PAGE.get_downloaded_dce_file_name()
    assert VIDEO_SEARCH_PAGE.check_file_exist(file_name) is True


# @LA-150994
@when('clicks on the download button and selects Download MP4')
def download_mp4():
    VIDEO_SEARCH_PAGE.click_download_icon()
    VIDEO_SEARCH_PAGE.click_download_button()


@then('the MP4 file should be downloaded')
def verify_mp4_file_downloaded():
    file_name = VIDEO_SEARCH_PAGE.get_downloaded_mp4_file_name()
    assert VIDEO_SEARCH_PAGE.check_file_exist(file_name)


# @LQ-136883
@when('the user navigates to the video search page and clicks on the Browse button for a vehicle and clicks on Save Video without entering a name')
def save_video_without_name():
    if VIDEO_SEARCH_PAGE.cross_button_is_present():
        VIDEO_SEARCH_PAGE.click_cross_button()
    VIDEO_SEARCH_PAGE.click_vehicle_tab_new()
    VIDEO_SEARCH_PAGE.click_browse_button()
    VIDEO_SEARCH_PAGE.click_save_to_library()
    VIDEO_SEARCH_PAGE.click_save_button()


@then('error message should be displayed indicating "Required field"')
def verify_error_message_for_empty_name():
    assert VIDEO_SEARCH_PAGE.get_error_message_text() == "You must enter a value"


# @LQ-151022
@when('the user selects 1 view in the dropdown and enters a name in the input box in the Save Video modal and clicks on the Save button')
def save_video_with_1_view():
    VIDEO_SEARCH_PAGE.select_1_view_from_available_views_dropdown()
    VIDEO_SEARCH_PAGE.type_video_name('Save Video Test 1 View')
    VIDEO_SEARCH_PAGE.click_save_button()
    VIDEO_SEARCH_PAGE.click_go_to_video_button()


@then('the user should be navigated to the Saved Videos page')
def assert_save_video_with_1_view():
    assert VIDEO_SEARCH_PAGE.get_video_player_title("VIDEO PLAYER") == "VIDEO PLAYER"



@when('the user navigates to Saved Video page and clicks the delete button')


# @LQ-136886
@when('the user navigates to the Map Search page and selects a date, time, address in the respective Filter')
def go_to_map_search_page_and_set_filters():
    VIDEO_SEARCH_PAGE.click_map_search_tab()
    VIDEO_SEARCH_PAGE.click_date_filter()
    VIDEO_SEARCH_PAGE.select_date()
    VIDEO_SEARCH_PAGE.click_time_filter()
    VIDEO_SEARCH_PAGE.select_time_in_filter()
    VIDEO_SEARCH_PAGE.click_search_address_box_map_search()
    VIDEO_SEARCH_PAGE.enter_address_in_search_box_map_search("Lytx, Inc., Towne Centre Drive")
    VIDEO_SEARCH_PAGE.select_searched_address_map_search()


@then('the map should display all the vehicles available at the selected address for the selected date and time')
def verify_vehicles_listed_on_map():
    assert VIDEO_SEARCH_PAGE.get_selected_time_range() == "Vehicles (12:30 AM - 1:00 AM)"


@when('the user clicks on the Browse button of a vehicle displayed')
def click_browse_button_in_map_search():
    VIDEO_SEARCH_PAGE.click_vehicle_dropdown()
    VIDEO_SEARCH_PAGE.click_map_browse_button()


@then('the user should be navigated to the Browse page')
def verify_navigate_to_browse_page_from_map_search():
    assert VIDEO_SEARCH_PAGE.get_video_browser_title("VIDEO BROWSER") == "VIDEO BROWSER"
    assert VIDEO_SEARCH_PAGE.browser_tab_is_active() is True
    assert VIDEO_SEARCH_PAGE.live_tab_is_active() is False
