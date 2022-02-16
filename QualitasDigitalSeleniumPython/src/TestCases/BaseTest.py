import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class BaseTest(unittest.TestCase):
    def setUp(self):
        options = Options()
        #options.add_argument('headless')
        options.add_argument('window-size=1920,1080')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(10000)
        self.driver.get("https://www.qualitasdigital.com/")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=1).run(suite)




