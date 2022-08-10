from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators


# класс для работы на странице корзины сайта
class BasketPage(BasePage):
    # общая проверка на пустую корзину
    def should_be_empty_basket(self):
        self.should_be_no_items()
        self.should_be_label_basket_is_empty()

    # проверка на наличие кнопки просмотреть корзину
    def should_be_button_view_basket(self):
        assert self.is_element_present(*BasePageLocators.VIEW_BASKET_BTN), "View Basket button is not presented"

    # проверка на пустую корзину
    def should_be_no_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_WITH_ITEMS), "Items isn`t in basket"

    # проверка на наличие текста о пустой корзине
    def should_be_label_basket_is_empty(self):
        assert self.browser.find_element(*BasketPageLocators.LABEL_BASKET_IS_EMPTY).text == "Your basket is empty. " \
                                                                                            "Continue shopping"
