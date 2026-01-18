from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
def check_file_upload():

    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()
        page.goto("https://the-internet.herokuapp.com/",timeout=80000, wait_until="domcontentloaded")
        page.locator("//a[text()='Horizontal Slider']").click()
        slider=page.locator("//input[@type='range']")
        slider.focus()
        slider.drag_to(slider)
        page.wait_for_timeout(50000)



chk = check_file_upload()


