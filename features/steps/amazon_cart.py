from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div#nav-cart-count-container').click()


@then('Empty cart page is shown')
def empty_cart(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text

    assert actual_result == expected_result, f'Expected {expected_result} but got {actual_result}'















