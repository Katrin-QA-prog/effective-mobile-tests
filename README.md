# effective-mobile-tests
for a test assignment for a vacancy at the company effektive-mobile

#  Effective Mobile — Автоматические тесты

Этот проект содержит набор автоматических тестов для сайта [https://effective-mobile.ru](https://effective-mobile.ru),  
написанных с использованием **Python + Playwright + Pytest + Allure**.

---

##  Возможности
- UI-тесты основных разделов сайта (`О нас`, `Услуги`, `Проекты`, `Отзывы`, `Контакты`)
- Реализован паттерн **Page Object Model**
- Поддержка **Allure Report** для наглядных отчётов
- Возможность запуска тестов в **Docker** для CI/CD и изолированной среды

---

##  Требования
- Python 3.10+
- Java 8+ (для Allure)
- Docker (опционально)
- Установленный браузер Chromium (устанавливается автоматически через Playwright)

---

## Запуск в IDE (PyCharm)
- pytest --alluredir=allure-results   (сохранение результата тестов)
- allure serve allure-results   (вывод в HTML страницу)

## Завпуск в Docker из PyCharm
- docker build -t em-tests .   (сборка образа)
- docker run --rm -it -v "$(pwd)/allure-results:/app/allure-results" em-tests   (запуск тестов (с сохранением Allure-результатов на хосте))
- allure serve allure-results   (Генерация локального отчёта)




