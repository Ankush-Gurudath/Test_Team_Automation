Feature: Permission Tests

@LQ-306
Scenario: Permission Test
  Given the login page is displayed in the browser
  When the user with multi company account enters username/password, clicks the login button in the page and select company from the list
  Then the user is successfully logged into the Driver Safety dashboard


@LQ-49067
Scenario: Full Access User Permission
  When the full access user lands on dashboard page
  Then the full access user should see Driver Safety & Fleet Tracking & Video Search & Admin & HOS tabs

@LQ-49069
Scenario: Safety Manager permission
  When the safety manager user lands on the dashboard page
  Then the safety manager user should see only Driver Safety & Admin tabs

@LQ-49101
Scenario: Coach User permission
  When the coach user lands on the dashboard page
  Then the coach user should see only Driver Safety & Admin tabs

@LQ-49102
Scenario: Program manager User permission
  When the program manager user lands on the dashboard page
  Then the program manager user should see only Driver Safety & Admin tabs

@LQ-49366
Scenario: Program manager Assistant User permission
  When the program manager assistant user lands on the dashboard page
  Then the program manager assistant user should see only Driver Safety & Admin tabs

@LQ-49367
Scenario: Event Dispatcher User permission
  When the event dispatcher user lands on the dashboard page
  Then the event dispatcher user should see only Driver Safety & Admin tabs

@LQ-49368
Scenario: Safety Read Only User permission
  When the safety read only user lands on the dashboard page
  Then the safety read only user should see only Driver Safety & Admin tabs

@LQ-49369
Scenario: Driver User permission
  When the driver user lands on the dashboard page
  Then the  driver user should see only Driver Safety & DVIR tabs

@LQ-49370
Scenario: Fleet Dispatcher User permission
  When the fleet dispatcher user lands on the Fleet Tracking page
  Then the fleet dispatcher user should see only Fleet Tracking & Admin tabs

@LQ-49371
Scenario: Fleet Read Only User permission
  When the fleet read only user lands on the Fleet Tracking page
  Then the fleet read only user should see only Fleet Tracking & Admin tabs

@LQ-49372
Scenario: Video Reviewer User permission
  When the video reviewer user lands on the dashboard page
  Then the video reviewer user should see only Video Service tab

@LQ-49373
Scenario: Video Reviewer Plus User permission
  When the video reviewer plus user lands on the dashboard page
  Then the video reviewer user should see only Video Service tab

@LQ-50532
Scenario: Permission DC Test
  Given the login page for DC is displayed in the browser
  When the full access user lands on dashboard DC page
  Then the user is successfully logged into the Driver Safety DC dashboard

@LQ-50533
Scenario: Permission Fleet Test
  Given the login fleet page is displayed in the browser
  When the fleet dispatcher user login to fleet login page
  Then the fleet dispatcher user successfully lands on Fleet Tracking dashboard
  When the fleet read only user login to fleet login page
  Then the fleet read only user successfully lands on Fleet Tracking dashboard

#@LQ-50534
#Scenario: Permission SSO Coach Test
#Given the login SSO page is displayed in the browser
#When the coach user login to sso login page
#Then the coach user successfully lands on Driver Safety dashboard from SSO
#
#@LQ-50535
#Scenario: Permission SSO Driver Test
#Given the login SSO page is displayed in the browser for driver user
#When the driver user login to sso login page
#Then the driver user successfully lands on Driver Safety dashboard from SSO

@LQ-131502
Scenario: Drivecam SSO in all uppercase is redirected to cloud SSO
  Given the Drivecam Online SSO login page is accessed using all uppercase SSO
  Then the user is redirected to the cloud SSO login page

@LQ-131504
Scenario: Drivecam SSO in all lowercase is redirected to cloud SSO
  Given the Drivecam Online SSO login page is accessed using all lowercase sso
  Then the user is redirected to the cloud SSO login page