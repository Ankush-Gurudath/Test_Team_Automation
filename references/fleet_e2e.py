import datetime
import json
import random
import string
import unittest
import uuid

import requests
import xmlrunner

global testAutomationURL
global companyEndpoint
global groupOptionEndpoint
global vehicleEndpoint
global deviceEndpoint
global userEndpoint
global eventEndpoint
global fleetDataEndpoint
global bulkCleanupEndpoint


class F2FSetupCoachingTestCase(unittest.TestCase):
    testAutomationURL = "https://cloud-lytx-cloud-testautomation-datacomposer-dev.aws.drivecaminc.xyz/v1/"
    # testAutomationURL = "https://lytx-testautomation-datamanager.stg2.drivecaminc.xyz/"
    companyEndpoint: str = testAutomationURL + "companies"
    groupOptionEndpoint: str = testAutomationURL + "groupOption"
    vehicleEndpoint: str = testAutomationURL + "vehicles"
    deviceEndpoint: str = testAutomationURL + "devices"
    assetEndpoint: str = testAutomationURL + "assets"
    userEndpoint: str = testAutomationURL + "users"
    fleetDataEndpoint: str = testAutomationURL + "fleet"
    prevMaintenanceServiceEndpoint: str = testAutomationURL + "prev-maint/service"
    prevMaintenanceServiceVehicleInstanceEndpoint: str = testAutomationURL + \
                                                         "prev-maint/serviceVehicleInstance"
    messageSimulatorEndpoint: str = testAutomationURL + "message-simulator"
    geoFencesEndpoint: str = testAutomationURL + "geoFences"
    geoFencesActivationEndpoint: str = testAutomationURL + "geoFences/activation"
    bulkCleanupEndpoint: str = testAutomationURL + "cleanUpAll/"

    def test_fleet_setup(self):
        # Add Company
        headers = {'Content-Type': 'application/json'}
        companyPayload = "{}"
        response = requests.request(
            "POST", self.companyEndpoint, headers=headers, data=companyPayload)

        if response.status_code == requests.codes.created:
            companyResponse = json.loads(response.text)
            self.rootGroupId = companyResponse["rootGroupId"]
            self.correlationId = companyResponse["correlationId"]
            self.companyName = companyResponse["companyName"]
            self.companyId = companyResponse["companyId"]
            print(
                "Company with name " + self.companyName + " created with id: " + str(
                    self.companyId) + " created with rootGroupId: " + self.rootGroupId + " with correlationId: " + self.correlationId)
        else:
            print("Company creation failed: " + response.text)

        # Enable Fleet and Idle violations
        headers = {'Content-Type': 'application/json'}
        fleetPayload = {"rootGroupId": self.rootGroupId, "GroupOptions": {
            "39": "True", "82": "True", "107": "True", "42": "True", "251": "True", "264": "True"}}
        jsonFleetPayload = json.dumps(fleetPayload)
        response = requests.request(
            "POST", self.groupOptionEndpoint, headers=headers, data=jsonFleetPayload)

        if response.status_code == requests.codes.ok:
            print("Fleet and Idle violations enabled!")
        else:
            print("Unable to enable Fleet and Idle: " + response.text)

        # Add Vehicle
        headers = {'Content-Type': 'application/json'}
        vehiclePayload = {"groupId": self.rootGroupId,
                          "correlationId": self.correlationId}
        jsonVehiclePayload = json.dumps(vehiclePayload)
        response = requests.request(
            "POST", self.vehicleEndpoint, headers=headers, data=jsonVehiclePayload)

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
        response = requests.request(
            "POST", self.deviceEndpoint, headers=headers, data=jsonDevicePayload)

        if response.status_code == requests.codes.created:
            deviceResponse = json.loads(response.text)
            self.deviceId = deviceResponse["id"]
            print("Device created: " + self.deviceId)
        else:
            print("Device creation failed: " + response.text)

        # Add Asset
        headers = {'Content-Type': 'application/json'}
        assetName = str(uuid.uuid1())
        assetPayload = {
            "confirmed": "false",
            "GroupId": self.rootGroupId,
            "AssetName": assetName,
            "AssetStatusId": 1,
            "AssetTypeId": 1,
            "CompanyId": self.companyId,
            "ClientSecret": "dbda12b2-7579-42f4-aac6-e68f4d7aebba"
        }
        jsonAssetPayload = json.dumps(assetPayload)
        response = requests.request(
            "POST", self.assetEndpoint, headers=headers, data=jsonAssetPayload)

        if response.status_code == requests.codes.created:
            assetResponse = json.loads(response.text)
            self.assetId = assetResponse["assetId"]
            self.assetCorrelationId = assetResponse["correlationId"]
            print("Asset created: " + self.assetId)
        else:
            print("Asset creation failed: " + response.text)

        # Associate Device to Vehicle
        headers = {'Content-Type': 'application/json'}
        associationPayload = {"deviceId": self.deviceId, "groupId": self.rootGroupId, "vehicleId": self.vehicleId,
                              "correlationId": self.correlationId}
        jsonAssociationPayload = json.dumps(associationPayload)
        response = requests.request("POST", self.deviceEndpoint + "/association", headers=headers,
                                    data=jsonAssociationPayload)

        if response.status_code == requests.codes.ok:
            print("Device " + self.deviceId +
                  " successfully associated to Vehicle: " + self.vehicleId)
        else:
            print("Device association failed: " + response.text)

        # Add Fleet user
        headers = {'Content-Type': 'application/json'}
        userPayload = {
            "lastName": "readonly",
            "firstName": "fleet",
            "userRoles": [{
                "roleId": "38",
                "groupId": self.rootGroupId
            }],
            "rootGroupId": self.rootGroupId,
            "isLoginEnabled": "true",
            "email": "123@asd.co",
            "password": "Login123!",
            "correlationId": self.correlationId
        }
        jsonUserPayload = json.dumps(userPayload)
        response = requests.request(
            "POST", self.userEndpoint, headers=headers, data=jsonUserPayload)
        userResponse = json.loads(response.text)
        self.fleetId = userResponse["userName"]

        if response.status_code == requests.codes.created:
            print("Fleet user created: " + self.fleetId)
        else:
            print("Fleet user creation failed: " + response.text)

        # Create fleet data
        headers = {'Content-Type': 'application/json'}
        fleetPayload = {"vehicleId": self.vehicleId, "groupId": self.rootGroupId, "deviceId": self.deviceId,
                        "correlationId": self.correlationId}
        jsonFleetPayload = json.dumps(fleetPayload)
        response = requests.request(
            "POST", self.fleetDataEndpoint, headers=headers, data=jsonFleetPayload)
        jsonResponse = json.loads(response.text)
        # self.trackPointsResponse = jsonResponse["trackPointsResponse"]
        # self.idleViolationResponse = jsonResponse["idleViolationResponse"]
        # self.speedViolationResponse = jsonResponse["speedViolationResponse"]
        # self.gpsTripResponse = jsonResponse["gpsTripResponse"]
        # self.geoFenceResponse = jsonResponse["geoFenceResponse"]

        if response.status_code == requests.codes.created:
            print("Fleet data created")
            print(jsonResponse["trackPointsResponse"])
            print(jsonResponse["idleViolationResponse"])
            print(jsonResponse["speedViolationResponse"])
            print(jsonResponse["gpsTripResponse"])
            print(jsonResponse["geoFenceResponse"])

        else:
            print("Fleet data creation failed: " + response.text)

        # create preventive maintenance data
        # service creation
        headers = {'Content-Type': 'application/json'}
        serviceAdditionPayload = {
            "GroupId": self.rootGroupId,
            "Name": 'Testing' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10)),
            "CreationDate": "2023-04-05",
            "DeletionDate": None,
            "aRevision": 123,
            "aRevisionDate": "2023-03-20",
            "aUser": self.fleetId,
            "aHSUser": self.correlationId,
            "aMachine": "lytx",
            "DueSoonDays": 99998,
            "DueSoonHours": 999999,
            "DueSoonKm": 1000000,
            "IntervalDays": 99999,
            "IntervalHours": 9999999,
            "IntervalKm": 9999999
        }

        jsonServiceAdditionPayload = json.dumps(serviceAdditionPayload)
        response = requests.request(
            "POST", self.prevMaintenanceServiceEndpoint, headers=headers, data=jsonServiceAdditionPayload)
        if response.status_code == requests.codes.created:
            jsonResponse = json.loads(response.text)
            self.prevMaintServiceId = jsonResponse["serviceId"]
            print("PrevMaint ServiceId created: " + self.prevMaintServiceId)
        else:
            print("PrevMaint ServiceId creation failed: " + response.text)

        # create preventive maintenance data
        # service vehicle instance creation
        headers = {'Content-Type': 'application/json'}
        serviceAdditionPayload = {
            "ServiceId": self.prevMaintServiceId,
            "VehicleId": self.vehicleId,
            "DueAtKm": 10000504,
            "Notes": 'Testing' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=100)),
            "DueAtDate": "2024-05-30",
            "DueAtHours": 10001499,
            "HoursAtCompletion": 0,
            "UntilDueDays": 99999,
            "UntilDueHours": 9999999,
            "UntilDueKm": 9999999,
            "CreationDate": "2023-05-30",
            "aRevision": 0,
            "aRevisionDate": "2023-05-30",
            "aUser": self.fleetId,
            "aMachine": "lytx",
            "aHSUser": self.correlationId
        }

        jsonServiceVehicleInstancePayload = json.dumps(serviceAdditionPayload)
        response = requests.request(
            "POST", self.prevMaintenanceServiceVehicleInstanceEndpoint, headers=headers,
            data=jsonServiceVehicleInstancePayload)
        if response.status_code == requests.codes.created:
            jsonResponse = json.loads(response.text)
            self.prevMaintServiceVehicleInstanceId = jsonResponse["serviceVehicleInstanceId"]
            print("PrevMaint Service Vehicle Instance created: " + self.prevMaintServiceVehicleInstanceId)
        else:
            print("PrevMaint Service Vehicle Instance reation failed: " + response.text)

        # create message simulator data
        headers = {'Content-Type': 'application/json'}
        now = datetime.datetime.now()
        later = now + datetime.timedelta(0, 10000)
        messageSimulatorPayload = {
            "serialNumber": "MV00003342",
            "startTime": now.strftime('%Y-%m-%d %H:%M:%S'),
            "endTime": later.strftime('%Y-%m-%d %H:%M:%S'),
            "kafkaTopic": "LegacyGpsV2",
            "intervalBetweenTrackPointsInMs": 1000,
            "companyId": 1129,
            "stackId": 4,
            "eventRecorderId": "3500FFFF-6B4A-A1A7-D800-22CA712B0000",
            "groupId": "5100ffff-60b6-d5cd-8c47-22ca712b0000",
            "rootGroupId": "2BB2D9B4-C801-E111-81CE-E61F13277AAB",
            "vehicleId": self.vehicleId,
            "modelNumber": "ER-SF300"
        }
        jsonMessageSimulatorPayload = json.dumps(messageSimulatorPayload)
        response = requests.request("POST", self.messageSimulatorEndpoint, headers=headers,
                                    data=jsonMessageSimulatorPayload)
        if response.status_code == requests.codes.ok:
            print("Successfully added messages")
        else:
            print("Adding messages failed: " + response.text)

        # create geofence data
        headers = {'Content-Type': 'application/json'}
        geofencesPayload = {
            "DeviceId": self.deviceId,
            "VehicleId": self.vehicleId,
            "GroupId": self.rootGroupId
        }
        jsongeofencesPayload = json.dumps(geofencesPayload)
        response = requests.request("POST", self.geoFencesEndpoint, headers=headers, data=jsongeofencesPayload)
        if response.status_code == requests.codes.created:
            jsonResponse = json.loads(response.text)
            self.geoFenceId = jsonResponse["geoFenceId"]
            self.fenceRollupId = jsonResponse["fenceRollupId"]
            self.correlationId = jsonResponse["correlationId"]
            print("GeoFence created: " + self.geoFenceId)
        else:
            print("Adding GeoFence failed: " + response.text)

        # create geofence activation data
        headers = {'Content-Type': 'application/json'}
        geoFencesActivationPayload = {
            "DeviceId": self.deviceId,
            "VehicleId": self.vehicleId,
            "GroupId": self.rootGroupId,
            "GeoFenceId": self.geoFenceId,
            "FenceRollupId": self.fenceRollupId,
            "CorrelationId": self.correlationId,
        }
        jsongeoFencesActivationPayload = json.dumps(geoFencesActivationPayload)
        response = requests.request("POST", self.geoFencesActivationEndpoint, headers=headers,
                                    data=jsongeoFencesActivationPayload)
        if response.status_code == requests.codes.created:
            print("GeoFence activation created")
        else:
            print("Adding GeoFence activation failed: " + response.text)

        # Bulk Cleanup
        # headers = {'Content-Type': 'application/json'}
        # response = requests.request("DELETE", self.bulkCleanupEndpoint + self.correlationId, headers=headers)
        #
        # if response.status_code == requests.codes.ok:
        #     print("Bulk cleanup successful")
        # else:
        #     print("Bulk cleanup failed: " + response.text)


if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(
        output='C:/results'), failfast=False, catchbreak=False)
