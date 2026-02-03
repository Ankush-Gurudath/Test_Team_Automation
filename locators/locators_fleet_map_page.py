class LocatorsFleetMap:
    fleet_tracking_title_id = 'fleetTrackingText'

    # Map Section
    working_list_tab_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                             '/div/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                             '/div[1]/lytx-tabs/div/div[1]'
    geofence_label_id = 'create-geofence'
    vehicle_name_label_xpath = '/html/body/app-root/shell/div/div/div' \
                               '/app-map/div/lytx-drawer/div/div/div[2]/app-working-list-new' \
                               '/div/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                               '/div[1]/div/div[2]/div[1]'
    history_selector_id = 'history-selector'
    apply_button_id = 'btn-apply'
    cancel_button_id = 'cancelButton'
    confirm_delete_id = 'modalShellPrimaryButton'
    delete_icon_id = 'deleteIcon'
    view_history_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                         '/div/lytx-fleet-tracker/div/div/div/div[8]/div/div/' \
                         'history-selector/div/div[1]'
    last_4_hours_xpath = '/html/body/app-root/shell/div/div/div/app-map/' \
                         'div/lytx-fleet-tracker/div/div/div/div[8]/div/div/history-selector' \
                         '/div/div[2]/lx-date-range-selector/div/div[2]/div[1]/div[2]'
    working_list_filter_xpath = '/html/body/app-root/shell/div/div/div' \
                                '/app-map/div/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                '/div/div[2]/div[2]/div/div[1]/multiselect-typeahead/div/div[1]' \
                                '/div/input'
    close_working_list_filter_xpath = '/html/body/app-root/shell/div/div/div' \
                                      '/app-map/div/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                      '/div/div[2]/div[2]/div/div[1]/multiselect-typeahead/div/div[2]/i'
    working_list_filter_prefix = 'multiselect-typeahead-1-'

    vehicle_name_in_history_xpath = '/html/body/app-root/shell/div/div/div/' \
                                    'app-map/div/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                    '/div/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport/' \
                                    'div[1]/div/div[2]/div[1]'
    delete_vehicle_history_xpath = '//*[@id="deleteIcon"]'
    # when there is only one message, use working_list_message
    working_list_message = '/html/body/app-root/shell/div/div/div/app-map/div' \
                           '/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]/div[2]' \
                           '/div/div[2]/div/div/div'
    # when there are multiple messages in working list, use working_list_message_x
    # those xpaths are not used for now
    working_list_message_one = '/html/body/app-root/shell/div/div/div/app-map' \
                               '/div/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                               '/div[2]/div/div[2]/div/div[1]/div'
    working_list_message_two = '/html/body/app-root/shell/div/div/div/app-map' \
                               '/div/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                               '/div[2]/div/div[2]/div/div[2]/div'
    working_list_message_three = '/html/body/app-root/shell/div/div/div/app-map' \
                                 '/div/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                                 '/div[2]/div/div[2]/div/div[3]/div'
    working_list_message_four = '/html/body/app-root/shell/div/div/div/app-map' \
                                '/div/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                                '/div[2]/div/div[2]/div/div[4]/div'
    working_list_message_five = '/html/body/app-root/shell/div/div/div/app-map' \
                                '/div/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                                '/div[2]/div/div[2]/div/div[5]/div'
    working_list_message_six = '/html/body/app-root/shell/div/div/div/app-map' \
                               '/div/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                               '/div[2]/div/div[2]/div/div[6]/div'
    working_list_message_seven = '/html/body/app-root/shell/div/div/div/app-map' \
                                 '/div/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                                 '/div[2]/div/div[2]/div/div[7]/div'

    select_vehicle_in_history_xpath = '/html/body/app-root/shell/div/div/div/' \
                                      'app-map/div/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                      '/div/div[1]/app-search-new/div/' \
                                      'ngb-typeahead-window/button[1]/div/span[2]'
    clear_working_list_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                               '/div/div/div[2]/app-working-list-new/div/div[2]/div[2]/div' \
                               '/div[1]/button'
    search_box_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                       '/div/div/div[2]/app-working-list-new/div/div[1]/app-search-new/div/input'
    search_icon_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                        '/div/div/div[2]/app-working-list-new/div/div[1]/app-search-new' \
                        '/div/span[1]'
    select_vehicle_xpath = '//*[@class="lx-checkbox-inactive lx-icon"]'
    suggestion_list_1st_item_id = 'ngb-typeahead-0-0'
    select_all_search_result_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                     '/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                     '/div/app-search-results-new/div/div[2]/div[2]'
    add_to_working_list_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                '/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                '/div/app-search-results-new/div/div[1]/button'
    moving_icon_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/' \
                        'lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                        '/div[2]/div/div[2]/cdk-virtual-scroll-viewport/div[1]' \
                        '/div/div[2]/ul/li[1]'
    speed_icon_id = 'speedViolation'
    idle_icon_id = 'idle'
    geofence_icon_id = 'geofenceTrigger'
    trip_icon_id = 'trips'
    routes_icon_id = 'routes'
    zoom_in_xpath = '//*[@class="zoom-control-in"]'
    zoom_out_xpath = '//*[@class="zoom-control-out"]'

    # settings tab
    settings_tab_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                         '/div/div/div[2]/app-working-list-new/div/div[2]/div[1]' \
                         '/lytx-tabs/div/div[2]/div'
    settings_load_no_vehicle = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                               '/div/div/div[2]/app-working-list-new/div/div[2]/div[2]/app-settings' \
                               '/form/div/div[4]/div[2]/div/div[4]/lytx-radio-button/label/div'
    settings_load_no_equipment = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                                 '/div/div/div[2]/app-working-list-new/div/div[2]/div[2]/app-settings' \
                                 '/form/div/div[4]/div[3]/div/lytx-radio-button[3]/label/div'
    settings_load_no_geofence = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                                '/div/div/div[2]/app-working-list-new/div/div[2]/div[2]/app-settings' \
                                '/form/div/div[4]/div[4]/div/lytx-radio-button[3]/label/div'

    # Map Section - pin detail
    live_map_pin_xpath = ('/html/body/app-root/shell/div/div/div/app-map/div/lytx-fleet-tracker/div/div/div[3]/div['
                          '1]/div[2]/div/div[3]/div[2]')
    pin_panel_close_xpath = ('/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer/div/div/div['
                             '2]/app-pin-detail/div/panel-close/div/button/div')
    live_pin_vehicle_name_xpath = '/html/body/app-root/shell/div/div/div' \
                                  '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                                  '/div/div/panel-header/div/div[2]'
    live_pin_status_xpath = '/html/body/app-root/shell/div/div/div' \
                            '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail/div' \
                            '/div/panel-body/div/panel-content[1]/div/div[2]/div[1]'
    live_pin_driver_xpath = '/html/body/app-root/shell/div/div/div' \
                            '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                            '/div/div/panel-body/div/panel-content[1]/div/div[2]/div[2]'
    live_pin_group_xpath = '/html/body/app-root/shell/div/div/div' \
                           '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                           '/div/div/panel-body/div/panel-content[1]/div/div[2]/div[3]'
    live_pin_device_xpath = '/html/body/app-root/shell/div/div/div' \
                            '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                            '/div/div/panel-body/div/panel-content[1]/div/div[2]/div[4]'
    live_pin_speed_xpath = '/html/body/app-root/shell/div/div/div' \
                           '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                           '/div/div/panel-body/div/panel-content[2]/div/div[2]/div[2]'
    live_pin_ignition_xpath = '/html/body/app-root/shell/div/div/div' \
                              '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                              '/div/div/panel-body/div/panel-content[2]/div/div[2]/div[3]'
    live_pin_triggering_geofences_xpath = '/html/body/app-root/shell/div/div/div' \
                                          '/app-map/div/lytx-drawer' \
                                          '/div/div/div[2]/app-pin-detail/div/div/panel-body' \
                                          '/div/panel-content[2]/div/div[2]/div[4]'
    live_pin_occur_time_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                '/div/lytx-drawer/div/div/div[2]/app-pin-detail/div/div/panel-body' \
                                '/div/panel-content[2]/div/div[2]/div[1]/div[1]'
    live_pin_time_since_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                '/div/lytx-drawer/div/div/div[2]/app-pin-detail/div/div/panel-body' \
                                '/div/panel-content[2]/div/div[2]/div[1]/div[3]'
    moving_pin_icon_working_list_xpath = '/html/body/app-root/shell/div/div/div' \
                                         '/app-map/div/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                         '/div/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                         '/div[1]/div/div[2]/ul/li/img'
    moving_pin_icon_panel_detail_xpath = '/html/body/app-root/shell/div/div/div' \
                                         '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                                         '/div/div/panel-header/div/div[1]/img'
    address_icon_panel_detail_xpath = '/html/body/app-root/shell/div/div/div' \
                                      '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                                      '/div/div/panel-body/div/panel-content[2]/div/div[1]/i'
    date_icon_panel_detail_xpath = '/html/body/app-root/shell/div/div/div' \
                                   '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                                   '/div/div/panel-body/div/copy-text/div/i'
    pin_panel_address_xpath = '/html/body/app-root/shell/div/div/div' \
                              '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                              '/div/div/panel-body/div/copy-text/div/div/div[1]'
    pin_panel_coordinate_xpath = '/html/body/app-root/shell/div/div/div' \
                                 '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                                 '/div/div/panel-body/div/copy-text/div/div/div[2]'
    trip_pin_address_xpath = '/html/body/app-root/shell/div/div/div' \
                             '/app-map/div/lytx-drawer/div/div/div[2]/trip-detail' \
                             '/div/panel-body/div/copy-text/div/div/div[1]'
    trip_pin_coordinate_xpath = '/html/body/app-root/shell/div/div/div' \
                                '/app-map/div/lytx-drawer/div/div/div[2]/trip-detail' \
                                '/div/panel-body/div/copy-text/div/div/div[2]'
    trip_pin_occur_time_xpath = '/html/body/app-root/shell/div/div/div' \
                                '/app-map/div/lytx-drawer/div/div/div[2]/trip-detail/div' \
                                '/panel-body/div/panel-content[2]/div/div[2]/div[1]/div[1]'
    trip_pin_time_since_xpath = '/html/body/app-root/shell/div/div/div' \
                                '/app-map/div/lytx-drawer/div/div/div[2]/trip-detail/div' \
                                '/panel-body/div/panel-content[2]/div/div[2]/div[1]/div[2]'

    # history date range
    date_range_start_month_xpath = '//*[@id="history-selector"]/div/div[2]/lx-date-range-selector' \
                                   '/div/div[1]/div[1]/div[2]/lx-date-input/div/input[1]'
    date_range_start_day_xpath = '//*[@id="history-selector"]/div/div[2]/lx-date-range-selector' \
                                 '/div/div[1]/div[1]/div[2]/lx-date-input/div/input[2]'
    date_range_start_year_xpath = '//*[@id="history-selector"]/div/div[2]/lx-date-range-selector' \
                                  '/div/div[1]/div[1]/div[2]/lx-date-input/div/input[3]'
    date_range_end_month_xpath = '//*[@id="history-selector"]/div/div[2]/lx-date-range-selector' \
                                 '/div/div[1]/div[3]/div[2]/lx-date-input/div/input[1]'
    date_range_end_day_xpath = '//*[@id="history-selector"]/div/div[2]/lx-date-range-selector' \
                               '/div/div[1]/div[3]/div[2]/lx-date-input/div/input[2]'
    date_range_end_year_xpath = '//*[@id="history-selector"]/div/div[2]/lx-date-range-selector' \
                                '/div/div[1]/div[3]/div[2]/lx-date-input/div/input[3]'

    # history moving track point
    view_moving_track_point_detail_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-fleet-tracker/div/div/div[3]/div[1]/div[2]/div/div[3]/div[1]'
    moving_panel_close_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                               '/div/div/div[2]/app-pin-detail/div/panel-close/div/button'
    moving_panel_vehicle_name_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/' \
                                      'lytx-drawer/div/div/div[2]/app-pin-detail/div/div/' \
                                      'panel-header/div/div[2]'
    moving_panel_status_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                                '/div/div/div[2]/app-pin-detail/div/div/panel-body/div/' \
                                'panel-content[1]/div/div[2]/div[1]'
    moving_panel_driver_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                                '/div/div/div[2]/app-pin-detail/div/div/panel-body/div/' \
                                'panel-content[1]/div/div[2]/div[2]'
    moving_panel_group_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                               '/div/div/div[2]/app-pin-detail/div/div/panel-body/div/' \
                               'panel-content[1]/div/div[2]/div[3]'
    moving_panel_device_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                                '/div/div/div[2]/app-pin-detail/div/div/panel-body/div/' \
                                'panel-content[1]/div/div[2]/div[4]'
    moving_panel_occur_time_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                                    '/div/div/div[2]/app-pin-detail/div/div/panel-body/div/' \
                                    'panel-content[2]/div/div[2]/div[1]/div[1]'
    moving_panel_since_time_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/' \
                                    'lytx-drawer/div/div/div[2]/app-pin-detail/div/div/' \
                                    'panel-body/div/panel-content[2]/div/div[2]/div[1]/div[2]'
    moving_panel_speed_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                               '/div/div/div[2]/app-pin-detail/div/div/panel-body/div/' \
                               'panel-content[2]/div/div[2]/div[2]'
    moving_panel_address_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                                 '/div/div/div[2]/app-pin-detail/div/div/panel-body/div/' \
                                 'copy-text/div/div/div[1]'
    moving_panel_coordinate_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                                    '/div/div/div[2]/app-pin-detail/div/div/panel-body/div/copy-text' \
                                    '/div/div/div[2]'
    moving_panel_google_street_view_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/' \
                                            'lytx-drawer/div/div/div[2]/app-pin-detail/div/div/panel-body' \
                                            '/div/panel-street-view/div/div/div[2]/div[1]/div[9]/div/div/canvas'

    # history trip start and trip end
    view_trip_start_detail_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-fleet-tracker/div/div/div[3]/div[1]/div[2]/div/div[3]/div[1]'
    view_trip_end_detail_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-fleet-tracker/div/div/div[3]/div[1]/div[2]/div/div[3]/div[2]'
    trip_panel_close_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                             '/lytx-drawer/div/div/div[2]/trip-detail/div/panel-close/div/button/div'
    trip_panel_vehicle_name_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                    '/div/lytx-drawer/div/div/div[2]/trip-detail/div/panel-header/div/div[2]'
    trip_tag_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                     '/lytx-drawer/div/div/div[2]/trip-detail/div/panel-body/div' \
                     '/panel-content[1]/div/div[2]/div[1]'
    trip_panel_driver_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                              '/lytx-drawer/div/div/div[2]/trip-detail/div/panel-body/div' \
                              '/panel-content[1]/div/div[2]/div[2]'
    trip_panel_group_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                             '/lytx-drawer/div/div/div[2]/trip-detail/div/panel-body/div' \
                             '/panel-content[1]/div/div[2]/div[3]'
    trip_panel_device_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                              '/lytx-drawer/div/div/div[2]/trip-detail/div/panel-body/div' \
                              '/panel-content[1]/div/div[2]/div[4]'
    trip_panel_trip_num_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                '/lytx-drawer/div/div/div[2]/trip-detail/div/panel-body/div/div'
    trip_panel_trip_duration_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                     '/div/lytx-drawer/div/div/div[2]/trip-detail/div/panel-body/div' \
                                     '/panel-content[2]/div/div[2]/div[2]'
    trip_panel_distance_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                '/div/lytx-drawer/div/div/div[2]/trip-detail/div/panel-body/div' \
                                '/panel-content[2]/div/div[2]/div[3]'
    trip_panel_max_speed_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                 '/div/lytx-drawer/div/div/div[2]/trip-detail/div/panel-body/div' \
                                 '/panel-content[2]/div/div[2]/div[4]'

    # history violations and activation details
    view_speed_violation_detail_xpath = ('/html/body/app-root/shell/div/div/div/app-map/div/lytx-fleet-tracker/div'
                                         '/div/div[3]/div[1]/div[2]/div/div[3]/div[1]')
    speed_violation_pin_speed_limit_xpath = '/html/body/app-root/shell/div/div/div' \
                                            '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                                            '/div/div/panel-body/div/panel-content[2]/div/div[2]/div[2]'
    speed_violation_pin_max_speed_xpath = '/html/body/app-root/shell/div/div/div' \
                                          '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                                          '/div/div/panel-body/div/panel-content[2]/div/div[2]/div[3]'
    speed_violation_pin_duration_xpath = '/html/body/app-root/shell/div/div/div' \
                                         '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                                         '/div/div/panel-body/div/panel-content[2]/div/div[2]/div[4]'
    speed_violation_pin_time_since_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                           '/lytx-drawer/div/div/div[2]/app-pin-detail/div/div' \
                                           '/panel-body/div/panel-content[2]/div/div[2]/div[1]/div[2]'

    view_idle_violation_detail_xpath = '//lytx-fleet-tracker/div/div/div[3]/div[1]/div[2]/div/div[3]/div[{0}]'
    idle_violation_pin_duration_xpath = '/html/body/app-root/shell/div/div/div' \
                                        '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                                        '/div/div/panel-body/div/panel-content[2]/div/div[2]/div[2]'
    idle_violation_pin_time_since_xpath = '/html/body/app-root/shell/div/div/div' \
                                          '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                                          '/div/div/panel-body/div/panel-content[2]/div/div[2]/div[1]/div[2]'
    view_geofence_violation_start_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-fleet-tracker/div/div/div[3]/div[1]/div[2]/div/div[3]/div[2]'
    view_geofence_violation_end_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-fleet-tracker/div/div/div[3]/div[1]/div[2]/div/div[3]/div[3]'
    geofence_violation_duration_xpath = '/html/body/app-root/shell/div/div/div' \
                                        '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                                        '/div/div/panel-body/div/panel-content[2]/div/div[2]/div[2]'
    geofence_violation_time_since_xpath = '/html/body/app-root/shell/div/div/div' \
                                          '/app-map/div/lytx-drawer/div/div/div[2]/app-pin-detail' \
                                          '/div/div/panel-body/div/panel-content[2]/div/div[2]/div[1]/div[2]'

    # geofence details
    view_geofence_detail_xpath = '/html/body/app-root/shell/div/div/div' \
                                 '/app-map/div/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                 '/div/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                 '/div[1]/div/div[2]/div[4]/button'
    geofence_detail_close_xpath = '//*[@class="close-text"]'
    geofence_detail_name_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                 '/div/lytx-drawer/div/div/div[2]/geofence-detail/div' \
                                 '/panel-header/div/div[2]'
    geofence_detail_setting_xpath = '/html/body/app-root/shell/div/div/div' \
                                    '/app-map/div/lytx-drawer/div/div/div[2]/geofence-detail' \
                                    '/div/panel-body/div/div'
    geofence_detail_status_xpath = '/html/body/app-root/shell/div/div/div' \
                                   '/app-map/div/lytx-drawer/div/div/div[2]/geofence-detail' \
                                   '/div/panel-body/div/panel-content[1]/div/div[2]/div[1]'
    geofence_detail_facing_xpath = '/html/body/app-root/shell/div/div/div' \
                                   '/app-map/div/lytx-drawer/div/div/div[2]/geofence-detail' \
                                   '/div/panel-body/div/panel-content[1]/div/div[2]/div[2]'
    geofence_detail_days_xpath = '/html/body/app-root/shell/div/div/div' \
                                 '/app-map/div/lytx-drawer/div/div/div[2]/geofence-detail' \
                                 '/div/panel-body/div/panel-content[1]/div/div[2]/div[3]'
    geofence_detail_time_xpath = '/html/body/app-root/shell/div/div/div' \
                                 '/app-map/div/lytx-drawer/div/div/div[2]/geofence-detail' \
                                 '/div/panel-body/div/panel-content[1]/div/div[2]/div[4]'
    geofence_detail_vehicles_xpath = '/html/body/app-root/shell/div/div/div' \
                                     '/app-map/div/lytx-drawer/div/div/div[2]/geofence-detail' \
                                     '/div/panel-body/div/panel-content[1]/div/div[2]/div[5]'
    geofence_detail_edit_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                 '/lytx-drawer/div/div/div[2]/geofence-detail/div/panel-body/div' \
                                 '/panel-content[2]/div/div[2]/div/button[1]'
    geofence_detail_delete_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                   '/lytx-drawer/div/div/div[2]/geofence-detail/div/panel-body/div' \
                                   '/panel-content[2]/div/div[2]/div/button[2]'
    trip_start_map_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-fleet-tracker/div/div/div[3]/div[1]/div[2]/div/div[3]/div[4]/img'
    trip_end_map_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-fleet-tracker/div/div/div[3]/div[1]/div[2]/div/div[3]/div[5]/img'

    # create/add/edit geofence
    working_list_2nd_geofence_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                      '/div/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                      '/div/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                      '/div[1]/div[2]/div[1]/i'
    working_list_geofence_name_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                       '/div/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                                       '/div[2]/div/div[2]/cdk-virtual-scroll-viewport/div[1]/div/div[2]/div[1]'
    working_list_geofence_status_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                         '/div/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                                         '/div[2]/div/div[2]/cdk-virtual-scroll-viewport/div[1]/div/div[2]/div[2]'
    working_list_geofence_type_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                       '/div/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                                       '/div[2]/div/div[2]/cdk-virtual-scroll-viewport/div[1]/div/div[2]/div[3]'
    working_list_geofence_name_1st_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                           '/div/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                                           '/div[2]/div/div[2]/cdk-virtual-scroll-viewport/div[1]/div/div[2]/div[1]'
    working_list_geofence_status_1st_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                             '/div/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                                             '/div[2]/div/div[2]/cdk-virtual-scroll-viewport/div[1]/div/div[2]/div[2]'
    working_list_geofence_type_1st_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                           '/div/lytx-drawer/div/div/div[2]/app-working-list-new/div/div[2]' \
                                           '/div[2]/div/div[2]/cdk-virtual-scroll-viewport/div[1]/div/div[2]/div[3]'
    working_list_geofence_name_2nd_xpath = '/html/body/app-root/shell/div/div/div' \
                                           '/app-map/div/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                           '/div/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                           '/div[1]/div[2]/div[2]/div[1]'
    working_list_geofence_status_2nd_xpath = '/html/body/app-root/shell/div/div/div' \
                                             '/app-map/div/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                             '/div/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                             '/div[1]/div[2]/div[2]/div[2]/span'
    working_list_geofence_type_2nd_xpath = '/html/body/app-root/shell/div/div/div' \
                                           '/app-map/div/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                           '/div/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                           '/div[1]/div[2]/div[2]/div[3]/span'
    working_list_geofence_prefix = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer/div' \
                                   '/div/div[2]/app-working-list-new/div/div[2]/div[2]/div/div[2]' \
                                   '/cdk-virtual-scroll-viewport/div[1]/div['
    working_list_geofence_name_suffix = ']/div[2]/div[1]'
    working_list_geofence_view_detail_suffix = ']/div[2]/div[4]/button'

    create_geofence_settings_id = 'create-geofence'
    create_geofence_save_xpath = '//*[@id="createGeofenceButton"]'
    geofence_shape_use_address_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                                       '/div/div/div[2]/app-geofence-edit-v2/div/panel-body/div' \
                                       '/panel-content[2]/div/div/fleet-tracker-geofence/div/button[4]'
    geofence_shape_custom_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                  '/lytx-drawer/div/div/div[2]/app-geofence-edit-v2/div/panel-body/div' \
                                  '/panel-content[2]/div/div/fleet-tracker-geofence/div/button[3]'
    geofence_shape_square_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                  '/lytx-drawer/div/div/div[2]/app-geofence-edit-v2/div/panel-body/div' \
                                  '/panel-content[2]/div/div/fleet-tracker-geofence/div/button[2]'
    geofence_shape_circle_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                  '/lytx-drawer/div/div/div[2]/app-geofence-edit-v2/div/panel-body/div' \
                                  '/panel-content[2]/div/div/fleet-tracker-geofence/div/button[1]'
    geofence_location_id = 'locationPickerInput'
    geofence_name_id = 'nameInput'

    # Find closest vehicles
    view_detail_address_xpath = '/html/body/app-root/shell/div/div/div' \
                                '/app-map/div/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                '/div/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                '/div[1]/div[1]/div[2]/div[3]/button'
    find_closest_vehicle_xpath = '/html/body/app-root/shell/div/div/div' \
                                 '/app-map/div/lytx-drawer/div/div/div[2]/app-address/div' \
                                 '/panel-body/div/span/div/button'
    title_find_closest_vehicle_xpath = '/html/body/app-root/shell/div/div/div' \
                                       '/app-map/div/lytx-drawer/div/div/div[2]/app-closest-vehicles/div/div'
    address_find_closest_vehicle_xpath = '/html/body/app-root/shell/div/div/div' \
                                         '/app-map/div/lytx-drawer/div/div/div[2]/app-closest-vehicles' \
                                         '/div/panel-body/div/copy-text/div/div/div[1]'
    coordinates_find_closest_vehicle_xpath = '/html/body/app-root/shell/div/div/div' \
                                             '/app-map/div/lytx-drawer/div/div/div[2]/app-closest-vehicles' \
                                             '/div/panel-body/div/copy-text/div/div/div[2]'
    vehicle_name_1st_closest_vehicle_xpath = '/html/body/app-root/shell/div/div/div' \
                                             '/app-map/div/lytx-drawer/div/div/div[2]/app-closest-vehicles' \
                                             '/div/panel-body/div/div/panel-content/div/div[2]/div[1]/div[1]'
    vehicle_driver_1st_find_closest_vehicle_xpath = '/html/body/app-root/shell/div/div/div' \
                                                    '/app-map/div/lytx-drawer/div/div/div[2]/app-closest-vehicles' \
                                                    '/div/panel-body/div/div/panel-content/div/div[2]/div[1]/div[2]'
    vehicle_group_1st_find_closest_vehicle_xpath = '/html/body/app-root/shell/div/div/div' \
                                                   '/app-map/div/lytx-drawer/div/div/div[2]/app-closest-vehicles' \
                                                   '/div/panel-body/div/div/panel-content/div/div[2]/div[1]/div[3]'
    vehicle_time_1st_find_closest_vehicle_xpath = '/html/body/app-root/shell/div/div/div' \
                                                  '/app-map/div/lytx-drawer/div/div/div[2]/app-closest-vehicles' \
                                                  '/div/panel-body/div/div/panel-content/div/div[2]/div[2]/div[1]'
    vehicle_distance_1st_find_closest_vehicle_xpath = '/html/body/app-root/shell/div/div/div' \
                                                      '/app-map/div/lytx-drawer/div/div/div[2]/app-closest-vehicles' \
                                                      '/div/panel-body/div/div/panel-content/div/div[2]/div[2]/div[2]'
    delete_1st_vehicle_find_closest_vehicle_id = 'deleteIcon'
    closest_vehicle_panel_close_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                        '/lytx-drawer/div/div/div[2]/app-closest-vehicles/div/panel-close/div/button'

    # Actions when the toggle ENABLE_FLEET_TRACKING_DASHBOARD set as true
    map_with_home_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[2]'

    # Actions when the toggle ENABLE_FLEET_TRACKING_DASHBOARD set as false
    map_xpath = '(.//*[text()="Map"])[1]'
    map_new_ui_xpath = '//*[text()=" Map "]'

    # equipment
    equipment_working_list_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer/div/div/div[2]' \
                                   '/app-working-list-new/div/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                   '/div[1]/div/div[2]/div[1]'
    equipment_live_map_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-fleet-tracker/div/div/div[3]/div[1]/div[2]/div/div[3]/div[2]'
    equipment_state_working_list_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                                         '/div/div/div[2]/app-working-list-new/div/div[2]/div[2]/div/div[2]' \
                                         '/cdk-virtual-scroll-viewport/div[1]/div'
    live_pin_equipment_name_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                                    '/div/div/div[2]/app-pin-detail/div/div/panel-header/div/div[2]'
    live_pin_equipment_status_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer/div/div/div[2]' \
                                      '/app-pin-detail/div/div/panel-body/div/panel-content[1]/div/div[2]/div[1]'
    live_pin_equipment_group_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer/div/div/div[2]' \
                                     '/app-pin-detail/div/div/panel-body/div/panel-content[1]/div/div[2]/div[2]'
    live_pin_equipment_device_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer/div/div/div[2]' \
                                      '/app-pin-detail/div/div/panel-body/div/panel-content[1]/div/div[2]/div[3]'
    live_pin_equipment_occur_time_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer/div/div/div[2]' \
                                          '/app-pin-detail/div/div/panel-body/div/panel-content[2]/div/div[2]/div/div[1]'
    live_pin_equipment_time_since_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer/div/div/div[2]' \
                                          '/app-pin-detail/div/div/panel-body/div/panel-content[2]/div/div[2]/div/div[2]'
    live_pin_equipment_address_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer/div/div/div[2]' \
                                       '/app-pin-detail/div/div/panel-body/div/copy-text/div/div/div[1]'
    live_pin_equipment_coordinate_since_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                                                '/div/div/div[2]/app-pin-detail/div/div/panel-body/div' \
                                                '/copy-text/div/div/div[2]'
    working_list_button_xpath = '//*[text()="Working List"]'
    map_button_xpath ='//*[@class="lx-btn-small lx-btn-negative search-list-item-btn map-button"]'
    map_button_new_ui_xpath = '//*[text()=" Map "]'
    check_box_button_xpath = '//*[@class="lx-checkbox-inactive lx-icon"]'
    name_text_xpath = '//*[@class="detail-header"]'
    clear_search_box_xpath = '(//*[@class="lx-icon lx-close-x"])[1]'
    right_faced_arrow_xpath = '//*[@class="lx-icon lx-arrow-forward"]'
    left_faced_arrow_xpath = '//*[@class="lx-icon lx-arrow-forward rotate-180"]'
    left_navigation_collapsed_xpath = '//*[@class="lx-icon lx-arrow-forward"]'
    left_navigation_expanded_xpath = '//*[@class="lx-icon lx-arrow-forward rotate-180"]'

