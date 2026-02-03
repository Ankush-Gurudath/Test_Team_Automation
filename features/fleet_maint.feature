Feature: End to end Fleet Maint workflow
  As a developer,
  I want to run end to end tests on the Fleet Maint application
  So I can confirm that code changes have not adversely affected the app.

  @LQ-511
  Scenario: Fleet - Maint Suite
  #Scenario: Fleet - Maint - User can access the Preventative Maintenance dashboard
    Given fleet dispatcher logs in
    When the user navigates to Maintenance -> Preventative Maintenance
    Then the Preventative Main labels are shown - Upcoming Services, History & Manage Services

  @LQ-527
  Scenario: User can access the Preventative Maintenance dashboard Manage Services page
    When the user clicks "Manage Services"
    Then the Manage Services page is displayed

  @LQ-528
  Scenario: Create service in Fleet Tracking Service Management page
    When the user clicks the "Create Service" button
    And the user enter some characters in the "SERVICE NAME", "SERVICE INTERVAL (MI)", "DUE SOON THRESHOLD (MI)" field
    And the user clicks the save button
    Then the service is created

  @LQ-529
  Scenario: Edit service in Fleet Tracking Service Management page
    When the user clicks a service name
    And the user enters some characters in the "SERVICE NAME" field
    And the user clicks the save button
    Then the service is edited

  @LQ-516
  Scenario: Filter by vehicle in PM upcoming Services page
    Given the "Fleet Dispatcher" user is in Fleet Tracking - MAINT. - PREVENTATIVE MAINTENANCE - Upcoming Service page
    When the user enters some characters into search vehicles box and the user selects a vehicle in the search vehicles box
    Then the data with selected vehicles are displayed on the table

  @LQ-521
  Scenario: Complete Service in PM Services Due page
    When the user clicks "Complete" hyperlink and the user selects a date and the user selects a time and the users click the "Complete" button
    Then the service of the vehicle is completed and the interval of the service is reset

  @LQ-522
  Scenario: View History in PM page
    When the user clicks "History"
    Then the table is displayed with columns: "VEHICLE", "GROUP", "SERVICE", "INTERVAL", "DATE SERVICED", "ODOMETER", "ENGINE HOURS", "NOTES", "ACTION" & the number of Services is displayed

  @LQ-524
  Scenario: Filter by date in PM Service History page
    When the user sets date filter in PM Service History page
    Then the data with selected filters are displayed on the table

#  @LQ-526
#  Scenario: Edit Service in Fleet Tracking Service History page
#    When the user clicks "Edit" hyperlink and the user selects a date and the user selects a time and the users click the "Save" button
#    Then the service of the vehicle is edited

  @LQ-531
  Scenario: User can access the Diagnostic Trouble Codes dashboard
    When the user navigates to Maintenance -> Diagnostic Trouble Codes
    Then the DTC page is displayed and the number of Codes, group filter and reset icon are displayed on the header bar and the table is displayed with columns: "VEHICLE", "GROUP", "DATE", "CODE (DESCRIPTION)"

  @LQ-532
  Scenario: Filter group in Diagnostic Trouble Codes page
    When  the user selects a group in the group filter in Diagnostic Trouble Codes page
    Then the data with selected group are displayed on the table in dtc page
