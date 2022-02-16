from src.Locators import *
from src.PageObjects.BasePage import BasePage
from src.Locators.ContactUsPageLocators import ContactUsPageLocators
from selenium.webdriver.common.by import By

class ContactUsPage(BasePage):
    def __init__(self, driver):
        self.locator = ContactUsPageLocators
        super(ContactUsPage, self).__init__(driver)
        self.go_to_url(ContactUsPageLocators.url)
        
    def validate_load(self):
        self.find_element(*self.locator.logo_image)

    def get_header_content(self):
        return self.find_element(*self.locator.header_content)
    def get_sidebar_content(self):
        return self.find_element(*self.locator.sidebar_content)
    def get_sidebar_links(self):
        return self.find_element(*self.locator.sidebar_links)
    def get_our_commitment_link(self):
        return self.find_element(*self.locator.our_commitment_link)
    def get_faq_link(self):
        return self.find_element(*self.locator.faq_link)
    def get_terms_and_conditions_link(self):
        return self.find_element(*self.locator.terms_and_conditions_link)
    def get_form_section(self):
        return self.find_element(*self.locator.form_section)
    def get_first_name_field(self):
        return self.find_element(*self.locator.first_name_field)
    def get_last_name_field(self):
        return self.find_element(*self.locator.last_name_field)
    def get_email_field(self):
        return self.find_element(*self.locator.email_field)
    def get_checkbox_section(self):
        return self.find_element(*self.locator.checkbox_section)
    def get_additional_message_text_area(self):
        return self.find_element(*self.locator.additional_message_text_area)
    def get_submit_button(self):
        return self.find_element(*self.locator.submit_button).find_element(By.TAG_NAME, "input")


