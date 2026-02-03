Feature: Admin - Config Settings In-Cab MVAI

  @LQ-180649
  Scenario: Admin - Config Settings In-Cab MVAI Tab, Title and Description Verification
    Given the "Administrator" user is in the "Program Configuration" tab of "CONFIGURATION SETTINGS"
    When the user selects the "In-Cab MV+AI" tab
    Then the user should see a header "In-Cab MV+AI"
    And the description should be "These features are compatible with SF300 devices and newer"

  @LQ-180749
  Scenario: Verify "Smoking" section, description, and checkbox interactivity
    Then the user should see the section "Smoking" with description "Detection of driver smoking while the vehicle is in motion."

  @LQ-180750
  Scenario: Verify "Food and Drink" section, description, and checkbox interactivity
    Then the user should see the section "Food and Drink" with description "Detection of driver eating or drinking while the vehicle is in motion."

  @LQ-180751
  Scenario: Verify "Inattentive" section, description, and checkbox interactivity
    Then the user should see the section "Inattentive" with description "Detection of driver lacking sufficient focus on the road while the vehicle is in motion."

  @LQ-180752
  Scenario: Verify "Lens Obstruction" section, description, and checkbox interactivity
    Then the user should see the section "Lens Obstruction" with description "Detection of obstruction of the inside lens while the vehicle is in motion."

  @LQ-180753
  Scenario: Verify "Handheld Device" section, description, and checkbox interactivity
    Then the user should see the section "Handheld Device" with description "Detection of driver holding and/or actively using a handheld device while the vehicle is in motion."

  @LQ-180756
  Scenario: Verify "No Seatbelt" section, description, and checkbox interactivity
    Then the user should see the section "No Seatbelt" with description "Detection of driver not wearing or improperly wearing the seatbelt while the vehicle is in motion."

  @LQ-180749
  Scenario: Verify all feature headers section, description, and checkbox interactivity
    Then the user should see all the sections with three checkboxes: "Audio Alerts", "LED Alerts", "Events" and each checkbox should be clickable

  @PHNX-5447
  Scenario: Changing the program configuration settings in admin should save the changes
    When the user clicks the checkbox for Smoking and clicks on save changes
    Then the changes should be saved with a confirmation message "Changes saved successfully"
