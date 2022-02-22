from src.Locators import *
from src.PageObjects.BasePage import BasePage
from src.Locators.ScheduleConsultationPageLocators import ScheduleConsultationPageLocators
from selenium.webdriver.common.by import By

class ScheduleConsultationPage(BasePage):
    def __init__(self, driver):
        self.locator = ScheduleConsultationPageLocators
        super(ScheduleConsultationPage, self).__init__(driver)
        self.go_to_url(ScheduleConsultationPageLocators.url)

    def validate_load(self):
        self.find_element(*self.locator.logo_image)

    def get_header_content(self):
        return self.find_element(*self.locator.header_content)
    def get_left_content(self):
        return self.find_element(*self.locator.left_content)
    def get_our_commitment_link(self):
        return self.find_element(*self.locator.our_commitment_link)
    def get_faq_link(self):
        return self.find_element(*self.locator.faq_link)
    def get_terms_and_conditions_link(self):
        return self.find_element(*self.locator.terms_and_conditions_link)
    def get_schedule_consultation_button(self):
        return self.find_element(*self.locator.schedule_consultation_button)
    def get_schedule_consultation_button_link(self):
        return self.get_schedule_consultation_button().find_element(*self.locator.schedule_consultation_button_link)




