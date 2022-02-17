from src.Locators import *
from src.PageObjects.BasePage import BasePage
from src.Locators.HomePageLocators import HomePageLocators
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, driver):
        self.locator = HomePageLocators
        super(HomePage, self).__init__(driver)
        self.go_to_url(HomePageLocators.url)

    def validate_load(self):
        self.find_element(*self.locator.logo_image)

    def get_nav_link_texts(self):
        mainNavigation = self.find_element(*self.locator.nav_section)
        linkElements = mainNavigation.find_elements(*self.locator.nav_collection)
        navLinkTexts = []
        for element in linkElements:
            text = element.find_element(By.TAG_NAME, "a").find_element(By.TAG_NAME, "span").get_attribute("innerText")
            if(text != ""):
                navLinkTexts.append(text)
        return navLinkTexts

    def get_nav_link_urls(self):
        mainNavigation = self.find_element(*self.locator.nav_section)
        linkElements = mainNavigation.find_elements(*self.locator.nav_collection)
        navLinkUrls = []
        for element in linkElements:
            text = element.find_element(By.TAG_NAME, "a").get_attribute("href")
            if(text != ""):
                navLinkUrls.append(text)
        return navLinkUrls

    def get_footer_link_texts(self):
        footerNavigation = self.find_element(*self.locator.footer_nav)
        linkElements = footerNavigation.find_elements(*self.locator.nav_collection)
        navLinkTexts = []
        for element in linkElements:
            text = element.find_element(By.TAG_NAME, "a").find_element(By.TAG_NAME, "span").get_attribute("innerText")
            if(text != ""):
                navLinkTexts.append(text)
        return navLinkTexts

    def get_footer_link_urls(self):
        footerNavigation = self.find_element(*self.locator.footer_nav)
        linkElements = footerNavigation.find_elements(*self.locator.nav_collection)
        navLinkUrls = []
        for element in linkElements:
            text = element.find_element(By.TAG_NAME, "a").get_attribute("href")
            if(text != ""):
                navLinkUrls.append(text)
        return navLinkUrls

    def get_nav_toggle(self):
        return self.find_element(*self.locator.nav_toggle)
    def get_nav_tray(self):
        return self.find_element(*self.locator.nav_tray)
    def get_nav_section(self):
        return self.find_element(*self.locator.nav_section)
    def get_nav_collection(self):
        return self.find_elements(*self.locator.nav_collection)
    def get_nav_body_text(self):
        return self.find_element(*self.locator.nav_body_text)
    def get_schedule_button(self):
        return self.find_element(*self.locator.nav_schedule_button)
    def get_search_button(self):
        return self.find_element(*self.locator.search_button)
    def get_search_text_box(self):
        return self.find_element(*self.locator.search_text_box)
    def get_search_result_text(self):
        return self.find_element(*self.locator.search_result_text)
    def get_primary_section_title(self):
        return self.find_element(*self.locator.primary_section_title)
    def get_primary_section_image(self):
        return self.find_element(*self.locator.primary_section_image).find_element(By.TAG_NAME, "img")
    def get_primary_section_body_text(self):
        return self.find_element(*self.locator.primary_section_body_text)
    def get_primary_section_schedule_button(self):
        return self.find_element(*self.locator.primary_section_schedule_button).find_element(By.TAG_NAME, "a")
    def get_our_services_section_title(self):
        return self.find_element(*self.locator.our_services_section_title)
    def get_our_services_section_body_text(self):
        return self.find_element(*self.locator.our_services_section_body_text)
    def get_our_services_section_link(self):
        return self.find_element(*self.locator.our_services_section_link)
    def get_our_commitment_section_title(self):
        return self.find_element(*self.locator.our_commitment_section_title)
    def get_our_commitment_section_body_text(self):
        return self.find_element(*self.locator.our_commitment_section_body_text)
    def get_our_commitment_section_link(self):
        return self.find_element(*self.locator.our_commitment_section_link)
    def get_monthly_articles_section_title(self):
        return self.find_element(*self.locator.monthly_articles_section_title)
    def get_monthly_articles_section_body_text(self):
        return self.find_element(*self.locator.monthly_articles_section_body_text)
    def get_monthly_articles_section_link(self):
        return self.find_element(*self.locator.monthly_articles_section_link)
    def get_secondary_section(self):
        return self.find_element(*self.locator.secondary_section)
    def get_secondary_section_title(self):
        return self.find_element(*self.locator.secondary_section_title)
    def get_secondary_section_image(self):
        return self.find_element(*self.locator.secondary_section_image).find_element(By.TAG_NAME, "img")
    def get_secondary_section_body_text(self):
        return self.find_element(*self.locator.secondary_section_body_text)
    def get_secondary_section_aboutus_button(self):
        return self.find_element(*self.locator.secondary_section_aboutus_button).find_element(By.TAG_NAME, "a")
    def get_mid_page_title(self):
        return self.find_element(*self.locator.mid_page_title)
    def get_tertiary_section(self):
        return self.find_element(*self.locator.tertiary_section)
    def get_tertiary_section_title(self):
        return self.find_element(*self.locator.tertiary_section_title)
    def get_tertiary_section_image(self):
        return self.find_element(*self.locator.tertiary_section_image).find_element(By.TAG_NAME, "img")
    def get_tertiary_section_body_text(self):
        return self.find_element(*self.locator.tertiary_section_body_text)
    def get_tertiary_section_client_testimonials_button(self):
        return self.find_element(*self.locator.tertiary_section_client_testimonials_button).find_element(By.TAG_NAME, "a")
    def get_footer_title(self):
        return self.find_element(*self.locator.footer_title)
    def get_footer_schedule_button(self):
        return self.find_element(*self.locator.footer_schedule_button).find_element(By.TAG_NAME, "a")
    def get_footer_nav(self):
        return self.find_element(*self.locator.footer_nav)
    def get_footer_links_section(self):
        return self.find_element(*self.locator.footer_links_section)
    def get_footer_links_collection(self):
        return self.find_element(*self.locator.footer_links_collection)

