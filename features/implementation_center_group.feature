Feature: Implementation Center - Group

  @ES-14471
  Scenario: verify group navigation menu
    Given the login page is displayed in the browser
    When the user with Implementation center account enters username/password, clicks the login button in the page
    And user select an account from the account selection dropdown
    Then User is successfully logged into the Implementation center dashboard and validate page title
    And validate group page app heading and page heading

  @ES-14475
  Scenario: validate download group template functionality
    When user download the group template
    Then validate file should be downloaded

  @ES-14477
  Scenario: Validate user is able to import group hierarchy
    When user upload group template
    Then validate group submission success pop up
    And close submission pop up

  @ES-14478
  Scenario: validate welcome pop up
    When user open welcome popup
    Then validate welcome pop up
    And close welcome popup

  @ES-14479
  Scenario: user is able to navigate to the LYTX support center
    When user click on LYTX support center link
    Then user should land on Lytx support center dashboard