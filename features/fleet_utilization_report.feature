Feature: End to end Utilization Report workflow
  As a developer,
  I want to run end to end tests on the Fleet Maint application
  So I can confirm that code changes have not adversely affected the app.


  @LQ-52158
  Scenario: view Distance tab in Fleet Utilization page
    Given the user is login with "Fleet Dispatcher"
    When the user clicks "Insights" and the user clicks "Fleet Utilization"
    Then the Distance tab of Fleet Utilization is displayed

  @LQ-47531
  Scenario: Filter by date in Fleet Utilization Distance page
    When the user sets date in the date filter
    Then the data with selected filters are displayed on the "Average Distance" trend, "Distance by Group", "Distance by Vehicle"

  @LQ-47527
  Scenario: Filter by group in Fleet Utilization Distance page
    When the user sets group filter to one group
    Then the data with selected filters are displayed on the "Average Distance" trend, "Distance by Group", "Distance by Vehicle"

  @LQ-47538
  Scenario: Views Distance by Group in Fleet Utilization page
     When the user clicks "Fleet Utilization"
     Then Distance by Group table  is displayed with columns "GROUP", "TOTAL VEHICLE", "TOTAL", "AVG/DAY"

  @LQ-47540
  Scenario: Views Distance by Vehicle in Fleet Utilization page
     When the user clicks "Fleet Utilization" in Insights
     Then Distance by Vehicle table is displayed with columns "VEHICLE", "GROUP", "TOTAL", "AVG/DAY"


  @LQ-52160
  Scenario: View detail ink in Distance by Group widget in Fleet Utilization page
     When the user clicks "view details" in Distance by Group widget
     Then the "fleet operation group tab" page is displayed

  @LQ-74987
  Scenario: Group name link in Distance by Group table in Fleet Utilization page
     When the user clicks "group name" from group column in Distance by Group table
     Then the fleet operation group page is displayed with same group filter

  @LQ-47532
  Scenario: View detail ink in Distance by Vehicle widget in Utilization Report page
     When the user clicks "view details" in Distance by Vehicle widget
     Then the "fleet operation vehicle tab" page is displayed

  Scenario: Vehicle name link in Distance by Vehicle widget in Utilization Report page
     When the user clicks "vehicle name" in Distance by Vehicle widget
     Then the "vehicle profile" page is displayed

  @LQ-52171
  Scenario:view Engine Hours tab in Utilization Report page
     When the user clicks "Engine Hours"
     Then the Engine Hours tab of Fleet Utilization is displayed

  @lQ-47543
    Scenario: Filter by date in Fleet Utilization Engine Hours page
    When the user sets date in the date filter in engine hours page
    Then the data with selected filters are displayed on the "Average Engine Hours" trend, "Engine Hours by Group", "Engine Hours by Vehicle"

  @LQ-47541
  Scenario: Filter by group in Fleet Utilization EngineHours page
    When the user sets group filter to one group in engine hours tab
    Then the data with selected filters are displayed on the "Average Engine Hours" trend, "Engine Hours by Group", "Engine Hours by Vehicle"

  @LQ-47544
  Scenario: Views Engine Hours by Group in Fleet Utilization page
     When the user clicks "Engine Hours" tab in Fleet Utilization
     Then Engine Hours by Group table  is displayed with columns "GROUP", "TOTAL VEHICLE", "TOTAL", "AVG/DAY"

  @LQ-47545
  Scenario: Views Engine Hours by Vehicle in Fleet Utilization page
     When the user clicks "Engine Hours" tab in Insights-Fleet Utilization
     Then Engine Hours by Vehicle table is displayed with columns "VEHICLE", "GROUP", "TOTAL", "AVG/DAY"


  @LQ-52170
  Scenario: View detail ink in Engine Hours by Group widget in Fleet Utilization page
     When the user clicks "view details" in Engine Hours by Group widget
     Then the "fleet operation group tab" of Engine Hours is displayed

  @LQ-75141
  Scenario: Group name link in Engine Hours by Group table in Fleet Utilization page
     When the user clicks "group name" from group column in Engine Hours by Group widget
     Then the fleet operation group page of Engine Hours is displayed with same group filter

  @LQ-47547
  Scenario: View detail ink in Engine Hours by Vehicle widget in Utilization Report page
     When the user clicks "view details" in Engine Hours by Vehicle widget
     Then the "fleet operation vehicle tab" Engine Hours is displayed

  Scenario: Vehicle name link in Engine Hours by Vehicle widget in Utilization Report page
     When the user clicks "vehicle name" in Engine Hours by Vehicle widget
     Then the "vehicle profile" page of Engine Hours is displayed










