class LocatorsCoachesReport:
    # CoachesReportTable
    coaches_num_text_xpath = '//*[@class="filter-header-bar__title__count--value--success"]'
    coach_text_xpath = '//*[text()="Coach"]'
    coach_profile_title_text_xpath = '//h1[contains(text(), "Coach Profile")]'
    group_text_xpath = '//*[text()="Group"]'
    coaching_effectiveness_text_xpath = '//*[text()="Coaching Effectiveness"]'
    avg_days_to_coach_text_xpath = '//*[text()="Avg Days To Coach"]'
    coached_events_text_xpath = '//*[text()="Coached Events"]'
    with_notes_text_xpath = '//*[text()="With Notes"]'
    last_login_text_xpath = '//*[text()="Last Login"]'

    # CoachesReportFilters
    filter_by_group_coaches_button_xpath = '//*[@id="groupSelectorIcon"]'
    search_by_group_coaches_textbox_xpath = '/html/body/ngb-modal-window/div/div/' \
                                            'group-selector-modal/group-selector/div/div' \
                                            '[1]/div[2]/div/lytx-typeahead/div/input'
    select_search_by_group_coaches_button_xpath = '/html/body/ngb-modal-window/div/div/' \
                                                  'group-selector-modal/group-selector/' \
                                                  'div/div[1]/div[2]/div/lytx-typeahead/div/' \
                                                  'ngb-typeahead-window/button'
    done_search_by_group_coaches_button_xpath = '/html/body/ngb-modal-window/div/div/' \
                                                'group-selector-modal' \
                                                '/group-selector/div/div[3]/button[2]'

    filter_by_date_coaches_button_xpath = '//insights-date-filter/lx-date-range-filter/div/div[1]'
    from_date_coaches_button_xpath = '//ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/div[5]/div[4]/span/span'
    end_date_coaches_button_xpath = '//ngb-datepicker/div[2]/div[2]/ngb-datepicker-month/div[4]/div[4]/span/span'
    apply_filter_by_date_coaches_button_xpath = '//*[text()="Apply"]'

    coaches_by_activity_filter_button_xpath = '(//*[@class="dropdown__select__content"])[1]'
    select_coaches_by_activity_button_xpath = '//*[text()=" Coaches with Activity "]'

    group_data_only_coaches_button_xpath = '(//*[@class="dropdown__select__content"])[2]'
    select_group_data_button_xpath = '//*[text()=" Selected Group Data Only "]'

    # Links

    coach_link_text_xpath = '//cdk-table/cdk-row[1]/cdk-cell[1]/div/div/div/div'
    coach_profile_text_xpath = '//lx-section-header//span'

    # Reset
    reset_button_xpath = '//*[text()="Reset"]'
    coach_name_xpath = '/html/body/app/shell/div/div/div/coaches-report/lx-page-block/div/' \
                       'lx-generic-block/div/div/report-table/div/div/cdk-table/cdk-row/cdk-cell[1]/div/div/div/div'
    total_count_load_xpath = '//*[@class="filter-header-bar__title__count--value--success"]'
    first_coach_name_xpath = '(//*[contains(@class, "coach-name")])[1]'
    group_name_xpath = '(//*[@class="group-names"])[1]'
