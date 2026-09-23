import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Scenario 1: Normal deployment
        await page.goto('http://localhost:5000')
        await page.fill('textarea[id="textToAnalyze"]', 'I am so happy I could cry')
        # Wait for the button and click it
        await page.click('button:has-text("Analyze Emotions")')
        await page.wait_for_selector('div[id="result"]:has-text("joy")')
        # Wait a small moment to ensure rendering is complete
        await page.wait_for_timeout(1000)
        await page.screenshot(path='6b_deployment_test.png')
        
        # Scenario 2: Error handling interface
        await page.fill('textarea[id="textToAnalyze"]', '')
        await page.click('button:has-text("Analyze Emotions")')
        await page.wait_for_selector('div[id="result"]:has-text("Invalid text! Please try again.")')
        await page.wait_for_timeout(1000)
        await page.screenshot(path='7c_error_handling_interface.png')
        
        await browser.close()

asyncio.run(main())
