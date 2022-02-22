from selenium.webdriver.common.by import By

class ScheduleConsultationPageLocators(object):
    url = "schedule-consultation"
    logo_image = (By.CLASS_NAME, "logo-image")
    header_content = (By.XPATH, "//*[@id='block-540803d1406a17b6338b']/div/h1")
    left_content = (By.XPATH, "//*[@id='block-6bcc55f9ff3b7b21fdea']/div/h2/em")
    our_commitment_link = (By.XPATH, "//*[@id='block-6bcc55f9ff3b7b21fdea']/div/p/a[1]")
    faq_link = (By.XPATH, "//*[@id='block-6bcc55f9ff3b7b21fdea']/div/p/a[2]")
    terms_and_conditions_link = (By.XPATH, "//*[@id='block-6bcc55f9ff3b7b21fdea']/div/p/a[3]")
    schedule_consultation_button = (By.CSS_SELECTOR, "div[id^='yui_3_17_2_1'][id$='76']")
    schedule_consultation_button_link = (By.TAG_NAME, "a")




