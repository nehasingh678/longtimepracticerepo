from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

def check_drag_and_drop():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()
        page.goto("https://the-internet.herokuapp.com/floating_menu#news")
        page.wait_for_timeout(6000)
        source_locteor=page.locator('//div[@id="menu"]//a[text()="Home"]').text_content()
        val=expect(page.locator('//div[@id="menu"]//a[text()="Home"]')).to_have_text('Home')
        print("returned",val)
        #source_locteor.drag_to(destination_locator)
        page.wait_for_timeout(6000)
        print(" source_locteor", source_locteor)


x=check_drag_and_drop()
print(x)

