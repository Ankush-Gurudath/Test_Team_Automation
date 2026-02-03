class LocatorsCoaching:
    # VideoWatching
    watch_video_xpath = '//video-player/div[2]/div[2]/div[2]/i'

    # Share
    share_button_xpath = '/html/body/app/shell/div/div/div/coaching-session' \
                         '/lx-page-container/div/div[4]/action-bar/div[1]/' \
                         'div[1]/span'
    share_copy_xpath = '/html/body/ngb-modal-window/div/div/share-event/' \
                       'lytx-modal-shell/div/div[2]/div[2]/lx-copy/div' \
                       '/div/button'
    share_close_xpath = '/html/body/ngb-modal-window/div/div/share-event' \
                        '/lytx-modal-shell/div/div[2]/div[3]/button'
    copy_button_text_class_name = 'lytx-copy__action'

    # AddRecognition
    add_recognition_button_xpath = '//*[@id="action-bar-positive-recognition"]'
    recognition_reason_xpath = '//*[@class="positive-recognition__content__edit--reason"]//textarea'
    recognition_complete_css = 'body > ngb-modal-window > div > div ' \
                               '> positive-recognition > div.positive-recognition' \
                               ' > div.positive-recognition__content.ng-star-inserted' \
                               ' > div.positive-recognition__content__edit.ng-star-inserted ' \
                               '> button'
    recognition_delete_css = 'body > ngb-modal-window > div > div > positive-recognition' \
                             ' > div.positive-recognition > ' \
                             'div.positive-recognition__content.ng-star-inserted ' \
                             '> div.positive-recognition__content__header >' \
                             ' div.positive-recognition__content__header__' \
                             'actions.ng-star-inserted ' \
                             '> div.delete-recognition.lx-link.ng-star-inserted'
    recognition_close_css = '#modalShellPrimaryButton'
    recognition_message_class_name = 'positive-recognition__content__preview--reason'

    # ContactLytx
    contact_tab_xpath = '//*[@data-test-id="shared-actionBar-contact"]'
    contact_issue_dropdown_xpath = '/html/body/ngb-modal-window/div/div/' \
                                   'contact-lytx/lytx-modal-shell/div/div[2]/div[' \
                                   '2]/div/div[2]/dropdown/div/span/span'
    contact_other_concern_xpath = '/html/body/ngb-modal-window/div/div/contact-lytx/' \
                                  'lytx-modal-shell/div/div[2]/div[2]/div/div[2]' \
                                  '/dropdown/div/div/ul/li[3]/span'
    contact_message_box_css = '#contact-lytx__message-field'
    contact_submit_css = '#modalShellPrimaryButton'
    contact_done_css = '#modalShellPrimaryButton'
    contact_submit_message_id = 'contact-lytx-success-message'

    # AddEventNotes
    add_event_notes_tab_css = '#event-notes__add'
    add_events_textbox_css = '#newCommentTextArea'
    add_events_submit_button_css = '#addEventCommentButton'
    event_note_container_id = 'event-viewer__event-notes'
    event_note_class_name = 'event-notes__body__note__container__text'

    # AddSessionNotes
    add_session_tab_id = 'event-notes__add'
    add_session_textbox_id = 'newCommentTextArea'
    add_session_submit_button_css = '#addEventCommentButton'
    session_note_container_id = 'event-viewer__session-notes'
    session_note_class_name = 'event-notes__body__note__container__text'
    session_note_xpath = '/html/body/app/shell/div/div/div/coaching-session/lx-page-container' \
                         '/div/div[6]/old-event-comments/lx-section/section/div[2]/' \
                         'lx-section-content/div/lx-comments/div/div[2]/div[2]/span'

    # ActionPlan
    action_plan_xpath = '/html/body/app/shell/div/div/div/coaching-session/lx-page-container/div/div[7]/action-plan-select/lx-section/section/div/div[2]/lx-section-content/div/form/lytx-radio-button[1]/label/div[1]/i'

    # CompleteSession
    complete_session_xpath = '//*[@id="coaching-session-complete-button"]'
    complete_session_save_css = '#modalShellPrimaryButton'
    complete_session_close_css = '#modalShellSecondaryButton'
    complete_session_message_id = 'coaching-session-confirmation'

    # CoachingTitle
    coaching_session_title_text_css = 'body > app > shell > div > div > div > ' \
                                      'coaching-task-card-list >' \
                                      ' task-card-list > div > div.ltc-list__header' \
                                      ' > filter-bar > div > ' \
                                      'div.filter-header-type > span.filter-header-title'
    task_coaching_label_xpath = '//div[contains(@class, "filter-header-bar")]//*[contains(text(), " task")]'
    driver_name_card_xpath = '/html/body/app/shell/div/div/div/coaching-task-card-list' \
                             '/task-card-list/div/div[3]/' \
                             'coaching-task-card/div/div[2]/event-task-content/div[1]/span/span'
    preview_card_xpath = '/html/body/app/shell/div/div/div/coaching-task-card-list/task-card-list' \
                         '/div/div[3]/coaching-task-card[1]/div/div[1]/div/div'
    group_card_id = 'group-label'
    vehicle_card_id = 'vehicle-label'
    event_date_card_id = 'date-label'
    time_card_id = 'time-label'
    overdue_date_card_id = 'overdue-label'
    behaviors_card_id = 'behaviors-label'
    no_coach_events_card_xpath = '/html/body/app/shell/div/div/div/coaching-task-card-list' \
                                 '/task-card-list/div/' \
                                 'div[3]/coaching-task-card/div/div[2]/div[2]/button'
    driver_coaching_session_title_xpath = '/html/body/app/shell/div/div/div/coaching-session' \
                                          '/lx-page-container/div/lx-page-header/h1'
    driver_coaching_session_title_xpath_new_UI = '//*[text()="DRIVER COACHING SESSION"]'
    driver_name_label_xpath = '//*[@class="driver-info__header lx-link sensitive-data"]'
    employee_id_xpath = '//*[@id="driver-info__employee-number-label"]/div'
    group_label_xpath = '//*[@id="driver-info__group-label"]/div'
    email_label_xpath = '//*[@id="driver-info__email-label"]/div'
    coaching_history_label_xpath = '//*[text()="Coaching History - Last 180 Days"]'
    event_videos_label_xpath = '//*[contains(@id, "event-carousel__header")]'
    video_section_xpath = '//*[@id="event-player-container"]/player-tabs/div/div[2]/div[1]'
    more_actions_xpath = '//span[text()="More Actions"]'
    reassign_driver_xpath = '/html/body/app/shell/div/div/div/coaching-session/lx-page-container/div' \
                            '/div[4]/action-bar/div[1]/div[4]/div/div/context-menu/div/ul/li[1]/span'
    assign_driver_search_xpath = '/html/body/ngb-modal-window/div/div/assign-driver/' \
                                 'lytx-modal-shell/div/div[2]/div[2]/div/div/user-search/div/' \
                                 'lytx-typeahead/div/input'
    select_assign_driver_search_xpath = '/html/body/ngb-modal-window/div/div/assign-driver/' \
                                        'lytx-modal-shell/div/div[2]/div[2]/div/div/user-search/' \
                                        'div/lytx-typeahead/div/ngb-typeahead-window/button'
    assign_driver_button_xpath = '/html/body/ngb-modal-window/div/div/assign-driver/' \
                                 'lytx-modal-shell/div/div[2]/div[3]/button[2]'
    behaviors_label_xpath = '//*[@id="event-viewer-details__behaviors-label"]'
    event_date_label_xpath = '//*[@id="event-viewer-details__record-date-label"]/div'
    event_label_xpath = '//*[@id="event-viewer-details__event-label"]/div'
    status_label_xpath = '//*[@id="event-viewer-details__aggregated-status-label"]/div'
    trigger_label_xpath = '//*[@id="event-viewer-details__trigger-label"]/div'
    score_label_xpath = '//*[@id="event-viewer-details__event-score-label"]/div'
    lytx_comments_label_xpath = '//*[text()="Lytx Comments"]'
    event_notes_label_xpath = '//*[@id="event-comments__header-notes"]/div/div/div'
    session_notes_label_xpath = '//*[@id="event-comments__header-notes"]/div/div/div/span'
    complete_session_label_xpath = '//*[@data-test-id="coachingSession-completeSession-buttonContainer"]'
    event_id_xpath = '//*[@id="event-viewer-details__data-content"]//lx-data-bar-item[2]//lx-data-bar-content/div'
    event_status_xpath = '//*[@id="event-viewer-details__data-content"]//lx-data-bar-item[3]//lx-data-bar-content/div'

    filter_by_group_button_xpath = '/html/body/app/shell/div/div/div/coaching-task-card-list/' \
                                   'task-card-list/div/div[1]/filter-bar/div/div[2]/div[2]' \
                                   '/group-filter/div/span'
    filter_by_group_search_box_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal/' \
                                       'group-selector/div/div[1]/div[2]/div/lytx-typeahead' \
                                       '/div/input'
    select_search_filter_by_group_xpath = '/html/body/ngb-modal-window/div/div/' \
                                          'group-selector-modal/group-selector/div/div[1]/div[2]' \
                                          '/div/lytx-typeahead/div/ngb-typeahead-window/button[1]'
    done_filter_by_group_button_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal' \
                                        '/group-selector/div/div[3]/button[2]'
    triggers_filter_button_xpath = '//*[@id="task-card-list-trigger-filter"]/div/div[1]/div/input'
    select_triggers_filter_xpath = '/html/body/app/shell/div/div/div/coaching-task-card-list' \
                                   '/task-card-list/div/div[1]/filter-bar/div/div[2]/div[2]/' \
                                   'multiselect-typeahead/div/div[1]/' \
                                   'div/multiselect-typeahead-window/button[9]/i'
    behaviors_filter_button_xpath = '//*[@id="task-card-list-behavior-filter"]/' \
                                    'multiselect-typeahead/div/div[1]/div/input'
    select_behaviors_filter_xpath = '/html/body/app/shell/div/div/div/coaching-task-card-list' \
                                    '/task-card-list/div/div[1]/filter-bar/div/div[2]/div[2]/' \
                                    'behavior-selector/multiselect-typeahead/' \
                                    'div/div[1]/div/multiselect-typeahead-window/button[5]/i'
    search_name_filter_box_xpath = '//*[@id="searchInput"]'
    reset_filter_button_xpath = '/html/body/app/shell/div/div/div/coaching-task-card-list' \
                                '/task-card-list/div/div[1]/filter-bar/div/div[2]' \
                                '/div[2]/button/div'
    group_card_name_xpath = '/html/body/app/shell/div/div/div/coaching-task-card-list' \
                            '/task-card-list/div/div[3]/coaching-task-card[1]/div/div[2]' \
                            '/event-task-content/div[2]/div[2]/span[1]'
    behaviors_card_name_xpath = '//*[@id="behaviors-data"]'
    filter_message_text_xpath = '/html/body/app/shell/div/div/div/coaching-task-card-list' \
                                '/task-card-list/div/div[3]/span'
    mark_self_coaching_tab_xpath = '//*[contains(text(), "Mark as Self Coaching")]'
    confirm_self_coaching_button_xpath = '//*[@id="modalShellPrimaryButton"]'

    # Notify driver
    kebab_icon_in_task_card_xpath = '//*[contains(@class, "ltc-list__item__content__kebab-icon")]'
    notify_driver_xpath = '//*[contains(text(), "Notify Driver")]'
    notify_button_xpath = '//*[@id="modalShellPrimaryButton"]'
    event_status_text_xpath = '//*[@id="event-viewer-details__aggregated-status"]/div'
    task_count_xpath = '/html/body/app/shell/div/div/div/coaching-task-card-list/task-card-list/' \
                       'div/div[1]/filter-bar/div/div[2]/div[1]/div[1]/div/div[1]/div'
    select_coaching_task_dialog_xpath = '/html/body/ngb-modal-window/div/div/select-coaching-tasks-modal'
    continue_button_id = 'modalShellPrimaryButton'

    # mark as FYI notify
    event_id_filter_xpath = '/html/body/ngb-modal-window/div/div/event-preview' \
                            '/div/div[1]/span[2]/dropdown/div/span'
    select_event_id_xpath = '/html/body/ngb-modal-window/div/div/event-preview' \
                            '/div/div[1]/span[2]/dropdown/div/div/ul/li[2]'
    more_actions_event_preview_xpath = '/html/body/ngb-modal-window/div/div/event-preview' \
                                       '/div/div[2]/div[2]/action-bar/div[1]/div[4]'
    mark_as_fyi_notify_tab_xpath = '/html/body/ngb-modal-window/div/div/event-preview' \
                                   '/div/div[2]/div[2]/action-bar/div[1]/div[4]/div/div' \
                                   '/context-menu/div/ul/li[4]'
    yes_confirm_button_xpath = '/html/body/ngb-modal-window[2]/div/div/action-modal' \
                               '/lytx-modal-shell/div/div[2]/div[3]/button[2]'
    close_preview_page_button_xpath = '/html/body/ngb-modal-window/div/div/event-preview/div/div[1]/i'
    video_displayed_xpath = '//*[@id="event-player-container"]/div[2]/error-message/div/div[2]'
    change_video_xpath = "//div[@class='event-carousel__date-label event-carousel__date-label--not-viewed']"
