from src.Locators import *
from src.PageObjects.BasePage import BasePage
from src.Locators.TestimonialsPageLocators import TestimonialsPageLocators
from selenium.webdriver.common.by import By

class TestimonialsPage(BasePage):
    def __init__(self, driver):
        self.locator = TestimonialsPageLocators
        super(TestimonialsPage, self).__init__(driver)
        self.go_to_url(TestimonialsPageLocators.url)

    def validate_load(self):
        self.find_element(*self.locator.logo_image)

    def get_highlighted_review_content(self):
        return self.find_element(*self.locator.highlighted_review_content)
    def get_highlighted_review_author(self):
        return self.find_element(*self.locator.highlighted_review_author)
    def get_midpage_title(self):
        return self.find_element(*self.locator.midpage_title)
    def get_review_one_content(self):
        return self.find_element(*self.locator.review_one_content)
    def get_review_one_author(self):
        return self.find_element(*self.locator.review_one_author)
    def get_review_two_content(self):
        return self.find_element(*self.locator.review_two_content)
    def get_review_two_author(self):
        return self.find_element(*self.locator.review_two_author)
    def get_review_three_content(self):
        return self.find_element(*self.locator.review_three_content)
    def get_review_three_author(self):
        return self.find_element(*self.locator.review_three_author)
    def get_review_four_content(self):
        return self.find_element(*self.locator.review_four_content)
    def get_review_four_author(self):
        return self.find_element(*self.locator.review_four_author)
    def get_review_five_content(self):
        return self.find_element(*self.locator.review_five_content)
    def get_review_five_author(self):
        return self.find_element(*self.locator.review_five_author)




