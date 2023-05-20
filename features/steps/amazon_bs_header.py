from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

HEADER_LINKS = (By.CSS_SELECTOR, '#zg_header a')


@given('Open amazon Best Sellers page')
def open_amazon_bestseller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@then('Verify there are 5 links')
def verify_links(context):
    links_count = len(context.driver.find_elements(*HEADER_LINKS))
    assert links_count == 5, f'Expected 5 links, but got {links_count}'
    print("Test passed")
