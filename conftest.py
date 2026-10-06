from playwright.sync_api import sync_playwright
import pytest


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=False, args=["--start-maximized"])
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    context = browser.new_context(no_viewport=True)
    page=context.new_page()
    yield page
    page.close()
    context.close()

