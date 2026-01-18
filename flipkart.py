from playwright.sync_api import sync_playwright

def flipkart():

    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()

        page.goto('https://bitmesra.ac.in/Other-Department-Pages/content/1/205/706')
        page.locator('//ul[@class="menu-section"]//a[text()="Academics"]').click()
        page.wait_for_timeout(3000)
        page.locator('//a[text()=" Institute Deans"]').click()
        page.wait_for_timeout(3000)



chk=flipkart()

