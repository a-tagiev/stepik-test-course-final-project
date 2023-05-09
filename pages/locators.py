from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    BUY_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRICE_VALUE = (By.CLASS_NAME, "price_color")
    BOOK_NAME = (By.TAG_NAME, "h1")
    BOOK_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) > .alertinner > strong")
    PRODUCT_PRICE_BASKET = (By.CSS_SELECTOR, "p.price_color")
    BOOK_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
