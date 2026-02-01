import allure
from allure_commons.types import Severity
from selene import browser, be
from selene.support import by


@allure.tag("regress")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "semenov")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")

def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-playwright-example")
    open_issue_tab()
    should_see_issue_with_number("#1")

def s(selector):
    return browser.element(selector)

def ss(selector):
    return browser.all(selector)


@allure.step("Открываем главную страницу")
def open_main_page():
    #Открываем страницу
    browser.open("https://github.com")


@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    # Клик по кнопке поиска
    s(".header-search-button").click()
    # Вводим имя репо и жмём Enter
    search_input = s("#query-builder-test")
    search_input.should(be.visible.and_(be.enabled))
    search_input.type(repo)
    search_input.press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    # Находим ссылку по точному href
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).should(be.existing)
