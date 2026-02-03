class LocatorsEvents:
    # SelectSearch
    select_search_filter_css = '#event-list-search-criteria > div > span'
    event_id_select_filter_xpath = '//dropdown[2]/div/div/ul/li[1]'
    search_by_id_tab_css = '#searchInput'
    search_button_xpath = '//*[@id="eventId-search-criteria"]/div/span'

    # Events
    first_event_tab_xpath = '//span[@data-test-id="video-preview-span"]'
    second_event_tab_css = 'body > app > shell > div > div > div ' \
                           '> ng-component > lx-page-container > ' \
                           'div > div > lx-table > div.lx-table__table' \
                           ' > div.lx-table__table__main > cdk-table > ' \
                           'cdk-row:nth-child(3) > cdk-cell.cdk-cell.' \
                           'lytx-table-cell.cdk-column-Event-ID > ' \
                           'span.cell-value > event-preview-link > span'
    first_event_date_xpath = '/html/body/app/shell/div/div/div/ng-component/lx-page-container/' \
                             'div/div/lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[7]'
    first_event_date_new_UI_xpath = '//*[contains(@class, "record-date")]'
    overlay_toggle_xpath = '//lytx-slide-toggle'
    overlay_toggle_hover_xpath = '//ngb-tooltip-window'
    overlay_label_xpath = '//*[contains(@class, "overlay-toggle ")]'
    download_option_mp4_with_overlay_xpath = '//context-menu//li[2]'

    # More Actions
    more_actions_tab_xpath = '/html/body/ngb-modal-window/div/div/event-preview/' \
                             'div/div[2]/div[2]/action-bar/div[1]/div[4]/span'
    reassign_driver_select_xpath = '/html/body/ngb-modal-window/div/div/event-preview' \
                                   '/div/div[2]/div[2]/action-bar/div[1]/div[3]' \
                                   '/div/div/context-menu/div/ul/li[1]/span'
    mark_as_f2f_coaching_xpath = '/html/body/ngb-modal-window/div/div/event-preview' \
                                 '/div/div[2]/div[2]/action-bar/div[1]/div[4]/' \
                                 'div/div/context-menu/div/ul/li[3]/span'
    yes_confirm_button_xpath = '/html/body/ngb-modal-window[2]/div/div/action-modal' \
                               '/lytx-modal-shell/div/div[2]/div[2]/button[2]'

    # AssignDriver
    assign_driver_search_xpath = '/html/body/ngb-modal-window[2]/div/div/assign-driver' \
                                 '/lytx-modal-shell/div/div[2]/div[2]/div/div/user-search' \
                                 '/div/lytx-typeahead/div/input'
    select_assigned_driver_xpath = '/html/body/ngb-modal-window[2]/div/div/assign-driver' \
                                   '/lytx-modal-shell/div/div[2]/div[2]/div/div/user-search' \
                                   '/div/lytx-typeahead/div/ngb-typeahead-window/button'
    assign_button_xpath = '/html/body/ngb-modal-window[2]/div/div/assign-driver/' \
                          'lytx-modal-shell/div/div[2]/div[3]/button[2]'

    # closevideo
    close_video_xpath = '/html/body/ngb-modal-window/div/div/event-preview/div/div[1]/i'

    # Driver
    driver_link_xpath = '/html/body/app/shell/div/div/div/ng-component/' \
                        'lx-page-container/div/div/lx-table/div[2]/div[2]' \
                        '/cdk-table/cdk-row[1]/cdk-cell[3]/span[2]/span'
    event_status_self_coaching_text_xpath = '/html/body/app/shell/div/div/div/ng-component/' \
                                            'lx-page-container/div/div/lx-table/div[2]/div[2]/' \
                                            'cdk-table/cdk-row[2]/cdk-cell[9]/span[2]/span'
    event_status_resolved_text_xpath = '/html/body/app/shell/div/div/div/ng-component/' \
                                       'lx-page-container/div/div/lx-table/div[2]/div[2]/' \
                                       'cdk-table/cdk-row[1]/cdk-cell[9]/span[2]/span'
