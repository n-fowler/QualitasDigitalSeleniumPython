from selenium.webdriver.common.by import By

class ContactUsPageLocators(object):
    url = "contact-us"
    logo_image = (By.CLASS_NAME, "logo-image")
    header_content = (By.XPATH, "//*[@id='block-66e658da5d8a61ea0d14']/div/h1")
    sidebar_content = (By.XPATH, "//*[@id='block-ef19513355911ef99e33']/div/h2")
    sidebar_links = (By.XPATH, "//*[@id='block-ef19513355911ef99e33']/div/p/a")
    our_commitment_link = (By.XPATH, "//*[@id='block-ef19513355911ef99e33']/div/p/a[1]")
    faq_link = (By.XPATH, "//*[@id='block-ef19513355911ef99e33']/div/p/a[2]")
    terms_and_conditions_link = (By.XPATH, "//*[@id='block-ef19513355911ef99e33']/div/p/a[3]")
    form_section = (By.ID, "block-1d7f70b9528dd074da0a")
    first_name_field = (By.NAME, "fname")
    last_name_field = (By.NAME, "lname")
    email_field = (By.NAME, "email")
    checkbox_section = (By.CSS_SELECTOR, "fieldset[id^='checkbox-yui_3_17_2_1'][id$='22390']")
    additional_message_text_area = (By.CSS_SELECTOR, "textarea[id^='textarea-yui_3_17_2_1'][id$='67663-field']")
    submit_button = (By.CLASS_NAME, "form-button-wrapper")


