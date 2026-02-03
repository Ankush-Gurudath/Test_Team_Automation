import json
import time
from datetime import datetime
from enum import Enum

import requests

import utils.property_reader_util as property
from data.int.fleet_insights_data_int import FleetInsightsDataInt as FID_INT
from data.int.ws_tasks_data_int import TaskDataInt as TD_INT
from data.prod.fleet_insights_data_prod import FleetInsightsDataProd as FID_PROD
from data.prod.ws_tasks_data_prod import TaskDataProd as TD_PROD
from data.stg.fleet_insights_data_stg import FleetInsightsDataStg as FID_STG
from data.stg.ws_tasks_data_stg import TaskDataStg as TD_STG

F2F_EVENT_ID_1ST = 0
F2F_EVENT_ID_2ND = 0
F2F_EVENT_ID_3RD = 0
F2F_EVENT_ID_4TH = 0
SELF_EVENT_ID_1ST = 0
COLLISION_EVENT_ID_1ST = 0
COLLISION_EVENT_ID_2ND = 0
COLLISION_EVENT_ID_3RD = 0
FYI_EVENT_ID_1ST = 0
FYI_EVENT_ID_2ND = 0
FYI_EVENT_ID_3RD = 0
FYI_EVENT_UUID_2ND = 0
FYI_EVENT_UUID_3RD = 0
POSSIBLE_COLLISION_EVENT_ID_1ST = 0
POSSIBLE_COLLISION_EVENT_ID_2ND = 0
DRIVER_ID = 0
TD = 0
FID = 0
VAULT_SECRETS = 0
AUTH_TOKEN = 0
access_token = ''

ENV = property.get_value('env')
API_URL = property.get_value('base_url_data_composer')
DC_URL = property.get_value('base_url_drivecam')
FLEET_URL = property.get_value('base_url_fleet')
WELCOME_URL = property.get_value('base_url_login')
SSO_URL = property.get_value('base_url_sso')
SSO_URL1 = property.get_value('base_url_sso1')
SSO_URL2 = property.get_value('base_url_sso2')
NEW_UI_FTM_URL = property.get_value('base_url_fleet_telematics')
GEOTAB_URL = property.get_value('base_url_geotab')
AUTH_URL = property.get_value('auth_url')
UPDATE_EVENT_BASE_URL = property.get_value('update_event_base_url')

if ENV == 'int':
    TD = TD_INT
    FID = FID_INT
elif ENV == 'stg':
    TD = TD_STG
    FID = FID_STG
elif ENV == 'prod':
    TD = TD_PROD
    FID = FID_PROD

# DRIVER_VEHICLE_SUMMARY_END_POINT: str = API_URL + "fleet-operations/driver-vehicle-summary"
# TRIP_DRIVER_PROFILE_END_POINT: str = API_URL + "trips/gps"
# IDLE_DRIVER_PROFILE_END_POINT: str = API_URL + "IdleViolations"
CLOUD_LYTX_CORE_VEHICLES_SERVICE_URL_STG = 'https://cloud-lytx-core-vehicles-service-stg.aws.drivecam.net'
BASE_URL_DEVICEPLATFORM_DEVICE_SIMULATOR_STG = 'https://cloud-lytx-deviceplatform-testing-simulator-stg.aws.drivecam.net'
BASE_URL_DEVICE_MESSAGE_SIMULATOR_STG = 'https://cloud-lytx-device-message-simulator-stg.aws.drivecam.net'
CREATE_DEVICES_ENDPOINT = BASE_URL_DEVICEPLATFORM_DEVICE_SIMULATOR_STG + '/devices'
CREATE_VEHICLE_ENDPOINT = CLOUD_LYTX_CORE_VEHICLES_SERVICE_URL_STG + '/vehicles'


class AutomationDataManager:
    def __init__(self):
        self.access_token = ""
        self.F2F_EVENT_ID = 0
        self.F2F_EVENT_ID_1ST = 0
        self.F2F_EVENT_ID_2ND = 0
        self.F2F_EVENT_ID_3RD = 0
        self.F2F_EVENT_ID_4TH = 0
        self.SELF_EVENT_ID_1ST = 0
        self.COLLISION_EVENT_ID_1ST = 0
        self.COLLISION_EVENT_ID_2ND = 0
        self.COLLISION_EVENT_ID_3RD = 0
        self.FYI_EVENT_ID_1ST = 0
        self.FYI_EVENT_ID_2ND = 0
        self.FYI_EVENT_ID_3RD = 0
        self.POSSIBLE_COLLISION_EVENT_ID_1ST = 0
        self.POSSIBLE_COLLISION_EVENT_ID_2ND = 0

        self.DRIVER_ID = 0

    def create_test_credentials(self, test_data_list):
        for i in test_data_list:
            self.create_data(i)

    def create_data(self, test_data_enum):
        global F2F_EVENT_ID_1ST, F2F_EVENT_ID_2ND, F2F_EVENT_ID_3RD, F2F_EVENT_ID_4TH, SELF_EVENT_ID_1ST, FYI_EVENT_ID_1ST, FYI_EVENT_ID_2ND, FYI_EVENT_ID_3RD, \
            COLLISION_EVENT_ID_1ST, COLLISION_EVENT_ID_2ND, COLLISION_EVENT_ID_3RD, POSSIBLE_COLLISION_EVENT_ID_1ST, POSSIBLE_COLLISION_EVENT_ID_2ND, FYI_EVENT_UUID_2ND, FYI_EVENT_UUID_3RD, AUTH_TOKEN, VAULT_SECRETS, access_token
        match test_data_enum:
            case TestDataEnum.AUTH_TOKEN:
                #     Get auth token from vault
                AUTH_TOKEN_URL = AUTH_URL + "connect/token"
                headers = {
                    'Content-Type': 'application/x-www-form-urlencoded',
                    'Authorization': 'Basic bHl0eDozMWIwOGZhOC1lOTRkLTQwZTgtYWU5Zi02NzQxN2UzODNmZTg='
                }
                event_payload = {
                    "grant_type": "password",
                    "scope": "email openid profile hbs offline_access",
                    "username": "AutoFullAccess88",
                    "password": "Login123!",
                    "acr_values": "tenant:4 co_id:8186"
                }
                response = requests.request("POST", AUTH_TOKEN_URL, headers=headers, data=event_payload)
                event_response = json.loads(response.text)
                access_token = event_response["access_token"]
                print("Auth Status code is " + str(response.status_code))
                self.access_token = access_token

            case TestDataEnum.VAULT_SECRETS:
                VAULT_SECRETS_URL = API_URL + "vault/secrets/db/safety/" + ENV
                headers = {
                    'Content-Type': 'application/json'
                }
                payload = json.dumps("")
                response = requests.request("POST", VAULT_SECRETS_URL, headers=headers, data=payload)
                print("Vaults response is:", response.status_code)

            case TestDataEnum.F2F_EVENT_1ST:
                # Create a new event then update to F2F
                url = API_URL + "event/create/backend"
                headers = {'Content-Type': 'application/json'}
                event_payload = json.dumps({
                    "groupId": "5100ffff-60b6-d5cd-be83-a8a3e03f0000",
                    "eventTriggerTypeId": 2004,
                    "triggerDateTimeUtc": "2025-10-18T17:12:44.882",
                    "preTriggerSeconds": 8,
                    "postTriggerSeconds": 4,
                    "serialNumber": "OV00075173",
                    "eventSourceId": 6,
                    "psvLatitude": 32.88716,
                    "psvLongitude": -117.211655,
                    "psvDeviceSpeedKph": 128,
                    "psvPostedSpeedKph": 104,
                    "deletedReasonId": 0,
                    "adasTriggerSourceId": 3,
                    "checkPrivacyMode": False,
                    "BehaviourName": "LensObstruction",
                    "CompanyId": 8186
                })
                response = requests.request("POST", url, headers=headers,
                                            data=event_payload)
                if response.status_code == requests.codes.ok:
                    print("Event created successfully")
                else:
                    print("Event creation failed: " + str(response.status_code))

                # get Event ID
                event_response = json.loads(response.text)
                F2F_EVENT_ID_1ST = event_response["customerEventIdString"]
                Event_ID = event_response["id"]
                if response.status_code == requests.codes.ok:
                    print(f"get Event ID {F2F_EVENT_ID_1ST}")
                else:
                    print("Get Event ID failed: ")

                # Update event to F2F
                time.sleep(5)
                Update_EVENT_URL = UPDATE_EVENT_BASE_URL + 'safetyevents/events/' + Event_ID + '/eventBehaviorReview'
                headers = {'Content-Type': 'application/json',
                           'Accept': 'application/json, text/plain, */*',
                           'Accept-Language': 'en-US,en;q=0.9,en-IN;q=0.8',
                           'Authorization': f"Bearer {access_token}",
                           'Cache-Control': 'no-cache',
                           'Connection': 'keep-alive',
                           'DNT': '1',
                           'Origin': 'https://drivecam-stg2.drivecam.com',
                           'Pragma': 'no-cache',
                           'Sec-Fetch-Dest': 'empty',
                           'Sec-Fetch-Mode': 'cors',
                           'Sec-Fetch-Site': 'cross-site',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
                           'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"macOS"'
                           }
                update_event_payload = json.dumps({
                    "eventId": Event_ID,
                    "behaviorEdits": [
                        {
                            "id": 58,
                            "behaviorId": 58,
                            "operation": "add",
                            "reasonId": 2
                        }
                    ]
                })
                response = requests.request("POST", Update_EVENT_URL, headers=headers, data=update_event_payload)
                if response.status_code == requests.codes.ok:
                    print("Event " + F2F_EVENT_ID_1ST + " was updated successfully")
                else:
                    print("Event update failed: " + response.text)
                self.F2F_EVENT_ID_1ST = F2F_EVENT_ID_1ST

            case TestDataEnum.F2F_EVENT_2ND:
                # Create a new event then update to F2F
                url = API_URL + "event/create/backend"
                headers = {'Content-Type': 'application/json'}
                event_payload = json.dumps({
                    "groupId": "5100ffff-60b6-d5cd-be83-a8a3e03f0000",
                    "eventTriggerTypeId": 2004,
                    "triggerDateTimeUtc": "2025-10-18T17:12:44.882",
                    "preTriggerSeconds": 8,
                    "postTriggerSeconds": 4,
                    "serialNumber": "OV00075173",
                    "eventSourceId": 6,
                    "psvLatitude": 32.88716,
                    "psvLongitude": -117.211655,
                    "psvDeviceSpeedKph": 128,
                    "psvPostedSpeedKph": 104,
                    "deletedReasonId": 0,
                    "adasTriggerSourceId": 3,
                    "checkPrivacyMode": False,
                    "BehaviourName": "LensObstruction",
                    "CompanyId": 8186
                })
                response = requests.request("POST", url, headers=headers,
                                            data=event_payload)
                if response.status_code == requests.codes.ok:
                    print("Event created successfully")
                else:
                    print("Event creation failed: " + str(response.status_code))

                # get Event ID
                event_response = json.loads(response.text)
                F2F_EVENT_ID_2ND = event_response["customerEventIdString"]
                Event_ID = event_response["id"]
                if response.status_code == requests.codes.ok:
                    print(f"get Event ID {F2F_EVENT_ID_2ND}")
                else:
                    print("Get Event ID failed: ")

                # Update event to F2F
                time.sleep(5)
                Update_EVENT_URL = UPDATE_EVENT_BASE_URL + 'safetyevents/events/' + Event_ID + '/eventBehaviorReview'
                headers = {'Content-Type': 'application/json',
                           'Accept': 'application/json, text/plain, */*',
                           'Accept-Language': 'en-US,en;q=0.9,en-IN;q=0.8',
                           'Authorization': f"Bearer {access_token}",
                           'Cache-Control': 'no-cache',
                           'Connection': 'keep-alive',
                           'DNT': '1',
                           'Origin': 'https://drivecam-stg2.drivecam.com',
                           'Pragma': 'no-cache',
                           'Sec-Fetch-Dest': 'empty',
                           'Sec-Fetch-Mode': 'cors',
                           'Sec-Fetch-Site': 'cross-site',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
                           'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"macOS"'
                           }
                update_event_payload = json.dumps({
                    "eventId": Event_ID,
                    "behaviorEdits": [
                        {
                            "id": 58,
                            "behaviorId": 58,
                            "operation": "add",
                            "reasonId": 2
                        }
                    ]
                })
                response = requests.request("POST", Update_EVENT_URL, headers=headers, data=update_event_payload)
                if response.status_code == requests.codes.ok:
                    print("Event " + F2F_EVENT_ID_2ND + " was updated successfully")
                else:
                    print("Event update failed: " + response.text)
                self.F2F_EVENT_ID_2ND = F2F_EVENT_ID_2ND

            case TestDataEnum.F2F_EVENT_3RD:
                # Create a new event then update to F2F
                url = API_URL + "event/create/backend"
                headers = {'Content-Type': 'application/json'}
                event_payload = json.dumps({
                    "groupId": "5100ffff-60b6-d5cd-be83-a8a3e03f0000",
                    "eventTriggerTypeId": 2004,
                    "triggerDateTimeUtc": "2025-10-18T17:12:44.882",
                    "preTriggerSeconds": 8,
                    "postTriggerSeconds": 4,
                    "serialNumber": "OV00075173",
                    "eventSourceId": 6,
                    "psvLatitude": 32.88716,
                    "psvLongitude": -117.211655,
                    "psvDeviceSpeedKph": 128,
                    "psvPostedSpeedKph": 104,
                    "deletedReasonId": 0,
                    "adasTriggerSourceId": 3,
                    "checkPrivacyMode": False,
                    "BehaviourName": "LensObstruction",
                    "CompanyId": 8186
                })
                response = requests.request("POST", url, headers=headers,
                                            data=event_payload)
                if response.status_code == requests.codes.ok:
                    print("Event created successfully")
                else:
                    print("Event creation failed: " + str(response.status_code))

                # get Event ID
                event_response = json.loads(response.text)
                F2F_EVENT_ID_3RD = event_response["customerEventIdString"]
                Event_ID = event_response["id"]
                if response.status_code == requests.codes.ok:
                    print(f"get Event ID {F2F_EVENT_ID_3RD}")
                else:
                    print("Get Event ID failed: ")

                # Update event to F2F
                time.sleep(5)
                Update_EVENT_URL = UPDATE_EVENT_BASE_URL + 'safetyevents/events/' + Event_ID + '/eventBehaviorReview'
                headers = {'Content-Type': 'application/json',
                           'Accept': 'application/json, text/plain, */*',
                           'Accept-Language': 'en-US,en;q=0.9,en-IN;q=0.8',
                           'Authorization': f"Bearer {access_token}",
                           'Cache-Control': 'no-cache',
                           'Connection': 'keep-alive',
                           'DNT': '1',
                           'Origin': 'https://drivecam-stg2.drivecam.com',
                           'Pragma': 'no-cache',
                           'Sec-Fetch-Dest': 'empty',
                           'Sec-Fetch-Mode': 'cors',
                           'Sec-Fetch-Site': 'cross-site',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
                           'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"macOS"'
                           }
                update_event_payload = json.dumps({
                    "eventId": Event_ID,
                    "behaviorEdits": [
                        {
                            "id": 58,
                            "behaviorId": 58,
                            "operation": "add",
                            "reasonId": 2
                        }
                    ]
                })
                response = requests.request("POST", Update_EVENT_URL, headers=headers, data=update_event_payload)
                if response.status_code == requests.codes.ok:
                    print("Event " + F2F_EVENT_ID_3RD + " was updated successfully")
                else:
                    print("Event update failed: " + response.text)
                self.F2F_EVENT_ID_3RD = F2F_EVENT_ID_3RD

            case TestDataEnum.F2F_EVENT_4TH:
                # Create a new event then update to F2F
                url = API_URL + "event/create/backend"
                headers = {'Content-Type': 'application/json'}
                event_payload = json.dumps({
                    "groupId": "5100ffff-60b6-d5cd-be83-a8a3e03f0000",
                    "eventTriggerTypeId": 2004,
                    "triggerDateTimeUtc": "2025-10-18T17:12:44.882",
                    "preTriggerSeconds": 8,
                    "postTriggerSeconds": 4,
                    "serialNumber": "OV00075173",
                    "eventSourceId": 6,
                    "psvLatitude": 32.88716,
                    "psvLongitude": -117.211655,
                    "psvDeviceSpeedKph": 128,
                    "psvPostedSpeedKph": 104,
                    "deletedReasonId": 0,
                    "adasTriggerSourceId": 3,
                    "checkPrivacyMode": False,
                    "BehaviourName": "LensObstruction",
                    "CompanyId": 8186
                })
                response = requests.request("POST", url, headers=headers,
                                            data=event_payload)
                if response.status_code == requests.codes.ok:
                    print("Event created successfully")
                else:
                    print("Event creation failed: " + str(response.status_code))

                # get Event ID
                event_response = json.loads(response.text)
                F2F_EVENT_ID_4TH = event_response["customerEventIdString"]
                Event_ID = event_response["id"]
                if response.status_code == requests.codes.ok:
                    print(f"get Event ID {F2F_EVENT_ID_4TH}")
                else:
                    print("Get Event ID failed: ")

                # Update event to F2F
                time.sleep(2)
                Update_EVENT_URL = UPDATE_EVENT_BASE_URL + 'safetyevents/events/' + Event_ID + '/eventBehaviorReview'
                headers = {'Content-Type': 'application/json',
                           'Accept': 'application/json, text/plain, */*',
                           'Accept-Language': 'en-US,en;q=0.9,en-IN;q=0.8',
                           'Authorization': f"Bearer {access_token}",
                           'Cache-Control': 'no-cache',
                           'Connection': 'keep-alive',
                           'DNT': '1',
                           'Origin': 'https://drivecam-stg2.drivecam.com',
                           'Pragma': 'no-cache',
                           'Sec-Fetch-Dest': 'empty',
                           'Sec-Fetch-Mode': 'cors',
                           'Sec-Fetch-Site': 'cross-site',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
                           'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"macOS"'
                           }
                update_event_payload = json.dumps({
                    "eventId": Event_ID,
                    "behaviorEdits": [
                        {
                            "id": 58,
                            "behaviorId": 58,
                            "operation": "add",
                            "reasonId": 2
                        }
                    ]
                })
                response = requests.request("POST", Update_EVENT_URL, headers=headers, data=update_event_payload)
                if response.status_code == requests.codes.ok:
                    print("Event " + F2F_EVENT_ID_4TH + " was updated successfully")
                else:
                    print("Event update failed: " + response.text)
                self.F2F_EVENT_ID_4TH = F2F_EVENT_ID_4TH

            case TestDataEnum.SELF_EVENT_1ST:
                # Create a new SELF event
                url = API_URL + "event/create/backend"
                headers = {'Content-Type': 'application/json'}
                event_payload = json.dumps({
                    "groupId": "5100ffff-60b6-d5cd-be83-a8a3e03f0000",
                    "eventTriggerTypeId": 2004,
                    "triggerDateTimeUtc": "2025-10-18T17:12:44.882",
                    "preTriggerSeconds": 8,
                    "postTriggerSeconds": 4,
                    "serialNumber": "OV00075173",
                    "eventSourceId": 6,
                    "psvLatitude": 32.88716,
                    "psvLongitude": -117.211655,
                    "psvDeviceSpeedKph": 128,
                    "psvPostedSpeedKph": 104,
                    "deletedReasonId": 0,
                    "adasTriggerSourceId": 3,
                    "checkPrivacyMode": False,
                    "BehaviourName": "LensObstruction",
                    "CompanyId": 8186
                })
                response = requests.request("POST", url, headers=headers,
                                            data=event_payload)
                if response.status_code == requests.codes.ok:
                    print("Event created successfully")
                else:
                    print("Event creation failed: " + str(response.status_code))

                # get Event ID
                event_response = json.loads(response.text)
                SELF_EVENT_ID_1ST = event_response["customerEventIdString"]
                Event_ID = event_response["id"]
                if response.status_code == requests.codes.ok:
                    print(f"get Event ID {SELF_EVENT_ID_1ST}")
                else:
                    print("Get Event ID failed: ")

                # Update event to Self event
                time.sleep(2)
                Update_EVENT_URL = UPDATE_EVENT_BASE_URL + 'safetyevents/events/' + Event_ID + '/eventBehaviorReview'
                headers = {'Content-Type': 'application/json',
                           'Accept': 'application/json, text/plain, */*',
                           'Accept-Language': 'en-US,en;q=0.9,en-IN;q=0.8',
                           'Authorization': f"Bearer {access_token}",
                           'Cache-Control': 'no-cache',
                           'Connection': 'keep-alive',
                           'DNT': '1',
                           'Origin': 'https://drivecam-stg2.drivecam.com',
                           'Pragma': 'no-cache',
                           'Sec-Fetch-Dest': 'empty',
                           'Sec-Fetch-Mode': 'cors',
                           'Sec-Fetch-Site': 'cross-site',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
                           'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"macOS"'
                           }
                update_event_payload = json.dumps({
                    "eventId": Event_ID,
                    "behaviorEdits": [
                        {
                            "id": 116,
                            "behaviorId": 116,
                            "operation": "add",
                            "reasonId": 2
                        }
                    ]
                })
                response = requests.request("POST", Update_EVENT_URL, headers=headers, data=update_event_payload)
                if response.status_code == requests.codes.ok:
                    print("Event " + SELF_EVENT_ID_1ST + " was updated successfully")
                else:
                    print("Event update failed: " + response.text)
                self.SELF_EVENT_ID_1ST = SELF_EVENT_ID_1ST

            case TestDataEnum.FYI_EVENT_1ST:
                # Create a new FYI event
                url = API_URL + "event/create/backend"
                headers = {'Content-Type': 'application/json'}
                event_payload = json.dumps({
                    "groupId": "5100ffff-60b6-d5cd-be83-a8a3e03f0000",
                    "eventTriggerTypeId": 2004,
                    "triggerDateTimeUtc": "2025-10-18T17:12:44.882",
                    "preTriggerSeconds": 8,
                    "postTriggerSeconds": 4,
                    "serialNumber": "OV00075173",
                    "eventSourceId": 6,
                    "psvLatitude": 32.88716,
                    "psvLongitude": -117.211655,
                    "psvDeviceSpeedKph": 128,
                    "psvPostedSpeedKph": 104,
                    "deletedReasonId": 0,
                    "adasTriggerSourceId": 3,
                    "checkPrivacyMode": False,
                    "BehaviourName": "LensObstruction",
                    "CompanyId": 8186
                })
                response = requests.request("POST", url, headers=headers,
                                            data=event_payload)
                if response.status_code == requests.codes.ok:
                    print("FYI_EVENT_1ST created successfully")
                else:
                    print("FYI_EVENT_1ST creation failed: " + str(response.status_code))

                # get Event ID
                event_response = json.loads(response.text)
                FYI_EVENT_ID_1ST = event_response["customerEventIdString"]
                Event_ID = event_response["id"]
                if response.status_code == requests.codes.ok:
                    print(f"get FYI_EVENT_1ST ID {FYI_EVENT_ID_1ST}")
                else:
                    print("Get FYI_EVENT_1ST ID failed: ")

                # Update event to FYI event
                time.sleep(2)
                Update_EVENT_URL = UPDATE_EVENT_BASE_URL + 'safetyevents/events/' + Event_ID + '/eventBehaviorReview'
                headers = {'Content-Type': 'application/json',
                           'Accept': 'application/json, text/plain, */*',
                           'Accept-Language': 'en-US,en;q=0.9,en-IN;q=0.8',
                           'Authorization': f"Bearer {access_token}",
                           'Cache-Control': 'no-cache',
                           'Connection': 'keep-alive',
                           'DNT': '1',
                           'Origin': 'https://drivecam-stg2.drivecam.com',
                           'Pragma': 'no-cache',
                           'Sec-Fetch-Dest': 'empty',
                           'Sec-Fetch-Mode': 'cors',
                           'Sec-Fetch-Site': 'cross-site',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
                           'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"macOS"'
                           }
                update_event_payload = json.dumps({
                    "eventId": Event_ID,
                    "behaviorEdits": [
                        {
                            "id": 144,
                            "behaviorId": 144,
                            "operation": "add",
                            "reasonId": 2
                        }
                    ]
                })
                response = requests.request("POST", Update_EVENT_URL, headers=headers, data=update_event_payload)
                if response.status_code == requests.codes.ok:
                    print("FYI_EVENT_1ST " + FYI_EVENT_ID_1ST + " was updated successfully")
                else:
                    print("FYI_EVENT_1ST update failed: " + response.text)
                self.FYI_EVENT_ID_1ST = FYI_EVENT_ID_1ST

            case TestDataEnum.FYI_EVENT_2ND:
                # Create a new FYI event
                url = API_URL + "event/create/backend"
                headers = {'Content-Type': 'application/json'}
                event_payload = json.dumps({
                    "groupId": "5100ffff-60b6-d5cd-be83-a8a3e03f0000",
                    "eventTriggerTypeId": 2004,
                    "triggerDateTimeUtc": "2025-10-18T17:12:44.882",
                    "preTriggerSeconds": 8,
                    "postTriggerSeconds": 4,
                    "serialNumber": "OV00075173",
                    "eventSourceId": 6,
                    "psvLatitude": 32.88716,
                    "psvLongitude": -117.211655,
                    "psvDeviceSpeedKph": 128,
                    "psvPostedSpeedKph": 104,
                    "deletedReasonId": 0,
                    "adasTriggerSourceId": 3,
                    "checkPrivacyMode": False,
                    "BehaviourName": "LensObstruction",
                    "CompanyId": 8186
                })
                response = requests.request("POST", url, headers=headers,
                                            data=event_payload)
                if response.status_code == requests.codes.ok:
                    print("FYI_EVENT_2ND created successfully")
                else:
                    print("FYI_EVENT_2ND creation failed: " + str(response.status_code))

                # get Event ID
                event_response = json.loads(response.text)
                FYI_EVENT_ID_2ND = event_response["customerEventIdString"]
                Event_ID = event_response["id"]
                if response.status_code == requests.codes.ok:
                    print(f"get FYI_EVENT_2ND ID {FYI_EVENT_ID_2ND}")
                else:
                    print("Get FYI_EVENT_2ND ID failed: ")

                # Update event to FYI event
                time.sleep(2)
                Update_EVENT_URL = UPDATE_EVENT_BASE_URL + 'safetyevents/events/' + Event_ID + '/eventBehaviorReview'
                headers = {'Content-Type': 'application/json',
                           'Accept': 'application/json, text/plain, */*',
                           'Accept-Language': 'en-US,en;q=0.9,en-IN;q=0.8',
                           'Authorization': f"Bearer {access_token}",
                           'Cache-Control': 'no-cache',
                           'Connection': 'keep-alive',
                           'DNT': '1',
                           'Origin': 'https://drivecam-stg2.drivecam.com',
                           'Pragma': 'no-cache',
                           'Sec-Fetch-Dest': 'empty',
                           'Sec-Fetch-Mode': 'cors',
                           'Sec-Fetch-Site': 'cross-site',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
                           'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"macOS"'
                           }
                update_event_payload = json.dumps({
                    "eventId": Event_ID,
                    "behaviorEdits": [
                        {
                            "id": 144,
                            "behaviorId": 144,
                            "operation": "add",
                            "reasonId": 2
                        }
                    ]
                })
                response = requests.request("POST", Update_EVENT_URL, headers=headers, data=update_event_payload)
                if response.status_code == requests.codes.ok:
                    print("FYI_EVENT_2ND " + FYI_EVENT_ID_2ND + " was updated successfully")
                else:
                    print("FYI_EVENT_2ND update failed: " + response.text)

                # assign driver to the event
                url = UPDATE_EVENT_BASE_URL + "safetyevents/events/" + Event_ID

                payload = json.dumps({
                    "driverId": TD.driver_id,
                    "groupId": TD.group_id
                })
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f"Bearer {access_token}"
                }

                driver_response = requests.request("PUT", url, headers=headers, data=payload)
                if driver_response.status_code == requests.codes.ok:
                    print(f"Driver assigned to FYI_EVENT_2ND {FYI_EVENT_ID_2ND} successfully")
                else:
                    print("Driver assignment failed: FYI_EVENT_2ND" + driver_response.text)

                self.FYI_EVENT_ID_2ND = FYI_EVENT_ID_2ND

            case TestDataEnum.FYI_EVENT_3RD:
                # Create a new FYI event
                url = API_URL + "event/create/backend"
                headers = {'Content-Type': 'application/json'}
                event_payload = json.dumps({
                    "groupId": "5100ffff-60b6-d5cd-be83-a8a3e03f0000",
                    "eventTriggerTypeId": 2004,
                    "triggerDateTimeUtc": "2025-10-18T17:12:44.882",
                    "preTriggerSeconds": 8,
                    "postTriggerSeconds": 4,
                    "serialNumber": "OV00075173",
                    "eventSourceId": 6,
                    "psvLatitude": 32.88716,
                    "psvLongitude": -117.211655,
                    "psvDeviceSpeedKph": 128,
                    "psvPostedSpeedKph": 104,
                    "deletedReasonId": 0,
                    "adasTriggerSourceId": 3,
                    "checkPrivacyMode": False,
                    "BehaviourName": "LensObstruction",
                    "CompanyId": 8186
                })
                response = requests.request("POST", url, headers=headers,
                                            data=event_payload)
                if response.status_code == requests.codes.ok:
                    print("FYI_EVENT_3RD created successfully")
                else:
                    print("FYI_EVENT_3RD creation failed: " + str(response.status_code))

                # get Event ID
                event_response = json.loads(response.text)
                FYI_EVENT_ID_3RD = event_response["customerEventIdString"]
                Event_ID = event_response["id"]
                if response.status_code == requests.codes.ok:
                    print(f"get FYI_EVENT_3RD ID {FYI_EVENT_ID_3RD}")
                else:
                    print("Get FYI_EVENT_3RD ID failed: ")

                # Update event to FYI event
                time.sleep(2)
                Update_EVENT_URL = UPDATE_EVENT_BASE_URL + 'safetyevents/events/' + Event_ID + '/eventBehaviorReview'
                headers = {'Content-Type': 'application/json',
                           'Accept': 'application/json, text/plain, */*',
                           'Accept-Language': 'en-US,en;q=0.9,en-IN;q=0.8',
                           'Authorization': f"Bearer {access_token}",
                           'Cache-Control': 'no-cache',
                           'Connection': 'keep-alive',
                           'DNT': '1',
                           'Origin': 'https://drivecam-stg2.drivecam.com',
                           'Pragma': 'no-cache',
                           'Sec-Fetch-Dest': 'empty',
                           'Sec-Fetch-Mode': 'cors',
                           'Sec-Fetch-Site': 'cross-site',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
                           'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"macOS"'
                           }
                update_event_payload = json.dumps({
                    "eventId": Event_ID,
                    "behaviorEdits": [
                        {
                            "id": 144,
                            "behaviorId": 144,
                            "operation": "add",
                            "reasonId": 2
                        }
                    ]
                })
                response = requests.request("POST", Update_EVENT_URL, headers=headers, data=update_event_payload)
                if response.status_code == requests.codes.ok:
                    print("FYI_EVENT_3RD " + FYI_EVENT_ID_3RD + " was updated successfully")
                else:
                    print("FYI_EVENT_3RD update failed: " + response.text)

                # assign driver to the event
                url = UPDATE_EVENT_BASE_URL + "safetyevents/events/" + Event_ID

                payload = json.dumps({
                    "driverId": TD.driver_id,
                    "groupId": TD.group_id
                })
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f"Bearer {access_token}"
                }

                driver_response = requests.request("PUT", url, headers=headers, data=payload)
                if driver_response.status_code == requests.codes.ok:
                    print(f"Driver assigned to FYI_EVENT_3RD {FYI_EVENT_ID_3RD} successfully")
                else:
                    print(f"Driver assignment failed: FYI_EVENT_3RD {driver_response.text}")

                self.FYI_EVENT_ID_3RD = FYI_EVENT_ID_3RD

            case TestDataEnum.COLLISION_EVENT_1ST:
                # Create a new COLLISION_EVENT_1ST event
                url = API_URL + "event/create/backend"
                headers = {'Content-Type': 'application/json'}
                event_payload = json.dumps({
                    "groupId": "5100ffff-60b6-d5cd-be83-a8a3e03f0000",
                    "eventTriggerTypeId": 2004,
                    "triggerDateTimeUtc": "2025-10-18T17:12:44.882",
                    "preTriggerSeconds": 8,
                    "postTriggerSeconds": 4,
                    "serialNumber": "OV00075173",
                    "eventSourceId": 6,
                    "psvLatitude": 32.88716,
                    "psvLongitude": -117.211655,
                    "psvDeviceSpeedKph": 128,
                    "psvPostedSpeedKph": 104,
                    "deletedReasonId": 0,
                    "adasTriggerSourceId": 3,
                    "checkPrivacyMode": False,
                    "BehaviourName": "LensObstruction",
                    "CompanyId": 8186
                })
                response = requests.request("POST", url, headers=headers,
                                            data=event_payload)
                if response.status_code == requests.codes.ok:
                    print("COLLISION_EVENT_1ST created successfully")
                else:
                    print("COLLISION_EVENT_1ST creation failed: " + str(response.status_code))

                # get Event ID
                event_response = json.loads(response.text)
                COLLISION_EVENT_ID_1ST = event_response["customerEventIdString"]
                Event_ID = event_response["id"]
                if response.status_code == requests.codes.ok:
                    print(f"get COLLISION_EVENT_1ST ID {COLLISION_EVENT_ID_1ST}")
                else:
                    print("Get COLLISION_EVENT_1ST ID failed: ")

                # Update event to COLLISION event
                time.sleep(2)
                Update_EVENT_URL = UPDATE_EVENT_BASE_URL + 'safetyevents/events/' + Event_ID + '/eventBehaviorReview'
                headers = {'Content-Type': 'application/json',
                           'Accept': 'application/json, text/plain, */*',
                           'Accept-Language': 'en-US,en;q=0.9,en-IN;q=0.8',
                           'Authorization': f"Bearer {access_token}",
                           'Cache-Control': 'no-cache',
                           'Connection': 'keep-alive',
                           'DNT': '1',
                           'Origin': 'https://drivecam-stg2.drivecam.com',
                           'Pragma': 'no-cache',
                           'Sec-Fetch-Dest': 'empty',
                           'Sec-Fetch-Mode': 'cors',
                           'Sec-Fetch-Site': 'cross-site',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
                           'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"macOS"'
                           }
                update_event_payload = json.dumps({
                    "eventId": Event_ID,
                    "behaviorEdits": [
                        {
                            "id": 47,
                            "behaviorId": 47,
                            "operation": "add",
                            "reasonId": 2
                        }
                    ]
                })
                response = requests.request("POST", Update_EVENT_URL, headers=headers, data=update_event_payload)
                if response.status_code == requests.codes.ok:
                    print("COLLISION_EVENT_1ST " + COLLISION_EVENT_ID_1ST + " was updated successfully")
                else:
                    print("COLLISION_EVENT_1ST update failed: " + response.text)

                self.COLLISION_EVENT_ID_1ST = COLLISION_EVENT_ID_1ST

            case TestDataEnum.COLLISION_EVENT_2ND:
                # Create a new COLLISION_EVENT_2ND event
                url = API_URL + "event/create/backend"
                headers = {'Content-Type': 'application/json'}
                event_payload = json.dumps({
                    "groupId": "5100ffff-60b6-d5cd-be83-a8a3e03f0000",
                    "eventTriggerTypeId": 2004,
                    "triggerDateTimeUtc": "2025-10-18T17:12:44.882",
                    "preTriggerSeconds": 8,
                    "postTriggerSeconds": 4,
                    "serialNumber": "OV00075173",
                    "eventSourceId": 6,
                    "psvLatitude": 32.88716,
                    "psvLongitude": -117.211655,
                    "psvDeviceSpeedKph": 128,
                    "psvPostedSpeedKph": 104,
                    "deletedReasonId": 0,
                    "adasTriggerSourceId": 3,
                    "checkPrivacyMode": False,
                    "BehaviourName": "LensObstruction",
                    "CompanyId": 8186
                })
                response = requests.request("POST", url, headers=headers,
                                            data=event_payload)
                if response.status_code == requests.codes.ok:
                    print("COLLISION_EVENT_2ND created successfully")
                else:
                    print("COLLISION_EVENT_2ND creation failed: " + str(response.status_code))

                # get Event ID
                event_response = json.loads(response.text)
                COLLISION_EVENT_ID_2ND = event_response["customerEventIdString"]
                Event_ID = event_response["id"]
                if response.status_code == requests.codes.ok:
                    print(f"get COLLISION_EVENT_2ND ID {COLLISION_EVENT_ID_2ND}")
                else:
                    print("Get COLLISION_EVENT_2ND ID failed: ")

                # Update event to COLLISION_EVENT_2ND event
                time.sleep(2)
                Update_EVENT_URL = UPDATE_EVENT_BASE_URL + 'safetyevents/events/' + Event_ID + '/eventBehaviorReview'
                headers = {'Content-Type': 'application/json',
                           'Accept': 'application/json, text/plain, */*',
                           'Accept-Language': 'en-US,en;q=0.9,en-IN;q=0.8',
                           'Authorization': f"Bearer {access_token}",
                           'Cache-Control': 'no-cache',
                           'Connection': 'keep-alive',
                           'DNT': '1',
                           'Origin': 'https://drivecam-stg2.drivecam.com',
                           'Pragma': 'no-cache',
                           'Sec-Fetch-Dest': 'empty',
                           'Sec-Fetch-Mode': 'cors',
                           'Sec-Fetch-Site': 'cross-site',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
                           'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"macOS"'
                           }
                update_event_payload = json.dumps({
                    "eventId": Event_ID,
                    "behaviorEdits": [
                        {
                            "id": 47,
                            "behaviorId": 47,
                            "operation": "add",
                            "reasonId": 2
                        }
                    ]
                })
                response = requests.request("POST", Update_EVENT_URL, headers=headers, data=update_event_payload)
                if response.status_code == requests.codes.ok:
                    print("COLLISION_EVENT_2ND " + COLLISION_EVENT_ID_2ND + " was updated successfully")
                else:
                    print("COLLISION_EVENT_2ND update failed: " + response.text)

                # assign driver to the event
                url = UPDATE_EVENT_BASE_URL + "safetyevents/events/" + Event_ID

                payload = json.dumps({
                    "driverId": TD.driver_id,
                    "groupId": TD.group_id
                })
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f"Bearer {access_token}"
                }

                driver_response = requests.request("PUT", url, headers=headers, data=payload)
                if driver_response.status_code == requests.codes.ok:
                    print(f"Driver assigned to COLLISION_EVENT_2ND {COLLISION_EVENT_ID_2ND} successfully")
                else:
                    print("Driver assignment failed: COLLISION_EVENT_2ND" + driver_response.text)

                self.COLLISION_EVENT_ID_2ND = COLLISION_EVENT_ID_2ND

            case TestDataEnum.POSSIBLE_COLLISION_EVENT_1ST:
                # Create a new POSSIBLE_COLLISION_EVENT_1ST event
                url = API_URL + "event/create/backend"
                headers = {'Content-Type': 'application/json'}
                event_payload = json.dumps({
                    "groupId": "5100ffff-60b6-d5cd-be83-a8a3e03f0000",
                    "eventTriggerTypeId": 2004,
                    "triggerDateTimeUtc": "2025-10-18T17:12:44.882",
                    "preTriggerSeconds": 8,
                    "postTriggerSeconds": 4,
                    "serialNumber": "OV00075173",
                    "eventSourceId": 6,
                    "psvLatitude": 32.88716,
                    "psvLongitude": -117.211655,
                    "psvDeviceSpeedKph": 128,
                    "psvPostedSpeedKph": 104,
                    "deletedReasonId": 0,
                    "adasTriggerSourceId": 3,
                    "checkPrivacyMode": False,
                    "BehaviourName": "LensObstruction",
                    "CompanyId": 8186
                })
                response = requests.request("POST", url, headers=headers,
                                            data=event_payload)
                if response.status_code == requests.codes.ok:
                    print("Event created successfully")
                else:
                    print("Event creation failed: " + str(response.status_code))

                # get Event ID
                event_response = json.loads(response.text)
                POSSIBLE_COLLISION_EVENT_ID_1ST = event_response["customerEventIdString"]
                Event_ID = event_response["id"]
                if response.status_code == requests.codes.ok:
                    print(f"get Event ID {POSSIBLE_COLLISION_EVENT_ID_1ST}")
                else:
                    print("Get Event ID failed: ")

                # Update event to POSSIBLE_COLLISION_EVENT_1ST event
                time.sleep(2)
                Update_EVENT_URL = UPDATE_EVENT_BASE_URL + 'safetyevents/events/' + Event_ID + '/eventBehaviorReview'
                headers = {'Content-Type': 'application/json',
                           'Accept': 'application/json, text/plain, */*',
                           'Accept-Language': 'en-US,en;q=0.9,en-IN;q=0.8',
                           'Authorization': f"Bearer {access_token}",
                           'Cache-Control': 'no-cache',
                           'Connection': 'keep-alive',
                           'DNT': '1',
                           'Origin': 'https://drivecam-stg2.drivecam.com',
                           'Pragma': 'no-cache',
                           'Sec-Fetch-Dest': 'empty',
                           'Sec-Fetch-Mode': 'cors',
                           'Sec-Fetch-Site': 'cross-site',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
                           'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"macOS"'
                           }
                update_event_payload = json.dumps({
                    "eventId": Event_ID,
                    "behaviorEdits": [
                        {
                            "id": 72,
                            "behaviorId": 72,
                            "operation": "add",
                            "reasonId": 2
                        }
                    ]
                })
                response = requests.request("POST", Update_EVENT_URL, headers=headers, data=update_event_payload)
                if response.status_code == requests.codes.ok:
                    print("Event " + POSSIBLE_COLLISION_EVENT_ID_1ST + " was updated successfully")
                else:
                    print("Event update failed: " + response.text)
                self.POSSIBLE_COLLISION_EVENT_ID_1ST = POSSIBLE_COLLISION_EVENT_ID_1ST

            case TestDataEnum.POSSIBLE_COLLISION_EVENT_2ND:
                # Create a new POSSIBLE_COLLISION_EVENT_2ND event
                url = API_URL + "event/create/backend"
                headers = {'Content-Type': 'application/json'}
                event_payload = json.dumps({
                    "groupId": "5100ffff-60b6-d5cd-be83-a8a3e03f0000",
                    "eventTriggerTypeId": 2004,
                    "triggerDateTimeUtc": "2025-10-18T17:12:44.882",
                    "preTriggerSeconds": 8,
                    "postTriggerSeconds": 4,
                    "serialNumber": "OV00075173",
                    "eventSourceId": 6,
                    "psvLatitude": 32.88716,
                    "psvLongitude": -117.211655,
                    "psvDeviceSpeedKph": 128,
                    "psvPostedSpeedKph": 104,
                    "deletedReasonId": 0,
                    "adasTriggerSourceId": 3,
                    "checkPrivacyMode": False,
                    "BehaviourName": "LensObstruction",
                    "CompanyId": 8186
                })
                response = requests.request("POST", url, headers=headers,
                                            data=event_payload)
                if response.status_code == requests.codes.ok:
                    print("Event created successfully")
                else:
                    print("Event creation failed: " + str(response.status_code))

                # get Event ID
                event_response = json.loads(response.text)
                POSSIBLE_COLLISION_EVENT_ID_2ND = event_response["customerEventIdString"]
                Event_ID = event_response["id"]
                if response.status_code == requests.codes.ok:
                    print(f"get Event ID {POSSIBLE_COLLISION_EVENT_ID_2ND}")
                else:
                    print("Get Event ID failed: ")

                # Update event to POSSIBLE_COLLISION_EVENT_2ND event
                time.sleep(2)
                Update_EVENT_URL = UPDATE_EVENT_BASE_URL + 'safetyevents/events/' + Event_ID + '/eventBehaviorReview'
                headers = {'Content-Type': 'application/json',
                           'Accept': 'application/json, text/plain, */*',
                           'Accept-Language': 'en-US,en;q=0.9,en-IN;q=0.8',
                           'Authorization': f"Bearer {access_token}",
                           'Cache-Control': 'no-cache',
                           'Connection': 'keep-alive',
                           'DNT': '1',
                           'Origin': 'https://drivecam-stg2.drivecam.com',
                           'Pragma': 'no-cache',
                           'Sec-Fetch-Dest': 'empty',
                           'Sec-Fetch-Mode': 'cors',
                           'Sec-Fetch-Site': 'cross-site',
                           'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0',
                           'sec-ch-ua': '"Chromium";v="140", "Not=A?Brand";v="24", "Microsoft Edge";v="140"',
                           'sec-ch-ua-mobile': '?0',
                           'sec-ch-ua-platform': '"macOS"'
                           }
                update_event_payload = json.dumps({
                    "eventId": Event_ID,
                    "behaviorEdits": [
                        {
                            "id": 72,
                            "behaviorId": 72,
                            "operation": "add",
                            "reasonId": 2
                        }
                    ]
                })
                response = requests.request("POST", Update_EVENT_URL, headers=headers, data=update_event_payload)
                if response.status_code == requests.codes.ok:
                    print("PC2 Event " + POSSIBLE_COLLISION_EVENT_ID_2ND + " was updated successfully")
                else:
                    print("PC2 Event update failed: " + response.text)

                # assign driver to the event
                url = UPDATE_EVENT_BASE_URL + "safetyevents/events/" + Event_ID

                payload = json.dumps({
                    "driverId": TD.driver_id,
                    "groupId": TD.group_id
                })
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': f"Bearer {access_token}"
                }

                driver_response = requests.request("PUT", url, headers=headers, data=payload)
                if driver_response.status_code == requests.codes.ok:
                    print(f"Driver assigned to POSSIBLE_COLLISION_EVENT_2ND {POSSIBLE_COLLISION_EVENT_ID_2ND} successfully")
                else:
                    print(f"Driver assignment failed: POSSIBLE_COLLISION_EVENT_2ND {driver_response.text}")

                self.POSSIBLE_COLLISION_EVENT_ID_2ND = POSSIBLE_COLLISION_EVENT_ID_2ND

    def cloud_add_vehicle(self, group_ID, company_id):
        headers = {'Content-Type': 'application/json'}
        timestamp_ms = int(time.time() * 1000)
        payload = {
            "groupId": group_ID,
            "name": "testautoVehicle" + str(timestamp_ms),
            "type": "Car",
            "status": "InService",
            "make": "PETERBILT",
            "model": "567",
            "deleted": False,
            "companyId": company_id,
            "seatBeltType": "ShoulderHarness",
            "appId": 0
        }
        json_updated_event_payload = json.dumps(payload)
        response = requests.request("POST", CREATE_VEHICLE_ENDPOINT, headers=headers,
                                    data=json_updated_event_payload)
        print(response.status_code)
        data = response.json()
        vehicleId = data['id']
        vehicleName = data['name']
        vehicle_data = {
            "vehicleName": vehicleName,
            "vehicleId": vehicleId
        }
        return vehicle_data

    def add_device(self, autobots_groupId, vehicleId, RootGroupId, company_id):
        headers = {'Content-Type': 'application/json'}

        timestamp_ms = int(time.time() * 1000)
        payload = {
            "SerialNumber": "testauto" + str(timestamp_ms),
            "stackId": 4,
            "groupId": autobots_groupId,
            "RootGroupId": RootGroupId,
            "companyId": company_id,
            "vehicleId": vehicleId
        }

        json_updated_event_payload = json.dumps(payload)
        response = requests.request("POST", CREATE_DEVICES_ENDPOINT, headers=headers,
                                    data=json_updated_event_payload)
        print(response.status_code)
        print(response.text)
        data = response.json()
        serialNumber = data['serialNumber']
        return serialNumber

    def send_device_speed_violations(self, serialNumber):
        headers = {'Content-Type': 'application/json'}
        send_device_speed_violations_url = BASE_URL_DEVICE_MESSAGE_SIMULATOR_STG + '/json/device.speedviolations/' + serialNumber
        now = datetime.utcnow()
        formatted = now.strftime("%Y-%m-%dT%H:%M:%S.") + f"{int(now.microsecond / 1000):03d}"
        print(formatted)
        payload = {
            "timestamp": str(formatted),
            "heading": 3.14159,
            "latitude": 40.7128,
            "longitude": -74.006,
            "speedThresholdKph": 110.777,
            "maxSpeedKph": 120.999,
            "durationInSec": 11,
            "type": 2,
            "speedSource": 0,
            "segmentId": "freeway"
        }
        json_updated_event_payload = json.dumps(payload)
        response = requests.request("POST", send_device_speed_violations_url, headers=headers,
                                    data=json_updated_event_payload)
        print(response.status_code)

    def send_device_idle_violations(self, serialNumber):
        headers = {'Content-Type': 'application/json'}
        send_device_idle_violations_url = BASE_URL_DEVICE_MESSAGE_SIMULATOR_STG + '/json/device.idleviolations/' + serialNumber
        now = datetime.utcnow()
        formatted = now.strftime("%Y-%m-%dT%H:%M:%S.") + f"{int(now.microsecond / 1000):03d}"
        payload = {
            "timestamp": str(formatted),
            "latitude": 51.547543,
            "longitude": 0.180833,
            "durationInSec": 3500
        }
        json_updated_event_payload = json.dumps(payload)
        response = requests.request("POST", send_device_idle_violations_url, headers=headers,
                                    data=json_updated_event_payload)
        print(response.status_code)


class TestDataEnum(Enum):
    AUTH_TOKEN = 0
    VAULT_SECRETS = 1
    FYI_EVENT_1ST = 6000
    FYI_EVENT_2ND = 6001
    FYI_EVENT_3RD = 6002
    F2F_EVENT_1ST = 6100
    F2F_EVENT_2ND = 6101
    F2F_EVENT_3RD = 6102
    F2F_EVENT_4TH = 6103
    COLLISION_EVENT_1ST = 6200
    COLLISION_EVENT_2ND = 6201
    COLLISION_EVENT_3RD = 6202
    POSSIBLE_COLLISION_EVENT_1ST = 6300
    POSSIBLE_COLLISION_EVENT_2ND = 6301
    SELF_EVENT_1ST = 6400

    DRIVER_VEHICLE_SUMMARY = 7000
    TRIP_DRIVER_PROFILE = 7001
    IDLE_DRIVER_PROFILE = 7002
