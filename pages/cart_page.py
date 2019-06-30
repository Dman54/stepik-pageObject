from .base_page import BasePage
# from selenium.webdriver.common.by import By
from .locators import CartPageLocators
# from .login_page import LoginPage


class CartPage(BasePage):
    # def should_be_empty_basket(self):
    #     self.should_not_be_products_in_the_basket()
    #     self.shout_be_text_about_basket_is_empty()

    def should_not_be_products_in_the_basket(self):
        assert self.is_not_element_present(
            *CartPageLocators.BASKET_ITEMS), "Success message is presented, but should not be"

    def shout_be_text_about_basket_is_empty(self):
        text_message_in_basket = self.browser.find_element(
            *CartPageLocators.MESSAGE_IN_BASKET).text
        assert "Your basket is empty" in text_message_in_basket, "The message that basket is empty not exist"
