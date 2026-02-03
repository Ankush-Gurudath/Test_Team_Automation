class LocatorsAddTrailerPage:
    group_button_xpath = '//*[@class="multi-group-filter__label"]'
    search_group_textbox_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                                 'multi-group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/input'
    select_group_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/multi-group-selector/' \
                                'div/div[1]/div[2]/div/lytx-typeahead/div/ngb-typeahead-window/button[1]'
    done_group_button_xpath = '/html/body/ngb-modal-window/div/div/multi-group-selector-modal/' \
                              'multi-group-selector/div/div[3]/button[2]'
    trailer_name_textbox_xpath = '//*[@id="name-control"]/div/div[2]/input'
    vin_textbox_xpath = '//*[@id="vin-control"]/div/div[2]/input'
    create_trailer_button_xpath = '//*[@id="submitButton"]'
    create_trailer_success_message_xpath = '//*[contains(text(), "successfully created.")]'
