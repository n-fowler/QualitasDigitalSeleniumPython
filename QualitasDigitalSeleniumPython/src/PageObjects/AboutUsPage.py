from src.Locators import *
from src.PageObjects.BasePage import BasePage
from src.Locators.AboutUsPageLocators import AboutUsPageLocators
from selenium.webdriver.common.by import By

class AboutUsPage(BasePage):
    def __init__(self, driver):
        self.locator = AboutUsPageLocators
        super(AboutUsPage, self).__init__(driver)
        self.go_to_url(AboutUsPageLocators.url)

    def validate_load(self):
        self.find_element(*self.locator.logo_image)
    
    def get_header_section(self):
        return self.find_element(*self.locator.header_section)
    def get_header_title(self):
        return self.find_element(*self.locator.header_title)
    def get_title(self):
        return self.find_element(*self.locator.title)
    def get_sidebar(self):
        return self.find_element(*self.locator.sidebar)
    def get_body_text(self):
        return self.find_element(*self.locator.body_text)
    def get_our_services_link(self):
        return self.find_element(*self.locator.our_services_link)
    def get_schedule_consultation_link(self):
        return self.find_element(*self.locator.schedule_consultation_link)
    def get_about_us_image_section(self):
        return self.find_element(*self.locator.about_us_image_section)
    def get_image(self):
        return self.find_element(*self.locator.image).find_element(By.TAG_NAME, "img")