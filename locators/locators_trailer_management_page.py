class LocatorsTrailerManagement:
    trailer_tab_xpath = '//*[contains(text(), "Trailers")]'
    trailer_management_text_xpath = '//*[text()="Trailer management"]'
    # Table column
    trailer_column_text_xpath = '//span[text()="trailer"]'
    group_column_text_xpath = '//span[text()="Group"]'
    license_plate_column_text_xpath = '//span[text()="License plate"]'
    vin_column_text_xpath = '//span[text()="VIN"]'
    inspection_list_column_text_xpath = '//cdk-header-cell//span[text()=" Inspection list "]'

    # Filter
    group_filter_xpath = '//*[text()=" Select Group(s) "]'
    search_group_textbox_xpath = '//input[@placeholder="Search Groups"]'
    select_searched_group_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                  'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/' \
                                  'ngb-typeahead-window/button'
    search_group_done_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal' \
                                     '/multi-group-selector/div/div[3]/button[2]'
    search_trailer_textbox_xpath = '//*[@id="searchInput"]'
    add_trailer_button_xpath = '//button[text()=" Add Trailer "]'
    searched_trailer_name_text_xpath = '//*[@id="table"]//cdk-row/cdk-cell[2]//a'
    reset_button_xpath = '//div[text()="Reset"]'
    select_first_trailer_checkbox_xpath = '//*[@id="table"]/div[2]//cdk-row[1]/cdk-cell[1]/div/div/i'
    select_second_trailer_checkbox_xpath = '//*[@id="table"]/div[2]//cdk-row[2]/cdk-cell[1]/div/div/i'
    set_inspection_list_button_xpath = '//*[text()="Set Inspection List"]'
    select_first_set_inspection_list_dialog_xpath = '/html/body/ngb-modal-window/div/div/app-set-inspection-list-modal' \
                                                    '/lytx-modal-shell/div/div[2]/div[2]/div/div/div/div[1]/input'
    select_second_set_inspection_list_dialog_xpath = '/html/body/ngb-modal-window/div/div/app-set-inspection-list-moda' \
                                                     'l/lytx-modal-shell/div/div[2]/div[2]/div/div/div/div[3]/input'
    set_inspection_list_dialog_button_xpath = '/html/body/ngb-modal-window/div/div/app-set-inspection-list-modal/' \
                                              'lytx-modal-shell/div/div[2]/div[3]/button[2]'
    first_inspection_list_status_text_xpath = '//*[@id="table"]/div[2]/div[2]/cdk-table/cdk-row[1]/cdk-cell[6]'
    second_inspection_list_status_text_xpath = '//*[@id="table"]/div[2]/div[2]/cdk-table/cdk-row[2]/cdk-cell[6]'

    first_trailer_group_xpath = '//*[@id="table"]//cdk-row[1]/cdk-cell[3]'
    trailer_count_xpath = '//*[@class="filter-header-bar__title__count--container"]'
    delete_trailer_button_id = 'deleteTrailerButton'
    confirm_delete_trailer_continue_button_id = 'modalShellPrimaryButton'
    trailer_deleted_popup_xpath = '//*[contains(text(), "successfully deleted.")]'
    no_trailers_found_text_xpath = '//*[contains(text(), "No trailers found")]'