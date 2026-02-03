class LocatorsDriversReportPage:
    # DriversScore

    driver_text_xpath = '//*[text()="Driver"]'
    group_text_xpath = '//*[text()="Group"]'
    coachable_score_text_xpath = '//*[contains(text(), "Coachable Score")]'
    coachable_events_text_xpath = '//*[contains(text(), "Coachable Events")]'
    total_score_text_xpath = '//*[contains(text(), "Total Score")]'
    total_events_text_xpath = '//*[contains(text(), "Total Events")]'
    driver_name_link_xpath = '(//*[contains(@class, "driver-name")])[1]'

    # Filtergroup

    filter_by_group_button_xpath = '//span[contains(text(), "Filter By Group")]'
    search_by_group_textbox_xpath = '//*[@placeholder="Search by Group"]'
    select_search_button_xpath = '//div/ngb-typeahead-window/button/div[1]/ngb-highlight'
    done_button_xpath = '//group-selector/div/div[3]/button[2]'

    # Filterdate

    date_filter_textbox_xpath = '//div[@class="lx-date-range-filter"]'
    from_date_textbox_xpath = '(//ngb-datepicker-month/div[3]/div[6]/span/span)[1]'
    end_date_textbox_xpath = '(//ngb-datepicker-month/div[4]/div[2]/span/span)[2]'
    apply_button_xpath = '//button[text()="Apply"]'

    # Filterbehavior
    behavior_textbox_xpath = '//*[@placeholder="Behaviors"]'
    select_behavior_dropdown_xpath = '//*[text()="Aggressive"]'
    close_behavior_list = '//behavior-selector/multiselect-typeahead/div/div[2]'

    # Searchdriverscore
    search_name_textbox_xpath = '//*[@placeholder="Search Name or ID"]'
    select_search_name_dropdown_xpath = '//*[@placeholder="Search Name or ID"]/parent::div//button'

    # reset
    reset_button_driver_score_xpath = '//div[text()="Reset"]'
    reset_button_xpath = '//*[text()="Reset"]'
    # Continualbehavior
    continual_behavior_link_xpath = '//*[text()="Continual Behaviors"]'
    driver_behave_text_xpath = '//*[text()="Driver"]'
    driver_name_behave_xpath = '(//*[contains(@class, "driver-name lx-link")])[1]'
    group_behave_text_xpath = '//*[text()="Group"]'
    continual_1st_behavior_xpath = '//*[text()=" Handheld Device "]'
    driver_behave_num_text_xpath = '/html/body/app/shell/div/div/div/' \
                                   'drivers-report/lx-page-container/div/div/lx-tabs/' \
                                   'driver-continual-behaviors-report' \
                                   '/div[1]/lx-filter-bar/div/div/div[1]/div[1]/div/div[1]/div'

    # Driverprofile
    driver_link_text_xpath = '(//*[contains(@class, "driver-name")])[1]'
    driver_profile_text_xpath = '(//*[contains(@class, "driver-info__header")])[1]'

    # Continualbehaviorfilters
    filter_group_behave_button_xpath = '//span[contains(text(), "Filter By Group")]'
    search_filter_group_behave_textbox_xpath = '/html/body/ngb-modal-window/div/div/' \
                                               'group-selector-modal/group-selector/div/div[1]' \
                                               '/div[2]/div/lytx-typeahead/div/input'
    select_search_filter_behave_button_xpath = '/html/body/ngb-modal-window/div/div/' \
                                               'group-selector-modal/group-selector/div' \
                                               '/div[1]/div[2]/div/lytx-typeahead' \
                                               '/div/ngb-typeahead-window/button'
    done_search_filter_behave_button_xpath = '/html/body/ngb-modal-window/div/div/' \
                                             'group-selector-modal/group-selector' \
                                             '/div/div[3]/button[2]'

    # datefilterbehave
    date_filter_behave_button_xpath = '//insights-date-filter/lx-date-range-filter/div/div[1]'
    from_date_filter_behave_button_xpath = '//insights-date-filter/lx-date-range-filter/div/div[2]/lx-date-range-selector/div/div[2]/div[2]/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div[3]/div[4]/span/span'
    end_date_filter_behave_button_xpath = '//insights-date-filter/lx-date-range-filter/div/div[2]/lx-date-range-selector/div/div[2]/div[2]/ngb-datepicker/div[2]/div[2]/ngb-datepicker-month/div[3]/div[2]/span/span'
    date_behave_apply_button_xpath = '//*[text()="Apply"]'

    # SearchNamebehave
    search_name_behave_textbox_xpath = '//*[@placeholder="Search Name or ID"]'
    select_search_behave_button_xpath = '//user-search/div/lytx-typeahead/div/ngb-typeahead-window/button[1]'

    # Alert link
    alert_link_text_xpath = '//*[text()="Alerts"]'
    driver_alert_text_xpath = '//*[text()="Driver"]'
    group_alert_text_xpath = '//*[text()="Group"]'
    total_alerts_text_xpath = '//*[text()=" Total Alerts "]'
    handheld_alert_text_xpath = '//*[text()=" Handheld Device "]'
    inattentive_alert_text_xpath = '//*[text()=" Inattentive "]'
    food_or_drink_alert_text_xpath = '//*[text()=" Food or Drink "]'
    driver_smoking_alert_text_xpath = '//*[text()=" Driver Smoking "]'
    policy_speed_alert_text_xpath = '//*[text()=" Policy Speed "]'
    posted_speed_alert_text_xpath = '//*[text()=" Posted Speed "]'
    no_seat_belt_alert_text_xpath = '//*[text()=" No Seat Belt "]'
    lensobst_alert_text_xpath = '//*[text()=" Lens Obstruction "]'
    lane_depart_alert_text_xpath = '//*[text()=" Lane Departure "]'
    rolling_alert_text_xpath = '//*[text()=" Rolling Stop "]'
    following_distance_alert_text_xpath = '//*[text()=" Following Distance "]'
    critical_distance_alert_text_xpath = '//*[text()=" Critical Distance "]'

    num_driver_alert_text_xpath = '/html/body/app/shell/div/div/div/drivers-report/' \
                                  'lx-page-container/div/div/lx-tabs/driver-alerts-report' \
                                  '/div[1]/lx-filter-bar/div/div/div[1]/div[1]/div/div[1]/div'

    # Filtergroupalert
    filter_group_alert_button_xpath = '//*[contains(text(), "Filter By Group")]'
    search_filter_group_alert_textbox_xpath = '/html/body/ngb-modal-window/div/div/' \
                                              'group-selector-modal/group-selector/' \
                                              'div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_search_filter_group_alert_button_xpath = '/html/body/ngb-modal-window/div/div/' \
                                                    'group-selector-modal/group-selector/' \
                                                    'div/div[1]/div[2]/div/lytx-typeahead/' \
                                                    'div/ngb-typeahead-window/button'
    done_button_alert_button_xpath = '/html/body/ngb-modal-window/div/div/' \
                                     'group-selector-modal/group-selector/div/div[3]/button[2]'

    # Datefilteralert
    date_filter_alert_textbox_xpath = '//insights-date-filter/lx-date-range-filter/div/div[1]'
    from_date_alert_textbox_xpath = '//insights-date-filter' \
                                    '/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                                    '/div/div[2]/div[2]/ngb-datepicker/div[2]/div[1]/' \
                                    'ngb-datepicker-month/div[4]/div[5]/span/span'
    end_date_alert_textbox_xpath = '//insights-date-filter' \
                                   '/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                                   '/div/div[2]/div[2]/ngb-datepicker/div[2]/div[2]/' \
                                   'ngb-datepicker-month/div[4]/div[4]/span/span'
    apply_date_alert_button_xpath = '//*[text()="Apply"]'

    # Behaviorfilteralert
    behavior_alert_textbox_xpath = '//*[@placeholder="Behaviors"]'
    select_behavior_alert_button_xpath = '//*[text()="Critical Distance"]'

    search_name_alert_textbox_xpath = '//*[@placeholder="Search Name or ID"]'
    select_search_name_alert_button_xpath = '//user-search/div/lytx-typeahead/div/ngb-typeahead-window/button[1]'

    # ResetAlert
    reset_button_alert_xpath = '//driver-alerts-report/div[1]/lx-filter-bar/div/div/div[2]/button'
    # Driverprofile
    driver_link_alert_text_xpath = '//cdk-table/cdk-row[1]/cdk-cell[1]/div/div/div/div'
    driver_profile_alert_text_xpath = '//*[@class="driver-info__header"]'

    # LinkinDriverScores
    driver_score_link_text_xpath = '//cdk-table/cdk-row[1]/cdk-cell[1]/div/div/div/div'
    driver_score_profile_text_xpath = '//*[@class="lx-section-header__text--bold"]'
    total_count = '(//*[contains(text(), "Driver")]/parent::div/preceding-sibling::div/div)[1]'
    total_count_load = '//*[@class="filter-header-bar__title__count--value--loading"]'
    first_group_name_xpath = '//span[@class="groups"]'
    close_behavior_alert_list = '//alert-selector/multiselect-typeahead/div/div[2]'
    length_of_columns_xpath = '//cdk-row[1]/cdk-cell'
    download_button_xpath = '//*[@class="dropdown__select__content"]'
    driver_event_history_csv_xpath = '//*[@class="download-csv"]'
    driver_event_history_report_xpath = '//*[text()=" Driver Event History (PDF) "]'
    continual_behave_tab_in_driver_profile_xpath = '//*[@class="continual_behaviors"]'
    browse_or_wake_link_xpath = '//*[@class="vehicle-actions__list__main"]'
    event_dates_xpath = '//cdk-row//cdk-cell[5]//span[2]/div'
    event_id_text_xpath = '//*[text()=" Event ID "]'
