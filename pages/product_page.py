from stepik_finale_project.pages.base_page import BasePage
from .locators import BasketPageLocators
from .locators import ProductPageLocators


# класс для работы со страницей продукта
class ProductPage(BasePage):
    # добавить предмет в корзину
    def add_item_to_basket_button(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.BASKET_ADD_BTN)
        add_to_basket_button.click()

    # проверка на наличие кнопки добавить в корзину
    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_ADD_BTN), "Add to Basket button is not presented"

    # проверка на наличие уведомления об успешном добавлении в корзину
    def should_be_success_alert(self):
        assert self.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS), "Success message is presented"

    # проверка на исчезновение уведомления об успешном добавлении в корзину
    def success_alert_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.ALERT_SUCCESS), "Success message is not disappeared"

    # проверка на наличие предмета в корзине
    def should_item_in_basket(self):
        self.should_cost_equal()
        self.should_name_equal()

    # проверка на одинаковую стоимость товара и товара в корзине
    def should_cost_equal(self):
        item_basket_cost = self.browser.find_element(*BasketPageLocators.BASKET_TOTAL)
        item_product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert item_basket_cost.text == item_product_cost.text, "Prices in Basket and in product page isn't equal"

    # проверка на одинаковое наименование товара и товара в корзине
    def should_name_equal(self):
        items_strong = self.browser.find_elements(*BasketPageLocators.BASKET_STRONG_NAMES)
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        names_equal = False
        for item_strong in items_strong:
            if item_strong.text == product_name:
                names_equal = True
        assert names_equal, "Names of product isn't equal"
