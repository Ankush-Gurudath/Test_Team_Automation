Feature: End to end Fleet Map workflow
  As a developer,
  I want to run end to end tests on the Fleet Map application
  So I can confirm that code changes have not adversely affected the app.

  @LQ-15218
  Scenario: Fleet - Map Suite
    Given the login page is displayed
    When the user enters a newly created username/password and clicks the login button
    Then the Fleet application is displayed

#  @LQ-12380
#  Scenario: There are Idle Duration count, Idle Duration widget, Geofence Triggers count, Geofence Triggers widget in Home page
#  When "Fleet Dispatcher" user is on the Home page (Dashboard)
#  Then the metrics table is displayed with columns: "VEHICLE", "GROUP", "IDLE VIOLATIONS", "IDLE DURATION COLUMNS" in Idle Duration widget and the table is displayed with columns: "GEOFENCE", "GROUP", "TRIGGERS", "TRIGGER DURATION COLUMNS" in Geofence Triggers widget
#
#  @LQ-12386
#  Scenario: Filter by group in Home page
#  When the user sets group filter to one group in the Dashboard
#  Then the vehicle count is displayed, the Idle Duration count with selected filters are displayed, the data with selected filters are displayed in Idle Duration widget, the Geofence Triggers count with selected filters are displayed, and the data with selected filters are displayed in Geofence Triggers widget
#
#  Scenario: Filter by group in Home page
#  When the user sets date filter in the Dashboard
#  Then the correct date related data for vehicle count is displayed, the Idle Duration count with selected filters are displayed, the data with selected filters are displayed in Idle Duration widget, the Geofence Triggers count with selected filters are displayed, and the data with selected filters are displayed in Geofence Triggers widget

  @LQ-447
  Scenario: Add Geofence Via Suggestion List
    When the user clicks "Clear List" and enters some characters in Search box and selects a geofence in the Suggestion List
    Then the geofence is displayed in Working List and the geofence is displayed on Map

  @LQ-445
  Scenario: View Geofence Detail
    When the user clicks "View Details" of a Geofence in Working List
    Then the Geofence detail panel is opened and Geofence Name is displayed and "Geofence Trigger Settings" is displayed with: "Status", "Facing, Day(s)", "Time", "Vehicles Group", "IncludeSubgroups" and there are "Edit Geofence", "Delete Geofence" buttons

  @LQ-112132
  Scenario: New Fleet Map Search Experiences for Geofences
    When the user search Geofences from search box and the user clicks Search button
    Then user should able to see matched Geofences with "+ Working List, Map, check box" options

  Scenario: Search Experience for Geofence “+ Working List”
    When user search Geofences from search box and the user clicks Search button and the user clicks "+Working list" button
    Then geofence is added to the working list with desired details

  Scenario: Search Experience for Geofence "Map"
    When user search geofence from search box and the user clicks Search button and the user clicks "Map" button
    Then geofence is centered on map & the desired details of geofence is displayed on left panel


  @LQ-446
  Scenario: Add Vehicle to the working list via Suggestion List on live mode
    When the user enters some characters in Search box and the user selects a vehicle in the Suggestion List
    Then the vehicles are displayed in Working List and the vehicles are displayed on Map

  Scenario: Add Vehicle to the working list via Search Result on live mode
    When the user enters some characters in Search box and the user clicks Search button and the user checks a vehicle and the user clicks "Add to Working List"
    Then the vehicles are displayed in Working List and the vehicles are displayed on Map

  @LQ-112120
  Scenario: New Fleet Map Search Experiences for vehicle
    When the user search vehicle from search box and the user clicks Search button
    Then user should able to see matched vehicle with "+ Working List, Map, check box" options

  Scenario: Search Experience for Vehicle “+ Working List”
    When user search vehicle from search box and the user clicks Search button and the user clicks "+Working list" button
    Then vehicle is added to the working list with desired details

  Scenario: Search Experience for Vehicle "Map"
    When user search vehicle from search box and the user clicks Search button and the user clicks "Map" button
    Then vehicle is centered on map & the desired details of vehicle is displayed on left panel

# no data in live mode because only the live data in recent 7 days is shown
#  @LQ-449
#  Scenario: Auto Refresh on live map
#    When the user waits for 10 seconds
#    Then the map refreshes and the vehicle is displayed on new location on Map
#
#  @LQ-7203
#  Scenario: Vehicle name displays correctly in pin details panel when zooming in
#    When the user clicks Zoom in icon on map
#    Then Map Zooms in one level and previous center of map will remain at the center for each zoom level change
#
#  Scenario: Vehicle name displays correctly in pin details panel when zooming out
#    When the user clicks Zoom out icon on map
#    Then Map Zooms out one level and previous center of map will remain at the center for each zoom level change
##
#  @LQ-442
#  Scenario: View Vehicle Pin Detail
#    When the user clicks a vehicle pin on Map
#    Then the pin detail panel is opened and "Vehicle Name", "Status", "Driver", "Group", "Device", Occurrence Time, Time since occurrence, "Speed", "Ignition", Address, Latitude, Longitude are displayed on pin detail panel
#
#  @LQ-7201
#  Scenario: Details information of moving vehicle
#    When the user clicks a moving vehicle on map
#    Then the details info is displayed on the left panel and icon on top left corner is arrow with green background color and there are Vehicle, Status, Driver, Group, Device, Date, Speed, Time since position(only has day, hour, minute), Ignition, Street Address info and lat/log and There are icons in front of vehicle, gps data, address and lat/log sections
#
#  @LQ-512
#  Scenario: Open Closest Vehicles page
#    When the user adds an address to working list and the user clicks "View Details" and the user clicks "Find Closest Vehicle"
#    Then three closest vehicles are displayed in Closest Vehicles list and the vehicle name, driver, group, estimation distance and time are displayed in Closest Vehicles list and the first vehicle is highlighted in Closest Vehicles list and the route of the three vehicles are displayed on map and the route of the first vehicle is highlighted on map

  @LQ-465
  Scenario: Add Vehicle to the working list via Suggestion List on history mode
    Given the user switch to history mode
    When the user enters some characters in Search box and the user selects a vehicle in the Suggestion List
    Then the vehicles are displayed in Working List and the vehicles are displayed on Map

  Scenario: Add Vehicle to the working list via Search Result on history mode
    When the user enters some characters in Search box and the user clicks Search button and the user checks a vehicle and the user clicks "Add to Working List"
    Then the vehicles are displayed in Working List and the vehicles are displayed on Map

#  @LQ-460
#  Scenario: View Trip, Route, Point on Map
#    When the user adds the vehicle to Working List and the user clicks "View History" and the user clicks "Yesterday" and the user clicks "Apply"
#    Then the Trip, Route, Point icon are displayed on Working List and the Trip pin, Route line are displayed on Map
#
#  @LQ-461
#  Scenario: View Moving Track Point Pin Detail
#    When the user clicks a Moving Track Point Pin on Map
#    Then the pin detail panel is opened and "Vehicle Name", "Moving", "Driver", "Group", "Device", Occurrence Time, Time since occurrence, "Speed", "Ignition", Address, Latitude, Longitude are displayed on pin detail panel and Google street view is displayed on pin detail panel
#
#  @LQ-462
#  Scenario: View Trip start Pin Detail
#    When the user clicks a Trip start pin on Map on history page
#    Then the start pin detail panel is opened and "Vehicle Name", "Status", "Driver", "Group", "Device", Occurrence Time, "Distance", "Max Speed", Address, Latitude, Longitude, "Stop Duration" are displayed on pin detail panel
#
#  Scenario: View Trip end Pin Detail
#    When the user clicks a Trip end pin on Map on history page
#    Then the end pin detail panel is opened and "Vehicle Name", "Status", "Driver", "Group", "Device", Occurrence Time, "Distance", "Max Speed", Address, Latitude, Longitude, "Stop Duration" are displayed on pin detail panel
#
#  @LQ-463
#  Scenario: View Speed Violation Pin Detail
#    When the user clicks speed violation on Map
#    Then Speed Violation pin detail panel is opened and "Vehicle Name", "Status", "Driver", "Group", "Device", Occurrence Time, "Speed Limit", "Max Speed", "Speed Duration", Address, Latitude, Longitude are displayed on pin detail panel
#
#  Scenario: View Idle Violation Pin Detail
#    When the user clicks Idle Violation on Map
#    Then Idle Violation pin panel is opened and "Vehicle Name", "Status: Idle Violation", "Driver", "Group", "Device", Occurrence Time, "Idle Duration", Address, Latitude, Longitude are displayed on pin detail panel
#
#  @LQ-3314
#  @LQ-463_part_3
#  Scenario: View Geofence Violation Start Pin Detail
#    When the user clicks Geofence Violation Start pin on Map
#    Then the Geofence Violation Start pin panel is opened and "Vehicle Name", "Status", "Driver", "Group", "Device", Occurrence Time, Address, Latitude, Longitude are displayed on pin detail panel
#
#  @LQ-3317
#  @LQ-463_part_4
#  Scenario: View Geofence Violation End Pin Detail
#    When the user clicks Geofence Violation End pin on Map
#    Then the Geofence Violation End pin panel is opened and "Vehicle Name", "Status", "Driver", "Group", "Device", Occurrence Time, Address, Latitude, Longitude are displayed on pin detail panel
#

  @LQ-7174
  Scenario: Display Asset on map
    When the user clicks the "View History" button & selects a date range for history mode & filter by vehicle from the working list
    Then Vehicle should be list in the history mode working list

  Scenario: Delete asset in Working List with history mode
    When the user deletes vehicle in working list
    Then the deleted asset will not be shown in working list

  Scenario: Add deleted asset into Working List
    When the user enter the deleted asset name to search it and the user selects the deleted asset from suggestion list
    Then the deleted asset will be shown in working list

  @LQ-452
  Scenario: Create Geofence
    When the user clicks SETTINGS and clicks "Create Geofence" and draws a shape on Map and enters a Geofence name and clicks "Create"
    Then the Geofence is added on Map and added to Working List

  @LQ-453
  Scenario: Edit Geofence
    When the user clicks "View Details" of a geofence and clicks "Edit Geofence" and changes the shape and changes the Geofence name and clicks "Save"
    Then the Geofence shape is updated on Map and the Geofence name is updated in Working List

  @LQ-447
  Scenario: Add Geofence Via Search result
    When the user clicks "Clear List" and enters some characters in Search box and the user clicks Search button and the user checks two Geofences and the user clicks "Add to Working List"
    Then the geofences are displayed in Working List and the geofences are displayed on Map

#  @LQ-3314
#  @LQ-463_part_3
#  Scenario: View Geofence Violation Start Pin Detail
#    When the user clicks Geofence Violation Start pin on Map
#    Then the Geofence Violation Start pin panel is opened and "Vehicle Name", "Status", "Driver", "Group", "Device", Occurrence Time, Address, Latitude, Longitude are displayed on pin detail panel
#
#  @LQ-3317
#  @LQ-463_part_4
#  Scenario: View Geofence Violation End Pin Detail
#    When the user clicks Geofence Violation End pin on Map
#    Then the Geofence Violation End pin panel is opened and "Vehicle Name", "Status", "Driver", "Group", "Device", Occurrence Time, Address, Latitude, Longitude are displayed on pin detail panel
#

  @LQ-7174
  Scenario: Display Asset on map
    When the user clicks the "View History" button & selects a date range for history mode & filter by vehicle from the working list
    Then Vehicle should be list in the history mode working list

  Scenario: Delete asset in Working List with history mode
    When the user deletes vehicle in working list
    Then the deleted asset will not be shown in working list

  Scenario: Add deleted asset into Working List
    When the user enter the deleted asset name to search it and the user selects the deleted asset from suggestion list
    Then the deleted asset will be shown in working list

  @LQ-452
  Scenario: Create Geofence
    When the user clicks SETTINGS and clicks "Create Geofence" and draws a shape on Map and enters a Geofence name and clicks "Create"
    Then the Geofence is added on Map and added to Working List

  @LQ-453
  Scenario: Edit Geofence
    When the user clicks "View Details" of a geofence and clicks "Edit Geofence" and changes the shape and changes the Geofence name and clicks "Save"
    Then the Geofence shape is updated on Map and the Geofence name is updated in Working List

  @LQ-447
  Scenario: Add Geofence Via Search result
    When the user clicks "Clear List" and enters some characters in Search box and the user clicks Search button and the user checks two Geofences and the user clicks "Add to Working List"
    Then the geofences are displayed in Working List and the geofences are displayed on Map

  @LQ-7177
  Scenario: Add Asset via Suggestion List
    When the user clicks on the search text box and the user enters a equipment name and the user selects the equipment from suggestion list
    Then the equipment is added into working list and the added equipment can be displayed on map

#  Scenario: Display Equipment on Map
#    When the user selects an equipment from the working list
#    Then Map is auto zoomed to show the equipment and the equipment is displayed in the map

#  @LQ-7176
#  Scenario: Display equipment detail panel
#    When the user clicks an equipment point on map
#    Then equipment details panel should be opened in the left panel and "Equipment Name", "Status", "Group", "Device", Occurrence Time, Time since occurrence, Address, Latitude, Longitude are displayed on pin detail panel

  @LQ-112131
  Scenario: New Fleet Map Search Experiences for asset
    When the user search asset from search box and the user clicks Search button
    Then user should able to see matched asset with "+ Working List, Map, check box" options

  Scenario: Search Experience for “+ Working List”
    When user search asset from search box and the user clicks Search button and the user clicks "+Working list" button
    Then asset is added to the working list with desired details

#  Scenario: Search Experience for "Map"
#    When user search asset from search box and the user clicks Search button and the user clicks "Map" button
#    Then asset is centered on map & the desired details of asset is displayed on left panel
