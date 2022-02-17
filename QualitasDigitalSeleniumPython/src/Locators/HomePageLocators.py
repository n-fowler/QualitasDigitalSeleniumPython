from selenium.webdriver.common.by import By

class HomePageLocators(object):
    url = ""
    logo_image = (By.CLASS_NAME, "logo-image")
    nav_toggle = (By.ID, "navToggle")
    nav_tray = (By.ID, "sideTrayWrapper")
    nav_section = (By.ID, "mainNavigation")
    nav_collection = (By.CLASS_NAME, "nav-link--collection")
    nav_body_text = (By.ID, "block-5aa025203dc65c6e55e9")
    nav_schedule_button = (By.ID,"block-d013aff45daaf1868f5b")
    search_button = (By.CLASS_NAME,"header-search")
    search_text_box = (By.CLASS_NAME,"header-search-form-input")
    search_result_text = (By.CLASS_NAME,"sqs-search-page-notice")
    primary_section_title = (By.XPATH, "//*[@id='block-a50c2484babd68ea94ea']/div/h1")
    primary_section_image = (By.CSS_SELECTOR, "div[id^='yui_3_17_2_1'][id$='67']")
    primary_section_body_text = (By.XPATH, "//*[@id='block-f99a4c371dd091271df7']/div/p")
    primary_section_schedule_button = (By.CSS_SELECTOR, "div[id^='yui_3_17_2_1'][id$='133']")
    our_services_section_title = (By.XPATH,"//*[@id='block-9b7a80e3167ce3d3995a']/div/h2")
    our_services_section_body_text = (By.XPATH,"//*[@id='block-9b7a80e3167ce3d3995a']/div/p[1]")
    our_services_section_link = (By.XPATH,"//*[@id='block-9b7a80e3167ce3d3995a']/div/p[2]/a")
    our_commitment_section_title = (By.XPATH,"//*[@id='block-2429c8770ce968f657a8']/div/h2")
    our_commitment_section_body_text = (By.XPATH,"//*[@id='block-2429c8770ce968f657a8']/div/p[1]")
    our_commitment_section_link = (By.XPATH,"//*[@id='block-2429c8770ce968f657a8']/div/p[2]/a")
    monthly_articles_section_title = (By.XPATH,"//*[@id='block-5c47022b53cd95d3d039']/div/h2")
    monthly_articles_section_body_text = (By.XPATH,"//*[@id='block-5c47022b53cd95d3d039']/div/p[1]")
    monthly_articles_section_link = (By.XPATH,"//*[@id='block-5c47022b53cd95d3d039']/div/p[2]/a")
    secondary_section = (By.ID, "block-98c1d846f408c7fae1f8")
    secondary_section_title = (By.CLASS_NAME, "image-title-wrapper")
    secondary_section_image = (By.CSS_SELECTOR, "div[id^='yui_3_17_2_1'][id$='88']")
    secondary_section_body_text = (By.CLASS_NAME, "image-subtitle-wrapper")
    secondary_section_aboutus_button = (By.CLASS_NAME, "image-button-wrapper")
    mid_page_title = (By.ID, "block-036c44c036644d931bc6")
    tertiary_section = (By.ID, "block-6863d26509d4596a922e")
    tertiary_section_title = (By.CLASS_NAME, "image-title-wrapper")
    tertiary_section_image = (By.CSS_SELECTOR, "div[id^='yui_3_17_2_1'][id$='106']")
    tertiary_section_body_text = (By.CLASS_NAME, "image-subtitle-wrapper")
    tertiary_section_client_testimonials_button = (By.CLASS_NAME, "image-button-wrapper")
    footer_title = (By.ID, "block-5694a211d5b58deead3e")
    footer_schedule_button = (By.CSS_SELECTOR, "div[id^='yui_3_17_2_1'][id$='140']")
    footer_nav = (By.ID, "footerNavWrapper")
    footer_links_section = (By.ID, "mainNavigation")
    footer_links_collection = (By.CLASS_NAME, "nav-link--collection")



