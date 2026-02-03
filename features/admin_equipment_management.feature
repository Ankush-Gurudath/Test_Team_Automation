Feature: Admin - Equipment Management

  @LQ-7126
  Scenario: Admin - Equipment Suite
  #Scenario: Admin - Equipment - The Equipment Management page is displayed
    Given the "Program Manager" user is in Admin
    When the user clicks the "EQUIPMENT" tab
    Then the page header "EQUIPMENT MANAGEMENT" is displayed and the table is displayed with columns: "EQUIPMENT", "DEVICE", "GROUP", "LAST CONNECTED", "STATUS"

  @LQ-7125
  Scenario: Add equipment on the Equipment Management page
    When the user clicks on "Add Equipment" and the user enters required fields: "Group" and "Equipment Name" and the user clicks "Create Equipment"
    Then the equipment is added

  @LQ-7127
  Scenario: Edit equipment on the Equipment Management page
    When the user clicks a created equipment, modifies required fields: “Group” and “Equipment Name”, and clicks “Save”
    Then the equipment is modified and saved

  @LQ-7136
  Scenario: Able to change device status to In Service successfully
    When the user selects a created equipment, selects “Change Status” button, clicks the "Select Status" dropdown button, selects "In Service", and clicks "Apply" button
    Then the selected equipment is changed to "In Service" status

  Scenario: Able to change device status to Out of Service successfully
    When the user selects a created equipment, selects “Change Status” button, clicks the "Select Status" dropdown button, selects "Out of Service", and clicks "Apply" button
    Then the selected equipment is changed to "Out of Service" status

  Scenario: Able to change device status to Spare successfully
    When the user selects a created equipment, selects “Change Status” button, clicks the "Select Status" dropdown button, selects "Spare", and clicks "Apply" button
    Then the searched equipment will be displayed on the page and has status Spare

  @LQ-7129
  Scenario: Filter equipment by selected group
    When the user clicks the filter “Select Group(s)” and the user selects groups
    Then the equipment list will be updated by the selected group and Equipment column values should be in ascending order

  @LQ-7130
  Scenario: Filter equipment by "In Service"
    When the user clicks the filter Status and the user selects "In Service"
    Then the equipment list will be updated by the "In Service" and Equipment column values should be in ascending order

  Scenario: Filter equipment by "Out of Service"
    When the user clicks the filter Status and the user selects "Out of Service"
    Then the equipment list will be updated by the "Out of Service" and Equipment column values should be in ascending order

  Scenario: Filter equipment by "Spare"
    When the user clicks the filter Status and the user selects "Spare"
    Then the equipment list will be updated by the "Spare" and Equipment column values should be in ascending order

  @LQ-7133
  Scenario: Filter equipment by last connected date
    When the user clicks the filter "Last Connected" and the user selects date range and the user clicks Apply button
    Then the equipment list will be updated by the selected last connected date

  @LQ-7132
  Scenario: Able to move equipment successfully
    When the user selects a created equipment and the user selects “Move Group” and the user selects a group and the user clicks Done on pop up window and the user clicks Continue button
    Then the equipment group is moved to the selected group

  @LQ-7682
  Scenario: Delete equipment on the Equipment Management page
    When the user checks some available equipment and the user clicks "Delete Equipment" and the user clicks "Confirm"
    Then the selected equipment are deleted

#  @LQ-7131
# Scenario: Able to detach device successfully
#    Given the "Program Manager" user is in the Equipment Management page
#    When the user selects a device that is bound to an equipment and the user selects “Detach Device” and the user clicks the Apply button
#    Then the "Success - x Equipment detached from the device" confirmation popup should come and the equipment is in Out of Service status and the device is not bound to this equipment
