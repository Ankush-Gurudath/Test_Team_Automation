class LocatorsDriverProfile:
    title_text_xpath = '//*[text()="Driver Profile"]'
    driver_name_text_xpath = '//span[@class="driver-info__header"]'
    add_recognition_link_xpath = '//*[@id="add-recognition-text"]'
    add_recognition_complete_button_xpath = '//button[text()="recognize"]'
    delete_recognition_button_xpath = '//div[text()="Delete "]'
    close_add_recognition_button_xpath = '//button[contains(text(), "close")]'
    coach_event_button_xpath = '/html/body/app/shell/div/div/div/ng-component/' \
                               'div/div[1]/div/div/button'
    view_remote_event_button_xpath = '/html/body/app/shell/div/div/div/ng-component/div/div[1]/div/div/button'
    play_video_button_xpath = '//video-player/div[2]/div[2]/div[2]'
    expand_icon_xpath = '//*[contains(@class, "expand-icon")]'
    event_status_text_xpath = '//*[@id="event-viewer-details__aggregated-status"]'
    close_preview_icon_xpath = '/html/body/ngb-modal-window/div/div/event-preview/div/div[1]/i'

    # View
    driver_profile_title_text_xpath = '//*[text()="Driver Profile"]'
    employee_id_text_xpath = '//*[@id="driver-info__employee-number-label"]/div'
    driver_group_text_xpath = '//*[@id="driver-info__group-label"]/div'
    email_text_xpath = '//*[@id="driver-info__email-label"]/div'

    coachable_driver_metrics_text_xpath = '//*[text()="Coachable Driver Metrics"]'
    score_metrics_text_xpath = '(//*[text()="SCORE"])[1]'
    events_metrics_text_xpath = '//*[contains(text(), "EVENTS")]'
    continual_behavior_metrics_text_xpath = '(//*[contains(text(), "Continual Behaviors")])[1]'
    driver_score_cards_text_xpath = '/html/body/app/shell/div/div/div/ng-component/div' \
                                    '/div[3]/driver-history/div/driver-metrics/lx-section' \
                                    '/section/div[2]/lx-section-content/div/div/div[2]/div[1]'
    coachable_behavior_text_xpath = '(//*[text()="COACHABLE BEHAVIOR "])[1]'
    frequency_text_xpath = '(//*[text()="FREQUENCY (A)"])[1]'
    weight_text_xpath = '(//*[contains(text(), "WEIGHT (B)")])[1]'
    points_text_xpath = '(//*[text()="POINTS (A × B)"])[1]'

    event_id_text_xpath = '//*[text()=" Event ID "]'
    event_group_text_xpath = '//*[text()=" Group "]'
    vehicle_text_xpath = '//*[text()=" Vehicle "]'
    device_text_xpath = '//*[text()=" Device "]'
    event_date_text_xpath = '//*[text()=" Event Date "]'
    event_score_text_xpath = '//*[text()=" Score "]'
    status_text_xpath = '//*[text()=" Status "]'
    trigger_text_xpath = '//*[text()=" Trigger "]'
    behaviors_metrics_text_xpath = '//*[text()=" Behaviors "]'

    continual_behavior_tab_text_xpath = '//*[contains(text(), " Continual Behaviors ")]'
    summary_count_text_xpath = '//*[text()="Summary"]'
    behavior_count_text_xpath = '//*[text()=" Behavior "]'
    duration_count_text_xpath = '//*[text()=" Duration "]'
    percent_of_drive_time_text_xpath = '//*[text()=" % Of Drive Time "]'
    incidents_tab_text_xpath = '//*[text()="Incidents"]'
    behavior_incident_text_xpath = '//*[text()=" Behavior "]'
    duration_incident_text_xpath = '//*[text()="Duration"]'
    date_incident_text_xpath = '//*[@id="sortableContainerStartTime"]/span[1]'

    coaching_history_tab_text_xpath = '//*[contains(@class, "coaching_history")]'
    coaching_history_tab_xpath = '(//*[contains(text(), " Coaching History ")])'
    session_id_text_xpath = '//*[text()=" Session ID "]'
    coach_date_text_xpath = '//*[@id="sortableContainerCoachDate"]/span[1]'
    overdue_date_text_xpath = '/html/body/app/shell/div/div/div/' \
                              'ng-component/div/div[3]/driver-history' \
                              '/div/driver-library/div/lx-tabs/' \
                              'driver-coaching-history-list/lx-section' \
                              '/section/div[2]/lx-section-content' \
                              '/div/div/coaching-sessions-history-table' \
                              '/lx-table/div[2]/div[2]/cdk-table/cdk-header-row' \
                              '/cdk-header-cell[3]/span/span'
    behaviors_coached_text_xpath = '/html/body/app/shell/div/div/div/' \
                                   'ng-component/div/div[3]/driver-history' \
                                   '/div/driver-library/div/lx-tabs/' \
                                   'driver-coaching-history-list/lx-section' \
                                   '/section/div[2]/lx-section-content' \
                                   '/div/div/coaching-sessions-history-table' \
                                   '/lx-table/div[2]/div[2]/cdk-table/cdk-header-row' \
                                   '/cdk-header-cell[4]/span/span'
    coach_text_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                       '/div/div[3]/driver-history/div/driver-library' \
                       '/div/lx-tabs/driver-coaching-history-list/lx-section' \
                       '/section/div[2]/lx-section-content/div/div/' \
                       'coaching-sessions-history-table/lx-table/' \
                       'div[2]/div[2]/cdk-table/cdk-header-row/' \
                       'cdk-header-cell[5]/span/span'
    notes_text_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                       '/div/div[3]/driver-history/div/driver-library' \
                       '/div/lx-tabs/driver-coaching-history-list/lx-section' \
                       '/section/div[2]/lx-section-content/div/div/' \
                       'coaching-sessions-history-table/lx-table/' \
                       'div[2]/div[2]/cdk-table/cdk-header-row/' \
                       'cdk-header-cell[6]/span/span'
    recognitions_tab_xpath = '//*[contains(text(), " Recognitions ")]'
    type_text_xpath = '//*[text()=" Type "]'
    event_id_rec_text_xpath = '//*[text()=" Event ID "]'
    issued_by_text_xpath = '//*[text()=" Issued By "]'
    issued_date_text_xpath = '//*[@id="sortableContainerIssuedDate"]/span[1]'
    recognition_reason_text_xpath = '//*[text()=" Recognition Reason "]'
    edit_message_button_xpath = '//div[contains(@class, "message")]//div[contains(@class, "edit-recognition lx-link")]'
    recognition_reason_text_area_xpath = '//*[@class="positive-recognition__content--reason"]/textarea'
    check_or_right_marke_edit_recognition_xpath = '//*[contains(@class, "lytx lx-icon lx-check")]'
    driver_profile_text_xpath = '// *[text() = "Driver Profile"]'