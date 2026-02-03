Feature: Video Search

  @LQ-15219
  Scenario: Video Search Suite
    Given the login page is displayed
    When the Video Reviewer Plus user enters a newly created username/password and clicks the login button
    Then the user is successfully logged into the Video Search page

  @LQ-205
  Scenario: The table show in vehicles page
    When the Video Reviewer Plus user is in Video Search page
    Then the vehicle count is displayed and the table is displayed with columns: "ACTIONS", "VEHICLES", "DEVICE", "LAST COMMUNICATED", "GROUP", "VIEWS"

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

  @LQ-10128
  Scenario: The columns are listed in Video Tags page
    When the user clicks on the Library and the user selects Video Tags
    Then the video tag count is displayed and the table is displayed with columns: "ACTIONS","VEHICLE","TAG NAME","CATEGORY","AVAILABLE VIEWS","GROUP","RECORD DATE"

#  @LQ-210
#  Scenario: Filter Date in the Video Tags page
#    When the user sets the date filter in the Video Tags page
#    Then the tagged videos belong to the date are listed

#  Scenario: Filter group in the Video Tags page
#    When the user sets group filter to one group in the Video Tags page
#    Then the tagged videos belong to the group are listed
#
#  Scenario: Filter Category in the Video Tags page
#    When the user selects driver tagged from "Category" filter in the Video Tags page
#    Then the tagged videos belong to the driver tagged are listed
#
#  @LQ-211
#  Scenario: Search the tagged video by tag name
#    When the user selects "Tag Name" from "Select Search" filter and the user inputs some characters
#    Then the tagged videos that tag name with the input characters are listed
#
#  Scenario: Search the tagged video by vehicle name
#    When the user selects "Vehicle Name" from "Select Search" filter and the user inputs some characters
#    Then the tagged videos that vehicle name with the input characters are listed

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

#  @LQ-202 commented due to existing bug VID-3343
#  Scenario: Save video for all the views when browse
#    Given "Video Reviewer Plus" user is in browser tab of VIDEO BROWSER page
#    When user clicks on the "Save To Library" button and user enters a video name in input box and user clicks "Save" button and user clicks "Go To Video" button on the success popup modal
#    Then the 120 seconds video for all the views is received and the user is navigated to Video Player page

  @LQ-207
  Scenario: The columns are listed in Saved Video page
    When the user clicks on the Library and the user selects Saved Videos
    Then the video count is displayed and the table is displayed with columns: "VIDEO NAME","STATUS","TAG TYPE","VEHICLE","GROUP","LENGTH","VIEWS","VIDEO DATE","REQUEST DATE"

  @LQ-206
  Scenario: Filter group in the Saved Videos page
    When the user sets group filter to one group in the Saved Videos page
    Then the saved videos belong to the selected group are listed in the Saved Videos page

#  Scenario: Date filter in the Saved Videos page
#    When the user sets the date filter in the Saved Videos page
#    Then the saved videos belong to the date are listed in the Saved Videos page

  Scenario: Search the saved video by vehicle name
    When user selects "Vehicle Name" from "Select Search" filter and user inputs some characters in the Saved Videos page
    Then the saved videos that vehicle name with the input characters are listed

  Scenario: Search the saved video by video name
    When the user selects "Video Name" of from "Select Search" filter and the user inputs some characters in the Saved Videos page
    Then the saved videos that video name with the input characters are listed

    @LQ-208
  Scenario: View the saved video
    When the user clicks the video name
    Then the video player page is opened and the video is auto-played
