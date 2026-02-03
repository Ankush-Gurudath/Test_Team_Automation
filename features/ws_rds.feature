Feature: RiskCompany

  @LQ-373
  Scenario: RDS Tests
   #Scenario: View Dashboard page of RDS company
    Given the welcome login page is displayed
    When the user login WS for a risk company
    Then the Dashboard page is displayed and the Dashboard page includes "Drivers by Highest Score","Categories by Highest Frequency" and And the Dashboard page includes a driver counts, Group filter, Date filter

  @LQ-375
  Scenario: Link in Dashboard page of RDS company
    When the user clicks "View Details"
    Then the Driver Report page is opened

  @LQ-376
  Scenario: Filter group in Dashboard page
    Given the "Safety Manager" user is on Dashboard page of company A & the dcops key "DC_EnableCoaching" is false of company A
    When the user sets group filter to one group in dashboard page
    Then the data belong to the selected group are displayed in dashboard page

  Scenario: Filter date in Dashboard
    When the user sets date filter in dashboard page
    Then the data belong to the selected date range are displayed in dashboard page

  @LQ-378
  Scenario: View drivers report in RDS company
    When the user clicks "INSIGHTS" & the user clicks "DRIVERS REPORT"
    Then the drivers report page is opened & there are 3 tabs： "Drivers Scores","Continual Behaviors", "Alerts" & the table of "Driver Scores" is displayed

  @LQ-380
  Scenario: Filter categories in Driver Report
    When the user selects some categories
    Then the data belong to the selected categories are displayed