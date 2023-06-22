from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL = (By.XPATH, "//input[@id='ap_email']")
ORDER_BTN = (By.ID, 'nav-orders')


@when('Click on orders')
def click_order(context):
    context.app.header.click_orders()


#@when('Verify sign-in header')
#def signin_header(context):
    #expected_result = 'Sign in'
    #actual_result = context.driver.find_element(*SIGNIN_HEADER).text

    #assert actual_result == expected_result


@then('Verify Sign In Page opens')
def verify_signin_opens(context):
    context.app.sign_in_page.verify_signin_opens()


