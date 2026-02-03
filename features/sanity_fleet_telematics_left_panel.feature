Feature: Sanity Test for Fleet Telematics - Left Panel

  @LQ-306
  Scenario: Verify top navigation tab Driver Safety and verify if the data is loaded in the center
    Given the login page is displayed in the browser
    When the user enters username/password, clicks the login button in the page and select company from the list
    Then the user is successfully in the Driver Safety dashboard

  @LQ-
  Scenario: To verify the Expand/Collapse button of the new UI Driver Safety application.
    Then the user should be able to see the left navigation in expand mode by default.
    When the user clicks the left arrow symbol present in the left navigation bar.
    Then the user should see the left navigation bar getting collapsed and the user should see the arrow symbol facing towards right side once it gets collapsed.

  @LQ-136300
  Scenario: Verify left panel and center pages of Driver Safety > Tasks menu > Due For Coaching
    When the user clicks on Tasks > Due For Coaching
    Then the user should see page header Due For Coaching with tasks count

  Scenario: Verify left panel and center pages of Driver Safety > Tasks menu > Assign Drivers
    When the user clicks on Tasks > Assign Drivers
    Then the user should see page header Assign Drivers with tasks count

  Scenario: Verify left panel and center pages of Driver Safety > Tasks menu > Collision
    When the user clicks on Tasks > Collision
    Then the user should see page header Collision with tasks count

  Scenario: Verify left panel and center pages of Driver Safety > Tasks menu > FYI Notify
    When the user clicks on Tasks > FYI Notify
    Then the user should see page header FYI Notify with tasks count

  @LQ-136305
  Scenario: Verify left panel and center pages of Driver Safety > Insights menu > Open Tasks Report
    When the user clicks on Insights > Open Tasks Report
    Then the user should see page header Open Tasks Report with drivers count

  Scenario: Verify left panel and center pages of Driver Safety > Insights menu > Drivers Report
    When the user clicks on Insights > Drivers Report
    Then the user should see page header Drivers Report with drivers count

  Scenario: Verify left panel and center pages of Driver Safety > Insights menu > Group Report
    When the user clicks on Insights > Group Report
    Then the user should see page header Group Report with subgroups count

  Scenario: Verify left panel and center pages of Driver Safety > Insights menu > Coaches Report
    When the user clicks on Insights > Coaches Report
    Then the user should see page header Coaches Report with coaches count

  Scenario: Verify left panel and center pages of Driver Safety > Insights menu > Program Status Report
    When the user clicks on Insights > Program Status Report
    Then the user should see page header Program Status Report with subgroups count

  Scenario: Verify left panel and center pages of Driver Safety > Insights menu > Behaviors Report
    When the user clicks on Insights > Behaviors Report
    Then the user should see page header Behaviors Report with Behaviors count

  @LQ-
  Scenario: Verify left panel and center pages of Driver Safety > Library menu > Events
    When the user clicks on Library > Events
    Then the user should see page header Library with events count

  Scenario: Verify left panel and center pages of Driver Safety > Library menu > Coaching History
    When the user clicks on Library > Coaching History
    Then the user should see page header Coaching History with sessions count

  Scenario: Verify left panel and center pages of Driver Safety > Library menu > Recognition History
    When the user clicks on Library > Recognition History
    Then the user should see page header Recognition History with recognitions count

  @LQ-136319
  Scenario: Verify left panel and center pages of Driver Safety > Library menu > Data Export
    When the user clicks on Library > Data Export
    Then the user should see page header Data Export

  @LQ-
  Scenario: Verify left panel and center pages of Driver Safety > Search
    When the user clicks on Search menu
    Then the user should see Search by event ID text box

  @LQ-152054
  Scenario: Verify top navigation tab Video Search and verify if the data is loaded in the center
    When the user clicks on video search
    Then the user is successfully in the Video Search page. The vehicle count is displayed and the table is displayed with columns: "ACTIONS", "VEHICLES", "DEVICE", "LAST COMMUNICATED", "GROUP", "VIEWS"

  @LQ-
  Scenario: To verify the Expand/Collapse button of the new UI Video Search application.
    Then the user should be able to see the left navigation in expand mode by default.
    When the user clicks the left arrow symbol present in the left navigation bar.
    Then the user should see the left navigation bar getting collapsed and the user should see the arrow symbol facing towards right side once it gets collapsed.

  Scenario: Verify left panel and center pages of Video Search > Map Search menu
    When the user clicks on Video Search > Map Search menu
    Then the user should see page header Map Search with vehicles count

  Scenario: Verify left panel and center pages of Video Search > Library > Saved Videos
    When the user clicks on Video Search > Library > Saved Videos
    Then the user should see page header Saved Videos with vehicles count

  Scenario: Verify left panel and center pages of Video Search > Library > Video Tags
    When the user clicks on Video Search > Library > Video Tags
    Then the user should see page header Video Tags with video tags count

  @LQ-136209
  Scenario: Verify top navigation tab Admin and verify if the data is loaded in the center
    When the user clicks on Admin tab
    Then the page header "USER MANAGEMENT" is displayed and the user count are displayed and the table is displayed with columns: "NAME", "EMPLOYEE ID", "LYTX BADGE", "PRIMARY DRIVER GROUP", "ROLES (GROUP)", "STATUS", "LOGIN", "USERNAME"

  @LQ-
  Scenario: To verify the Expand/Collapse button of the new UI Admin application.
    Then the user should be able to see the left navigation in expand mode by default.
    When the user clicks the left arrow symbol present in the left navigation bar.
    Then the user should see the left navigation bar getting collapsed and the user should see the arrow symbol facing towards right side once it gets collapsed.

  @LQ-136363
  Scenario: Verify left panel and center pages of Admin > Vehicles menu
    When the user clicks on Admin > Vehicles menu
    Then the user should see page header Vehicles with vehicles count

  @LQ-148199
  Scenario: Verify left panel and center pages of Admin > Telematics Assets menu
    When the user clicks on Admin > Telematics Assets menu
    Then the user should see page header Assets, assets tab, cameras tab, and all required UI fields

  @LQ-119298
  Scenario: To verify the "Linked Assets" page of Admin
    When the user clicks Admin - Telematics Assets - Linked Assets
    Then the user should be navigated to the "Linked Assets" page

  @LQ-136223
  Scenario: Verify left panel and center pages of Admin > Device menu
    When the user clicks on Admin > Device menu
    Then the user should see page header Device Management with device count

  @LQ-136374
  Scenario: Verify left panel and center pages of Admin > Geofence menu
    When the user clicks on Admin > Geofence menu
    Then the user should see page header Geofence Management with device count

  @LQ-136375
  Scenario: Verify left panel and center pages of Admin > Insights menu > Driver ID Assignment submenu
    When the user clicks on Admin > Insights menu > Driver ID Assignment submenu
    Then the user should see page header Driver ID Assignment with trips count

  Scenario: Verify left panel and center pages of Admin > Config Settings menu
    When the user clicks on Admin > Config Settings menu
    Then the user should see page header Configuration Settings

    # ---Commenting because of SHARK-2855---
#  @LQ-136400
#  Scenario: Verify left panel and center pages of Admin > Config Settings menu > Safe Driving Report
#    When the user clicks on Config Settings menu > Safe Driving Report
#    Then the user should see page setting, groups and minimum distance driven table headers with only edit icon for root group and edit, delete icons for all other groups

    # ---Commenting because of MEGA-4238---
#   @LQ-172939
#  Scenario: Verify the refresh and browse back functionality in the HOS application
#    Given the "Administrator" user is in NEW UI HOS Application
#    When the user clicks the refresh button in the browser
#    Then the user should be able to see the HOS application and when user click on other app "fleet telematics" and click on back button then user should come back to HOS application

  @LQ-108840
  Scenario: Verify Fleet Telematics tab
    When the user clicks Fleet Telematics tab
    Then the Fleet Telematics main page is loaded successfully

  @LQ-110640
  Scenario: To verify the Expand/Collapse button of the new UI fleet telematics application.
    Then the user should be able to see the left navigation in expand mode by default.
    When the user clicks the left arrow symbol present in the left navigation bar.
    Then the user should see the left navigation bar getting collapsed and the user should see the arrow symbol facing towards right side once it gets collapsed.

  @LQ-110122
  Scenario: To verify all menu's in the Left navigation bar of FLEET TELEMATICS application in New UI
    Then the user should see the tabs in the left Navigation bar such as Dashboard, Map, Productivity, Compliance, Maintenance, Sustainability, Reports, Rules & Exceptions, Messages & Notifications

  @LQ-110112
  Scenario: To validate the refresh and browse back functionality in New UI.
    When the user clicks refresh icon in the browser
    Then the user should see the page getting refreshed and landed to fleet telematics application, click on any menu and the user click back button in the browser and the user should go to the previous page where the user was.

  @LQ-110714
  Scenario: To verify the Productivity menu in the left Navigation bar in Expand Mode
    When the user clicks the dropdown icon present next to "Productivity" menu
    Then the user should see the sub-menus such as Trip History, Routes, Zones, Driver Congregation, Asset Location Sharing, Linked Assets & Risk Management

  Scenario: To verify the 2nd level sub-menus of Productivity in the left Navigation bar
    When the user clicks the dropdown icon present left to "Routes" menu
    Then the user should see the child menus of Routes such as Planned vs Actual, Route Summary, Unmatched Route, Import Routes with a vertical line.
    When the user clicks the dropdown icon present left to "Zones" menu
    Then the user should see the child menus of Zones such as Zones, Zone Visits, Zone Types & Import Zones with a vertical line.

  @LQ-110742
  Scenario: To verify the Compliance menu in the left Navigation bar in Expand Mode
    When the user clicks the dropdown icon present next to "Compliance" menu
    Then the user should see the sub-menus HOS, Time Card Report, IFTA Report & Clean Truck Check

  Scenario: To verify the 2nd level sub-menus of Compliance in the left Navigation bar
    When the user clicks the dropdown icon present left to "HOS" menu
    Then the user should see the child menus of HOS such as Logs, Unidentified Driving, Violations & Availability with a vertical line.

  @LQ-146379
  Scenario: To verify the Maintenance menu in the left Navigation bar in Expand Mode
    When the user clicks the dropdown icon present next to "Maintenance" menu
    Then the user should see the sub-menus Work Orders, Schedules, Asset Inspection, Faults & Measurements


  @LQ-111061
  Scenario: To verify the Sustainability menu in the left Navigation bar in Expand Mode
    When the user clicks the dropdown icon present next to "Sustainability" menu
    Then the user should see the sub-menus such as Sustainability Overview, Fuel & Energy Usage, EV Battery Health, EV Charging History & BEV Range Capability

  Scenario: To verify the Reports menu in the left Navigation bar in Expand Mode
    When the user clicks the dropdown icon present next to "Reports" menu
    Then the user should see the sub-menus such as My Reports & Report Setup

  Scenario: To verify the Rules & Exceptions menu in the left Navigation bar in Expand Mode
    When the user clicks the dropdown icon present next to "Rules & Exceptions" menu
    Then the user should see the "Rules" and "Exceptions" sub-menus

  @CODE-2496
  Scenario: To verify addins menu in left panel
    When the user scrolls to the bottom of left panel
    Then the Addins menu should be present