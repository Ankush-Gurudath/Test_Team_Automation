from threading import local
import pytest
from selenium import webdriver
from selenium.common.exceptions import InvalidSessionIdException, WebDriverException

import utils.property_reader_util as property
from environment import stop_local
from utils import logging_util

assertError = local()
assertError.result = False

testName = ""
log = logging_util.logger(__name__)

# Fixtures
@pytest.fixture(scope="session")
def browser(request):
    browserName = request.config.getoption("--browser")
    log.info("Given browserName:" + browserName)

    if browserName != None and browserName != "":
        match browserName.lower():
            case "firefox":
                driver = AutoRestartWebDriver('Firefox')
            case "chrome":
                if(property.get_value_or_default("add_chrome_extension", "false").lower() == "true" or property.get_value_or_default("add_chrome_extension", "no").lower() == "yes"):
                    log.info("Initializing Chrome browser with extension...")
                    options = webdriver.ChromeOptions()
                    options.add_extension(property.get_value_or_default("chrome_extension_path_1", "files/chromeextension/GLEEKBFJEKINIECKNBKAMFMKOHKPODHE_2_0_0_0.crx"))
                    options.add_extension(property.get_value_or_default("chrome_extension_path_2", "files/chromeextension/HNOJOEMNDPDJOFCDAONBEFCFECPJFFLH_0_1_2_0.crx"))
                    options.add_extension(property.get_value_or_default("chrome_extension_path_3",
                                                                        "files/chromeextension/LHOBAFAHDDGCELFFKEICBAGINIGEEJLF_0_2_0_0.crx"))
                    driver = AutoRestartWebDriver('Chrome', options=options)
                else:
                    driver = AutoRestartWebDriver('Chrome')
            case "safari":
                driver = AutoRestartWebDriver('Safari')
            case "edge":
                driver = AutoRestartWebDriver('Edge')
            case _:
                pytest.fail('Incorrect browser given: ' + browserName + '. Please give correct browser name')
                log.error('Incorrect browser given: ' + browserName + '. Please give correct browser name')
    else:
        log.info("Initializing default browser...Chrome")
        driver = AutoRestartWebDriver('Chrome')

    assertError.result = False
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    yield driver
    driver.quit()
    stop_local()


@pytest.fixture
def context():
    return {}


def pytest_addoption(parser):
    property.load_environment()
    property.load_property()
    for property_key, property_value in property.properties.items():
        parser.addoption("--" + property_key, action="store", default=property_value)


# Enter any code that has to run before scenario is called
def pytest_bdd_before_scenario(scenario):
    global testName
    testName = str(scenario.name)
    log.info(testName)


class AutoRestartWebDriver:
    def __init__(self, browser="chrome", options=None, restart_on_fail=True):
        self.browser = browser
        self.options = options
        self.restart_on_fail = restart_on_fail
        self.last_url = None
        self._cookies = []
        self._local_storage = {}
        self._start_driver()

    def _start_driver(self):
        log.info("Starting new browser session...")
        if self.browser.lower() == "chrome":
            self.driver = webdriver.Chrome(options=self.options)
        elif self.browser.lower() == "firefox":
            self.driver = webdriver.Firefox(options=self.options)
        elif self.browser.lower() == "safari":
            self.driver = webdriver.Safari(options=self.options)
        elif self.browser.lower() == "edge":
            self.driver = webdriver.Edge(options=self.options)
        else:
            raise ValueError(f"Unsupported browser: {self.browser}")
        log.info(f"Session started: {self.driver.session_id}")

        if self.last_url:
            log.info(f"Restoring last visited URL: {self.last_url}")
            try:
                self.driver.get(self.last_url)
                self._restore_cookies_and_storage()
            except Exception as e:
                log.error(f"Failed to restore URL {self.last_url}: {e}")

    def _save_cookies_and_storage(self):
        try:
            self._cookies = self.driver.get_cookies()
            self._local_storage = self.driver.execute_script(
                "let ls = {}; for(let i=0; i<localStorage.length; i++){"
                "let k=localStorage.key(i); ls[k]=localStorage.getItem(k);} return ls;"
            )
            log.info(f"Saved {len(self._cookies)} cookies and {len(self._local_storage)} localStorage items")
        except Exception as e:
            log.error(f"Failed to save cookies/localStorage: {e}")

    def _restore_cookies_and_storage(self):
        try:
            for cookie in self._cookies:
                # Selenium expects expiry as int, ensure that
                if 'expiry' in cookie and isinstance(cookie['expiry'], float):
                    cookie['expiry'] = int(cookie['expiry'])
                try:
                    self.driver.add_cookie(cookie)
                except Exception as e:
                    log.warning(f"Failed to add cookie {cookie.get('name')}: {e}")

            self.driver.execute_script(
                "try { window.localStorage.clear(); } catch (e) { /* ignore */ }"
            )
            for key, value in self._local_storage.items():
                self.driver.execute_script(
                    f"window.localStorage.setItem(arguments[0], arguments[1]);",
                    key, value
                )
            log.info(f"Restored cookies and localStorage")
            # Refresh to apply cookies/localStorage if needed
            self.driver.refresh()
        except Exception as e:
            log.error(f"Failed to restore cookies/localStorage: {e}")

    def _restart_driver(self):
        try:
            log.info("Saving cookies and localStorage before restart...")
            self._save_cookies_and_storage()
        except Exception:
            pass

        try:
            log.info("Attempting to quit old driver...")
            self.driver.quit()
        except Exception:
            pass

        self._start_driver()

    def __getattr__(self, item):
        orig_attr = getattr(self.driver, item)

        if callable(orig_attr):
            def hooked(*args, **kwargs):
                try:
                    if item == "get" and args:
                        self.last_url = args[0]
                        log.info(f"Tracking last URL: {self.last_url}")

                    result = orig_attr(*args, **kwargs)
                    return result

                except InvalidSessionIdException:
                    log.error(f"SESSION LOST during: {item} | session_id={self.driver.session_id}")
                    if self.restart_on_fail:
                        log.info("Restarting browser session...")
                        self._restart_driver()
                        log.info(f"Retrying: {item}")
                        return getattr(self.driver, item)(*args, **kwargs)
                    raise

                except WebDriverException as e:
                    log.error(f"WebDriverException in {item}: {e}")
                    raise
            return hooked
        else:
            return orig_attr

    def is_session_alive(self):
        try:
            # Attempt to access current_url; will raise if session is dead
            _ = self.driver.current_url
            return True
        except (InvalidSessionIdException, WebDriverException):
            return False

    def quit(self):
        log.info(f"Closing session: {self.driver.session_id}")
        try:
            self.driver.quit()
        except Exception:
            pass