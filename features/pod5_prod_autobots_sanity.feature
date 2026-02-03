Feature: Sanity Test - Pod5 Autobots Prod

  @LQ-306
  Scenario: Sanity Test - Pod5 Autobots Prod
    Given the login page is displayed in the browser
    When the user enters a newly created username/password and clicks the login button in the page
    Then the user is successfully logged into the Driver Safety dashboard in the same company

  @LQ-387
  Scenario: View Tasks in Dashboard page
    When the user signs in to Driver Safety
    Then the Dashboard page is displayed & the Drivers count is displayed & the UNASSIGNED DRIVERS count is displayed in last 90 days & the DUE FOR COACHING count is displayed in last 90 days & the FYI NOTIFY count is displayed in last 90 days $ the COLLISIONS count is displayed in last 90 days & the POSSIBLE COLLISIONS count is displayed in last 90 days

  @LQ-390
  Scenario: Links in Tasks in Dashboard page
    When the user clicks link
    Then the page is displayed

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

  @LQ-383
  Scenario: Driver Safety - Insights Suite
    When the user clicks "INSIGHTS" and the user clicks "OPEN TASKS REPORT" in Open Tasks Report page
    Then the Event profile page is displayed in Open Tasks Report page

  @LQ-391
  Scenario: View Recognition History
    When the user clicks "LIBRARY" and the user clicks "RECOGNITION HISTORY"
    Then all recognition history are displayed and the table is displayed with columns "TYPE","DRIVER","GROUP","EVENTID","ISSUED BY","ISSUED DATE","RECOGNITION REASON"

  @LQ-386
  Scenario: View Data Export page
    When the user clicks "LIBRARY" and the user clicks "DATA EXPORT"
    Then the requested records are displayed and the table is displayed with columns "REPORT TYPE", "GROUP", "DATE RANGE", "FILTERS", "REQUESTED DATE","ACTION" and a "New Export" button

  @LQ-251
  Scenario: The Admin page is displayed
    When the user clicks on Admin tab
    Then the page header "USER MANAGEMENT" is displayed and the user count are displayed and the table is displayed with columns: "NAME", "EMPLOYEE ID", "LYTX BADGE", "PRIMARY DRIVER GROUP", "ROLES (GROUP)", "STATUS", "LOGIN", "USERNAME"

  @LQ-230
  Scenario: The Device Management page is displayed correctly
    When the user clicks the "DEVICES" tab
    Then the page header "DEVICE MANAGEMENT" is displayed and the user count are displayed and the table is displayed with columns: "DEVICE", "DEVICE TYPE", "VEHICLE", "GROUP", "LAST CONNECTED", "INITIAL CONNECTION"

  @LQ-12437
  Scenario: DVIR Suite
    When the user clicks DVIR
    Then Total reports count, reset button, group filter, date filter, status filter, defect filter and wild search filter are shown on "DRIVER VEHICLE INSPECTION REPORTS" page and table columns are: "REPORT ID", "TYPE", "STATUS", "REPORT DATE", "DRIVER", "VEHICLE", "MAJOR VEHICLE DEFECTS", "MINOR VEHICLE DEFECTS", "VEHICLE INSPECTION LIST", "TRAILER", "MAJOR TRAILER DEFECTS", "MINOR TRAILER DEFECTS", "TRAILER INSPECTION LIST", "MECHANIC/AGENT", "REVIEWER"

  @LQ-12436
  Scenario: View Vehicle Schedule table
    When user clicks "SCHEDULE" on left navigation
    Then the page header "INSPECTION SCHEDULES" is displayed & the count of the vehicle schedule report is displayed & the table is displayed with columns

  @LQ-12446
  Scenario: Default list of vehicle list
    When the "Full Access" user is in the Vehicle list page
    Then the title "VEHICLE INSPECTION LISTS" is displayed & there is a default vehicle inspection list and named "Default" & there is a duplicate icon behind the list name


  @LQ-15218
  Scenario: Fleet - Map Suite
    Given "Fleet read only" user is in Fleet Dashboard
    When the user clicks on Map
    Then the Fleet application is displayed


  @LQ-544
  Scenario: Fleet - Insights Suite
    When the user navigates to Insights -> Fleet Operations
    Then the groups tab of Fleet Operations page is displayed


  @LQ-549
  Scenario: User can access the Fleet Operations dashboard drivers tab
    When the user clicks Drivers in Fleet Operations page
    Then the drivers tab of Fleet Operations page is displayed

  @LQ-15219
  Scenario: Video Search Suite
    Given the login page is displayed in Video Search
    When user enters username and password and hits SignIn button
    Then the user is successfully logged into the Video Search page

  @LQ-373
  Scenario: RDS Tests
   #Scenario: View Dashboard page of RDS company
    Given the welcome login page is displayed for RDS company
    When the user login WS for a risk company
    Then the Dashboard page is displayed and the Dashboard page includes "Drivers by Highest Score","Categories by Highest Frequency" and And the Dashboard page includes a driver counts, Group filter, Date filter

  @LQ-378
  Scenario: View drivers report in RDS company
    When the user clicks "INSIGHTS" & the user clicks "DRIVERS REPORT"
    Then the drivers report page is opened & there are 3 tabs： "Drivers Scores","Continual Behaviors", "Alerts" & the table of "Driver Scores" is displayed
