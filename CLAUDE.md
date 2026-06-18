# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Selenium + Pytest** test automation framework targeting the SauceDemo e-commerce demo app at https://www.saucedemo.com/. It follows the Page Object Model (POM) pattern.

## Running Tests

```bash
# Run all tests
pytest

# Run by marker
pytest -m smoke
pytest -m regression

# Run a single test file
pytest tests/test_login.py

# Run with HTML report
pytest --html=reports/report.html

# Verbose output
pytest -v
```

Markers are defined in `pytest.ini`: `smoke`, `regression`.

To run in headless mode, uncomment `--headless` in the Chrome options inside `conftest.py`.

## Architecture

### Page Object Model

Each page of the application maps to a class in `pageobjects/`. Page classes own all locators and interaction methods for their page — tests never call WebDriver methods directly.

Flow: `Login → Inventory → Cart → Checkout → Checkout Overview → Checkout Complete`

### Key Files

| File | Role |
|------|------|
| `conftest.py` | Browser fixture (Chrome WebDriver), test data loader, screenshot-on-failure autouse fixture |
| `fixtures/cart_fixtures.py` | Factory fixtures that navigate to a logged-in state with items already in the cart |
| `data/test_login.json` | Valid and invalid credentials used by parametrized login tests |
| `utils/browserutils.py` | Base utility class with shared browser helper methods (inherited by page objects) |

### Fixture Layering

- `browser` fixture (function-scoped) — creates and tears down the Chrome WebDriver
- `data_load` fixture — reads `data/test_login.json` and returns parsed credentials
- `screenshot_on_fail` (autouse) — captures a screenshot to `screenshots/` on any test failure
- `cart_fixtures.py` — higher-level fixtures that compose the `browser` fixture with login and cart-population steps

### Test Data

Credentials live in `data/test_login.json`. Valid user: `standard_user / secret_sauce`. Tests use `@pytest.mark.parametrize` to drive multiple credential scenarios from this file.

### Waits Strategy

`conftest.py` sets an implicit wait of 10 seconds on the driver. Cart and inventory page objects additionally use explicit `WebDriverWait` for elements that require dynamic loading.
