from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class selenium_extensions:
    def find_element_by_class_name(driver, class_name):
        return driver.find_element_by_class_name