class LocatorsInspectionSchedules:
    inspection_schedules_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[1]'
    reports_count_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                                'lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/div[1]/' \
                                'vehicle-schedules-filter/lx-filter-bar/div/div/div[1]/div[1]/div/div[2]/span'
    vehicle_name_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                               'lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/div[2]/' \
                               'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[1]'
    vehicle_group_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                                'lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/div[2]/' \
                                'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[2]'
    status_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                         'lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/div[2]/' \
                         'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[3]'
    due_date_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                           'lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/div[2]/' \
                           'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[4]'
    inspection_list_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                                  'lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/div[2]/' \
                                  'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[5]'
    inspection_frequency_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                                       'lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/div[2]/' \
                                       'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[6]'
    last_inspected_date_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                                      'lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/div[2]/' \
                                      'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[7]'
    last_inspected_driver_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                                        'lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/div[2]/' \
                                        'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[8]'
    groups_filter_button_xpath = '//*[@id="vehicle_schedule_list-filter-multi-group-filter"]/div'
    search_group_textbox_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/multi-group-selector/' \
                                 'div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_group_filter_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/multi-group-selector/' \
                                       'div/div[1]/div[2]/div/lytx-typeahead/div/ngb-typeahead-window/button[1]'
    done_button_group_filter_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                     'multi-group-selector/div/div[3]/button[2]'
    inspection_list_filter_button_xpath = '//*[@id="vehicle_schedule_list-filter-multi-select-inspection_list"]/' \
                                          'div/div[1]/div/input'
    select_inspection_list_filter_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/' \
                                          'div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/' \
                                          'dvir-vehicle-schedules/div[1]/vehicle-schedules-filter/lx-filter-bar/' \
                                          'div/div/div[2]/multiselect-typeahead/div/div[1]/div/' \
                                          'multiselect-typeahead-window/button[4]'
    selected_inspection_list_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]' \
                                          '/lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/div[1]' \
                                          '/vehicle-schedules-filter/lx-filter-bar/div/div/div[2]/' \
                                          'multiselect-typeahead/div/div[1]/div/multiselect-typeahead-window/button[1]'
    close_vehicle_inspection_list_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                                          'lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/div[1]' \
                                          '/vehicle-schedules-filter/lx-filter-bar/div/div/div[2]/multiselect-typeahead/div/div[2]'
    status_filter_button_xpath = '//*[@id="vehicle_schedule_list-filter-multi-select-statuses"]/div/span'
    select_status_filter_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                                        'lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/' \
                                        'div[1]/vehicle-schedules-filter/lx-filter-bar/div/div/div[2]/' \
                                        'multiselect-dropdown/div/div/ul/li[2]/span/i'
    search_vehicle_name_textbox_xpath = '//*[@id="searchInput"]'
    reset_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                         'lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/div[1]/' \
                         'vehicle-schedules-filter/lx-filter-bar/div/div/div[2]/button'
    vehicle_group_first_row_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/' \
                                         'div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/' \
                                         'div[2]/lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[2]'
    status_first_row_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                                  'lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/div[2]/' \
                                  'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[3]'
    inspection_list_first_row_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/' \
                                           'div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/' \
                                           'dvir-vehicle-schedules/div[2]/lx-table/div[2]/div[2]/cdk-table/' \
                                           'cdk-row[1]/cdk-cell[5]'
    vehicle_name_first_row_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                                        'lytx-tab-views/div/div[2]/lytx-tab-view[1]/div/dvir-vehicle-schedules/div[2]/' \
                                        'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[1]'
    search_vehicle_name_icon_xpath = '//*[@id="vehicle_schedule_list-filter-search-input"]/div/span'
    download_csv_button_xpath = '//*[@id="csv_download-button"]'
    trailer_schedules_link_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                                   'lytx-tab-views/div/div[1]/button[2]/span'
    trailer_name_column_xpath = '//*[@id="sortableContainertrailerName"]/span[1]'
    trailer_group_column_xpath = '//*[@id="sortableContainertrailerGroup"]/span[1]'
    status_column_xpath = '//*[@id="sortableContainerstatus"]/span[1]'
    due_date_column_xpath = '//*[@id="sortableContainerdueDate"]/span[1]'
    inspection_list_column_xpath = '//*[@id="sortableContainerinspectionList"]/span[1]'
    inspection_frequency_column_xpath = '//*[@id="sortableContainerinspectionFrequency"]/span[1]'
    last_inspected_date_column_xpath = '//*[@id="sortableContainerlastinspectedDate"]/span[1]'
    last_inspected_driver_column_xpath = '//*[@id="sortableContainerlastinspectedDriver"]/span[1]'
    trailer_group_filter_button_xpath = '//*[@id="trailer_schedule_list-filter-multi-group-filter"]/div'
    trailer_search_group_filter_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                        'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    trailer_select_group_filter_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                        'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/' \
                                        'ngb-typeahead-window/button[1]'
    trailer_select_group_root_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                      'multi-group-selector/div/div[2]/div/div[2]/div[1]/div/div/span/i'
    trailer_group_done_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                      'multi-group-selector/div/div[3]/button[2]'
    trailer_inspection_list_filter_button_xpath = '//*[@id="trailer_schedule_list-filter-multi-select-inspection_list"]' \
                                                  '/div/div[1]/div/input'
    trailer_select_inspection_list_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/' \
                                                  'div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[2]/div/' \
                                                  'dvir-trailer-schedules/div[1]/trailer-schedules-filter/lx-filter-bar/' \
                                                  'div/div/div[2]/multiselect-typeahead/div/div[1]/div/' \
                                                  'multiselect-typeahead-window/button[6]/i'
    selected_trailer_inspection_list_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]' \
                                                  '/lytx-tab-views/div/div[2]/lytx-tab-view[2]/div/dvir-trailer-schedules/div[1]' \
                                                  '/trailer-schedules-filter/lx-filter-bar/div/div/div[2]/multiselect-typeahead' \
                                                  '/div/div[1]/div/multiselect-typeahead-window/button[1]'
    close_trailer_inspection_list_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/lytx-tab-views' \
                                          '/div/div[2]/lytx-tab-view[2]/div/dvir-trailer-schedules/div[1]/trailer-schedules-filter/lx-filter-bar/div/div/div[2]/multiselect-typeahead/div/div[2]'
    trailer_status_filter_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/lytx-tab-views' \
                                         '/div/div[2]/lytx-tab-view[2]/div/dvir-trailer-schedules/div[1]/trailer-schedules-filter/lx-filter-bar/div/div/div[2]/multiselect-dropdown/div/span/span'
    trailer_select_status_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/' \
                                         'div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[2]/div/dvir-trailer-schedules/' \
                                         'div[1]/trailer-schedules-filter/lx-filter-bar/div/div/div[2]/' \
                                         'multiselect-dropdown/div/div/ul/li[2]/span/i'
    search_trailer_name_filter_textbox_xpath = '//*[@id="searchInput"]'
    click_search_trailer_name_icon_xpath = '//*[@id="trailer_schedule_list-filter-search-input"]/div/span'
    trailer_reset_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                                 'lytx-tab-views/div/div[2]/lytx-tab-view[2]/div/dvir-trailer-schedules/div[1]/' \
                                 'trailer-schedules-filter/lx-filter-bar/div/div/div[2]/button'

    first_trailer_group_text_xpath = '//*[contains(@class, "cdk-column-Trailer-Group")]//*[text()=" ***Root "]'
    first_trailer_inspection_list_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/' \
                                               'div[2]/lytx-tab-views/div/div[2]/lytx-tab-view[2]/div/' \
                                               'dvir-trailer-schedules/div[2]/lx-table/div[2]/div[2]/cdk-table/' \
                                               'cdk-row[1]/cdk-cell[5]'
    first_trailer_status_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                                      'lytx-tab-views/div/div[2]/lytx-tab-view[2]/div/dvir-trailer-schedules/div[2]/' \
                                      'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[3]'
    first_trailer_name_text_stg_xpath = '//cdk-table/cdk-row[1]/cdk-cell[1]/span[2]'
    first_trailer_name_text_int_xpath = '// *[text()=" Test Alex3 "]'
    reports_trailer_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-schedules/div/div[2]/' \
                                  'lytx-tab-views/div/div[2]/lytx-tab-view[2]/div/dvir-trailer-schedules/div[1]/' \
                                  'trailer-schedules-filter/lx-filter-bar/div/div/div[1]/div[1]/div/div[2]/span'
