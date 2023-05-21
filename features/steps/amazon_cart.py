from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, 'div#nav-cart-count-container').click()


@then('Verify cart has {expected_count} item')
def verify_cart_item(context,expected_count):
    actual_result = (context.driver.find_element(By.ID, 'nav-cart-count-container')).text
    assert expected_count == actual_result, f'Expected{expected_count},but got{actual_result}'


    #@then('Empty cart page is shown')
#def empty_cart(context):
    #xpected_result = 'Your Amazon Cart is empty'
    #actual_result = context.driver.find_element(By.CSS_SELECTOR, 'div.a-row.sc-your-amazon-cart-is-empty').text

 #   assert actual_result == expected_result, f'Expected {expected_result} but got {actual_result}'















