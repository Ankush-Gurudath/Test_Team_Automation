Feature: Admin - Group Management New Ui Shell

  @LQ-136352
  Scenario: Admin - Group suite
    Given admin user logs in
    When user clicks groups tab
    Then groups management page is displayed
    And the user should be able to see the group hierarchy with hyperlinks present for each group like "Devices","Vehicles","Events" and "Users"
    And the user should be able to see the groups count and "Search Groups" filter in the header
    And the user should see the buttons download "CSV" and "Import Groups"

  @LQ-140071
  Scenario: Verify for Parent group kebab menu is not present
    When user clicks on parent group
    Then kebab menu should not be present for Parent group

  @LQ-140093
  Scenario: Verify when user tap on group + icon is displayed
    When user tap on first group
    Then plus "+" icon should be displayed

  Scenario: Verify add group - Add screen is displayed and create button remains disabled when group name is empty
    When user clicks on Add group "+" icon
    Then add group pop-up should be displayed with "Group name", "Group path" and "Description"
    And create button should be disabled with empty fields

    # Commenting as per UI changes. Scripts need to be updated.
#  Scenario: Verify Add Group by entering all required fields
#    When user fills all required fields in add group pop-up "Group name" and "Description"
#    Then new group should be created and pop-up message should appear, group name and description is present in the group container
#
  Scenario: Verify that creating an already existing group shows an appropriate error message - Negative
    When the user tries to add a group with an existing "Group name"
    Then an error message should appear indicating the group already exists

#  Scenario: Verify Kebab menu button
#    When user clicks on the kebab for one group "Automation_Group1"
#    Then "Edit", "Move" and "Delete" options will be displayed

#  @LQ-140100
#  Scenario: Verify edit group pop-up is displayed and save changes button is disabled
#    When user clicks on edit option
#    Then edit group pop-up should be displayed with "Group Name", "Group Path", "Subgroups" and "description"
#    And group name should be a required field
#    And save changes button is disabled

  Scenario: Verify edit group Cancel button
    When user clicks on cancel button
    Then edit group pop up should disappear

  Scenario: Verify editing the group name save changes button is enabled
    Given user clicks on the kebab for one group "Automation_Group1"
    When user clicks on edit option
    And user modifies group name and description
    Then the save changes button is enabled

  Scenario: Verify user can edit group and save successfully
    When user clicks save changes button
    Then group name and description should be changed for the same group

  Scenario: Edit group name with an existing name and get a validation error
    Given create a new group under parent group
    When user clicks on the kebab for one group "Automation_Group2"
    And user notes down sibling group name
    And user clicks on edit option
    And rename the group as same as sibling group
    Then group name should not be changed, there should be an error "Error! Group already exists with same Name and ParentId."

#  @LQ-141011
#  Scenario: Verify delete button from - kebab menu
#    When user clicks on the kebab for one group "Automation_Group2"
#    And user clicks on delete option from kebab
#    Then delete group confirmation pop-up should be displayed with "Cancel" and "Delete"

#  Scenario: Verify delete group Cancel button
#    When user clicks on cancel button
#    Then delete-group pop up should be disappear

#  Scenario: Verify delete group Delete button - Kebab menu
#    Given user clicks on the kebab for one group "Automation_Group2"
#    When user clicks on delete option from kebab
#    And user deletes the group
#    Then group should be deleted
#
#  Scenario: Verify "Delete" group when there are sub groups
#    Given user creates child group with name "Child_Automation_Group1" and description "Child_Automation_Group1_description"
#    When user clicks on the kebab for one group "Auto_modified_group"
#    And user clicks on delete option from kebab
#    And user deletes the group
#    Then cannot delete group pop up should be displayed and "All subgroups within the group must be moved or deleted prior to group deletion", "Close" button is displayed
#
#  Scenario: Verify close button in Delete group pop up
#    When user clicks on close button
#    Then group should not be deleted
#
#  Scenario: Verify Delete parent group after deleting child group
#    When delete child group "Child_Automation_Group1"
#    Then child group "Child_Automation_Group1" should be deleted
#
#  Scenario: Verify delete button from edit screen
#    When user clicks on the kebab for one group "Auto_modified_group"
#    And user clicks on edit option
#    And click delete from edit group pop_up
#    Then delete group confirmation pop-up should be displayed with "Cancel" and "Delete"
#
#  Scenario: Verify Cancel button functionality in the Delete Group pop-up on the Edit page
#    When user clicks on cancel button in delete pop up
#    Then delete-group pop up should be disappear

#  Scenario: Verify Delete Group functionality on the Edit page
#    When user deletes the group from edit page
#    Then group should be deleted

  @LQ-141023
  Scenario: Verify search functionality with invalid group name
    When user enters group name in search box "invalid_group"
    Then drop down should not be present

  Scenario: Verify search functionality with valid group name
    When user enters group name in search box
    Then drop down should be present

#  Scenario: Verify search group - Focus searched group
#    When user clicks group name from suggestion
#    Then same group should be focused

  @LQ-141033
  Scenario: Verify subgroups are displayed on group click
    When user tap on "The Doughnut Peddler, LLC- Main" group
    Then subgroups are displayed

  Scenario: Verify breadcrumb is updated after group is expanded
    When the user clicks on child group "Distribution Centers"
    Then the breadcrumb should display with opened group names

  @LQ-TBD
  Scenario: Verify that the Group Audit log tab is displayed
    Given the "Administrator/FA" user is in Group Page
    When the user clicks on the "View Change History" in Group Management page
    Then the user should be able to see the table columns: "GROUP AFFECTED", "ACTION", "ACTION DETAILS","EDITOR", "ACTION DATE" and page header "Group Audit Log"
    And The user should be see the filters ‘Search Group Affected’, Date filter and ‘Select Action(s)’ in the header, and the ‘Download Log’ button

  @LQ-TBD
  Scenario: Verify search functionality using a valid Group
    When the user enters a valid Group in "Search Group Affected"
    Then the system should display only matching logs

  Scenario: Verify search functionality with no matching group
    When the user enters an invalid group number in "Search Group Affected"
    Then the system should show no results message

  Scenario: Verify closing the Group Audit Log tab
    When the user clicks on the "Close" button
    Then the group Audit Log tab should be closed successfully

  @LQ-TBD
  Scenario: Verify filtering functionality with Edited action
    Given user clicks on "View Change History" in Group Management page
    When the user selects the Action "Edited" from the "Select Action(s)" filter dropdown
    Then the Group Audit Log should display logs with the Action type as "Edited"

  @LQ-TBD
  Scenario: Verify successfully Download the audit logs in the CSV format
    When the user clicks "Download Log" in the Group audit log tab
    Then the Group audit log is downloaded successfully

  Scenario: Verify the "Download Log" functionality is disabled when there is no audit log data
    When search an invalid group in "Search group Affected" filter
    Then the "Download Log" button is disabled in group Audit Log

  @CIPHER-3786
  Scenario: Verify Groups permission for full access user + Safety Manager role
    Given admin user logs in with FA/SM user
    When user navigates to Groups management page
    Then user should be able to view Groups belongs to Full access user only