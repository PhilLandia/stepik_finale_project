from stepik_finale_project.pages.base_page import BasePage
from .locators import BasePageLocators


# класс для работы с главной страницей сайта
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    # перейти в корзину
    def go_to_the_basket(self):
        basket_button = self.browser.find_element(*BasePageLocators.VIEW_BASKET_BTN)
        basket_button.click()

    # переход на страницу с формой авторизации
    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    # проверка на наличие ссылки на страницу логина
    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"
