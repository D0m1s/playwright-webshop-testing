import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://demoqa.com/"


def test_dynamic_properties(page: Page) -> None:
    page.goto(BASE_URL)

    go_to_dynamic_properties(page)

    enable_button = page.get_by_role("button", name="Will enable 5 seconds")
    visible_button = page.get_by_role("button", name="Visible After 5 Seconds")

    expect(enable_button).to_be_disabled()

    expect(visible_button).to_be_hidden()

    expect(enable_button).to_be_enabled(timeout=5050)

    expect(visible_button).to_be_visible(timeout=5050)


def go_to_dynamic_properties(page: Page) -> None:
    page.locator(".card-body").filter(has_text="Elements").first.click()
    page.get_by_text("Dynamic Properties", exact=True).click()
