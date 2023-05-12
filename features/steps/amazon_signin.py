from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@when('Click on orders')
def click_order(context):
    context.driver.find_element(By.ID, 'nav-orders').click()



@when('Verify sign-in header')
def signin_header(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']").text

    assert actual_result == expected_result


@then('Verify input field is present')
def verify_inputfield(context):
    input_id = context.driver.find_element(By.XPATH, "//input[@id='ap_email']")

    assert input_id.is_displayed(), 'Element not found'



