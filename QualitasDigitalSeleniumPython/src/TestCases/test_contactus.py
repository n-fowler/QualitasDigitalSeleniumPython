import unittest
from src.TestCases.BaseTest import BaseTest
from src.PageObjects.ContactUsPage import ContactUsPage
from src.TestData.ContactUsPageTestData import ContactUsPageTestData
from selenium.webdriver.common.by import By

class Test_ContactUs(BaseTest):
    def test_contactus_load(self):
        contactus_page = ContactUsPage(self.driver)
        contactus_page.validate_load()
    def test_contactus_content(self):
        contactus_page = ContactUsPage(self.driver)
        self.assertEqual(ContactUsPageTestData.left_content, contactus_page.get_sidebar_content().get_attribute("innerText"))
        self.assertEqual(ContactUsPageTestData.our_commitment_link, contactus_page.get_our_commitment_link().get_attribute("href"))
        self.assertEqual(ContactUsPageTestData.faq_link, contactus_page.get_faq_link().get_attribute("href"))
        self.assertEqual(ContactUsPageTestData.terms_and_conditions_link, contactus_page.get_terms_and_conditions_link().get_attribute("href"))
        self.assertIsNotNone(contactus_page.get_first_name_field())
        self.assertIsNotNone(contactus_page.get_last_name_field())
        self.assertIsNotNone(contactus_page.get_email_field())

        options = contactus_page.get_checkbox_section().find_elements(By.TAG_NAME, "div")
        expectedOptions = [
            "Additional Test Coverage",
            "Framework Updates",
            "Process Automation",
            "Dashboards",
            "Training",
            "Coaching",
            "Road maps",
            "Trusted Advisor",
            "Technical Co-Founder",
            "Other* (Include additional detail below)"]

        for i in range(len(options)):
            self.assertEqual("checkbox", options[i].find_element(By.TAG_NAME, "label").find_element(By.TAG_NAME, "input").get_property("type"))
            self.assertEqual(expectedOptions[i], options[i].find_element(By.TAG_NAME, "label").find_element(By.TAG_NAME, "input").get_property("value"))

        self.assertIsNotNone(contactus_page.get_additional_message_text_area())
        self.assertIsNotNone(contactus_page.get_submit_button())
        self.assertEqual("submit", contactus_page.get_submit_button().get_property("type"))
        self.assertEqual("Submit", contactus_page.get_submit_button().get_property("value"))