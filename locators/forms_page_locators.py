from selenium.webdriver.common.by import By

PRACTICE_FORM = (By.XPATH, "//span[text()='Practice Form']")
FIRST_NAME_FIELD = (By.CSS_SELECTOR, "#firstName")
LAST_NAME_FIELD = (By.CSS_SELECTOR, "#lastName")
PHONE_FIELD = (By.CSS_SELECTOR, "#userNumber")
GENDER_MALE = (By.XPATH, "//div[@id='genterWrapper']//input[@value='Male']/..")
GENDER_FEMALE = (By.XPATH, "//div[@id='genterWrapper']//input[@value='Female']/..")
GENDER_OTHER = (By.XPATH, "//div[@id='genterWrapper']//input[@value='Other']/..")
SUBMIT_BUTTON = (By.CSS_SELECTOR, "button#submit")


NAME_ON_WINDOW_OF_SUBMITTED_DATA = (By.XPATH, "//td[text()='Student Name']/../td[2]")
PHONE_ON_WINDOW_OF_SUBMITTED_DATA = (By.XPATH, "//td[text()='Mobile']/../td[2]")
GENDER_ON_WINDOW_OF_SUBMITTED_DATA = (By.XPATH, "//td[text()='Gender']/../td[2]")
