from selenium.webdriver.common.by import By

class AboutUsPageLocators(object):
    url = "about-us"
    logo_image = (By.CLASS_NAME, "logo-image")
    header_section = (By.ID, "block-8d07de855042f0a5360c")
    header_title = (By.XPATH, "//*[@id='block-8d07de855042f0a5360c']/div/h1")
    title = (By.XPATH, "//*[@id='block-54dfc3255ea4a1352072']/div/h2")
    sidebar = (By.XPATH, "//*[@id='block-54dfc3255ea4a1352072']/div/p") 
    body_text = (By.XPATH, "//*[@id='block-54dfc3255ea4a1352072']/div/p[1]")
    our_services_link = (By.XPATH, "//*[@id='block-54dfc3255ea4a1352072']/div/p[2]/a[1]")
    schedule_consultation_link = (By.XPATH, "//*[@id='block-54dfc3255ea4a1352072']/div/p[2]/a[2]")
    about_us_image_section = (By.ID,"block-5347679b4da120838be3")
    image = (By.CSS_SELECTOR, "div[id^='yui_3_17_2_1'][id$='68']")