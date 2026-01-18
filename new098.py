from playwright.sync_api import sync_playwright

def check_playwright():

    with sync_playwright() as p:

        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()

        url="https://www.amazon.com/"
        page.goto(url)
        page.locator("//button[text()='Continue shopping']").click()
        #page.wait_for_timeout(90000)
        #page.wait_for_selector('//span[@class="a-button-inner"]//span[normalize-space()="Dismiss"]').hover()
        chk=page.wait_for_selector('//span[@class="a-button-inner"]//span[normalize-space()="Dismiss"]').is_visible()
        if chk:
            page.wait_for_selector('//span[@class="a-button-inner"]//span[normalize-space()="Dismiss"]').click(force=True)
            page.locator("//span[@class='hm-icon-label' and text()='All']").click()
            page.get_by_role("button", name="Computers").click(force=True)
            page.wait_for_timeout(3000)



x=check_playwright()
