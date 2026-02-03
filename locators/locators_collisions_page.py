class LocatorsCollisions:
    filter_by_group_button_xpath = '/html/body/app/shell/div/div/div/collision-task-card-list/' \
                                   'task-card-list/div/div[1]/filter-bar/div/div[2]/div[2]/group-filter/div'
    search_by_group_textbox_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal/group-selector/' \
                                    'div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_search_by_group_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal/group-selector/' \
                                   'div/div[1]/div[2]/div/lytx-typeahead/div/ngb-typeahead-window/button'
    done_filter_by_group_button_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal/' \
                                        'group-selector/div/div[3]/button[2]'
    reset_button_xpath = '/html/body/app/shell/div/div/div/collision-task-card-list/task-card-list/' \
                         'div/div[1]/filter-bar/div/div[2]/div[2]/button/div'
    search_driver_name_text_box_xpath = '//*[@id="searchInput"]'
    collision_tasks_text_xpath = '/html/body/app/shell/div/div/div/collision-task-card-list/' \
                                 'task-card-list/div/div[3]/span'

    # view collision task
    task_count_xpath = '/html/body/app/shell/div/div/div/collision-task-card-list/task-card-list/' \
                       'div/div[1]/filter-bar/div/div[2]/div[1]/div[1]/div/div[1]/div'
    driver_name_text_xpath = '/html/body/app-root/shell/div/div/div/collision-task-card-list/task-card-list/div/div[3]/collision-task-card[1]/div/div[2]/event-task-content/div[1]/span/span'
    driver_name_on_task_card_xpath = '//*[@data-test-id="driverProfileLink-ltcList-text"]'
    group_text_xpath = '/html/body/app/shell/div/div/div/collision-task-card-list/task-card-list/' \
                       'div/div[3]/collision-task-card[1]/div/div[2]/event-task-content/div[2]/div[1]/span[1]'
    group_text_id = 'group-label'
    vehicle_text_id = 'vehicle-label'
    date_text_id = 'date-label'
    time_text_id = 'time-label'
    overdue_text_id = 'overdue-label'
    preview_card_xpath = '//*[@class="ltc-list__item__content__footer__btn__text"]'

    vehicle_text_xpath = '/html/body/app/shell/div/div/div/collision-task-card-list/task-card-list' \
                         '/div/div[3]/collision-task-card[1]/div/div[2]/event-task-content/div[2]/div[1]/span[2]'
    event_date_text_xpath = '/html/body/app/shell/div/div/div/collision-task-card-list/task-card-list' \
                            '/div/div[3]/collision-task-card[1]/div/div[2]/event-task-content/div[3]/div[1]/span[1]'
    time_text_xpath = '/html/body/app/shell/div/div/div/collision-task-card-list/task-card-list/div/div[3]/' \
                      'collision-task-card[1]/div/div[2]/event-task-content/div[3]/div[1]/span[2]'
    preview_button_text_xpath = '/html/body/app/shell/div/div/div/collision-task-card-list/task-card-list' \
                                '/div/div[3]/collision-task-card[1]/div/div[2]/div/button'
    group_name_xpath = '/html/body/app/shell/div/div/div/collision-task-card-list/task-card-list' \
                       '/div/div[3]/collision-task-card[1]/div/div[2]/event-task-content/div[2]/div[2]/span[1]'

    resolved_button_id = 'resolveEvent'
    coach_later_button_id = 'coachEventLater'
    confirm_button_xpath = '/html/body/ngb-modal-window[2]/div/div/action-modal/lytx-modal-shell/div/div[2]/div[2]/button[2]'
    coach_now_button_id = 'coachEventNow'

    no_not_a_collision_button_xpath = '/html/body/ngb-modal-window/div/div/event-preview/div/event-actions/div/div[2]/button[1]'
    yes_for_possible_collision_button_xpath = '/html/body/ngb-modal-window/div/div/event-preview/div/event-actions/div/div[2]/button[2]'
    close_icon_xpath = '/html/body/ngb-modal-window/div/div/event-preview/div/div[1]/i'

    kebab_button_xpath = '/html/body/app/shell/div/div/div/collision-task-card-list/task-card-list/' \
                         'div/div[3]/collision-task-card/div/div[2]/event-task-content/div[1]/div/i'
    reassign_driver_xpath = '/html/body/app/shell/div/div/div/collision-task-card-list/' \
                            'task-card-list/div/div[3]/collision-task-card[1]/div/div[2]/' \
                            'event-task-content/div[1]/div/div/context-menu/div/ul/li[1]'
    search_driver_textbox_xpath = '/html/body/ngb-modal-window/div/div/assign-driver/' \
                                  'lytx-modal-shell/div/div[2]/div[2]/div/div/user-search/' \
                                  'div/lytx-typeahead/div/input'
    select_searched_driver_xpath = '/html/body/ngb-modal-window/div/div/assign-driver/' \
                                   'lytx-modal-shell/div/div[2]/div[2]/div/div/user-search/' \
                                   'div/lytx-typeahead/div/ngb-typeahead-window/button'
    assign_button_xpath = '/html/body/ngb-modal-window/div/div/assign-driver/lytx-modal-shell' \
                          '/div/div[2]/div[3]/button[2]'
