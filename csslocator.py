from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com')

#locator for Create Account page elements

#amazon logo
driver.find_element(By.CSS_SELECTOR, 'a.a-link-nav-icon')

#create Account Header
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#name input field
driver.find_element(By.CSS_SELECTOR, 'input#ap_customer_name.a-input-text.a-span12.auth-autofocus.auth-required-field')

#email input field
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')

#password field
driver.find_element(By.CSS_SELECTOR, 'input#password')

#re-enter password field
driver.find_element(By.CSS_SELECTOR, 'input#ap_password_check')

#continue button
driver.find_element(By.CSS_SELECTOR, 'input#continue.a-button-input')

#condition of use
driver.find_element(By.CSS_SELECTOR, "a[href='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

#notice of privacy
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_register_notification_privacy_notice']")

#sign in
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?openid.pape.max_auth_age']")

