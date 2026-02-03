Feature: Implementation Center - Vehicle

  @ES-13735
  Scenario: verify navigation menu
    Given the login page is displayed in the browser
    When the user with Implementation center account enters username/password, clicks the login button in the page
    And user select an account from the account selection dropdown
    Then User is successfully logged into the Implementation center dashboard and validate page title
    And validate vehicle dashboard app heading and page heading

  @ES-13736
  Scenario: Validate add vehicle pop up labels and placeholders
    When user click on Add vehicle button on Vehicle Lists page
    Then validate add vehicle pop up
    And validate all labels and placeholder

  @ES-13737
  Scenario: Validate user should be able to add a vehicle
    When save the vehicle information
    Then Validate add vehicle success notification should appear
    And validate vehicle dashboard app heading and page heading
    And validate the recently added record on vehicle page

  @ES-16590
  Scenario: validate user can able to update vehicle details
    When user click on recently added vehicle
    Then Validate vehicle info on edit vehicle
    And save updated details of vehicle information
    And Validate updated vehicle success notification should appear

  @ES-16591
  Scenario: Validate search functionality on vehicle dashboard
    When user provide the vehicle name to search
    Then validate result table should be filtered based on searched text

  @ES-16592
  Scenario: Validate user is able to download vehicle records
    When user download vehicle records
    Then validate the downloaded vehicle records

  @ES-16593
  Scenario: Validate user is able to download a vehicle template
    When user download the vehicle template
    Then validate the downloaded vehicle template

  @ES-16594
  Scenario: Validate user is able to import vehicle
    When user upload vehicle template
    Then validate vehicles should be imported

  @ES-13738
  Scenario: Validate user is able to delete vehicle
    When user will delete recently added vehicle
    Then Validate vehicle delete notification should appear

  @ES-16595
  Scenario: To validate pagination functionality
    When user click on pagination next button
    Then validate next 50 records should be visible
    When user click on pagination previous button
    Then validate previous 50 records should be visible

  @ES-16596
  Scenario: To validate show rows functionality
    Then validate total 50 records should be visible by default
    When user select 100 rows count from Show row
    Then validate total 100 records should be visible
    When user select 150 rows count from Show row
    Then validate total 150 records should be visible
    When user select 200 rows count from Show row
    Then validate total 200 records should be visible
    When user select 250 rows count from Show row
    Then validate total 250 records should be visible

  @ES-16597
  Scenario: validate welcome pop up
    When user open welcome popup
    Then validate welcome pop up
    And close welcome popup

  @ES-16598
  Scenario: user is able to navigate to the LYTX support center
    When user click on LYTX support center link
    Then user should land on Lytx support center dashboard