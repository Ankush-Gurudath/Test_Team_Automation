from selenium.webdriver.common.by import By

from locators.locators_coach_profile_page import LocatorsCoachesProfile as PR
from pages.base_page import BasePage


class CoachesProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_coach_profile_text(self):
        return self.get_text((By.XPATH, PR.coach_profile_text_xpath))

    def get_employee_id_text(self):
        return self.get_text((By.XPATH, PR.employee_id_text_xpath))

    def get_group_text(self):
        return self.get_text((By.XPATH, PR.group_text_xpath))

    def get_email_text(self):
        return self.get_text((By.XPATH, PR.email_text_xpath))

    def get_last_login_text(self):
        return self.get_text((By.XPATH, PR.last_login_text_xpath))

    def get_coaching_effectiveness_text(self):
        return self.get_text((By.XPATH, PR.coaching_effectiveness_text_xpath))

    def get_coached_behaviors_text(self):
        return self.get_text((By.XPATH, PR.coached_behaviors_text_xpath))

    def get_repeated_behaviors_text(self):
        return self.get_text((By.XPATH, PR.repeated_behaviors_text_xpath))

    def get_coached_events_text(self):
        return self.get_text((By.XPATH, PR.coached_events_text_xpath))

    def get_avg_days_to_coach_text(self):
        return self.get_text((By.XPATH, PR.avg_days_to_coach_text_xpath))

    def get_with_notes_text(self):
        return self.get_text((By.XPATH, PR.with_notes_text_xpath))

    def get_coaching_effectiveness_graph_text(self):
        return self.get_text((By.XPATH, PR.coaching_effectiveness_graph_text_xpath))

    def get_driver_text(self):
        return self.get_text((By.XPATH, PR.driver_text_xpath))

    def get_drivers_coaching_effectiveness_text(self):
        return self.get_text((By.XPATH, PR.drivers_coaching_effectiveness_text_xpath))

    def get_drivers_behaviors_group_text(self):
        return self.get_text((By.XPATH, PR.drivers_behaviors_group_text_xpath))

    def get_drivers_coached_behaviors_text(self):
        return self.get_text((By.XPATH, PR.drivers_coached_behaviors_text_xpath))

    def get_drivers_repeated_behaviors_text(self):
        return self.get_text((By.XPATH, PR.drivers_repeated_behaviors_text_xpath))

    def click_behaviors_group_tab(self):
        self.click((By.XPATH, PR.behavior_groups_tab_xpath))

    def get_behavior_group_text(self):
        return self.get_text((By.XPATH, PR.behavior_group_text_xpath))

    def get_behavior_coaching_effectiveness_text(self):
        return self.get_text((By.XPATH, PR.behavior_coaching_effectiveness_text_xpath))

    def get_behavior_drivers_text(self):
        return self.get_text((By.XPATH, PR.behavior_drivers_text_xpath))

    def get_coached_behaviors_group_text(self):
        return self.get_text((By.XPATH, PR.coached_behaviors_group_text_xpath))

    def get_repeated_behaviors_group_text(self):
        return self.get_text((By.XPATH, PR.repeated_behaviors_group_text_xpath))
