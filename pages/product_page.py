import math

from selenium.common import NoAlertPresentException

from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        login_link = self.browser.find_element(*ProductPageLocators.BUY_BUTTON)
        login_link.click()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.BUY_BUTTON), "Button isn't presented"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def should_be_the_same_names(self):
        page_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        basket_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME_IN_BASKET).text
        assert page_name == basket_name, "names are different"

    def should_be_the_same_prices(self):
        page_price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_BASKET).text
        assert page_price == basket_price, "prices are different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_should_dissapear(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE) == True, \
            "Success message is not dissapeared, but should be"
