class LocatorsOpenTasksReport:
    # OpenTasksReportLocators
    filter_group_button_xpath = '//*[@class="group-filter"]'
    search_by_group_box_xpath = '//*[@placeholder="Search by Group"]'
    select_group_search_xpath = '(//*[@class="dropdown-item__top"])[1]'
    done_button_xpath = '//*[@class="group-selector-bottom-done lx-btn lx-btn-primary"]'

    search_name_box_xpath = '//*[@placeholder="Search Name or ID"]'
    select_name_search_xpath = '//*[contains(@class,"dropdown-item")]'

    driver_text_xpath = '//*[text()="Driver"]'
    driver_group_text_xpath = '//*[contains(text(), "s Group")]'
    face_to_face_text_xpath = '//*[text()=" Face-to-face "]'
    face_to_face_overdue_text_xpath = '//*[text()=" Face-to-face (Overdue) "]'
    fyi_notify_text_xpath = '//*[text()=" FYI Notify "]'

    reset_link_xpath = '//*[@class="lx-btn lx-btn-text filter-header-bar__filters--reset"]'

    driver_link_xpath = '//cdk-table/cdk-row[1]/cdk-cell[1]/div/div/div/div'
    event_link_xpath = '//cdk-table/cdk-row[1]/cdk-cell[3]/div/div[1]/div/div/span'

    driver_number_text_xpath = '/html/body/app/shell/div/div/div/open-tasks-report' \
                               '/div/filter-bar/div/div[2]/div[1]/div[1]/div/div[1]/div'

    driver_profile_text_xpath = '/html/body/app/shell/div/div/div/ng-component' \
                                '/div/div[2]/driver-info/lx-section/section' \
                                '/div[1]/lx-section-header/div/span'
    event_profile_text_xpath = '//*[text()="Events"]'
    xml_value_attribute = 'value'
    total_count = '//*[@class="filter-header-bar__title__count--value--success"]'
    paginator_count = '//div[@class="paginator__count"]'
