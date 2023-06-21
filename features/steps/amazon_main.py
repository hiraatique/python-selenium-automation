from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ORDERS_BTN = (By.ID, 'nav-orders')
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
#FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterMoreOnAmazon a')

@given('Open amazon page')
def open_amazon(context):
    context.app.main_page.open_main_page()


@when('Search for {search_word}')
def search_amazon(context, search_word):
    #context.driver.find_element(*SEARCH_FIELD).send_keys(search_query)
    #context.driver.find_element(*SEARCH_BTN).click()
    context.app.header.search_amazon()




#@then('Verify there are 36 links')
#def verify_link_count(context):
 #   links_count = len(context.driver.find_elements(*FOOTER_LINKS))
#    print(context.driver.find_elements(*FOOTER_LINKS))
 #   assert links_count ==36, f'Expected 36 links, but got {links_count}'

