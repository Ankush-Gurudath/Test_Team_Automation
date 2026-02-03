Feature: Driver Safety - Home Suite

  @LQ-304
  Scenario: Driver Safety - Home Suite
    Given the login page is displayed
    When the user enters a newly created username/password and clicks the login button
    Then the user is successfully logged into the Driver Safety dashboard

  @LQ-387
  Scenario: View Tasks in Dashboard page
    When the user signs in to Driver Safety
    Then the Dashboard page is displayed & the Drivers count is displayed & the UNASSIGNED DRIVERS count is displayed in last 90 days & the DUE FOR COACHING count is displayed in last 90 days & the FYI NOTIFY count is displayed in last 90 days $ the COLLISIONS count is displayed in last 90 days & the POSSIBLE COLLISIONS count is displayed in last 90 days

  @LQ-390
  Scenario: Links in Tasks in Dashboard page
    When the user clicks link
    Then the page is displayed

  Scenario: Verify Due for Coaching link navigates to the correct page
    When the user clicks Due for Coaching link
    Then the Due for Coaching page is displayed

  Scenario: Verify Collision link navigates to the correct page
    When the user clicks Collision link
    Then the Collision page is displayed

  Scenario: Verify FYI Notify link navigates to the correct page
    When the user clicks FYI Notify link
    Then the FYI Notify page is displayed

#  @LQ-312
#  Scenario: Add recognition in Driver Profile page
#    Given "Safety Manager" user is in Driver Profile page
#    When the user clicks "Add Recognition" button And the user clicks "Complete" button
#    Then the recognition is added

#    since event creation is not available, commenting this test
#  @LQ-310
#  Scenario: Coach event in Driver Profile page
#    When the user clicks "Coach Event" button
#    Then Driver Coaching Session page is opened

  @LQ-392
  Scenario: Views Groups by Highest Score in Dashboard page
    When the user is in Driver Safety
    Then there is "Groups by Highest Score" in "METRICS" & the table are displayed with columns "GROUP", "COACHABLE SCORE", "COACHABLE SCORE TREND", "COACHABLE EVENTS", COACHABLE EVENTS TREND

  @LQ-398
  Scenario: View Coaches by Lowest Effectiveness in Dashboard page
    When the user is in Dashboard page
    Then there is "Coaches by Lowest Effectiveness" in "METRICS" & the table are displayed with columns "COACH", "COACHING EFFECTIVENESS", "AVG DAYS TO COACH", "COACHED EVENTS", WITH NOTES

  @LQ-404
  Scenario: View Drivers by Highest Score in Dashboard page
    When the user landed in Driver Safety
    Then there is "Drivers by Highest Score" in "METRICS" & the table are displayed with columns "DRIVER", "COACHABLE SCORE", "TREND", IMPACT

  @LQ-407
  Scenario: View Behaviors by Highest Frequency in Dashboard page
    When the user is back to Driver Safety
    Then there is "Behaviors by Highest Frequency" in "METRICS" & the table are displayed with columns "BEHAVIOR", "FREQ.", TREND

  @LQ-409
  Scenario: Filter group in Dashboard page
    When the user sets group filter to one group
    Then the data belong to the group are listed in "TASKS" & in other metrics

  Scenario: Filter date in Dashboard page
    When the user sets date filter
    Then the data belong to last 90 days are listed in "TASKS" & in other metrics

#  @LQ-307
#  Scenario: Search event in Quick Search box
#    Given Safety Manager user is in Driver Safety
#    When the user clicks "SEARCH" button in left navigation & the user inputs a valid event id & the user clicks search icon
#    Then preview modal of the searched event is opened

  @LQ-309
  Scenario: View Driver Profile page
    Given "Safety Manager" user is in Driver Report page
    When the user clicks driver name
    Then Driver Profile page is opened & the driver info is displayed

  Scenario: View Continual Behaviors tab in Driver Profile page
    When the user clicks Continual Behaviors tab
    Then the Continual Behaviors drop down is shown & the Summary section & the Incidents section is displayed

  Scenario: View Coaching History tab in Driver Profile page
    When the user clicks Coaching History tab
    Then the table is displayed with columns:"SESSION ID","COACH DATE","OVERDUE DATE", "BEHAVIORS COACHED","COACH", NOTES

  Scenario: View Recognitions tab in Driver Profile page
    When the user clicks Recognitions tab
    Then the table is displayed with columns:"TYPE","EVENT ID","ISSUED BY","ISSUED DATE", RECOGNITION REASON
