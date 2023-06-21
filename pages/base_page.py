class Page:
    def __init__(self, driver):
        self.driver = driver

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def open_page(self, url):
        self.driver.get(url)

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def verify_text(self, expected_text, *locator):
      actual_text = self.driver.find_element(*locator).text
      assert expected_text == actual_text, f'Error! Expected {expected_text} but got actual {actual_text}'

