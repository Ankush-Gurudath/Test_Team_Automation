Feature: Admin - Geofence Management

  @LQ-3557
  Scenario: The Geofence Management page is displayed
    Given fa user logs in
    When the user clicks "GEOFENCES"
    Then the page header "GEOFENCE MANAGEMENT" and geofence count are displayed and the table is displayed with columns: "GEOFENCE", "GROUP", "RECENT ACTIVITY", "STATUS", "ASSETS", "TRIGGER TYPE", "CREATED DATE", "SOURCE"

  @LQ-3558
  Scenario: Filter by group in Geofences page
    When the user sets group filter to one group in Geofences page
    Then the data with selected group are displayed on the table

  Scenario: Filter by recent activity in Geofences page
    When the user sets date filter of "Recent Activity" in Geofences page
    Then the data with selected recent activity are displayed on the table

  Scenario: Filter by status in Geofences page
    When the user sets status filter to active status in Geofences page
    Then the data with selected status are displayed on the table

  Scenario: Filter by creation date in Geofences page
    When the user sets date filter of "Creation Date" in Geofences page
    Then the data with selected created date are displayed on the table

  Scenario: Filter by geofence name in Geofences page
    When the user enters search criteria in "Search Geofence" in Geofences page
    Then the data match the search criteria are displayed on the table

  @LQ-3565
  Scenario: Download template in Import Geofences page
    When the user clicks "Import" and the user clicks "Geofence Excel Template"
    Then the ImportGeofence template is downloaded
