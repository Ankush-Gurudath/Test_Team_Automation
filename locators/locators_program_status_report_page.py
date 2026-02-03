class LocatorsProgramStatusReportPage:
    # ProgramStatusReportTable

    num_of_subgroups_text_xpath = '//*[@class="filter-header-bar__title__count--value--success"]'
    group_text_xpath = '//*[text()="Group"]'
    num_of_devices_text_xpath = '//*[text()="# of Devices"]'
    unassigned_drivers_text_xpath = '//*[text()="Unassigned Drivers"]'
    overdue_for_check_in_text_xpath = '//*[text()="Overdue for Check-In"]'
    overdue_for_coaching_text_xpath = '//*[text()="Overdue for Coaching"]'
    coaching_effectiveness_text_xpath = '//*[text()="Coaching Effectiveness"]'
    program_effectiveness_text_xpath = '//*[text()="Program Effectiveness"]'

    # Filters
    filter_by_group_program_status_button_xpath = '//*[@class="group-filter"]'
    search_by_group_program_status_textbox_xpath = '//*[@placeholder="Search by Group"]'
    select_search_by_group_program_status_button_xpath = ('/html/body/ngb-modal-window/div/div/group-selector-modal'
                                                          '/group-selector/div/div[1]/div['
                                                          '2]/div/lytx-typeahead/div/ngb-typeahead-window/button[1]')
    done_filter_program_status_button_xpath = '//*[@class="group-selector-bottom-done lx-btn lx-btn-primary"]'

    # Reset
    reset_program_status_button_xpath = '//*[text()="Reset"]'

    # Links
    group_link_text_xpath = '(//*[@class="group-name"])[3]'
    unassigned_driver_link_text_xpath = '(//*[@class="lx-link unassigned-drivers-percentage row-item-hovered"])[1]'
    overdue_for_coaching_link_text_xpath = '(//*[@class="lx-link overdue-for-coaching-percentage row-item-hovered"])[2]'
    coaching_effectiveness_link_text_xpath = '(//*[@class="coaching-effectiveness-percentage lx-link row-item-hovered"])[2]'

    # ProgramStatuReportPage
    program_status_report_page_text_xpath = '//*[@class="filter-header-title"]'

    # AssignDriverPage
    assign_driver_page_text_xpath = '//*[@class="filter-header-title"]'

    # DueForCoachingPage
    due_for_coaching_text_xpath = '//*[@class="filter-header-title"]'

    # CoachReportPage
    coaches_report_text_xpath = '//*[text()="Coaches Report"]'
    total_count_load_xpath = '//*[@class="filter-header-bar__title__count--value--loading"]'
    first_group_name_text_xpath = '(//cdk-cell//div[@class="group-name"])[2]'
