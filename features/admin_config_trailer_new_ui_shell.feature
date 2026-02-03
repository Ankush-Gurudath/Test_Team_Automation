Feature: Admin - Configuration Settings & Trailer Management New-Ui-Shell

  @LQ-136388
  Scenario: Admin - Configuration Settings & Trailer Management
    Given Administrator user is in Admin
    When the user clicks CONFIG SETTING
    Then Full access role is in tier 1 by default with "Role","Description" and "Admin Permission"
    And the user should see the "Edit" icon for the first tier
#    And the user should see the both "Edit" and "Delete" icon   #this same step verified after adding second tier role

  @LQ-244
  Scenario: Add new Tier on the Config setting page
    When the user click the "Add New Tier" button & the user selects some roles & the user clicks "Confirm" on the popup
    Then the selected roles are listed under the newly added tier
    And the user should see the both "Edit" and "Delete" icon

  @LQ-5557
  Scenario: Edit tier on the Config setting page
    When the user clicks "Edit Tier" icon for tier 1 & the user checks some roles & the user clicks "Confirm" on the popup
    Then the checked roles are updated

  Scenario: Delete tier on the Config setting page
    When the user clicks on the "Delete Tier" button & the user clicks "Confirm" button on the popup
    Then the tier is deleted


#    Commenting test untill Program Configuration feature is enabled in the application
#  @LQ-136649
#  Scenario: Verify the "Program Configuration" tab under "Config.Settings" menu
#    When the user clicks the "Program Configuration" tab
#    Then the user should see the behavior "Critical Distance" and the alerts like "Audio Alerts","LED Alerts" and "Events"
#    And the user should see the behavior "Following Distance" and the alerts like "Audio Alerts","LED Alerts" and "Events"
#    And the user should see the behavior "Lane Departure" and the alerts like "Audio Alerts","LED Alerts" and "Events"
#    And the user should see the behavior "Rolling Stop" and the alerts like "Audio Alerts","LED Alerts" and "Events"

  @LQ-136648
  Scenario: Verify the "Action Plan" tab under "Config.Settings" menu
    When the user clicks the "Action Plan" tab
    Then the user should see the corrective action title and "Edit" button in Action Plan

  @CHIPER-4016
  Scenario: Add Corrective Action on the Action Plan page
    When the user clicks on "Add Corrective Action" & the user enters required fields: "Name" and "Description" & the user clicks "Save"
    Then the Corrective Action is added

  Scenario: Delete Corrective Action on the Action Plan page
    When the user clicks on "Delete" button for a corrective action & the user clicks "Confirm" on the popup
    Then the Corrective Action is deleted

  @LQ-136373
  Scenario: The Trailer Management page is displayed
    When the user clicks the "TRAILER" tab
    Then the page header "TRAILER MANAGEMENT" is displayed and the table is displayed with columns: "TRAILER", "GROUP", "LICENSE PLATE", "VIN", "INSPECTION LIST"
    And the user should see the filters like "Select Group(s)", "Search Trailer" and "Reset"
    And the user should see the Trailers count and "Add Trailers" button

  @LQ-12129
  Scenario: Filter group(s) on the Trailer Management page
    When the user sets group filter to one group on the Trailer Management page
    Then the Trailer belong to the group are listed

  Scenario: Select Trailer on the Trailer Management page
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
