Feature: Sanity Test for EmpireCLS in PROD

  @LQ-306
  Scenario: Sanity Test for PROD Customers
    Given the login page is displayed in the browser
    When the user enters username/password, clicks the login button in the page and select company from the list
    Then the user is successfully logged into the Driver Safety dashboard

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


  @LQ-15219
  Scenario: Video Search Suite
    When user clicks the Video Search tab
    Then the user is placed on the Video Search page

  @LQ-205
  Scenario: The table show in vehicles page
    When the Video Reviewer Plus user is in Video Search page
    Then the vehicle count is displayed and the table is displayed with columns: "ACTIONS", "VEHICLES", "DEVICE", "LAST COMMUNICATED", "GROUP", "VIEWS"

  Scenario: Navigate to Live in VIDEO BROWSER page from vehicles page
    When user clicks on "Live" from the ACTIONS for one vehicle
    Then user is navigated to "Live" in VIDEO BROWSER page

  @LQ-203
  Scenario: Live stream of a vehicle
    When the user clicks on "live" link
    Then the outside video is live played on the left and the map is displayed on the right with current position and the GPS speed is displayed on the bottom

  @LQ-207
  Scenario: The columns are listed in Saved Video page
    When the user clicks on the Library and the user selects Saved Videos
    Then the video count is displayed and the table is displayed with columns: "VIDEO NAME","STATUS","TAG TYPE","VEHICLE","GROUP","LENGTH","VIEWS","VIDEO DATE","REQUEST DATE"

  @LQ-208
  Scenario: View the saved video
    When the user clicks the video name
    Then the video player page is opened and the video is auto-played

  @LQ-10128
  Scenario: The columns are listed in Video Tags page
    When the user clicks on the Library and the user selects Video Tags
    Then the video tag count is displayed and the table is displayed with columns: "ACTIONS","VEHICLE","TAG NAME","CATEGORY","AVAILABLE VIEWS","GROUP","RECORD DATE"