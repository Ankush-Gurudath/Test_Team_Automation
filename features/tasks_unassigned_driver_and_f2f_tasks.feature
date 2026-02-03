Feature: Unassigned driver and F2F Tasks Workflow

  @LQ-313
  Scenario: Tasks - Assign Driver and F2F Tasks Suite
  #Scenario: View Assign Drivers tasks
    Given the coach user logs in
    When the user clicks "TASKS" and the user clicks "ASSIGN DRIVERS"
    Then the task count is displayed & there is "Assign Selected" button with un-selectable status & there is "Move Group" button with un-selectable status & there are "VEHICLE", "GROUP", "EVENT DATE", "EVENT ID", "BEHAVIORS" column & there are checkbox & "ASSIGN" button for each Assign Driver task

  @LQ-315
  Scenario: Filter group in Assign Driver Task page
    When the user sets group filter to one group in assign driver page
    Then the Assign Driver tasks belong to the group are listed in assign driver page

  @LQ-316
  Scenario: Coach is able to assign a driver to an event
    When coach is able to see Assign Drivers tasks on the dashboard page and clicks on the tasks and directed to the Assign Driver page
    Then coach must successfully assign a driver to an event

  @LQ-266
  Scenario: View Due For Coaching tasks
    Given Safety Manager user is in Driver Safety
    When the user clicks "TASKS" & the user clicks DUE FOR COACHING
    Then the task count is displayed & there are some information on the card

  @LQ-274
  Scenario: View Driver Coaching Session page
    Given Safety Manager user is in Due For Coaching page
    When the user clicks "Coach X Events" of the first bundle card
    Then the Driver Coaching Session page is opened &  there is driver info in the page

  @LQ-267
  Scenario: Filter group in Due For Coaching page
    Given Safety Manager user is back in Due For Coaching page
    When the user sets group filter to one group
    Then the data belong to the group are listed

  Scenario: Filter trigger in Due For Coaching page
    When the user sets trigger filter to one trigger
    Then the data belong to the trigger are listed

  Scenario: Filter behavior in Due For Coaching page
    When the user sets behavior filter to one behavior
    Then the data belong to the behavior are listed

  Scenario: Filter driver in Due For Coaching page
    When the user enters some characters into "Search Name or ID" field
    Then the data that have the inputted characters in their name or employeeid are shown

  @LQ-6905
  Scenario: Coach is able to coach & share a coaching event
    Given coach is on Driver Coaching Session page
    When coach clicks on share button
    Then coach must successfully share a coaching event

  @LQ-312
  Scenario: Coach is able to add recognition to a coaching event
    When coach clicks on Add Recognition Tab
    Then coach must successfully Add Recognition to a coaching event

  @LQ-268
  Scenario: Coach is able to fill out and submit Contact Lytx form
    When coach clicks on Contact Lytx Tab
    Then coach must successfully fill out and submit the Contact Lytx form

  @LQ-275
  Scenario: Single coach Due For Coaching task
    When the user plays the video and the user adds event notes and the user adds session notes and the user clicks "Complete Session"
    Then the event is successfully coached

  @CIPHER-2845
  Scenario: Verify Coaching history date
    Given the user clicks "LIBRARY" and then clicks "COACHING HISTORY"
    When the user selects the "Coach" from "Select Search" drop down list in CH and the user inputs a valid coach name and the user selects that value from suggested list
#    Then the coaching date is correct  -- commented to investigate the failure

#  Those two cases are P1 label
#  @LQ-573
#  Scenario: Coach is able to add Event Notes to a coaching event
#    When coach clicks on Add Event Note button
#    Then coach must successfully add Event notes to a coaching event
#
#  Scenario: Coach is able to add Session Note to a coaching event
#    When coach clicks on Add Session Note button
#    Then coach must successfully add Session notes to a coaching event
#
#  @LQ-574
#  Scenario: Coach is able to complete a coaching session
#    When coach clicks on Complete session button
#    Then coach must successfully complete a coaching session event

  @LQ-317
  Scenario: Batch assign driver to some events in Assign Driver Task page
    When the user checks some events and the user clicks "Assign Selected" button and the user inputs some characters in input box of pop-up and the user selects one driver and the user clicks "Assign" button
    Then these events are assigned to driver


  @LQ-5543
  Scenario: Mark F2F event as self coaching
    Given the "Coach" user is in event preview
    When the user selects "Marked as Self Coaching" from more action & the user clicks "Yes, Confirm" button
    Then the event status is changed to self coaching

  @LQ-1994
  Scenario: Notify driver in due for coaching page
    Given driver with an F2F status event
    When the coach user clicks kebab in the task card & the user clicks "Notify Driver" & the user clicks "Notify"
    Then the event status is "Remote Coaching : Driver Notified"

  @LQ-17902
  Scenario: Verify the event status changes to FYI Notify from F2F event
    Given the Full Access user is in Events page there are some F2F events filtered out
    When the user clicks one F2F event id and the user clicks "More Actions" button the user clicks "Mark as FYI Notify" option and the user clicks "Yes,Confirm"
    Then the F2F status event changes to FYI Notify

  Scenario: Verify the event status changes to FYI Notify from self-coaching event
    Given the Full Access user is in Events page there are some self-coaching events filtered out
    When the user clicks one self-coaching event id and the user clicks "More Actions" button the user clicks "Mark as FYI Notify" option and the user clicks "Yes,Confirm"
    Then the Self Coaching status event changes to FYI Notify

  Scenario: Verify the event move to FYI Notify after marking as FYI Notify in Due for coaching page
    Given the Full Access user is in Due for coaching page
    When the user previews F2F event and the user clicks "More Actions" button and the user clicks "Mark as FYI Notify" option and the user clicks "Yes,Confirm"
    Then the previewed F2F events move to FYI Notify task

  Scenario: Verify the event move to FYI Notify after marking as FYI Notify in Assign Drivers page
    Given the Full Access user is in Assign Drivers page
    When the user previews one event and the user clicks "More Actions" button and the user clicks "Mark as FYI Notify" option and the user clicks "Yes,Confirm"
    Then the previewed events move to FYI Notify task


  @LQ-311
  Scenario: View remote events in Driver Profile page
    Given "Driver" user is in Driver Profile page
    When the user clicks "View Remote Events" button and the user plays video on event preview modal
    Then the event status is updated to "Remote Coaching: Driver Viewed"

  @LQ-5544
  Scenario: Driver Self coaching
    Given "Driver" user is in Due For Coaching page
    When the user clicks "Coach Event" & the user clicks "Complete Session"
    Then the event is coached
