Feature: Localization

  @LQ-306
  Scenario: Localization Test
    Given the login page is displayed in the browser
    When the user with multi company account enters username/password, clicks the login button in the page and select company from the list
    Then the user is successfully logged into the Driver Safety dashboard

  @LQ-53288
  Scenario: Localization - Event Suite
    When the user clicks "LIBRARY" and then clicks "EVENTS"
    Then the Date displays with correct format for every language

  @LQ-262290
  Scenario: Verify Overlay label
    When search an event with no adas and open the event
    Then the overlay label is displayed in the selected language

  Scenario: Verify tooltip translation
    When user hovers over the button to see the tooltip
    Then the tooltip is displayed in the selected language

  Scenario: localized file name format
    When the user downloads the "MP4 with overlay" file
    Then the file name is displayed in the selected language format