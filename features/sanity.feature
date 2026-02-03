Feature: Sanity Test

  @LQ-306
  Scenario: Sanity Test
    Given the login page is displayed in the browser
    When the user with multi company account enters username/password, clicks the login button in the page and select company from the list
    Then the user is successfully logged into the Driver Safety dashboard
    When the user enters username/password for env1, clicks the login button in the page
    Then there is "Groups by Highest Score" in "METRICS" & the table are displayed with columns "GROUP", "COACHABLE SCORE", "COACHABLE SCORE TREND", "COACHABLE EVENTS", COACHABLE EVENTS TREND
    Then there is "Coaches by Lowest Effectiveness" in "METRICS" & the table are displayed with columns "COACH", "COACHING EFFECTIVENESS", "AVG DAYS TO COACH", "COACHED EVENTS", WITH NOTES
    Then the user is successfully logged into the dashboard 1

  Scenario: Login to Driver Safety with single company account
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
  #Scenario: WS - Insights - Filter group in Open Tasks Report page
   # Given the coach user logs in
    When the user clicks "INSIGHTS" and the user clicks "OPEN TASKS REPORT" in Open Tasks Report page
    Then the Event profile page is displayed in Open Tasks Report page

  @LQ-391
  Scenario: View Coaching History
    When the user clicks "LIBRARY" and the user clicks "COACHING HISTORY"
    Then all coaching history are displayed and the table is displayed with columns "TYPE","DRIVER","GROUP","EVENTID","ISSUED BY","ISSUED DATE","RECOGNITION REASON"

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
    Given full access user logs in DVIR
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

  @LQ-300
  Scenario: Navigate to FLEET TRACKING page from top navigation bar
    Given "Full access" user is in Fleet Dashboard
    When user clicks on "FLEET TRACKING" on top navigation
    Then user is navigated to "FLEET TRACKING" accordingly

  @LQ-15218
  Scenario: Fleet - Map Suite
    Given the login page is displayed
    When the user enters a newly created username/password and clicks the login button
    Then the Fleet application is displayed

    # Commented due to existing bug CXFA-9254
  @LQ-447
  Scenario: Add Geofence Via Suggestion List
    When the user clicks "Clear List" and enters some characters in Search box and selects a geofence in the Suggestion List
    Then the geofence is displayed in Working List and the geofence is displayed on Map

  @LQ-544
  Scenario: Fleet - Insights Suite
  #Scenario: Fleet - Insights - User can access the Fleet Operations dashboard groups tab
    Given user logins to fleet page
    When the user navigates to Insights -> Fleet Operations
    Then the groups tab of Fleet Operations page is displayed

#  @LQ-543
#  Scenario: Filter group in Fleet Operations page Groups tab
#    When the user sets group filter to one group in Fleet Operations page Groups tab
#    Then the data belong to the group are listed in Fleet Operations page Groups tab

  @LQ-549
  Scenario: User can access the Fleet Operations dashboard drivers tab
    When the user clicks Drivers in Fleet Operations page
    Then the drivers tab of Fleet Operations page is displayed

  @LQ-15219
  Scenario: Video Search Suite
    Given the login page is displayed in Video Search
    When the Video Reviewer Plus user enters a newly created username/password and clicks the login button
    Then the user is successfully logged into the Video Search page

  @LQ-201
  Scenario: Filter group in vehicles page
    When the user sets group filter to one group in vehicles page
    Then the vehicles belong to the group are listed

  Scenario: Search by vehicle name in vehicles page
    When the user selects "Vehicle Name" from "Select Search" dropdown and the user input some characters in search bar
    Then the vehicles with the inputted characters are listed

  Scenario: Search by serial number in vehicles page
    When the user selects "Serial Number" from "Select Search" dropdown and the user input some characters in search bar
    Then the vehicles which attached ER serial number with the inputted characters are listed

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
