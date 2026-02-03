Feature: Admin - User Management Workflow

  @LQ-304
  Scenario: Admin - Login
    Given the login page is displayed
    When the user enters a newly created username/password and clicks the login button
    Then the user is successfully logged into the Driver Safety dashboard


  @LQ-251
  Scenario: The User Management page is displayed
    When the user clicks on Admin tab
    Then the page header "USER MANAGEMENT" is displayed and the user count are displayed and the table is displayed with columns: "NAME", "EMPLOYEE ID", "LYTX BADGE", "PRIMARY DRIVER GROUP", "ROLES (GROUP)", "STATUS", "LOGIN", "USERNAME"


  @LQ-253
  Scenario: Add user on the User Management page
    When the user clicks on "Add User" & the user enters required fields: "First Name", "Last Name", "EmployeeID", "Email", "Cell Phone", "Group" and "Role" on the "Info" tab & the user clicks "Create User"
    Then the user is added


  @LQ-254
  Scenario: Edit user on the User Management page
    Given the "Program Manager" user is in the Edit User page
    When the user clicks on the name of a user & the user changes "First Name" on Edit User page & the user clicks Save Changes
    Then the First Name of the edited user is updated


  Scenario: Edit report and notification on the User Management page
    Given the "Program Manager" user is in the Edit self page
    When the user adds a notification on the "Notification" tab & the user adds a report on the "Report" tab & the user clicks Save Changes
    Then the notification and report are added for the user & the edited user receives the subscribed report at the selected date time


  Scenario: Delete user on edit user page
    When the user clicks on the "Delete user" & the user clicks "Confirm" button on the popup message
    Then the selected user is deleted