import unittest
from src.TestCases.BaseTest import BaseTest
from src.PageObjects.PricingAndServicesPage import PricingAndServicesPage
from src.TestData.PricingAndServicesPageTestData import PricingAndServicesPageTestData
from selenium.webdriver.common.by import By

class Test_PricingAndServices(BaseTest):
    def test_pricingandservices_load(self):
        pricingandservices_page = PricingAndServicesPage(self.driver)
        pricingandservices_page.validate_load()
    def test_pricingandservices_content(self):
        pricingandservices_page = PricingAndServicesPage(self.driver)

        #Validate header
        self.assertEqual(PricingAndServicesPageTestData.pricing_and_services_title, pricingandservices_page.get_header_title().get_attribute("innerText"))

        #Validate left subsection
        self.assertEqual(PricingAndServicesPageTestData.pricing_and_services_subtitle, pricingandservices_page.get_sub_title().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.our_commitment_link, pricingandservices_page.get_our_commitment_link().get_attribute("href"))

        #Validate middle subsection
        self.assertEqual(PricingAndServicesPageTestData.additional_test_coverage_title, pricingandservices_page.get_additional_test_coverage_title().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.additional_test_coverage_body_text, pricingandservices_page.get_additional_test_coverage_body_text().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.framework_updates_title, pricingandservices_page.get_framework_updates_title().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.framework_updates_upgrades_body_text,pricingandservices_page.get_framework_updates_body_text().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.framework_updates_custom_tailored_body_text,pricingandservices_page.get_framework_updates_custom_tailored_body_text().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.process_automation_title,pricingandservices_page.get_process_automation_title().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.process_automation_body_text,pricingandservices_page.get_process_automation_body_text().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.dashboards_title,pricingandservices_page.get_dashboards_title().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.dashboards_on_premise_body_text,pricingandservices_page.get_dashboards_on_premise_body_text().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.dashboards_saas_body_text,pricingandservices_page.get_dashboards_saas_body_text().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.dashboards_disclaimer_body_text,pricingandservices_page.get_dashboards_disclaimer_body_text().get_attribute("innerText"))

        #Validate right subsection
        self.assertEqual(PricingAndServicesPageTestData.training_title,pricingandservices_page.get_training_title().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.training_body_text,pricingandservices_page.get_training_body_text().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.coaching_title,pricingandservices_page.get_coaching_title().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.coaching_body_text,pricingandservices_page.get_coaching_body_text().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.roadmaps_title,pricingandservices_page.get_roadmaps_title().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.roadmaps_body_text,pricingandservices_page.get_roadmaps_body_text().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.trusted_advisor_title,pricingandservices_page.get_trusted_advisor_title().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.trusted_advisor_body_text,pricingandservices_page.get_trusted_advisor_body_text().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.technical_cofounder_title,pricingandservices_page.get_technical_cofounder_title().get_attribute("innerText"))
        self.assertEqual(PricingAndServicesPageTestData.technical_cofounder_body_text,pricingandservices_page.get_technical_cofounder_body_text().get_attribute("innerText"))




