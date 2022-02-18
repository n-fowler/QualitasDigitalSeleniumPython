from src.Locators import *
from src.PageObjects.BasePage import BasePage
from src.Locators.NewsAndNotesPageLocators import NewsAndNotesPageLocators
from selenium.webdriver.common.by import By

class NewsAndNotesPage(BasePage):
    def __init__(self, driver):
        self.locator = NewsAndNotesPageLocators
        super(NewsAndNotesPage, self).__init__(driver)
        self.go_to_url(NewsAndNotesPageLocators.url)

    def validate_load(self):
        self.find_element(*self.locator.logo_image)

    def get_logo_image(self):
        return self.find_element(*self.locator.logo_image)

    def get_entries(self):
        return self.find_elements(*self.locator.entries)

