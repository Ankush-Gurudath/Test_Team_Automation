import random
import string
import time
from datetime import datetime
from random import randint
from time import sleep

from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException, \
    ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
import os


class BasePage:
    def __init__(self, driver):
        self.random_word = None
        self.random_name = None
        self.random_digit = None
        self.driver = driver

    def find(self, locator):
        return WebDriverWait(self.driver, 60).until(ec.presence_of_element_located(locator))

    def wait_for_page_to_fully_load(self):
        return WebDriverWait(self.driver, 60).until(lambda d: d.execute_script('return document.readyState') == 'complete')

    def find_no_timeout(self, locator):
        return WebDriverWait(self.driver, 1).until(ec.presence_of_element_located(locator))

    def find_elements(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(ec.presence_of_all_elements_located(locator))
        except TimeoutException:
            elements = []
            return elements

    def click(self, locator):
        try:
            self.wait_for_element_is_clickable(locator)
            self.find(locator).click()
        except (ElementClickInterceptedException, ElementNotInteractableException, StaleElementReferenceException, TimeoutException):
            sleep(2)
            webElement = self.find(locator)
            self.driver.execute_script("arguments[0].click();", webElement)

    def type(self, locator, input_text):
        try:
            self.find(locator).send_keys(input_text)
        except (StaleElementReferenceException, ElementNotInteractableException, TimeoutException):
            element = self.find(locator)
            self.driver.execute_script("arguments[0].value = arguments[1];", element, input_text)

    def type_and_auto_search(self, locator, input_text):
        for i in input_text:
            self.find(locator).send_keys(i)
            sleep(0.01)

    def get_text(self, locator):
        try:
            element = self.find(locator)
            text = element.text.strip()

            # Fallback if .text is empty
            if not text:
                text = self.driver.execute_script(
                    "return arguments[0].innerText || arguments[0].textContent;",
                    element
                ).strip()
            return text

        except (StaleElementReferenceException, ElementClickInterceptedException,
                ElementNotInteractableException, TimeoutException):
            sleep(2)
            element = self.find(locator)
            text = element.text.strip()

            if not text:
                text = self.driver.execute_script(
                    "return arguments[0].innerText || arguments[0].textContent;",
                    element
                ).strip()
            return text

    def get_attribute(self, locator, attribute):
        return self.find(locator).get_attribute(attribute)

    def back(self):
        self.driver.back()

    def clear(self, locator):
        self.find(locator).clear()

    def get_row_count(self, attempts=2):
        sleep(3)
        i = 0
        while i < attempts:
            try:
                self.find((By.TAG_NAME, "cdk-table"))
                break
            except (TimeoutException, NoSuchElementException):
                i += 2

        sleep(3)
        self.find((By.TAG_NAME, "cdk-table"))
        rows = self.find_elements((By.TAG_NAME, "cdk-row"))
        if rows is None:
            return 0
        return len(rows)

    def get_random_name(self, length):
        global random_name

        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        print("Random string of length", length, "is:", result_str)
        self.random_name = result_str
        return self.random_name

    def get_random_string(self):
        global random_word
        characters = string.ascii_letters + string.digits + string.punctuation
        characters = string.ascii_letters + string.digits + string.punctuation.replace('\\', '')
        password = ''.join(random.choice(characters) for i in range(8))
        print("Random password is:", password)
        self.random_word = password
        return self.random_word

    def get_random_with_N_digits(self, n):
        global random_digit
        range_start = 10 ** (n - 1)
        range_end = (10 ** n) - 1
        num = randint(range_start, range_end)
        self.random_digit = num
        return self.random_digit

    def click_refresh_button(self):
        self.driver.refresh()

    def element_is_displayed(self, locator):
        try:
            elements = self.find_elements(locator)
            if len(elements) == 0:
                return False
            else:
                return True
        except TimeoutException:
            return False

    def element_is_displayed_no_timeout(self, locator):
        try:
            self.find_no_timeout(locator)
        except (TimeoutException, NoSuchElementException):
            return False
        return True

    def wait_for_element_is_clickable(self, locator, wait_time=20):
        return WebDriverWait(self.driver, wait_time).until(ec.element_to_be_clickable(locator))

    def close_walkme_dialog(self):
        self.wait_for_page_to_fully_load()
        walkme_dialog_count = len(self.find_elements((By.XPATH, '//*[contains(@class, "close")]')))
        i = 0
        while i < walkme_dialog_count:
            self.find_elements((By.XPATH, '//*[contains(@class, "close")]'))[0].click()
            i += 1
            sleep(2)

    def close_pendo_dialog(self):
        self.wait_for_page_to_fully_load()
        pendo_dialog_count = len(self.find_elements((By.XPATH, '//button[contains(text(), "Done")]')))
        i = 0
        while i < pendo_dialog_count:
            self.find_elements((By.XPATH, '//button[contains(text(), "Done")]'))[0].click()
            i += 1
            sleep(2)

    def accept_geotab_end_user_agreement(self):
        self.wait_for_page_to_fully_load()
        if self.element_is_displayed((By.XPATH, '//*[text()="End User Agreement"]')) is True:
            self.click((By.XPATH, '//*[text()="Geotab End User Agreement"]'))
            self.scroll_to_element(self.find((By.XPATH, '//*[contains(text(),"V.4")]')))
            self.click((By.ID, 'acceptEulaButtonId'))

    def url_change(self, expected_url):
        return WebDriverWait(self.driver, 60).until(ec.url_changes(expected_url))

    def wait_for_expected_text(self, locator, expected_text, attempts=5, wait_time=5):
        n = 0
        while n < attempts:
            n += 1
            try:
                if expected_text in self.get_text(locator):
                    break
                sleep(wait_time)
            except StaleElementReferenceException:
                sleep(wait_time)
            except TimeoutException:
                sleep(1)
        return self.get_text(locator)

    def wait_for_expected_text_change(self, locator, expected_text, attempts=5, wait_time=10):
        n = 0
        while n < attempts:
            n += 1
            try:
                if expected_text != self.get_text(locator):
                    break
                sleep(wait_time)
            except StaleElementReferenceException:
                sleep(wait_time)
            except TimeoutException:
                sleep(1)

        return self.get_text(locator)

    def wait_for_expected_number(self, locator, expected_number='', attempts=5):
        n = 0
        while n < attempts:
            n += 1
            try:
                if expected_number.isdigit() and int(expected_number) == self.get_text(locator):
                    break
                if not expected_number.isdigit() and self.get_text(locator).isdigit():
                    break
                sleep(5)
            except StaleElementReferenceException:
                sleep(5)
            except TimeoutException:
                sleep(1)

        return self.get_text(locator)

    def wait_for_element_displayed(self, locator, attempts=5):
        n = 0
        while n < attempts:
            n += 1
            try:
                if self.element_is_displayed(locator):
                    break
            except StaleElementReferenceException:
                sleep(5)
            except TimeoutException:
                sleep(1)

        return self.element_is_displayed(locator)

    def wait_for_element_with_attribute(self, locator, attribute_name, attempts=5):
        n = 0
        while n < attempts:
            n += 1
            try:
                self.get_attribute(locator, attribute_name)
                break
            except StaleElementReferenceException:
                sleep(5)
            except TimeoutException:
                sleep(1)

        return self.get_attribute(locator, attribute_name)

    def click_element_ignore_exceptions(self, locator, attempts=5):
        n = 0
        while n < attempts:
            n += 1
            try:
                self.click(locator)
                break
            except (StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException):
                sleep(5)
            except TimeoutException:
                sleep(1)

        if n == attempts:
            self.click(locator)

    def type_ignore_exceptions(self, locator, input_text, attempts=5):
        self.wait_for_element_displayed(locator)
        n = 0
        while n < attempts:
            n += 1
            try:
                self.type(locator, input_text)
                break
            except StaleElementReferenceException:
                sleep(5)
            except TimeoutException:
                sleep(1)

        if n == attempts:
            self.type(locator, input_text)

    def check_file_exist(self, file_name):
        file_exist_script = 'browserstack_executor: {"action": "fileExists", "arguments": ' \
                            '{"fileName": "' + file_name + '"}}'

        return self.driver.execute_script(file_exist_script)

    def wait_for_file_downloaded(self, file_name):
        i = 0
        while i < 10:
            i += 1
            sleep(10)
            if self.check_file_exist(file_name) is True:
                break
        return self.check_file_exist(file_name)

    def scroll_page_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_page_left(self, pixels=100):
        self.driver.execute_script(f"window.scrollBy(-{pixels}, 0);")

    def get_current_url(self):
        return self.driver.current_url

    def scroll_page_up(self):
        self.driver.execute_script("window.scrollTo(0,0)")

    def scroll_to_element(self, web_element):
        self.driver.execute_script("arguments[0].scrollIntoView();", web_element)

    def switch_to_first_tab(self, index):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[index])

    def wait_till_element_disappear(self, locator):
        try:
            WebDriverWait(self.driver, 10).until_not(
                ec.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False

    def wait_till_file_downloaded_local(self, path, file_name):
        seconds = 0
        dl_wait = True
        while dl_wait and seconds < 120:
            sleep(1)
            dl_wait = False
            for fname in os.listdir(path):
                if fname == file_name and fname.endswith('.crdownload'):
                    dl_wait = True
                    break
            seconds += 1

    def wait_for_page_load(self):
        i = 0
        while i < 15:
            element = self.wait_till_element_disappear((By.XPATH, '//*[@class="circular"]'))
            i = i + 1
            if element is True:
                break

    def wait_for_element_enabled(self, locator):
        WebDriverWait(self.driver, 60).until_not(
            ec.presence_of_element_located(locator))

    def move_to_element(self, web_element):
        actions = ActionChains(self.driver)
        actions.move_to_element(web_element).perform()

    def navigate_to(self, url):
        self.driver.get(url)

    # it will return a date like Jun 5, 2024
    def get_time_today(self):
        now = datetime.now()
        today = f"{now.strftime('%b')} {now.day}, {now.year}"
        return today

    def check_download_file_exist(self, file_name):
        # Prepend wildcard to ignore date prefix
        file_name_with_wildcard = f"*{file_name}"

        file_exist_script = (
                'browserstack_executor: {"action": "fileExists", "arguments": '
                '{"_download-file/-name": "' + file_name_with_wildcard + '"}}'
        )
        return self.driver.execute_script(file_exist_script)

    # Wait for the download file to appear
    def wait_for_download_file(self, file_name, timeout=30):
        interval = 10
        for _ in range(timeout // interval):
            time.sleep(interval)
            if self.check_download_file_exist(file_name):
                return True
        return False




