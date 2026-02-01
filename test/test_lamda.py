import allure
from selene.support.conditions import be, have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

def test_dinamic_lamda():
    with allure.step('Открываем главную страницу'):
        browser.open("https://github.com")

    # 1. Клик по кнопке поиска (она точно есть)
    with allure.step('Ищем репозиторий'):
        s(".header-search-button").click()
    # 2. Ждём появления модального окна с query builder
        s("#query-builder-test").should(be.visible.and_(be.enabled))
    # 3. Вводим текст напрямую в этот input
        search_box = s("#query-builder-test")
        search_box.type("eroshenkoam/allure-example/allure-example")
    # 4. Нажимаем Enter
        search_box.press_enter()

    # находим репу и кликаем
    with allure.step('Находим репозиторий'):
        s('a[href$="eroshenkoam/allure-playwright-example"]').click()

    # ищем и кликаем issues
    with allure.step('Открываем таб issues'):
        s('#issues-tab').click()

    # сравниваем что issues есть
    with allure.step('сравниваем issues'):
        s('//span[contains(., "#1")]')