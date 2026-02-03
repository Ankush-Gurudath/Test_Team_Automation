Feature: Admin - User Management - Old UI

  @LQ-304
  Scenario: Admin - User Management Suite
    Given the login page is displayed
    When the user enters a newly created username/password and clicks the login button
    Then the user is successfully logged into the Driver Safety dashboard

  @LQ-251
  Scenario: The User Management page is displayed
    Given the "Program Manager" user is in the Driver Safety page
    When the user clicks on Admin tab
    Then the page header "USER MANAGEMENT" is displayed and the user count are displayed and the table is displayed with columns: "NAME", "EMPLOYEE ID", "LYTX BADGE", "PRIMARY DRIVER GROUP", "ROLES (GROUP)", "STATUS", "LOGIN", "USERNAME"

  @LQ-136209
  Scenario: Verify the "Users" module
    When the user clicks on the "Users" menu
    Then the user should be able to see all the filters like "Select Group(s)","Roles","Login" ,"Status", "Reset" and "Search Name or ID"
    And the user should see the buttons "Import Users" and "Add Users"
    And the user should see the pagination and download CSV in the bottom of the page

  @LQ-252
  Scenario: Filter group(s) on the User Management page
    When the user sets group filter to one group
    Then the users belong to the group are listed

  @LQ-TB
  Scenario: verify the group filter functionality
    When the user selects multiple groups from the "Select Group(s)" filter
    Then the users belong to the selected groups are listed

  Scenario: Filter Role on the User Management page
    When the user clicks on "Roles" filter & the user selects one role
    Then the users with the selected role are displayed on the table

  Scenario: Filter Login status on the User Management page
    When the user clicks on "Login" filter & the user selects "Enable"
    Then the users with Login enabled are displayed on the table

  Scenario: Filter Status on the User Management page
    When the user clicks on "Status" filter & the user selects "Inactive"
    Then the inactive users are displayed on the table

  Scenario: Search Name or ID on the User Management page
    When the user enters some characters into "Search Name or ID" field
    Then the users that have the inputted characters in their name or employeeid are shown

  @LQ-12783
  Scenario: The Driver badge model pops up
    When the user clicks Driver ID of one driver
    Then Preview badge page appeared and three buttons "Cancel","Download Badge","Email Badge" displayed on the bottom

  @LQ-2593
  Scenario: The Driver badge on Add User Page
    Given the "Program Manager" user is in the Add User Page
    When the user adds one driver role
    Then the LYTX BADGE section will display a Lytx icon without QR code and a message on the right: "Will be created once the user is added."

  @CODE-2045
  Scenario: Add driver user without emailid and without enabling login on the Add User Page
    When the user add firstname, lastname, select group, role as driver and click on create button
    Then the driver user is added successfully and qr_code is displayed

  @LQ-253
  Scenario: Add user on the User Management page
    When the user clicks on "Add User" & the user enters required fields: "First Name", "Last Name", "EmployeeID", "Email", "Cell Phone", "Group" and "Role" on the "Info" tab & the user clicks "Create User"
    Then the user is added

  @LQ-257
  Scenario: Edit group on the User Management page
    When the user checks some available users & And the user clicks "Edit Group" & the user selects a group & the user selects a role & the user clicks Apply
    Then the new role-group is added to the selected users

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

#  @LQ-259
#  Scenario: Change status on the User Management page
#    When the user checks some available users & the user clicks "Change Status" & the user selects "Inactive" & the user clicks Apply
#    Then the status of selected users is updated to Inactive

  @LQ-261
  Scenario: Edit Login on the User Management page
    When the user checks some available users & the user clicks "Edit Login" & the user selects "Enable" & the user clicks Apply
    Then the login status of selected users is updated to Enable

  @LQ-248
  Scenario: View user info on my account
    When the user clicks humanoid icon & the user clicks MY ACCOUNT
    Then the user info is displayed in Info tab with: "FIRST NAME", "LAST NAME", "EMPLOYEE ID" & the contact Information is displayed in contact Info tab with: "EMAIL ADDRESS", "CELL PHONE" &  the group role assignment is displayed in Info tab with: "GROUP ROLE ASSIGNMENT" & the username and password is displayed in Info tab with: "USERNAME","PASSWORD" and Lytx Badge

  Scenario: Edit email and cell phone on my account
    When the user clicks the "Edit" icon on contact section & the user edits the email address with valid value &  the user clicks "Save" button
    Then the info is updated

  @LQ-250
  Scenario: Reports tab in my account page
    When the user opens reports tab in My account page
    Then reports are displayed

  @LQ-249
  Scenario: Notifications tab in my account page
    When the user navigates to notification tab in my account page
    Then the subscribed notifications are listed

  @LQ-258
  Scenario: Delete users on the User Management page
    When the user checks some available users & the user clicks "Delete Users" & the user clicks "Confirm"
    Then the status of selected users is updated to deleted

  @240087
  Scenario: Verify that the User Audit log tab is displayed
    Given internal FA user login to the application
    When the user click on "Change View History" in the header of User Management Page
    Then the user should be able to see the table columns: "USER AFFECTED", "ACTION", "ACTION DETAILS","EDITOR", "ACTION DATE"
    And the user should see the User Audit log count along with the filters "Search User Affected" and "Select Action(s)" in the header
    And the user should see the buttons "Download Log"

  @LQ-240255
  Scenario: Verify Search audit log
    When user input a valid value in the "Search User Affected" field
    Then the searched user should be able to see in the User Audit Log

  Scenario: Verify search functionality with no matching user
    When user input an invalid value in the "Search User Affected" field
    Then it should display a message "No audit logs available for the selected user/date range" with empty table

  Scenario: Verify filter action type in User Audit Log
    When user select an action type from "Action Type" dropdown
    Then the user should be able to see the logs based on selected action type in the User Audit Log

    # Re-enable after DOM-2499 is fixed
#  Scenario: Verify filter date range in User Audit Log
#    When the user select a date range from "Date Range" dropdown
#    Then the user should be able to see the logs based on selected date range in the User Audit Log

  Scenario: Verify close User Audit Log tab
    When the user click on the "Close" button for the User Audit Log tab
    Then the user Audit Log tab should be closed successfully
    And verify it should be redirected back to the User Management page

  @LQ-240175
  Scenario: Verify successfully Download the audit logs in the CSV format
    When the user clicks on the "View Change History" icon in the header
    And the user clicks "Download Log" in the User audit log tab
    Then it should download the audit logs in the .CSV file format

  Scenario: Verify successfully download the audit logs with selected filter
    When search the specific name of any User in "Search User Affected" filter
    Then the "Download Log" in the User audit log tab is displayed

  Scenario: Verify the "Download Log" functionality is disabled when there is no audit log data
    When the user select any date from the calendar and select any Action from the dropdown filter
    Then the "Download Log" functionality should be disabled
