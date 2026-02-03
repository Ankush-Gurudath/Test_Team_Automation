Feature: Insights

#InsightsOpentaskReport
  @LQ-384
  Scenario: WS - Insights - Filter group in Open Tasks Report page
    Given the coach user logs in
    When the user clicks "INSIGHTS" and the user clicks "OPEN TASKS REPORT" And the user sets group filter to one group in Open Tasks Report page
    Then the data belong to the group are listed in Open Tasks Report page

  Scenario: Search driver in Open Tasks Report page
    When the user enters some characters into "Search Name or ID" field in Open Tasks Report page
    Then the data belong to the driver are listed in Open Tasks Report page

  @LQ-383
  Scenario: View Open Tasks Report page
    When the user clicks "INSIGHTS" and the user clicks "OPEN TASKS REPORT" in Open Tasks Report page
    Then the number of drivers is displayed in Open Tasks Report page

  @LQ-385
  Scenario: Links in Open Tasks Report page
    When the user clicks the Tasks Link in Open Tasks Report page
    Then the Event profile page is displayed in Open Tasks Report page

##DriversReport
  @LQ-339
  Scenario: View Driver Scores in Drivers Report page
    When the user clicks "INSIGHTS" and the user clicks "DRIVERS REPORT" in Drivers Report page
    Then the Driver Scores tab is selected and the number of drivers is displayed and the table is displayed with columns "DRIVER NAME", "GROUP", "COACHABLE SCORE Total", "COACHABLE SCORE Trend", "COACHABLE EVENTS Total", "COACHABLE EVENTS Trend", "TOTAL SCORE Total", "TOTAL SCORE Trend", "TOTAL EVENTS Total", "TOTAL EVENTS Trend" in Drivers Report page

  @LQ-340
  Scenario: Filter group in Driver Scores in Drivers Report page
    When the user sets group filter to one group in Drivers Report page
    Then the data belong to the group are listed in Drivers Report page

  Scenario: Filter date in Driver Scores in Drivers Report page
    When the user sets date filter in Driver Scores in Drivers Report page
    Then the data belong to the date are listed in Driver Scores in Drivers Report page

  Scenario: Filter behavior in Driver Scores in Drivers Report page
    When the user sets behavior filter to one behavior in Driver Scores in Drivers Report page
    Then the data belong to the behavior are listed in Driver Scores in Drivers Report page

  Scenario: Search driver in Driver Scores in Drivers Report page
    When the user enters some characters into "Search Name or ID" field in Driver Scores and the user selects a driver from the suggestion list in Drivers Report page
    Then the data belong to the driver are listed in Driver Scores in Drivers Report page

  @LQ-341
  Scenario: Links in Driver Scores in Drivers Report page
    When the user clicks the Driver Scores link in Drivers Report page
    Then the Driver Profile page is displayed in Drivers Report page

  @LQ-342
  Scenario: View Continual Behaviors in Drivers Report page
    When the user clicks "Continual Behaviors" in Drivers Report page
    Then the Continual Behaviors tab is selected and the number of drivers is displayed and the table is displayed with columns "DRIVER NAME", "GROUP", "HANDHELD DEVICE Duration", "HANDHELD DEVICE % Of Drive Time", "INATTETIVE Duration", "INATTETIVE % Of Drive Time", "FOOD OR DRINK Duration", "FOOD OR DRINK % Of Drive Time", "DRIVER SMOKING Duration", "DRIVER SMOKING % Of Drive Time", "POLICY SPEED Duration", "POLICY SPEED % Of Drive Time", "NO SEAT BELT Duration", "NO SEAT BELT % Of Drive Time" in Drivers Report page

  @LQ-343
  Scenario: Filter group in Continual Behaviors in Drivers Report page
    When the user sets group filter to one group in continual behavior in Drivers Report page
    Then the data belong to the group are listed in continual behavior in Drivers Report page

  Scenario: Filter date in Continual Behaviors in Drivers Report page
    When the user sets date filter in continual behavior in Drivers Report page
    Then the data belong to the date are listed in continual behavior in Drivers Report page

  Scenario: Search driver in Continual Behaviors in Drivers Report page
    When the user enters some characters into "Search Name or ID" field in continual behavior and the user selects a driver from the suggestion list in Drivers Report page
    Then the data belong to the driver are listed in continual behavior in Drivers Report page

  @LQ-344
  Scenario: Links in Continual Behaviors in Drivers Report page
    When the user clicks Continual Behaviors tab and clicks the first driver in Drivers Report page
    Then the Driver Profile page for the chosen result is displayed in Drivers Report page

  @ALC-1192
  Scenario: Drivers Report - Continual Behaviors Browse Video Links
    When the user clicks Continual Behaviors tab in driver profile
    Then Browse or Wake Video Links is displayed in Drivers profile page

  @LQ-345
  Scenario: View Alerts in Drivers Report page
    When the user clicks "Alerts" in Drivers Report page
    Then the Alerts tab is selected and the number of drivers is displayed and the table is displayed with columns "DRIVER NAME", "GROUP", "ALERTS Total", "ALERTS Trend" in Drivers Report page

  @LQ-346
  Scenario: Filter group in Alerts in Drivers Report page
    When the user sets group filter to one group in Alert in Drivers Report page
    Then the data belong to the group are listed in Alert in Drivers Report page

  Scenario: Filter date in Alerts in Drivers Report page
    When the user sets date filter in Alert in Drivers Report page
    Then the data belong to the date are listed in Alert in Drivers Report page

  Scenario: Filter behavior in Alerts in Drivers Report page
    When the user sets behavior filter to one behavior in Alert in Drivers Report page
    Then the data belong to the behavior are listed in Alert in Drivers Report page

  Scenario: Search driver in Alerts in Drivers Report page
    When the user enters some characters into "Search Name or ID" field in Alert and the user selects a driver from the suggestion list in Drivers Report page
    Then the data belong to the driver are listed in Alert in Drivers Report page

  @LQ-347
  Scenario: Links in Alerts in Drivers Report page
    When the user clicks the first driver in Alert in Drivers Report page
    Then the Driver Profile page for the chosen result is displayed for Alert in Drivers Report page

#GroupReport
  @LQ-366
  Scenario: View Group Report page
    When the user clicks "INSIGHTS" And the user clicks "GROUP REPORT" in Group Report page
    Then the number of group is displayed and the table is displayed with columns "GROUP", "# OF VEHICLES", "COACHABLE SCORE Total", "COACHABLE SCORE Trend", "COACHABLE EVENTS Total", "COACHABLE EVENTS Trend" in Group Report page

  @LQ-367
  Scenario: Filter group in Group Report page
    When the user sets group filter to one group in Group Report page
    Then the data belong to the group are listed in Group Report page

  Scenario: Filter date in Group Report page
    When the user sets date filter in Group Report page
    Then the data belong to the date are listed in Group Report page

  Scenario: Filter behavior in Group Report page
    When the user sets behavior filter to one behavior in Group Report page
    Then the data belong to the behavior are listed in Group Report page

  Scenario: Set Normalized in Group Report page
    When the user sets Normalized filter to "Normalized by number of Vehicles" in Group Report page
    Then the normalized data are displayed in Group Report page

  @LQ-368
  Scenario: Links in Group Report page
    When the user clicks the Group Link in Group Report page
    Then the Drivers Report page is displayed for the chosen result in Group Report page

#CoachesReport
  @LQ-379
  Scenario: View Coaches Report page
    When the user clicks "INSIGHTS" And the user clicks "COACHES REPORT" in Coaches Report page
    Then the number of coaches is displayed  in Coaches Report page And the table is displayed with columns "COACH", "GROUP", "COACHING EFFECTIVENESS", "AVG DAYS TO COACH", "COACHED EVENTS", "WITH NOTES", "LAST LOGIN" in Coaches Report page

  @LQ-381
  Scenario: Filter group in Coaches Report page
    When the user sets group filter to one group in Coaches Report page
    Then the data belong to the group are listed in Coaches Report page

  Scenario: Filter date in Coaches Report page
    When the user sets date filter in Coaches Report page
    Then the data belong to the date are listed in Coaches Report page

  Scenario: Filter coach in Coaches Report page
    When the user selects "Coaches with Activity" in coach filter in Coaches Report page
    Then the coaches belong to the filter are listed in Coaches Report page

  Scenario: Filter data in Coaches Report page
    When the user selects "Selected Group Data Only" in data filter And the user sets group filter to one group in Coaches Report page
    Then the data only belong to the selected group are listed  in Coaches Report page

  @LQ-382
  Scenario: Links in Coaches Report page
    When the user clicks the Coaches link in Coaches Report page
    Then the Coaches profile is displayed in Coaches Report page

#ProgramStatusReport
  @LQ-369
  Scenario: View Program Status Report page
    When the user clicks "INSIGHTS" And the user clicks "PROGRAM STATUS REPORT" in Program Status Report page
    Then the number of subgroups is displayed And the table is displayed with columns "GROUP", "# OF DEVICES", "UNASSIGNED DRIVERS", "OVERDUE FOR CHECK-IN", "OVERDUE FOR COACHING", "COACHING EFFECTIVENESS", "PROGRAM EFFECTIVENESS" in Program Status Report page

  @LQ-370
  Scenario: Filter group in Driver Scores in Program Status Report page
    When the user sets group filter to one group in program status report page
    Then the data belong to the group are listed in program status report page

  @LQ-371
  Scenario: Unassigned drivers value link in Program Status Report page
    When the user clicks a Unassigned drivers value
    Then the Assign Drivers page is displayed

  Scenario: Group links in Program Status Report page
    When the user clicks a group link
    Then the Program Status Report page is displayed

  Scenario: Overdue for coaching link in Program Status Report page
    When the user clicks a overdue for coaching value
    Then the Due For Coaching page is displayed

  Scenario: Overdue for coaching link in Program Status Report page
    When the user clicks a overdue for coaching value
    Then the Due For Coaching page is displayed

  Scenario: coaching effectiveness link in Program Status Report page
    When the user clicks a coaching effectiveness value
    Then the Coaches Report page is displayed


  @LQ-372
  Scenario: View Behaviors Report page
    When the user clicks "INSIGHTS" and the user clicks "BEHAVIORS REPORT" in Behaviors Report page
    Then the number of behaviors is displayed and  the table is displayed with columns "BEHAVIOR", "FREQUENCY", "TREND" in Behaviors Report page

  @LQ-374
  Scenario: Filter group in Behaviors Report page
    When the user sets group filter to one group in Behaviors Report page
    Then the data belong to the group are listed in Behaviors Report page

#  Scenario: Filter date in Behaviors Report page
#    When the user sets date filter in Behaviors Report page
#    Then the data belong to the date are listed in Behaviors Report page

  @LQ-377
  Scenario: Links in Behaviors Report page
    When the user clicks the first frequency value
    Then the Drivers Report page for the chosen result is displayed

#  @LQ-308
#  Scenario: View Coach Profile page
#    Given Safety Manager user is in Coaches Report page
#    When the user clicks a coach name
#    Then Coach Profile page is opened & the coach info are shown with: "EMPLOYEE ID","GROUP","EMAIL", LAST LOGIN
#
#  Scenario: View Behavior Groups tab in Coach Profile page
#    When the user clicks Behavior Groups tab
#    Then the table is displayed with columns:"BEHAVIOR GROUPS","COACHING EFFECTIVENESS","DRIVER","COACHED BEHAVIORS", REPEATED BEHAVIORS
#
#  @LQ-90415
#  Scenario: Safe Driving Trend - widget
#    When user clicks on Home button
#    Then there is Safe Driving Trend present in Metrics and trend chart is present along with pi-chart
#
#  @LQ-90415
#  Scenario: Groups by highest % Safe drivers - Widget
#    When user clicks on Home button
#    Then there is Groups by highest % Safe drivers trend is present with columns "GROUP", "% SAFE DRIVERS", "ELIGIBLE FOR RECOGNITION", "RECOGNIZED"
#
#  @LQ-90417
#  Scenario: Verify Hyperlinks in Groups by highest % Safe drivers - widget
#    When user clicks on group name
#    Then user should navigate to Safe driving report and same group filter applied in the page
#
#  @LQ-90419
#  Scenario: Verify Hyperlinks in Safe driving Trend - widget
#    When user clicks "Recognize" button in widget
#    Then user should navigate to Safe driving report - drivers page
#
#  @LQ-75797 @LQ-95442
#  Scenario: Driver Safety - Safe Driving Report
#    When the user clicks Insights and clicks Safe Driving Report
#    Then the Safe Driving Report page is loaded correctly the table is displayed with columns: "DRIVER", "GROUP", "DISTANCE DRIVEN", "ACHIEVEMENT", "NON-COACHABLE BEHAVIORS"
#    Then there is a verbiage under the table "Reports are provided for informational purposes only and may vary based on data availability.  Reports may contain data generated by AI, which is not to be used for employment-related decisions without appropriate human supervision."
#
#  @LQ-90421
#  Scenario: Verify tooltip for Achievement
#    When user hover on the Achievement icon
#    Then tool-tip named "Coachable Score of X in XX XXXX" is present
#
#
#  @LQ-121697
#  Scenario: Group filter - Drivers - Safe driving report
#    When user click on group filter and user selects one group
#    Then the data belong to the group are listed in Safe driving Report page
#
#  @LQ-121697
#  Scenario: Quarted filter - Drivers - Safe driving report
#    When user clicks on quarter filter button and user selects first quarter
#    Then data belong to quarter should be displayed
#
#  @LQ-121683
#  Scenario: Include/Exclude drivers with behaviors
#    When user clicks on filter button - include/exclude drivers and user selects first data
#    Then data belongs to drivers should be displayed for include/exclude behaviors
#
#  @LQ-121682
#  Scenario: Search driver - Safe driver report
#    When user clicks and searches the driver name
#    Then data belongs to driver should displayed

@LQ-TB @ProdTests
  Scenario: verify Group report coachable events count matching with events page count
    When the user clicks Insights and clicks Group Report and clicks on first group coachable events count
    Then the events page events count should be same as Group report coachable events count

@LQ-TB
  Scenario: Verify download driver event history report
    When the user clicks download driver event history report
    Then the report is downloaded successfully


