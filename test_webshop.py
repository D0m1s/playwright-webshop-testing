import json
import pytest
from pathlib import Path
from playwright.sync_api import Page, expect

BASE_URL = "https://demowebshop.tricentis.com/"
PRICE_THRESHOLD = 800

DATA_FILE = Path(__file__).parent / "data" / "shopping_cart.json"
DATA = json.loads(DATA_FILE.read_text())


def clear_cart(page: Page) -> None:
    page.goto(BASE_URL + "cart")
    checkboxes = page.locator("input[name='removefromcart']")
    if checkboxes.count() > 0:
        for checkbox in checkboxes.all():
            checkbox.check()
        page.get_by_role("button", name="Update shopping cart").click()


@pytest.fixture()
def logged_in_page(page: Page):
    login_info = DATA["login_info"]

    page.goto(BASE_URL + "login")
    page.locator("#Email").fill(login_info["email"])
    page.locator("#Password").fill(login_info["password"])
    page.get_by_role("button", name="Log in").click()
    expect(page.get_by_role("link", name=login_info["email"])).to_be_visible()

    clear_cart(page)

    yield page

    clear_cart(page)
    page.locator(".ico-logout").click()


def test_shopping_cart_edit_flow(logged_in_page: Page) -> None:
    page = logged_in_page
    computer_type = DATA["computer_info"]["computer_type"]
    specs = DATA["computer_info"]["specs"]

    page.goto(BASE_URL)
    
    go_to_desktops(page)

    page.locator(".product-title a", has_text=computer_type).click()

    page.locator("input.add-to-cart-button").click()

    open_cart(page)
    cart_row = page.locator("tr.cart-item-row")
    expect(cart_row).to_contain_text(computer_type)

    cart_row.get_by_role("link", name="Edit").click()
    for spec in specs:
        page.get_by_label(spec).check()

    page.get_by_role("button", name="Update").click()

    open_cart(page)
    cart_row = page.locator("tr.cart-item-row")
    for spec in specs:
        expect(cart_row).to_contain_text(spec)

    cart_row.locator("input[name='removefromcart']").check()
    page.get_by_role("button", name="Update shopping cart").click()
    expect(page.get_by_text("Your Shopping Cart is empty!")).to_be_visible()


def test_bulk_add_by_price(logged_in_page: Page) -> None:
    page = logged_in_page   
    page.goto(BASE_URL)
    go_to_desktops(page)

    bulk_product_names = []
    for box in page.locator(".item-box").all():
        price_text = box.locator(".actual-price").inner_text()
        price = float(price_text.strip())
        cart_button = box.locator("input[value='Add to cart']")
        
        if price > PRICE_THRESHOLD and cart_button.count() > 0:
            name = box.locator(".product-title a").inner_text()
            bulk_product_names.append(name)

    for name in bulk_product_names:
        page.get_by_role("link", name=name, exact=True).click()
        
        for dropdown in page.locator(".attributes select").all():
            dropdown.select_option(index=1)
        
        for radio_group in page.locator(".attributes .option-list").all():
            first_radio = radio_group.locator("input[type='radio']").first
            if first_radio.count() > 0:
                first_radio.check()

        page.locator(".add-to-cart-button").first.click()
        
        expect(page.locator("#bar-notification")).to_be_visible()
        page.locator("#bar-notification").press("Escape")
        go_to_desktops(page)

    open_cart(page)
    
    assert page.locator("tr.cart-item-row").count() == len(bulk_product_names)

    calculated_total = 0.0
    for subtotal_cell in page.locator("span.product-subtotal").all():
        calculated_total += float(subtotal_cell.inner_text().strip())

    displayed_total_text = page.locator(".order-total strong").inner_text()
    displayed_total = float(displayed_total_text.strip())

    assert calculated_total == pytest.approx(displayed_total)

    for checkbox in page.locator("input[name='removefromcart']").all():
        checkbox.check()
    page.get_by_role("button", name="Update shopping cart").click()

    expect(page.get_by_text("Your Shopping Cart is empty!")).to_be_visible()


def go_to_desktops(page: Page) -> None:
    top_menu = page.locator("ul.top-menu")
    top_menu.get_by_role("link", name="Computers").hover()
    top_menu.get_by_role("link", name="Desktops").click()


def open_cart(page: Page) -> None:
    page.locator("#topcartlink .ico-cart").click()