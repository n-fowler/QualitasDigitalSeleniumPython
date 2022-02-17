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
        actualLinkTexts = home_page.get_nav_link_texts()
        actualLinkUrls = home_page.get_nav_link_urls()
        self.assertEqual(expectedLinkTexts,actualLinkTexts)
        self.assertEqual(expectedPageUrls,actualLinkUrls)

        expectedNavigationBodyText = "Qualitas Digital brings Software Quality Automation within reach. Our solutions help you bridge the gap between where you are and where you want to be. We help you create Quality Automation programs that scale without the high overhead of a purely manual approach.  Take advantage of a free consultation today."
        self.assertEqual(expectedNavigationBodyText, home_page.get_nav_body_text().get_attribute("innerText"))
        self.assertIsNotNone(home_page.get_primary_section_schedule_button())
    def test_home_search(self):
        home_page = HomePage(self.driver)
        home_page.get_search_button().click()
        self.assertEqual("Search", home_page.get_search_text_box().get_attribute("placeholder"))
        home_page.get_search_text_box().send_keys("abc")
        home_page.get_search_text_box().submit()
        self.assertEqual("https://www.qualitasdigital.com/search?q=abc", self.driver.current_url)
        self.assertEqual("Your search did not match any documents.", home_page.get_search_result_text().get_attribute("innerText"))
    def test_home_content(self):
        home_page = HomePage(self.driver)

        #validate primary section
        self.assertEqual(HomePageTestData.primary_section_title, home_page.get_primary_section_title().get_attribute("innerText"))
        self.assertIn(HomePageTestData.primary_section_image_src, home_page.get_primary_section_image().get_attribute("src"))
        self.assertEqual(HomePageTestData.primary_section_body_text, home_page.get_primary_section_body_text().get_attribute("innerText"))
        self.assertEqual(HomePageTestData.primary_section_schedule_button_link, home_page.get_primary_section_schedule_button().get_attribute("href"))

        #validate Our Services Section
        self.assertEqual(HomePageTestData.our_services_section_title, home_page.get_our_services_section_title().get_attribute("innerText"))
        self.assertEqual(HomePageTestData.our_services_section_body_text, home_page.get_our_services_section_body_text().get_attribute("innerText"))
        self.assertEqual(HomePageTestData.our_services_section_link, home_page.get_our_services_section_link().get_attribute("href"))

        #Validate Our Commitment section
        self.assertEqual(HomePageTestData.our_commitment_section_title, home_page.get_our_commitment_section_title().get_attribute("innerText"))
        self.assertEqual(HomePageTestData.our_commitment_section_body_text, home_page.get_our_commitment_section_body_text().get_attribute("innerText"))
        self.assertEqual(HomePageTestData.our_commitment_section_link, home_page.get_our_commitment_section_link().get_attribute("href"))

        #Validate Monthly Articles section
        self.assertEqual(HomePageTestData.monthly_articles_Section_title, home_page.get_monthly_articles_section_title().get_attribute("innerText"))
        self.assertEqual(HomePageTestData.monthly_articles_section_body_text, home_page.get_monthly_articles_section_body_text().get_attribute("innerText"))
        self.assertEqual(HomePageTestData.monthly_articles_section_link, home_page.get_monthly_articles_section_link().get_attribute("href"))

        #Validate secondary section
        self.assertEqual(HomePageTestData.secondary_section_title, home_page.get_secondary_section_title().get_attribute("innerText"))
        self.assertIn(HomePageTestData.secondary_section_image_src, home_page.get_secondary_section_image().get_attribute("src"))
        self.assertEqual(HomePageTestData.secondary_section_body_text, home_page.get_secondary_section_body_text().get_attribute("innerText").replace("\r", "").replace("\n", ""))
        self.assertEqual(HomePageTestData.secondary_section_aboutus_button_link, home_page.get_secondary_section_aboutus_button().get_attribute("href"))

        #Validate mid page title
        self.assertEqual(HomePageTestData.midpage_title, home_page.get_mid_page_title().get_attribute("innerText"))

        #Validate tertiary section
        self.assertEqual(HomePageTestData.tertiary_section_title, home_page.get_tertiary_section_title().get_attribute("innerText"))
        self.assertIn(HomePageTestData.tertiary_section_image_src, home_page.get_tertiary_section_image().get_attribute("src"))
        self.assertEqual(HomePageTestData.tertiary_section_body_text, home_page.get_tertiary_section_body_text().get_attribute("innerText"))
        self.assertEqual(HomePageTestData.tertiary_section_client_testimonials_button_link, home_page.get_tertiary_section_client_testimonials_button().get_attribute("href"))

        #Validate footer
        self.assertEqual(HomePageTestData.footer_title, home_page.get_footer_title().get_attribute("innerText"))
        self.assertEqual(HomePageTestData.footer_schedule_button_link, home_page.get_footer_schedule_button().get_attribute("href"))

        #Verify footer expected link texts and urls
        expectedLinkTexts = [
            "Our Commitment",
            "Terms + Conditions"]
        expectedPageUrls = [
            "https://www.qualitasdigital.com/our-commitment",
            "https://www.qualitasdigital.com/terms-conditions"]
        actualLinkTexts = home_page.get_footer_link_texts()
        actualLinkUrls = home_page.get_footer_link_urls()
        self.assertEqual(expectedLinkTexts,actualLinkTexts)
        self.assertEqual(expectedPageUrls,actualLinkUrls)
