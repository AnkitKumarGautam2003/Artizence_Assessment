from playwright.sync_api import sync_playwright

def search_amazon(product):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.amazon.in")
        page.fill("input[name='field-keywords']", product)
        page.click("input[type='submit']")
        page.wait_for_timeout(3000)

        items = page.query_selector_all(".s-title-instructions-style")
        results = []
        for item in items[:5]:
            title = item.inner_text()
            results.append({"Product": title})

        browser.close()
        return results