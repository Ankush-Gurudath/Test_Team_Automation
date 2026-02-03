Feature: Admin - Trailer Workflow

#
  @LQ-12128
  Scenario: The Trailer Management page is displayed
    Given Administrator user is in Admin
    When the user performs the Trailer Management workflow
    Then a trailer can be added, edited, have inspection lists set, and be filtered by group, and then deleted.
