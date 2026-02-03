Feature: Implementation Center - Location

  @ES-13730
  Scenario: verify navigation menu
    Given the login page is displayed in the browser
    When the user with Implementation center account enters username/password, clicks the login button in the page
    And user select an account from the account selection dropdown
    Then User is successfully logged into the Implementation center dashboard and validate page title

  @ES-13731
  Scenario: Validate add location pop up labels and placeholders
    When user navigate to location page
    Then validate location dashboard app heading and page heading
    And validate location page add location pop up
    And validate all labels and placeholder

  @ES-13732
  Scenario: Validate USA and CANADA options should be visible under country dropdown
    When click on select country dropdown
    Then validate USA and canada country option visible

  @ES-13733
  Scenario: Validate user should be able to add usa location
    When save the location information
    Then Validate location success notification should appear
    And validate location dashboard app heading and page heading
    And validate the recently added record on location page

  @ES-13734
  Scenario: Validate location info on edit location
    When user navigate to edit location pop up
    Then Validate location info on edit location
    And close the edit popup

  @ES-14962
  Scenario: Validate user is able to download a location template
    When user download the location template
    Then validate the downloaded location template

  @ES-14963
  Scenario: Validate user is able to import location
    When user upload location template
    Then validate locations should be imported

  @ES-14964
  Scenario: Validate user is able to download location records
    When user download location records
    Then validate the downloaded location records

  @ES-14965
  Scenario: To validate pagination functionality
    When user click on pagination next button
    Then validate next 50 records should be visible
    When user click on pagination previous button
    Then validate previous 50 records should be visible

  @ES-14966
  Scenario: To validate filter functionality
    When user select Inactive filter
    Then validate only Inactive records should be visible under table result
    When user select Active filter
    Then validate only active records should be visible under table result

  @ES-14967
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

  @ES-14968
  Scenario: Validate search functionality on location dashboard
    When user provide the location name to search
    Then validate result table should be filtered based on searched text

  @ES-14969
  Scenario: validate welcome pop up
    When user open welcome popup
    Then validate welcome pop up
    And close welcome popup

  @ES-14970
  Scenario: user is able to navigate to the LYTX support center
    When user click on LYTX support center link
    Then user should land on Lytx support center dashboard