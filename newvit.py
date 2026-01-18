from playwright.sync_api import sync_playwright


def check_playwright():

    with sync_playwright() as p:

        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()

        page.goto('https://vit.ac.in/')
        with context.expect_page() as new_tab:

            page.locator('//span[text()="Apply Now"]').click()

        new_page1=new_tab.value
        print("title",new_page1.title())
        new_page1 = new_tab.value
        print("title", new_page1.title())

        # Wait for the menu to appear
        new_page1.wait_for_selector('//li[@id="menu-item-77"]//a[text()="International"]', state="visible",timeout=10000)

        # Hover if it's a dropdown menu
        new_page1.locator('//li[@id="menu-item-77"]').hover()

        # Click the International link (force click if needed)
        new_page1.locator('//li[@id="menu-item-77"]//a[text()="International"]').click(force=True)
        print("clicked")
        new_page1.wait_for_timeout(5000)

        with context.expect_page() as new_page2:
            new_page1.locator('//span[text()="UG Foreign Application 2025 - 2026 - Apply Now"]').click()
        newpage2 = new_page2.value
        newpage2.wait_for_timeout(4000)


chk=check_playwright()



