import unittest
from src.TestCases.BaseTest import BaseTest
from src.PageObjects.FaqPage import FaqPage
from src.TestData.FaqPageTestData import FaqPageTestData

class Test_Faq(BaseTest):
    def test_faq_load(self):
        faq_page = FaqPage(self.driver)
        faq_page.validate_load()
    def test_faq_content(self):
        faq_page = FaqPage(self.driver)
        self.assertEqual(FaqPageTestData.faq_title, faq_page.get_header_content().get_attribute("innerText"))
        self.assertEqual(FaqPageTestData.faq_subtitle, faq_page.get_sidebar_content().get_attribute("innerText"))
        self.assertEqual(FaqPageTestData.contactus_link, faq_page.get_contact_us_link().get_attribute("href"))
        faqPageExpectedTitles = [
            FaqPageTestData.title_one,
            FaqPageTestData.title_two,
            FaqPageTestData.title_three,
            FaqPageTestData.title_four,
            FaqPageTestData.title_five,
            FaqPageTestData.title_six,
            FaqPageTestData.title_seven,
            FaqPageTestData.title_eight,
            FaqPageTestData.title_nine,
            FaqPageTestData.title_eight,
            FaqPageTestData.title_eleven,
            FaqPageTestData.title_twelve,
            FaqPageTestData.title_thirteen,
            FaqPageTestData.title_fourteen,
            FaqPageTestData.title_fifteen]
        
        faqPageExpectedBodies = [
            FaqPageTestData.body_one,
            FaqPageTestData.body_two,
            FaqPageTestData.body_three,
            FaqPageTestData.body_four,
            FaqPageTestData.body_five,
            FaqPageTestData.body_six,
            FaqPageTestData.body_seven,
            FaqPageTestData.body_eight,
            FaqPageTestData.body_nine,
            FaqPageTestData.body_ten,
            FaqPageTestData.body_eleven,
            FaqPageTestData.body_twelve,
            FaqPageTestData.body_thirteen,
            FaqPageTestData.body_fourteen,
            FaqPageTestData.body_fifteen]

        faqPageActualTitles = faq_page.get_faq_page_titles()
        faqPageActualBodies = faq_page.get_faq_page_bodies()

        self.assertSetEqual(faqPageExpectedTitles, faqPageActualTitles)
        self.assertSetEqual(faqPageExpectedBodies, faqPageActualBodies)