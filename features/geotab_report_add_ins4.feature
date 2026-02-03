Feature: Geotab Report Add-Ins Suite

  @LQ-108840
  Scenario: Login as multi-company user to newui lytx+geotab fleet telematics tab
    Given the login page is displayed in the browser
    When the multi-company user enters username/password, clicks the login button in the page and select company from the list
    Then the user is successfully logged into the Driver Safety dashboard

  @LQ-108840
  Scenario: Fleet Telematics tab
    When the user clicks Fleet Telematics tab
    Then the Fleet Telematics main page is loaded successfully

  @LQ-173162
  Scenario Outline: <report_name> - Validate user can upload geotab report add-in and send email for multiuser, driver user, full access user and fleet telematics manager user
    When the user clicks upload file, configure <report_name> and send email
    Then the user should be able to see the saved <report_name> in dashboard
   # Dividing in different sets because upload-media in yml supports only upto 5 media-ids at a time
    Examples:
      | report_name                     |
#      | DriverAvailability      |
#      | DriversApproachingLimit   |
#      | DriversONDutyinGeotabDrive    |
#      | EgregiousHOSViolationsCost     |
#      | EVChargingCostReport  |

#     | Odometer_Jump_Report |
#      | OFF_Duty_to_Drive_Instances      |
#      | Small_Fleet_Driver_Payroll_v20211101     |
#      | Telematics_Fault_Detection_Previous_7_days   |
#      | Unplug_Report_Marketplace   |
#
#      | ELD_Advanced_HOS_Logs_Email_or_Report_View   |
#      | ELD_Diagnostics_Malfunctions   |
#      | ELD_Driver_Violations_Alert   |
#      | ELD_HOS_Violations   |
#      | ELD_Unverified_Logs_Template   |
#
      | Excessive_PC                    |
#      | Excessive_YM                    |
#      | Fuel_Tax_Distance_Records_IFTA  |
#      | IFTA_Troubleshooting_Report_NEW |

# Below are xlsm reports. To be run locally as they arent supported in BrowserStack currently.
#  Scenario Outline: <report_name> - Validate user can upload geotab report add-in and send email for multiuser, driver user, full access user and fleet telematics manager user
#    When the user clicks upload file, configure <report_name> and send email
#    Then the user should be able to see the saved <report_name> in dashboard
#    Examples:
#      | report_name       |
#      | CO2_Emissions_Report      |
#      | Dynamic_Sending_Maintenance_Reminder   |
#        | Engine_Light_Percentage                |
#      | Fleet_Breakdown_by_Make  |
#      | Global_Fleet_Savings_Summary_Report_V9   |
#      | Last_3_Months_Fuel_Trend   |
#      | Last_3_Months_Idling_Trend   |
#      | Last_3_Months_Mileage_Trend   |

#      | Exception_Details_with_Trips_History     |
#      | PUBAverage_Fuel_Economy_KML   |
#      | Watchdog_Report_by_Minute   |
#      | Weekly_Idle_Cost_Daily_Trend_Gal   |
#      | Weekly_Idle_Cost_Daily_Trend_Litres   |

#  @LQ-
#  Scenario: Remove reports that are created by automation tests
#    When the user search by test_automation, preview it and click on remove button
#    Then the user should not see the reports with test_automation in dashboard