from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_in_basket(self):
        button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        button.click()
        self.solve_quiz_and_get_code()

    def should_be_correct_adding_product_name(self):
        product_name = self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME)
        message_about_adding = self.browser.find_element(
            *ProductPageLocators.MESSAGE_ABOUT_ADDING)
        print(product_name.text)
        print(message_about_adding.text)
        assert product_name.text == message_about_adding.text, "No product name in the message"

    def should_be_correct_adding_product_price(self):
        message_basket_total = self.browser.find_element(
            *ProductPageLocators.MESSAGE_BASKET_TOTAL)
        product_price = self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE)
        print(product_price.text)
        print(message_basket_total.text)
        assert product_price.text == message_basket_total.text, "No product price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
