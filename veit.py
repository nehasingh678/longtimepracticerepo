from playwright.sync_api import sync_playwright

def vit_vellore():

    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        context=browser.new_context()
        page=context.new_page()

        page.goto('https://vit.ac.in/admissions/international/btech-eligibilityandprocedure')
        #page.locator("//span[@class='elementor-button-text'][contains(normalize-space(),'Announcements')]").click()
        #page.locator('//ul[@id="lists"]//a[text()="VITEEE 2026 "]').click()
        page.locator('//a[text()="About"]').click()
        page.locator("//span[text()='Ranking and Recognition']").click()
        value=page.title()
        #page.wait_for_selector('//span[@class="elementor-button-text"][contains(normalize-space(),"VIT - Campuses")]//i[@class="fa fa-chevron-circle-down"]').click(force=True)
        btn = page.locator(
            "//a[contains(@class,'elementor-button') and .//span[contains(normalize-space(),'VIT - Campuses')]]")
        btn.hover()
        btn.dispatch_event("mousedown")
        btn.dispatch_event("mouseup")
        btn.dispatch_event("click")
        # page.locator('//span[text()="VIT - Bhopal"]').click()
        # page.wait_for_timeout(40000)
        # btn1 = page.locator(
        #     "(//div[contains(@class,'brave_popupMargin__wrap')]//div[contains(@class,'brave_popup__close')])[1]"
        # )
        #
        # btn1.hover()
        # btn1.dispatch_event("mousedown")
        # btn1.dispatch_event("mouseup")
        # btn1.dispatch_event("click")
        #
        # btn1.hover()
        # btn1.dispatch_event("mousedown")
        # btn1.dispatch_event("mouseup")
        # btn1.dispatch_event("click")
        with page.context.expect_page() as new_page_info:
            page.locator('//span[text()="VIT - Bhopal"]').click()

        new_page = new_page_info.value
        new_page.wait_for_load_state()
        new_page.locator("(//div[contains(@class,'brave_popupMargin__wrap')]//div[contains(@class,'brave_popup__close')])[1]").click()

        # btn1.wait_for(state="attached")
        # btn1.hover()
        # btn1.dispatch_event("mousedown")
        # btn1.dispatch_event("mouseup")
        # btn1.dispatch_event("click")
        new_page.locator('//ul[@id="menu-main-menu-header"]//span[text()="RESEARCH"]').hover()


        page.wait_for_timeout(40000)



chk=vit_vellore()
