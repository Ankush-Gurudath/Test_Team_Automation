Feature: Sanity Test - Pod2 Prod

  @LQ-306
  Scenario: Sanity Test - Pod2 Prod
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

  @LQ-93743
  Scenario: View Safe Driving Trend in Dashboard page - Driver
    When the user is back to Driver Safety
    Then there is "Safe Driving Trend" in "METRICS" and the graph and pi chart is displayed

  @LQ-93743
  Scenario: View Safe Driving Trend in Dashboard page - Group
    When the user is back to Driver Safety
    Then there is "Groups by Highest % Safe Drivers" in "METRICS" and the table contains columns "group","% safe drivers", "eligible for recognition", "recognized"

  @LQ-266
  Scenario: View Due For Coaching tasks
    Given Safety Manager user is in Driver Safety
    When the user clicks "TASKS" & the user clicks DUE FOR COACHING
    Then the task count is displayed & there are some information on the card

  @LQ-274
  Scenario: View Driver Coaching Session page
    When the user clicks "Coach X Events" of the first bundle card
    Then the Driver Coaching Session page is opened &  there is driver info in the page

  @LQ-313
  Scenario: View Assign Driver tasks
    When the user clicks "TASKS" and the user clicks "ASSIGN DRIVERS"
    Then the task count is displayed & there is "Assign Selected" button with un-selectable status & there is "Move Group" button with un-selectable status & there are "VEHICLE", "GROUP", "EVENT DATE", "EVENT ID", "BEHAVIORS" column & there are checkbox & "ASSIGN" button for each Assign Driver task

  @LQ-318
  Scenario: View Collisions tasks
    When the user clicks "TASKS" and the user clicks "COLLISIONS"
    Then the task count is displayed and there are "DRIVER NAME", "GROUP", "VEHICLE", "EVENT DATE", "TIME" for each card and there is "Preview" button

  @LQ-325
  Scenario: View FYI Notify tasks
    When the user clicks "TASKS" & the user clicks "FYI NOTIFY"
    Then  there are "GROUP", "VEHICLE", "EVENT DATE", "TIME" for each card & there is "Preview" button

  @LQ-383
  Scenario: Driver Safety - Insights Suite
    When the user clicks "INSIGHTS" and the user clicks "OPEN TASKS REPORT" in Open Tasks Report page
    Then the Event profile page is displayed in Open Tasks Report page

  @LQ-339
  Scenario: View Driver Scores in Drivers Report page
    When the user clicks "INSIGHTS" and the user clicks "DRIVERS REPORT" in Drivers Report page
    Then the Driver Scores tab is selected and the number of drivers is displayed and the table is displayed with columns "DRIVER NAME", "GROUP", "COACHABLE SCORE Total", "COACHABLE SCORE Trend", "COACHABLE EVENTS Total", "COACHABLE EVENTS Trend", "TOTAL SCORE Total", "TOTAL SCORE Trend", "TOTAL EVENTS Total", "TOTAL EVENTS Trend" in Drivers Report page

  @LQ-366
  Scenario: View Group Report page
    When the user clicks "INSIGHTS" And the user clicks "GROUP REPORT" in Group Report page
    Then the number of group is displayed and the table is displayed with columns "GROUP", "# OF VEHICLES", "COACHABLE SCORE Total", "COACHABLE SCORE Trend", "COACHABLE EVENTS Total", "COACHABLE EVENTS Trend" in Group Report page

  @LQ-379
  Scenario: View Coaches Report page
    When the user clicks "INSIGHTS" And the user clicks "COACHES REPORT" in Coaches Report page
    Then the number of coaches is displayed  in Coaches Report page And the table is displayed with columns "COACH", "GROUP", "COACHING EFFECTIVENESS", "AVG DAYS TO COACH", "COACHED EVENTS", "WITH NOTES", "LAST LOGIN" in Coaches Report page

  @LQ-369
  Scenario: View Program Status Report page
    When the user clicks "INSIGHTS" And the user clicks "PROGRAM STATUS REPORT" in Program Status Report page
    Then the number of subgroups is displayed And the table is displayed with columns "GROUP", "# OF DEVICES", "UNASSIGNED DRIVERS", "OVERDUE FOR CHECK-IN", "OVERDUE FOR COACHING", "COACHING EFFECTIVENESS", "PROGRAM EFFECTIVENESS" in Program Status Report page

  @LQ-372
  Scenario: View Behaviors Report page
    When the user clicks "INSIGHTS" and the user clicks "BEHAVIORS REPORT" in Behaviors Report page
    Then the number of behaviors is displayed and  the table is displayed with columns "BEHAVIOR", "FREQUENCY", "TREND" in Behaviors Report page

  @LQ-263
  Scenario: Driver Safety - Library  - Events Suite
    When the user clicks "LIBRARY" and then clicks "EVENTS"
    Then the events page is displayed and the table is displayed with columns "EVENT ID","DRIVER","GROUP","VEHICLE","EVENT DATE","SCORE","STATUS","TRIGGER" and "BEHAVIORS"

  @LQ-400
  Scenario: The session list is displayed
    When the user clicks "LIBRARY" and then clicks "COACHING HISTORY"
    Then the Coaching History page is displayed and the table is displayed with columns "SESSION ID", "COACH DATE", "OVERDUE DATE", "DRIVER","BEHAVIORS COACHED","GROUP","COACH","NOTES" and the coaching sessions count is displayed

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

  @LQ-254
  Scenario: Edit user page loaded successfully
    When the "Full Access" user is in the Edit User page
    Then Edit user page displayed

  @LQ-236
  Scenario: Admin - Vehicle Management Suite
    When the user clicks the "VEHICLES" tab
    Then the page header "VEHICLE MANAGEMENT" and the vehicle count are displayed and the table is displayed with columns: "VEHICLE", "GROUP", "DRIVER", "DEVICE", "LAST CHECK IN", "STATUS"

  @LQ-239
  Scenario: Add vehicle page is displayed
    When the user clicks on "Add Vehicle"
    Then the Add vehicle page is displayed

  @LQ-230
  Scenario: The Device Management page is displayed correctly
    When the user clicks the "DEVICES" tab
    Then the page header "DEVICE MANAGEMENT" is displayed and the user count are displayed and the table is displayed with columns: "DEVICE", "DEVICE TYPE", "VEHICLE", "GROUP", "LAST CONNECTED", "INITIAL CONNECTION"

  @LQ-4456
  Scenario: The Device profile page is opened
    When the user clicks a device link
    Then the "DEVICE PROFILE" page is opened

  @LQ-3557
  Scenario: The Geofence Management page is displayed
    When the user clicks "GEOFENCES"
    Then the page header "GEOFENCE MANAGEMENT" and geofence count are displayed and the table is displayed with columns: "GEOFENCE", "GROUP", "RECENT ACTIVITY", "STATUS", "ASSETS", "TRIGGER TYPE", "CREATED DATE", "SOURCE"

  @LQ-12128
  Scenario: The Trailer Management page is displayed
    When the user clicks the "TRAILER" tab
    Then the page header "TRAILER MANAGEMENT" is displayed and the table is displayed with columns: "TRAILER", "GROUP", "LICENSE PLATE", "VIN", "INSPECTION LIST"

  @LQ-242
  Scenario: Admin - Config Setting & Trailer Management Suite
    When the user clicks CONFIG SETTING
    Then Full access role is in tier 1 by default

  @LQ-7126
  Scenario: Admin - Equipment Suite
    When the user clicks the "EQUIPMENT" tab
    Then the page header "EQUIPMENT MANAGEMENT" is displayed and the table is displayed with columns: "EQUIPMENT", "DEVICE", "GROUP", "LAST CONNECTED", "STATUS"

  @LQ-136386
  Scenario: Verify the sub-menu "Consent Report" sub-menu under "Insights" menu.
    When the user click on the "Consent Report" module
    Then the user should see all the filter like "All Available Groups", "Status", "Search Name or ID" and "Reset"
    And the user should see the count of Drivers with tabs named "Facial ID", "Video Safety" and "Distraction and Fatigue Detection"

  @LQ-157939
  Scenario: To verify the elements and columns present in the Consent Report page.
#    When the user is in "Facial ID" product tab   # This step is commented because by default Facial ID tab is selected
    Then the user should see the title "Consent Report" and the user should see the columns "NAME","GROUPS","STATUS", "SENT DATE" and "REQUESTED DATE"
    And the user see the options "0 selected","Clear All","Download PDF", "Revoke Consent" and "CSV"



  @LQ-12437
  Scenario: DVIR Suite
    When the user clicks DVIR
    Then Total reports count, reset button, group filter, date filter, status filter, defect filter and wild search filter are shown on "DRIVER VEHICLE INSPECTION REPORTS" page and table columns are: "REPORT ID", "TYPE", "STATUS", "REPORT DATE", "DRIVER", "VEHICLE", "MAJOR VEHICLE DEFECTS", "MINOR VEHICLE DEFECTS", "VEHICLE INSPECTION LIST", "TRAILER", "MAJOR TRAILER DEFECTS", "MINOR TRAILER DEFECTS", "TRAILER INSPECTION LIST", "MECHANIC/AGENT", "REVIEWER"

  @LQ-12436
  Scenario: View Vehicle Schedule table
    When user clicks "SCHEDULE" on left navigation
    Then the page header "INSPECTION SCHEDULES" is displayed & the count of the vehicle schedule report is displayed & the table is displayed with columns

  @LQ-12461
  Scenario: View Trailer Schedule table
    When user clicks "SCHEDULE" on left navigation & user clicks "Trailer Schedule"
    Then the page header "INSPECTION SCHEDULES" is displayed & the count of the trailer schedule report is displayed & the table is displayed with columns

  @LQ-12446
  Scenario: Default list of vehicle list
    When the "Full Access" user is in the Vehicle list page
    Then the title "VEHICLE INSPECTION LISTS" is displayed & there is a default vehicle inspection list and named "Default" & there is a duplicate icon behind the list name

  @LQ-12447
  Scenario: Default list of Trailer list
    When the "Full Access" user is in the Trailer list page
    Then the title "TRAILER INSPECTION LISTS" is displayed & there is a default trailer inspection list and named "Default" & there is a duplicate icon behind the list name

  @LQ-12430
  Scenario: The Vehicle Assignment page is displayed
    When the user clicks the "List Settings" tab & the user clicks "List Assignment"
    Then the page header "INSPECTION LIST ASSIGNMENT" is displayed & the vehicle count is displayed & the table is displayed with columns: "VEHICLE", "GROUP", "VEHICLE TYPE" and "INSPECTION LIST"

  @LQ-12433
  Scenario: The Trailer Assignment page is displayed
    When the user clicks the "Trailer Assignment" tab
    Then the page header "INSPECTION LIST ASSIGNMENT" is displayed & the trailer count is displayed & the table is displayed with columns: "TRAILER", "GROUP", "TRAILER TYPE" and "INSPECTION LIST"

  @LQ-15218
  Scenario: Fleet - Map Suite
    When the user clicks on Map
    Then the Fleet application is displayed


  @LQ-511
  Scenario: Fleet - Maint Suite
    When the user navigates to Maintenance -> Preventative Maintenance
    Then the Preventative Main labels are shown - Upcoming Services, History & Manage Services


   @LQ-522
  Scenario: View History in PM page
    When the user clicks "History"
    Then the table is displayed with columns: "VEHICLE", "GROUP", "SERVICE", "INTERVAL", "DATE SERVICED", "ODOMETER", "ENGINE HOURS", "NOTES", "ACTION" & the number of Services is displayed


  @LQ-527
  Scenario: User can access the Preventative Maintenance dashboard Manage Services page
    When the user clicks "Manage Services"
    Then the Manage Services page is displayed


  @LQ-531
  Scenario: User can access the Diagnostic Trouble Codes dashboard
    When the user navigates to Maintenance -> Diagnostic Trouble Codes
    Then the DTC page is displayed and the number of Codes, group filter and reset icon are displayed on the header bar and the table is displayed with columns: "VEHICLE", "GROUP", "DATE", "CODE (DESCRIPTION)"


  @LQ-544
  Scenario: Fleet - Insights Suite
    When the user navigates to Insights -> Fleet Operations
    Then the groups tab of Fleet Operations page is displayed


  @LQ-549
  Scenario: User can access the Fleet Operations dashboard drivers tab
    When the user clicks Drivers in Fleet Operations page
    Then the drivers tab of Fleet Operations page is displayed

  @LQ-558
  Scenario: View metadata bar in Driver Profile page
    When the user clicks a driver name
    Then the driver name is displayed and the metadata bar is displayed with labels: "EMPLOYEE ID", "GROUP", "VEHICLE NAME", "EMAIL"

  Scenario: View summary section in Driver Profile page
    When the user clicks the expand icon on the summary section
    Then view type buttons are displayed: "Daily Avg", "Total"
    And the summary section is displayed with labels: "ROUTE TIME", "DISTANCE", "TRIPS", "STOPS", "STOP TIME", "DRIVING TIME", "ENGINE HOURS", "IDLE VIOLATIONS", "IDLE DURATION", "SPEED VIOLATIONS", "SPEEDING DURATION" on driver profile page

  @LQ-547
  Scenario: User can access the Fleet Operations dashboard vehicles tab
    When the user clicks Vehicles in Fleet Operations page
    Then the vehicles tab of Fleet Operations page is displayed

  @LQ-545
  Scenario: Search Vehicles in Fleet Operation Vehicles page
    When the user inputs some characters in Search Vehicles box
    And the user selects one vehicle
    Then the vehicle profile page is displayed

  @LQ-550
  Scenario: View metrics in Fleet data page
    When the user clicks "INSIGHTS" and the user clicks "FLEET DATA"
    Then the metrics is displayed with columns: "AVERAGE", "TOTAL"
    And the metrics is displayed with values: "DISTANCE", "ENGINE HOURS", "DRIVING HOURS", "IDLE TIME", "IDLE PTO TIME", "FUEL CONSUMED", "DRIVING FUEL", "IDLING FUEL", "PTO IDLING FUEL", "FUEL ECONOMY", "DRIVING FUEL ECONOMY"

  Scenario: View groups table in Fleet data page
    When the user clicks "GROUP" tab
    Then the table is displayed with columns: "GROUP", "DISTANCE, "ENGINE HOURS, "DRIVING HOURS", "IDLE TIME", "IDLE PTO TIME", "FUEL CONSUMED", "DRIVING FUEL", "IDLING FUEL", "PTO IDLING FUEL", "FUEL ECONOMY", "DRIVING FUEL ECONOMY"

  Scenario: View vehicles table in Fleet data page
    When the user clicks "VEHICLE" tab
    Then the table is displayed with columns: "VEHICLE", "ODOMETER READING", "DISTANCE", "ENGINE HOURS", "DRIVING HOURS, "IDLE TIME", "IDLE PTO TIME", "FUEL CONSUMED", "DRIVING FUEL", "IDLING FUEL", "PTO IDLING FUEL", "FUEL ECONOMY", "DRIVING FUEL ECONOMY"

  @LQ-7134
  Scenario: Fleet - Insights - User can access the Equipment Status dashboard
    When the user clicks "INSIGHTS" and then clicks "EQUIPMENT STATUS"
    Then the table is displayed with columns: "EQUIPMENT", "GROUP", "DEVICE SERIAL NUMBER", "LAST LOCATION", "LAST CONNECTED", "LAST MOVEMENT", "STATIONARY DURATION", "BATTERY LEVEL"

  @LQ-519
  Scenario: User can access the Geofences dashboard
    When the user navigates to Insights -> Geofences
    Then the Geofences page is displayed

  @LQ-562
  Scenario: View metadata bar in Geofence Profile page
    When the user clicks a geofence or search and select a geofence to go to geofence profile page
    Then the metadata bar is displayed with labels: "GEOFENCE NAME", "DATE CREATED", "DAYS APPLIED", "RANGE OF TIME", "Trigger Type", "GROUP", "SUBGROUPS", "VEHICLES"

  @LQ-514
  Scenario: View table in State Mileage page
    When the user navigates to Insights -> State Mileage
    Then the State Mileage page is displayed and the table is displayed with columns: "VEHICLE", "GROUP", "DEVICE SERIAL", "STATE,COUNTRY", "DISTANCE" and the number of records is displayed

  Scenario: View summary in State Mileage page
    When the user clicks "INSIGHTS" and the user clicks "STATE MILEAGE"
    Then the summary contains "METRICS", "TOTAL", "TOTAL DISTANCE", distance for each state

  @LQ-457
  Scenario: User can access the Data Export dashboard
    When the user clicks "INSIGHTS" and the user selects "DATA EXPORT
    Then there are group, date, vehicle filters and the table is displayed with columns "ACTION", "REPORT TYPE", "GROUP", "START DATE", "END DATE", "VEHICLE", "REQUESTED DATE


  @LQ-15219
  Scenario: Video Search Suite
    When user enters username and password and hits SignIn button
    Then the user is successfully logged into the Video Search page

  @LQ-205
  Scenario: The table show in vehicles page
    When the Video Reviewer Plus user is in Video Search page
    Then the vehicle count is displayed and the table is displayed with columns: "ACTIONS", "VEHICLES", "DEVICE", "LAST COMMUNICATED", "GROUP", "VIEWS"


  @LQ-207
  Scenario: The columns are listed in Saved Video page
    When the user clicks on the Library and the user selects Saved Videos
    Then the video count is displayed and the table is displayed with columns: "VIDEO NAME","STATUS","TAG TYPE","VEHICLE","GROUP","LENGTH","VIEWS","VIDEO DATE","REQUEST DATE"


  @LQ-10128
  Scenario: The columns are listed in Video Tags page
    When the user clicks on the Library and the user selects Video Tags
    Then the video tag count is displayed and the table is displayed with columns: "ACTIONS","VEHICLE","TAG NAME","CATEGORY","AVAILABLE VIEWS","GROUP","RECORD DATE"


 @LQ-204
   Scenario: Navigate to Browser in VIDEO BROWSER page from vehicles page
 #    Given "Video Reviewer Plus" user is in VIDEO SEARCH
     When user clicks on "Browse" from the ACTIONS for one vehicle
     Then user is navigated to "Browser" in VIDEO BROWSER page

   Scenario: Navigate to Live in VIDEO BROWSER page from vehicles page
     When user clicks on "Live" from the ACTIONS for one vehicle
     Then user is navigated to "Live" in VIDEO BROWSER page

   @LQ-203
   Scenario: Live stream of a vehicle
     When the user clicks on "live" link
     Then the outside video is live played on the left and the map is displayed on the right with current position and the GSP speed is displayed on the bottom

   @LQ-202
   Scenario: Save video for all the views when browse
     Given "Video Reviewer Plus" user is in browser tab of VIDEO BROWSER page
     When user clicks on the "Save To Library" button and user enters a video name in input box and user clicks "Save" button and user clicks "Go To Video" button on the success popup modal
     Then the 120 seconds video for all the views is received and the user is navigated to Video Player page

    @LQ-373
  Scenario: RDS Tests
    Given the welcome login page is displayed for RDS company
    When the user login WS for a risk company
    Then the Dashboard page is displayed and the Dashboard page includes "Drivers by Highest Score","Categories by Highest Frequency" and And the Dashboard page includes a driver counts, Group filter, Date filter

  @LQ-378
  Scenario: View drivers report in RDS company
    When the user clicks "INSIGHTS" & the user clicks "DRIVERS REPORT"
    Then the drivers report page is opened & there are 3 tabs： "Drivers Scores","Continual Behaviors", "Alerts" & the table of "Driver Scores" is displayed