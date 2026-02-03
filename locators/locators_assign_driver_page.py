class LocatorsAssignDriver:
    # AssignDriversLocators
    assign_button_xpath = '//*[@data-test-id="assignDriver-card-Button"]'
    assign_driver_search_xpath = '//*[@placeholder="Search Name or ID"]'
    select_assign_driver_search_xpath = '/html/body/ngb-modal-window/div/div/assign-driver/' \
                                        'lytx-modal-shell/div/div[2]/div[2]/div/div/user-search/' \
                                        'div/lytx-typeahead/div/ngb-typeahead-window/button'
    assign_driver_button_xpath = '/html/body/ngb-modal-window/div/div/assign-driver/' \
                                 'lytx-modal-shell/div/div[2]/div[3]/button[2]'
    filter_group_button_xpath = '//*[@id="groupSelectorIcon"]'
    search_group_filter_box_xpath = '//*[@placeholder="Search by Group"]'
    select_search_group_filter_xpath = '/html/body/ngb-modal-window/div/div/group-selector-modal/' \
                                       'group-selector/div/div[1]/div[2]/div/lytx-typeahead/div/' \
                                       'ngb-typeahead-window/button[1]'
    done_button_group_filter_xpath = '//*[contains(text(), "Done")]'
    group_name_text_xpath = '//*[contains(@class, "group-name")]'
    reset_button_xpath = '//*[text()="Reset"]'

    third_assign_driver_task_checkbox_xpath = '(//*[@id="assignDriverCheckbox"])[3]'
    fourth_assign_driver_task_checkbox_xpath = '(//*[@id="assignDriverCheckbox"])[4]'

    # view assign driver task card
    task_count_xpath = '//*[@class="filter-header-bar__title__count--container"]/div[1]'
    assign_selected_button_xpath = '//*[@id="batchAssignButton"]'
    move_group_button_xpath = '//*[contains(text(), "Move Group")]'
    vehicle_text_xpath = '//cdk-header-cell//span[contains(text(), "Vehicle")]'
    group_text_xpath = '//cdk-header-cell//span[contains(text(), "Group")]'
    event_date_text_xpath = '//cdk-header-cell//span[contains(text(), "Event Date")]'
    event_id_text_xpath = '//cdk-header-cell//span[contains(text(), "Event ID")]'
    behavior_text_xpath = '//cdk-header-cell//span[contains(text(), "Behaviors")]'
    assign_driver_checkbox_xpath = '//*[@id="assignDriverCheckbox"]'
    preview_button_xpath = '//*[@data-test-id="assignDriver-preview-button"]'
    more_actions_button_xpath = '//*[@data-test-id="actionBar-moreActions-text"]'
    mark_as_fyi_notify_xpath = '//*[text()="Mark as FYI Notify"]'
    yes_confirm_button_xpath = '/html/body/ngb-modal-window[2]/div/div/action-modal/lytx-modal-shell' \
                               '/div/div[2]/div[3]/button[2]'
    close_preview_button_xpath = '/html/body/ngb-modal-window/div/div/event-preview/div/div[1]/i'
