from playwright.sync_api import sync_playwright

def search_flipkart(product):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.flipkart.com")

        try:
            page.click("button._2KpZ6l._2doB4z")  # Close login popup
        except:
            pass

        page.fill("input[name='q']", product)
        page.keyboard.press('Enter')
        page.wait_for_timeout(3000)

        results = []
        items = page.query_selector_all("._4rR01T")  # Titles
        prices = page.query_selector_all("._30jeq3")  # Prices

        for i in range(min(5, len(items))):
            results.append({
                "Product": items[i].inner_text(),
                "Price": prices[i].inner_text() if i < len(prices) else "N/A"
            })

        browser.close()
        return results
