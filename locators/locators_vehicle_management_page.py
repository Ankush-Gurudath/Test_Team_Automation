class LocatorsVehicleManagement:
    vehicle_management_title_xpath = './/*[text()="Vehicle Management"]'
    # Filters
    group_filter_button_xpath = '//span[text()=" Select Group(s) "]'
    search_group_textbox_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                 'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_group_filter_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                       'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/' \
                                       'ngb-typeahead-window/button'
    done_filter_group_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                     'multi-group-selector/div/div[3]/button[2]'
    last_connected_filter_button_xpath = '//*[text()="Last Connected"]'
    first_date_filter_button_xpath = '(//*[@data-test-id="lytx-dateRangeSelector-day" and contains(text(), "17")])[1]'
    second_date_filter_button_xpath = '(//*[@data-test-id="lytx-dateRangeSelector-day" and contains(text(), "24")])[1]'
    apply_filter_date_button_xpath = '//*[@id="btn-apply"]'
    status_filter_button_xpath = '//*[@id="statusFilter"]/div/span'
    select_status_button_xpath = '//li//span[contains(text(), "In Service")]'
    out_of_service_button_xpath = '//li/span[text()=" Out Of Service "]'
    select_search_filter_button_xpath = '//*[@id="multiTypeFilter"]/div/span'
    vehicle_select_search_button_xpath = '//li/span[text()=" Vehicle "]'
    device_select_search_button_xpath = '//li/span[text()=" Device "]'
    driver_select_search_button_xpath = '//li/span[text()=" Driver "]'
    search_vehicle_name_textbox_xpath = '//*[@id="searchInput"]'
    reset_button_xpath = './/*[text()="Reset"]'
    first_row_vehicle_name_xpath = '//*[@id="table"]/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[2]'
    test_vehicle_name_xpath = './/*[normalize-space(.)="TESLA"]'
    first_row_group_name_xpath = '//*[@id="table"]/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[3]'
    first_row_driver_name_xpath = '//*[@id="table"]/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[4]'
    first_row_device_name_xpath = '//*[@id="table"]/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[5]'
    first_row_last_connected_name_xpath = '//*[@id="table"]/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[6]'
    first_row_status_name_xpath = '//*[@id="table"]/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[7]'
    add_vehicle_button_xpath = '//*[@id="table"]/div[2]/div[1]/div/div[4]/button'
    select_first_vehicle_checkbox_xpath = '//*[@id="table"]/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[1]/div/div/i'
    select_second_vehicle_checkbox_xpath = '//*[@id="table"]/div[2]/div[2]/cdk-table/cdk-row[2]/cdk-cell[1]/div/div'

    first_vehicle_selected_xpath = '//*[@id="table"]/div[2]/div[2]/cdk-table/cdk-row/cdk-cell[2]/span[2]'
    first_vehicle_xpath = '//span[contains(@class,"cell-value")]//span[contains(@class,"lx-link")][1]'
    more_option_button_xpath = '//*[@id="table"]/div[2]/div[1]/div/div[3]/div/div[1]/span'
    move_group_continue_button_xpath = '/html/body/ngb-modal-window/div/div/bulk-vehicle-group/' \
                                       'bulk-vehicle-action-modal/lytx-modal-shell/div/div[2]/div[3]/button[2]'
    apply_detach_device_button_xpath = '//*[@id="modalShellPrimaryButton" and text()=" Apply "]'
    detach_device_button_xpath = '//button[normalize-space(.)="Detach Device"]'
    confirm_delete_vehicle_button_xpath = '/html/body/ngb-modal-window/div/div/bulk-delete-vehicles/' \
                                          'bulk-vehicle-action-modal/lytx-modal-shell/div/div[2]/div[3]/button[2]'

    # Bulk edit vehicle
    edit_vehicle_button_xpath = '//*[@id="table"]/div[2]/div[1]/div/div[3]/button[1]'
    group_filter_edit_vehicle_button_xpath = '/html/body/ngb-modal-window/div/div/bulk-edit-vehicles/lytx-modal-shell/' \
                                             'div/div[2]/div[2]/div/div[2]/group-filter/div'
    bulk_edit_search_group_textbox_xpath = '/html/body/ngb-modal-window[2]/div/div/group-selector-modal/' \
                                           'group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    bulk_edit_select_group_button_xpath = '/html/body/ngb-modal-window[2]/div/div/group-selector-modal/' \
                                          'group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/ngb-typeahead-window'
    bulk_edit_group_done_button_xpath = '/html/body/ngb-modal-window[2]/div/div/group-selector-modal/group-selector/' \
                                        'div/div[3]/button[2]'
    bulk_edit_group_apply_button_xpath = '/html/body/ngb-modal-window/div/div/bulk-edit-vehicles/lytx-modal-shell/' \
                                         'div/div[2]/div[3]/button[2]'
    bulk_edit_open_status_drop_down_button_xpath = '//*[@id="statusSelector"]/div/span/span'
    bulk_edit_select_status_xpath = '/html/body/ngb-modal-window/div/div/bulk-edit-vehicles/lytx-modal-shell/' \
                                    'div/div[2]/div[2]/div/div[3]/dropdown/div/div/ul/li[2]'
    bulk_edit_vehicle_apply_button = '/html/body/ngb-modal-window/div/div/bulk-edit-vehicles/lytx-modal-shell/' \
                                     'div/div[2]/div[3]/button[2]'
    bulk_edit_dvir_access_drop_down_xpath = '/html/body/ngb-modal-window/div/div/bulk-edit-vehicles/' \
                                            'lytx-modal-shell/div/div[2]/div[2]/div/div[4]/div[2]/dropdown/div/span/span'
    bulk_edit_select_enable_status_xpath = '/html/body/ngb-modal-window/div/div/bulk-edit-vehicles/lytx-modal-shell' \
                                           '/div/div[2]/div[2]/div/div[4]/div[2]/dropdown/div/div/ul/li[1]'
    delete_vehicle_button_xpath = '//*[@id="table"]/div[2]/div[1]/div/div[3]/button[2]'
    detach_device_tab_xpath = '//*[@id="table"]//*[text()="Detach Device"]'

    vehicle_page_title_xpath = '//span[text()="Vehicle Management"]'
    vehicle_count_xpath = '(//*[contains(text()," vehicle")]/parent::div/preceding-sibling::div/div)[1]'

    # vehicle list column
    vehicle_column_text_xpath = '//span[@id="sortableContainerVehicleName"]/span[text()="Vehicle"]'
    group_column_text_xpath = '//span[@id="sortableContainerGroupName"]'
    driver_column_text_xpath = '//span[text()="Driver"]'
    device_column_text_xpath = '//cdk-header-cell//span//*[contains(text(),"Device")]'
    last_connected_column_text_xpath = '//span[text()="Last Check In"]'
    status_column_text_xpath = '//cdk-header-cell//span[text()=" Status "]'

    select_all_checkbox_xpath = '//cdk-header-cell/i'
    vehicle_list_xpath = './/*[@class="lx-link ng-star-inserted"]'
    active_checkbox_xpath = './/*[@class="lx-icon table-checkbox lx-checkbox-active"]'
    close_search_icon_xpath = './/*[@class="lx-icon lx-close-x"]'
    vehicle_detached_from_device_success_message = '//*[contains(text(), "vehicle detached from a device")]'

    checkbox_xpath = '(//cdk-row[1]//i[contains(@class,"table-checkbox")])[1]'
    detach_button_xpath = '//button[normalize-space(.)="Detach Device"]'
    apply_button_xpath = '//button[@id="modalShellPrimaryButton" and normalize-space(.)="Apply"]'

    # Vehicle Audit Log
    change_view_history_button_xpath = '//*[@ngbtooltip="View Change History"]'
    vehicle_affected_column_xpath = '//cdk-header-cell//span[text()="Vehicle Affected"]'
    action_column_xpath = '//cdk-header-cell//span[text()="Action"]'
    action_details_column_xpath = '//cdk-header-cell//span[contains(text(), "Action Details")]'
    editor_column_xpath = '//cdk-header-cell//span[contains(text(), "Editor")]'
    action_date_column_xpath = '//cdk-header-cell//span[contains(text(), "Action Date")]'
    search_vehicle_affected_filter_xpath = '//*[@id="searchInput"]'
    date_range_dropdown_xpath = '//*[@class="audit-date"]'
    select_date_range_today_xpath = '//*[@class="audit-date"]//span[contains(@class, "today")]'
    select_actions_filter_xpath = '//*[@class="audit-actions"]'
    download_log_button_xpath = '//*[contains(text(),"Download Log")]'
    download_log_button_disabled_xpath = '//*[@class="audit-download"]//button[@disabled]'
    first_vehicle_affected_text_xpath = '//audit-log-table//cdk-row[1]/cdk-cell[1]'
    no_audit_logs_message_xpath = '//*[contains(@class,"lx-table__table__empty-message")]'
    action_date_xpath = '//audit-log-table//cdk-row[1]/cdk-cell[5]'
    close_view_change_history_xpath = '//*[text()=" Close "]'
    view_change_history_popup_xpath = '//*[@modalcomponentname="VehicleAuditLog"]'
    reset_button_audit_page_xpath = '//*[@class="audit-log-modal-shell"]//*[text()="Reset"]'
    select_action_type_xpath = '//li/span[contains(text(), "Added")]'
    select_edited_xpath = '//li/span[contains(text(), "Edited")]'
    action_type_text_xpath = '//audit-log-table//cdk-row[1]/cdk-cell[2]'
    first_action_details_text_xpath = '//cdk-table/cdk-row[1]/cdk-cell[3]/span[2]/span'
    select_deleted_xpath = '//li/span[text() = " Deleted "]'
    select_imported_xpath = '//li/span[text() = " Imported "]'
    group_row_text_xpath = '//*[@id="table"]/div[2]/div[2]/cdk-table/cdk-row[{row}]/cdk-cell[3]/span[2]'
    vehicles_count_xpath = '//*[@data-test-id="filter-headerBar-countValue"]'
