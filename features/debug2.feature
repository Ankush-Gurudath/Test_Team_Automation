Feature: Sanity Test for PROD Customers

  @LQ-306
  Scenario: Sanity Test for PROD Customers
    Given the login page is displayed in the browser
    When the user enters username/password, clicks the login button in the page and select company from the list
    Then the user is successfully logged into the Driver Safety dashboard

  @LQ-300
  Scenario: Navigate to FLEET TRACKING page from top navigation bar
    When user clicks on "FLEET TRACKING" on top navigation
    Then user is navigated to "FLEET TRACKING" accordingly