import json
import unittest

import requests

global testAutomationURL
global companyEndpoint
global vehicleEndpoint
global deviceEndpoint
global userEndpoint
global eventEndpoint


class F2FSetupCoachingTestCase(unittest.TestCase):
    testAutomationURL = "https://cloud-lytx-cloud-testautomation-datacomposer-dev.aws.drivecaminc.xyz/v1/"
    # testAutomationURL = "https://lytx-testautomation-datamanager.stg2.drivecaminc.xyz/"
    companyEndpoint: str = testAutomationURL + "companies"
    vehicleEndpoint: str = testAutomationURL + "vehicles"
    deviceEndpoint: str = testAutomationURL + "devices"
    userEndpoint: str = testAutomationURL + "users"
    eventEndpoint: str = testAutomationURL + "events"
    bulkCleanup: str = testAutomationURL + "cleanUpAll/"

    def test_coaching_setup(self):
        # Add Company
        headers = {'Content-Type': 'application/json'}
        companyPayload = "{}"
        response = requests.request("POST", self.companyEndpoint, headers=headers, data=companyPayload)

        if response.status_code == requests.codes.created:
            companyResponse = json.loads(response.text)
            self.rootGroupId = companyResponse["rootGroupId"]
            self.correlationId = companyResponse["correlationId"]
            self.companyName = companyResponse["companyName"]
            print(
                "Company " + self.companyName + " created: " + self.rootGroupId + " with correlationId: " + self.correlationId)
        else:
            print("Company creation failed: " + response.text)

        # Add Vehicle
        headers = {'Content-Type': 'application/json'}
        vehiclePayload = {"groupId": self.rootGroupId, "correlationId": self.correlationId}
        jsonVehiclePayload = json.dumps(vehiclePayload)
        response = requests.request("POST", self.vehicleEndpoint, headers=headers, data=jsonVehiclePayload)

        if response.status_code == requests.codes.created:
            vehicleResponse = json.loads(response.text)
            self.vehicleId = vehicleResponse["vehicleId"]
            print("Vehicle created: " + self.vehicleId)
        else:
            print("Vehicle creation failed: " + response.text)

        # Add Device
        headers = {'Content-Type': 'application/json'}
        devicePayload = {"correlationId": self.correlationId}
        jsonDevicePayload = json.dumps(devicePayload)
        response = requests.request("POST", self.deviceEndpoint, headers=headers, data=jsonDevicePayload)

        if response.status_code == requests.codes.created:
            deviceResponse = json.loads(response.text)
            self.deviceId = deviceResponse["id"]
            self.serialNumber = deviceResponse["serialNumber"]
            print("Device created: " + self.deviceId)
        else:
            print("Device creation failed: " + response.text)

        # Associate Device to Vehicle
        headers = {'Content-Type': 'application/json'}
        associationPayload = {"deviceId": self.deviceId, "groupId": self.rootGroupId, "vehicleId": self.vehicleId,
                              "correlationId": self.correlationId}
        jsonAssociationPayload = json.dumps(associationPayload)
        response = requests.request("POST", self.deviceEndpoint + "/association", headers=headers,
                                    data=jsonAssociationPayload)

        if response.status_code == requests.codes.ok:
            print("Device " + self.deviceId + " successfully associated to Vehicle: " + self.vehicleId)
        else:
            print("Device association failed: " + response.text)

        # Add Driver
        headers = {'Content-Type': 'application/json'}
        userPayload = {
            "lastName": "test",
            "firstName": "driver",
            "userRoles": [{
                "roleId": "38",
                "groupId": self.rootGroupId
            }, {
                "roleId": "4",
                "groupId": self.rootGroupId
            }],
            "rootGroupId": self.rootGroupId,
            "isLoginEnabled": "true",
            "email": "123@asd.co",
            "password": "Login123!",
            "correlationId": self.correlationId
        }
        jsonUserPayload = json.dumps(userPayload)
        response = requests.request("POST", self.userEndpoint, headers=headers, data=jsonUserPayload)
        driverResponse = json.loads(response.text)
        self.driverId = driverResponse["userName"]

        if response.status_code == requests.codes.created:
            print("Driver created: " + self.driverId)
        else:
            print("Driver creation failed: " + response.text)

        # Add Coach
        headers = {'Content-Type': 'application/json'}
        coachPayload = {
            "lastName": "user",
            "firstName": "coach",
            "userRoles": [{
                "roleId": "38",
                "groupId": self.rootGroupId
            }, {
                "roleId": "5",
                "groupId": self.rootGroupId
            }],
            "rootGroupId": self.rootGroupId,
            "isLoginEnabled": "true",
            "email": "123@asd.co",
            "password": "Login123!",
            "correlationId": self.correlationId
        }
        jsonCoachPayload = json.dumps(coachPayload)
        response = requests.request("POST", self.userEndpoint, headers=headers, data=jsonCoachPayload)
        driverResponse = json.loads(response.text)
        self.coachId = driverResponse["userName"]

        if response.status_code == requests.codes.created:
            print("Coach created: " + self.coachId)
        else:
            print("Coach creation failed: " + response.text)

        # Add Program Manager
        headers = {'Content-Type': 'application/json'}
        pm_payload = {
            "lastName": "manager",
            "firstName": "program",
            "userRoles": [{
                "roleId": "38",
                "groupId": self.rootGroupId
            }, {
                "roleId": "10",
                "groupId": self.rootGroupId
            }],
            "rootGroupId": self.rootGroupId,
            "isLoginEnabled": "true",
            "email": "123@asd.co",
            "password": "Login123!",
            "correlationId": self.correlationId
        }
        json_pm_payload = json.dumps(pm_payload)
        response = requests.request("POST", self.userEndpoint, headers=headers,
                                    data=json_pm_payload)
        pm_response = json.loads(response.text)
        self.pm_login = pm_response["userName"]

        if response.status_code == requests.codes.created:
            print("PM created: " + self.pm_login)
        else:
            print("PM creation failed: " + response.text)

        # Create event
        headers = {'Content-Type': 'application/json'}
        eventPayload = {"SerialNumber": self.serialNumber, "BehaviorName": "cellphone",
                        "correlationId": self.correlationId}
        jsonEventPayload = json.dumps(eventPayload)
        response = requests.request("POST", self.eventEndpoint, headers=headers, data=jsonEventPayload)
        eventResponse = json.loads(response.text)
        self.eventId = eventResponse["eventId"]

        if response.status_code == requests.codes.created:
            print("Event created: " + self.eventId)
        else:
            print("Event creation failed: " + response.text)

        # Update event
        headers = {'Content-Type': 'application/json'}
        updateEventPayload = {"EventStatus": "Collision", "TaskStatus": "Face-To-Face Coaching"}
        jsonUpdatedEventPayload = json.dumps(updateEventPayload)
        response = requests.request("PUT", self.eventEndpoint + "/status/" + self.eventId, headers=headers,
                                    data=jsonUpdatedEventPayload)

        #
        if response.status_code == requests.codes.ok:
            print("Event " + self.eventId + " was updated successfully")
        else:
            print("Event update failed: " + self.eventId + response.text)

        # # Bulk Cleanup
        # headers = {'Content-Type': 'application/json'}
        # response = requests.request("DELETE", self.bulkCleanup + self.correlationId, headers=headers)
        #
        # if response.status_code == requests.codes.ok:
        #     print("Bulk cleanup successful")
        # else:
        #     print("Bulk cleanup failed: " + response.text)

