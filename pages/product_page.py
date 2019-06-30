from .base_page import BasePage
# from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
import time


class ProductPage(BasePage):
    def should_be_product_in_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()
        time.sleep(10)

    def should_be_correct_adding_product_name(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME)
        message_about_adding = self.browser.find_element(
            *ProductPageLocators.MESSAGE_ABOUT_ADDING)
        # assert product_name, "Product name is not presented"
        # assert message_about_adding, "Message about adding is not presented"
        print(product_name.text)
        print(message_about_adding.text)
        assert product_name.text == message_about_adding.text, "No product name in the message"

    def should_be_correct_adding_product_price(self):
        message_basket_total = self.browser.find_element(
            *ProductPageLocators.MESSAGE_BASKET_TOTAL)
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE)
        # assert message_basket_total, "Message basket total is not presented"
        # assert product_price, "Product price is not presented"
        print(product_price.text)
        print(message_basket_total.text)
        assert product_price.text == message_basket_total.text, "No product price in the message"
