from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//span[@data-component-type='s-search-results']//a[.//span[@class='a-price']]")
PRODUCT_NAME = (By.CSS_SELECTOR, "#sc-active-cart li")


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()


@then('Verify search results for {expected_result} are shown')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    assert expected_result == actual_result, f'Error! Actual text {actual_result} does not match'












