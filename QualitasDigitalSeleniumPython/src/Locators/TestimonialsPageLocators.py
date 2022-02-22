from selenium.webdriver.common.by import By

class TestimonialsPageLocators(object):
    url = "testimonials"
    logo_image = (By.CLASS_NAME, "logo-image")
    highlighted_review_content = (By.XPATH, "//*[@id='block-af6af313004c75816482']/div/figure/blockquote")
    highlighted_review_author = (By.XPATH, "//*[@id='block-af6af313004c75816482']/div/figure/figcaption")
    midpage_title = (By.XPATH, "//*[@id='block-797e974aa3c773f59547']/div/h1")
    review_one_content = (By.XPATH, "//*[@id='block-3f00d4aac80b3b685ab4']/div/p")
    review_one_author = (By.XPATH, "//*[@id='block-3f00d4aac80b3b685ab4']/div/h3")
    review_two_content = (By.XPATH, "//*[@id='block-d4ed1102416f802aa412']/div/p")
    review_two_author = (By.XPATH, "//*[@id='block-d4ed1102416f802aa412']/div/h3")
    review_three_content = (By.XPATH, "//*[@id='block-21f65fd856a855645486']/div/p")
    review_three_author = (By.XPATH, "//*[@id='block-21f65fd856a855645486']/div/h3")
    review_four_content = (By.XPATH, "//*[@id='block-4e70a0e5d8b1842d6a94']/div/p")
    review_four_author = (By.XPATH, "//*[@id='block-4e70a0e5d8b1842d6a94']/div/h3")
    review_five_content = (By.XPATH, "//*[@id='block-3b57590e10d83c5450ee']/div/p")
    review_five_author = (By.XPATH, "//*[@id='block-3b57590e10d83c5450ee']/div/h3")




