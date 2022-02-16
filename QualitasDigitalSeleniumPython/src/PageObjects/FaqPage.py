from src.Locators import *
from src.PageObjects.BasePage import BasePage
from src.Locators.FaqPageLocators import FaqPageLocators
from selenium.webdriver.common.by import By

class FaqPage(BasePage):
    def __init__(self, driver):
        self.locator = FaqPageLocators
        super(FaqPage, self).__init__(driver)
        self.go_to_url(FaqPageLocators.url)

    def validate_load(self):
        self.find_element(*self.locator.logo_image)

    def get_logo_image(self):
        return self.find_element(*self.locator.logo_image)
    def get_header_content(self):
        return self.find_element(*self.locator.header_content)
    def get_sidebar_content(self):
        return self.find_element(*self.locator.sidebar_content)
    def get_contact_us_link(self):
        return self.find_element(*self.locator.contact_us_link)
    def get_center_section(self):
        return self.find_element(*self.locator.center_section)
    def get_left_titles(self):
        return self.find_elements(*self.locator.left_titles)
    def get_left_bodies(self):
        return self.find_elements(*self.locator.left_bodies)
    def get_right_titles(self):
        return self.find_elements(*self.locator.right_titles)
    def get_right_bodies(self):
        return self.find_elements(*self.locator.right_bodies)

    def get_faq_page_titles(self):
        faq_page_actual_titles = []
        for left_title in self.get_left_titles():
            faq_page_actual_titles.append(left_title)
        for right_title in self.get_right_titles():
            faq_page_actual_titles.append(right_title)
    def get_faq_page_bodies(self):
        faq_page_actual_bodies = []
        for left_body in self.get_left_bodies():
            faq_page_actual_bodies.append(left_body)
        for right_body in self.get_right_bodies():
            faq_page_actual_bodies.append(right_body)