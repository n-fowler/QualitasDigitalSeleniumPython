from selenium.webdriver.common.by import By

class FaqPageLocators(object):
    url = "faq"
    logo_image = (By.CLASS_NAME, "logo-image")
    header_content = (By.XPATH, "//*[@id='block-0872d1f64aa73dc210a0']/div/h1")
    sidebar_content = (By.XPATH, "//*[@id='block-5a5c2d60498a7ac2f90c']/div/h2")
    contact_us_link = (By.XPATH, "//*[@id='block-5a5c2d60498a7ac2f90c']/div/p/a")
    center_section = (By.ID, "block-07ad9bb3be93b9c67b17")
    left_titles = (By.XPATH, "//*[@id='block-07ad9bb3be93b9c67b17']/div/h3")
    left_bodies = (By.XPATH, "//*[@id='block-07ad9bb3be93b9c67b17']/div/p")
    right_titles = (By.XPATH, "//*[@id='block-156845d943225c44b8dd']/div/h3")
    right_bodies = (By.XPATH, "//*[@id='block-156845d943225c44b8dd']/div/p")