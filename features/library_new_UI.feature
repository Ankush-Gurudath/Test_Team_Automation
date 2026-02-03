Feature: Library

  @LQ-263
  Scenario: Driver Safety - Library Suite
    Given the coach user logs in
    When the user clicks "LIBRARY" and then clicks "EVENTS"
    Then the events page is displayed and the table is displayed with columns "EVENT ID","DRIVER","GROUP","VEHICLE","EVENT DATE","SCORE","STATUS","TRIGGER" and "BEHAVIORS"

  @LQ-5541
  Scenario: Reassign driver in event preview
    When the user reassigns a driver in event preview
    Then the event driver is updated

  @LQ-15537
  Scenario: Link to driver profile from event list
    When the user clicks the driver name of one event
    Then the corresponding driver profile page is opened

  @LQ-15538
  Scenario: Open event preview event list
    When the user clicks "LIBRARY" and then clicks "EVENTS" and the user clicks the event ID
    Then the event preview is opened

  @LQ-262
  Scenario: Filter group in events page
    When the user sets group filter to one group
    Then the events in the selected group and subgroup are displayed

  Scenario: Filter date in event page
    When the user sets date filter as one option
    Then the events in the selected date range are displayed

  Scenario: Filter event type in event page
    When the user selects coachable from type filter
    Then only the events with the selected type are displayed

  Scenario: Filter event triggers in event page
    When the user selects some triggers from trigger filter
    Then all the events triggered by selected triggers are displayed

  Scenario: Filter event behavior in event page
    When the user selects some behaviors from behavior filter
    Then all the events including one or more of the selected behavior are displayed

  Scenario: Filter event status in event page
    When the user selects one option from status filter
    Then only the events in the selected status are displayed in events list

  Scenario: Search event by event ID in event page
    When the user selects the "Event Id" from "Select Search" drop down list and the user inputs an valid custom event ID and the user clicks search button
    Then the searched event is displayed

  Scenario: Search event by driver in event page
    When the user selects the "Driver" from "Select Search" drop down list and the user inputs the valid driver name and the user selects that value from suggested list
    Then the events of this driver are displayed

  Scenario: Search event by vehicle in event page
    When the user selects the "Vehicle" from "Select Search" drop down list and the user inputs the valid vehicle name and the user selects that value from suggested list
    Then the events of this vehicle are displayed

  Scenario: Search event by device in event page
    When the user selects the "Device" from "Select Search" drop down list and the user inputs the valid ER serial number and the user selects that value from suggested list
    Then the events of this device are displayed

#    Commenting due to an open issue in the library filter function - Status filter
#  @LQ-136311
#  Scenario: Verify user can add behavior tag to an event
#    When the user selects an event and adds a behavior tag (e.g., "Driver Smoking")
#    Then the behavior tag should be saved and displayed for the event
#
#  @LQ-136313
#  Scenario: Verify user can remove a behavior tag from an event
#    When the user removes the behavior tag
#    Then the tag should be removed successfully


  @LQ-5540
  Scenario: Add event level recognition in event preview
    When the user click "Add Recognition" button and the user clicks "Complete" button
    Then the Recognition is added

  @LQ-5542
  Scenario: Reassign group in event preview
    When the user changes the event group to another group in event preview
    Then the event group is updated


  @LQ-265
  Scenario: Batch move event in event page
    When the user check on some events and the user clicks "Move Group" and the user selects target group and the user clicks "Done" and the user clicks "Continue"
    Then the selected events are moved

  @LQ-391
  Scenario: View Recognition History
    When the user clicks "LIBRARY" and the user clicks "RECOGNITION HISTORY"
    Then all recognition history are displayed and the table is displayed with columns "TYPE","DRIVER","GROUP","EVENTID","ISSUED BY","ISSUED DATE","RECOGNITION REASON"

  @LQ-393
  Scenario: Filter group in Recognition History
    When the user sets group filter to one group in Recognition History
    Then the data belong to the selected group are displayed in Recognition History

  Scenario: Filter date in Recognition History
    When the user sets date filter in Recognition History
    Then the data belong to the selected date range are displayed

#  Scenario: Search driver in Recognition History
#    When the user selects the "Driver" from "Select Search" drop down list and the user inputs a valid driver name and the user selects that value from suggested list in RH
#    Then the recognitions of this driver are displayed
#
#  Scenario: Search issued by in Recognition History
#    When the user selects the "Issued By" from "Select Search" drop down list and the user inputs a valid user name and the user selects that value from suggested list
#    Then the recognitions of this user are displayed

  Scenario: Search event id in Recognition History
    When the user selects the "Event ID" from "Select Search" drop down list and the user inputs an valid custom event ID and the user clicks search button
    Then the recognition related to searched event ID is displayed

  @LQ-5556
  Scenario: Links in Recognition History - Type
    When the user clicks "TYPE" in RH
    Then the corresponding "recognition certificate" page is opened

  @LQ-394
  Scenario: Links in Recognition History - Driver
    When the user clicks "DRIVER" in RH
    Then the corresponding "driver profile" page is opened

  Scenario: Links in Recognition History - Event ID
    When the user clicks "Event ID" in RH
    Then the corresponding "event preview" page is opened

  Scenario: Links in Recognition History - Issued By
    When the user clicks "Issued By" in RH
    Then the corresponding "coach profile" page is opened

#  @LQ-396
#  Scenario: Download recognition certificate from Recognition History
#    When the user opens a recognition and clicks "Download" button
#    Then the recognition is downloaded

  Scenario: Edit recognition certificate from Recognition History
    When the user opens a recognition, clicks "Edit" button, updates "Recognition Reason" and clicks "Complete" button
    Then the recognition is updated

  Scenario: Delete recognition certificate from Recognition History                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          recognition certificate from Recognition History
    When the user opens a recognition and the user clicks "Delete" button
    Then the recognition is deleted

  @LQ-386
  Scenario: View Data Export page
    When the user clicks "LIBRARY" and the user clicks "DATA EXPORT"
    Then the requested records are displayed and the table is displayed with columns "REPORT TYPE", "GROUP", "DATE RANGE", "FILTERS", "REQUESTED DATE","ACTION" and a "New Export" button

#  @LQ-389
# Scenario: Request event data
#   When the user clicks "New Export" button and the user selects "Event Data" option and the user sets date filter and the user clicks "Request Data"
#   Then the event data is requested
#
#  Scenario: Request speed data
#   When the user clicks "New Export" button and the user selects "Speed Data" option and the user sets group filter to one group and the user clicks "Request Data"
#   Then the speed data is requested
#
#  @LQ-388
# Scenario: Download Requested record in WS Library data export page
#   When the user clicks "Download" button in Library data export page
#   Then the Library data export data is downloaded

  @LQ-400
  Scenario: The session list is displayed
    When the user clicks "LIBRARY" and then clicks "COACHING HISTORY"
    Then the Coaching History page is displayed and the table is displayed with columns "SESSION ID", "COACH DATE", "OVERDUE DATE", "DRIVER","BEHAVIORS COACHED","GROUP","COACH","NOTES" and the coaching sessions count is displayed

  @LQ-401
  Scenario: Filter group in Coaching History
    When the user sets group filter to one group in Coaching History
    Then the data belong to the selected group are displayed in Coaching History

  Scenario: Filter Date in Coaching History
    When the user sets date filter in Coaching History
    Then the data belong to the selected daterange are displayed

  Scenario: Filter event behavior in Coaching History
    When the user selects unusual event
    Then the coaching sessions that contained selected coachable behaviors are displayed

#  Scenario: Search driver in Coaching History
#    When the user selects the "Driver" from "Select Search" drop down list in CH and the user inputs the valid driver name and the user selects that value from suggested list
#    Then the coaching session of this driver are displayed
#
#  Scenario: Search coach in Coaching History
#    When the user selects the "Coach" from "Select Search" drop down list in CH and the user inputs a valid coach name and the user selects that value from suggested list
#    Then the coaching session of this coach are displayed
#
#  Scenario: Search session ID in Coaching History
#    When the "Session Id" is selected from select search drop down list in CH and the user inputs a valid coaching session ID and the user clicks search button
#    Then the searched coaching session is displayed

  @LQ-403
  Scenario: View Past Session page
    When the user clicks one session id
    Then the Past Session page is opened and the Past Session page includes "Summary","Session Notes", "X Events Coached"

  # LQ-402/405 are commented out until the API creates an event with a behavior.they are P1 label
#@LQ-402
#Scenario: Links in Coaching History
#  Given an event is coached
#  When the user clicks session ID in Coaching History
#  Then the past session page is opened
#
#Scenario: Links in Coaching History
#  When the user clicks driver in Coaching History
#  Then the corresponding driver profile page is opened
#
#Scenario: Links in Coaching History
#  When the user clicks coach in Coaching History
#  Then the corresponding "coach profile" page is opened
#-------------------------------------------------------------------------------------------------
#@LQ-403
#Scenario: View Past Session page
#  Given the "Coach" user is in Coaching History
#  When the user clicks one session id
#  Then the Past Session page is opened
#  And the Past Session page includes "Summary","Session Notes", "X Events Coached"
#
#@LQ-405
#Scenario: Add session notes in Past Session page
#  Given the Past Session page is opened
#  When the user inputs some charactors
#  And the user clicks "Submit" button
#  Then the session notes is added
#  And the author and date of new added session notes are displayed
#
#Scenario Outline: Links in Past Session
#  Given the "Coach" user is in Past Session page
#  When the user clicks "<Name>" in Past Session page
#  Then the corresponding "<page>" page is opened
#
#Examples:
#  | Name        | page           |
#  | driver name | driver profile |
#  | coach name  | coach profile  |
#
#Scenario: Open the event preview from Past Session page
#  Given the "Coach" user is in Past Session page
#  When the user clicks one coached event ID
#  Then the corresponding event preview is opened
#
#
#Scenario: Download PDF report from Past Session page
#  Given the "Coach" user is in Past Session page
#  When the user clicks "Download PDF" button
#  Then the corresponding coaching session report is downloaded
