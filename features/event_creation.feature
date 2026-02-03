Feature: Event Creation

  @LQ-263
  Scenario: Event Creation
    Given the coach user logs in
    When the user clicks "LIBRARY" and then clicks "EVENTS"
    Then the events page is displayed and the table is displayed with columns "EVENT ID","DRIVER","GROUP","VEHICLE","EVENT DATE","SCORE","STATUS","TRIGGER" and "BEHAVIORS"

  @LQ-47009
  Scenario: Add Behavior
    When the user adds a behavior
    Then the behavior is added

  @LQ-6820
  Scenario: Remove Behavior
    When the user removes a behavior
    Then the behavior is removed

  @LQ-5544
  Scenario: Driver Self coaching
    When the user clicks "Coach Event" & the user clicks "Complete Session"
    Then the event is coached