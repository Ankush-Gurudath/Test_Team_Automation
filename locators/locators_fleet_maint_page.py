class LocatorsFleetMaint:
    fleet_tracking_title_id = 'fleetTrackingText'
    apply_button_id = 'btn-apply'
    preventative_maintenance_title_xpath = '/html/body/app-root/shell/div/' \
                                           'div/div/app-maintenance/div/div[1]'

    # Maintenance_Preventative maintenance_upcoming service
    pm_upcoming_service_xpath = '//*[text()="Upcoming Services"]'
    pm_upcoming_service_search_vehicle_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance' \
                                               '/div/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[1]' \
                                               '/div/services-due/div[1]/lx-filter-bar/div/div/div[2]' \
                                               '/lytx-typeahead/div/input'
    pm_upcoming_service_select_vehicle_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]' \
                                               '/lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/services-due' \
                                               '/div[1]/lx-filter-bar/div/div/div[2]/lytx-typeahead/div' \
                                               '/ngb-typeahead-window/button'
    pm_upcoming_service_count_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]' \
                                      '/lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/services-due' \
                                      '/div[1]/lx-filter-bar/div/div/div[1]/div[1]/div/div[1]/div'
    pm_upcoming_service_1st_vehicle_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance' \
                                            '/div/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[1]' \
                                            '/div/services-due/div[2]/lx-table/div[2]/div[2]/cdk-table' \
                                            '/cdk-row/cdk-cell[1]/span[2]/span'
    pm_upcoming_service_1st_group_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance' \
                                          '/div/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[1]/div' \
                                          '/services-due/div[2]/lx-table/div[2]/div[2]/cdk-table' \
                                          '/cdk-row/cdk-cell[2]/span[2]'
    pm_upcoming_service_1st_service_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance' \
                                            '/div/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[1]/div' \
                                            '/services-due/div[2]/lx-table/div[2]/div[2]/cdk-table' \
                                            '/cdk-row/cdk-cell[3]/span[2]'
    pm_upcoming_service_1st_interval_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance' \
                                             '/div/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[1]/div' \
                                             '/services-due/div[2]/lx-table/div[2]/div[2]/cdk-table' \
                                             '/cdk-row/cdk-cell[4]/span[2]'
    pm_upcoming_service_1st_status_xpath = '//cdk-cell[3][.//span[normalize-space(.)="000___A"]]/parent::cdk-row/cdk-cell[5]'
    pm_upcoming_service_1st_action_xpath = '//cdk-cell[3][.//span[normalize-space(.)="000___A"]]/parent::cdk-row/cdk-cell[6]//span[normalize-space(.)="Complete"]'
    pm_complete_service_dialog_complete_id = 'modalShellPrimaryButton'

    # Maintenance_Preventative maintenance_history
    pm_history_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]' \
                       '/lytx-tab-views/div/div[1]/button[2]/span'
    pm_history_count_xpath = '//*[@data-test-id="filter-bar-count"]'
    pm_history_vehicle_label_xpath = '/html/body/app-root/shell/div/div/div/' \
                                     'app-maintenance/div/div[2]/lytx-tab-views' \
                                     '/div/div[2]/lytx-tab-view[2]/div/' \
                                     'service-history/div[2]/lx-table/div[2]' \
                                     '/div[2]/cdk-table/cdk-header-row/' \
                                     'cdk-header-cell[1]/span/span/span[1]'
    pm_history_group_label_xpath = '/html/body/app-root/shell/div/div/div/' \
                                   'app-maintenance/div/div[2]/lytx-tab-views' \
                                   '/div/div[2]/lytx-tab-view[2]/div/service-history' \
                                   '/div[2]/lx-table/div[2]/div[2]/cdk-table/' \
                                   'cdk-header-row/cdk-header-cell[2]/span/span'
    pm_history_service_label_xpath = '/html/body/app-root/shell/div/div/div/' \
                                     'app-maintenance/div/div[2]/lytx-tab-views' \
                                     '/div/div[2]/lytx-tab-view[2]/div/service-history' \
                                     '/div[2]/lx-table/div[2]/div[2]/cdk-table/' \
                                     'cdk-header-row/cdk-header-cell[3]/span/span'
    pm_history_interval_label_xpath = '/html/body/app-root/shell/div/div/div/' \
                                      'app-maintenance/div/div[2]/lytx-tab-views' \
                                      '/div/div[2]/lytx-tab-view[2]/div/service-history' \
                                      '/div[2]/lx-table/div[2]/div[2]/cdk-table/' \
                                      'cdk-header-row/cdk-header-cell[4]/span/span'
    pm_history_date_serviced_label_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance' \
                                           '/div/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[2]' \
                                           '/div/service-history/div[2]/lx-table/div[2]/div[2]/' \
                                           'cdk-table/cdk-header-row/cdk-header-cell[5]/span/span/span[1]'
    pm_history_odometer_label_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance' \
                                      '/div/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[2]' \
                                      '/div/service-history/div[2]/lx-table/div[2]/div[2]/' \
                                      'cdk-table/cdk-header-row/cdk-header-cell[6]/span/span'
    pm_history_engine_hours_label_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance' \
                                          '/div/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[2]' \
                                          '/div/service-history/div[2]/lx-table/div[2]/div[2]/' \
                                          'cdk-table/cdk-header-row/cdk-header-cell[7]/span/span'
    pm_history_notes_label_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/' \
                                   'div/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[2]/' \
                                   'div/service-history/div[2]/lx-table/div[2]/div[2]/' \
                                   'cdk-table/cdk-header-row/cdk-header-cell[8]/span/span'
    pm_history_action_label_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance' \
                                    '/div/div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[2]' \
                                    '/div/service-history/div[2]/lx-table/div[2]/div[2]/' \
                                    'cdk-table/cdk-header-row/cdk-header-cell[9]/span/span'
    pm_history_date_filter_xpath = '/html/body/app-root/shell/div/div/div/' \
                                   'app-maintenance/div/div[2]/lytx-tab-views/' \
                                   'div/div[2]/lytx-tab-view[2]/div/service-history' \
                                   '/div[1]/lx-filter-bar/div/div/div[2]/' \
                                   'lx-date-range-filter/div/div[1]'
    pm_history_last_60_days_xpath = '/html/body/app-root/shell/div/div/div/' \
                                    'app-maintenance/div/div[2]/lytx-tab-views/' \
                                    'div/div[2]/lytx-tab-view[2]/div/service-history/' \
                                    'div[1]/lx-filter-bar/div/div/div[2]/lx-date-range-filter' \
                                    '/div/div[2]/lx-date-range-selector/div/div[2]/div[1]/div[3]'
    pm_history_1st_vehicle_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]/lytx-tab-views' \
                                   '/div/div[2]/lytx-tab-view[2]/div/service-history/div[2]/lx-table/div[2]/div[2]' \
                                   '/cdk-table/cdk-row/cdk-cell[1]/span[2]/span'
    pm_history_1st_group_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]/lytx-tab-views' \
                                 '/div/div[2]/lytx-tab-view[2]/div/service-history/div[2]/lx-table/div[2]/div[2]' \
                                 '/cdk-table/cdk-row/cdk-cell[2]/span[2]'
    pm_history_1st_service_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]/lytx-tab-views' \
                                   '/div/div[2]/lytx-tab-view[2]/div/service-history/div[2]/lx-table/div[2]/div[2]' \
                                   '/cdk-table/cdk-row/cdk-cell[3]/span[2]'
    pm_history_1st_interval_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]/lytx-tab-views' \
                                    '/div/div[2]/lytx-tab-view[2]/div/service-history/div[2]/lx-table/div[2]/div[2]' \
                                    '/cdk-table/cdk-row/cdk-cell[4]/span[2]'
    pm_history_1st_date_serviced_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]' \
                                         '/lytx-tab-views/div/div[2]/lytx-tab-view[2]/div/service-history/div[2]' \
                                         '/lx-table/div[2]/div[2]/cdk-table/cdk-row/cdk-cell[5]/span[2]'
    pm_history_1st_odometer_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]/lytx-tab-views' \
                                    '/div/div[2]/lytx-tab-view[2]/div/service-history/div[2]/lx-table/div[2]/div[2]' \
                                    '/cdk-table/cdk-row/cdk-cell[6]/span[2]'
    pm_history_1st_engine_hours_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]' \
                                        '/lytx-tab-views/div/div[2]/lytx-tab-view[2]/div/service-history/div[2]' \
                                        '/lx-table/div[2]/div[2]/cdk-table/cdk-row/cdk-cell[7]/span[2]'
    pm_history_1st_notes_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]/lytx-tab-views' \
                                 '/div/div[2]/lytx-tab-view[2]/div/service-history/div[2]/lx-table/div[2]/div[2]' \
                                 '/cdk-table/cdk-row/cdk-cell[8]/span[2]'
    pm_history_1st_edit_xpath = '//*[text()=" Edit "]'
    pm_history_1st_only_edit_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]/lytx-tab-views' \
                                     '/div/div[2]/lytx-tab-view[2]/div/service-history/div[2]/lx-table/div[2]/div[2]' \
                                     '/cdk-table/cdk-row/cdk-cell[9]/span[2]'
    pm_history_service_page_count = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]/lytx-tab-views' \
                                    '/div/div[2]/lytx-tab-view[2]/div/service-history/div[2]/paginator/div/div[3]' \
                                    '/download-csv/div/button/span'

    # pm history edit service
    pm_history_edit_service_date_selector_xpath = '/html/body/ngb-modal-window/div/div/complete-or-edit-service-interval' \
                                                  '/lytx-modal-shell/div/div[2]/div[2]/div[1]/div/div[7]/lytx-date-picker'
    pm_history_edit_service_1st_day_xpath = '/html/body/ngb-modal-window/div/div/complete-or-edit-service-interval' \
                                            '/lytx-modal-shell/div/div[2]/div[2]/div[1]/div/div[7]/lytx-date-picker' \
                                            '/div/div[2]/ngb-datepicker/div[2]/div/ngb-datepicker-month/div[2]/div[1]'
    pm_history_edit_service_hour_xpath = '/html/body/ngb-modal-window/div/div/complete-or-edit-service-interval' \
                                         '/lytx-modal-shell/div/div[2]/div[2]/div[1]/div/div[8]' \
                                         '/time-selector/div/div[1]/input[1]'
    pm_history_edit_service_minute_xpath = '/html/body/ngb-modal-window/div/div/complete-or-edit-service-interval' \
                                           '/lytx-modal-shell/div/div[2]/div[2]/div[1]/div/div[8]' \
                                           '/time-selector/div/div[1]/input[2]'
    pm_history_edit_service_period_xpath = '/html/body/ngb-modal-window/div/div/complete-or-edit-service-interval' \
                                           '/lytx-modal-shell/div/div[2]/div[2]/div[1]/div/div[8]' \
                                           '/time-selector/div/div[1]/input[3]'
    pm_history_edit_service_save_id = 'modalShellPrimaryButton'
    pm_history_previous_month_xpath = '/html/body/ngb-modal-window/div/div/complete-or-edit-service-interval' \
                                      '/lytx-modal-shell/div/div[2]/div[2]/div[1]/div/div[7]/lytx-date-picker' \
                                      '/div/div[2]/ngb-datepicker/div[1]/ngb-datepicker-navigation/div[1]/button'
    # Maintenance_Preventative maintenance_manage service
    maint_manage_services_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div' \
                                  '/div[2]/lytx-tab-views/div/div[1]/button[3]'

    manage_service_count_xpath = '/html/body/app-root/shell/div/div/div/app-maintenance/div/div[2]' \
                                 '/lytx-tab-views/div/div[2]/lytx-tab-view[3]/div' \
                                 '/service-management-new/div[1]/lx-filter-bar/div/div' \
                                 '/div[1]/div[1]/div/div[1]/div'
    maint_create_service_xpath = '//*[text()=" Create Service "]'
    maint_service_name_xpath = '//*[@id="service-name-input"]/lytx-input/div/div[2]/input'

    # Note: this id changes when different pre-steps are performed
    maint_service_check_mile_xpath = '(//*[@class="lx-icon lx-checkbox-inactive"])[1]'
    maint_service_mile_due_xpath = '//*[@id="service-interval-input"]/lytx-number-input/div/div[2]/input'
    maint_service_mile_due_soon_xpath = '//*[@id="due-soon-input"]/lytx-number-input/div/div[2]/input'
    maint_service_vehicle_dropdown_xpath = '//*[@id="vehicles-section"]/div[1]/div[3]/multiselect-typeahead/div/div[1]'
    maint_service_select_vehicle_xpath = '/html/body/app-root/shell/div/div/div/app-service-form-new/div/form/div[1]' \
                                         '/div[4]/div/div[1]/div[3]/multiselect-typeahead/div/div[1]/div' \
                                         '/multiselect-typeahead-window/button/multiselect-highlight'
    maint_service_save_xpath = '//*[@id="submitButton"]'
    maint_service_delete_id = 'deleteButton'
    maint_service_confirm_delete_id = 'modalShellPrimaryButton'
    maint_service_list_service_name_xpath = '//*[text()="000__A"]'
    updated_service_list_service_name_xpath = '//*[text()="000___A"]'

    # Maintenance_Diagnostic trouble codes
    dtc_title_xpath = '/html/body/app-root/shell/div/div/div/' \
                      'app-dtc/div/div[1]/filter-bar/div/div[1]/span[1]'

    group_filter_dtc_page_xpath = '/html/body/app-root/shell/div/div/div/' \
                                  'app-dtc/div/div[1]/filter-bar/div/div[2]/div[2]/group-filter/div'
    search_by_group_textbox_dtc_page_xpath = '/html/body/ngb-modal-window/' \
                                             'div/div/group-selector-modal/group-selector' \
                                             '/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_search_button_dtc_page_xpath = '/html/body/ngb-modal-window/div/div/' \
                                          'group-selector-modal/group-selector/div/div[1]' \
                                          '/div[2]/div/lytx-typeahead/div/' \
                                          'ngb-typeahead-window/button'
    done_button_dtc_page_xpath = '/html/body/ngb-modal-window/div/div/' \
                                 'group-selector-modal/group-selector/' \
                                 'div/div[3]/button[2]'
    code_count_xpath = '/html/body/app-root/shell/div/div/div/app-dtc/div/div[1]/filter-bar/div/' \
                       'div[2]/div[1]/div[1]/div/div[1]'
    vehicle_column_text_dtc_page_xpath = '/html/body/app-root/shell/div/div/div/app-dtc/div/' \
                                         'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                         'cdk-header-cell[1]/span'
    group_column_text_dtc_page_xpath = '/html/body/app-root/shell/div/div/div/app-dtc/div/' \
                                       'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/' \
                                       'cdk-header-cell[2]/span'
    code_column_text_dtc_page_xpath = '/html/body/app-root/shell/div/div/div/app-dtc/div/lx-table/div[2]' \
                                      '/div[2]/cdk-table/cdk-header-row/cdk-header-cell[4]/span/span'
    date_column_text_dtc_page_xpath = '/html/body/app-root/shell/div/div/div/app-dtc/div/' \
                                      'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[3]/span/span'

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
    maintenance_xpath = '//*[text()="Maintenance"]'
    maintenance_new_ui_xpath = '//div[span[contains(normalize-space(.), "Maintenance")]]'
    preventative_maintenance_xpath = '(//*[text()=" Preventative Maintenance "])[1]'
    preventative_maintenance_new_ui_xpath = '(//*[text()=" Preventative Maintenance"])[1]'
    dtc_xpath = '(//*[text()=" Diagnostic Trouble Codes "])[1]'
    dtc_new_ui_xpath = '(//*[text()=" Diagnostic Trouble Codes"])[1]'
    insights_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[3]'
    fleet_operations_xpath = '/html/body/app-root/shell/div' \
                             '/div/navigation/div[1]/div[3]/div[2]/div[2]/div[1]/div'
    fleet_data_xpath = '/html/body/app-root/shell/div/div/navigation' \
                       '/div[1]/div[3]/div[2]/div[2]/div[2]/div'
    equipment_status_xpath = '/html/body/app-root/shell/div/div/' \
                             'navigation/div[1]/div[3]/div[2]/div[2]/div[3]/div'
    geofences_xpath = '/html/body/app-root/shell/div/div/' \
                      'navigation/div[1]/div[3]/div[2]/div[2]/div[4]/div'

    state_mileage_xpath = '/html/body/app-root/shell/div/div/' \
                          'navigation/div[1]/div[3]/div[2]/div[2]/div[5]/div'

    data_export_xpath = '/html/body/app-root/shell/div/div/' \
                        'navigation/div[1]/div[3]/div[2]/div[2]/div[6]/div'

    click_on_service_interval_xpath = '/html/body/app-root/shell/div/div/div/app-service-form-new/div/form/div[1]/div[4]/div/div[2]/div'
    vehicle_name_xpath = '//*[text()=" Truck 692 "]'
    cancel_button_xpath = '//*[@id="cancelButton"]'
    newly_created_service_in_pm_upcoming_service_list_xpath = '//*[text()=" 000___A "]'
