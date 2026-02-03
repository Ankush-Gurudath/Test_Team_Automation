class LocatorsDriverVehicleInspectionReportsPage:
    # DRIVER VEHICLE INSPECTION REPORTS

    total_reports_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-list/section/div[2]/dvir-list-filter/' \
                               'lx-filter-bar/div/div/div[1]/div[1]/div/div[2]/span'
    loading_icon_xpath = '//*[@data-test-id="filterHeaderBar-titleCountValue-loading"]'
    top_total_count_reports_xpath = '/html/body/app-root/shell/div/div/div/dvir-list/section/div[2]/dvir-list-filter' \
                                    '/lx-filter-bar/div/div/div[1]/div[1]/div/div[1]/div'
    total_reports_page_count_xpath = '/html/body/app-root/shell/div/div/div/dvir-list/section/div[3]/persist-pagination/div/' \
                                     'paginator/div/div[3]/div[2]/button'
    select_group_filter_text_xpath = '//*[@id="dvir-list-filter-group"]/div'
    select_date_range_text_xpath = '//*[@id="dvir-list-filter-date-picker-range"]/div/div[1]'
    statuses_filter_text_xpath = '//*[@id="dvir-list-filter-multi-select-statuses"]/div/span/span'
    defects_filter_text_xpath = '//*[@id="dvir-list-filter-multi-select-defect-type"]/div/div[1]/div/input'
    close_icon_defect_filter_xpath = '/html/body/app-root/shell/div/div/div/dvir-list/section/div[2]' \
                                     '/dvir-list-filter/lx-filter-bar/div/div/div[2]/multiselect-typeahead/div/div[2]'
    select_search_filter_text_xpath = '//*[@id="dvir-list-filter-dropdown-search-criteria"]/div/span/span'
    select_search_criteria_filter_text_xpath = '//*[@id="dvir-list-filter-dropdown-search-criteria"]/div/span'
    search_criteria_filter_textbox_xpath = '/html/body/app-root/shell/div/div/div/dvir-list/section/div[2]/' \
                                           'dvir-list-filter/lx-filter-bar/div/div/div[2]/div/lytx-search/' \
                                           'div/form/input'
    reset_button_text_xpath = '//*[@class="reset-button-text"]'
    report_Id_text_xpath = '//*[@id="sortableContaineruniqueName"]/span[1]'
    type_text_xpath = '//*[@id="sortableContainerinspectionType"]'
    status_text_xpath = '//*[@id="sortableContainerinspectionStatus"]/span[1]'
    report_date_text_xpath = '//*[@id="sortableContainercreationDate"]/span[1]'
    duration_text_xpath = '//*[@id="sortableContainerelapsedTime"]'
    driver_text_xpath = '//*[@id="sortableContainerdriverName"]/span[1]'
    vehicle_text_xpath = '//*[@id="sortableContainervehicleName"]/span[1]'
    major_vehicle_defects_text_xpath = '//*[@id="sortableContainervehicleMajorDefects"]/span[1]'
    minor_vehicle_defects_text_xpath = '//*[@id="sortableContainervehicleMinorDefects"]/span[1]'
    vehicle_inspection_list_text_xpath = '//*[@id="sortableContainerinspectionListVehicle"]/span[1]'
    trailer_text_xpath = '//*[@id="sortableContainertrailerName"]/span[1]'
    major_trailers_defects_text_xpath = '//*[@id="sortableContainertrailerMajorDefects"]/span[1]'
    minor_trailers_defects_text_xpath = '//*[@id="sortableContainertrailerMinorDefects"]/span[1]'
    trailer_inspection_list_text_xpath = '//*[@id="sortableContainerinspectionListTrailer"]/span[1]'
    mechanic_agent_text_xpath = '//*[@id="sortableContainerreviewerName"]/span[1]'
    reviewer_text_xpath = '//*[@id="sortableContainerapproverName"]/span[1]'

    status_filter_dropdown_xpath = '/html/body/app-root/shell/div/div/div/dvir-list/section/div[2]/dvir-list-filter/' \
                                   'lx-filter-bar/div/div/div[2]/multiselect-dropdown/div/div/ul/li[1]/span/i'
    select_date_filter_date1_xpath = '/html/body/app-root/shell/div/div/div/dvir-list/section/div[2]/dvir-list-filter/' \
                                     'lx-filter-bar/div/div/div[2]/lx-date-range-filter/div/div[2]/' \
                                     'lx-date-range-selector/div/div[2]/div[2]/ngb-datepicker/div[2]/' \
                                     'div[1]/ngb-datepicker-month/div[3]/div[4]/span/span'
    select_date_filter_date2_xpath = '/html/body/app-root/shell/div/div/div/dvir-list/section/div[2]/dvir-list-filter' \
                                     '/lx-filter-bar/div/div/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector' \
                                     '/div/div[2]/div[2]/ngb-datepicker/div[2]/div[1]/ngb-datepicker-month/' \
                                     'div[6]/div[2]/span/span'
    current_month_year_xpath = '/html/body/app-root/shell/div/div/div/dvir-list/section/div[2]/dvir-list-filter/lx-filter-bar' \
                               '/div/div/div[2]/lx-date-range-filter/div/div[2]/lx-date-range-selector/div/div[2]/div[2]' \
                               '/ngb-datepicker/div[2]/div[2]/div'
    current_day_class = 'custom-day.start-date.end-date.today'
    date_filter_apply_button_xpath = '//*[@id="btn-apply"]'
    search_group_textbox_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/multi-group-selector/' \
                                 'div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_searched_group_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/multi-group-selector/' \
                                  'div/div[1]/div[2]/div/lytx-typeahead/div/ngb-typeahead-window/button[1]'
    group_filter_done_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                     'multi-group-selector/div/div[3]/button[2]'
    defects_filter_xpath = '//*[@id="dvir-list-filter-multi-select-defect-type"]/div/div[1]/div/input'
    select_defect_filter_dropdown_xpath = '/html/body/app-root/shell/div/div/div/dvir-list/section/div[2]/' \
                                          'dvir-list-filter/lx-filter-bar/div/div/div[2]/multiselect-typeahead/' \
                                          'div/div[1]/div/multiselect-typeahead-window/button[2]'
    select_search_dropdown_xpath = '/html/body/app-root/shell/div/div/div/dvir-list/section/div[2]/dvir-list-filter/' \
                                   'lx-filter-bar/div/div/div[2]/dropdown/div/div/ul/li[1]'
    list_settings_tab_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[3]'
    list_setting_tab_existing_user_xpath = '//*[contains(text(), "List Settings")]'
    list_management_tab_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[3]/div[2]/div[2]/div[1]'
    list_management_tab_existing_user_xpath = '//*[contains(text(), " List Management")]'
    list_assignment_tab_xpath = '//*[contains(text(), " List Assignment")]'
    download_csv_button_xpath = '//*[contains(text(), " Download CSV ")]'
    schedules_tab_xpath = '//*[contains(text(), "Schedules")]'
    list_assignment_tab_existing_user_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/' \
                                              'div[3]/div[2]/div[2]/div[2]'
    list_assignment_tab_existing_user_new_ui_xpath = '(//span[contains(text(),"List Assignment")])'
    first_report_id_link_xpath = '/html/body/app-root/shell/div/div/div/dvir-list/section/div[3]/dvir-list-table/' \
                                 'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[1]/span[2]/span'
    dvir_tab_xpath = '//*[contains(text(), "DVIR") and @class="menu-text"]'
    dvir_tab_new_ui_xpath = '//span[contains(text(), "DVIR")]'
    select_search_dropdown_report_id_xpath = '//*[@id="dvir-list-filter-dropdown-search-criteria"]/div/div/ul/li[4]'
    first_report_id_searched_xpath = '//cdk-table/cdk-row/cdk-cell[1]/span[2]'
    first_row_status_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-list/section/div[3]/dvir-list-table/' \
                                  'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[3]/span[2]'
    first_row_driver_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-list/section/div[3]/dvir-list-table/' \
                                  'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[6]'