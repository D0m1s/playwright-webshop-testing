import pytest
from playwright.sync_api import Page, expect

BASE_URL = "https://demoqa.com/"
ENTRIES_TO_ADD = 8


def test_web_tables_pagination_after_delete(page: Page) -> None:
    page.goto(BASE_URL)
    go_to_web_tables(page)

    page.evaluate("document.getElementById('fixedban')?.remove()")

    for i in range(ENTRIES_TO_ADD):
        add_entry(page, f"Test{i}", f"User{i}", f"test.user{i}@example.com",
                  str(25 + i), str(30000 + i * 1000), f"Dept{i}")

    page_indicator = page.locator(".pagination strong")
    expect(page_indicator).to_have_text("1 of 2")

    page.get_by_role("button", name="Next").click()
    expect(page_indicator).to_have_text("2 of 2")

    page.locator("[id^='delete-record-']").first.click()
    expect(page_indicator).to_have_text("1 of 1")


def go_to_web_tables(page: Page):
    page.locator(".card-body").filter(has_text="Elements").first.click()
    page.get_by_text("Web Tables", exact=True).click()


def add_entry(page: Page, first_name: str, last_name: str, email: str, age: str, salary: str, department: str):
    page.get_by_role("button", name="Add").click()
    page.get_by_placeholder("First Name").fill(first_name)
    page.get_by_placeholder("Last Name").fill(last_name)
    page.get_by_placeholder("name@example.com").fill(email)
    page.get_by_placeholder("Age").fill(age)
    page.get_by_placeholder("Salary").fill(salary)
    page.get_by_placeholder("Department").fill(department)
    page.get_by_role("button", name="Submit").click()
