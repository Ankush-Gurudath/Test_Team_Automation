class LocatorsLibrary:
    # events table columns
    event_id_text_xpath = '//*[@role="columnheader"]//*[text()=" Event ID "]'
    driver_text_xpath = '//*[@role="columnheader"]//*[text()=" Driver "]'
    group_text_xpath = '//*[@role="columnheader"]//*[text()="Group"]'
    vehicle_text_xpath = '//*[@role="columnheader"]//*[text()="Vehicle"]'
    device_text_xpath = '//*[@role="columnheader"]//*[text()=" Device "]'
    event_date_text_xpath = '//*[@role="columnheader"]//*[text()="Event Date"]'
    score_text_xpath = '//*[@role="columnheader"]//*[text()="Score"]'
    status_text_xpath = '//*[@role="columnheader"]//*[text()=" Status "]'
    trigger_text_xpath = '//*[@role="columnheader"]//*[text()=" Trigger "]'
    behaviors_text_xpath = '//*[@role="columnheader"]//*[text()=" Behaviors "]'

    driver_name_text_xpath = '//*[contains(@class, "driver-name")]'
    events_preview_text_xpath = '//*[text()="Preview: "]'
    video_player_xpath = '//*[@id="video-element"]'
    event_id_button_xpath = '//span[contains(@class, "cell-value")]//event-preview-link'
    close_preview_button_xpath = '//*[@id="close-modal-icon_after-load"]'
    vehicle_name_text_xpath = '//*[contains(@class,"vehicle-name")]'
    device_name_text_xpath = '//*[contains(@class,"serial-number")]'
    first_event_status_xpath = '//*[contains(@class,"event-status")]'
    first_event_behavior_xpath = '//*[contains(@class,"cdk-cell lytx-table-cell cdk-column-Behaviors lytx-table-cell-width-limit-400 collapsed")]'
    first_event_driver_xpath = '//*[contains(@class, "driver-name")]'

    # filters
    event_list_search_criteria_xpath = '//lytx-typeahead/div/input'
    event_list_search_event_id_xpath = '//lytx-search/div/form/input'
    select_date_button_xpath = '//*[@class="lx-date-range-filter"]'
    select_last_7_days_button_xpath = '//*[text()=" Last 7 Days "]'
    select_last_90_days_button_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                       '/lx-page-container/div/lx-filter-bar/div/div/div[2]' \
                                       '/lx-date-range-filter/div/div[2]' \
                                       '/lx-date-range-selector/div/div[2]/div[1]/div[5]'
    apply_button_id = 'btn-apply'
    search_by_group_box_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal' \
                                '/group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_group_search_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal/group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/ngb-typeahead-window/button'
    done_button_xpath = '//*[text()="Done" or text()="DONE"]'
    filter_by_group_button_id = 'event-list-group-filter'
    filter_by_date_button_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                  '/lx-page-container/div/lx-filter-bar/div/div/div[2]' \
                                  '/lx-date-range-filter/div/div[1]/span'
    filter_by_type_button_id = 'event-list-type-filter'
    filter_by_trigger_button_id = 'event-list-trigger-filter'
    filter_by_behavior_button_id = 'event-list-behavior-filter'
    filter_by_status_button_id = 'event-list-status-filter'
    reset_button_xpath = '//*[text()="Reset"]'
    triggers_close_button_xpath = '(//*[text()=" Driver "])[2]'
    behaviors_close_button_xpath = '(//*[@class="lx-icon lx-chevron-lrg-up"])'
    statuses_close_button_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                  '/lx-page-container/div/lx-filter-bar/div/div/div[2]' \
                                  '/multiselect-typeahead[2]/div/div[2]'
    select_handheld_device_button_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                          '/lx-page-container/div/lx-filter-bar/div/div/div[2]' \
                                          '/behavior-selector/multiselect-typeahead/div/div[1]' \
                                          '/div/multiselect-typeahead-window/button[33]'
    select_coachable_button_xpath = '//*[text()=" Show Only Coachable "]'
    select_none_selected_button_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                        '/lx-page-container/div/lx-filter-bar/div/div/div[2]' \
                                        '/multiselect-typeahead[1]/div/div[1]/div' \
                                        '/multiselect-typeahead-window/button[1]'
    select_face_to_face_button_xpath = '//*[text()="Face-To-Face"]'
    select_fyi_notify_button_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                     '/lx-page-container/div/lx-filter-bar/div/div/div[2]' \
                                     '/multiselect-typeahead[2]/div/div[1]/div/' \
                                     'multiselect-typeahead-window/button[2]/multiselect-highlight'
    select_search_drop_down_id = 'event-list-search-criteria'
    select_search_button_xpath = '//lytx-search//span[contains(@class, "lx-search")]'
    select_event_id_button_xpath = '(//*[text()=" Event ID "])[1]'
    select_driver_button_xpath = '(//*[text()=" Driver "])[1]'
    select_vehicle_button_xpath = '(//*[text()=" Vehicle "])[1]'
    select_device_button_xpath = '(//*[text()=" Device "])[1]'
    search_event_id_combobox_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                     '/lx-page-container/div/lx-filter-bar/div/div/div[2]' \
                                     '/dropdown[2]/div/div/ul/li[1]/span'
    search_driver_combobox_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                   '/lx-page-container/div/lx-filter-bar/div/div/div[2]' \
                                   '/dropdown[2]/div/div/ul/li[2]/span'
    search_vehicle_combobox_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                    '/lx-page-container/div/lx-filter-bar/div/div/div[2]' \
                                    '/dropdown[2]/div/div/ul/li[3]/span'
    search_device_combobox_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                   '/lx-page-container/div/lx-filter-bar/div/div/div[2]' \
                                   '/dropdown[2]/div/div/ul/li[4]'
    coach_now_button_id = 'coachEventNow'
    coach_later_button_id = 'coachEventLater'
    resolve_button_id = 'resolveEvent'
    cancel_button_xpath = '/html/body/ngb-modal-window[2]/div/div/action-modal' \
                          '/lytx-modal-shell/div/div[2]/div[2]/button[1]'
    yes_confirm_button_xpath = '/html/body/ngb-modal-window[2]/div/div/action-modal' \
                               '/lytx-modal-shell/div/div[2]/div[2]/button[2]'
    add_recognition_button_xpath = '//*[@id="action-bar-positive-recognition"]'
    complete_recognition_button_xpath = '/html/body/ngb-modal-window[2]/div/div/' \
                                        'positive-recognition/div[1]/div[2]/div[3]/button'
    recognition_page_recognition_reason_xpath = '//textarea[contains(@class, "edit--reason--value")]'
    recognition_list_recognition_reason_xpath = '//*[text()=" Recognition Edited Reason: Good "]'
    close_recognition_button_xpath = '/html/body/ngb-modal-window[2]/div/div/' \
                                     'positive-recognition/div[1]/div[1]/i'
    more_actions_button_xpath = '/html/body/ngb-modal-window/div/div/event-preview' \
                                '/div/div[2]/div[2]/action-bar/div[1]/div[3]/span'
    more_actions_button_ar_xpath = '//span[text()="More Actions"]'
    more_actions_button_reassign_group_xpath = '//span[text()="Reassign Group"]'
    mark_as_fyi_notify_button_xpath = '/html/body/ngb-modal-window/div/div/event-preview/div/div[2]/div[2]/action-bar/div[1]/div[3]/div/div/context-menu/div/ul/li[3]'
    confirm_mark_as_fyi_notify_button_xpath = '//*[contains(text(), "Yes, confirm")]'
    # the assign driver xpath when there IS driver assigned to the event
    reassign_driver_button_xpath = '/html/body/ngb-modal-window/div/div/event-preview' \
                                   '/div/div[2]/div[2]/action-bar/div[1]/div[4]/div/div' \
                                   '/context-menu/div/ul/li[1]/span'
    # the assign driver xpath when there is NO driver assigned to the event
    reassign_driver_button_wd_xpath = '/html/body/ngb-modal-window/div/div/event-preview' \
                                      '/div/div[2]/div[2]/action-bar/div[1]/div[3]/div/div' \
                                      '/context-menu/div/ul/li[1]/span'
    mark_as_self_coaching_button_xpath = '/html/body/ngb-modal-window/div/div/event-preview' \
                                         '/div/div[2]/div[2]/action-bar/div[1]/div[4]' \
                                         '/div/div/context-menu/div/ul/li[4]/span'
    event_preview_assign_driver_textbox_xpath = '/html/body/ngb-modal-window[2]/div/div/' \
                                                'assign-driver/lytx-modal-shell/div/div[2]' \
                                                '/div[2]/div/div/user-search/div/' \
                                                'lytx-typeahead/div/input'
    event_preview_assign_button_xpath = '/html/body/ngb-modal-window[2]/div/div' \
                                        '/assign-driver/lytx-modal-shell/div/div[2]' \
                                        '/div[3]/button[2]'

    event_preview_assign_group_textbox_xpath = '//input[@placeholder="Search by Group"]'
    event_preview_select_group_xpath = '/html/body/ngb-modal-window[2]/div/div/event-group-selector' \
                                       '/group-selector/div/div[1]/div[2]/div/lytx-typeahead/' \
                                       'div/ngb-typeahead-window/button'
    event_preview_done_button_xpath = '//*[text()="Done" or text()="DONE"]'
    reassign_group_done_button_xpath = '//*[text()="Done" or text()="DONE"]'
    event_detail_expand_icon_xpath = '//div[@class="expand-icon__background"]'
    event_group_text_xpath = '//*[@id="event-viewer-details__group-name"]'
    select_search_name_xpath = '/html/body/ngb-modal-window[2]/div/div/assign-driver' \
                               '/lytx-modal-shell/div/div[2]/div[2]/div/div/user-search' \
                               '/div/lytx-typeahead/div/ngb-typeahead-window/button'
    close_status_dropdown_button_xpath = '(//*[@class="lx-icon lx-chevron-lrg-up"])'
    success_event_assigned_dialog_xpath = '/html/body/div[2]/div/div/div'
    success_event_moved_dialog_xpath = '/html/body/div/div/div/div'
    event_preview_status_xpath = '/html/body/ngb-modal-window/div/div/event-preview' \
                                 '/div/div[2]/div[2]/event-details-info/div[1]/div[3]' \
                                 '/lx-data-bar/div/div[2]/lx-data-bar-item[3]' \
                                 '/div/lx-data-bar-content/div'
    select_first_event_id_checkbox_xpath = '(//*[@class="checkbox"])[1]'
    move_group_button_xpath = '//*[text()="Move Group"]'
    change_group_done_button_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal' \
                                     '/group-selector/div/div[3]/button[2]/span'
    move_group_continue_button_xpath = '//*[@id="modalShellPrimaryButton"]'
    success_message_close_button_xpath = '/html/body/div[2]/div/div/button/span'
    recognition_text_xpath = '//*[text()="View Recognition"]'
    # RECOGNITION HISTORY
    type_column_name_xpath = '//*[text()=" Type "]'
    driver_column_name_xpath = '(//*[text()=" Driver "])[2]'
    group_column_name_recognition_history_xpath = '//*[text()=" Group "]'
    event_id_column_name_xpath = '(//*[text()=" Event ID "])[2]'
    issued_by_column_name_xpath = '(//*[text()=" Issued By "])[2]'
    issued_date_column_name_xpath = '(//*[text()="Issued Date"])[1]'
    recognition_reason_column_name_xpath = '//*[text()=" Recognition Reason "]'
    filter_by_search_dropdown_id = 'recognition-history-search-filter'
    filter_by_driver_dropdown_xpath = '(//*[text()=" Driver "])[1]'
    filter_by_issued_by_dropdown_xpath = '(//*[text()=" Issued By "])[1]'
    filter_by_event_id_dropdown_xpath = '(//*[text()=" Event ID "])[1]'
    filter_by_search_criteria_textbox_xpath = '//*[@class="typeahead-search"]'
    filter_by_event_id_textbox_xpath = '//lytx-search/div/form/input'
    filter_by_search_criteria_button_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                             '/lx-page-container/div/lx-filter-bar/div/div/' \
                                             'div[2]/div/div/div/span'
    type_link_xpath = '(//*[contains(@class, "cell-value")]//*[contains(@class, "lx-link recognition-link")])[1]'
    driver_link_xpath = '(//*[contains(@class, "cell-value")]//*[contains(@class, "driver-name")])[1]'
    event_id_link_xpath = '//*[contains(@class, "event-id")]'
    issued_by_link_xpath = '(//*[contains(@class, "cell-value")]//*[contains(@class, "recognition-list__list__item--issuer lx-link sensitive-data")])[1]'
    recognition_certificate_title_xpath = '//*[contains(text(), "Recognition Certificate")]'
    recognition_close_button_xpath = '//*[text()=" close "]'
    recognition_download_button_xpath = '//*[contains(@class, "download-recognition")]'
    recognition_edit_button_xpath = '//*[contains(text(), "Edit")]'
    recognition_delete_button_xpath = '//*[contains(text(), "Delete")]'
    recognition_complete_button_xpath = '//button[text()="Complete"]'
    recognition_confirm_delete_button_xpath = '//*[@id="modalShellPrimaryButton"]'
    recognition_issued_date_xpath = '(//*[contains(@class, "recognition-list__list__item--date")])[1]'
    first_recognition_link_xpath = '(//*[contains(@class, "cell-value")]//*[contains(@class, "lx-link recognition-link")])[1]'
    recognition_count_xpath = '//*[contains(@class, "title__count--value--success")]'
    group_name_recognition_page_xpath = '//*[contains(@class, "group_name")]'
    # COACHING HISTORY
    session_count_label_xpath = '//*[@class="filter-header-bar__title__count--container"]'
    sessions_label_xpath = '/html/body/app/shell/div/div/div/ng-component/' \
                           'lx-page-container/div/lx-filter-bar/div/div/' \
                           'div[1]/div[1]/div[1]/div[2]'
    sessions_label_xpath_new_UI = '//*[@data-test-id="filterHeaderBar-titleCount-label"]'
    session_ID_label_xpath = '(//*[text()=" Session ID "])[2]'
    coach_date_label_xpath = '//*[@id="sortableContainerCoachDate"]'
    overdue_date_label_xpath = '//cdk-header-cell//span[contains(text(), "OverDue Date")]'
    driver_label_xpath = '//cdk-header-cell//span[contains(text(), "Driver")]'
    behaviors_coached_label_xpath = '//cdk-header-cell//span[contains(text(), " Behaviors Coached ")]'
    group_label_xpath = '//cdk-header-cell//span[contains(text(), " Group ")]'
    coach_label_xpath = '//cdk-header-cell//span[contains(text(), " Coach ")]'
    notes_label_xpath = '//cdk-header-cell//span[contains(text(), " Notes ")]'
    action_plan_label_xpath = '//cdk-header-cell//span[contains(text(), " Action Plan ")]'
    coaching_history_tab_xpath = '/html/body/app/shell/div/div/navigation/' \
                                 'div[1]/div[4]/div[2]/div[2]/div[2]'
    coaching_history_tab_xpath_new_ui = '//*[@href="#/driver-safety/library/coachinghistory"]'
    behaviors_drop_down_xpath = '//*[@id="coaching-history-behavior-filter"]'
    unusual_event_check_box_xpath = '//*[text()="*Unusual Event"]'
    select_search_drop_down_ch_xpath = '//*[@id="coaching-history-search-filter"]'
    filter_by_coach_dropdown_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                     '/lx-page-container/div/lx-filter-bar/div/div/div[2]' \
                                     '/dropdown/div/div/ul/li[1]'
    coaching_history_coach_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                   '/lx-page-container/div/lx-filter-bar' \
                                   '/div/div/div[2]/dropdown/div/div/ul/li[1]'
    coaching_history_driver_xpath = '//*[text()=" Driver "]'
    coaching_history_session_id_xpath = '//li//*[contains(text(), "Session ID")]'
    search_name_or_id_ch_textbox_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                         '/lx-page-container/div/lx-filter-bar/div/div' \
                                         '/div[2]/div/div/user-search/div/lytx-typeahead/div/input '
    search_session_id_ch_textbox_xpath = '//*[@id="searchInput"]'
    first_driver_in_dropdown_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                     '/lx-page-container/div/lx-filter' \
                                     '-bar/div/div/div[2]/div/div/user-search/div/' \
                                     'lytx-typeahead/div/ngb-typeahead-window/button[' \
                                     '1]/span'
    first_coach_in_dropdown_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                    '/lx-page-container' \
                                    '/div/lx-filter-bar/div/div/div[2]/div/div/user-search/div/' \
                                    'lytx-typeahead/div/ngb-typeahead-window/button/span '
    session_id_value_xpath = '//*[contains(@class, "cdk-column-Session-ID")]//span[contains(@class, "lx-link")]'
    driver_value_xpath = '/html/body/app/shell/div/div/div/ng-component/' \
                         'lx-page-container/div/div/div/coaching' \
                         '-sessions-history-table/lx-table/div[2]/div[2]' \
                         '/cdk-table/cdk-row[1]/cdk-cell[3]/span[2]/span '
    coach_value_xpath = '/html/body/app/shell/div/div/div/ng-component/' \
                        'lx-page-container/div/div/div/coaching' \
                        '-sessions-history-table/lx-table/div[2]/div[2]/' \
                        'cdk-table/cdk-row[1]/cdk-cell[5]/span[2]/span '
    past_session_title_xpath = '//*[text()="Past Session"]'
    summary_label_xpath = '//*[text()="Summary "]'
    session_notes_label_xpath = '//*[text()="Session Notes"]'
    event_coached_label_xpath = '//*[contains(text(), "Event Coached") or contains(text(), "Events Coached")]'
    data_export_tab_xpath = '/html/body/app/shell/div/div/navigation/div[1]' \
                            '/div[4]/div[2]/div[2]/div[4]'
    data_export_tab_xpath_new_ui = '//*[@href="#/driver-safety/library/dataexport"]'
    data_export_title_xpath = '//*[text()="Data Export"]'
    data_export_action_xpath = '/html/body/app/shell/div/div/div/data-export/lx-page-block' \
                               '/div/lx-header-free-floating-block/div/data-export-table' \
                               '/lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[6]/span[2]/span'
    report_type_column_name_xpath = '//*[text()=" Report Type "]'
    group_column_name_xpath = '//*[text()=" Group "]'
    date_range_column_name_xpath = '//*[text()=" Date Range "]'
    filters_column_name_xpath = '//*[text()=" Filters "]'
    requested_date_column_name_xpath = '//*[text()=" Requested Date "]'
    action_column_name_xpath = '//*[text()=" Action "]'
    new_export_button_xpath = '//*[text()=" New Export "]'
    requested_date_1st_request_xpath = '/html/body/app/shell/div/div/div/data-export' \
                                       '/lx-page-block/div/lx-header-free-floating-block' \
                                       '/div/data-export-table/lx-table/div[2]/div[2]' \
                                       '/cdk-table/cdk-row[1]/cdk-cell[5]/span[2]/span'
    report_type_value_xpath = '/html/body/app/shell/div/div/div/data-export/lx-page-block' \
                              '/div/lx-header-free-floating-block/div/data-export-table/' \
                              'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[' \
                              '1]/span[2]/span '
    report_type_dropdown_id = 'data-export-request-report-type-dropdown'
    event_data_text_xpath = '/html/body/ngb-modal-window/div/div/data-export-request-modal/' \
                            'lytx-modal-shell/div/div[' \
                            '2]/div[2]/div/div/dropdown/div/div/ul/li[1] '
    speed_data_text_xpath = '/html/body/ngb-modal-window/div/div/data-export-request-modal' \
                            '/lytx-modal-shell/div/div[' \
                            '2]/div[2]/div/div/dropdown/div/div/ul/li[2]/span '
    request_data_button_id = 'modalShellPrimaryButton'
    request_date_range_text_xpath = '/html/body/app/shell/div/div/div/data-export/lx-page-block' \
                                    '/div/lx-header-free-floating-block/div/data-export-table/' \
                                    'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[3]/span[2]/span'

    # Event page
    event_count_xpath = '//div[contains(@class, "title__count--value--success")]'
    trigger_filter_xpath_prefix = '//multiselect-typeahead[1]/div/div[1]/div/multiselect-typeahead-window/button['
    behavior_filter_xpath = '//*[text()="{0}"]'
    events_page_date_range_start_month_xpath = '/html/body/app/shell/div/div/div/ng-component/lx-page-container' \
                                               '/div/lx-filter-bar/div/div/div[2]/lx-date-range-filter/div/div[2]' \
                                               '/lx-date-range-selector/div/div[1]/div[1]/div[2]/lx-date-input/div/input[1]'
    events_page_date_range_start_day_xpath = '/html/body/app/shell/div/div/div/ng-component/lx-page-container' \
                                             '/div/lx-filter-bar/div/div/div[2]/lx-date-range-filter/div/div[2]' \
                                             '/lx-date-range-selector/div/div[1]/div[1]/div[2]/lx-date-input/div/input[2]'
    events_page_date_range_start_year_xpath = '/html/body/app/shell/div/div/div/ng-component/lx-page-container' \
                                              '/div/lx-filter-bar/div/div/div[2]/lx-date-range-filter/div/div[2]' \
                                              '/lx-date-range-selector/div/div[1]/div[1]/div[2]/lx-date-input/div/input[3]'
    events_page_date_range_end_month_xpath = '/html/body/app/shell/div/div/div/ng-component/lx-page-container' \
                                             '/div/lx-filter-bar/div/div/div[2]/lx-date-range-filter/div/div[2]' \
                                             '/lx-date-range-selector/div/div[1]/div[2]/div[2]/lx-date-input/div/input[1]'
    events_page_date_range_end_day_xpath = '/html/body/app/shell/div/div/div/ng-component/lx-page-container' \
                                           '/div/lx-filter-bar/div/div/div[2]/lx-date-range-filter/div/div[2]' \
                                           '/lx-date-range-selector/div/div[1]/div[2]/div[2]/lx-date-input/div/input[2]'
    events_page_date_range_end_year_xpath = '/html/body/app/shell/div/div/div/ng-component/lx-page-container' \
                                            '/div/lx-filter-bar/div/div/div[2]/lx-date-range-filter/div/div[2]' \
                                            '/lx-date-range-selector/div/div[1]/div[2]/div[2]/lx-date-input/div/input[3]'
    walkme_close_button_xpath = '/html/body/div[1]/div/div[1]/div[2]/div/div[1]'
    f2f_event_id = '(//event-preview-link)[1]'
    device_serial = '(//*[contains(@class,"serial-number")])[1]'
    vehicle_name = '(//*[contains(@class, "vehicle-name")])[1]'

    edit_behavior_id = 'event-viewer-details__behaviors-content__edit-icon'
    add_behavior_xpath = '//*[@id="event-viewer-details__behaviors-content__edit-icon"]'
    plus_add_behavior_xpath = '//*[contains(text(), "Add Behavior")]'
    event_preview_add_behavior_drop_down_xpath = '//*[contains(text(), "Add Behavior")]'
    select_first_behavior_in_drop_down_xpath = '//*[@id="event-viewer-details__behaviors-content"]//li[1]/span'
    select_behavior_not_captured_reason = '//*[contains(text(),"Behavior not captured")]'
    select_incorrect_behavior_identified_reason = '//*[contains(text(),"Incorrect behavior identified")]'
    reason_done_button_id = 'modalShellPrimaryButton'
    event_preview_add_behavior_save_button_xpath = '//*[@id="event-viewer-details__behaviors-content"]/div[2]/div[1]/div[2]/button'
    remove_behavior_button_xpath = '//*[@id="event-viewer-details__behaviors-content"]/div[1]/div[1]/lytx-pill/span/button/i'
    first_behavior = '//*[@id="event-viewer-details__behaviors-content"]/div/div[1]/lytx-pill/span/span'
    second_behavior = '//*[@id="event-viewer-details__behaviors-content"]/div/div[2]/lytx-pill/span/span'
    search_serial_number = '//*[@id="deviceInput"]/div/input'
    device_id_button_xpath = '//*[@id="ngb-typeahead-0-0"]'
    group_name_event_page_xpath = '//span[contains(@class, "group-name")]'
    vehicle_name_event_page_xpath = '//span[contains(@class, "vehicle-name")]'
    filter_by_group_recognition_history_id = 'recognition-history-group-filter'
    filter_by_group_coaching_history_id = 'coaching-history-group-filter'
    added_behavior_text_xpath = '//*[@id="event-viewer-details__behaviors-content"]//span/span'
    behavior_name_xpath = '//*[@class="behaviors_content__behaviors"]//lytx-pill/span'
    download_button_xpath = '(//*[contains(@class, "lx-icon lx-download download-icon ")])'
    mp4_button_xpath = '//*[text()="MP4"]'
    loading_indicator_xpath = '//*[@class="loading-indicator-container"]'
    coaching_date_text_coaching_history_tab_xpath = '//*[contains(@class, "coach-date")]'
    browse_in_video_search_xpath = '//*[@data-test-id="context-menu-list-4"]'
    browse_button_xpath = '//*[@id="browseText"]'
    emp_id_next_to_driver_name_xpath = '//*[contains(text(), "76582")]'
    overlay_toggle_xpath = '//*[@class="switch disabled small"]'
    overlay_label_xpath = '//*[text()="Overlay"]'
    overlay_tooltip_xpath = '//*[@class="tooltip-inner"]'
    download_button_event_preview_xpath = '//*[contains(@class,"lx-icon lx-download download-icon")]'
    download_option_dce_xpath = '//*[text()="DCE"]'
    download_option_mp4_with_overlay_xpath = '//context-menu//li[2]'
    library_search_bar_xpath = '(//*[@class="icon"])[5]'
    library_search_input_xpath = '//*[@id="searchInput"]'
    library_search_button_xpath = '//*[contains(@class, "lytx-search__magnifier")]'
    download_loading_xpath = '//*[@class="loading-indicator-container"]'
    download_option_mp4_without_overlay_xpath = '//*[text()="MP4 without overlay"]'
    event_id_link_coaching_history_xpath = '//*[@data-test-id="video-preview-span"]'

