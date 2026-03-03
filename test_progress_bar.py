import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://demoqa.com/"


def test_progress_bar_functionality(page: Page) -> None:
    page.goto(BASE_URL)

    go_to_progress_bar(page)

    progress_bar = page.get_by_role("progressbar")
    expect(progress_bar).to_have_text("0%")

    page.get_by_role("button", name="Start").click()

    expect(progress_bar).not_to_have_text("0%", timeout=5000)

    expect(progress_bar).to_have_text("100%", timeout=60000)

    expect(page.get_by_role("button", name="Reset")).to_be_visible()


def go_to_progress_bar(page: Page) -> None:
    page.locator(".card-body").filter(has_text="Widgets").first.click()
    page.get_by_text("Progress Bar", exact=True).click()
