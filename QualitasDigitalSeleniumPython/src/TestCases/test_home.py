import unittest
from src.TestCases.BaseTest import BaseTest
from src.PageObjects.HomePage import HomePage
from src.TestData.HomePageTestData import HomePageTestData

class Test_Home(BaseTest):
    def test_home_load(self):
        home_page = HomePage(self.driver)
        home_page.validate_load()
    def test_home_navigation(self):
        home_page = HomePage(self.driver)
        nav_collection = home_page.get_nav_collection()
        home_page.get_nav_toggle().click()
        expectedLinkTexts = [
            "Home",
            "About Us",
            "Pricing + Services",
            "FAQ",
            "News + Notes",
            "Testimonials",
            "Schedule Consultation",
            "Contact Us"]
        expectedPageUrls = [
            "https://www.qualitasdigital.com/",
            "https://www.qualitasdigital.com/about-us",
            "https://www.qualitasdigital.com/pricing-services",
            "https://www.qualitasdigital.com/faq",
            "https://www.qualitasdigital.com/news-notes-qualitas",
            "https://www.qualitasdigital.com/testimonials",
            "https://www.qualitasdigital.com/schedule-consultation",
            "https://www.qualitasdigital.com/contact-us"]
        actualLinkTexts = home_page.get_link_texts()
        actualLinkUrls = home_page.get_link_urls()
        self.assertEqual(expectedLinkTexts,actualLinkTexts)
        self.assertEqual(expectedPageUrls,actualLinkUrls)

        expectedNavigationBodyText = "Qualitas Digital brings Software Quality Automation within reach. Our solutions help you bridge the gap between where you are and where you want to be. We help you create Quality Automation programs that scale without the high overhead of a purely manual approach.  Take advantage of a free consultation today."
        self.assertEqual(expectedNavigationBodyText, home_page.get_nav_body_text().get_attribute("innerText"))
        self.assertIsNotNone(home_page.get_primary_section_schedule_button())
        pass
    def test_home_search(self):
        home_page = HomePage(self.driver)
        home_page.get_search_button().click()
        self.assertEqual("Search", home_page.get_search_text_box().get_attribute("placeholder"))
        home_page.get_search_text_box().send_keys("abc")
        home_page.get_search_text_box().submit()
        self.assertEqual("https://www.qualitasdigital.com/search?q=abc", self.driver.current_url)
        self.assertEqual("Your search did not match any documents.", home_page.get_search_result_text().get_attribute("innerText"))
        pass
    def test_home_content(self):
        home_page = HomePage(self.driver)
        pass




