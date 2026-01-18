from playwright.sync_api import sync_playwright

def check_playwright():

    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()

        page.goto('https://rnd.iitb.ac.in/technology_innovation_landing_page')
        page.scr