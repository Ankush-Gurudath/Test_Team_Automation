Feature: Sanity Test - Landcare

  @LQ-306
  Scenario: Verify top navigation tab Driver Safety and verify if the data is loaded in the center
    Given the login page is displayed in the browser
    When the user enters username/password, clicks the login button in the page and select company from the list
    Then the user is successfully in the Driver Safety dashboard

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

  Scenario: Verify left panel and center pages of Driver Safety > Search
    When the user clicks on Search menu
    Then the user should see Search by event ID text box

  @LQ-152054
  Scenario: Verify top navigation tab Video Search and verify if the data is loaded in the center
    When the user clicks on video search
    Then the user is successfully in the Video Search page. The vehicle count is displayed and the table is displayed with columns: "ACTIONS", "VEHICLES", "DEVICE", "LAST COMMUNICATED", "GROUP", "VIEWS"

  Scenario: Navigate to Live in VIDEO BROWSER page from vehicles page
    When user clicks on "Live" from the ACTIONS for one vehicle
    Then user is navigated to "Live" in VIDEO BROWSER page

  @LQ-203
  Scenario: Live stream of a vehicle
    When the user clicks on "live" link
    Then the outside video is live played on the left and the map is displayed on the right with current position and the GPS speed is displayed on the bottom

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

  @LQ-136363
  Scenario: Verify left panel and center pages of Admin > Vehicles menu
    When the user clicks on Admin > Vehicles menu
    Then the user should see page header Vehicles with vehicles count

  @LQ-136223
  Scenario: Verify left panel and center pages of Admin > Device menu
    When the user clicks on Admin > Device menu
    Then the user should see page header Device Management with device count

    # Commenting because of MEGA-3534
#  @LQ-136374
#  Scenario: Verify left panel and center pages of Admin > Geofence menu
#    When the user clicks on Admin > Geofence menu
#    Then the user should see page header Geofence Management with device count

  @LQ-136375
  Scenario: Verify left panel and center pages of Admin > Insights menu > Driver ID Assignment submenu
    When the user clicks on Admin > Insights menu > Driver ID Assignment submenu
    Then the user should see page header Driver ID Assignment with trips count

    # Commenting because of SHARK-2855
#  @LQ-136400
#  Scenario: Verify left panel and center pages of Admin > Config Settings menu > Safe Driving Report
#    When the user clicks on Config Settings menu > Safe Driving Report
#    Then the user should see page setting, groups and minimum distance driven table headers with only edit icon for root group and edit, delete icons for all other groups

  @LQ-108840
  Scenario: Verify Fleet Telematics tab
    When the user clicks Fleet Telematics tab
    Then the Fleet Telematics main page is loaded successfully

  @LQ-110122
  Scenario: To verify all menu's in the Left navigation bar of FLEET TELEMATICS application in New UI
    Then the user should see the tabs in the left Navigation bar such as Dashboard, Map, Productivity, Compliance, Maintenance, Sustainability, Reports, Rules & Exceptions, Messages & Notifications

