Feature: Geotab Page Add-Ins Tests

  @LQ-108840
  Scenario: Login as multi-company user to newui lytx+geotab
    Given the login page is displayed in the browser
    When the multi-company user enters username/password, clicks the login button in the page and select company from the list
    Then the user is successfully logged into the Driver Safety dashboard


  Scenario: Verify Fleet Telematics tab
    When the user clicks Fleet Telematics tab
    Then the Fleet Telematics main page is loaded successfully

# Below 2 tests should be enabled when there's no test data in fleet settings page
#  @LQ-173162
#  Scenario: Verify Fleet Settings page
#    When the user clicks config menu > Fleet Settings sub-menu
#    Then the Fleet Settings page is loaded successfully
#
#
#  Scenario Outline: "<addin_name>" - Validate user can add geotab page add-in config file in lytx+geotab new UI
#    When the user clicks Config menu > Fleet Settings sub-menu and add the config "<addin_name>" in the configuration tab
#    Then the user should be able to add the config
#    Examples:
#      | addin_name              |
#      | fbt                     |
#      | eld support             |
#      | compliance data summary |
#      | eld settings validator  |
#      | evsa                    |
#      | import hos logs         |
#      | hos driver summary      |

# All addins may not be present all the time due to changing test data, hence commenting the test
  @LQ-173162
  Scenario: Verify if all added configs are present in AddIns menu(left panel) of New UI
    When the user click on AddIns menu
#    Then the AddIns menu is displayed with all the configured addins in left panel

# All addins may not be present all the time due to changing test data, hence commenting the test
  Scenario Outline: "<addin_name>" - Verify if page add-ins loads fine in New UI center page
    When the user click on "<addin_name>" config in the AddIns menu
    Then "<addin_name>" page loads fine
    Examples:
      | addin_name             |
#      | fbt                    |
#      | eld info config        |
      | eld settings validator |
#      | evsa                   |
#      | import hos logs        |
#      | hos driver summary     |

  Scenario: Verify login to mygeotab UI as a full access user
    Given mygeotab login page is displayed in the browser
    When the fa user enters username and password
    Then the user logs into the geotab dashboard with header "Product Guide" and company logo mygeotab is displayed


  Scenario Outline: "<addin_name>" - Verify if page add-ins is present and loads fine in MyGeotab UI
    When user search and click on "<addin_name>" config in mygeotab dashboard
    Then "<addin_name>" page with header should load fine
    Examples:
      | addin_name             |
#      | fbt                       |
#      | eld support               |
      | eld settings validator |
#      | import hos logs           |
#      | hos driver summary        |
#      | ev suitability assessment |
#

#  Scenario: Compliance data summary - Verify page add-in in MyGeotab UI
#    When user search for compliance data summary in Map menu
#    Then compliance data summary should be present in Map menu
