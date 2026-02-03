class LocatorsGeofenceManagement:
    geofence_page_title_xpath = '//*[text()="Geofence Management"]'
    geofence_count_xpath = '//span[contains(text(), "Geofence")]/parent::div/preceding-sibling::div/div'

    # geofences list column
    geofence_column_text_xpath = '//span[text()="Geofence"]'
    group_column_text_xpath = '//span[text()="Group"]'
    recent_activity_column_text_xpath = '//cdk-header-cell//span[text()="Recent Activity"]'
    status_column_text_xpath = '//*[text()="Status"]'
    assets_column_text_xpath = '(//*[text()=" Assets "])[1]'
    trigger_type_column_text_xpath = '//*[text()="Trigger Type"]'
    created_date_column_text_xpath = '//cdk-header-cell//*[text()="Created Date"]'
    source_column_text_xpath = '//*[text()="Source"]'

    # Filter on geofence page
    group_filter_xpath = '//*[text()=" Select Group(s) "]'
    search_group_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                         'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_searched_group_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                  'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/' \
                                  'ngb-typeahead-window/button'
    done_button_xpath = '//*[contains(@class, "multi-group-selector-bottom-done lx-btn lx-btn-primary")]'
    recent_activity_filter_xpath = '//lx-date-range-filter//*[text()="Recent Activity"]'
    recent_activity_last_7_days_xpath = '//div[contains(text(), " Last 7 Days")]'
    recent_activity_apply_button_xpath = '//*[text()="Recent Activity"]/ancestor::lx-date-range-filter//*[text()="Apply"]'
    status_filter_xpath = '//*[@id="statusFilter"]'
    select_active_status_xpath = '//li//*[text()=" Active "]'
    created_date_filter_xpath = '//lx-date-range-filter//span[text()="Created Date"]'

    created_date_range_start_month_xpath = '//*[text()="Created Date"]/parent::div/following-sibling::div//*[text()="From"]/parent::div//input[contains(@class, "date day")]'
    created_date_range_start_day_xpath = '//*[text()="Created Date"]/parent::div/following-sibling::div//*[text()="From"]/parent::div//input[contains(@class, "date month")]'
    created_date_range_start_year_xpath = '//*[text()="Created Date"]/parent::div/following-sibling::div//*[text()="From"]/parent::div//input[contains(@class, "date year")]'
    created_date_range_end_month_xpath = '//*[text()="Created Date"]/parent::div/following-sibling::div//*[text()="To"]/parent::div//input[contains(@class, "date month")]'
    created_date_range_end_day_xpath = '//*[text()="Created Date"]/parent::div/following-sibling::div//*[text()="To"]/parent::div//input[contains(@class, "date day")]'
    created_date_range_end_year_xpath = '//*[text()="Created Date"]/parent::div/following-sibling::div//*[text()="To"]/parent::div//input[contains(@class, "date year")]'
    created_date_apply_button_xpath = '//*[text()="Created Date"]/ancestor::lx-date-range-filter//*[text()="Apply"]'
    search_geofence_name_input_box_xpath = '//input[@id="searchInput"]'
    reset_button_xpath = '//*[text()="Reset"]'
    import_button_xpath = '//*[@id="table"]//*[text()=" Import "]'
    download_template_xpath = '//*[@class="download-template"]'
    group_name_xpath = '//cdk-row/cdk-cell[2]/span[2]'
