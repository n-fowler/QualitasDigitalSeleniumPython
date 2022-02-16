import unittest
from src.TestCases.BaseTest import BaseTest
from src.PageObjects.AboutUsPage import AboutUsPage
from src.TestData.AboutUsPageTestData import AboutUsPageTestData

class Test_AboutUs(BaseTest):
    def test_aboutus_load(self):
        aboutus_page = AboutUsPage(self.driver)
        aboutus_page.validate_load()
    def test_aboutus_content(self):
        aboutus_page = AboutUsPage(self.driver)
        self.assertEqual(AboutUsPageTestData.header_title, aboutus_page.get_header_title().get_attribute("innerText"))
        self.assertEqual(AboutUsPageTestData.aboutus_title, aboutus_page.get_title().get_attribute("innerText"))
        self.assertIn(AboutUsPageTestData.aboutus_image_src, aboutus_page.get_image().get_attribute("src"))
        self.assertEqual(AboutUsPageTestData.aboutus_body_text, aboutus_page.get_body_text().get_attribute("innerText"))
        self.assertEqual(AboutUsPageTestData.our_services_link, aboutus_page.get_our_services_link().get_attribute("href"))
        self.assertEqual(AboutUsPageTestData.schedule_consultation_link, aboutus_page.get_schedule_consultation_link().get_attribute("href"))