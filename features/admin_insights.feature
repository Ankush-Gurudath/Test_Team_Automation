Feature: Admin - Insights

  @LQ-235
  Scenario: Admin - Insights Suite
  # Scenario: The driver id assignment is shown
    Given fa user logs in
    When the user clicks "INSIGHTS" & the user clicks "DRIVER ID ASSIGNMENT"
    Then the trip count is displayed and the table section is displayed with columns: "Vehicle","Group","Driver","Employee ID","Driver ID Source", "Trip Start","Trip End","Duration" & the summary section is displayed with: "ASSIGNED TRIPS", "ASSIGNED BY LYTX BADGE", "ASSIGNED BY VEHICLE", "UNASSIGNED TRIPS" & the graph section is displayed

#  @LQ-228
#  Scenario: The Device health page is shown
#    When the user clicks "INSIGHTS" & the user clicks "DEVICE HEALTH"
#    Then the device count is displayed and the table is displayed with columns: "DEVICE","DEVICE TYPE","VEHICLE","GROUP","OVERDUE FOR CHECK-IN","POWER DISCONNECTS","IGNITION NOT DETECTED","OPEN RMA" & the summary section is displayed with issues: "ALL DEVICE ISSUES", "OVERDUE FOR CHECK-IN", "POWER DISCONNECTS", "IGNITION NOT DETECTED", "OPEN RMA" & the graph section is displayed

  @LQ-238
  Scenario: Filter group(s) in driver id assignment page
    Given the "Program Manager" user is in driver id assignment page
    When the user sets group filter to one group in driver id assignment page
    Then the data belong to the group are listed in driver id assignment page

  Scenario: Date range filter in driver id assignment page
    Given the "Program Manager" user opens the date range filter on the Driver Id assignment page
    When the user selects date & the user clicks Apply in driver id assignment page
    Then the data belong to the date range are listed in driver id assignment page

  Scenario: Fiter by Driver in driver id assignment page
    Given the "Program Manager" user clicks on "Select Search" filter & the user selects Driver in driver id assignment page
    When the user enters driver name into "Search Name or ID" field & the user selects one name from suggestion list in driver id assignment page
    Then the data belong to the driver name are listed in driver id assignment page

  Scenario: Fiter by Vehicle in driver id assignment page
    Given the "Program Manager" user clicks on "Select Search" filter & the user selects "Vehicle" in driver id assignment page
    When the user enters vehicle name into "Search Vehicle Name" field & the user selects one vehicle name from suggestion list in driver id assignment page
    Then the data belong to the vehicle name are listed in driver id assignment page

#  @LQ-229
#  Scenario: Filter group(s) in Device health page
#    Given the "Program Manager" user is in the Device Health page
#    When the user sets group filter to one group in the Device Health page
#    Then the data belong to the group are listed in the Device Health page
#
#  Scenario: Filter Issue in Device health page
#    When the user clicks on "Select Issue" filter & the user selects Overdue for Check-in
#    Then the data belong to the Overdue for Check-in issue are listed in the Device Health page

#  Scenario: Filter Power Disconnects in Device health page
#    When the user clicks on "Select Issue" filter & the user selects Power Disconnects
#    Then the data belong to the Power Disconnects issue are listed in the Device Health page and the table is displayed with columns: "DEVICE", "DEVICE TYPE", "VEHICLE", "GROUP", "DISCONNECT TIME", "RECONNECT TIME","DURATION"

#  Scenario: Search Device in Device health page
#    When the user clicks on "Select Search" filter & the user selects "Device" & the user enters some characters into "Search Device" field in the Device Health page
#    Then the data that contained inputted characters in the serial number are shown in the Device Health page
#
#  Scenario: Search Vehicle in Device health page
#    When the user clicks on "Select Search" filter & the user selects "Vehicle" & the user enters some characters into "Search Vehicle" field in the Device Health page
#    Then the data that contained inputted characters in the Vehicle name are shown in the Device Health page
