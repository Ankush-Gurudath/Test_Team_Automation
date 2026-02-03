class LocatorsMapLivePage:
    fleet_tracking_title_id = 'fleetTrackingText'

    # working list items
    clear_working_list_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer/div' \
                               '/div/div[2]/app-working-list-new/div/div[2]/div[2]/div/div[1]/button'
    search_box_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                       '/div/div/div[2]/app-working-list-new/div/div[1]/app-search-new/div/input'
    select_all_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer/div/div' \
                       '/div[2]/app-working-list-new/div/app-search-results-new/div/div[2]/div[2]'
    add_to_working_list_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-drawer' \
                                '/div/div/div[2]/app-working-list-new/div' \
                                '/app-search-results-new/div/div[1]/button'

    suggestion_list_1st_item_id = 'ngb-typeahead-0-0'

    address_view_detail_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                '/lytx-drawer/div/div/div[2]/app-working-list-new/div' \
                                '/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                '/div[1]/div[1]/div[2]/div[3]/button'

    # working list vehicle, geofence and equipment items
    working_list_item_toggle_prefix_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                            '/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                            '/div/div[2]/div[2]/div/div[2]' \
                                            '/cdk-virtual-scroll-viewport/div[1]/div['
    working_list_item_toggle_suffix_xpath = ']/div[3]/slide-toggle/label/span'
    working_list_1st_item_toggle_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                         '/lytx-drawer/div/div/div[2]/app-working-list-new/div' \
                                         '/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                         '/div[1]/div[1]/div[3]/slide-toggle/label/span'
    working_list_1st_item_name_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                       '/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                       '/div/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                       '/div[1]/div[1]/div[2]/div[1]'
    working_list_1st_item_driver_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                         '/lytx-drawer/div/div/div[2]/app-working-list-new/div' \
                                         '/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                         '/div[1]/div[1]/div[2]/div[2]/span'
    working_list_1st_item_group_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                        '/lytx-drawer/div/div/div[2]/app-working-list-new/div' \
                                        '/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                        '/div[1]/div[1]/div[2]/div[3]/span'
    working_list_1st_item_status_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                         '/lytx-drawer/div/div/div[2]/app-working-list-new/div' \
                                         '/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                         '/div[1]/div/div[2]/div[2]/span'
    working_list_1st_item_type_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                       '/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                       '/div/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                       '/div[1]/div[1]/div[2]/div[3]/span'

    working_list_2nd_item_toggle_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                         '/lytx-drawer/div/div/div[2]/app-working-list-new/div' \
                                         '/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                         '/div[1]/div[2]/div[3]/slide-toggle/label/span'
    working_list_2nd_item_trash_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                        '/lytx-drawer/div/div/div[2]/app-working-list-new/div' \
                                        '/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                        '/div[1]/div[2]/div[4]/i'
    working_list_2nd_item_name_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                       '/lytx-drawer/div/div/div[2]/app-working-list-new/div' \
                                       '/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                       '/div[1]/div[2]/div[2]/div[1]'
    working_list_2nd_item_status_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                         '/lytx-drawer/div/div/div[2]/app-working-list-new' \
                                         '/div/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                         '/div[1]/div[2]/div[2]/div[2]/span'
    working_list_2nd_item_type_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                       '/lytx-drawer/div/div/div[2]/app-working-list-new/div' \
                                       '/div[2]/div[2]/div/div[2]/cdk-virtual-scroll-viewport' \
                                       '/div[1]/div[2]/div[2]/div[3]/span'

    # map pins
    vehicle_pin_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-fleet-tracker' \
                        '/div/div/div/div[2]/div[2]/div/div[3]/div[3]/img'
    geofence_pin_xpath = '/html/body/app-root/shell/div/div/div/app-map/div/lytx-fleet-tracker' \
                         '/div/div/div/div[2]/div[2]/div/div[3]/div/img'
    vehicle_pin_closest_vehicle_xpath = '/html/body/app-root/shell/div/div/div/app-map/div' \
                                        '/lytx-fleet-tracker/div/div/div/div[2]/div[2]/div' \
                                        '/div[3]/div[4]/img'
    closest_vehicle_estimate_time_xpath = '/html/body/app-root/shell/div/div/div/app-map' \
                                          '/div/lytx-fleet-tracker/div/div/div/div[2]' \
                                          '/div[2]/div/div[4]/div/div/div/div[1]'
