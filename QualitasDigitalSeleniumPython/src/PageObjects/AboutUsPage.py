from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class AboutUsPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.qualitasdigital.com/about-us"
        self.logo_image = driver.find_element_by_class_name("logo-image")
        self.header_section = driver.find_element_by_id("block-8d07de855042f0a5360c")
        self.header_title = driver.find_element_by_xpath("//*[@id='block-8d07de855042f0a5360c']/div/h1")
        self.title = driver.find_element_by_xpath("//*[@id='block-54dfc3255ea4a1352072']/div/h2")
        self.sidebar = driver.find_elements_by_xpath("//*[@id='block-54dfc3255ea4a1352072']/div/p") 
        self.body_text = self.sidebar[0]
        self.sidebar_links = self.sidebar[1].find_elements_by_tag_name("a")
        self.our_services_link = self.sidebar_links[0]
        self.schedule_consultation_link = self.sidebar_links[1]
        self.about_us_image_section = driver.find_element_by_id("block-5347679b4da120838be3")





