class LocatorsFleetInsights:
    fleet_tracking_title_id = 'fleetTrackingText'
    apply_button_id = 'btn-apply'

    # Insights_Fleet Operation
    fleet_operations_title_xpath = '/html/body/app-root/shell/div/' \
                                   'div/div/app-fleet-operations/div/div[1]'
    groups_tab_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-operations' \
                            '/div/div[2]/lytx-tab-views/div/div[1]/button[1]/span'
    vehicles_tab_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-operations/div' \
                         '/div[2]/lytx-tab-views/div/div[1]/button[2]'
    vehicles_tab_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-operations' \
                              '/div/div[2]/lytx-tab-views/div/div[1]/button[2]/span'
    drivers_tab_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-operations/div' \
                        '/div[2]/lytx-tab-views/div/div[1]/button[3]'
    drivers_tab_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-operations' \
                             '/div/div[2]/lytx-tab-views/div/div[1]/button[3]/span'

    # Filter Group
    group_filter_button_group_xpath = '//*[@class="group-filter__label"]'
    group_filter_button_vehicle_xpath = '/html/body/app-root/shell/div/div/div' \
                                        '/app-fleet-operations/div/div[2]' \
                                        '/lytx-tab-views/div/div[2]/lytx-tab-view[2]' \
                                        '/div/app-fleet-operations-vehicles/div/div[1]' \
                                        '/lx-filter-bar/div/div/div[2]/group-filter/div'
    group_filter_button_driver_xpath = '/html/body/app-root/shell/div/div/div' \
                                       '/app-fleet-operations/div/div[2]/lytx-tab-views' \
                                       '/div/div[2]/lytx-tab-view[3]/div' \
                                       '/app-fleet-operations-drivers/div/div[1]' \
                                       '/lx-filter-bar/div/div/div[2]/group-filter/div'
    search_by_group_textbox_xpath = '/html/body/ngb-modal-window/div/div/' \
                                    'group-selector-modal/group-selector' \
                                    '/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_search_button_xpath = '(//*[@class="dropdown-item active"])[1]'
    select_vehicle_search_button_stg_xpath = '//*[text()="***Root > ***a group1 > ***Klint Crawford"]'
    done_button_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal' \
                        '/group-selector/div/div[3]/button[2]'

    # Filter Date
    date_filter_group_xpath = '//*[@class="lx-date-range-filter"]'
    date_filter_vehicle_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-operations/div' \
                                '/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[2]/div' \
                                '/app-fleet-operations-vehicles/div/div[1]/lx-filter-bar/div' \
                                '/div/div[2]/lx-date-range-filter/div/div[1]'
    date_filter_driver_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-operations/div' \
                               '/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[3]/div' \
                               '/app-fleet-operations-drivers/div/div[1]/lx-filter-bar/div/div' \
                               '/div[2]/lx-date-range-filter/div/div[1]'

    from_date_group_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-operations/div' \
                            '/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[1]/div' \
                            '/app-fleet-operations-group/div/div[1]/lx-filter-bar/div/div' \
                            '/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                            '/div/div[2]/div[2]/ngb-datepicker/div[2]/div[1]' \
                            '/ngb-datepicker-month/div[3]/div[2]/span/span'
    from_date_vehicle_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-operations/div' \
                              '/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[2]/div' \
                              '/app-fleet-operations-vehicles/div/div[1]/lx-filter-bar' \
                              '/div/div/div[2]/lx-date-range-filter/div/div[2]' \
                              '/lx-date-range-selector/div/div[2]/div[2]/ngb-datepicker' \
                              '/div[2]/div[1]/ngb-datepicker-month/div[3]/div[5]/span/span'
    from_date_driver_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-operations/div' \
                             '/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[3]/div' \
                             '/app-fleet-operations-drivers/div/div[1]/lx-filter-bar/div/div' \
                             '/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                             '/div/div[2]/div[2]/ngb-datepicker/div[2]/div[1]' \
                             '/ngb-datepicker-month/div[3]/div[4]/span/span'

    end_date_group_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-operations/div' \
                           '/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[1]/div' \
                           '/app-fleet-operations-group/div/div[1]/lx-filter-bar/div/div' \
                           '/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                           '/div/div[2]/div[2]/ngb-datepicker/div[2]/div[1]' \
                           '/ngb-datepicker-month/div[4]/div[5]/span/span'
    end_date_vehicle_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-operations/div' \
                             '/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[2]/div' \
                             '/app-fleet-operations-vehicles/div/div[1]/lx-filter-bar/div/div' \
                             '/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                             '/div/div[2]/div[2]/ngb-datepicker/div[2]/div[1]' \
                             '/ngb-datepicker-month/div[4]/div[7]/span/span'
    end_date_driver_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-operations/div' \
                            '/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[3]/div' \
                            '/app-fleet-operations-drivers/div/div[1]/lx-filter-bar/div/div' \
                            '/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                            '/div/div[2]/div[2]/ngb-datepicker/div[2]/div[1]' \
                            '/ngb-datepicker-month/div[5]/div[6]/span/span'
    last_90_days_driver_xpath = '//*[text()=" Last 90 Days "]'
    last_90_days_vehicle_xpath = '//*[text()=" Last 90 Days "]'

    # reset button
    reset_driver_tab_button_xpath = '//*[@class="reset-button-text"]'

    # link to driver profile page
    driver_name_xpath = '//cdk-table/cdk-row/cdk-cell[1]/div/div/div/div'

    # Insights_Geofences
    geofences_title_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-summary' \
                            '/div/div[1]/filter-bar/div/div[1]/span[1]'
    geofences_group_filter_button_xpath = '/html/body/app-root/shell/div/div/div' \
                                          '/app-geofence-summary/div/div[1]/filter-bar' \
                                          '/div/div[2]/div[2]/group-filter/div/span'
    geofences_search_by_group_textbox_xpath = '/html/body/ngb-modal-window/div/div/' \
                                              'group-selector-modal/group-selector/div/' \
                                              'div[1]/div[2]/div/lytx-typeahead/div/input'
    geofences_select_search_button_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal' \
                                           '/group-selector/div/div[1]/div[2]/div/lytx-typeahead' \
                                           '/div/ngb-typeahead-window/button'
    geofences_search_geofence_xpath = '/html/body/app-root/shell/div/div/div' \
                                      '/app-geofence-summary/div/div[1]/div' \
                                      '/lytx-typeahead/div/input'
    geofences_search_geofence_1st_xpath = '/html/body/app-root/shell/div/div/div' \
                                          '/app-geofence-summary/div/div[1]/div' \
                                          '/lytx-typeahead/div/ngb-typeahead-window/button'

    geofences_done_button_xpath = '/html/body/ngb-modal-window/div/div/' \
                                  'group-selector-modal/group-selector/div/div[3]/button[2]'
    geofences_date_filter_xpath = '/html/body/app-root/shell/div/div/div/' \
                                  'app-geofence-summary/div/div[1]/filter-bar' \
                                  '/div/div[2]/div[2]/lx-date-range-filter/div/div[1]'
    geofences_last_60_days_xpath = '/html/body/app-root/shell/div/div/div/' \
                                   'app-geofence-summary/div/div[1]/filter-bar' \
                                   '/div/div[2]/div[2]/lx-date-range-filter/' \
                                   'div/div[2]/lx-date-range-selector/div/div[2]/div[1]/div[3]'
    geofences_date_range_start_month_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-summary' \
                                             '/div/div[1]/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                             '/div/div[2]/lx-date-range-selector/div/div[1]/div[1]/div[2]' \
                                             '/lx-date-input/div/input[1]'
    geofences_date_range_start_day_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-summary' \
                                           '/div/div[1]/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                           '/div/div[2]/lx-date-range-selector/div/div[1]/div[1]/div[2]' \
                                           '/lx-date-input/div/input[2]'
    geofences_date_range_start_year_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-summary' \
                                            '/div/div[1]/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                            '/div/div[2]/lx-date-range-selector/div/div[1]/div[1]/div[2]' \
                                            '/lx-date-input/div/input[3]'
    geofences_date_range_end_month_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-summary' \
                                           '/div/div[1]/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                           '/div/div[2]/lx-date-range-selector/div/div[1]/div[2]/div[2]' \
                                           '/lx-date-input/div/input[1]'
    geofences_date_range_end_day_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-summary' \
                                         '/div/div[1]/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                         '/div/div[2]/lx-date-range-selector/div/div[1]/div[2]/div[2]' \
                                         '/lx-date-input/div/input[2]'
    geofences_date_range_end_year_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-summary' \
                                          '/div/div[1]/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                          '/div/div[2]/lx-date-range-selector/div/div[1]/div[2]/div[2]' \
                                          '/lx-date-input/div/input[3]'

    # Insights_Geofence profile
    geofence_profile_search_geofence_xpath = '/html/body/app-root/shell/div/div/div' \
                                             '/app-geofence-profile/div/div[2]/div[1]' \
                                             '/lytx-typeahead/div/input'
    geofence_profile_search_geofence_1st_xpath = '/html/body/app-root/shell/div/div/div' \
                                                 '/app-geofence-profile/div/div[2]/div[1]' \
                                                 '/lytx-typeahead/div/ngb-typeahead-window/button'
    geofence_profile_metadata_name_xpath = '/html/body/app-root/shell/div/div/div' \
                                           '/app-geofence-profile/div/div[2]/div[2]/div/div[1]/div[1]'
    geofence_profile_metadata_date_created_xpath = '/html/body/app-root/shell/div/div/div' \
                                                   '/app-geofence-profile/div/div[2]/div[2]/div/div[2]/div[1]'
    geofence_profile_metadata_days_applied_xpath = '/html/body/app-root/shell/div/div/div' \
                                                   '/app-geofence-profile/div/div[2]/div[2]/div/div[3]/div[1]'
    geofence_profile_metadata_time_xpath = '/html/body/app-root/shell/div/div/div' \
                                           '/app-geofence-profile/div/div[2]/div[2]/div/div[4]/div[1]'
    geofence_profile_metadata_type_xpath = '/html/body/app-root/shell/div/div/div' \
                                           '/app-geofence-profile/div/div[2]/div[2]/div/div[5]/div[1]'
    geofence_profile_metadata_group_xpath = '/html/body/app-root/shell/div/div/div' \
                                            '/app-geofence-profile/div/div[2]/div[2]/div/div[6]/div[1]'
    geofence_profile_metadata_subgroup_xpath = '/html/body/app-root/shell/div/div/div' \
                                               '/app-geofence-profile/div/div[2]/div[2]/div/div[7]/div[1]'
    geofence_profile_metadata_vehicles_xpath = '/html/body/app-root/shell/div/div/div' \
                                               '/app-geofence-profile/div/div[2]/div[2]/div/div[8]/div[1]'
    geofence_profile_summary_date_picker_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                 '/div/div[3]/div[1]/lx-date-range-filter/div/div[1]/span'
    geofence_profile_summary_total_trigger_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                   '/div/div[3]/div[2]/lx-metadata-bar/div/div/div[1]/div[1]'
    geofence_profile_summary_total_duration_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                    '/div/div[3]/div[2]/lx-metadata-bar/div/div/div[2]/div[1]'
    geofence_profile_summary_total_vehicle_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                   '/div/div[3]/div[2]/lx-metadata-bar/div/div/div[3]/div[1]'
    geofence_profile_summary_driving_time_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                  '/div/div[3]/div[2]/lx-metadata-bar/div/div/div[4]/div[1]'
    geofence_profile_summary_idle_time_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                               '/div/div[3]/div[2]/lx-metadata-bar/div/div/div[5]/div[1]'
    geofence_profile_summary_stop_time_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                               '/div/div[3]/div[2]/lx-metadata-bar/div/div/div[6]/div[1]'
    geofence_profile_summary_total_trigger_count_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                         '/div/div[3]/div[2]/lx-metadata-bar/div/div/div[1]/div[2]'
    geofence_profile_summary_total_duration_time_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                         '/div/div[3]/div[2]/lx-metadata-bar/div/div/div[2]/div[2]'
    geofence_profile_summary_total_vehicle_count_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                         '/div/div[3]/div[2]/lx-metadata-bar/div/div/div[3]/div[2]'
    geofence_profile_summary_driving_time_num_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                      '/div/div[3]/div[2]/lx-metadata-bar/div/div/div[4]/div[2]'
    geofence_profile_summary_idle_time_num_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                   '/div/div[3]/div[2]/lx-metadata-bar/div/div/div[5]/div[2]'
    geofence_profile_summary_stop_time_num_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                   '/div/div[3]/div[2]/lx-metadata-bar/div/div/div[6]/div[2]'
    geofence_profile_detail_triggers_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                             '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div' \
                                             '/lytx-accordion/div/div[1]'
    geofence_profile_trigger_vehicle_xpath = '(//*[@class="data-item-title"])[1]'
    geofence_profile_trigger_trigger_start_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                   '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div/' \
                                                   'lytx-accordion/div/div[2]/div/div/div/ul/li[1]/p[1]'
    geofence_profile_trigger_trigger_end_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                 '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div/' \
                                                 'lytx-accordion/div/div[2]/div/div/div/ul/li[2]/p[1]'
    geofence_profile_trigger_driver_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                            '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div/' \
                                            'lytx-accordion/div/div[2]/div/div/div/div[2]/span[1]'
    geofence_profile_trigger_trigger_type_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                  '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div/' \
                                                  'lytx-accordion/div/div[2]/div/div/div/div[3]/span[1]'
    geofence_profile_trigger_driving_time_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                  '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div/' \
                                                  'lytx-accordion/div/div[2]/div/div/div/div[4]/span[1]'
    geofence_profile_trigger_stop_time_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                               '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div/' \
                                               'lytx-accordion/div/div[2]/div/div/div/div[5]/span[1]'
    geofence_profile_trigger_idle_time_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                               '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]' \
                                               '/div/lytx-accordion/div/div[2]/div/div/div/div[6]/span[1]'
    geofence_profile_trigger_duration_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                              '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div/' \
                                              'lytx-accordion/div/div[2]/div/div/div/div[7]/span[1]'
    geofence_profile_trigger_geofence_pin_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile/div/div[3]/div[3]/lytx-fleet-tracker/div/div/div[3]/div[1]/div[2]/div/div[3]/div[1]/img'
    geofence_profile_date_range_start_month_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                    '/div/div[3]/div[1]/lx-date-range-filter/div/div[2]' \
                                                    '/lx-date-range-selector/div/div[1]/div[1]/div[2]' \
                                                    '/lx-date-input/div/input[1]'
    geofence_profile_date_range_start_day_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                  '/div/div[3]/div[1]/lx-date-range-filter/div/div[2]' \
                                                  '/lx-date-range-selector/div/div[1]/div[1]/div[2]' \
                                                  '/lx-date-input/div/input[2]'
    geofence_profile_date_range_start_year_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                   '/div/div[3]/div[1]/lx-date-range-filter/div/div[2]' \
                                                   '/lx-date-range-selector/div/div[1]/div[1]/div[2]' \
                                                   '/lx-date-input/div/input[3]'
    geofence_profile_date_range_end_month_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                  '/div/div[3]/div[1]/lx-date-range-filter/div/div[2]' \
                                                  '/lx-date-range-selector/div/div[1]/div[2]/div[2]' \
                                                  '/lx-date-input/div/input[1]'
    geofence_profile_date_range_end_day_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                '/div/div[3]/div[1]/lx-date-range-filter/div/div[2]' \
                                                '/lx-date-range-selector/div/div[1]/div[2]/div[2]' \
                                                '/lx-date-input/div/input[2]'
    geofence_profile_date_range_end_year_xpath = '/html/body/app-root/shell/div/div/div/app-geofence-profile' \
                                                 '/div/div[3]/div[1]/lx-date-range-filter/div/div[2]' \
                                                 '/lx-date-range-selector/div/div[1]/div[2]/div[2]' \
                                                 '/lx-date-input/div/input[3]'

    # Insights_State_Mileage
    state_mileage_title_xpath = '/html/body/app-root/shell/div/div/div/' \
                                'app-state-mileage/div/div[1]/filter-bar/div/div[1]/span[1]'
    group_filter_button_state_mileage_xpath = '/html/body/app-root/shell/div/div/div/' \
                                              'app-state-mileage/div/div[1]/filter-bar' \
                                              '/div/div[2]/div[2]/group-filter/div/span'
    search_by_group_textbox_state_mileage_xpath = '/html/body/ngb-modal-window/div/div/' \
                                                  'group-selector-modal/group-selector/div' \
                                                  '/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_search_button_state_mileage_xpath = '/html/body/ngb-modal-window/div/div/' \
                                               'group-selector-modal/group-selector/div/' \
                                               'div[1]/div[2]/div/lytx-typeahead/div/' \
                                               'ngb-typeahead-window/button'
    done_button_state_mileage_xpath = '/html/body/ngb-modal-window/div/div/' \
                                      'group-selector-modal/group-selector/div/div[3]/button[2]'
    date_filter_state_mileage_xpath = '/html/body/app-root/shell/div/div/div/app-state-mileage' \
                                      '/div/div[1]/filter-bar/div/div[2]/div[2]/' \
                                      'lx-date-range-filter/div/div[1]'
    last_60_days_state_mileage_xpath = '/html/body/app-root/shell/div/div/div/app-state-mileage' \
                                       '/div/div[1]/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                       '/div/div[2]/lx-date-range-selector/div/div[2]/div[1]/div[3]'
    vehicle_column_text_state_mileage_xpath = '/html/body/app-root/shell/div/div/div/app-state-mileage' \
                                              '/div/div[3]/report-table/div/div/cdk-table/cdk-header-row' \
                                              '/cdk-header-cell[1]/span'
    group_column_text_state_mileage_xpath = '/html/body/app-root/shell/div/div/div/app-state-mileage' \
                                            '/div/div[3]/report-table/div/div/cdk-table/cdk-header-row' \
                                            '/cdk-header-cell[2]/span'
    device_serial_column_text_state_mileage_xpath = '/html/body/app-root/shell/div/div/div/app-state-mileage' \
                                                    '/div/div[3]/report-table/div/div/cdk-table/cdk-header-row' \
                                                    '/cdk-header-cell[3]/span'
    state_country_column_text_state_mileage_xpath = '/html/body/app-root/shell/div/div/div/app-state-mileage' \
                                                    '/div/div[3]/report-table/div/div/cdk-table/cdk-header-row' \
                                                    '/cdk-header-cell[4]/span'
    distance_column_text_state_mileage_xpath = '/html/body/app-root/shell/div/div/div/app-state-mileage/div/' \
                                               'div[3]/report-table/div/div/cdk-table/cdk-header-row/' \
                                               'cdk-header-cell[5]/span'
    count_record_state_mileage_xpath = '/html/body/app-root/shell/div/div/div/app-state-mileage/div/div[1]' \
                                       '/filter-bar/div/div[2]/div[1]/div[1]/div/div[1]/div'

    metrics_text_state_mileage_xpath = '/html/body/app-root/shell/div/div/div/app-state-mileage/div/div[2]' \
                                       '/lx-summary-table/div/div[1]/div[1]'
    total_text_state_mileage_xpath = '/html/body/app-root/shell/div/div/div/app-state-mileage/div/div[2]' \
                                     '/lx-summary-table/div/div[1]/div[2]'
    total_distance_text_state_mileage_xpath = '/html/body/app-root/shell/div/div/div/app-state-mileage/div' \
                                              '/div[2]/lx-summary-table/div/div[2]/div[1]'

    trend_header_text_state_mileage_xpath = '/html/body/app-root/shell/div/div/div/app-state-mileage' \
                                            '/div/div[2]/lytx-trends/div/div[1]/div[1]'

    # Insights_Data_Export
    data_export_title_xpath = '/html/body/app-root/shell/div/div/div/app-data-export' \
                              '/div/div[1]/filter-bar/div/div[1]/span[1]'
    filter_by_group_dropdown_xpath = 'html/body/app-root/shell/div/div/div/app-data-export' \
                                     '/div/div[1]/filter-bar/div/div[2]/div[2]/group-filter/div'
    data_export_search_by_vehicle = '//*[@id="vehicleSelector"]/div[1]/input'
    date_dropdown_xpath = '/html/body/app-root/shell/div/div/div/' \
                          'app-data-export/div/div[1]/filter-bar/div/div[2]' \
                          '/div[2]/lx-date-range-filter/div/div[1]/span'
    vehicle_combobox_xpath = '/html/body/app-root/shell/div/div/' \
                             'div/app-data-export/div/div[1]/filter-bar' \
                             '/div/div[2]/div[2]/div/lytx-typeahead/div/input'
    action_label_xpath = '/html/body/app-root/shell/div/div/' \
                         'div/app-data-export/div/div[3]/lx-table/div[2]/div[2]' \
                         '/cdk-table/cdk-header-row/cdk-header-cell[1]/span/span'
    report_type_label_xpath = '/html/body/app-root/shell/div/div/div/app-data-export' \
                              '/div/div[3]/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                              'cdk-header-cell[2]/span/span'
    group_label_xpath = '/html/body/app-root/shell/div/div/div/app-data-export/' \
                        'div/div[3]/lx-table/div[2]/div[2]/cdk-table/' \
                        'cdk-header-row/cdk-header-cell[3]/span/span'
    start_date_label_xpath = '/html/body/app-root/shell/div/div/div/' \
                             'app-data-export/div/div[3]/lx-table/div[2]/div[2]' \
                             '/cdk-table/cdk-header-row/cdk-header-cell[4]/span/span'
    end_date_label_xpath = '/html/body/app-root/shell/div/div/div/' \
                           'app-data-export/div/div[3]/lx-table/div[2]/' \
                           'div[2]/cdk-table/cdk-header-row/cdk-header-cell[5]/span/span'

    vehicle_label_xpath = '/html/body/app-root/shell/div/div/div/' \
                          'app-data-export/div/div[3]/lx-table/div[2]/' \
                          'div[2]/cdk-table/cdk-header-row/cdk-header-cell[6]/span/span'

    requested_date_label_xpath = '/html/body/app-root/shell/div/div/div' \
                                 '/app-data-export/div/div[3]/lx-table/div[2]' \
                                 '/div[2]/cdk-table/cdk-header-row/cdk-header-cell[7]/span/span'

    data_export_30_days_xpath = '/html/body/app-root/shell/div/div/div/app-data-export/div' \
                                '/div[1]/filter-bar/div/div[2]/div[2]/lx-date-range-filter/div' \
                                '/div[2]/lx-date-range-selector/div/div[2]/div[1]/div[2]'
    data_export_select_date_xpath = '/html/body/app-root/shell/div/div/div/app-data-export' \
                                    '/div/div[1]/filter-bar/div/div[2]/div[2]' \
                                    '/lx-date-range-filter/div/div[1]'
    data_export_request_data_id = '//*[@id="submitButton"]'
    data_export_request_status_xpath = '/html/body/app-root/shell/div/div/div/app-data-export' \
                                       '/div/div[3]/lx-table/div[2]/div[2]/cdk-table/cdk-row' \
                                       '/cdk-cell[1]/span[2]/div/span'
    data_export_request_type_xpath = '/html/body/app-root/shell/div/div/div/app-data-export' \
                                     '/div/div[3]/lx-table/div[2]/div[2]/cdk-table/cdk-row' \
                                     '/cdk-cell[2]/span[2]'
    data_export_status_xpath = '/html/body/app-root/shell/div/div/div/app-data-export/div' \
                               '/div[3]/lx-table/div[2]/div[2]/cdk-table/cdk-row' \
                               '/cdk-cell[1]/span[2]/div/span'
    data_export_download_xpath = '/html/body/app-root/shell/div/div/div/app-data-export/div' \
                                 '/div[3]/lx-table/div[2]/div[2]/cdk-table/cdk-row' \
                                 '/cdk-cell[1]/span[2]/div/span/div'
    data_export_cancel_request_class = 'lx-close-x'
    data_export_delete_request_class = 'lx-trashcan'
    data_export_confirm_delete_request_id = 'modalShellPrimaryButton'

    # Actions when the toggle ENABLE_FLEET_TRACKING_DASHBOARD set as true
    # map_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[2]'
    # maintenance_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[3]'

    # preventative_maintenance_xpath = '/html/body/app-root/shell/div/' \
    #                                 'div/navigation/div[1]/div[3]/div[2]/div[2]/div[1]/div'

    # dtc_xpath = '/html/body/app-root/shell/div/div/' \
    #            'navigation/div[1]/div[3]/div[2]/div[2]/div[2]/div'

    # insights_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[4]'
    # fleet_operations_xpath = '/html/body/app-root/shell/div' \
    #                         '/div/navigation/div[1]/div[4]/div[2]/div[2]/div[1]/div'
    # fleet_data_xpath = '/html/body/app-root/shell/div/div/navigation' \
    #                   '/div[1]/div[4]/div[2]/div[2]/div[2]/div'
    # geofences_xpath = '/html/body/app-root/shell/div/div/' \
    #                  'navigation/div[1]/div[4]/div[2]/div[2]/div[4]/div'

    # state_mileage_xpath = '/html/body/app-root/shell/div/div/' \
    #                      'navigation/div[1]/div[4]/div[2]/div[2]/div[5]/div'

    # data_export_xpath = '/html/body/app-root/shell/div/div/' \
    #                    'navigation/div[1]/div[4]/div[2]/div[2]/div[6]/div'

    # Actions when the toggle ENABLE_FLEET_TRACKING_DASHBOARD set as false
    map_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[1]'
    maintenance_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[2]'

    preventative_maintenance_xpath = '/html/body/app-root/shell/div/' \
                                     'div/navigation/div[1]/div[2]/div[2]/div[2]/div[1]/div'

    dtc_xpath = '/html/body/app-root/shell/div/div/' \
                'navigation/div[1]/div[2]/div[2]/div[2]/div[2]/div'

    insights_xpath = '(.//*[text()="Insights"])[1]'
    insights_new_ui_xpath = '(.//*[text()=" Insights "])[1]'
    insights_dycom_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[3]'
    fleet_operations_xpath = '(.//*[text()=" Fleet Operations "])[1]'
    fleet_operations_new_ui_xpath = '(//*[text()=" Fleet Operations"])[1]'
    fleet_data_xpath = '//*[text()=" Fleet Data "]'
    fleet_data_new_ui_xpath = '//*[text()=" Fleet Data"]'
    equipment_status_xpath = '(//*[text()=" Equipment Status "])[1]'
    equipment_status_new_ui_xpath = '(//*[text()=" Equipment Status"])[1]'
    geofences_xpath = '(//*[contains(text(),"Geofences")])[1]'
    state_mileage_xpath = '(//*[text()=" State Mileage "])[1]'
    state_mileage_new_ui_xpath = '(//*[text()=" State Mileage"])[1]'
    data_export_xpath = '(//*[text()=" Data Export "])[1]'
    data_export_new_ui_xpath = '(//*[text()=" Data Export"])[1]'
    reset_button_xpath = '//*[@class="lx-btn lx-btn-text filter-header-bar__filters--reset"]'
    equipment_status_record_count_xpath = '//*[@data-test-id="filter-headerBar-countValue"]'

    # Insights_Fleet Data Page(need to set Enable Fuel Management UI(GroupOptionId=42) as true)
    average_text_xpath = '/html/body/app-root/shell/div/div/div/' \
                         'app-fleet-data/div/div[2]/lx-summary-table' \
                         '/div/div[1]/div[2]/span'
    total_text_xpath = '/html/body/app-root/shell/div/div/div/' \
                       'app-fleet-data/div/div[2]/lx-summary-table/' \
                       'div/div[1]/div[3]/span'
    metric_detail_xpath = '/html/body/app-root/shell/div/div/div/' \
                          'app-fleet-data/div/div[2]/lx-summary-table'
    distance_xpath = '/html/body/app-root/shell/div/div/div' \
                     '/app-fleet-data/div/div[2]/lx-summary-table' \
                     '/div/div[2]/div[1]/div'
    graph_header_title_text_xpath = '/html/body/app-root/shell/div/div/div' \
                                    '/app-fleet-data/div/div[2]/' \
                                    'lytx-trends/div/div[1]/div[1]'
    groups_tab_table_xpath = '/html/body/app-root/shell/div/div/div/' \
                             'app-fleet-data/div/div[3]/button[1]'
    vehicles_tab_table_xpath = '/html/body/app-root/shell/div/div/div/' \
                               'app-fleet-data/div/div[3]/button[2]'
    groups_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                        '/div/div[4]/report-table/div/div/cdk-table/' \
                        'cdk-header-row/cdk-header-cell[1]/span/span/span[1]'
    distance_text_xpath = '/html/body/app-root/shell/div/div/div/' \
                          'app-fleet-data/div/div[4]/report-table/div/div/' \
                          'cdk-table/cdk-header-row/cdk-header-cell[2]/div/div[1]'
    engine_hours_text_xpath = '/html/body/app-root/shell/div/div/div/' \
                              'app-fleet-data/div/div[4]/report-table/div/div/' \
                              'cdk-table/cdk-header-row/cdk-header-cell[3]/div/div[1]'
    driving_hours_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                               '/div/div[4]/report-table/div/div/cdk-table/' \
                               'cdk-header-row/cdk-header-cell[4]/div/div[1]'
    idle_time_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                           '/div/div[4]/report-table/div/div/cdk-table/' \
                           'cdk-header-row/cdk-header-cell[5]/div/div[1]'
    idle_pto_time_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                               '/div/div[4]/report-table/div/div/cdk-table/' \
                               'cdk-header-row/cdk-header-cell[6]/div/div[1]'
    fuel_consumed_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                               '/div/div[4]/report-table/div/div/cdk-table/' \
                               'cdk-header-row/cdk-header-cell[7]/div/div[1]'
    driving_fuel_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                              '/div/div[4]/report-table/div/div/cdk-table/' \
                              'cdk-header-row/cdk-header-cell[8]/div/div[1]'
    idling_fuel_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                             '/div/div[4]/report-table/div/div/cdk-table/' \
                             'cdk-header-row/cdk-header-cell[9]/div/div[1]'
    pto_idling_fuel_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                                 '/div/div[4]/report-table/div/div/cdk-table/' \
                                 'cdk-header-row/cdk-header-cell[10]/div/div[1]'
    fuel_economy_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data/div' \
                              '/div[4]/report-table/div/div/cdk-table/' \
                              'cdk-header-row/cdk-header-cell[11]/div/div[1]'
    driving_fuel_economy_text_xpath = '/html/body/app-root/shell/div/div/div/a' \
                                      'pp-fleet-data/div/div[4]/report-table/div/div/' \
                                      'cdk-table/cdk-header-row/cdk-header-cell[12]/div/div[1]'
    vehicle_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data/' \
                         'div/div[4]/report-table/div/div/cdk-table/cdk-header-row/' \
                         'cdk-header-cell[1]/span/span/span[1]'
    vehicle_odometer_reading_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                                          '/div/div[4]/report-table/div/div/cdk-table/' \
                                          'cdk-header-row/cdk-header-cell[2]/div/div[1]'
    vehicle_distance_text_xpath = '/html/body/app-root/shell/div/div/div/' \
                                  'app-fleet-data/div/div[4]/report-table/' \
                                  'div/div/cdk-table/cdk-header-row/cdk-header-' \
                                  'cell[3]/div/div[1]'
    vehicle_engine_hours_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                                      '/div/div[4]/report-table/div/div/cdk-table/' \
                                      'cdk-header-row/cdk-header-cell[4]/div/div[1]'
    vehicle_driving_hours_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data/' \
                                       'div/div[4]/report-table/div/div/cdk-table/' \
                                       'cdk-header-row/cdk-header-cell[5]/div/div[1]'
    vehicle_idle_time_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                                   '/div/div[4]/report-table/div/div/cdk-table/' \
                                   'cdk-header-row/cdk-header-cell[6]/div/div[1]'
    vehicle_idle_pto_time_text_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                                       '/div/div[4]/report-table/div/div/cdk-table/' \
                                       'cdk-header-row/cdk-header-cell[7]/div/div[1]'
    vehicle_fuel_consumed_text_xpath = '/html/body/app-root/shell/div/div/div/' \
                                       'app-fleet-data/div/div[4]/report-table/div/div/' \
                                       'cdk-table/cdk-header-row/cdk-header-cell[8]/div/div[1]'
    vehicle_driving_fuel_text_xpath = '/html/body/app-root/shell/div/div/div/' \
                                      'app-fleet-data/div/div[4]/report-table/div/div/' \
                                      'cdk-table/cdk-header-row/cdk-header-cell[9]/div/div[1]'
    vehicle_idling_fuel_text_xpath = '/html/body/app-root/shell/div/div/div/' \
                                     'app-fleet-data/div/div[4]/report-table/div/div/' \
                                     'cdk-table/cdk-header-row/cdk-header-cell[10]/div/div[1]'
    vehicle_pto_idling_fuel_text_xpath = '/html/body/app-root/shell/div/div/div/' \
                                         'app-fleet-data/div/div[4]/report-table/div/div/' \
                                         'cdk-table/cdk-header-row/cdk-header-cell[11]/div/div[1]'
    vehicle_fuel_economy_text_xpath = '/html/body/app-root/shell/div/div/div/' \
                                      'app-fleet-data/div/div[4]/report-table/div/div/' \
                                      'cdk-table/cdk-header-row/cdk-header-cell[12]/div/div[1]'
    vehicle_driving_fuel_economy_text_xpath = '/html/body/app-root/shell/div/div/div/' \
                                              'app-fleet-data/div/div[4]/report-table/div/div/' \
                                              'cdk-table/cdk-header-row/cdk-header-cell[13]/' \
                                              'div/div[1]'
    # Filter Group/Date
    fleet_data_group_filter_button_xpath = '/html/body/app-root/shell/div/div/div/' \
                                           'app-fleet-data/div/div[1]/filter-bar/div/' \
                                           'div[2]/div[2]/group-filter/div/span'
    fleet_data_search_by_group_textbox_xpath = '/html/body/ngb-modal-window/' \
                                               'div/div/group-selector-modal/group-selector' \
                                               '/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    fleet_data_select_search_button_xpath = '/html/body/ngb-modal-window/div/div/' \
                                            'group-selector-modal/group-selector' \
                                            '/div/div[1]/div[2]/div/lytx-typeahead/div' \
                                            '/ngb-typeahead-window/button[1]'
    fleet_data_done_button_xpath = '/html/body/ngb-modal-window/div/div/' \
                                   'group-selector-modal/group-selector' \
                                   '/div/div[3]/button[2]/span'
    fleet_data_date_filter_xpath = '/html/body/app-root/shell/div/div/div/' \
                                   'app-fleet-data/div/div[1]/filter-bar/' \
                                   'div/div[2]/div[2]/lx-date-range-filter/div/div[1]'
    fleet_data_date_range_start_month_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                                              '/div/div[1]/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                              '/div/div[2]/lx-date-range-selector/div/div[1]/div[1]/div[2]' \
                                              '/lx-date-input/div/input[1]'
    fleet_data_date_range_start_day_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                                            '/div/div[1]/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                            '/div/div[2]/lx-date-range-selector/div/div[1]/div[1]/div[2]' \
                                            '/lx-date-input/div/input[2]'
    fleet_data_date_range_start_year_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                                             '/div/div[1]/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                             '/div/div[2]/lx-date-range-selector/div/div[1]/div[1]/div[2]' \
                                             '/lx-date-input/div/input[3]'
    fleet_data_date_range_end_month_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                                            '/div/div[1]/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                            '/div/div[2]/lx-date-range-selector/div/div[1]/div[2]/div[2]' \
                                            '/lx-date-input/div/input[1]'
    fleet_data_date_range_end_day_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                                          '/div/div[1]/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                          '/div/div[2]/lx-date-range-selector/div/div[1]/div[2]/div[2]' \
                                          '/lx-date-input/div/input[2]'
    fleet_data_date_range_end_year_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-data' \
                                           '/div/div[1]/filter-bar/div/div[2]/div[2]/lx-date-range-filter' \
                                           '/div/div[2]/lx-date-range-selector/div/div[1]/div[2]/div[2]' \
                                           '/lx-date-input/div/input[3]'

    # Vehicle Profile Page
    # not sure why, but the xpath of vehicle search box in fleet operation page changes back and force
    # vehicle_search_xpath = '/html/body/app-root/shell/div/div/div/app-fleet-operations' \
    #                        '/div/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[2]/div' \
    #                        '/app-fleet-operations-vehicles/div/div[1]/div' \
    #                        '/lytx-typeahead/div/input'
    vehicle_search_xpath = '//input[@placeholder="Search Vehicles"]'

    vehicle_select_xpath = '//*[text()="Truck 692"]'
    expand_metadata_icon_xpath = '//*[@class="expand-icon__background"]'
    expand_vehicle_summary_icon_xpath = '/html/body/app-root/shell/div/div/div' \
                                        '/app-vehicle-profile/div/div[3]/div[2]' \
                                        '/lx-metadata-bar/div/div[1]/div/i'
    vehicle_profile_title_xpath = '/html/body/app-root/shell/div/div/div' \
                                  '/app-vehicle-profile/div/div[1]'

    date_filter_vehicle_profile_xpath = '/html/body/app-root/shell/div/div/div' \
                                        '/app-vehicle-profile/div/div[3]/div[1]' \
                                        '/lx-date-range-filter/div/div[1]'
    vehicle_profile_date_range_start_month_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                                                   '/div/div[3]/div[1]/lx-date-range-filter/div/div[2]' \
                                                   '/lx-date-range-selector/div/div[1]/div[1]/div[2]' \
                                                   '/lx-date-input/div/input[1]'
    vehicle_profile_date_range_start_day_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                                                 '/div/div[3]/div[1]/lx-date-range-filter/div/div[2]' \
                                                 '/lx-date-range-selector/div/div[1]/div[1]/div[2]' \
                                                 '/lx-date-input/div/input[2]'
    vehicle_profile_date_range_start_year_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                                                  '/div/div[3]/div[1]/lx-date-range-filter/div/div[2]' \
                                                  '/lx-date-range-selector/div/div[1]/div[1]/div[2]' \
                                                  '/lx-date-input/div/input[3]'
    vehicle_profile_date_range_end_month_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                                                 '/div/div[3]/div[1]/lx-date-range-filter/div/div[2]' \
                                                 '/lx-date-range-selector/div/div[1]/div[2]/div[2]' \
                                                 '/lx-date-input/div/input[1]'
    vehicle_profile_date_range_end_day_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                                               '/div/div[3]/div[1]/lx-date-range-filter/div/div[2]' \
                                               '/lx-date-range-selector/div/div[1]/div[2]/div[2]' \
                                               '/lx-date-input/div/input[2]'
    vehicle_profile_date_range_end_year_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                                                '/div/div[3]/div[1]/lx-date-range-filter/div/div[2]' \
                                                '/lx-date-range-selector/div/div[1]/div[2]/div[2]' \
                                                '/lx-date-input/div/input[3]'
    trip_count_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile/div/div[3]' \
                       '/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[1]'
    idle_count_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile/div/div[3]' \
                       '/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[1]'
    trip_tab_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                     '/div/div[3]/lytx-tabs/div/div[1]'
    idle_tab_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                     '/div/div[3]/lytx-tabs/div/div[2]'

    date_trip_detail_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                             '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div' \
                             '/lytx-accordion/div/div[2]/div'
    date_idle_detail_xpath = '//*[@id="itemHeader"]'
    vehicle_profile_trip_info_xpath = '//*[@class="data-item-title"]'
    vehicle_profile_trip_num_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                                     '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div' \
                                     '/lytx-accordion/div/div[2]/div/div/div/div[1]/span[1]'
    vehicle_profile_trip_driver_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                                        '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div' \
                                        '/lytx-accordion/div/div[2]/div/div/div/div[2]/span[1]'
    vehicle_profile_trip_duration_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                                          '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div' \
                                          '/lytx-accordion/div/div[2]/div/div/div/div[3]/span[1]'
    vehicle_profile_trip_distance_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                                          '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div' \
                                          '/lytx-accordion/div/div[2]/div/div/div/div[4]/span[1]'
    vehicle_profile_trip_speed_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                                       '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div' \
                                       '/lytx-accordion/div/div[2]/div/div/div/div[5]/span[1]'
    vehicle_profile_trip_stop_duration_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                                               '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div' \
                                               '/lytx-accordion/div/div[2]/div/div/div/div[6]/span[1]'
    vehicle_profile_idle_info_xpath = '//*[@class="data-item-title"]'
    vehicle_profile_idle_num_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                                     '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div' \
                                     '/lytx-accordion/div/div[2]/div/div/div/div[1]/span[1]'
    vehicle_profile_idle_driver_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                                        '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div' \
                                        '/lytx-accordion/div/div[2]/div/div/div/div[2]/span[1]'
    vehicle_profile_idle_duration_xpath = '(//*[text()="IDLE DURATION"])[1]'
    vehicle_profile_idle_occur_time_xpath = '/html/body/app-root/shell/div/div/div' \
                                            '/app-vehicle-profile/div/div[3]/div[3]/lytx-drawer' \
                                            '/div/div/div[2]/div/lytx-accordion/div/div[2]' \
                                            '/div/div/div/ul/li/p[2]'
    vehicle_profile_idle_address_xpath = '/html/body/app-root/shell/div/div/div' \
                                         '/app-vehicle-profile/div/div[3]/div[3]/lytx-drawer' \
                                         '/div/div/div[2]/div/lytx-accordion/div/div[2]' \
                                         '/div/div/div/ul/li/p[3]'

    # Vehicle Profile Metadata
    empty_list_message_xpath = '/html/body/app-root/shell/div/div/div/app-vehicle-profile' \
                               '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div' \
                               '/lytx-accordion/div/div[2]/div'
    vehicle_profile_vehicle_name_xpath = '/html/body/app-root/shell/div/div/div' \
                                         '/app-vehicle-profile/div/div[2]/lx-metadata-bar' \
                                         '/div/div[2]/div[1]/div[1]'
    vehicle_profile_group_xpath = '/html/body/app-root/shell/div/div/div' \
                                  '/app-vehicle-profile/div/div[2]/lx-metadata-bar' \
                                  '/div/div[2]/div[2]/div[1]'
    vehicle_profile_driver_xpath = '//*[text()="DRIVER"]'
    vehicle_profile_device_xpath = '/html/body/app-root/shell/div/div/div' \
                                   '/app-vehicle-profile/div/div[2]/lx-metadata-bar' \
                                   '/div/div[2]/div[4]/div[1]'
    vehicle_profile_status_xpath = '/html/body/app-root/shell/div/div/div' \
                                   '/app-vehicle-profile/div/div[2]/lx-metadata-bar' \
                                   '/div/div[2]/div[5]/div[1]'
    vehicle_profile_make_xpath = '/html/body/app-root/shell/div/div/div' \
                                 '/app-vehicle-profile/div/div[2]/lx-metadata-bar' \
                                 '/div/div[2]/div[6]/div[1]'
    vehicle_profile_license_xpath = '/html/body/app-root/shell/div/div/div' \
                                    '/app-vehicle-profile/div/div[2]/lx-metadata-bar' \
                                    '/div/div[2]/div[7]/div[1]'
    vehicle_profile_hibernation_xpath = '/html/body/app-root/shell/div/div/div' \
                                        '/app-vehicle-profile/div/div[2]/lx-metadata-bar' \
                                        '/div/div[2]/div[8]/div[1]'
    vehicle_profile_vin_xpath = '/html/body/app-root/shell/div/div/div' \
                                '/app-vehicle-profile/div/div[2]/lx-metadata-bar' \
                                '/div/div[2]/div[9]/div[1]'
    vehicle_profile_vehicle_type_xpath = '/html/body/app-root/shell/div/div/div' \
                                         '/app-vehicle-profile/div/div[2]/lx-metadata-bar' \
                                         '/div/div[2]/div[10]/div[1]'
    vehicle_profile_seat_belt_xpath = '/html/body/app-root/shell/div/div/div' \
                                      '/app-vehicle-profile/div/div[2]/lx-metadata-bar' \
                                      '/div/div[2]/div[11]/div[1]'

    # Vehicle Profile Summary
    vehicle_profile_route_time_xpath = '/html/body/app-root/shell/div/div/div' \
                                       '/app-vehicle-profile/div/div[3]/div[2]/lx-metadata-bar' \
                                       '/div/div[2]/div[1]/div[1]'
    vehicle_profile_route_time_value_xpath = '/html/body/app-root/shell/div/div/div' \
                                             '/app-vehicle-profile/div/div[3]/div[2]' \
                                             '/lx-metadata-bar/div/div[2]/div[1]/div[2]'
    vehicle_profile_distance_xpath = '/html/body/app-root/shell/div/div/div' \
                                     '/app-vehicle-profile/div/div[3]/div[2]' \
                                     '/lx-metadata-bar/div/div[2]/div[2]/div[1]'
    vehicle_profile_trips_xpath = '/html/body/app-root/shell/div/div/div' \
                                  '/app-vehicle-profile/div/div[3]/div[2]/lx-metadata-bar' \
                                  '/div/div[2]/div[3]/div[1]'
    vehicle_profile_stops_xpath = '/html/body/app-root/shell/div/div/div' \
                                  '/app-vehicle-profile/div/div[3]/div[2]/lx-metadata-bar' \
                                  '/div/div[2]/div[4]/div[1]'
    vehicle_profile_stop_time_xpath = '/html/body/app-root/shell/div/div/div' \
                                      '/app-vehicle-profile/div/div[3]/div[2]/lx-metadata-bar' \
                                      '/div/div[2]/div[5]/div[1]'
    vehicle_profile_driving_time_xpath = '/html/body/app-root/shell/div/div/div' \
                                         '/app-vehicle-profile/div/div[3]/div[2]/lx-metadata-bar' \
                                         '/div/div[2]/div[6]/div[1]'
    vehicle_profile_engine_hours_xpath = '/html/body/app-root/shell/div/div/div' \
                                         '/app-vehicle-profile/div/div[3]/div[2]/lx-metadata-bar' \
                                         '/div/div[2]/div[7]/div[1]'
    vehicle_profile_idle_violation_xpath = '/html/body/app-root/shell/div/div/div' \
                                           '/app-vehicle-profile/div/div[3]/div[2]' \
                                           '/lx-metadata-bar/div/div[2]/div[8]/div[1]'
    vehicle_profile_idle_duration_xpath = '/html/body/app-root/shell/div/div/div' \
                                          '/app-vehicle-profile/div/div[3]/div[2]/lx-metadata-bar' \
                                          '/div/div[2]/div[9]/div[1]'
    vehicle_profile_speed_violation_xpath = '/html/body/app-root/shell/div/div/div' \
                                            '/app-vehicle-profile/div/div[3]/div[2]' \
                                            '/lx-metadata-bar/div/div[2]/div[10]/div[1]'
    vehicle_profile_speed_duration_xpath = '/html/body/app-root/shell/div/div/div' \
                                           '/app-vehicle-profile/div/div[3]/div[2]' \
                                           '/lx-metadata-bar/div/div[2]/div[11]/div[1]'

    # Insights - Equipment Status
    equipment_status_title_xpath = '/html/body/app-root/shell/div/div/div/' \
                                   'app-asset-status/div/div/filter-bar/div/div[1]/span[1]'
    equipment_column_title_id = 'sortableContainerassetName'
    equipment_group_column_id = 'sortableContainergroupName'
    equipment_device_column_id = 'sortableContainerserialNumber'
    equipment_last_location_column_xpath = '/html/body/app-root/shell/div/div/div/' \
                                           'app-asset-status/div/lx-table/div[2]/div[2]/' \
                                           'cdk-table/cdk-header-row/cdk-header-cell[4]/span/span'
    equipment_last_connected_column_id = 'sortableContainerlastConnectedDate'
    equipment_last_movement_column_id = 'sortableContainerlastMovementDate'
    equipment_stationary_duration_column_xpath = '/html/body/app-root/shell/div/div/div/' \
                                                 'app-asset-status/div/lx-table/div[2]/div[2]' \
                                                 '/cdk-table/cdk-header-row/cdk-header-cell[7]' \
                                                 '/span/span/span[1]'
    equipment_battery_level_column_id = 'sortableContainerbattery'
    group_filter_equipment_status_xpath = '/html/body/app-root/shell/div/div/div/app-asset-status' \
                                          '/div/div/filter-bar/div/div[2]/div[2]/group-filter/div'
    search_by_group_textbox_equipment_status_xpath = '/html/body/ngb-modal-window/div/div' \
                                                     '/group-selector-modal/group-selector/div' \
                                                     '/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_search_button_equipment_status_xpath = '/html/body/ngb-modal-window/div/div/' \
                                                  'group-selector-modal/group-selector' \
                                                  '/div/div[1]/div[2]/div/lytx-typeahead/div' \
                                                  '/ngb-typeahead-window/button[1]'
    done_button_equipment_status_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal' \
                                         '/group-selector/div/div[3]/button[2]'
    equipment_status_search_assert_type_xpath = '//*[@id="assetSearchType"]/div/span/span'
    equipment_status_asset_type_equipment_xpath = '//*[@id="assetSearchType"]/div/div/ul/li[1]'
    equipment_status_asset_type_device_xpath = '//*[@id="assetSearchType"]/div/div/ul/li[2]'
    search_criteria_equipment_status_xpath = '//*[@id="searchInput"]'

    # maint. PM
    maint_manage_services_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div' \
                                  '/div[2]/lytx-tab-views/div/div[1]/button[3]'

    manage_service_count_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]' \
                                 '/lytx-tab-views/div/div[2]/lytx-tab-view[3]/div' \
                                 '/service-management-new/div[1]/lx-filter-bar/div/div' \
                                 '/div[1]/div[1]/div/div[1]/div'
    maint_create_service_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]' \
                                 '/lytx-tab-views/div/div[2]/lytx-tab-view[3]/div' \
                                 '/service-management-new/div[1]/button'
    maint_service_name_xpath = '//*[@id="service-name-input"]/lytx-input/div/div[2]/input'

    # Note: this id changes when different pre-steps are performed
    maint_service_check_mile_xpath = '/html/body/app-root/shell/div/div/div/app-service-form-new' \
                                     '/div/form/div[1]/div[3]/div[1]/div[2]/div[1]/div/mat-checkbox'
    maint_service_mile_due_xpath = '//*[@id="service-interval-input"]/lytx-number-input/div/div[2]/input'
    maint_service_mile_due_soon_xpath = '//*[@id="due-soon-input"]/lytx-number-input/div/div[2]/input'
    maint_service_save_xpath = '//*[@id="submitButton"]'
    maint_service_list_service_name_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div' \
                                            '/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[3]/div' \
                                            '/service-management-new/div[2]/lx-table/div[2]/div[2]' \
                                            '/cdk-table/cdk-row[1]/cdk-cell[1]/span[2]/div[1]/span'

    # Driver Profile page
    driver_profile_date_range_start_month_xpath = '(//*[@data-test-id="dateInput-month-field"])[1]'
    driver_profile_date_range_start_day_xpath = '(//*[@data-test-id="dateInput-day-field"])[1]'
    driver_profile_date_range_start_year_xpath = '(//*[@data-test-id="dateInput-year-field"])[1]'
    driver_profile_date_range_end_month_xpath = '(//*[@data-test-id="dateInput-month-field"])[2]'
    driver_profile_date_range_end_day_xpath = '(//*[@data-test-id="dateInput-day-field"])[2]'
    driver_profile_date_range_end_year_xpath = '(//*[@data-test-id="dateInput-year-field"])[2]'
    driver_profile_title_text_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[1]'
    driver_name_text_driver_profile_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div' \
                                            '/div[2]/lx-metadata-bar/div/div[1]'
    employee_id_text_driver_profile_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/' \
                                            'div/div[2]/lx-metadata-bar/div/div[2]/div[1]/div[1]'
    group_text_driver_profile_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div' \
                                      '/div[2]/lx-metadata-bar/div/div[2]/div[2]/div[1]'
    vehicle_name_text_driver_profile_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile' \
                                             '/div/div[2]/lx-metadata-bar/div/div[2]/div[3]/div[1]'
    email_text_driver_profile_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/' \
                                      'div[2]/lx-metadata-bar/div/div[2]/div[4]/div[1]'
    expand_driver_summary_icon_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div' \
                                       '/div[3]/div[2]/lx-metadata-bar/div/div[1]/div'
    daily_avg_text_driver_profile_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div' \
                                          '/div[3]/div[1]/div/button[1]'
    total_text_driver_profile_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div' \
                                      '/div[3]/div[1]/div/button[2]'
    route_time_driver_profile_xpath = '//*[text()="ROUTE TIME"]'
    distance_driver_profile_xpath = '//*[text()="DISTANCE"]'
    trips_driver_profile_xpath = '//*[text()="TRIPS"]'
    stops_driver_profile_xpath = '//*[text()="STOPS"]'
    stop_time_driver_profile_xpath = '//*[text()="STOP TIME"]'
    driving_time_driver_profile_xpath = '//*[text()="DRIVING TIME"]'
    engine_hours_driver_profile_xpath = '//*[text()="ENGINE HOURS"]'
    idle_violations_driver_profile_xpath = '//*[text()="IDLE OVERAGE"]'
    idle_duration_driver_profile_xpath = '//*[text()="IDLE VIOLATIONS DURATION"]'
    speed_violation_driver_profile_xpath = '//div[contains(@class,"metadata-bar__label") and normalize-space(text())="SPEED VIOLATIONS"]'
    speeding_duration_driver_profile_xpath = '//*[text()="SPEED VIOLATIONS DURATION"]'
    open_trip_driver_profile_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]' \
                                     '/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[2]/button'
    trip1_label_driver_profile_trip_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div' \
                                            '/div[3]/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion' \
                                            '/div/div[2]/div/div/div/div[1]/span[1]'
    start_time_driver_profile_trip_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]' \
                                           '/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[2]' \
                                           '/div/div/div/ul/li[1]/p[2]'
    end_time_driver_profile_trip_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]' \
                                         '/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[2]/div/' \
                                         'div/div/ul/li[2]/p[2]'
    start_address_driver_profile_trip_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div' \
                                              '/div[3]/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion' \
                                              '/div/div[2]/div/div/div/ul/li[1]/p[3]'
    end_address_driver_profile_trip_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div' \
                                            '/div[3]/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion/' \
                                            'div/div[2]/div/div/div/ul/li[2]/p[3]'
    vehicle_driver_profile_trip_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/' \
                                        'div[3]/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion/' \
                                        'div/div[2]/div/div/div/div[2]/span[1]'
    trip_duration_driver_profile_trip_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile' \
                                              '/div/div[3]/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion' \
                                              '/div/div[2]/div/div/div/div[3]/span[1]'
    distance_driver_profile_trip_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]' \
                                         '/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[2]' \
                                         '/div/div/div/div[4]/span[1]'
    max_speed_driver_profile_trip_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]' \
                                          '/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[2]/' \
                                          'div/div/div/div[5]/span[1]'
    stop_duration_driver_profile_trip_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div' \
                                              '/div[3]/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion/' \
                                              'div/div[2]/div/div/div/div[6]/span[1]'

    idle_tab_driver_profile_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]/lytx-tabs/div/div[2]'
    open_idle_driver_profile_idle_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]' \
                                          '/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[2]/button'
    idle1_text_driver_profile_idle_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]' \
                                           '/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[2]/' \
                                           'div/div[1]/div/div[1]/span[1]'
    address_driver_profile_idle_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]/div[3]' \
                                        '/lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[2]/div/div/div/ul/li/p[3]'
    time_driver_profile_idle_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]/div[3]/' \
                                     'lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[2]/div/div/div/ul/li/p[2]'
    vehicle_text_driver_profile_idle_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]' \
                                             '/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[2]/' \
                                             'div/div/div/div[2]/span[1]'
    idle_duration_driver_profile_idle_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]' \
                                              '/div[3]/lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[2]' \
                                              '/div/div/div/div[3]/span[1]'
    date_filter_driver_profile_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]/div[1]' \
                                       '/lx-date-range-filter/div/div[1]'
    last_90_days_driver_profile_xpath = '//*[text()=" Last 90 Days "]'
    apply_button_driver_profile_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]/div[1]' \
                                        '/lx-date-range-filter/div/div[2]/lx-date-range-selector/div/div[2]/div[2]/div/div[2]/button[2]'
    idles_count_driver_profile_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]/div[3]' \
                                       '/lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[1]'
    trips_count_driver_profile_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]/div[3]' \
                                       '/lytx-drawer/div/div/div[2]/div/lytx-accordion/div/div[1]'
    trip_tab_driver_profile_xpath = '/html/body/app-root/shell/div/div/div/app-driver-profile/div/div[3]/lytx-tabs' \
                                    '/div/div[1]'

    fleet_operation_date_range_start_month_xpath = '(//*[@data-test-id="dateInput-month-field"])[1]'
    fleet_operation_date_range_start_day_xpath = '(//*[@data-test-id="dateInput-day-field"])[1]'
    fleet_operation_date_range_start_year_xpath = '(//*[@data-test-id="dateInput-year-field"])[1]'
    fleet_operation_date_range_end_month_xpath = '(//*[@data-test-id="dateInput-month-field"])[2]'
    fleet_operation_date_range_end_day_xpath = '(//*[@data-test-id="dateInput-day-field"])[2]'
    fleet_operation_date_range_end_year_xpath = '(//*[@data-test-id="dateInput-year-field"])[2]'

    drivers_tab_date_range_start_month_xpath = '(//*[@data-test-id="dateInput-month-field"])[1]'
    drivers_tab_date_range_start_day_xpath = '(//*[@data-test-id="dateInput-day-field"])[1]'
    drivers_tab_date_range_start_year_xpath = '(//*[@data-test-id="dateInput-year-field"])[1]'
    drivers_tab_date_range_end_month_xpath = '(//*[@data-test-id="dateInput-month-field"])[2]'
    drivers_tab_date_range_end_day_xpath = '(//*[@data-test-id="dateInput-day-field"])[2]'
    drivers_tab_date_range_end_year_xpath = '(//*[@data-test-id="dateInput-year-field"])[2]'
    vehicles_tab_date_range_start_month_xpath = '(//*[@data-test-id="dateInput-month-field"])[1]'
    vehicles_tab_date_range_start_day_xpath = '(//*[@data-test-id="dateInput-day-field"])[1]'
    vehicles_tab_date_range_start_year_xpath = '(//*[@data-test-id="dateInput-year-field"])[1]'
    vehicles_tab_date_range_end_month_xpath = '(//*[@data-test-id="dateInput-month-field"])[2]'
    vehicles_tab_date_range_end_day_xpath = '(//*[@data-test-id="dateInput-day-field"])[2]'
    vehicles_tab_date_range_end_year_xpath = '(//*[@data-test-id="dateInput-year-field"])[2]'
    vehicle_suggestion_xpath = '//*[text()="{0}"]'
    select_search_filter_xpath = '//*[contains(text(), "{0}")]'
    device_column_xpath = '//cdk-row'
    device_row_xpath = '//cdk-cell[3]/span[2]'
    equipment_data_loaded_xpath = '(//*[@class="cdk-row lytx-table-row"])[1]'





