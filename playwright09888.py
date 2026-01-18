from playwright.sync_api import sync_playwright

def check_playwright():

    with sync_playwright() as p:

        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()

        url="https://www.amazon.com/"
        page.goto(url)
        page.locator('//span[@class="a-button-inner"]//span[normalize-space()="Dismiss"]').click()
        page.wait_for_timeout(30000)


x=check_playwright()
