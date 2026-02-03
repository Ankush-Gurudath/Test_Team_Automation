class LocatorsDeviceHealth:
    device_count_xpath = '//span[contains(text()," Device")]/parent::div/preceding-sibling::div/div'
    device_label_xpath = '//cdk-header-cell//*[text()=" Device "]'
    device_type_label_xpath = '//cdk-header-cell//*[text()=" Device Type "]'
    vehicle_label_xpath = '//cdk-header-cell//*[text()=" Vehicle "]'
    overdue_for_check_in_label_xpath = '//cdk-header-cell//*[text()=" Overdue for Check-in "]'
    power_disconnects_label_xpath = '//cdk-header-cell//*[text()=" Power Disconnects "]'
    ignition_not_detected_label_xpath = '//cdk-header-cell//*[text()=" Ignition Not Detected "]'
    open_rma_label_xpath = '//cdk-header-cell//*[text()=" Open RMA "]'
    all_device_issues_label_summary_xpath = '//*[text()="ALL DEVICE ISSUES"]'
    overdue_for_check_in_summary_label_xpath = '//*[text()="OVERDUE FOR CHECK-IN"]'
    power_disconnects_summary_label_xpath = '//*[text()="POWER DISCONNECTS"]'
    ignition_not_detected_summary_label_xpath = '//*[text()="IGNITION NOT DETECTED"]'
    open_rma_summary_label_xpath = '//div[text()="OPEN RMA"]'
    all_device_issues_graph_label_xpath = '//div[text()="All Device Issues"]'
    group_filter_button_xpath = '//*[text()=" Select Group(s) "]'
    search_group_filter_textbox_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                        'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_group_filter_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                       'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/' \
                                       'ngb-typeahead-window/button[1]'
    done_group_filter_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                     'multi-group-selector/div/div[3]/button[2]'
    select_issue_filter_button_xpath = '//*[@id="issueTypeDropdown"]/div/span'
    select_overdue_issue_button_xpath = '//li/span[text()=" Overdue for Check-in "]'
    select_power_disconnects_button_xpath = '//li/span[text()=" Power Disconnects "]'
    select_search_filter_button_xpath = '//*[@id="searchTypeDropdown"]/div/span'
    select_search_device_button_xpath = '//*[@id="searchTypeDropdown"]/div/div/ul/li[1]'
    select_search_vehicle_button_xpath = '//*[@id="searchTypeDropdown"]/div/div/ul/li[2]'
    search_criteria_textbox_xpath = '//*[@id="searchInput"]'
    first_device_text_xpath = '/html/body/app-root/shell/div/div/div/device-issues/div/div[2]/device-health-table/' \
                              'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[1]'
    first_vehicle_text_xpath = '/html/body/app-root/shell/div/div/div/device-issues/div/div[2]/device-health-table/' \
                               'lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[3]'
    first_row_overdue_text_xpath = '/html/body/app-root/shell/div/div/div/device-issues/div/div[2]/' \
                                   'device-health-table/lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[4]'
    first_row_power_disconnects_text_xpath = '/html/body/app-root/shell/div/div/div/device-issues/div/div[2]/' \
                                             'device-health-table/lx-table/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[5]'
    power_disconnects_graph_xpath = '//div[text()="Power Disconnects"]'
    overdue_for_check_in_graph_xpath = '//div[text()="Overdue for Check-in"]'
    reset_button_xpath = '//*[text()="Reset"]'

    # table columns when set the issue filter as power disconnect
    device_column_text_xpath = '//cdk-header-cell//*[text()="Device"]'
    device_type_column_text_xpath = '//cdk-header-cell//*[text()="Device Type"]'
    vehicle_column_text_xpath = '//cdk-header-cell//*[text()="Vehicle"]'
    group_column_text_xpath = '//cdk-header-cell//*[text()="Group"]'
    disconnect_time_column_text_xpath = '//cdk-header-cell//*[text()="Disconnect Time"]'
    reconnect_time_column_text_xpath = '//cdk-header-cell//*[text()="Reconnect Time"]'
    duration_column_text_xpath = '//cdk-header-cell//*[text()="Duration"]'
