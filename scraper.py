"""
Phase 1: Web Scraper using Selenium
Scrapes product data from books.toscrape.com (a practice site)
Output: data/raw_products.csv
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"
TOTAL_PAGES = 10  # Scrape 10 pages (~200 books)


def init_driver(headless=True):
    """Initialize Chrome WebDriver."""
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1280,800")
    return webdriver.Chrome(options=options)


def scrape_page(driver, page_num):
    """Scrape a single page and return list of product dicts."""
    url = BASE_URL.format(page_num)
    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "product_pod"))
        )
    except Exception as e:
        logger.warning(f"Page {page_num} load timeout: {e}")
        return []

    products = []
    books = driver.find_elements(By.CLASS_NAME, "product_pod")

    for book in books:
        try:
            title = book.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
            price_text = book.find_element(By.CLASS_NAME, "price_color").text
            rating_class = book.find_element(By.CLASS_NAME, "star-rating").get_attribute("class")
            availability = book.find_element(By.CLASS_NAME, "availability").text.strip()

            products.append({
                "title": title,
                "price_raw": price_text,
                "rating_raw": rating_class,
                "availability": availability,
                "page": page_num
            })
        except Exception as e:
            logger.warning(f"Error parsing book on page {page_num}: {e}")

    logger.info(f"Page {page_num}: scraped {len(products)} products")
    return products


def main():
    logger.info("Starting scraper...")
    driver = init_driver(headless=True)
    all_products = []

    try:
        for page in range(1, TOTAL_PAGES + 1):
            products = scrape_page(driver, page)
            all_products.extend(products)
            time.sleep(1)  # Polite delay between requests
    finally:
        driver.quit()

    df = pd.DataFrame(all_products)
    df.to_csv("data/raw_products.csv", index=False)
    logger.info(f"Saved {len(df)} products to data/raw_products.csv")
    print(df.head())


if __name__ == "__main__":
    main()
