import unittest
from src.TestCases.BaseTest import BaseTest
from src.PageObjects.ScheduleConsultationPage import ScheduleConsultationPage
from src.TestData.ScheduleConsultationPageTestData import ScheduleConsultationPageTestData
from selenium.webdriver.common.by import By

class Test_ScheduleConsultation(BaseTest):
    def test_scheduleconsultation_load(self):
        scheduleconsultation_page = ScheduleConsultationPage(self.driver)
        scheduleconsultation_page.validate_load()
    def test_scheduleconsultation_content(self):
        scheduleconsultation_page = ScheduleConsultationPage(self.driver)

        #Validate title
        self.assertEqual(ScheduleConsultationPageTestData.header_content, scheduleconsultation_page.get_header_content().get_attribute("innerText"))

        #Validate left section
        self.assertEqual(ScheduleConsultationPageTestData.left_content, scheduleconsultation_page.get_left_content().get_attribute("innerText"))
        self.assertEqual(ScheduleConsultationPageTestData.our_commitment_link, scheduleconsultation_page.get_our_commitment_link().get_attribute("href"))
        self.assertEqual(ScheduleConsultationPageTestData.faq_link, scheduleconsultation_page.get_header_content().get_attribute("href"))
        self.assertEqual(ScheduleConsultationPageTestData.terms_and_conditions_link, scheduleconsultation_page.get_header_content().get_attribute("href"))

        #Validate right section
        self.assertEqual(ScheduleConsultationPageTestData.schedule_consultation_button_link, scheduleconsultation_page.get_schedule_consultation_button_link().get_attribute("href"))
        
        #Due to the lack of test environments, there aren't any tests for scheduling the consultation on calendly, and their tests cover that anyway.


