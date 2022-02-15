import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep
from src.Extensions.WebDriverSetup import WebDriverSetup
from src.PageObjects.AboutUsPage import AboutUsPage
from src.TestData.AboutUsPageTestData import AboutUsPageTestData

class Test_AboutUs(WebDriverSetup):
    def test_aboutus_load(self):
        self.driver.get("https://www.qualitasdigital.com/about-us")
        self.driver.set_page_load_timeout(10)
        about_us_page = AboutUsPage(self.driver)
        self.assertTrue(about_us_page.logo_image.is_displayed())
    def test_aboutus_content(self):
        self.driver.get("https://www.qualitasdigital.com/about-us")
        self.driver.set_page_load_timeout(10)
        about_us_page = AboutUsPage(self.driver)
        self.assertEqual(AboutUsPageTestData.header_title, about_us_page.header_title.get_attribute("innerText"))
        self.assertEqual(AboutUsPageTestData.aboutus_title, about_us_page.title.get_attribute("innerText"))
        self.assertIn(AboutUsPageTestData.aboutus_image_src, about_us_page.image.get_attribute("src"))
        self.assertEqual(AboutUsPageTestData.aboutus_body_text, about_us_page.body_text.get_attribute("innerText"))
        self.assertEqual(AboutUsPageTestData.our_services_link, about_us_page.our_services_link.get_attribute("href"))
        self.assertEqual(AboutUsPageTestData.schedule_consultation_link, about_us_page.schedule_consultation_link.get_attribute("href"))

    if __name__ == '__main__':
        unittest.main()