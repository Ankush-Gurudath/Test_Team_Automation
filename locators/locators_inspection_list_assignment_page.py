class LocatorsInspectionListAssignmentPage:
    inspection_list_assignment_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/div'
    vehicle_count_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-filter-bar/' \
                                'filter-bar/div/div[1]/div[1]/div[1]/div/div[2]/span'
    vehicle_table_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-table/' \
                                'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[2]'
    group_table_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                              'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-table/' \
                              'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[3]'
    vehicle_type_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                               'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-table/' \
                               'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[4]'
    inspection_list_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                  'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-table/' \
                                  'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[5]'

    groups_filter_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                 'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-filter-bar/' \
                                 'filter-bar/div/div[1]/div[2]/multi-group-filter/div'
    search_group_filter_textbox_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                        'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_searched_group_filter_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                         'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/' \
                                         'ngb-typeahead-window/button[1]'
    group_filter_done_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                     'multi-group-selector/div/div[3]/button[2]'
    vehicle_type_filter_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                       'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-filter-bar/' \
                                       'filter-bar/div/div[1]/div[2]/multiselect-dropdown[1]/div/span'
    select_vehicle_type_filter_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                       'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-filter-bar/' \
                                       'filter-bar/div/div[1]/div[2]/multiselect-dropdown[1]/div/div/ul/li[1]'
    inspection_list_filter_button_xpath = '//span[contains(text(), " Inspection List ")]/parent::div/following-sibling::div'
    select_inspection_list_filter_xpath = '//*[text()="Default"]'
    search_vehicle_name_textbox_xpath = '//*[@id="searchInput"]'
    first_row_inspection_list_name_xpath = '(//*[text()=" Default "])[1]'
    search_vehicle_icon_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/dvir-assignments-vehicles/' \
                                'dvir-assignments-tab/dvir-assignments-filter-bar/filter-bar/div/div[1]/div[2]/' \
                                'lytx-search/div/span'
    reset_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/dvir-assignments-vehicles/' \
                         'dvir-assignments-tab/dvir-assignments-filter-bar/filter-bar/div/div[1]/div[2]/button'
    trailer_assignment_link_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                    'lytx-tab-views/div/div[1]/button[2]/span'
    trailers_count_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                'dvir-assignments-trailers/dvir-assignments-tab/dvir-assignments-filter-bar/' \
                                'filter-bar/div/div[1]/div[1]/div[1]/div/div[2]/span'
    trailer_column_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                 'dvir-assignments-trailers/dvir-assignments-tab/dvir-assignments-table/' \
                                 'lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[2]/span/span/span[1]'
    trailer_group_title_xpath = '//*[@id="sortableContainergroup"]/span[1]'
    trailer_type_title_xpath = '//*[@id="sortableContainertype"]/span[1]'
    trailer_inspection_list_title_xpath = '//*[@id="sortableContainerinspection"]/span[1]'
    group_filter_trailer_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                        'dvir-assignments-trailers/dvir-assignments-tab/dvir-assignments-filter-bar/' \
                                        'filter-bar/div/div[1]/div[2]/multi-group-filter/div'
    search_group_trailer_textbox_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                         'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_searched_group_filter_trailer_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                                 'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/' \
                                                 'ngb-typeahead-window/button[1]'
    deselect_sub_group_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                      'multi-group-selector/div/div[2]/div/div[2]/div[3]/div[1]/i'
    done_group_filter_trailer_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                             'multi-group-selector/div/div[3]/button[2]'
    trailer_assignment_type_filter_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                                  'dvir-assignments-trailers/dvir-assignments-tab/' \
                                                  'dvir-assignments-filter-bar/filter-bar/div/div[1]/div[2]/' \
                                                  'multiselect-dropdown[1]/div/span'
    select_trailer_assignment_type_filter_button = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                                   'dvir-assignments-trailers/dvir-assignments-tab/' \
                                                   'dvir-assignments-filter-bar/filter-bar/div/div[1]/div[2]/' \
                                                   'multiselect-dropdown[1]/div/div/ul/li[1]'
    selected_trailer_type_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                       'dvir-assignments-trailers/dvir-assignments-tab/' \
                                       'dvir-assignments-filter-bar/filter-bar/div/div[1]/div[2]/' \
                                       'multiselect-dropdown[1]/div/div/ul/li[1]'
    inspection_list_filter_trailer_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section' \
                                                  '/dvir-assignments-trailers/dvir-assignments-tab/dvir-assignments-filter-bar' \
                                                  '/filter-bar/div/div[1]/div[2]/multiselect-typeahead/div/div[1]/div/input'
    select_inspection_list_filter_trailer_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                                  'dvir-assignments-trailers/dvir-assignments-tab/' \
                                                  'dvir-assignments-filter-bar/filter-bar/div/div[1]/div[2]/' \
                                                  'multiselect-typeahead/div/div[1]/div/multiselect-typeahead-window/button[1]'
    close_inspection_list_filter_trailer_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                                 'dvir-assignments-trailers/dvir-assignments-tab/dvir-assignments-filter-bar' \
                                                 '/filter-bar/div/div[1]/div[2]/multiselect-typeahead/div/div[2]'
    selected_inspection_list_trailer_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/dvir-assignments-trailers' \
                                             '/dvir-assignments-tab/dvir-assignments-filter-bar/filter-bar/div/div[1]/div[2]' \
                                             '/multiselect-typeahead/div/div[1]/div/multiselect-typeahead-window/button[1]' \
                                             '/multiselect-highlight'
    search_trailer_name_textbox_xpath = '//*[@id="searchInput"]'
    search_trailer_icon_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/dvir-assignments-trailers/' \
                                'dvir-assignments-tab/dvir-assignments-filter-bar/filter-bar/div/div[1]/div[2]/' \
                                'lytx-search/div/span'
    reset_button_trailer_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                 'dvir-assignments-trailers/dvir-assignments-tab/dvir-assignments-filter-bar/' \
                                 'filter-bar/div/div[1]/div[2]/button'
    select_first_trailer_list_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                             'dvir-assignments-trailers/dvir-assignments-tab/dvir-assignments-table/' \
                                             'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[1]/div/div/i'
    select_second_trailer_list_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                              'dvir-assignments-trailers/dvir-assignments-tab/dvir-assignments-table/' \
                                              'lx-table/div[2]/div[2]/cdk-table/cdk-row[2]/cdk-cell[1]/div/div/i'
    set_trailer_inspection_list_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                               'dvir-assignments-trailers/dvir-assignments-tab/dvir-assignments-table/' \
                                               'lx-table/div[2]/div[1]/div/div[3]/button'
    select_default_set_inspection_list_button = '/html/body/ngb-modal-window/div/div/dvir-set-inspection-list/' \
                                                'lytx-modal-shell/div/div[2]/div[2]/div/div/div/div[1]/input'
    set_inspection_popup_button_xpath = '/html/body/ngb-modal-window/div/div/dvir-set-inspection-list/lytx-modal-shell' \
                                        '/div/div[2]/div[3]/button[2]'
    open_inspection_list_trailer_assignment_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section' \
                                                    '/dvir-assignments-trailers/dvir-assignments-tab/dvir-assignments-filter-bar' \
                                                    '/filter-bar/div/div[1]/div[2]/multiselect-typeahead/div/div[1]/div/input'
    first_inspection_list_trailer_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                               'dvir-assignments-trailers/dvir-assignments-tab/dvir-assignments-table/' \
                                               'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[5]/span[2]'
    second_inspection_list_trailer_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                                'dvir-assignments-trailers/dvir-assignments-tab/dvir-assignments-table/' \
                                                'lx-table/div[2]/div[2]/cdk-table/cdk-row[2]/cdk-cell[5]/span[2]'
    first_trailer_group_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/dvir-assignments-trailers/' \
                                     'dvir-assignments-tab/dvir-assignments-table/lx-table/div[2]/div[2]/cdk-table/' \
                                     'cdk-row[1]/cdk-cell[3]'
    first_trailer_type_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                    'dvir-assignments-trailers/dvir-assignments-tab/dvir-assignments-table/' \
                                    'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[4]'
    first_trailer_name_text_stg_xpath = '//cdk-table/cdk-row[1]/cdk-cell[2]/span[2]'
    first_trailer_name_text_int_xpath = '// *[text()=" Alex "]'
    first_vehicle_checkbox_xpath = '(//div[@class="checkbox"])[1]'
    second_vehicle_checkbox_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                    'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-table/' \
                                    'lx-table/div[2]/div[2]/cdk-table/cdk-row[2]/cdk-cell[1]/div/div/i'
    set_inspection_list_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                       'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-table/' \
                                       'lx-table/div[2]/div[1]/div/div[3]/button'
    set_inspection_default_checkbox_xpath = '/html/body/ngb-modal-window/div/div/dvir-set-inspection-list/' \
                                            'lytx-modal-shell/div/div[2]/div[2]/div/div/div/div[1]/input'
    set_button_popup_xpath = '/html/body/ngb-modal-window/div/div/dvir-set-inspection-list/lytx-modal-shell' \
                             '/div/div[2]/div[3]/button[2]'
    first_vehicle_inspection_list_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                          'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-table/' \
                                          'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[5]/span[2]'
    second_vehicle_inspection_list_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                           'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-table/' \
                                           'lx-table/div[2]/div[2]/cdk-table/cdk-row[2]/cdk-cell[5]/span[2]'
    vehicle_assignment_link_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/lytx-tab-views/' \
                                    'div/div[1]/button[1]/span'
    vehicle_set_inspection_button_xpath = '/html/body/ngb-modal-window/div/div/dvir-set-inspection-list/' \
                                          'lytx-modal-shell/div/div[2]/div[3]/button[2]'
    first_row_vehicle_group_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                         'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-table/' \
                                         'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[3]'
    first_row_vehicle_type_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                        'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-table/' \
                                        'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[4]'
    first_row_vehicle_name_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                        'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-table/' \
                                        'lx-table/div[2]/div[2]/cdk-table/cdk-row/cdk-cell[2]'
    first_row_inspection_list_text_xpath = '/html/body/app-root/shell/div/div/div/dvir-assignment/section/' \
                                           'dvir-assignments-vehicles/dvir-assignments-tab/dvir-assignments-table' \
                                           '/lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[5]/span[2]'
