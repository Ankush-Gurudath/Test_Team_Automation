Feature: Sanity Test for Geotab

  @LQ-306
  Scenario: Sanity Test for PROD Customers
    Given the login page is displayed in the browser
    When the user enters username/password, clicks the login button in the page and select company from the list
    Then the user is successfully logged into the Driver Safety dashboard

  @LQ-74
  Scenario: HOS Suite
    When the user clicks HOS tab
    Then the HOS main page is loaded successfully

  @LQ-93605
  Scenario: User can successfully navigate to Compliance Logs
    When the user clicks Compliance and navigates to logs
    Then the HOS Logs page is loaded successfully

  @LQ-93606
  Scenario: User can successfully navigate to HOS Violations
    When the user clicks Compliance and navigates to Violations
    Then the HOS Violations page is loaded successfully

  @LQ-93607
  Scenario: User can successfully navigate to Assets
    When the user clicks the Assets menu item
    Then the Assets page is loaded successfully
