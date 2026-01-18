from playwright.sync_api import sync_playwright

def check_playwright():

    with sync_playwright() as p:

        brrowser=p.chromium.launch(headless=False)
        context=brrowser.new_context()
        page=context.new_page()

        page.goto("https://www.zomato.com/bangalore/restaurants")
        page.locator('//input[@placeholder="Search for restaurant, cuisine or a dish"]').click()
        page.locator('//input[@placeholder="Search for restaurant, cuisine or a dish"]').type("Bengaluru")
        page.locator('//div//p[text()="JW Marriott Bengaluru, Lavelle Road"]').click()
        page.wait_for_timeout(30000)

    return 1

chk=check_playwright()







