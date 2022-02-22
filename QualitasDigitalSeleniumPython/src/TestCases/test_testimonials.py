import unittest
from src.TestCases.BaseTest import BaseTest
from src.PageObjects.TestimonialsPage import TestimonialsPage
from src.TestData.TestimonialsPageTestData import TestimonialsPageTestData
from selenium.webdriver.common.by import By

class Test_Testimonials(BaseTest):
    def test_testimonials_load(self):
        testimonials_page = TestimonialsPage(self.driver)
        testimonials_page.validate_load()
    def test_testimonials_content(self):
        testimonials_page = TestimonialsPage(self.driver)

        #There should be a centered review in green #0d5
        self.assertEqual(TestimonialsPageTestData.highlighted_review_content, testimonials_page.get_highlighted_review_content().get_attribute("innerText"))
        self.assertEqual("rgba(0, 221, 85, 1)", testimonials_page.get_highlighted_review_content().get_attribute("color"))
        self.assertEqual(TestimonialsPageTestData.highlighted_review_author, testimonials_page.get_highlighted_review_author().get_attribute("innerText"))
        self.assertEqual("rgba(0, 221, 85, 0.6)", testimonials_page.get_highlighted_review_author().get_attribute("color"))

        #There should be a mid page title 'Others have had this to say...
        self.assertEqual(TestimonialsPageTestData.mid_page_title, testimonials_page.get_midpage_title().get_attribute("innerText"))

        #The mid page title isn't the same color as the highlighted review
        self.assertNotEqual("rgba(0, 221, 85, 1)", testimonials_page.get_midpage_title().get_attribute("color"))

        #Validate that the color of linked in review elements isn't the same as the highlighted review
        self.assertNotEqual("rgba(0, 221, 85, 1)", testimonials_page.get_review_one_content().get_attribute("color"))
        self.assertNotEqual("rgba(0, 221, 85, 1)", testimonials_page.get_review_two_content().get_attribute("color"))
        self.assertNotEqual("rgba(0, 221, 85, 1)", testimonials_page.get_review_three_content().get_attribute("color"))
        self.assertNotEqual("rgba(0, 221, 85, 1)", testimonials_page.get_review_four_content().get_attribute("color"))
        self.assertNotEqual("rgba(0, 221, 85, 1)", testimonials_page.get_review_five_content().get_attribute("color"))

        #There should be five linked in based reviews that also aren't in green
        self.assertEqual(TestimonialsPageTestData.review_one_content, testimonials_page.get_review_one_content().get_attribute("innerText"))
        self.assertEqual(TestimonialsPageTestData.review_one_author, testimonials_page.get_review_one_author().get_attribute("innerText"))
        self.assertEqual(TestimonialsPageTestData.review_two_content, testimonials_page.get_review_two_content().get_attribute("innerText"))
        self.assertEqual(TestimonialsPageTestData.review_two_author, testimonials_page.get_review_two_author().get_attribute("innerText"))
        self.assertEqual(TestimonialsPageTestData.review_three_content, testimonials_page.get_review_three_content().get_attribute("innerText"))
        self.assertEqual(TestimonialsPageTestData.review_three_author, testimonials_page.get_review_three_author().get_attribute("innerText"))
        self.assertEqual(TestimonialsPageTestData.review_four_content, testimonials_page.get_review_four_content().get_attribute("innerText"))
        self.assertEqual(TestimonialsPageTestData.review_four_author, testimonials_page.get_review_four_author().get_attribute("innerText"))
        self.assertEqual(TestimonialsPageTestData.review_five_content, testimonials_page.get_review_five_content().get_attribute("innerText"))
        self.assertEqual(TestimonialsPageTestData.review_five_author, testimonials_page.get_review_five_author().get_attribute("innerText"))



