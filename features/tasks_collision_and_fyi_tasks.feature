Feature: Collision and FYI tasks Workflow

  @LQ-304
  Scenario: Tasks - Collision and FYI Tasks Suite
  #Scenario: Driver Safety - Collision and FYI Tasks
    Given the welcome login page is displayed
    When the "Coach" user inputs name and password and the user clicks "Sign In" button on welcome login page
    Then the Driver Safety page is opened

  @LQ-305
  Scenario: Logout Driver Safety
    When the user clicks "Sign Out" button from DC
    Then the DC login page is opened

  @LQ-324
  Scenario: Choose No for a possible collision event
    Given "Safety Manager" user is in Collisions page
    When the user previews a possible collision event and the user chooses "No,It is not a collision" for the event and the user clicks "Yes,Confirm" in pop-up
    Then the possible collision event is changed to new status

  Scenario: Choose Yes for a possible collision event
    Given "Safety Manager" user go to Collisions page
    When the user previews a possible collision event and the user chooses "Yes,It is a collision" for the event and the user clicks "Yes,Confirm" in pop-up
    Then the event is changed to Collision event

  @LQ-318
  Scenario: View Collisions tasks
    When the user clicks "TASKS" and the user clicks "COLLISIONS"
    Then the task count is displayed and there are "DRIVER NAME", "GROUP", "VEHICLE", "EVENT DATE", "TIME" for each card and there is "Preview" button

  @LQ-319
  Scenario: Filter group in Collisions page
    When the user sets group filter to one group in collisions page
    Then the tasks belong to the group are listed in collisions page

  @LQ-320
  Scenario: Search driver in Collisions page
    When the user inputs some characters in search box in collisions page
    Then the tasks which driver name contains the inputted characters are shown in collisions page

  @LQ-323
  Scenario: Resolve collision event
    When the user previews a collision event and the user clicks "Resolve" and the user clicks "Yes,Confirm" in pop-up
    Then the collision event status is resolved

  Scenario: Coach Later for collision event
    When the user previews a collision event and the user clicks "Coach Later" and the user clicks "Yes,Confirm" in pop-up
    Then the event status is Face-To-Face

  Scenario: Coach Now for collision event
    Given "Safety Manager" user is in Collisions page and search a collision event with driver assigned
    When the user previews a collision event and the user clicks "Coach Now" and the user clicks "Yes,Confirm" in pop-up
    Then driver coaching session page is opened and the collision event status is Face-To-Face

  @LQ-326
  Scenario: Filter group in FYI Notify page
    Given Safety Manager user is in FYI Notify page
    When the user sets group filter to one group in FYI Notify page
    Then the FYI Notify tasks belong to the group are listed in FYI Notify page

  @LQ-327
  Scenario: Search driver in FYI Notify page
    When the user inputs some characters in search box in FYI Notify page
    Then the tasks which driver name contains the inputted characters are shown in FYI Notify page

  @LQ-325
  # need to add behavior label once api creates event with behavior
  Scenario: View FYI Notify tasks
    Given coach user in dashboard page
    When the user clicks "TASKS" & the user clicks "FYI NOTIFY"
    Then  there are "GROUP", "VEHICLE", "EVENT DATE", "TIME" for each card & there is "Preview" button

  @LQ-330
  Scenario: Resolve FYI Notify event
    When the user previews a FYI Notify event & the user clicks "Resolve" & the user clicks "Yes,Confirm" in pop-up
    Then the event status is resolved

  Scenario: Coach Later for FYI NOTIFY event
    When the user previews a FYI Notify event & the user clicks "Coach Later" & the user clicks "Yes,Confirm" in pop-up
    Then the FYI event status is Face-To-Face

  Scenario: Coach Now for FYI Notify event
    Given the FYI event with driver assigned
    When the user previews a FYI Notify even & the user clicks "Coach Now" & the user clicks "Yes,Confirm" in pop-up
    Then driver coaching session page is opened and the event status is Face-To-Face

  @LQ-276
  Scenario: Bulk coach Due For Coaching task
    Given "Safety Manager" user is in Due For Coaching page
    When the user navigate to Driver coaching session page and the user views one event and complete the coaching session
    Then the both Events are coached