import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from time import sleep
from src.Extensions.WebDriverSetup import WebDriverSetup
from src.PageObjects.AboutUsPage import AboutUsPage

class Test_AboutUs(WebDriverSetup):
    def test_aboutus_load(self):
        self.driver.get("https://www.qualitasdigital.com/about-us")
        self.driver.set_page_load_timeout(10)
        about_us_page = AboutUsPage(self.driver)
        print(about_us_page.header_title.text)
        self.assertEqual("Let Us Build Something Together", about_us_page.header_title.text)

    if __name__ == '__main__':
        unittest.main()