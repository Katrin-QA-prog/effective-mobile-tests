from playwright.sync_api import expect
from .base_page import BasePage

class MainPage(BasePage):
    BASE_URL = "https://effective-mobile.ru/"
#локаторы
    def link_about(self):
        return self.page.get_by_role("link", name="[ О нас ]")

    def link_services(self):
        return self.page.get_by_role("link", name="[ Услуги ]")

    def link_projects(self):
        return self.page.get_by_role("link", name="[ Проекты ]")

    def link_reviews(self):
        return self.page.get_by_role("link", name="[ Отзывы ]")

    def link_contacts(self):
        return self.page.get_by_role("link", name="[ Контакты ]")

#действия
    def open_page(self):
        self.open(self.BASE_URL)

    def open_about(self):
        self.link_about().click()

    def open_services(self):
        self.link_services().click()

    def open_projects(self):
        self.link_projects().click()

    def open_reviews(self):
        self.link_reviews().click()

    def open_contacts(self):
        self.link_contacts().click()

#проверки
    def should_see_about(self):
        expect(self.page.locator("div.tn-atom", has_text="о нас")).to_be_visible()

    def should_see_services(self):
        expect(self.page.locator("div.tn-atom", has_text="услуги")).to_be_visible()

    def should_see_projects(self):
        expect(self.page.get_by_text("ОТЗЫВЫ КЛИЕНТОВ")).to_be_visible()

    def should_see_reviews(self):
        expect(self.page.get_by_text("ОТЗЫВЫ КЛИЕНТОВ")).to_be_visible()

    def should_see_contacts(self):
        expect(self.page.locator("div.tn-atom", has_text="контакты")).to_be_visible()
