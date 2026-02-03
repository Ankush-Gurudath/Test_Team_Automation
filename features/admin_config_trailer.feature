Feature: Admin - Configuration Settings & Trailer Management

  @LQ-242
  Scenario: Admin - Configuration Settings & Trailer Management
  # Scenario: Tier list is shown in config setting page
    Given Administrator user is in Admin
    When the user clicks CONFIG SETTING
#    Then Full access role is in tier 1 by default

#  @LQ-244
#  Scenario: Add new Tier on the Config setting page
#    When the user click the "Add New Tier" button & the user selects some roles & the user clicks "Confirm" on the popup
#    Then the selected roles are listed under the newly added tier
#
#  @LQ-5557
#  Scenario: Edit tier on the Config setting page
#    When the user clicks "Edit Tier" icon for tier 1 & the user checks some roles & the user clicks "Confirm" on the popup
#    Then the checked roles are updated
#
#  Scenario: Delete tier on the Config setting page
#    When the user clicks on the "Delete Tier" button & the user clicks "Confirm" button on the popup
#    Then the tier is deleted


  @LQ-101422
  Scenario: To verify the Workflow page in the Coaching Workflows tab under Config.Setting in Admin application.
    When the user clicks the "Coaching Workflows" tab
    Then the user should be able to see the page with the header "Workflows" and all the available workflows listed below.
    Then the user should be able to see a button "Create Workflow" filled with blue color in the right top corner.


  @LQ-101424
  Scenario: To verify the Icons present for the Workflows in the Workflows page
#    When the user navigated to the "Workflows" page    (When part is covered in LQ-101422)
    Then the user should be able to see all the workflows with the "Groups", "Duplicate", "Edit", "Delete", "Download" present straight to it in hyperlink format.

#  @LQ-106871
#  Scenario: To verify the groups selection in the Workflows page
#    When the user sets group filter to one group on the coaching workflow page
#    Then the workflows belong to the group are listed


  @LQ-101427
  Scenario: To verify the "Create Workflow" button present in the Workflows page
    When the user clicks the "Create Workflow" button.
    Then the user should see "Create Workflow" page coming from the bottom.


  @LQ-103680
  Scenario: create a new workflow
    When the user clicks the "Create Workflow" button & enters the workflow name
    And the user selects the the behaviour, coaching status from the dropdowns and the user gives a custom score & the user clicks on save button
    Then new coaching workflow is created


  @LQ-104058
  Scenario: To verify the download workflow button present in the Workflows page
  When the user clicks the download button of any workflow
  Then the user should see the workflow downloaded in the CSV Format "YYYY-MM-DD_Events_Workflow_Workflow name.csv"

  @LQ-104000
  Scenario: To verify the edit workflow button present in the Workflows page
    When the user clicks the edit button
    Then the user should see "Edit Workflow" page coming from the bottom


  @LQ-104043
  Scenario: To verify the Cancel functionality in the Edit Workflow page
  When the user clicks the "Cancel" button without doing any changes
  Then the user should be redirected to the Workflows page without any pop-up message.


#  @LQ-105094
#  Scenario: To verify the delete icon present in Edit Workflow page in the Workflows page
#  When the user is on edit workflow page
#  Then the user should be able to see the workflow rules of the workflow and the user should be able to see delete icon present at the end of every rule of the workflow.


#  @LQ-104032
#  Scenario: To verify the Save functionality in the Edit Workflow page
#    When the user edit behavior, or Coaching status or custom score
#    Then the user should able save the changes
#    Then user should be navigated to the Workflows page with the success pop-up message "Sucessfully updated the workflow"

#  @LQ-105045
#  Scenario: To verify the duplicate button present in the Workflows page
#    When the user clicks the Duplicate icon of any workflow which is present next to Groups icon.
#    Then the user should be navigated to "Create Worflow" page with the respective rules of the selected workflow
#    Then the user inputs a unique workflow name and the user should be able to change any behaviors,coaching status or custom score.
#    Then the user should be able to add new rule using "+Add" button and the user clicks "Save" button.
#    Then the user should be redirected to Workflows page and see the created workflow with the respective rules.

#  @LQ-103684
#  Scenario: To verify the delete workflow functionality in the Coaching Workflows tab under Config.Setting in Admin application.
#    When the user clicks the delete icon present straight to the workflow name.
#    Then the user should be able to see a success pop-up message "Workflows deleted successfully".
#    Then the user should not be able see the delete workflow in the Workflows page.


  @LQ-12128
  Scenario: The Trailer Management page is displayed
    When the user clicks the "TRAILER" tab
    Then the page header "TRAILER MANAGEMENT" is displayed and the table is displayed with columns: "TRAILER", "GROUP", "LICENSE PLATE", "VIN", "INSPECTION LIST"
    When the user enters some characters into "Search Trailer" field on the Trailer Management page
    Then the Trailers that contained the inputted characters are shown

  @LQ-12159
  Scenario: Add trailer on the Trailer Management page
    When the user clicks on "Add Trailer" & the user enters required fields: "Group" and "Trailer Name" & the user enters required fields: "Group" and "Trailer Name"
    Then the Trailer is added

  @LQ-17331
  Scenario: Edit trailer on the Trailer Management page
    When the user clicks on the name of a trailer & the user changes "Trailer Name" on Edit Trailer page & the user sets one group & the user clicks "Save Changes"
    Then the First Name of the edited trailer is updated