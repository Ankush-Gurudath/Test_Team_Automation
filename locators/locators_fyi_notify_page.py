class LocatorsFyinotify:
    # Filters
    filter_by_group_button_xpath = '/html/body/app/shell/div/div/div/fyi-notify-task-card-list/' \
                                   'task-card-list/div/div[1]/filter-bar/div/div[2]' \
                                   '/div[2]/group-filter/div'
    search_filter_by_group_textbox_xpath = '/html/body/ngb-modal-window/div/div/' \
                                           'group-selector-modal/' \
                                           'group-selector/div/div[1]/div[2]/div/' \
                                           'lytx-typeahead/div/input'
    select_search_filter_by_group_xpath = '/html/body/ngb-modal-window/div/div/' \
                                          'group-selector-modal/' \
                                          'group-selector/div/div[1]/div[2]/div/' \
                                          'lytx-typeahead/div/' \
                                          'ngb-typeahead-window/button'
    done_filter_by_group_button_xpath = '/html/body/ngb-modal-window/div/div/' \
                                        'group-selector-modal/' \
                                        'group-selector/div/div[3]/button[2]'
    search_driver_name_textbox_xpath = '//*[@id="searchInput"]'
    reset_fyi_notify_button_xpath = '/html/body/app/shell/div/div/div/fyi-notify-task-card-list/' \
                                    'task-card-list/div/div[1]/filter-bar/div/' \
                                    'div[2]/div[2]/button/div'
    fyi_notify_tasks_message_xpath = '/html/body/app/shell/div/div/div/fyi-notify-task-card-list/' \
                                     'task-card-list/div/div[3]/span'
    # View FYI task
    # need to add behavior label once api creates event with behavior
    group_card_name_xpath = '/html/body/app/shell/div/div/div/fyi-notify-task-card-list/' \
                            'task-card-list/div/div[3]/fyi-notify-card[1]/div/div[2]/' \
                            'event-task-content/div[2]/div[2]/span[1]'
    group_text_xpath = '/html/body/app/shell/div/div/div/fyi-notify-task-card-list/' \
                       'task-card-list/div/div[3]/fyi-notify-card/div/div[2]/' \
                       'event-task-content/div[2]/div[1]/span[1]'
    vehicle_text_xpath = '/html/body/app/shell/div/div/div/fyi-notify-task-card-list/' \
                         'task-card-list/div/div[3]/fyi-notify-card/div/div[2]/' \
                         'event-task-content/div[2]/div[1]/span[2]'
    event_date_text_xpath = '/html/body/app/shell/div/div/div/fyi-notify-task-card-list/' \
                            'task-card-list/div/div[3]/fyi-notify-card/div/div[2]/' \
                            'event-task-content/div[3]/div[1]/span[1]'
    time_text_xpath = '/html/body/app/shell/div/div/div/fyi-notify-task-card-list/' \
                      'task-card-list/div/div[3]/fyi-notify-card/div/div[2]/' \
                      'event-task-content/div[3]/div[1]/span[2]'
    preview_button_xpath = '/html/body/app/shell/div/div/div/fyi-notify-task-card-list/' \
                           'task-card-list/div/div[3]/fyi-notify-card[1]' \
                           '/div/div[2]/div[2]/button/span'
    close_preview_page_button_xpath = '/html/body/ngb-modal-window/div/div/event-preview/div/div[1]/i'
    # action for FYI event--the coach later will be the first if the FYI event without driver assigned
    coach_now_button_id = 'coachEventNow'
    coach_later_button_id = 'coachEventLater'
    resolve_button_id = 'resolveEvent'
    confirm_button_xpath = '/html/body/ngb-modal-window[2]/div/div/action-modal' \
                           '/lytx-modal-shell/div/div[2]/div[2]/button[2]'

    # assign driver for fyi event
    kebab_button_xpath = '/html/body/app/shell/div/div/div/fyi-notify-task-card-list/task-card-list/div/' \
                         'div[3]/fyi-notify-card[1]/div/div[2]/event-task-content/div[1]/div/i'
    reassign_driver_xpath = '/html/body/app/shell/div/div/div/fyi-notify-task-card-list/task-card-list' \
                            '/div/div[3]/fyi-notify-card[1]/div/div[2]/event-task-content/div[1]/div/div' \
                            '/context-menu/div/ul/li[1]'
    search_driver_textbox_xpath = '/html/body/ngb-modal-window/div/div/assign-driver/lytx-modal-shell' \
                                  '/div/div[2]/div[2]/div/div/user-search/div/lytx-typeahead/div/input'
    select_searched_driver_xpath = '/html/body/ngb-modal-window/div/div/assign-driver/' \
                                   'lytx-modal-shell/div/div[2]/div[2]/div/div/user-search/' \
                                   'div/lytx-typeahead/div/ngb-typeahead-window/button'
    assign_button_xpath = '/html/body/ngb-modal-window/div/div/assign-driver/lytx-modal-shell' \
                          '/div/div[2]/div[3]/button[2]'
    fyi_task_count_xpath = '/html/body/app/shell/div/div/div/fyi-notify-task-card-list/' \
                           'task-card-list/div/div[1]/filter-bar/div/div[2]/div[1]/div[1]/div/div[1]/div'
