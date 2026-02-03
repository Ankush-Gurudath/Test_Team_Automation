class LocatorsGroupReportPage:
    # SubgroupsNumber

    subgroups_text_xpath = '//*[@class="filter-header-bar__title__count--value--success"]'
    total_count_load = '//*[@class="filter-header-bar__title__count--value--loading"]'

    # Table columns

    group_text_xpath = '//*[text()="Group"]'
    num_of_vehicles_text_xpath = '//*[text()="# of vehicles"]'
    coachable_score_text_xpath = '//*[text()=" Coachable Score "]'
    coachable_events_text_xpath = '//*[text()=" Coachable Events "]'

    # FiltersByGroup

    group_by_filter_tab_xpath = '//*[contains(text(),"Filter By Group")]'
    search_group_by_filter_textbox_xpath = '/html/body/ngb-modal-window/div/div/' \
                                           'group-selector-modal/group-selector/div/div[1]' \
                                           '/div[2]/div/lytx-typeahead/div/input'
    select_search_group_by_filter_button_xpath = ('/html/body/ngb-modal-window/div/div/group-selector-modal/group'
                                                  '-selector/div/div[1]/div['
                                                  '2]/div/lytx-typeahead/div/ngb-typeahead-window/button[1]')
    done_filter_button_xpath = '/html/body/ngb-modal-window/div/div/' \
                               'group-selector-modal/group-selector/div/div[3]/button[2]'

    # FiltersByDate
    date_filter_tab_xpath = '//insights-date-filter/lx-date-range-filter/div/div[1]'
    from_date_filter_button_xpath = '//ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div[4]/div[4]/span/span'
    end_date_filter_button_xpath = '//ngb-datepicker/div[2]/div[2]/ngb-datepicker-month/div[4]/div[2]/span/span'
    apply_filter_button_xpath = '//*[text()="Apply"]'

    # BehaviorFilter
    behavior_filter_button_xpath = '//*[@id="group-report-behavior-filter"]'
    select_group_behavior_button_xpath = '//*[text()="Aggressive"]'

    # NormalizedFilter
    normalized_filter_button_xpath = '//*[@id="normalized-by-vehicle"]/div/span/span'
    select_normalized_filter_dropdown_xpath = '//*[text()=" Normalized by # of Vehicles "]'

    # Links
    group_link_textbox_xpath = '(//*[contains(@class, "lx-link sortable group-name")])[1]'

    drivers_report_page_link_textbox_xpath = '//*[text()="DRIVERS REPORT"]'

    reset_button_xpath = '//*[text()="Reset"]'
    first_group_name_xpath = '(//cdk-row/cdk-cell[1]/div/div/div)[1]'
    close_behavior_filter_xpath = '//behavior-selector/multiselect-typeahead/div/div[2]'
    group_coachable_events_count_xpath = '//cdk-table/cdk-row[7]/cdk-cell[4]/div/div[1]/div/span'
    events_count_in_events_page_xpath = '//*[@data-test-id="filter-bar-count"]'
