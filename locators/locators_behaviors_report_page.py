class LocatorsBehaviorsReportPage:
    # BehaviorPage
    behavior_tab_xpath = '//*[text()="Behavior"]'
    frequency_tab_xpath = '//*[text()="Frequency"]'
    trend_tab_xpath = '//*[text()="Trend"]'
    count_of_behavior = '//*[contains(@class, "count--value")]'
    total_count_load_xpath = '//*[@class="filter-header-bar__title__count--value--loading"]'

    # Filters
    filter_by_group_behave_button_xpath = '//*[@class="group-filter"]'
    search_by_group_behave_textbox_xpath = '//*[@placeholder="Search by Group"]'
    select_search_behave_button_xpath = ('/html/body/ngb-modal-window/div/div/group-selector-modal/group-selector/div'
                                         '/div[1]/div[2]/div/lytx-typeahead/div/ngb-typeahead-window/button[1]')
    done_behave_button_xpath = '//*[@class="group-selector-bottom-done lx-btn lx-btn-primary"]'

    # Date filter
    date_filter_behave_button_xpath = '//*[@class="lx-date-range-filter"]'
    from_date_behave_textbox_xpath = '(//*[contains(@class,"custom-day") and text()=" 9 "])[1]'
    end_date_behave_textbox_xpath = '(//*[contains(@class,"custom-day") and text()=" 9 "])[2]'
    apply_behave_button_xpath = '//*[@id="btn-apply"]'

    # NumBehavior
    num_of_behave_textbox_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                  '/div/filter-bar/div/div[2]/div[1]/div[1]/div/div[1]/div'

    # Link on report
    reset_button_xpath = '//*[@class="lx-btn lx-btn-text filter-header-bar__filters--reset"]'
    first_frequency_value_xpath = '(//*[@class="lx-link frequency"])[1]'
    driver_report_title_text_xpath = '//*[text()="DRIVERS REPORT"]'
