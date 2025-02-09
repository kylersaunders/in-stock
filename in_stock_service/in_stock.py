from playwright.sync_api import sync_playwright


def check_stock(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            page.goto(url)

            # Wait for the 'Ship to me' option to load
            page.locator("li:has-text('Ship to me')").wait_for()

            # Find the radio input button within the 'Ship to me' li and click it
            radio_button_locator = "li:has-text('Ship to me') input[type='radio']"
            page.locator(radio_button_locator).click()

           # Wait for the stock status element to appear
            stock_status_locator = "[data-testid='stock-status']"
            page.locator(stock_status_locator).wait_for()

            # Determine the stock status
            stock_status_text = page.locator(stock_status_locator).inner_text()

            h1_locator = "h1"
            h1_text = page.locator(h1_locator).inner_text()
            return stock_status_text, h1_text

        except Exception as e:
            print(f"An error occurred checking stock: {e}")
            return "Error occurred while checking stock"

        finally:
            browser.close()
