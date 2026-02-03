class LocatorsLicenseManagement:
    licensing_button_xpath = '/html/body/app-root/shell/div/div/navigation/div[1]/div[8]'
    license_count_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]' \
                          '/filter-bar/div/div[2]/div[1]/div[1]/div/div[1]/div'
    license_column_id = 'sortableContainerLicenseSerialNumber'
    services_column_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[3]/lx-table/div[2]/div[2]/cdk-table/cdk-header-row/cdk-header-cell[2]/span/span'
    cost_center_column_id = 'sortableContainerCostCenter'
    group_column_id = 'sortableContainerGroupName'
    vehicle_column_id = 'sortableContainerVehicleName'
    device_column_id = 'sortableContainerDeviceSerialNumber'
    license_status_column_id = 'sortableContainerStatus'
    device_licenses_label_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[2]/div[1]/license-summary-widget/div/div[1]'
    device_services_activation_label_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[2]/div[2]/license-summary-widget/div/div'
    devices_activated_label_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[2]/div[1]/license-summary-widget/div/div[2]/div[1]/span[1]'
    licenses_assigned_activated_label_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[2]/div[1]/license-summary-widget/div/div[3]/div[1]/span[1]'
    license_management_title_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]/filter-bar/div/div[1]/span[1]'

    # Filter
    group_filter_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]/filter-bar/' \
                         'div/div[2]/div[2]/multi-group-filter/div/span'
    search_group_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/multi-group-selector/' \
                         'div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_searched_group_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                  'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/' \
                                  'ngb-typeahead-window/button[1]'
    done_button_group_filter_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                     'multi-group-selector/div/div[3]/button[2]'
    service_filter_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]/filter-bar' \
                           '/div/div[2]/div[2]/multiselect-typeahead[1]/div/div[1]/div/input'
    select_driver_safety_service_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]/filter-bar' \
                                         '/div/div[2]/div[2]/multiselect-typeahead[1]/div/div[1]/div/' \
                                         'multiselect-typeahead-window/button[1]'
    arrow_icon_service_filter_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]/filter-bar/' \
                                      'div/div[2]/div[2]/multiselect-typeahead[1]/div/div[2]'
    select_device_type_filter_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]/filter-bar/' \
                                      'div/div[2]/div[2]/multiselect-typeahead[2]/div/div[1]/div/input'
    select_DC2_device_type_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]/filter-bar/div/div[2]' \
                                   '/div[2]/multiselect-typeahead[2]/div/div[1]/div/multiselect-typeahead-window/button[1]'
    arrow_icon_device_type_filter_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]/' \
                                          'filter-bar/div/div[2]/div[2]/multiselect-typeahead[2]/div/div[2]'
    select_license_status_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]/' \
                                  'filter-bar/div/div[2]/div[2]/dropdown[1]/div/span/span'
    select_assigned_status_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]/filter-bar/' \
                                   'div/div[2]/div[2]/dropdown[1]/div/div/ul/li[1]'
    reset_button_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]/' \
                         'filter-bar/div/div[2]/div[2]/button'
    select_search_filter_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]/' \
                                 'filter-bar/div/div[2]/div[2]/dropdown[2]/div/span/span'
    select_device_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]/' \
                          'filter-bar/div/div[2]/div[2]/dropdown[2]/div/div/ul/li[1]'
    select_license_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]' \
                           '/filter-bar/div/div[2]/div[2]/dropdown[2]/div/div/ul/li[2]'
    select_vehicle_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]' \
                           '/filter-bar/div/div[2]/div[2]/dropdown[2]/div/div/ul/li[3]'
    search_criteria_input_xpath = '/html/body/app-root/shell/div/div/div/license-list/div/div[1]' \
                                  '/filter-bar/div/div[2]/div[2]/div/div/lytx-search/div/form/input'
