from playwright.sync_api import sync_playwright

def chk_upload():

    with sync_playwright() as p:

        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()

        url="https://easyupload.io/"
        page.goto(url)
        page.locator('//span[text()="(Max 50 files, 10 GB per file, total 100 GB)"]').click()
        page.set_input_files('//span[text()="(Max 50 files, 10 GB per file, total 100 GB)"]','/Users/neha/PycharmProjects/nehalearningvenev/playwright/new.doc')
        page.wait_for_timeout(30000)
        print("uploaded")


chk=chk_upload()






