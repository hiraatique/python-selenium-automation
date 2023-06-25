from selenium.webdriver.common.by import By
from pages.base_page import Page


class click_cart(Page):
    CLICK_CART = (By.CSS_SELECTOR, 'div#nav-cart-count-container')
    EMPTY_CART = (By.XPATH, "//div[@class='a-row sc-your-amazon-cart-is-empty']")

    def empty_cart(self):
        self.verify_is_displayed(*self.EMPTY_CART)
        print('Amazon Cart is empty')







