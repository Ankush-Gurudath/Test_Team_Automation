Feature: Sanity Test for Fleet Telematics - Center Page Geotab

  @LQ-306
  Scenario: Sanity Test for Fleet Telematics - Center Page
    Given the login page is displayed in the browser
    When the user enters username/password, clicks the login button in the page and select company from the list
    Then the user is successfully logged into the Driver Safety dashboard

  @LQ-108840
  Scenario: Fleet Telematics tab
    When the user clicks Fleet Telematics tab
    Then the Fleet Telematics main page is loaded successfully

  @LQ-117225
  Scenario: To verify the Map menu page of fleet telematics application in New UI
    When the user clicks on MAP menu in the left navigation bar
    Then the user should be navigated to the Map page with the headers such as Search asset,VIN or serial number, Status, Saved Views, Map Options and Add Zone and the icons such as Zoom in, Zoom out present inside the map

  @LQ-118189
  Scenario: To verify the Options present in the Trips History sub-menu page under Productivity menu
    When the user clicks Productivity menu - Trips History submenu
    Then the user should be navigated to the Trips History Page and the user should be able to see the Headers such as Search, Options, Summary, Live Positions, Report, Map Options present in the Trips History page

  @LQ-171226
  Scenario: To verify the "Routes" child-menu of Productivity Menu
    When the user clicks Productivity menu - Routes submenu- Routes subchild
    Then the user should be navigated to the "Routes" page and options such as "Search name","Add route","Filter" and "Columns"

  Scenario: To verify the Options present in "Columns" textbox under "Routes" sub-menu of Productivity Menu.
    When the user clicks the dropdown icon present near the "Columns"
    Then the user should be able to see the Options such as "Reset to default","Name","Assigned Asset","Scheduled Start Time" and "Status" available

  @LQ-118200
  Scenario: To verify the "Planned vs Actual" sub-menu page of Productivity > Routes
    When the user clicks Productivity menu - Routes submenu- Planned vs actual routes subchild
    Then the user should be navigated to the "Planned vs actual route report" page and the user should be able to see the headers such as search assets, options and report present in the page

  @LQ-118210
  Scenario: To verify the "Route Summary" sub-menu page of Productivity > Routes
    When the user clicks Productivity menu - Routes submenu- Route Summary subchild
    Then the user should be navigated to the "Route Summary Report" page and the user should be able to see the headers such as options, stop processing and report present in the page

  @LQ-97664
  Scenario: To verify the "Unmatched Route" sub-menu page of Productivity > Routes
    When the user clicks Productivity menu - Routes submenu- Unmatched Route subchild
    Then the user should be navigated to the "Unmatched Route Report" page and the user should be able to see the headers such as options and report present in the page

  @LQ-118220
  Scenario: To verify the "Import Routes" sub-menu page of Productivity > Routes
    When the user clicks Productivity menu - Routes submenu- Import Routes subchild
    Then the user should be navigated to the "Import Routes Report" page and the user should be able to see the headers such as import routes title, drop area, and sample table present in the page

  @LQ-118722
  Scenario: To verify the "Zones" sub-menu page of Productivity > Zones
    When the user clicks Productivity menu - Zones - Zones subchild
    Then the user should be navigated to the "Zones" page and the user should be able to see the headers such as search name, filter, add, sort by, types, report, select none, columns present in the page

  @LQ-118724
  Scenario: To verify the "Zone Visits" sub-menu page of Productivity > Zones
    When the user clicks Productivity menu - Zones - Zone Visits subchild
    Then the user should be navigated to the "Zone Visits" page and the user should be able to see the headers such as search assets, options, sort by, report, columns present in the page

  @LQ-118733
  Scenario: To verify the "Zone Types" sub-menu page of Productivity > Zones
    When the user clicks Productivity menu - Zones - Zone Types subchild
    Then the user should be navigated to the "Zone Types" page and the user should be able to see the headers such as search name or comment, add zone type present in the page

  @LQ-118734
  Scenario: To verify the "Import Zones" sub-menu page of Productivity > Zones
    When the user clicks Productivity menu - Zones - Import Zones subchild
    Then the user should be navigated to the "Import Zones" page and the user should be able to see the headers such as options, drop files area, sample table present in the page

  @LQ-118743
  Scenario: To verify the "Driver Congregation" sub-menu page of Productivity menu
    When the user clicks Productivity menu - Driver Congregation submenu
    Then the user should be navigated to the "Driver Congregation" page

  @LQ-118745
  Scenario: To verify the "Asset Location Sharing" sub-menu page of Productivity menu
    When the user clicks Productivity menu - Asset Location Sharing submenu
    Then the user should be navigated to the "Asset Location Sharing" page


  @LQ-
  Scenario: To verify the "Risk Management" sub-menu page of Productivity menu
    When the user clicks Productivity menu - Risk Management submenu
    Then the user should be navigated to the "Risk Management" page

  @LQ-119240
  Scenario: To verify the "Logs" sub-menu page of Compliance > HOS
    When the user clicks Compliance menu - HOS submenu - Logs subchild
    Then the user should be navigated to the "HOS Logs" page

  @LQ-119241
  Scenario: To verify the "Unidentified Driving" sub-menu page of Compliance > HOS
    When the user clicks Compliance menu - HOS submenu - Unidentified Driving subchild
    Then the user should be navigated to the "Unidentified Driving" page

  @LQ-119242
  Scenario: To verify the "Violations" sub-menu page of Compliance > HOS
    When the user clicks Compliance menu - HOS submenu - Violations subchild
    Then the user should be navigated to the "Violations" page

  @LQ-119243
  Scenario: To verify the "Availability" sub-menu page of Compliance > HOS
    When the user clicks Compliance menu - HOS submenu - Availability subchild
    Then the user should be navigated to the "Availability" page

  @LQ-119271
  Scenario: To verify the "Time Card Report" sub-menu page of Compliance
    When the user clicks Compliance menu - Time Card Report submenu
    Then the user should be navigated to the "Time Card Report" page

  @LQ-119273
  Scenario: To verify the "IFTA Report" sub-menu page of Compliance
    When the user clicks Compliance menu - IFTA Report submenu
    Then the user should be navigated to the "IFTA Report" page

  @LQ-119282
  Scenario: To verify the "Clean Truck Check" sub-menu page of Compliance
    When the user clicks Compliance menu - Clean Truck Check submenu
    Then the user should be navigated to the "Clean Truck Check" page


  @LQ-146480
  Scenario: To verify the "Work Order" child-menu of "Maintenance" menu
    Given the user clicks Maintenance menu
    When the user clicks the "Work Order" submenu
    Then the user should be navigated to the "Work Order Management" page with sub-tabs "Requests","Orders" and "Jobs"

  @LQ-146663
  Scenario: To verify the "Request" tab in "Work Order" page
    When the user clicks the "Work Order" submenu
    Then the user is in "Request" tab by default with "Schedules","Reports" and "Work Request" in the header
    And the user should see the options "Groups","Assets" and "Filters" under the tab
    And the user should see columns "Asset","Source","Maintenance Type","Categories","Severity","Triggered date","Status" and "Description" present by default in the tabular form

  @LQ-146688
  Scenario: To verify the columns present in the "Request" tab in "Work Order" page
    When the user clicks the Setting icon present above the tabular column
    Then all the setting names should be present for requests tab

  @LQ-151157
  Scenario: To verify the "Filters" option in the Requests tab in "Work Order" page
    When the user clicks the "Filters" options
    Then the user should see an pop-up having a header named " All Filters" and all the filter options

  Scenario: User selects a group from the "Groups" dropdown of "Work Order" child menu
    When the user clicks on the "Groups" dropdown and selects a group option
    Then the selected group should be applied to the filter

  Scenario: User selects a maintenance from the "Maintenance types" dropdown in "Work Order" page
    When the user clicks on the "Maintenance types" dropdown and selects a maintenance type
    Then the selected maintenance type should be applied to the filter

  Scenario: To verify Source types in dropdown for Source filter in "Work Order" page
    When the user clicks on the "Sources" dropdown
    Then the user should see the types "Manual","Data Insight","Scheduled","Driver reported","Faults" with "Select All" option

  Scenario: User selects a source from the "Sources" dropdown in "Work Order" page
    When the user selects any source type
    Then the selected source type should be applied to the filter

  Scenario: To verify Severity types in dropdown for Source filter in "Work Order" page
    When the user clicks on the "Severity" dropdown
    Then the user should see the types "Unknown","Low","Medium","High","Critical" with "Select All" option

  Scenario: User selects a severity from "Severity types" dropdown in "Work Order" page
    When the user selects a severity
    Then the user selected severity type should be applied to the filter

  @LQ-147372
  Scenario: To verify the "Orders" tab of "Work Order" child menu under Maintenance menu
    When the user clicks the "Orders" sub-tab
    Then the "Orders" tab should be displayed with buttons "Reports", "Bulk upload" and "Work Order" in the header
    And the user should see the options "Groups","Assets","Status" and "Filters" under the tab

  Scenario: To verify dropdown values for Status filter in "Work Order" page
    When the user clicks the dropdown present near "Status" field
    Then the user should be able to see the types "Open","Assigned","In progress","On hold","Completed" and "Cancelled" available and buttons "Clear","Cancel" and "Apply"
    And the user should see the columns Asset, Order reference, Date created, Date completed, Priority, status

  @LQ-147415
  Scenario: To verify the columns present in the "Orders" tab in "Work Order" page
    When the user clicks the Setting icon present above the tabular column
    Then all the setting names should be present for orders tab

  @LQ-151175
  Scenario: To verify all filter options in the Orders tab in "Work Order" page
    When the user clicks the "Filters" option in Orders tab
    Then user should see all filter options

  Scenario: User selects a group from the "Groups" dropdown in "Work Order" page
    When the user clicks on the "Groups" dropdown and selects a group option - orders tab
    Then the selected group should be applied to the filter in orders tab


  Scenario: Verify status options from the "Status" dropdown in "Work Order" page
    When the user clicks on the "Status" dropdown
    Then the user should see the types "Open","Assigned","In progress","On hold","Completed" and "Cancelled" available with a "Clear" button disabled

  Scenario: User selects one status from dropdown in "Work Order" page
    When the user selects any status
    Then the selected status should be applied to the filter

  @LQ-166493
  Scenario: To verify options for select date in "Work Order" page
    When the user clicks the "Select Date" button
    Then the user should see the header "Date created" with options like "Today","Yesterday","This week","Last week","This month","Last month","Last 3 months" and "Custom"

  Scenario: To verify date filter in orders tab - Filters in "Work Order" page
    When selects any date option
    Then the selected date should be applied to the filter

  Scenario: To verify the "Priority" fields in the Orders tab in "Work Order" page
#    When there is a Priority option available  -- not needs to executed as already its in Filters tab
    Then the user should see "Low","Medium", "High" and "Critical" options

  Scenario: To verify Reference Filter in Orders tab in "Work Order" page
    When the user clicks any of the priority
    Then the user should see the selected priority checked

  @LQ-147426
  Scenario: To verify the "Jobs" tab of "Work Order" child menu under Maintenance menu
    When the user clicks the "Jobs" sub-tab
    Then the user should see the options "Groups","Assets","This month","Status" and "Filters" under the tab
    And the user should see the columns "Asset","Order reference","Source","Maintenance type","Categories","Status","Date started","Date completed" and "Date created"

  Scenario: To verify dropdown values for Status filter - Jobs tab in "Work Order" page
    When the user clicks the dropdown present near "Status" field
    Then the user should be able to see the types "Open","Assigned","In progress","On hold","Completed" and "Cancelled" available with "Select all" option and "Clear" displayed

  Scenario: To verify the calendar option "This month" present in the Jobs page
    When the user clicks the "This month" option
    Then the user should see the "Dates" with a header "Date completed" and other options "Today","Yesterday","This week","Last week","This month","Last month","Last 3 months" and "Custom" available
    And the user should see the "Clear" button disabled

  @LQ-166510
  Scenario: To verify the columns present in the "Jobs" tab under "Maintenance" menu
    When the user clicks the Setting icon present above the tabular column
    Then the user should see all the options with reset button

  @LQ-146415
  Scenario: To verify the Schedules submenu of "Maintenance" menu
    When the user clicks the "Schedules" submenu
    Then the "Maintenance Schedules" page is displayed with Headers such as "Reports","Work requests" "Bulk upload" and "Schedule"
    And the user should be able to see the filter options such as "Groups", "Search", "Frequency","Repeats" and a settings icon
    And the user should be able to see the list of schedules such as "Name","Categories","Repeats","Frequency" and "Assets added" present in the page

  @LQ-146432
  Scenario: To verify the Frequency Option present in the header under Reminders menu of Maintenance Menu
    When the user clicks the dropdown icon present near the "Frequency" textbox
    Then the user should be able to see the frequencies such as "Frequency based on distance", "Frequency based on months", "Frequency based on weeks", "Frequency based on days" and "Frequency based on engine hours"
    And the user should be able to see the "Clear" and "Apply" buttons which is disabled and "Cancel" button which is enabled

  Scenario: To verify the Repeats Option present in the header under Reminders sub-menu of Maintenance Menu
    When the user clicks the dropdown icon present near the "Repeats" textbox
    Then the user should be able to see "Yes" and "No" options available
    And the user should be able to see the "Clear" button disabled

  @LQ-146433
  Scenario: To verify setting options in "Schedules" child-menu of Maintenance Menu
    When the user clicks the Setting icon present above the tabular column
    Then the user should be able to see the options "Name","Categories","Repeats","Frequency","Asset added","Days","Weeks","Months","Day of week","Day of month","Engine hours","Distance","Event date" and "Source" available with scroll bar under the settings icon and Reset button is available

  @LQ-171273
  Scenario: To verify the Asset Inspection sub-menu of Maintenance Menu
    When the user click the "Asset Inspection" sub-menu under Maintenance menu
    Then the user should be navigated to the "Asset Inspection" page and all the UI components should be loaded

  @LQ-171276
  Scenario: To verify the Options present in "Sort by" textbox under "Asset Inspection" sub-menu of Maintenance Menu.
    When the user clicks the dropdown icon present near the "Sort by: Asset" button
    Then the user should be able to see the options such as "Asset","Date" and "Duration"

  Scenario: To verify the Options present in the Columns list under "Asset Inspection" sub-menu of Maintenance Menu.
    When the user clicks the Settings icon box present in the left-side top corner
    Then the user should be able to see all the options

  @LQ-146436
  Scenario: To verify the Faults submenu under Maintenance menu
    When the user clicks the Faults submenu under Maintenance menu
    Then the user should be navigated to the "Faults" page with elements such as "Filter", "Sort by: Fault Code", "Report", "Dismiss faults" and "Columns" present in the page

  @LQ-146437
  Scenario: To verify the Options present in "Sort by" textbox under "Faults" submenu
    When the user clicks the dropdown icon present near the "Sort by: Fault Code" button
    Then the user should be able to see the options such as "Fault Code","Description","Times Logged","Source" and "Severity" available

  Scenario: To verify the Options present in the Columns list under "Faults" submenu
    When the user clicks the "Columns" drop down box present in the left-side top corner
    Then the user should be able to see the columns such as "Reset to default", "Fault Code", "Description", "Current Status", "Times Logged", "Source", "Protocol", "Advanced Details", "Selection", "Severity" and "Controller"  available

  @LQ-146446
  Scenario: To verify the Measurements submenu under Maintenance menu
    When the user clicks the "Measurements" submenu
    Then the user should be navigated to the "Measurements" page with elements such as "Filters", "Group by: Diagnostic" and "Report" present in the page

  Scenario: To verify the "Group by" dropdown present in the Measurements page
    When the user clicks the dropdown icon present near the "Group by: Diagnostic" textbox
    Then the user should be able to see the options "Diagnostic","Date" options

  @LQ-122663
  Scenario: To verify the "Sustainability Overview" sub-menu page of Sustainability
    When the user clicks Sustainability menu - Sustainability Overview submenu
    Then the user should be navigated to the "Sustainability Overview" page

  @LQ-122664
  Scenario: To verify the "Fuel & EV energy usage" sub-menu page of Sustainability
    When the user clicks Sustainability menu - Fuel & EV energy usage submenu
    Then the user should be navigated to the "Fuel & EV energy usage" page

#Removing until new page is available -  https://lytx.atlassian.net/browse/MEGA-3680
#  @LQ-122665
#  Scenario: To verify the "EV Battery Health" sub-menu page of Sustainability
#    When the user clicks Sustainability menu - EV Battery Health submenu
#    Then the user should be navigated to the "EV Battery Health" page

#  @LQ-122668
#  Scenario: To verify the "EV Charging History" sub-menu page of Sustainability
#    When the user clicks Sustainability menu - EV Charging History submenu
#    Then the user should be navigated to the "EV Charging History" page

#Removing until new page is available -  https://lytx.atlassian.net/browse/MEGA-3680
#  @LQ-122674
#  Scenario: To verify the "BEV Range Capability" sub-menu page of Sustainability
#    When the user clicks Sustainability menu - BEV Range Capability submenu
#    Then the user should be navigated to the "BEV Range Capability" page

  @LQ-
  Scenario: To verify the "My Reports" sub-menu page of Reports
    When the user clicks Reports menu - My Reports submenu
    Then the user should be navigated to the "My Reports" page

  @LQ-
  Scenario: To verify the "Report Setup" sub-menu page of Reports
    When the user clicks Reports menu - Report Setup submenu
    Then the user should be navigated to the "Report Setup" page

  @LQ-136768
  Scenario: To verify the "Rules" sub-menu page of Rules & Exceptions
    When the user clicks Rules & Exceptions menu - Rules submenu
    Then the user should be navigated to the "Rules" page, header and safety section should be displayed

  @LQ-94886 # LQ-96386
  Scenario: To verify the add functionality of Rules page
    When the user clicks on the "Add" button in the Rules page
    Then the user should be navigated to the "Exception Rule Edit" page and should be able to see tabs such as name, condition, notifications and media upload tab, save and cancel buttons and 7 colors

  @LQ-136802
  Scenario: To verify Name tab in exception rule edit page
#    When the user is in the Exception Rule Edit page and clicks on the "Name" tab  -- already in Name tab by default
    Then the user should be able to see fields such as "name", "color", "Publish to groups", "Comment"

  Scenario: To verify publish to groups field in Name tab
    Given the user clicks on the "Publish to groups" dropdown field
    When the user selects any group from the dropdown
    Then the user should be able to see selected groups

  Scenario: To verify remove selected groups of "PublishGroup" field
    When the user click the cross mark symbol present next to the selected groups
    Then the user should not see the groups that was selected

  @LQ-144481
  Scenario: To verify Condition tab in exception rule edit page
    When the user clicks on the "Condition" tab
    Then the user should be navigated to Conditions page and the user should see "Engine data"

  Scenario: To Verify Engine data in conditions tab
    When the user clicks on the "Engine data" condition box
    Then the user should see options such as "Active Fault", "Any Fault" and "Measurement or Data"
    And the user should see all the components under "Engine data"

  @LQ-144499
  Scenario: To verify "Zone or Zone type" tab in Conditions tab
    When the user clicks "Zone or Zone Type" text box
    Then the user should navigate to the "Zone or Zone Type" page
    And the user should be able to see options named "Type", "Zone" and "Event"
    And the user should see all the Event types names "Entering", "Exiting", "Outside", "inside" and "Inside", "add" and "cancel" button and "add a Condition" input box

  @LQ-144502
  Scenario: To validate the "Roads with speed limit" Condition under Conditions sub-tab of Add Button
    When the user clicks "Roads with speed limit" text box
    Then the user should be able to see the Dialog box named "Roads with speed limit" and "Over" and "Under" and an empty text box under that with unit "mph"
    And the user should see "Add" and "Cancel" button and input box "Add a condition..."

  @LQ-144503
  Scenario: To validate the "Speed" Condition under Conditions sub-tab of Add Button
    When the user clicks "Speed" text box
    Then the user should be able to see the Dialog box named "Speed" with "Over" and "Under" and an empty text box under that with unit "mph"
    And the user should see "Add" and "Cancel" button and input box "Add a condition..."

  @LQ-144512
  Scenario: To validate the "Speed limit" Condition under Conditions sub-tab of Add Button
    When the user clicks "Speed limit" text box
    Then the user should be able to see the Dialog box named "Speed limit" with the field named "Truck speed limit" with "Yes" and "No" buttons
    And the user should see the field named "Over the limit by" and an empty textbox and field named "Exclude estimated speed limits" with "On", "Off" buttons
    And the user should see "Add" and "Cancel" button and input box "Add a condition..."

  @LQ-144513
  Scenario: Verify more button in conditions tab - Device
    When the user clicks the dropdown present near to "More" in condition tab
    Then the user should see a header named "Device" and the options "Ignition", "Asset", "Driver", "Group", "Asset Inspection Defect"

  @LQ-144514
  Scenario: Verify more button in conditions tab - Trip
#    When the user clicks the dropdown present near to "More" in condition tab -- already in More tab
    Then the user should see a header named "Trip" and the options "Driving", "Stop", "Trip distance", "Trip duration"

  @LQ-144516
  Scenario: Verify more button in conditions tab - Auxiliaries
#    When the user clicks the dropdown present near to "More" in condition tab -- already in More tab
    Then the user should see a header named "Auxiliaries" and the options "Aux 1", "Aux 2", "Aux 3", "Aux 4", "Aux 5", "Aux 6", "Aux 7", "Aux 8"

  @LQ-144589
  Scenario: Verify more button in conditions tab - Work Hours
#    When the user clicks the dropdown present near to "More" in condition tab -- already in More tab
    Then the user should see a header named "Work Hours" and the options "After work hours rule", "Work hours rule", "After work hours device", "Device work hours"

  @LQ-144566
  Scenario: Verify more button in conditions tab - Wrappers and Logic
#    When the user clicks the dropdown present near to "More" in condition tab -- already in More tab
    Then the user should see a header named "Wrappers" and the options "Is value more than", "Is value less than", "Is value equal to"
    And user should see header named "Logic" with the options "And", "Or" available

  @LQ-144567
  Scenario: To validate the "Notifications" sub-tab in Rules menu
    When the user clicks Notifications tab
    Then the user should be navigated to Notifications page with header "NOTIFICATION RECIPIENTS" and "Add email", "Add alert", "Add driver feedback", "More" options
    And user should see Summary under "HELP" Section

  @LQ-144568
  Scenario: To validate the Email recipient in "Notifications" sub-tab under Add functionality in Rules page .
    When the user clicks "AddEmail" Button
    Then the user should see the Fields Template and Email

  Scenario: To validate the  template field under "AddEmail" recipient.
    When the user clicks the dropdown of the Template field
    Then the user should see the "Default email template" and "Add new template"

  Scenario: To validate the selection of email templates under "AddEmail" recipient
    When the user clicks the Add new template
    Then the user should see pop-up

  Scenario: To validate the "Email" field under "AddEmail" recipient.
    When the user clicks the textbox of the email
    Then the user should see the dropdown with valid and invalid email IDs

  @LQ-144590
  Scenario: To validate the "Add alert" recipient under "Notifications" sub-tab.
    When the user clicks the dropdown present near the Option "Add alert"
    Then the user should see the "Popup" alert and the "Description"
    And the user should see the "Urgent popup" alert and the "Description"
    And the user should see the "Log only" alert and the "Description"

  @LQ-144591
  Scenario:To validate the "Add driver feedback" recipient under "Notifications" sub-tab
    When the user clicks the dropdown present near the Option "Add driver feedback"
    Then the user should see the "Beep three times" and the respective "Description"
    And the user should see the "Beep three times rapidly" and the respective "Description"
    And the user should see the "Beep ten times rapidly" and the respective "Description"
    And the user should see the "Text message" and the respective "Description"
    And the user should see the "GO TALK" and the respective "Description"
    And the user should see the "Change status" and the respective "Description"

  @LQ-144592
  Scenario: To check the additional recipient "More" under "Notifications" sub-tab in rules page.
    When the user clicks the dropdown present near the "More" options
    Then the user should see the "Web request" and the respective "Description"
    And the user should see the "Assign to group" and the respective "Description"
    And the user should see the "Email to group" and the respective "Description"
    And the user should see the "Distribution list" and the respective "Description"
    And the user should see the "Assign as Personal/Business" and the respective "Description"

  @LQ-144593
  Scenario: To verify the "Media Upload" sub-tab in Rules page
    When the user clicks Media Upload tab
    Then the user should see "MEDIA UPLOAD SETTINGS" with "Media type" with an information symbol

  Scenario: To verify hovers text in "Media Upload" page
    When the user hovers on to the symbol
    Then the user should see the message "The type of media when a rule is triggered."
    And the user sees three buttons "Video", "Snapshot" and "None"

#  @LQ-144602
  Scenario: To validate the Notification Template functionality of Rules page
    Given user clicks back button in the Exception Rule Edit page
    When the user clicks on the "Notification Templates" button in the header
    Then the user should be redirected to the "Notifications Templates" page and user should see the Options "Search","Sort by : Name", "Add email template", "Add web template", "Add text template"

  @LQ-146703
  Scenario: To validate the Email template under Notification templates functionality of Rules page
    When the user clicks "Add email template" button
    Then the "Email Template Edit" page is displayed with parameters such as "Name", "Subject", "Body", "Exception Report"

  Scenario: To validate the "Exception Report" field of Email template under Notification templates functionality of Rules page
    When the user clicks the dropdown present next to "Do not attach Exceptions Detail Report" textbox
    Then the user should be able to see the dropdown options "Do not attach Exceptions Detail Report", "Default Exceptions Detail Report", "Possible Collisions" and "Advanced Exceptions Detail Report"

  @LQ-146704
  Scenario Outline: To validate the Available Tokens of Email Template under Notification templates functionality of Rules page
#    When the user clicks "Add email template" button -- already in Add email template page
    Then the user should be able to see Available Tokens <S__No>, <Token_Name> and <Description> in a tabular format
    Examples:
      | S__No | Token_Name                       | Description                                                                                    |
      | 1     | {Address}                        | The street address at time the exception occurred                                              |
      | 2     | {Database}                       | The database for this device                                                                   |
      | 3     | {Date}                           | The date the exception occurred                                                                |
      | 4     | {Device}                         | The name and serial number of the device that triggered the exception                          |
      | 5     | {Device Comments}                | The comment field for the device                                                               |
      | 6     | {Device Groups}                  | The groups to which the device belongs                                                         |
      | 7     | {Device ID}                      | The identifier for the device                                                                  |
      | 8     | {Device With Driver Name}        | The device and driver name                                                                     |
      | 9     | {Device name}                    | The name of the device that triggered the exception.                                           |
      | 10    | {Diagnostic}                     | The diagnostic names and values associated with the exception                                  |
      | 11    | {Diagnostic code}                | The diagnostic code associated with the exception                                              |
      | 12    | {Driver Comment}                 | The driver's comments                                                                          |
      | 13    | {Driver First Name}              | The first name of the driver                                                                   |
      | 14    | {Driver Groups}                  | The groups to which the driver belongs                                                         |
      | 15    | {Driver Last Name}               | The last name of the driver                                                                    |
      | 16    | {Driver Name}                    | The name of the driver                                                                         |
      | 17    | {Asset Inspection defect}        | The Asset Inspection defects when the exception occurred                                       |
      | 18    | {Asset Inspection Defect Remark} | The remark tied to the defect of an asset inspection                                           |
      | 19    | {Asset Inspection Driver Remark} | Driver's remark for the asset inspection                                                       |
      | 20    | {Asset Inspection Type}          | The type of inspection created for the asset                                                   |
      | 21    | {EV Battery Charge %}            | The Electric Vehicle's (EV's) battery charge % (state of charge)                               |
      | 22    | {EV Charging State}              | The charging state of the Electric Vehicle: 0 = not charging, 1 = AC charging, 2 = DC charging |
      | 23    | {Exception Id}                   | The identifier for the exception                                                               |
      | 24    | {Latitude}                       | The latitude where the exception occurred                                                      |
      | 25    | {Longitude}                      | The longitude where the exception occurred                                                     |
      | 26    | {Odometer}                       | The odometer value of the device                                                               |
      | 27    | {Rule}                           | The exception rule that was broken                                                             |
      | 28    | {Serial number}                  | The device serial number                                                                       |
      | 29    | {Speed}                          | The max speed of the vehicle during the exception                                              |
      | 30    | {Speed limit}                    | The speed limit when the exception occurred                                                    |
      | 31    | {Time}                           | The time the exception occurred                                                                |
      | 32    | {Timezone}                       | The Timezone for the exception date and time                                                   |
      | 33    | {Vin}                            | The vehicle's identification number                                                            |
      | 34    | {Zone}                           | The name of the zone in which the vehicle was located at the time of the exception             |
      | 35    | {Zone Comment}                   | The comment for the zone in which the vehicle was located at the time of the exception         |
      | 36    | {Zone ID}                        | The identifier for the zone in which the vehicle was located at the time of the exception      |
      | 37    | {Map}                            | The map view of the location where the exception occurred                                      |

  @LQ-144747
  Scenario: To validate the Web template under Notification templates functionality of Rules page
    Given user closes "Add Email Template" page
    When the user clicks "Add web template" button
    Then the "Web Request Template Edit" page is displayed with parameters "Template Name", "URL", "HTTP request type" and "Available Tokens"
    And the user should see 2 toggle buttons "GET" & "POST" for "HTTP request type"

  @LQ-136769
  Scenario: To verify the "Exceptions" sub-menu page of Rules & Exceptions
    When the user clicks Rules & Exceptions menu - Exceptions submenu
    Then the user should be navigated to the "Exceptions" page

  @LQ-
  Scenario: To verify the Messages page
    When the user clicks Messages menu
    Then the user should be navigated to the "Messages" page

  @LQ-165571
  Scenario: To verify the Message button present in the Messages page
    When the user clicks the "Message" button present with plus symbol
    Then the user should see a pop up opening with a title "New Message" with a description "Messages can be sent to multiple assets and users. Select all that apply. Replies are only visible to you", search filter with a water mark "Search for asset or user" and the user sees "Compose message" button is disabled.
    And the user should see list of assets under "Assets" sub-tab with checkboxes.


  Scenario: To verify the User sub-tab present in the Message page
    When the user clicks the "Users" sub-tab
    Then the user should see the list of users with checkboxes.

  @LQ-165575
  Scenario: To verify the "Compose message" in the message pop-up
    When the user selects any user under "Users" tab and the user should see the "Compose message" button enabled and the user clicks the "Compose message" button
    Then the user should see a dialog box with the options "back to asset selection" , user name , search icon and cross mark symbol

  @LQ-
  Scenario: To verify the Notifications page
    When the user clicks Notifications menu
    Then the user should be navigated to the "Notifications" page, header and notification types should be displayed

  @LQ-146401
  Scenario: To verify the "Config" module in the fleet telematics application
    When the user clicks the dropdown present near "Config" menu
    Then the user should see of all the submenus under Config

  @LQ-151000
  Scenario: To verify the Config page -> Fleet Settings
    When the user clicks the "Fleet Settings" sub-menu and navigates to System Settings page
    Then the user should be able to see all of the headers in the System Settings page

    # Commenting because of MEGA-3955
#  @LQ-151090
#  Scenario: To verify the Config page -> Work Hours
#    When the user clicks the "Work Hours" sub-menu
#    Then the user should be navigated to "Work Hours" page with a "Work Hours" button, fields like "Search", "Sort by: Name" and "Total items", and see all of the work hours available

  @LQ-151111
  Scenario: To verify the "Audit Log" sub-menu under Config module
    When the user clicks the "Audit Log" menu
    Then the user should be redirected to "Audit Log" page with "Search","Options" and "Reports" fields, and user login details with the email id and Time

    # Commenting until MEGA-3894 is fixed
#  @LQ-186738
#  Scenario: To verify the "Holidays" page under Config menu
#    When the user clicks the "Holidays" menu
#    Then the user should be redirected to "Holidays" page and should have Holidays header, search, add holiday and table consisting of name, date and group

#  @LQ-197697
#  Scenario: To verify the Add Holiday functionality in the Holidays page
#    When the user clicks on Add Holiday button
#    Then add holiday page should be opened with fields like name, date, holiday group id with default value as 1, enabled cancel and disabled save button