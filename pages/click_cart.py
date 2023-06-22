from selenium.webdriver.common.by import By
from pages.base_page import Page


class click_cart(Page):
    CLICK_CART = (By.CSS_SELECTOR, 'div#nav-cart-count-container')

    def empty_cart(self, expected_result):
        self.verify_text(expected_result, *self.CLICK_CART)





