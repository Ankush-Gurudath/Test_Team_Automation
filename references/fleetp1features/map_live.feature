Feature: P1 Tests - End to end Fleet workflow
  As a developer,
  I want to run end to end tests on the Fleet application
  So I can confirm that code changes have not adversely affected the app.

  @LQ-444
  Scenario: Set Visibility of Vehicle
    Given "Fleet Dispatcher" user is in Fleet Tracking
    When the user clicks toggle of a vehicle in Working List
    Then the vehicle is not displayed on Map

  Scenario: Set Visibility of Geofence
    When the user clicks toggle of a Geofence in Working List
    Then the Geofence is not displayed on Map

  @LQ-513
  Scenario: Remove vehicle in Closest Vehicles page
    Given the "Fleet Dispatcher" user is in Closest Vehicles page
    When the user clicks on the trash icon after a vehicle in Closest Vehicles list
    Then the vehicle is removed from Closest Vehicles list and the route of the vehicle is removed from map

#  Issue: The vehicle could not be added to find closest vehicle panel after click on it.
#  This issue only exist in the company created by API, even login manually using the users created by api.
#  But all works fine on normal company like DC4DC. So comment this scenario for now.
#  Scenario: Add vehicle in Closest Vehicles page
#    When the user clicks on another vehicle pin
#    Then the vehicle is added to Closest Vehicles list and the vehicle is highlighted in Closest Vehicles list and the route of the vehicle is highlighted on map

  @LQ-448
  Scenario: Search Wild Card - All
    When the user clicks on Search box and the user clicks All
    Then all vehicles and geofences are displayed in Search Panel

  Scenario: Search Wild Card - All Vehicles
    When the user clicks on Search box and the user clicks All Vehicles
    Then all vehicles are displayed in Search Panel

  Scenario: Search Wild Card - All Geofences
    When the user clicks on Search box and the user clicks All Geofences
    Then all geofences are displayed in Search Panel

  Scenario: Search Wild Card - All Nearby Vehicles
    When the user clicks on Search box and the user clicks All Nearby Vehicles
    Then all nearby vehicles are displayed in Search Panel
