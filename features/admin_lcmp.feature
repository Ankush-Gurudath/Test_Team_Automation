Feature: Admin - LCMP

  @LQ-253
  Scenario: Add user on the User Management page
    Given admin user logs in
    When the user clicks on "Add User" & the user enters required fields: "First Name", "Last Name", "EmployeeID", "Email", "Cell Phone", "Group" and "Role" on the "Info" tab & the user clicks "Create User"
    Then the user is added

  @LQ-152866
  Scenario: To verify the driver roles can see "Request user consent" tab in more option.
  When the user clicks driver name the "More Options" tab
  Then the user should see the "Request user consent" tab available

  Scenario: To verify the driver roles can see "Request user consent" tab in Admin application.
    When the user clicks "Request user consent" tab
    Then the user should see the tab opens from bottom with title "Request User Consent"

  @LQ-152962
  Scenario: User selects the system and communication mode
  When the user checks the "Facial ID" system and the user selects the "Email" communication mode and the user clicks the next button
  Then the user should see the "Confirm Request" modal getting opened.

  @LQ-153001
  Scenario: To verify the user is able to send the consent
  When the user click the "Send Request" button in the "Confirm Request" modal
  Then the user should see the success message "User consent request sent successfully" and the user should be redirected to User Management page.

  @LQ-136386
  Scenario: Verify the sub-menu "Consent Report" sub-menu under "Insights" menu.
    When the user click on the "Consent Report" module
    Then the user should see all the filter like "All Available Groups", "Status", "Search Name or ID" and "Reset"
    And the user should see the count of Drivers with tabs named "Facial ID", "Video Safety" and "Distraction and Fatigue Detection"

  @LQ-157939
  Scenario: To verify the elements and columns present in the Consent Report page.
#    When the user is in "Facial ID" product tab   # This step is commented because by default Facial ID tab is selected
    Then the user should see the title "Consent Report" and the user should see the columns "NAME","GROUPS","STATUS", "SENT DATE" and "REQUESTED DATE"
    And the user see the options "0 selected","Clear All","Download PDF", "Revoke Consent" and "CSV"

  @LQ-157911
  Scenario: To verify the group filters in the Consent Report Page
    When the user selects any group
    Then the user should be able to see the selected group data

  Scenario: To verify the newly sent consent user is present
    When the user search the username in the search filter
    Then the user should be able to see the newly sent consent user in the Consent Report page with employee ID

  Scenario: To verify the Status filters in the Consent Report Page
   When the user clicks "Status" the dropdown
   Then the user should see four statuses options "Not Received","Revoked","Received" and "Opted Out"

  Scenario: To verify the not received status filters in the Consent Report Page
    When the user clicks "Status" the dropdown and the user selects "Not Received" status
    Then the user should be able to see the data for the selected not received status

  Scenario: To verify the received status filters in the Consent Report Page
    When the user clicks "Status" the dropdown and the user selects "Received" status
    Then the user should be able to see the data for the selected received status

  Scenario: To verify the revoked status filters in the Consent Report Page
    When the user clicks "Status" the dropdown and the user selects "Revoked" status
    Then the user should be able to see the data for the selected revoked status

  Scenario: To verify the opted out status filters in the Consent Report Page
    When the user clicks "Status" the dropdown and the user selects "Opted Out" status
    Then the user should be able to see the data for the selected opted out status

  Scenario: To verify the "Search Name or ID" filter for first page in the Consent Report Page
    When the user inputs driver name from first page in the "Search Name or ID" field
    Then the user should be able to see the data related to the provided name or ID

#  @PHNX-4627 - commenting because the bug is still open in STG
#  Scenario: To verify the "Search Name or ID" filter for last page in the Consent Report Page
#    When the user inputs driver name from last page in the "Search Name or ID" field
#    Then the user should be able to see the data related to the provided name

 @PHNX-5485
  Scenario: To get the driver count in enable product page with selected group
    When the user navigates to Enable Product page and select a group in the group filter
    Then the user get the driver count of selected group

  @LQ-161688
  Scenario: To verify the download CSV in the Consent Report page
    When the user clicks the CSV button
    Then the user should see the excel getting downloaded in the format (YYYY-MM-DD_Productname_Consent_Status_Report.csv)

  @LQ-161373
  Scenario: Verify the download PDF of Consent Report page.
  When the user clicks the "PDF" with download icon available for "Revoked" and "Received" status
  Then the user should see the PDF getting downloaded in a format (ConsentID.pdf)

  @LQ-258
  Scenario: Delete users on the User Management page
    When the user checks some available users & the user clicks "Delete Users" & the user clicks "Confirm"
    Then the status of selected users is updated to deleted

  Scenario: Verify the removed employee id in the user page is not displayed in consent report page
    When the user search the username in the search filter after deleting the user
    Then the user should not see the removed employee id next to username in the Consent Report page

  @PHNX-5485
  Scenario: To verify the inactive user is not displayed in Enable Product page
    When the user navigates to Enable Product page from User Management page
    Then the user count should be less for the selected group based on inactive the user
