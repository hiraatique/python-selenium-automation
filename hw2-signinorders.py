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
driver.find_element(By.ID, 'nav-orders').click()

sleep(5)

#verify sign-in header visiblity
header_text = driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text


#verify email input field
input_id = driver.find_element(By.XPATH, "//input[@id='ap_email']").id

found_input_email = False
if input_id != '':
    found_input_email = True

Expected_Result_1 = 'Sign in'
Actual_Result_1 = header_text
assert Expected_Result_1 == Actual_Result_1


Expected_Result_2 = True
Actual_Result_2 = found_input_email
assert Expected_Result_2 == Actual_Result_2, 'test failed'
driver.quit()
print('test case passed')










