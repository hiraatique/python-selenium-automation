from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()



@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088")


@when('Store original windows')
def store_original_windows(context):
    context.original_window = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice')
def click_amazon_privacy_notice(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='/privacy']").click()


@when('Switch to the newly opened window')
def switch_newly_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    all_windows = context.driver.current_window_handle
    context.driver.switch_to.window(switch_newly_window)
    context.driver.switch_to.window(all_windows[1])


@then('Verify Amazon Privacy page is opened')
def verify_amazon_privacy_page_open(context):
    assert "Amazon Privacy Notice" in driver.title


@then('User can close new window and switch back to original')
def user_close(context):
    context.driver.close()
    context.original_window = context.driver.current_window_handle










