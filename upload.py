from playwright.sync_api import sync_playwright
import os

def check_uplad():

    with sync_playwright() as p:

        browser= p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()

        url="https://www.file.io/"
        page.goto(url)
        page.locator("//label[normalize-space(text()='Upload Files')]//*[name()='svg']").click()
        print("uploda button clicked")

        # Upload file using hidden input
        page.set_input_files("//label[normalize-space(text()='Upload Files')]//*[name()='svg']",
            "/Users/neha/PycharmProjects/nehalearningvenev/playwright/new.doc"
        )
        #file_chooser.set_files('/Users/neha/PycharmProjects/nehalearningvenev/playwright/python1.py')
        page.wait_for_timeout(30000)

        #upload_file=upload.set_input_files('/Users/neha/PycharmProjects/nehalearningvenev/playwright','p')

        print("file uploaaded ")

        return 1

chk=check_uplad()



