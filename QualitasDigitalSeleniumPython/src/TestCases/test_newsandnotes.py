import unittest
from src.TestCases.BaseTest import BaseTest
from src.PageObjects.NewsAndNotesPage import NewsAndNotesPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_NewsAndNotes(BaseTest):
    def test_newsandnotes_load(self):
        newsandnotes_page = NewsAndNotesPage(self.driver)
        newsandnotes_page.validate_load()
    def test_newsandnotes_content(self):
        newsandnotes_page = NewsAndNotesPage(self.driver)

        #There should be at least one article
        self.assertTrue(len(newsandnotes_page.get_entries()) >= 1)

        #It should have a date
        self.assertIsNotNone(newsandnotes_page.get_entries()[0].find_element(By.CLASS_NAME, "date-wrapper"))

        #It should have a clickable title
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "entry-title")))
        entryLink = newsandnotes_page.get_entries()[0].find_element(By.CLASS_NAME, "entry-title").find_element(By.TAG_NAME, "a")
        self.assertIsNotNone(entryLink)
        self.assertNotEqual("", entryLink.get_attribute("href"))
        self.assertNotEqual("", entryLink.text)

        #It should have a clickable category
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "blog-categories")))
        entryCategory = newsandnotes_page.get_entries()[0].find_element(By.CLASS_NAME, "blog-categories").find_element(By.TAG_NAME, "a")
        self.assertIsNotNone(entryCategory)
        self.assertNotEqual("", entryCategory.get_attribute("href"))
        self.assertNotEqual("", entryCategory.text)

        #It should have a summary body
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "entry-excerpt")))
        entryExcerpt = newsandnotes_page.get_entries()[0].find_element(By.CLASS_NAME, "entry-excerpt").find_element(By.TAG_NAME, "p")
        self.assertIsNotNone(entryExcerpt)
        self.assertNotEqual("", entryExcerpt.text)




