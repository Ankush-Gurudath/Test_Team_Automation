import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options as ChromeOptions
import requests
import yaml
from requests.auth import HTTPBasicAuth
from selenium.common import NoSuchElementException, TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from locators.locators_fleet_telematics_centerpage import LocatorsFleetTelematicsCenterPage as GR
from pages.base_page import BasePage
from selenium.webdriver.remote.file_detector import LocalFileDetector


class GeotabReportAddIns(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.GET_URL = "https://api-cloud.browserstack.com/automate/recent_media_files"
        self.DELETE_URL = "https://api-cloud.browserstack.com/automate/custom_media/delete/{}"
        self.UPLOAD_URL = "https://api-cloud.browserstack.com/automate/upload-media"
        self.YAML_FILE = os.path.join(os.getcwd(), "browserstack_geotab_report_add_ins_stg.yml")

    def file_upload_preloaded_files(self, report_name):
        report_name = report_name.strip()
        file_path = os.path.join(r"C:\Users\hello\Documents\documents", report_name)
        if file_path.lower().endswith(".xlsx"):
            file_path = file_path
        else:
            file_path = f"{file_path}.xlsx"
        self.driver.find_element(By.XPATH, '//input[@class="uploadFileElement"]').send_keys(file_path)
        self.wait_for_page_to_fully_load()
        if self.element_is_displayed((By.ID, GR.savereport_id)):
            self.driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"passed", "reason": "Successfully uploaded!!"}}')
        else:
            self.driver.execute_script(
                'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "File upload failed!!"}}')

    def upload_file_locally(self, folder_name, report_name):
        report_name = report_name.strip()
        absolute_path = os.path.abspath("files/" + folder_name + "/" + report_name)
        print("Resolved path:", absolute_path)
        print("Exists:", os.path.isfile(absolute_path))

        if not os.path.isfile(absolute_path):
            raise FileNotFoundError(f"File not found at: {absolute_path}")

        file_input = self.driver.find_element(By.XPATH, '//input[@class="uploadFileElement"]')

        self.driver.execute_script("""
            arguments[0].style.display = 'block';
            arguments[0].style.visibility = 'visible';
            arguments[0].style.opacity = 1;
        """, file_input)
        file_input.send_keys(absolute_path)
        self.wait_for_page_to_fully_load()
        self.wait_for_element_displayed((By.ID, GR.savereport_id))
        print("File upload triggered successfully.")

    def click_email_tab(self):
        self.wait_for_geo_spinning_icon_to_disappear()
        try:
            self.wait_for_element_displayed((By.ID, GR.email_report_tab_id))
            element = self.wait_for_element_is_clickable((By.ID, GR.email_report_tab_id))
            element.click()
        except (TimeoutException, NoSuchElementException, ElementClickInterceptedException):
            element = self.wait_for_element_is_clickable((By.ID, GR.email_report_tab_id))
            element.click()

    def wait_for_geo_spinning_icon_to_disappear(self):
        i = 0
        while i < 15:
            element = self.wait_till_element_disappear((By.XPATH, '//*[@class="geo-icon waitingElement"]'))
            i = i + 1
            if element is True:
                break

    def click_email_options_on(self):
        self.click((By.XPATH, GR.email_options_label_xpath))
        element = self.wait_for_element_is_clickable((By.XPATH, GR.email_options_on_xpath))
        element.click()

    def select_time_now_option(self):
        self.click((By.XPATH, GR.next_run_xpath1))
        # self.scroll_page_down()
        self.click((By.XPATH, GR.now_button_xpath))
        self.click((By.XPATH, GR.done_button_xpath))

    def select_refresh_period_30min(self):
        self.scroll_to_element(self.find((By.XPATH, '//*[text()="Type of report"]')))
        self.click((By.XPATH, GR.refresh_period_xpath))
        self.click((By.XPATH, GR.every_30min_period_xpath))

    def configure_report_send_email(self):
        self.wait_for_page_to_fully_load()
        self.click_email_tab()
        self.click((By.XPATH, GR.edit_report_name_xpath))
        report_name = self.driver.find_element(By.XPATH, GR.edit_report_name_xpath)
        self.click((By.ID, GR.report_name_id))
        report_name.send_keys("_testautomation_FTM")
        self.click_email_options_on()

    def add_individual_email(self, email):
        self.scroll_to_element(self.find((By.XPATH, GR.select_users_xpath)))
        self.wait_for_element_is_clickable((By.XPATH, GR.select_users_xpath))
        self.click((By.XPATH, GR.select_users_xpath))
        self.type((By.XPATH, GR.select_users_xpath), email)
        sleep(2)
        user1_option = (By.XPATH, f'//*[contains(text(), "{email}")]')
        self.wait_for_element_is_clickable(user1_option)
        self.click(user1_option)
        self.click((By.XPATH, '//*[text()="Email the report to me"]'))

    def save_report_and_wait_for_dashboard(self):
        self.scroll_to_element(self.find((By.XPATH, '//*[text()="Type of report"]')))
        self.click((By.ID, GR.savereport_id))
        self.wait_for_page_to_fully_load()
        self.wait_for_element_displayed((By.XPATH, GR.zt_search_name_comment_xpath))
        self.scroll_page_up()
        print("Report saved and Email Sent successfully")

    def saved_report_exists_in_dashboard(self, report_name):
        self.click((By.XPATH, GR.zt_search_name_comment_xpath))
        self.type((By.XPATH, GR.zt_search_name_comment_xpath), report_name + "_testautomation")
        if self.element_is_displayed((By.XPATH, "//*[text()=" + report_name + "_testautomation""]")):
            print(report_name + " Report is saved successfully and is displayed in the dashboard")
        self.driver.execute_script("window.scrollTo(0, 0);")
        self.scroll_page_up()
        return True

    def get_reportname_dashboard(self, reportname):
        try:
            report_text = self.get_text((By.XPATH, f'//*[text()="{reportname}_testautomation"]'))
            return report_text
        except (NoSuchElementException, TimeoutException):
            print("Report not found in dashboard")
            return None

    def remove_all_automation_reports(self):
        try:
            # Search for all reports ending with _testautomation
            self.click((By.XPATH, GR.zt_search_name_comment_xpath))
            self.type((By.XPATH, GR.zt_search_name_comment_xpath), "_testautomation")
            self.wait_for_page_to_fully_load()

            reports = self.driver.find_elements(
                By.XPATH, '(//*[contains(text(), "_testautomation")])[2]'
            )

            if not reports:
                print("No automation reports found to remove.")
                return

            print(f"Found {len(reports)} automation reports to remove.")

            for i in range(len(reports)):
                try:
                    # Always search again because DOM may refresh after deletion
                    self.click((By.XPATH, GR.zt_search_name_comment_xpath))
                    self.clear((By.XPATH, GR.zt_search_name_comment_xpath))
                    self.type((By.XPATH, GR.zt_search_name_comment_xpath), "_testautomation")
                    self.wait_for_page_to_fully_load()

                    report_element = self.find(
                        (By.XPATH, '(//*[contains(text(), "_testautomation")])[2]')
                    )
                    report_name = report_element.text.strip()
                    self.scroll_to_element(report_element)
                    print(f"Found report element: {report_name}")
                    report_element.click()
                    print(f"Clicked on report: {report_name}")

                    self.wait_for_page_to_fully_load()
                    element = self.driver.find_element(By.ID, "customReport_Uploader")
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
                    element.click()
                    print("Navigated to report uploader")

                    # Remove report
                    self.wait_for_element_is_clickable((By.ID, GR.remove_report_button_id))
                    self.click((By.ID, GR.remove_report_button_id))
                    print(f"Clicked remove button for: {report_name}")

                    self.click((By.ID, GR.remove_report_confirmation_button_xpath))
                    print(f"Report '{report_name}' removed successfully.")

                    # Small delay to let UI refresh after deletion
                    self.wait_for_page_to_fully_load()

                except Exception as e:
                    print(f"Could not remove report due to: {str(e)}")
                    continue

            print("Cleanup complete: All automation reports removed.")

        except Exception as e:
            print(f"Error during cleanup: {str(e)}")

    # Script to delete all media files from BrowserStack account
    def delete_all_media_files(self):

        # Step 1: Fetch all media files
        response = requests.get(self.GET_URL, auth=HTTPBasicAuth("aaronfawcett_7yUJj9", "1NnNfSqs2s5cwsggj6sj"))

        if response.status_code != 200:
            print(f"Failed to fetch media files. Status: {response.status_code}, Response: {response.text}")
            return

        media_files = response.json()

        if not media_files:
            print("No media files found.")
            return

        print(f"Found {len(media_files)} media files. Deleting...")

        # Step 2: Loop through and delete each media_id
        for media in media_files:
            media_id = media["media_id"]
            delete_endpoint = self.DELETE_URL.format(media_id)

            del_response = requests.delete(delete_endpoint,
                                           auth=HTTPBasicAuth("aaronfawcett_7yUJj9", "1NnNfSqs2s5cwsggj6sj"))

            if del_response.status_code == 200:
                print(f"Deleted: {media['media_name']} ({media_id})")
            else:
                print(
                    f"Failed to delete {media_id}. Status: {del_response.status_code}, Response: {del_response.text}")

    if __name__ == "__main__":
        delete_all_media_files()
        print("All media files deleted.")

    def upload_files_and_store_yaml(self, report_folder):
        TEST_FOLDER = os.path.join(os.getcwd(), "files", report_folder)
        if not os.path.exists(TEST_FOLDER):
            raise FileNotFoundError(f"Test folder not found: {TEST_FOLDER}")

        files = os.listdir(TEST_FOLDER)
        if not files:
            raise FileNotFoundError("No files found inside test folder.")

        print(f"Found {len(files)} files. Uploading...")

        media_urls = []

        for filename in files:
            file_path = os.path.join(TEST_FOLDER, filename)

            if os.path.isfile(file_path):
                with open(file_path, "rb") as f:
                    response = requests.post(
                        self.UPLOAD_URL,
                        auth=HTTPBasicAuth("aaronfawcett_7yUJj9", "1NnNfSqs2s5cwsggj6sj"),
                        files={"file": f}
                    )

                try:
                    resp_json = response.json()
                except Exception:
                    print(f"Could not parse JSON. Raw response: {response.text}")
                    continue

                if response.status_code == 200 and "media_url" in resp_json:
                    full_media_url = resp_json["media_url"]
                    media_id = full_media_url.split("//")[-1]  # only after //

                    media_urls.append(f"media://{media_id}")
                    print(f"Uploaded {filename} | media_id: {media_id}")
                else:
                    print(f"Failed to upload {filename}. "
                          f"Status: {response.status_code}, Response: {resp_json}")

            # Save media URLs into YAML in array format
        if media_urls:
            final_yaml = {"uploadMedia": media_urls}

            with open(self.YAML_FILE, "w") as yaml_file:
                yaml.dump(final_yaml, yaml_file, default_flow_style=True)

            print(f"\nMedia IDs stored in {self.YAML_FILE}")
            print(yaml.dump(final_yaml, default_flow_style=True))  # preview
            return final_yaml
        else:
            raise RuntimeError("No files were uploaded successfully.")
