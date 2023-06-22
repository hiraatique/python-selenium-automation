from selenium.webdriver.common.by import By
from pages.base_page import Page


class Header(Page):
    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    ORDER_BTN = (By.ID, 'nav-orders')
    CLICK_CART = (By.CSS_SELECTOR, 'div#nav-cart-count-container')

    def search_amazon(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_orders(self):
        self.click(*self.ORDER_BTN)

    def click_cart_icon(self):
        self.click(*self.CLICK_CART)




