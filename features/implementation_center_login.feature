Feature: Implementation Center - Login

  @ES-13739
  Scenario: validate login functionality
    Given the login page is displayed in the browser
    When the user with Implementation center account enters username/password, clicks the login button in the page
    And user select an account from the account selection dropdown
    Then User is successfully logged into the Implementation center dashboard and validate page title

  @ES-13740
  Scenario: validate logout functionality
    When user logout from the application
    Then verify signin page visible