Feature: Device Status

  @Device_status @LQ-230
  Scenario: Device Management Page is displayed
    Given Admin user logs in into Admin page
    When user navigates to Device Management page
    Then Device Management Page is displayed

  @Stg_devices @LQ-113260
  Scenario Outline:  New Image request from device in Device profile latest date for STG
    When the user search for <device> and clicks the device
    And user clicks the Request New image for <device>
    Then a new image should be displayed in the UI
    Examples:
      | device   |
      |QM40008310|
      |QM40895252|

  @Int_devices @LQ-113260
  Scenario Outline:  New Image request from device in Device profile latest date for INT
    When the user search for <device> and clicks the device
    And user clicks the Request New image for <device>
    Then a new image should be displayed in the UI
    Examples:
      | device   |
      |QM40008297|
      |QM40008302|

  @Prod_devices @LQ-113260
  Scenario Outline:  New Image request from device in Device profile latest date for PROD
    When the user search for <device> and clicks the device
    And user clicks the Request New image for <device>
    Then a new image should be displayed in the UI
    Examples:
      | device   |
      |QM40008292|