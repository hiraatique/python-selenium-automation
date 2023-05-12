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

driver.find_element(By.CSS_SELECTOR, 'div#nav-cart-count-container').click()

expected_result = 'Your Amazon Cart is empty'
actual_result = driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text

assert actual_result == expected_result, f'Expected {expected_result} but got {actual_result}'

driver.quit()

print('Test case Passed')


