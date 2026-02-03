Feature: End to end Fleet Map workflow
  As a developer,
  I want to run end to end tests on the Fleet Map application
  So I can confirm that code changes have not adversely affected the app.

  @LQ-15218
  Scenario: JB Hunt Fleet
    Given the login page is displayed
    When the user enters a JBHunt username/password and clicks the login button
    Then the Fleet application is displayed

  @LQ-15218
  Scenario: Foodliner Fleet
    When the user enters a Foodliner username/password and clicks the login button
    Then the Fleet application is displayed

  @LQ-15218
  Scenario: UPS Fleet
    When the user enters a UPS username/password and clicks the login button
    Then the Fleet application is displayed

  @LQ-15218
  Scenario: Ryder Fleet
    When the user enters a Ryder username/password and clicks the login button
    Then the Fleet application is displayed