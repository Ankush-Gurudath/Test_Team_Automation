Feature: Admin - Coaching Workflow

@LQ-136388
  Scenario: Admin - Configuration Settings & Trailer Management
    Given Administrator user is in Admin
    When the user clicks the "Coaching Workflows" tab

@LQ-136414 @LQ-101424
  Scenario: To verify the Workflow page in the Coaching Workflows tab under Config.Setting in Admin application.
    When the user clicks the "Coaching Workflows" tab
    Then the user should be able to see the page with the header "Workflows" and all the available workflows listed below.
    And the user should be able to see a button "Create Workflow" filled with blue color in the right top corner.
    And the user should see the count of Workflow and filters like "Select Group", "Search Workflow" and "Reset"
    And the user should be able to see all the workflows with the "Groups", "Duplicate", "Edit", "Delete", "Download" present straight to it in hyperlink format.

  @LQ-101427
  Scenario: To verify the "Create Workflow" button present in the Workflows page
    When the user clicks the "Create Workflow" button.
    Then the user should see "Create Workflow" page coming from the bottom.

  @LQ-161146
  Scenario: To verify the close button works in the Create Workflow modal
    When the user clicks the "X" icon present at the top right corner of the create Workflow modal
    Then the user should be redirected to the Workflows page.

  @LQ-103680
  Scenario: create a new workflow
    When the user clicks the "Create Workflow" button & enters the workflow name
    Then the user selects the the behaviour, coaching status from the dropdowns and the user gives a custom score & the user clicks on save button
    Then new coaching workflow is created

  @PHNX-4284
  Scenario: Verify user should not be able to create workflow with existing workflow name
    When the user clicks the "Create Workflow" button & enters the existing workflow name
    Then the user should be able to see an error message "Duplicate workflow name. Please enter a unique name."

  Scenario: select the group for newly created workflow
    When the user clicks on the "Groups" icon present next to the newly created workflow and select group and clicks on "Save" button
    Then the selected groups should be listed under the respective workflow.

  @LQ-104058
  Scenario: To verify the download workflow button present in the Workflows page
  When the user clicks the download button of any workflow
  Then the user should see the workflow downloaded in the CSV Format "YYYY-MM-DD_Events_Workflow_Workflow name.csv"

  @LQ-104000
  Scenario: To verify the edit workflow button present in the Workflows page
    When the user clicks the edit button
    Then the user should see "Edit Workflow" page coming from the bottom and a Description & Note text

  @LQ-104043
  Scenario: To verify the Cancel functionality in the Edit Workflow page
  When the user clicks the "Cancel" button without doing any changes
  Then the user should be redirected to the Workflows page without any pop-up message.

  @LQ-161146
  Scenario: To verify the close button works in the Edit Workflow modal
    When the user clicks the "X" icon present at the top right corner of the Edit Workflow modal
    Then the user should be redirected to the Workflows page.


  @LQ-104032
  Scenario: To verify the Save functionality in the Edit Workflow page
    When the user edit behavior, or Coaching status or custom score and remove the behaviour & coaching status
    Then the user should able save the changes
    Then user should be navigated to the Workflows page with the success pop-up message "Successfully updated the workflow"

  @LQ-105094
  Scenario: To verify the delete icon present in Edit Workflow page in the Workflows page
  When the user is on edit workflow page
  Then the user should be able to see the workflow rules of the workflow and the user should be able to see delete icon present at the end of every rule of the workflow.

  @PHNX-4284
  Scenario: Verify user should not be able to edit workflow with existing workflow name
    When the user clicks the "Edit Workflow" button & enters the existing workflow name
    Then the user should be able to see an error message "Duplicate workflow name. Please enter a unique name."

  Scenario: Verify user should not be able to duplicate workflow with existing workflow name
    When the user clicks the "Duplicate Workflow" button & enters the existing workflow name
    Then the user should be able to see an error message "Duplicate workflow name. Please enter a unique name."


  @LQ-105045
  Scenario: To verify the duplicate button present in the Workflows page
    When the user clicks the Duplicate icon of any workflow which is present next to Groups icon.
    Then the user should be navigated to "Create Workflow" page with the respective rules of the selected workflow
    Then the user inputs a unique workflow name and the user should be able to change any behaviors,coaching status or custom score.
    Then the user should be able to add new rule using "+Add" button and the user clicks "Save" button.
    Then the user should be redirected to Workflows page and see the created workflow with the respective rules.

  @LQ-103684
  Scenario: To verify the delete workflow functionality in the Coaching Workflows tab under Config.Setting in Admin application.
    When the user clicks the delete icon present straight to the workflow name.
    Then the user should be able to see a success pop-up message "Workflows deleted successfully".
    Then the user should not be able see the delete workflow in the Workflows page.

  @PHNX-4054
  Scenario: Verify the create workflow page should not load when behaviour score is set less than the default value
    When the user clicks the "Create Workflow" button & enters the workflow name
    Then the user selects the behaviour from the dropdown and sets the score less than the default value
    Then the user should be able to save the changes without any loading issue

