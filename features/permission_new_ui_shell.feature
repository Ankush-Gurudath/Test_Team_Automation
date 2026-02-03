Feature: Fleet Telematics - Permission with New UI Shell

  @LQ-147460
  Scenario: Multi Company Access User Permission to New UI Fleet Telematics
    Given the login page is displayed in the browser
    When the multi company access user enters username/password, clicks the login button in the page and select company from the list
    Then the user should successfully login to newui and land on the Driver Safety Home page, and all tabs such as Video Search, Driver Safety, Admin, Fleet Tracking, Fleet Telematics, DVIR should be displayed

  @LQ-136509
  Scenario: Full Access User Permission to New UI Fleet Telematics
    When the full access role user enters username/password and clicks the login button
    Then the user should successfully login to newui and land on the Driver Safety Home page, and all tabs such as Video Search, Driver Safety, Admin, Fleet Tracking, Fleet Telematics, DVIR should be displayed

  @LQ-136510
  Scenario: Driver User permission to New UI Fleet Telematics
    When the driver role user enters username/password and clicks the login button
    Then the user should successfully login to newui and land on the Driver Safety Home page, tabs such as Driver Safety, Fleet Telematics, DVIR should be displayed and tabs such as Admin, Fleet Tracking, Video Search should not be displayed

  @LQ-136511
  Scenario: Coach User permission to New UI but not to Fleet Telematics
    When the coach role user enters username/password and clicks the login button
    Then the user should successfully login to newui and land on the Driver Safety Home page, tabs such as Driver Safety and Admin should be displayed but not fleet telematics

  @LQ-136490
  Scenario: Safety Manager User permission to New UI but not to Fleet Telematics
    When the safety manager role user enters username/password and clicks the login button
    Then the user should successfully login to newui and land on the Driver Safety Home page, tabs such as Driver Safety and Admin should be displayed but not fleet telematics

  @LQ-136493
  Scenario: Safety Manager Plus User permission to New UI but not to Fleet Telematics
    When the safety manager plus role user enters username/password and clicks the login button
    Then the user should successfully login to newui and land on the Driver Safety Home page, tabs such as Driver Safety and Admin should be displayed but not fleet telematics

  @LQ-136508
  Scenario: Safety Read Only User permission to New UI but not to Fleet Telematics
    When the safety read only role user enters username/password and clicks the login button
    Then the user should successfully login to newui and land on the Driver Safety Home page, tabs such as Driver Safety and Admin should be displayed but not fleet telematics

  @LQ-136491
  Scenario: Fleet Dispatcher User permission to New UI but not to Fleet Telematics
    When the fleet dispatcher role user enters username/password and clicks the login button
    Then the user should successfully login to newui and land on the Fleet Tracking Home page, tabs such as Fleet Tracking and Admin should be displayed but not fleet telematics

  @LQ-136492
  Scenario: Fleet Read Only User permission to New UI but not to Fleet Telematics
    When the fleet read only role user enters username/password and clicks the login button
    Then the user should successfully login to newui and land on the Fleet Tracking Home page, tabs such as Fleet Tracking and Admin should be displayed but not fleet telematics

  @LQ-136694
  Scenario: Video Reviewer User permission to New UI but not to Fleet Telematics
    When the video reviewer role user enters username/password and clicks the login button
    Then the user should successfully login to newui and land on the Video Search page, and fleet telematics should not be displayed

  @LQ-136695
  Scenario: Video Reviewer Plus User permission to New UI but not to Fleet Telematics
    When the video reviewer plus role user enters username/password and clicks the login button
    Then the user should successfully login to newui and land on the Video Search page, and fleet telematics should not be displayed

  @LQ-136489
  Scenario: Program Manager User permission to New UI but not to Fleet Telematics
    When the program manager role user enters username/password and clicks the login button
    Then the user should successfully login to newui and land on the Driver Safety Home page, tabs such as Driver Safety and Admin should be displayed but not fleet telematics

  @LQ-136507
  Scenario: Program Manager Assistance User permission to New UI but not to Fleet Telematics
    When the program manager assistance role user enters username/password and clicks the login button
    Then the user should successfully login to newui and land on the Driver Safety Home page, tabs such as Driver Safety and Admin should be displayed but not fleet telematics

  @LQ-136502
  Scenario: Event Dispatcher User permission to New UI but not to Fleet Telematics
    When the event dispatcher role user enters username/password and clicks the login button
    Then the user should successfully login to newui and land on the Driver Safety Home page, tabs such as Driver Safety and Admin should be displayed but not fleet telematics

  @LQ-147462
  Scenario: Compliance Manager User permission to New UI but not to Fleet Telematics
    When the compliance manager role user enters username/password and clicks the login button
    Then the user should successfully land on the HOS page and fleet telematics should not be displayed

  @LQ-147461
  Scenario: Compliance Read Only User permission to New UI but not to Fleet Telematics
    When the compliance read only role user enters username/password and clicks the login button
    Then the user should successfully land on the HOS page and fleet telematics should not be displayed

  @LQ-136510
  Scenario: Fleet Telematics Manager User permission to New UI Fleet Telematics
    When the fleet telematics manager role user enters username/password and clicks the login button
    Then the user should successfully login to newui and land on the Admin page and Fleet Telematics should be displayed