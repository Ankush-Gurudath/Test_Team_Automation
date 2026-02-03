Feature: Admin - Device Management New-Ui-Shell

  @LQ-236
  Scenario: Admin - Device Management Suite
    Given pm user logs in
    When the user clicks the "VEHICLES" tab
    Then the page header "VEHICLE MANAGEMENT" and the vehicle count are displayed and the table is displayed with columns: "VEHICLE", "GROUP", "DRIVER", "DEVICE", "LAST CONNECTED", "STATUS"

  @LQ-230
  Scenario: The Device Management page is displayed correctly
    When the user clicks the "DEVICES" tab
    Then the page header "DEVICE MANAGEMENT" is displayed and the user count are displayed and the table is displayed with columns: "DEVICE", "DEVICE TYPE", "VEHICLE", "GROUP", "LAST CONNECTED", "INITIAL CONNECTION"

  @LQ-231
  Scenario: Filter group(s) on the Device Management page
    When the user sets group filter to one group in Device Management Page
    Then the devices belong to the group are listed

  @StageTest
  Scenario: Filter Device Type on the Device Management page
    When the user clicks on "Device Type" filter & the user selects one type
    Then the devices of the selected type are displayed

  @StageTest
  Scenario: Filter Status on the Device Management page
    When the user clicks on "Status" filter & the user selects "In Service"
    Then the devices with "In Service" status are displayed

  @StageTest
  Scenario: Search Device on the Device Management page
    When the user enters some characters into "Search Device" field
    Then the devices that contained inputted characters in the serial number are shown

  @LQ-4456
  Scenario: The Device profile page is opened
    When the user clicks a device link
    Then the "DEVICE PROFILE" page is opened and the fields are displayed:"DEVICE", "DEVICE TYPE", "GROUP", "STATUS", "HEALTH", "LAST COMMUNICATED", "LAST MOVEMENT", "INITIAL CONNECTION"

  @LQ-233 @StageTest
  Scenario: Move group for devices on the Device Management page
    When the user checks some available devices & the user clicks "Move Group" & the user selects one group & the user clicks "Done" on the Group Selector pop-up
    Then the selected devices are moved to the new group

  @LQ-234
  Scenario: Change status on the Device Management page
    When the user checks some available devices & the user clicks "Change Status" & the user selects "Spare" & the user clicks Save
    Then the status of selected devices are updated to Spare

  Scenario: Delete vehicle added in prerequisite step for tests
    When the user click on vehicle menu to delete the vehicle added for tests
    Then the vehicle is deleted

  @LQ-241222
  Scenario: Verify that the Device Audit log tab is displayed
    Given the "Administrator/FA" user is in Device Page
    When the user clicks on the "View Change History" in Device Management page
    Then the user should be able to see the table columns: "DEVICE AFFECTED", "ACTION", "ACTION DETAILS","EDITOR", "ACTION DATE" and page header "Device Audit Log"
    And The user should be see the filters ‘Search Device Affected’, Date filter and ‘Select Action(s)’ in the header, and the ‘Download Log’ button

  @LQ-241241
  Scenario: Verify search functionality using a valid device
    When the user enters a valid device number in "Search Device Affected"
    Then the system should display only matching logs

  Scenario: Verify search functionality with no matching device
    When the user enters an invalid device number in "Search Device Affected"
    Then the system should show no results message

    # Re-enable after DOM-2499 is fixed
#  Scenario: Verify Date filter functionality
#    When the user selects a date range in the Date filter
#    Then the system should display logs within the selected date range

  Scenario: Verify closing the Device Audit Log tab
    When the user clicks on the "Close" button
    Then the device Audit Log tab should be closed successfully

  Scenario: Verify Group modifications in audit logs
    Given user moved a device to another group in Device Management page
    When user clicks on "View Change History" in Device Management page and search for a device
    Then the Device Audit Log should display logs with the Action type as "Edited" and Action details as Group

  @LQ-249538
  Scenario: Verify filtering functionality with Edited action
    When the user selects the Action "Edited" from the "Select Action(s)" filter dropdown
    Then the Device Audit Log should display logs with the Action type as "Edited"

  @LQ-249600
  Scenario: Verify successfully Download the audit logs in the CSV format
    When the user clicks "Download Log" in the Device audit log tab
    Then the Device audit log is downloaded successfully

  Scenario: Verify the "Download Log" functionality is disabled when there is no audit log data
    When search an invalid device in "Search device Affected" filter
    Then the "Download Log" button is disabled in Device Audit Log