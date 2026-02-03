class LocatorsVideoSearchPage:
    video_search_page_title_id = 'videoSearchText'
    vehicle_tab_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[1]/div'
    library_tab_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[3]/div'
    saved_videos_tab_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[3]/' \
                             'div[2]/div[2]/div[1]/div'
    video_tags_tab_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[3]' \
                           '/div[2]/div[2]/div[2]'

    # table columns in vehicle page
    actions_column_text_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div/' \
                                'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                'cdk-header-cell[1]/span/span'
    vehicles_column_text_xpath = '/html/body/app-root/shell/div/div/div/ng-component/' \
                                 'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row' \
                                 '/cdk-header-cell[2]/span/span'
    device_column_text_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div' \
                               '/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                               'cdk-header-cell[3]/span/span'
    last_communicated_column_text_xpath = '/html/body/app-root/shell/div/div/div/ng-component' \
                                          '/div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                          'cdk-header-cell[4]/span/span'
    group_column_text_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div/lx-table/' \
                              'div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[5]/span/span'
    views_column_text_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div/lx-table' \
                              '/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[6]/span/span'
    vehicle_count_text_xpath = '//div[@data-test-id="filter-headerBar-countValueSuccess"]'
    video_count_text_xpath = '(//*[contains(text(), "Video")]/parent::div/preceding-sibling::div/div)[1]'

    # Filters and select search criteria in vehicle page
    group_filter_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div/div/' \
                         'vehicles-list-filter/filter-bar/div/div[2]/div[2]/group-filter/div'
    search_group_textbox_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal' \
                                 '/group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_searched_group_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal/' \
                                  'group-selector/div/div[1]/div[2]/div/lytx-typeahead/div' \
                                  '/ngb-typeahead-window/button[1]'
    done_button_group_filter_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal' \
                                     '/group-selector/div/div[3]/button[2]'
    reset_button_xpath = '//div[@class="reset-button-text"]'
    select_search_filter_xpath = '/html/body/app-root/shell/div/div/div/ng-component/' \
                                 'div/div/vehicles-list-filter/filter-bar/div/div[2]/div[2]/' \
                                 'dropdown/div/span/span'
    select_vehicle_name_dropdown_xpath = '/html/body/app-root/shell/div/div/div/ng-component' \
                                         '/div/div/vehicles-list-filter/filter-bar/div/div[2]/div[2]' \
                                         '/dropdown/div/div/ul/li[1]'
    select_serial_number_dropdown_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div/' \
                                          'div/vehicles-list-filter/filter-bar/div/div[2]/div[2]' \
                                          '/dropdown/div/div/ul/li[2]'
    search_criteria_textbox_xpath = '/html/body/app-root/shell/div/div/div/ng-component/div/div' \
                                    '/vehicles-list-filter/filter-bar/div/div[2]/div[2]/div/' \
                                    'lytx-search/div/form/input'

    # table columns in saved videos page
    video_name_column_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/' \
                                   'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                   'cdk-header-cell[2]/span/span'
    status_column_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div' \
                               '/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                               'cdk-header-cell[3]/span/span'
    tag_type_column_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div' \
                                 '/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                 'cdk-header-cell[4]/span/span'
    vehicle_column_saved_videos_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/' \
                                             'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                             'cdk-header-cell[5]/span/span'
    group_column_saved_videos_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/' \
                                           'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                           'cdk-header-cell[6]/span/span'
    length_column_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library' \
                               '/div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                               'cdk-header-cell[7]/span/span'
    views_column_saved_videos_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/' \
                                           'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                           'cdk-header-cell[8]/span/span'
    video_date_column_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library' \
                                   '/div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                   'cdk-header-cell[9]/span/span'
    request_date_column_text_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/' \
                                     'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                     'cdk-header-cell[10]/span/span'
    first_video_name_xpath = '(//video-preview-link[@data-test-id="library-savedVideo-videoName"]/span)[1]'
    saved_video_name_xpath = '//cdk-row[.//cdk-cell[3]//span[normalize-space()="Completed"]]//cdk-cell[2]//video-preview-link'
    tenth_video_name_xpath = '//*[@data-test-id="cdkRow-cellSpan-9-0"]'
    first_video_status_xpath = '//*[@data-test-id="cdkRow-cellSpan-0-1"]'
    tenth_video_status_xpath = '//*[@data-test-id="cdkRow-cellSpan-9-1"]'

    first_completed_status_xpath = '(//*[@class="media-status ng-star-inserted"])[1]'
    # Filters and select search criteria in saved videos page
    group_filter_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div' \
                                      '/event-library-filter/filter-bar/div/div[2]/div[2]/' \
                                      'group-filter/div'
    search_group_textbox_saved_videos_xpath = '/html/body/ngb-modal-window/div/div/' \
                                              'group-selector-modal/group-selector/div' \
                                              '/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_searched_group_saved_videos_xpath = '/html/body/ngb-modal-window/div/div/' \
                                               'group-selector-modal/group-selector/div/div[1]/div[2]/div/' \
                                               'lytx-typeahead/div/ngb-typeahead-window/button'
    done_button_group_filter_saved_videos_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal/' \
                                                  'group-selector/div/div[3]/button[2]'
    date_filter_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/' \
                                     'event-library-filter/filter-bar/div/div[2]/div[2]/' \
                                     'lx-date-range-filter/div/div[1]'
    date_range_start_month_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/event-library-filter/' \
                                   'filter-bar/div/div[2]/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                                   '/div/div[1]/div[1]/div[2]/lx-date-input/div/input[1]'
    date_range_start_day_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/event-library-filter' \
                                 '/filter-bar/div/div[2]/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                                 '/div/div[1]/div[1]/div[2]/lx-date-input/div/input[2]'
    date_range_start_year_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/event-library-filte' \
                                  'r/filter-bar/div/div[2]/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                                  '/div/div[1]/div[1]/div[2]/lx-date-input/div/input[3]'
    date_range_end_month_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/event-library-filter' \
                                 '/filter-bar/div/div[2]/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                                 '/div/div[1]/div[2]/div[2]/lx-date-input/div/input[1]'
    date_range_end_day_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/event-library-filter' \
                               '/filter-bar/div/div[2]/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                               '/div/div[1]/div[2]/div[2]/lx-date-input/div/input[2]'
    date_range_end_year_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/event-library-filter/' \
                                'filter-bar/div/div[2]/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                                '/div/div[1]/div[2]/div[2]/lx-date-input/div/input[3]'
    apply_button_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/' \
                                      'event-library-filter/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                      '/div/div[2]/lx-date-range-selector/div/div[2]/div[2]/div/div[2]/button[2]'
    select_search_filter_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/event-library-filter' \
                                              '/filter-bar/div/div[2]/div[2]/dropdown/div/span/span'
    video_name_dropdown_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/' \
                                             'div/event-library-filter/filter-bar/div/div[2]/div[2]/' \
                                             'dropdown/div/div/ul/li[1]'
    vehicle_name_dropdown_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/' \
                                               'event-library-filter/filter-bar/div/div[2]/div[2]/dropdown/div/div/ul/li[2]'
    search_criteria_textbox_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library' \
                                                 '/div/event-library-filter/filter-bar/div/div[2]/div[2]/div/' \
                                                 'lytx-search/div/form/input'
    reset_button_saved_videos_xpath = '/html/body/app-root/shell/div/div/div/saved-video-library/div/' \
                                      'event-library-filter/filter-bar/div/div[2]/div[2]/button'

    # table columns in video tags page
    actions_column_text_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/' \
                                           'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                           'cdk-header-cell[1]/span/span'
    vehicle_column_video_tags_text_xpath = '/html/body/app-root/shell/div/div/div/tag-library/' \
                                           'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                           'cdk-header-cell[2]/span/span'
    tag_name_column_text_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/lx-table/div[2]' \
                                 '/div[2]/cdk-table/cdk-header-row/cdk-header-cell[3]/span/span'
    category_column_text_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/lx-table' \
                                 '/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[4]/span/span'
    available_views_column_text_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div' \
                                        '/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                        'cdk-header-cell[5]/span/span'
    group_column_video_tag_text_xpath = '/html/body/app-root/shell/div/div/div/tag-library/' \
                                        'div/lx-table/div[2]/div[2]/cdk-table/cdk-header-row' \
                                        '/cdk-header-cell[6]/span/span'
    record_date_column_text_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/' \
                                    'lx-table/div[2]/div[2]/cdk-table/cdk-header-row' \
                                    '/cdk-header-cell[7]/span/span'
    video_tags_count_text_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div' \
                                  '/event-library-filter/filter-bar/div/div[2]/div[1]/div[1]' \
                                  '/div/div[1]/div'

    # Filters and select search criteria on Video tags page
    group_filter_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/' \
                                    'event-library-filter/filter-bar/div/div[2]/div[2]/' \
                                    'group-filter/div/span'
    search_group_textbox_video_tags_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal/' \
                                            'group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_searched_group_video_tags_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal' \
                                             '/group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/' \
                                             'ngb-typeahead-window/button'
    done_button_group_filter_video_tags_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal/' \
                                                'group-selector/div/div[3]/button[2]'
    reset_button_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/event-library-filter' \
                                    '/filter-bar/div/div[2]/div[2]/button'
    date_filter_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/event-library-filter' \
                                   '/filter-bar/div/div[2]/div[2]/lx-date-range-filter/div/div[1]'
    last_30_days_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/event-library-filter/filter-bar/' \
                                    'div/div[2]/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector/' \
                                    'div/div[2]/div[1]/div[3]'
    last_90_days_video_tags_xpath = '//*[text()=" Last 90 Days "]'
    apply_date_button_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/' \
                                         'event-library-filter/filter-bar/div/div[2]/div[2]/' \
                                         'lx-date-range-filter/div/div[2]/lx-date-range-selector/' \
                                         'div/div[2]/div[2]/div/div[2]/button[2]'
    category_filter_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/event-library-filter' \
                            '/filter-bar/div/div[2]/div[2]/dropdown[1]/div/span/span'
    driver_tagged_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/event-library-filter' \
                          '/filter-bar/div/div[2]/div[2]/dropdown[1]/div/div/ul/li[1]'
    select_search_filter_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library' \
                                            '/div/event-library-filter/filter-bar/div/div[2]/div[2]' \
                                            '/dropdown[2]/div/span/span'
    select_tag_name_dropdown_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div' \
                                                '/event-library-filter/filter-bar/div/div[2]/div[2]/' \
                                                'dropdown[2]/div/div/ul/li[1]'
    select_vehicle_name_dropdown_video_tags_xpath = '/html/body/app-root/shell/div/div/div' \
                                                    '/tag-library/div/event-library-filter/filter-bar/' \
                                                    'div/div[2]/div[2]/dropdown[2]/div/div/ul/li[2]'
    search_criteria_textbox_video_tags_xpath = '/html/body/app-root/shell/div/div/div/tag-library/div/' \
                                               'event-library-filter/filter-bar/div/div[2]/div[2]/div/' \
                                               'lytx-search/div/form/input'

    # Video Player page:
    video_player_title_xpath = '/html/body/app-root/shell/div/div/div/saved-video-player/div/div[1]'
    video_date_xpath = '(//*[@class="video-date"])[1]'
    play_button_xpath = '/html/body/app-root/shell/div/div/div/saved-video-player/div/' \
                        'simultaneous-video-player/div/synchronized-video-player/div[2]/' \
                        'video-player-control-bar/div[1]/div[2]/div/i'
    video_play_time_xpath = '/html/body/app-root/shell/div/div/div/saved-video-player/div/' \
                            'simultaneous-video-player/div/synchronized-video-player/div[2]/' \
                            'video-player-control-bar/div[1]/div[1]/div[1]'

    browse_button_xpath = '(//*[@id="browseContainer"])'
    live_button_xpath = '(//*[@id="liveStream"])'
    wake_button_id = 'wakeButton'
    video_browser_title_text_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/div' \
                                     '/div[1]/div[1]'
    browser_tab_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/div/div[1]/div[2]' \
                        '/lytx-tab-views/div/div[1]/button[1]'
    live_tab_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/div/div[1]/div[2]' \
                     '/lytx-tab-views/div/div[1]/button[2]'

    outside_view_tab_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/' \
                             'div/div[2]/player-tabs/div/div[2]/div[1]'
    map_live_tab_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/div/div[2]' \
                         '/livestream/div/div[1]/div[2]'
    gps_speed_text_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/div/div[2]' \
                           '/livestream/div/div[2]/span'

    save_to_library_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/div/div[2]' \
                            '/simultaneous-view-browser/div[1]/div[2]/browser-control-bar/div' \
                            '/div[1]/div[3]/div[4]/i'
    video_name_input_box_xpath = '/html/body/app-root/shell/div/div/div/browse-vehicle/div/div[3]' \
                                 '/simultaneous-view-browser/div[1]/div[2]/browser-control-bar/' \
                                 'div/trim-transfer-dialog/div/div/div[1]/div[1]/input'
    save_button_id = 'saveButton'
    go_to_video_button_xpath = '/html/body/ngb-modal-window/div/div/action-modal/lytx-modal-shell' \
                               '/div/div[2]/div[3]/button[2]'
    length_value_id = 'clipLength'
    profile_xpath = '//span[@id="profileButton"]'
    sign_out_button_xpath = '//*[text()="Sign Out"]'
    vehicles_tab_xpath = '//*[text()="Vehicles"]'
    no_vehicles_found_xpath = '//*[contains(text(), "No vehicles found.")]'
    no_vehicles_or_videos_found_xpath = '//*[text()="No vehicles found." or text()="No videos found."]'
    retry_button_id = 'retryButton'


    # New UI left panel xpath
    vehicles_menu_xpath = '//*[@class="menu-text" and text()=" Vehicles "]'
    map_search_menu_xpath = '//*[@class="menu-text" and text()=" Map Search "]'
    vs_library_menu_xpath = '//*[@class="menu-text" and text()=" Library "]'
    saved_videos_submenu_xpath = '//*[@href = "#/lvs/library/saved"]'
    video_tags_submenu_xpath = '//*[@href = "#/lvs/library/tagged"]'
    pagination_dropdown_xpath = '(//*[contains(text(), "Show: 10")])[1]'
    select_pagination_xpath = '//*[contains(text(), "Show: 50")]'
    right_arrow_button_xpath = '//*[@class="lx-icon lx-chevron-lrg-right"]'
    left_arrow_button_xpath = '//*[@class="lx-icon lx-chevron-lrg-left"]'
    page_result_xpath = '//*[@class="amount-of-pages"]'
    edit_name_option_xpath = '//*[@class="video-details__pen-icon ng-star-inserted"]'
    video_name_text_id = 'videoNameTitle'
    vehicle_name_text_id = 'vehicleTitle'
    video_length_text_id = 'clipLengthTitle'
    view_text_id = 'viewsTitle'
    video_date_text_id = 'eventDateTitle'
    request_date_text_id = 'requestDateTitle'
    last_7_days_xpath = '//*[text()=" Last 7 Days "]'
    download_csv_button_in_vehicles_page_xpath = '//*[@class="download-csv"]'
    tooltip_icon_xpath = '(//*[@class="lytx-info-icon"])[1]'
    device_information_title_xpath = '//*[@class="vehicle-list__list__item__tooltip__header"]'
    device_serial_number_with_device_status_id = 'serialNumber'
    last_communication_id = 'lastCommunication'
    date_filter_xpath = '//*[@class="lytx-datepicker__selector lytx-datepicker__selector__active"]'
    save_video_button_xpath = '//*[@class="lx-icon lx-saved-video"]'
    vehicle_name_xpath = '//*[@class="browse-vehicle__header-bar__vehicle"]'
    play_pause_button_xpath = '//*[@class="browser-control-bar__playback__controls__play"]'
    playback_speed_option_xpath = '//*[@class="browser-control-bar__playback__actions__speed-options"]'
    time_dropdown_xpath = '//*[@class="browser-control-bar__timeframe__control"]'
    trip_inprogress_markers_on_timeline_xpath = '//*[text()="Trip In-Progress "]'
    alerts_on_timeline_xpath = '//*[text()="Alerts "]'
    events_on_timeline_xpath = '//*[text()="Events "]'
    select_the_vehicle_xpath = '(//*[@class="lx-icon table-checkbox lx-checkbox-inactive"])[1]'
    delete_button_xpath = '//*[text()="Delete Videos"]'
    confirm_button_id = 'modalShellPrimaryButton'
    video_deleted_popup_xpath = '//*[@aria-label="Success - 1 video deleted."]'
    lytx_geotab_logo_xpath = '//*[@class="logo-container__lytx_geotab_logo"]'
    download_icon_xpath = '//*[@id="downloadIcon"]'
    download_dce_button_xpath = '//*[text()=" Download DCE "]'
    download_button_xpath = '//*[text()=" Download "]'
    error_message_xpath = '//*[@id="required-label"]'
    map_search_tab_xpath = '//*[contains(text(),"Map Search")]'
    select_date_xpath = ' (//*[contains(@class, "custom-day")])[2]'
    time_filter_xpath = ' //*[@class="dropdown__select"]'
    select_time_in_filter_xpath = ' //*[text()=" 12:30 AM - 1:00 AM "]'
    search_address_box_map_search_xpath = ' //*[@id="locationPickerInput"]'
    select_searched_address_map_search_xpath = '(//*[@class="pac-item"])[1]'
    selected_time_range_xpath = '//*[text()=" Vehicles (12:30 AM - 1:00 AM) "]'
    video_expired_popup_xpath = '//*[text()="Video Expired"]'
    video_expired_popup_ok_button_id = 'modalShellPrimaryButton'
    select_1_view_from_available_views_xpath = '//*[@class="lx-icon lx-1-view"]'
    available_views_dropdown_xpath = '//*[@class="layout-selector__button"]'
    map_tab_xpath = '//*[@aria-label="Map"]'
    map_zoom_in_button_xpath = '(//*[@aria-label="Zoom in"])[2]'
    map_zoom_out_button_xpath = '(//*[@aria-label="Zoom out"])[2]'
    map_camera_control_button_xpath = '//*[@aria-label="Map camera controls"]'
    view_on_icon_xpath = '//*[contains(@class, "lx-icon lx-3-views")]'
    select_1st_view_xpath = '//*[@class="lx-icon lx-1-view"]'
    view_1_displayed_xpath = '(//*[@class="simultaneous-view__header"])[1]'
    view_2_displayed_xpath = '(//*[@class="simultaneous-view__header"])[2]'
    vehicle_dropdown_xpath = '(//*[@class="title"])[1]'
    map_browse_button_xpath = '(//*[@id="browseContainer"])[1]'
    back_to_vehicles_button_id = 'primary-button'
    connection_issue_title_xpath = '//*[@class="error-modal__title"]'
    live_button_additional_xpath = '/following-sibling::div)[1]'
    enable_video_stitching_section_xpath = '//*[@class="download-videos-modal__video-stitching-title"]'
    views_dropdown_xpath = '//*[@data-test-id="multiselectDropdown-selectContent-span"]'
    select_outside_view_xpath = '(//*[contains(@class, "lx-checkbox-active")])[1]'
    select_inside_view_xpath = '(//*[contains(@class, "lx-checkbox-active")])[1]'
    deselect_inside_view_xpath = '(//*[contains(@class, "lx-checkbox-inactive")])[1]'
    media_type_dce_xpath = '//*[text()=" Download DCE "]'
    enable_stitching_toggle_xpath = '//*[@class="slider round"]'
    error_message_download_hd_video_longer_than_3_minutes_xpath = '//*[text()="Unavailable for HD videos longer than 3 minutes"]'
    cancel_button_xpath = '//*[text()=" Cancel "]'
    download_mp4_button_xpath = '//*[text()=" Download MP4 "]'
    cross_button_xpath = '//*[contains(@class, "lx-icon lx-close-x ")]'

