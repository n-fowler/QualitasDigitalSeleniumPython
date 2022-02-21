from src.Locators import *
from src.PageObjects.BasePage import BasePage
from src.Locators.PricingAndServicesPageLocators import PricingAndServicesPageLocators
from selenium.webdriver.common.by import By

class PricingAndServicesPage(BasePage):
    def __init__(self, driver):
        self.locator = PricingAndServicesPageLocators
        super(PricingAndServicesPage, self).__init__(driver)
        self.go_to_url(PricingAndServicesPageLocators.url)

    def validate_load(self):
        self.find_element(*self.locator.logo_image)

    def get_header_title(self):
        return self.find_element(*self.locator.header_title)
    def get_sub_title(self):
        return self.find_element(*self.locator.sub_title)
    def get_our_commitment_link(self):
        return self.find_element(*self.locator.our_commitment_link)
    def get_additional_test_coverage_title(self):
        return self.find_element(*self.locator.additional_test_coverage_title)
    def get_additional_test_coverage_body_text(self):
        return self.find_element(*self.locator.additional_test_coverage_body_text)
    def get_framework_updates_title(self):
        return self.find_element(*self.locator.framework_updates_title)
    def get_framework_updates_body_text(self):
        return self.find_element(*self.locator.framework_updates_body_text)
    def get_framework_updates_custom_tailored_body_text(self):
        return self.find_element(*self.locator.framework_updates_custom_tailored_body_text)
    def get_process_automation_title(self):
        return self.find_element(*self.locator.process_automation_title)
    def get_process_automation_body_text(self):
        return self.find_element(*self.locator.process_automation_body_text)
    def get_dashboards_title(self):
        return self.find_element(*self.locator.dashboards_title)
    def get_dashboards_on_premise_body_text(self):
        return self.find_element(*self.locator.dashboards_on_premise_body_text)
    def get_dashboards_saas_body_text(self):
        return self.find_element(*self.locator.dashboards_saas_body_text)
    def get_dashboards_disclaimer_body_text(self):
        return self.find_element(*self.locator.dashboards_disclaimer_body_text)
    def get_training_title(self):
        return self.find_element(*self.locator.training_title)
    def get_training_body_text(self):
        return self.find_element(*self.locator.training_body_text)
    def get_coaching_title(self):
        return self.find_element(*self.locator.coaching_title)
    def get_coaching_body_text(self):
        return self.find_element(*self.locator.coaching_body_text)
    def get_roadmaps_title(self):
        return self.find_element(*self.locator.roadmaps_title)
    def get_roadmaps_body_text(self):
        return self.find_element(*self.locator.roadmaps_body_text)
    def get_trusted_advisor_title(self):
        return self.find_element(*self.locator.trusted_advisor_title)
    def get_trusted_advisor_body_text(self):
        return self.find_element(*self.locator.trusted_advisor_body_text)
    def get_technical_cofounder_title(self):
        return self.find_element(*self.locator.technical_cofounder_title)
    def get_technical_cofounder_body_text(self):
        return self.find_element(*self.locator.technical_cofounder_body_text)




