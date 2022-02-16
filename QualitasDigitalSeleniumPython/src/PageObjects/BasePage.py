from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage(object):
    def __init__(self, driver, base_url='https://www.qualitasdigital.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def go_to_url(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_url(self):
        return self.driver.current_url

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        except TimeoutException:
            print("\n * Element not found within the given time. --> %s" %(locator[1]))
            self.driver.quit()




