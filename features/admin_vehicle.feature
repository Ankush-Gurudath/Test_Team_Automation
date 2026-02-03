Feature: Admin - Vehicle Management - Old UI

  @LQ-236
  Scenario: Admin - The Vehicle Management page is displayed
    Given pm user logs in
    When the user clicks the "VEHICLES" tab
    Then the page header "VEHICLE MANAGEMENT" and the vehicle count are displayed and the table is displayed with columns: "VEHICLE", "GROUP", "DRIVER", "DEVICE", "LAST CHECK IN", "STATUS"

  @LQ-TB
  Scenario: verify the group filter functionality
    When the user selects multiple groups from the "Select Group(s)" filter
    Then the vehicles belong to the selected groups are listed

  @LQ-239
  Scenario: Add vehicle on the Vehicle Management page
    When the user clicks on "Add Vehicle" & the user enters required fields: "Group" and "Vehicle Name" & the user clicks Create Vehicle
    Then the vehicle is added

  @LQ-237
  Scenario: Filter Last Connected on the Vehicle Management page
    When the user clicks on "Last Connected" filter & the user selects a date range in the Vehicle Management page
    Then the vehicles which Last Connected time is within the date range are displayed in the Vehicle Management page

  Scenario: Filter vehicle Status on the Vehicle Management page
    When the user clicks on "Status" filter & the user selects "In Service" in the Vehicle Management page
    Then the vehicles with In Service status are displayed in the Vehicle Management page

  Scenario: Select Search Driver on the Vehicle Management page
    When the user selects "Driver" from "Select Search" dropdown & the user enters some characters into "Search Name or ID" field in the Vehicle Management page
    Then the vehicles with assigned driver that have inputted characters in their name or employeeid are shown in the Vehicle Management page

  Scenario: Select Search Vehicle on the Vehicle Management page
    When the user selects "Vehicle" from "Select Search" dropdown & the user enters some characters into "Search Vehicle Name" field in the Vehicle Management page
    Then the vehicles which name contains the inputted characters are shown in the Vehicle Management page

  Scenario: Select Search Device on the Vehicle Management page
    When the user selects "Device" from "Select Search" dropdown & the user enters some characters into "Search Device" field in the Vehicle Management page
    Then the vehicles with ER assigned that contained inputted characters in the serial number are shown in the Vehicle Management page

  @LQ-245
  Scenario: Detach Device on the Vehicle Management page
    When the user checks some available vehicles & the user clicks "Detach Device" & the user clicks Apply
    Then the devices are detached from the selected vehicles

  @LQ-240
  Scenario: Edit vehicle on the Vehicle Management page
    When the user clicks on the vehicle name & the user changes "Vehicle Name" on Edit Vehicle page & the user clicks Save Changes
    Then the vehicle name of the edited vehicle is updated

  @LQ-12022
  Scenario: Edit vehicle- move group on the Vehicle Management page
    When the user checks some available vehicles & the user clicks "Edit vehicle" Button & the user selects one group on the group selector & the user clicks "Done" on the group selector & the user clicks "Apply" button & the user clicks "Continue" button
    Then the selected vehicles are moved to the new group

  Scenario: Edit vehicle - Change status on the Vehicle Management page
    When the user checks some available vehicles & the user clicks "Edit vehicle" Button & the user selects "Out of Service" on the Status selector & the user clicks "Apply" button
    Then the status of selected vehicles are updated

  @LQ-15217
  Scenario: Delete vehicle without device assigned from edit vehicle page
    When the user clicks on the "Delete Vehicle" & the user clicks "Continue" button on the pop-up
    Then the vehicle is deleted


  @LQ-233729
  Scenario: Verify that Audit log tab is displayed
    Given the "Administrator/FA" user is in Vehicle Page
    When the user clicks on the "View Change History" in Vehicle Management page
    Then the user should be able to see the table columns, Filters, and Download Log button in View Change History pop-up

  @LQ-237892
  Scenario: Verify search functionality using valid Vehicle Name
    When the user enters a valid Vehicle Name in "Search Vehicle Affected" Search panel
    Then the searched vehicle should be able to see in the Vehicle Audit Log

  Scenario: Verify search functionality with no matching vehicle
    When the user enters an invalid or non-existing Vehicle details in "Search Vehicle Affected"
    Then the searched vehicle should not be able to see in the Vehicle Audit Log

    # Re-enable after DOM-2499 is fixed
#  Scenario: Verify Date Filter functionality
#    When the user selects a specific date range in the Date Filter
#    Then the Vehicle Audit Log should display logs corresponding to the selected date range

  Scenario: Verify close Vehicle Audit Log tab
    When the user click on the "Close" button
    Then the user Audit Log tab should be closed successfully

  @LQ-249616
  Scenario: Verify filtering functionality with Added action
    Given user clicks on "View Change History" in Vehicle Management page
    When the user selects the Action "Added" from the "Select Action(s)" filter dropdown
    Then the Vehicle Audit Log should display logs with the Action type as "Added"

  Scenario: Verify filtering functionality with Edited action
    When the user selects the Action "Edited" from the "Select Action(s)" filter dropdown
    Then the Vehicle Audit Log should display logs with the Action type as "Edited"

  Scenario: Verify filtering functionality with Deleted action
    When the user selects the Action "Deleted" from the "Select Action(s)" filter dropdown
    Then the Vehicle Audit Log should display logs with the Action type as "Deleted"

  Scenario: Verify filtering functionality with Imported action
    When the user selects the Action "Imported" from the "Select Action(s)" filter dropdown
    Then the Vehicle Audit Log should display logs with the Action type as "Imported"

  @LQ-249624
  Scenario: Verify successfully Download the audit logs in the CSV format
    When the user clicks "Download Log" in the Vehicle audit log tab
    Then the vehicle audit log is downloaded successfully

  Scenario: Verify the "Download Log" functionality is disabled when there is no audit log data
    When search an invalid vehicle in "Search Vehicle Affected" filter
    Then the "Download Log" button is disabled in Vehicle Audit Log