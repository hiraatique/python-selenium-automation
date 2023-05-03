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
driver.get('https://www.amazon.com/sign-in')

#find amazon logo
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")

#find email field
driver.find_element(By.ID, 'ap_email')

#find Continue button
driver.find_element(By.ID, 'continue')

#find need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#forgot your password link
driver.find_element(By.XPATH, "//a[contains(@href,'forgotpassword')]")

#other issues with sign-in
driver.find_element(By.XPATH, "//a[contains(@href, 'account-issue')]")

#Create account button
driver.find_element(By.CLASS_NAME, 'a-button-text')

#condition of use link
driver.find_element(By.XPATH, '//a[contains(@href, "notification_condition_of_use")]')

#Notice of privacy
driver.find_element(By.XPATH, '//a[contains(@href, "notification_privacy_notice")]')
