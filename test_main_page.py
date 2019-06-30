from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage

'''
def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    page.open()                      # открываем страницу
    #     page.go_to_login_page() # выполняем метод страницы - переходим на страницу логина
    page.should_be_login_link()
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
'''


# def test_guest_can_go_to_login_link(browser):
#     link = "http://selenium1py.pythonanywhere.com"
#     page = MainPage(browser, link)
#     page.open()

#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)
#     login_page.should_be_login_page()

#     # login_page = page.go_to_login_page()
#     # login_page.should_be_login_page()


def test_guest_cant_see_product_in_cart_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = CartPage(browser, browser.current_url)
    basket_page.should_not_be_products_in_the_basket()
    basket_page.shout_be_text_about_basket_is_empty
