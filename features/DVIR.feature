Feature:DVIR

  @LQ-12437
  Scenario: DVIR Suite
  #Scenario: DVIR - Access to "DRIVER VEHICLE INSPECTION REPORTS" page
    Given full access user logs in
    When the user clicks DVIR
    Then Total reports count, reset button, group filter, date filter, status filter, defect filter and wild search filter are shown on "DRIVER VEHICLE INSPECTION REPORTS" page and table columns are: "REPORT ID", "TYPE", "STATUS", "REPORT DATE", "DURATION", "DRIVER", "VEHICLE", "MAJOR VEHICLE DEFECTS", "MINOR VEHICLE DEFECTS", "VEHICLE INSPECTION LIST", "TRAILER", "MAJOR TRAILER DEFECTS", "MINOR TRAILER DEFECTS", "TRAILER INSPECTION LIST", "MECHANIC/AGENT", "REVIEWER"

  @LQ-12439
  Scenario: Filter by Statuses on "DRIVER VEHICLE INSPECTION REPORTS" page
    When the user clicks Statuses and select one or multiple statuses on "DRIVER VEHICLE INSPECTION REPORTS" page
    Then "DRIVER VEHICLE INSPECTION" reports with selected status are shown in table

  Scenario: Filter by Date on "DRIVER VEHICLE INSPECTION REPORTS" page
    When the user clicks Select Date Range and select dates on "DRIVER VEHICLE INSPECTION REPORTS" page
    Then "DRIVER VEHICLE INSPECTION" reports within the selected date range are shown in table

  Scenario: Filter by Group on "DRIVER VEHICLE INSPECTION REPORTS" page
    When the user selects a group in Select Group dialog
    Then "DRIVER VEHICLE INSPECTION" reports belongs to the group are shown in table

  Scenario: Filter by Defect on "DRIVER VEHICLE INSPECTION REPORTS" page
    When the user clicks Defect and select one or multiple defects on "DRIVER VEHICLE INSPECTION REPORTS" page
    Then "DRIVER VEHICLE INSPECTION" reports with the defect are shown in table

  Scenario: Filter by wild search on "DRIVER VEHICLE INSPECTION REPORTS" page
    When the user clicks Select Search, select a search option and input search criteria on "DRIVER VEHICLE INSPECTION REPORTS" page
    Then "DRIVER VEHICLE INSPECTION" reports match the search criteria are shown in table

  @LQ-27998
  Scenario: Resolve-repaired defects in Report Details page
    Given there are some defect status reports
    When the user clicks one report id of defect status and the user clicks "Resolve" dropdown and the user selects Repaired
    Then The "Reopen" button displays with Repaired text

  Scenario: Reopen defects in Report Details page
    When the user clicks "Reopen" button behind defect
    Then The "Resolve" button displays

  Scenario: Resolve-no repaired needed defects in Report Details page
    When the user clicks "Resolve" dropdown and the user selects No Repair Needed
    Then The "Reopen" button displays with No Repair Needed text


  @LQ-12444
  Scenario: Download "INSPECTION REPORT" on "INSPECTION REPORT" page
    When the user clicks Download Report
    Then the "INSPECTION REPORT" is downloaded

  @LQ-12430
  Scenario: The Vehicle Assignment page is displayed
    When the user clicks the "List Settings" tab & the user clicks "List Assignment"
    Then the page header "INSPECTION LIST ASSIGNMENT" is displayed & the vehicle count is displayed & the table is displayed with columns: "VEHICLE", "GROUP", "VEHICLE TYPE" and "INSPECTION LIST"

  @LQ-12431
  Scenario: Filter group(s) on the Vehicle Assignment page
    When the user sets group filter to one group
    Then the vehicles belong to the group are listed

  Scenario: Filter Vehicle Type on the Vehicle Assignment page
    When the user clicks on "Vehicle Type" filter & the user selects one or more vehicle type(s)
    Then the vehicles with the selected vehicle type(s) are displayed

#TODO: This test commented due to the bug LQ-12716
  Scenario: Filter inspection list on the Vehicle Assignment page
  When the user clicks on "Inspection List" filter & the user selects one or more inspection list(s) on the Vehicle Assignment page
  Then the vehicles with the selected inspection list are displayed


  Scenario: Search Vehicle on the Vehicle Assignment page
    When the user enters some characters into "Search Vehicle Name" field
    Then the vehicles names have inputted characters are shown

  @LQ-12432
  Scenario: Set inspection list on the Vehicle Assignment page
    When the user checks some available vehicles & the user clicks "Set Inspection List" Button on the Vehicle Assignment page
    Then the selected inspection list(s) are set to the selected vehicles on the Vehicle Assignment page

  @LQ-12436
  Scenario: View Vehicle Schedule table
    When user clicks "SCHEDULE" on left navigation
    Then the page header "INSPECTION SCHEDULES" is displayed & the count of the vehicle schedule report is displayed & the table is displayed with columns

  @LQ-12459
  Scenario: Filter group(s) on the Vehicle Schedule page
    When the user sets group filter to one group in Vehicle Schedule page
    Then the vehicles schedule reports vehicle group belong to the group are listed

 # Scenario: Filter inspection list on the Vehicle Schedule page
 # When the user clicks on "Inspection List" filter & the user selects one or more inspection list(s) on the Vehicle Schedule page
  #Then the vehicle schedule reports with the selected inspection list are displayed

  Scenario: Filter status on the Vehicle Schedule page
    When the user clicks on "Status" filter & the user selects one or more status
    Then the vehicle schedule reports with the selected status are displayed

  Scenario: Search Vehicle on the Vehicle Schedule page
    When the user enters some characters into "Search Vehicle Name" field & the user clicks the search icon
    Then the vehicle schedule reports belong to the filtered vehicles are shown

#  @LQ-12460 # commenting due to open bug TOTORO-5964
#  Scenario: Download "Vehicle Schedule report"
#    When the user clicks Download CSV in vehicle schedule page
#    Then the Vehicle Schedule report is downloaded

  @LQ-12446
  Scenario: Default list of vehicle list
    When the "Full Access" user is in the Vehicle list page
    Then the title "VEHICLE INSPECTION LISTS" is displayed & there is a default vehicle inspection list and named "Default" & there is a duplicate icon behind the list name

  @LQ-12423
  Scenario: Edit vehicle inspection List on the Inspection List Management page
    When the user clicks on Edit icon of one list & the user updates the List name & the user clicks "Save Changes"
    Then the vehicle inspection list is updated

  @LQ-12422
  Scenario: Add vehicle inspection List on the Inspection List Management page
    When the user clicks on "New List" button & the user enters required fields: "List Name", "Inspection Item Section" and "Inspection Points" & the user clicks Create
    Then the vehicle inspection list is added

  @LQ-12424
  Scenario: Duplicate vehicle inspection List on the Inspection List Management page
    When the user clicks on Duplicate icon of one list
    Then the duplicate vehicle inspection list is added & the name of the duplicate vehicle inspection list ends in "Copy1"

  @LQ-12425
  Scenario: Delete vehicle inspection List on the Inspection List Management page
    When the user clicks on Delete icon of one list & the user clicks "Delete" button on the pop-up
    Then the vehicle inspection list is deleted

  @LQ-12447
  Scenario: Default list of Trailer list
    When the "Full Access" user is in the Trailer list page
    Then the title "TRAILER INSPECTION LISTS" is displayed & there is a default trailer inspection list and named "Default" & there is a duplicate icon behind the list name

  @LQ-12427
  Scenario: Edit trailer inspection List on the Inspection List Management page
    When the user clicks on Edit icon of one list in trailer list & the user update the List name & the user clicks "Save Changes"
    Then the trailer inspection list is update

  @LQ-12426
  Scenario: Add trailer inspection List on the Inspection List Management page
    When the user clicks on "New List" button in trailer list & the user enters required fields: "List Name", "Inspection Item Section" and "Inspection Points" & the user clicks "Create"
    Then the trailer inspection list is added

  @LQ-12428
  Scenario: Duplicate trailer inspection List on the Inspection List Management page
    When the user clicks on Duplicate icon of one list on trailer list
    Then the duplicate trailer inspection list is added & the name of the duplicate trailer inspection list ends in "Copy1"

  @LQ-12429
  Scenario: Delete trailer inspection List on the Inspection List Management page
    When the user clicks on Delete icon of one list & the user clicks "Delete" button on the pop-up in trailer list
    Then the trailer inspection list is deleted

  @LQ-12433
  Scenario: The Trailer Assignment page is displayed
    Given the "Full Access" user is in Vehicle Assignment page
    When the user clicks the "Trailer Assignment" tab
    Then the page header "INSPECTION LIST ASSIGNMENT" is displayed & the trailer count is displayed & the table is displayed with columns: "TRAILER", "GROUP", "TRAILER TYPE" and "INSPECTION LIST"

  @LQ-12434
  Scenario: Filter group(s) on the Trailer Assignment page
    When the user sets group filter to one group in trailer assignment page
    Then the trailers belong to the group are listed

  Scenario: Filter Vehicle Type on the Trailer Assignment page
    When the user clicks on "Trailer Type" filter & the user selects one or more trailer type(s) in trailer assignment page
    Then the trailers with the selected trailer type(s) are displayed

  Scenario: Filter inspection list on the Trailer Assignment page
    When the user clicks on "Inspection List" filter & the user selects one or more inspection list(s) in trailer assignment page
    Then the trailers with the selected inspection list are displayed

  Scenario: Search Trailer on the Trailer Assignment page
    When the user enters some characters into "Search Trailer Name" field in trailer assignment page
    Then the trailers names have inputted characters are shown

  @LQ-12435
  Scenario: Set inspection list on the Trailer Assignment page
    When the user checks some available trailers & the user clicks "Set Inspection List" Button & the user selects one or more inspection list(s) & the user clicks "Set" button in trailer assignment page
    Then the selected inspection list(s) are set to the selected trailers

#  @LQ-12463 # commenting due to open bug TOTORO-5964
#  Scenario: Download "Trailer Schedule report" commenting due to open bug TOTORO-5964
#    Given the "Full Access" user is in the trailer schedule page
#    When the user clicks Download CSV in trailer schedule page
#    Then the Trailer Schedule report is downloaded in trailer schedule page

  @LQ-12461
  Scenario: View Trailer Schedule table
    When user clicks "SCHEDULE" on left navigation & user clicks "Trailer Schedule"
    Then the page header "INSPECTION SCHEDULES" is displayed & the count of the trailer schedule report is displayed & the table is displayed with columns

  @LQ-12462
  Scenario: Filter group(s) on the Trailer Schedule page
    When the user sets group filter to one group in Trailer Schedule page
    Then the trailer schedule reports trailer group belong to the group are listed in Trailer Schedule Page

 # Scenario: Filter inspection list on the Trailer Schedule page
 # When the user clicks on "Inspection List" filter & the user selects one or more inspection list(s) in Trailer Schedule page
  #Then the trailer schedule reports with the selected inspection list are displayed

  Scenario: Filter status on the Trailer Schedule page
    When the user clicks on "Status" filter & the user selects one or more status in Trailer Schedule page
    Then the trailer schedule reports with the selected status are displayed

  Scenario: Search trailer on the Trailer Schedule page
    When the user enters some characters into "Search Trailer Name" field
    Then the trailer schedule reports belong to the filtered trailers are shown

  @LQ-12442
  Scenario: Open "INSPECTION REPORT" on "DRIVER VEHICLE INSPECTION REPORTS" page
    When the user clicks an "INSPECTION REPORT"
    Then the "INSPECTION REPORT" is opened with "REPORT ID", "INSPECTION TYPE", "DRIVER", "REPORT DATE", "STATUS" and "LOCATION" & the vehicle info is shown with "LICENSE PLATE", "ODOMETER" and status & the driver signature is shown with name and date

  @LQ-5410
  Scenario: Add note in "INSPECTION REPORT" page
    When the user clicks "Add Note" button & the user enters some characters & the user clicks "Save" button
    Then the entered characters are added & the "Edit" button and "Delete" button will show

  @LQ-5437
  Scenario: Edit the note that added by login user
    When the user clicks the keboo & the user clicks 'Edit' button & the user enters some characters & the user clicks 'Save' button
    Then the note updated correctly

  @LQ-12445
  Scenario: Back to "DRIVER VEHICLE INSPECTION REPORTS" page from "INSPECTION REPORT" page
    When the user clicks Back
    Then Total reports count, group filter, date filter, status filter, defect filter and wild search filter are shown on "DRIVER VEHICLE INSPECTION REPORTS" page

  @LQ-12441
  Scenario: Download reports on "DRIVER VEHICLE INSPECTION REPORTS" page
    When the user clicks Download CSV on "DRIVER VEHICLE INSPECTION REPORTS" page
    Then "DRIVER VEHICLE INSPECTION" reports are downloaded successfully

  Scenario: Edit the note that added by other user
    When the other user clicks the keboo & the user clicks 'Edit' button & the user enters some characters & the user clicks 'Save' button
    Then the note updated correctly in the inspection report page

  @LQ-27997
  Scenario: Reset in Driver Vehicle Inspection Reports
    Given support user logs in dvir page
    When the user sets group filter to one group, sets one date range, sets Status filter to one status, sets Defects filter to one defect, searches vehicle by inputting some characters and clicks "Reset"
    Then all filter back to default, the DVIR list is updated correctly according to default filter and the first page is displayed
