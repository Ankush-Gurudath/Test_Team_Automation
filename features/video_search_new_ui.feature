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

  @LQ-136862
  Scenario: Filter group in vehicles page
    When the user sets group filter to one group in vehicles page
    Then the vehicles belong to the group are listed

  Scenario: Search by vehicle name in vehicles page
    When the user selects "Vehicle Name" from "Select Search" dropdown and the user input some characters in search bar
    Then the vehicles with the inputted characters are listed

  Scenario: Search by serial number in vehicles page
    When the user selects "Serial Number" from "Select Search" dropdown and the user input some characters in search bar
    Then the vehicles which attached ER serial number with the inputted characters are listed

#  @LQ-136867 # The downloaded filename contains timing with 'seconds'. Validating this is a bit challenging and requires some investigation. A story has been created in the backlog to track it.
#  Scenario: Download full data as CSV without filters
#    When the user clicks on the "Download CSV" button on the bottom right corner in vehicles page
#    Then CSV file should be downloaded containing all the available data

  @LQ-136875
  Scenario: Tooltip displays device information on hover
   When the user hovers the mouse over the tooltip before the vehicle name
   Then the tooltip should display the device information including Serial Number, Active/Inactive status and Last Communication Date and Time

#  @LQ-136865
#  Scenario: Navigate to next page using arrow button
#  When the user clicks the arrow button in the page number section
#  Then the user should be navigated to the next page of results

  Scenario: Change number of vehicles displayed per page using pagination
   When the user selects a value from the pagination dropdown 10 vehicles, 50 vehicles, 100 vehicles
   Then the page should display the selected number of vehicles accordingly

  @LQ-136887
  Scenario: The columns are listed in Video Tags page
    When the user clicks on the Library and the user selects Video Tags
    Then the video tag count is displayed and the table is displayed with columns: "ACTIONS","VEHICLE","TAG NAME","CATEGORY","AVAILABLE VIEWS","GROUP","RECORD DATE"

#  @LQ-136887
#  Scenario: Filter Date in the Video Tags page
#    When the user sets the date filter in the Video Tags page
#    Then the tagged videos belong to the date are listed
#
#  Scenario: Filter group in the Video Tags page
#    When the user sets group filter to one group in the Video Tags page
#    Then the tagged videos belong to the group are listed
#
#  Scenario: Filter Category in the Video Tags page
#    When the user selects driver tagged from "Category" filter in the Video Tags page
#    Then the tagged videos belong to the driver tagged are listed

#  @LQ-136887
#  Scenario: Search the tagged video by tag name
#    When the user selects "Tag Name" from "Select Search" filter and the user inputs some characters
#    Then the tagged videos that tag name with the input characters are listed
#
#  Scenario: Search the tagged video by vehicle name
#    When the user selects "Vehicle Name" from "Select Search" filter and the user inputs some characters
#    Then the tagged videos that vehicle name with the input characters are listed

#  Scenario: Navigate between pages using arrows
#    When the user clicks on the left or right navigation arrows at the bottom of the page
#    Then the page should navigate as per the direction of the arrow clicked

  Scenario: Verify pagination functionality
    When the user selects pagination options 10, 50, 100 videos from the bottom left corner
    Then the page should display the videos according to the selected pagination option

#  @LQ-150975
#  Scenario: Verify browse functionality from video tag page
#    When clicks on the Browse button
#    Then user should be navigated to the Browse page

  @LQ-204
  Scenario: Navigate to Browser in VIDEO BROWSER page from vehicles page
#    Given "Video Reviewer Plus" user is in VIDEO SEARCH
    When user clicks on "Browse" from the ACTIONS for one vehicle
    Then user is navigated to "Browser" in VIDEO BROWSER page

  @LQ-136880
  Scenario: Verify Browse page elements and non-API behavior
#    When the user clicks on the Browse button for a vehicle
    Then the Browse page should open with the following elements should be visible "date filter","save video button", "vehicle name", "play/pause button", "playback speed option", "time dropdown", "Trip In-Progress markers on timeline", "Alerts on timeline", "Events on timeline"

  @LQ-136884
  Scenario: Navigate to Live in VIDEO BROWSER page from vehicles page
    When user clicks on "Live" from the ACTIONS for one vehicle
    Then user is navigated to "Live" in VIDEO BROWSER page


  @LQ-203
  Scenario: Live stream of a vehicle
    When the user clicks on "live" link
    Then the outside video is live played on the left and the map is displayed on the right with current position and the GSP speed is displayed on the bottom

#  @LQ-151039 commented due to existing bug VID-3343
#  Scenario: Save video for all the views when browse
#    Given "Video Reviewer Plus" user is in browser tab of VIDEO BROWSER page
#    When user clicks on the "Save To Library" button and user enters a video name in input box and user clicks "Save" button and user clicks "Go To Video" button on the success popup modal
#    Then the 120 seconds video for all the views is received and the user is navigated to Video Player page

  @LQ-136890
  Scenario: The columns are listed in Saved Video page
    When the user clicks on the Library and the user selects Saved Videos
    Then the video count is displayed and the table is displayed with columns: "VIDEO NAME","STATUS","TAG TYPE","VEHICLE","GROUP","LENGTH","VIEWS","VIDEO DATE","REQUEST DATE"

  @LQ-136890
  Scenario: Filter group in the Saved Videos page
    When the user sets group filter to one group in the Saved Videos page
    Then the saved videos belong to the selected group are listed in the Saved Videos page

  Scenario: Date filter in the Saved Videos page
    When the user sets the date filter in the Saved Videos page
    Then the saved videos belong to the date are listed in the Saved Videos page

  Scenario: Search the saved video by vehicle name
    When user selects "Vehicle Name" from "Select Search" filter and user inputs some characters in the Saved Videos page
    Then the saved videos that vehicle name with the input characters are listed

  Scenario: Search the saved video by video name
    When the user selects "Video Name" of from "Select Search" filter and the user inputs some characters in the Saved Videos page
    Then the saved videos that video name with the input characters are listed


  @LQ-136890
#  Scenario: Navigate between pages using arrows
#    When the user clicks on the left or right navigation arrows at the bottom of the page
#    Then the page should navigate as per the direction of the arrow clicked

  Scenario: Verify pagination functionality
    When the user selects pagination options 10, 50, 100 videos from the bottom left corner
    Then the page should display the videos according to the selected pagination option

#  @LQ-136890 @SkipProdTests
#  Scenario: View the saved video
#    When the user clicks the video name
#    Then the video player page is opened and the video is auto-played
#
#  @LQ-150991 @SkipProdTests
#  Scenario: Verify map functionality on the saved video player
#   # When the user navigates to Saved Video page and opens a saved video (covered in LQ-208 test)
#    Then the map should be displayed on the video player page


  @LQ-136890 @SkipProdTests
  Scenario: Open and verify saved video details
    When the user clicks the video name
    Then the video player page should display video name (with edit option), vehicle name, length, views, video date, and request date

  @LQ-278664 @SkipProdTests
  Scenario: VS_Download modal shows stitching section with toggle OFF by default
    When the user opens the saved video and opens the Download modal
    Then the "Enable Video Stitching" section is visible

  @LQ-278666 @SkipProdTests
  Scenario: VS_Stitching section visibility for MP4 and Alert Decorated MP4 views when only inside view is selected
    When the user opens the Download modal for that video and selects media type "MP4" And selects view "Inside only"
    Then the "Enable Video Stitching" section is not visible

  @SkipProdTests
  Scenario: VS_Stitching section visibility for MP4 and Alert Decorated MP4 views when only outside view is selected
    When the user selects view "Outside only"
    Then the "Enable Video Stitching" section should not be visible

  @SkipProdTests
  Scenario: VS_Stitching section visibility for MP4 and Alert Decorated MP4 views when both views are selected
    When the user selects view "Inside + Outside"
    Then the "Enable Video Stitching" section is visible

  @LQ-278669 @SkipProdTests
  Scenario: VS_Stitching section is hidden for non-MP4 media types
    When the user selects media type "DCE" and selects view "Inside + Outside"
    Then the "Enable Video Stitching" section is not visible for Download DCE option

  @LQ-278671 @SkipProdTests
  Scenario: VS_Progress indicator and modal behavior during stitched video download
    When the user enables the stitching toggle and clicks Download button
    Then the stitched video is downloaded successfully

  @LQ-278687 @SkipProdTests
  Scenario: Verify downloading the stitching video which is more than 3 minutes
    When the user selects a saved video longer than 3 minutes and clicks Download button
    Then the user should see an error message indicating "Unavailable for HD videos longer than 3 minutes"

#  @LQ-151018
#  Scenario: Verify DCE file download functionality
#    When clicks on the download button and selects Download DCE
#    Then the DCE file should be downloaded
#
#  @LQ-150994
#  Scenario: Verify MP4 download functionality
#    When clicks on the download button and selects Download MP4
#    Then the MP4 file should be downloaded

#  @LQ-151021
#  Scenario: Verify view selection on saved video timeline
#    When the user navigates to Saved Video page and clicks on displayed views in the timeline
#    Then the user should be able to select and switch between the available views


  @LQ-136883
  Scenario: Save video with a single view and no name entered
    When the user navigates to the video search page and clicks on the Browse button for a vehicle and clicks on Save Video without entering a name
    Then error message should be displayed indicating "Required field"

  @LQ-151022
  Scenario: Save video with a single view
    When the user selects 1 view in the dropdown and enters a name in the input box in the Save Video modal and clicks on the Save button
    Then the user should be navigated to the Saved Videos page



#  @LQ-136886
#  Scenario: Display vehicles based on selected date, time, and address
#    When the user navigates to the Map Search page and selects a date, time, address in the respective Filter
#    Then the map should display all the vehicles available at the selected address for the selected date and time
#
#  @LQ-150962
#  Scenario: Navigate to browse page from map search results
#    When the user clicks on the Browse button of a vehicle displayed
#    Then the user should be navigated to the Browse page


