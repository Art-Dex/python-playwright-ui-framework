# UI Automation Framework (Python + Playwright)

Автоматизированный тестовый фреймворк для UI-тестирования интернет-магазина https://www.saucedemo.com/

## Стек технологий

- Python 3.12.4
- Pytest
- Playwright
- Pytest-Playwright

---

## Структура проекта
```
python-playwright-ui-framework/
│ 
├── core/ 
├── pages/ 
├── tests/ 
├── conftest.py 
└── README.md
```

## Архитектура

Проект построен с использованием паттерна Page Object Model (POM).

- BasePage — базовый класс для всех страниц
- Page Objects — инкапсулируют логику взаимодействия с UI
- Tests — содержат только бизнес-сценарии