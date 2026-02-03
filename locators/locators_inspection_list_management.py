class LocatorsInspectionListManagementPage:
    vehicle_inspection_list_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/' \
                                          'dvir-inspections-tab/div/section/div/h2'
    default_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/dvir-inspections-tab/' \
                          'div/section/dvir-inspections-list/dvir-inspections-list-item[1]/div[1]'
    duplicate_icon_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/dvir-inspections-tab/' \
                           'div/section/dvir-inspections-list/dvir-inspections-list-item[1]/div[2]/button'
    edit_list_button_icon_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/' \
                                  'dvir-inspections-tab/div/section/dvir-inspections-list/' \
                                  'dvir-inspections-list-item[2]/div[2]/button[2]'
    list_name_textbox_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-form/div/section/form/div[1]/' \
                              'lytx-input/div/div/input'
    save_changes_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-form/div/div[2]/button[2]'
    first_vehicle_list_name_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/dvir-inspections-tab/' \
                                    'div/section/dvir-inspections-list/dvir-inspections-list-item[2]/div[1]'
    all_vehicle_inspection_lists_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/dvir-inspections-tab' \
                                         '/div/section/dvir-inspections-list'
    default_inspection_list_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/dvir-inspections-tab/div/section/dvir-inspections-list/dvir-inspections-list-item[1]/div[1]'
    new_list_button_xpath = '//*[text()=" New List "]'
    new_list_name_textbox_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-form/div/section/' \
                                  'form/div[1]/lytx-input/div/div/input'
    section_items_textbox_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-form/div/section/form/' \
                                  'div[3]/div[1]/div[1]/div/lytx-input/div/div/input'
    list_inspection_points_textbox_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-form/div/section/' \
                                           'form/div[3]/div[1]/div[2]/dvir-textarea/div/textarea'
    create_list_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-form/div/div[2]/button[2]'

    delete_list_icon_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/dvir-inspections-tab/div/' \
                             'section/dvir-inspections-list/dvir-inspections-list-item[2]/div[2]/button[1]'
    delete_inspection_list_button_xpath = '/html/body/ngb-modal-window/div/div/action-modal/lytx-modal-shell/' \
                                          'div/div[2]/div[3]/button[2]'
    trailer_list_link_xpath = '//*[text()="Trailer List"]'
    trailer_inspection_lists_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/' \
                                           'dvir-inspections-tab/div/section/div/h2'
    trailer_default_title_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/dvir-inspections-tab/' \
                                  'div/section/dvir-inspections-list/dvir-inspections-list-item[1]/div[1]'
    trailer_duplicate_icon_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/dvir-inspections-tab' \
                                   '/div/section/dvir-inspections-list/dvir-inspections-list-item[1]/div[2]/button'
    trailer_edit_list_icon_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/dvir-inspections-tab/' \
                                   'div/section/dvir-inspections-list/dvir-inspections-list-item[2]/div[2]/button[2]'
    trailer_edit_list_name_textbox_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-form/div/section/' \
                                           'form/div[1]/lytx-input/div/div/input'
    trailer_inspection_items_section_textbox_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-form/' \
                                                     'div/section/form/div[3]/div[1]/div[1]/div/lytx-input/' \
                                                     'div/div[1]/input'
    trailer_inspection_points_textbox_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-form/div/section/' \
                                              'form/div[3]/div[1]/div[2]/dvir-textarea/div/textarea'
    trailer_save_changes_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-form/div/div[2]/button[2]'
    trailer_all_list_section_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/dvir-inspections-tab/' \
                                     'div/section'
    first_trailer_list_name_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/dvir-inspections-tab/' \
                                    'div/section/dvir-inspections-list/dvir-inspections-list-item[2]/div[1]'
    trailer_new_list_name_textbox_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-form/div/section/' \
                                          'form/div[1]/lytx-input/div/div/input'
    trailer_create_new_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspection-form/div/div[2]/button[2]'
    trailer_list_delete_button_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/dvir-inspections-tab/' \
                                       'div/section/dvir-inspections-list/dvir-inspections-list-item[2]/div[2]/' \
                                       'button[1]/span'
    trailer_delete_list_popup_button_xpath = '/html/body/ngb-modal-window/div/div/action-modal/lytx-modal-shell/' \
                                             'div/div[2]/div[3]/button[2]'
    all_trailer_inspection_list_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/' \
                                        'dvir-inspections-tab/div'
    first_trailer_inspection_list_xpath = ('/html/body/app-root/shell/div/div/div/dvir-inspections/div/dvir'
                                           '-inspections-tab/div/section/dvir-inspections-list/dvir-inspections-list'
                                           '-item[2]')
    trailer_list_second_row_xpath = '/html/body/app-root/shell/div/div/div/dvir-inspections/div/dvir-inspections-tab/' \
                                    'div/section/dvir-inspections-list/dvir-inspections-list-item[3]/div[1]'
    vehicle_list_link = '//*[text()="Vehicle List"]'
    new_inspection_list_title_xpath = '//*[contains(text(), "New Inspection List")]'
    list_management_highlighted_xpath = '//*[@class="subitem-row subitem-link active"]'
