Feature: End to end Fleet Insights workflow
  As a developer,
  I want to run end to end tests on the Fleet Insights application
  So I can confirm that code changes have not adversely affected the app.

  @LQ-544
  Scenario: Fleet - Insights Suite
  #Scenario: Fleet - Insights - User can access the Fleet Operations dashboard groups tab
    Given user logins to fleet page
    When the user navigates to Insights -> Fleet Operations
    Then the groups tab of Fleet Operations page is displayed

  @LQ-543
  Scenario: Filter group in Fleet Operations page Groups tab
    When the user sets group filter to one group in Fleet Operations page Groups tab
    Then the data belong to the group are listed in Fleet Operations page Groups tab

#  Scenario: Filter date in Fleet Operations page Groups tab
#    When the user sets date filter in Fleet Operations page Groups tab
#    Then the data belong to the date are listed in Fleet Operations page Groups tab

  @LQ-549
  Scenario: User can access the Fleet Operations dashboard drivers tab
    When the user clicks Drivers in Fleet Operations page
    Then the drivers tab of Fleet Operations page is displayed

#  @LQ-548
#  Scenario: Filter group in Fleet Operations page Drivers tab
#    When the user sets group filter to one group in Fleet Operations page Drivers tab
#    Then the data belong to the group are listed in Fleet Operations page Drivers tab
#
#  Scenario: Filter date in Fleet Operations page Drivers tab
#    When the user sets date filter in Fleet Operations page Drivers tab
#    Then the data belong to the date are listed in Fleet Operations page Drivers tab

#  @LQ-2346
#  Scenario: Link to Driver Profile in Fleet Operation Drivers page
#    When the user clicks a driver name in the bottom table
#    Then the driver profile page is displayed
#
#  @LQ-558
#  Scenario: View metadata bar in Driver Profile page
#    When the user clicks a driver name
#    Then the driver name is displayed and the metadata bar is displayed with labels: "EMPLOYEE ID", "GROUP", "VEHICLE NAME", "EMAIL"
#
#  Scenario: View summary section in Driver Profile page
#    When the user clicks the expand icon on the summary section
#    Then view type buttons are displayed: "Daily Avg", "Total"
#    And the summary section is displayed with labels: "ROUTE TIME", "DISTANCE", "TRIPS", "STOPS", "STOP TIME", "DRIVING TIME", "ENGINE HOURS", "IDLE VIOLATIONS", "IDLE DURATION", "SPEED VIOLATIONS", "SPEEDING DURATION" on driver profile page
#
#  @LQ-559
#  Scenario: The selected trips are displayed on the map
#    When the user clicks a date and open the trip
#    Then the first trip is displayed with labels: "Trip1", start time, start address, end time, end address, "VEHICLE", "TRIP DURATION", "DISTANCE", "MAX SPEED", "STOP DURATION"
#
#  @LQ-560
#  Scenario: The selected idles are displayed on the map
#    When the user clicks "Idles" and open the idle
#    Then the first idle is displayed with labels: "Idle1", start time, end time, address, "VEHICLE", "IDLE DURATION"
#
#  @LQ-557
#  Scenario: Filter by date in Driver Profile page
#    When the user sets date filter in Driver Profile page
#    Then the data with selected filters are displayed on the idles in Driver Profile page
#    And the data with selected filters are displayed on the trips in Driver Profile page
#
#  @LQ-547
#  Scenario: User can access the Fleet Operations dashboard vehicles tab
#    When the user clicks Vehicles in Fleet Operations page
#    Then the vehicles tab of Fleet Operations page is displayed
#
#  @LQ-546
#  Scenario: Filter group in Fleet Operations page Vehicles tab
#    When the user sets group filter to one group in Fleet Operations page Vehicles tab
#    Then the data belong to the group are listed in Fleet Operations page Vehicles tab
#
#  Scenario: Filter date in Fleet Operations page Vehicles tab
#    When the user sets date filter in Fleet Operations page Vehicles tab
#    Then the data belong to the date are listed in Fleet Operations page Vehicles tab
#
#  @LQ-545
#  Scenario: Search Vehicles in Fleet Operation Vehicles page
#    When the user inputs some characters in Search Vehicles box
#    And the user selects one vehicle
#    Then the vehicle profile page is displayed
#
#  @LQ-553
#  Scenario: View metadata bar in Vehicle Profile page
#    When the user clicks the expand icon on metadata bar
#    Then the metadata bar is displayed with labels: "VEHICLE NAME", "GROUP", "DRIVER", "DEVICE", "STATUS", "MAKE & MODEL", "LICENSE PLATE", "HIBERNATION SETTING", "VIN", "VEHICLE TYPE", "SEAT BELT TYPE"
#
#  @LQ-552
#  Scenario: Filter by date in Vehicle Profile page
#    When the user sets date filter in vehicle profile page
#    Then the data with selected filters are displayed on the trips
#    And the data with selected filters are displayed on the idles
#    And the summary section is displayed with labels: "ROUTE TIME", "DISTANCE", "TRIPS", "STOPS", "STOP TIME", "DRIVING TIME", "ENGINE HOURS", "IDLE VIOLATIONS", "IDLE DURATION", "SPEED VIOLATIONS", "SPEEDING DURATION"
#
#  @LQ-554
#  Scenario: The selected trips are displayed on map in Vehicle Profile page
#    When the user clicks a date
#    Then the first trip is displayed with labels: "Trip1", start time, start address, end time, end address, "DRIVER", "TRIP DURATION", "DISTANCE", "MAX SPEED", "STOP DURATION"
#
#  @LQ-555
#  Scenario: The selected idles are displayed on map in Vehicle Profile page
#    When the user clicks "Idles" and clicks a date
#    Then the first idle is displayed with labels: "Idle1", "START TIME", "END TIME", "ADDRESS", "DRIVER", "IDLE DURATION"

  @LQ-7134
  Scenario: Fleet - Insights - User can access the Equipment Status dashboard
    When the user clicks "INSIGHTS" and then clicks "EQUIPMENT STATUS"
    Then the table is displayed with columns: "EQUIPMENT", "GROUP", "DEVICE SERIAL NUMBER", "LAST LOCATION", "LAST CONNECTED", "LAST MOVEMENT", "STATIONARY DURATION", "BATTERY LEVEL"

  @LQ-7135
  Scenario: Filter group in Equipment Status page
    When the user selects a group in the group filter in Equipment Status page
    Then the data with selected group are displayed on the table in Equipment Status page

  Scenario: Filter by Equipment in Equipment Status page
    When the user select Equipment and the user sets search criteria in Equipment Status page
    Then the data with select Equipment are displayed on the table in Equipment Status page

  Scenario: Filter by Device in Equipment Status page
    When the user select Device and the user sets search criteria in Equipment Status page
    Then the data with select Device are displayed on the table in Equipment Status page

  Scenario: get the number of records in Equipment Status page
    When the user navigates to Insights -> Equipment Status
    Then the number of records is displayed in Equipment Status page

  @LQ-519
  Scenario: User can access the Geofences dashboard
    When the user navigates to Insights -> Geofences
    Then the Geofences page is displayed

  @LQ-520
  Scenario: Filter by date in Geofences page
    When the user sets date filter in Geofences page
    Then the data within selected date range are displayed in METRICS, TREND, table

  Scenario: Filter by group in Geofences page
    When the user sets group filter to one group in Geofences page
    Then the data with selected group are displayed in METRICS, TREND, table

  @LQ-562
  Scenario: View metadata bar in Geofence Profile page
    When the user clicks a geofence or search and select a geofence to go to geofence profile page
    Then the metadata bar is displayed with labels: "GEOFENCE NAME", "DATE CREATED", "DAYS APPLIED", "RANGE OF TIME", "Trigger Type", "GROUP", "SUBGROUPS", "VEHICLES"

  Scenario: View summary section in Geofence Profile page
    When the user search and select a geofence in geofence profile page
    Then the date picker selector is displayed and the vehicle is displayed below the summary section and the Vehicle Name, Start Point Date/Time, duration are displayed
    And the summary section is displayed with labels: "TOTAL TRIGGERS", "TOTAL DURATION", "TOTAL VEHICLES", "DRIVING TIME IN GEOFENCES", "IDLE TIME IN GEOFENCES", "STOP TIME IN GEOFENCES"

  @LQ-563
  Scenario: The selected triggers are displayed on the map in Geofence Profile page
    When the user clicks a vehicle
    Then the trigger is displayed with labels: "Trigger Start", Start Point Date/Time, Start Point Address, "Trigger End", End Point Date/Time, End Point Address, "DRIVER", "TRIGGER TYPE", "DRIVING TIME", "STOP TIME", "IDLE TIME", "DURATION" and the selected trigger is displayed on the map

#  @LQ-561 commented due to open bug CXFA-10838
#  Scenario: Filter by date in Geofence Profile page
#    When the user sets date filter in geofence profile page
#    Then the data with selected filters are displayed on the summary section and the data with selected filters are displayed on the triggers

  @LQ-514
  Scenario: View table in State Mileage page
    When the user navigates to Insights -> State Mileage
    Then the State Mileage page is displayed and the table is displayed with columns: "VEHICLE", "GROUP", "DEVICE SERIAL", "STATE,COUNTRY", "DISTANCE" and the number of records is displayed

  Scenario: View summary in State Mileage page
    When the user clicks "INSIGHTS" and the user clicks "STATE MILEAGE"
    Then the summary contains "METRICS", "TOTAL", "TOTAL DISTANCE", distance for each state

  Scenario: View trend in State Mileage page
    When the user clicks on a state
    Then the trend is updated with data of the selected state

  @LQ-515
  Scenario: Filter by group in State Mileage page
    When the user sets group filter to one group in State Mileage page
    Then the data belong to the group are displayed in metrics, trend, table

  Scenario: Filter by date in State Mileage page
    When the user sets date filter in State Mileage page
    Then the data belong to the date are displayed in metrics, trend, table

  @LQ-457
  Scenario: User can access the Data Export dashboard
    When the user clicks "INSIGHTS" and the user selects "DATA EXPORT
    Then there are group, date, vehicle filters and the table is displayed with columns "ACTION", "REPORT TYPE", "GROUP", "START DATE", "END DATE", "VEHICLE", "REQUESTED DATE

  #@LQ-458
  #Scenario: User can request Data Export report
  #  When the user sets date filter in Data Export report
  #  And the user clicks "Request Data"
  #  Then the report is requested

  #@LQ-459
  #Scenario: Download Requested Report
  #  When the user clicks "Download" button of a request
  #  Then the report is downloaded

  @LQ-550
  Scenario: View metrics in Fleet data page
    When the user clicks "INSIGHTS" and the user clicks "FLEET DATA"
    Then the metrics is displayed with columns: "AVERAGE", "TOTAL"
    And the metrics is displayed with values: "DISTANCE", "ENGINE HOURS", "DRIVING HOURS", "IDLE TIME", "IDLE PTO TIME", "FUEL CONSUMED", "DRIVING FUEL", "IDLING FUEL", "PTO IDLING FUEL", "FUEL ECONOMY", "DRIVING FUEL ECONOMY"

  Scenario: View trend in Fleet data page
    When  the user clicks Distance column on the metrics on fleet data page
    Then the trend of the selected column is displayed with title

  Scenario: View groups table in Fleet data page
    When the user clicks "GROUP" tab
    Then the table is displayed with columns: "GROUP", "DISTANCE, "ENGINE HOURS, "DRIVING HOURS", "IDLE TIME", "IDLE PTO TIME", "FUEL CONSUMED", "DRIVING FUEL", "IDLING FUEL", "PTO IDLING FUEL", "FUEL ECONOMY", "DRIVING FUEL ECONOMY"

  Scenario: View vehicles table in Fleet data page
    When the user clicks "VEHICLE" tab
    Then the table is displayed with columns: "VEHICLE", "ODOMETER READING", "DISTANCE", "ENGINE HOURS", "DRIVING HOURS, "IDLE TIME", "IDLE PTO TIME", "FUEL CONSUMED", "DRIVING FUEL", "IDLING FUEL", "PTO IDLING FUEL", "FUEL ECONOMY", "DRIVING FUEL ECONOMY"

  @LQ-523
  Scenario: Filter by date in Fleet data page
    When the user sets date filter in Fleet data page
    Then the data with selected date filters are displayed in Fleet data page

  Scenario: Filter by group in Fleet data page
    When the user sets group filter to one group in Fleet data page
    Then the data with selected group filters are displayed in Fleet data page


  @LQ-Ad
  Scenario: get the number of records in Admin Equipment Management page
    When the user navigates to Admin -> Equipment Management page
    Then get the number of equipment with attached devices
