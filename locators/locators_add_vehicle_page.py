class LocatorsAddVehicle:
    add_group_button_xpath = '//*[@id="groupSelector"]/div'
    search_group_textbox_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                 'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_search_group_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                       'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/' \
                                       'ngb-typeahead-window/button'
    done_group_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                              'multi-group-selector/div/div[3]/button[2]'
    vehicle_name_textbox_xpath = '//*[@id="vehicleName"]'
    create_vehicle_button_xpath = '//*[@id="submitButton"]'
    continue_alert_xpath = '(.//*[normalize-space(.)="Continue"])[1]'
    add_vehicle_page_title_xpath = "//*[contains(text(), 'Add Vehicle')]"
    create_vehicle_success_message_xpath = '//*[contains(text(), "successfully created.")]'