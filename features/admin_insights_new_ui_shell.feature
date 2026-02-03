Feature: Admin - Insights New UI Shell

  @LQ-235
  Scenario: Admin - Insights Suite
    Given fa user logs in
    When the user clicks "INSIGHTS" & the user clicks "DRIVER ID ASSIGNMENT"
    Then the trip count is displayed and the table section is displayed with columns: "Vehicle","Group","Driver","Employee ID","Driver ID Source", "Trip Start","Trip End","Duration" & the summary section is displayed with: "ASSIGNED TRIPS", "ASSIGNED BY LYTX BADGE", "ASSIGNED BY VEHICLE", "UNASSIGNED TRIPS" & the graph section is displayed

  @LQ-238
  Scenario: Filter group(s) in driver id assignment page
    Given the "Program Manager" user is in driver id assignment page
    When the user sets group filter to one group in driver id assignment page
    Then the data belong to the group are listed in driver id assignment page

  Scenario: Date range filter in driver id assignment page
    Given the "Program Manager" user opens the date range filter on the Driver Id assignment page
    When the user selects date & the user clicks Apply in driver id assignment page
    Then the data belong to the date range are listed in driver id assignment page

  Scenario: Filter by Driver in driver id assignment page
    Given the "Program Manager" user clicks on "Select Search" filter & the user selects Driver in driver id assignment page
    When the user enters driver name into "Search Name or ID" field & the user selects one name from suggestion list in driver id assignment page
    Then the data belong to the driver name are listed in driver id assignment page

  Scenario: Filter by Vehicle in driver id assignment page
    Given the "Program Manager" user clicks on "Select Search" filter & the user selects "Vehicle" in driver id assignment page
    When the user enters vehicle name into "Search Vehicle Name" field & the user selects one vehicle name from suggestion list in driver id assignment page
    Then the data belong to the vehicle name are listed in driver id assignment page
