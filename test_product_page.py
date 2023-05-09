import time

from pages.product_page import ProductPage
import pytest

num_promo = [pytest.param(num, marks=pytest.mark.xfail) if num == 7 else num for num in range(10)]


@pytest.mark.parametrize('num', num_promo)
def test_guest_can_add_product_to_basket(browser, num):
    link = f"http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=offer{num}"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    browser.implicitly_wait(3)
    page.should_be_the_same_names()
    page.should_be_the_same_prices()


