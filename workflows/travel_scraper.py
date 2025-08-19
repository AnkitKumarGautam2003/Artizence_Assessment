from playwright.sync_api import sync_playwright
import time

def search_travel(from_city,To_city):
   1235
    # Dummy placeholder (actual travel scraping is complex)
   with sync_playwright() as p:
    browser =p.chromium.launch(headless=False)
    page=browser.new_page()

    
    
    page.goto("https://www.makemytrip.global/?cc=in")
    time.sleep(3)
    page.click("div.landingContainer")

    

    page.click('label[for="fromCity"]')
    page.fill('input[placeholder="From"]', from_city)
    page.keyboard.press("Enter")

    page.click('label[for=toCity]')
    page.fill('input[placeholder="To"]',To_city)
    page.keyboard.press("Enter")


    page.click('label[for="departure"]')
    page.click('//div[@aria-label="Fri Aug 29 2025"]')

    page.click('a.widgetSearchBtn')
    page.wait_for_timeout(5000)
    time.sleep(3)
    
    flights_cards=page.query_selector_all('div.listingCard')
    results=[]
    
    for i in flights_cards:
        air_line=i.query_selector('span.airlineName')
        pri_ce=i.query_selector('div.clusterViewPrice')

        airline=air_line.inner_text().strip() if air_line else "N/A"
        price_text=pri_ce.inner_text().strip() if pri_ce else "N/A"
        
        try:
            price = int("".join(filter(str.isdigit, price_text)))
        except:
            price = 999999  # if parse fails, set very high so it won't be in cheapest

        results.append({"Airline": airline, "Price": price, "RawPrice": price_text})

    # Sort by price
    results = sorted(results, key=lambda x: x["Price"])

    # Take cheapest 5
    cheapest_5 = results[:5]

    browser.close()
    return cheapest_5
    
    
        