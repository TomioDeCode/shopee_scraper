from scraper import ShopeeScraper
from exceptions import (
    ScraperException,
    LoginError,
    ProductExtractionError,
    NetworkError,
)
from tqdm import tqdm


def main():
    scraper = ShopeeScraper()
    try:
        products = scraper.run()

        for product in tqdm(products, desc="Scraping Products", unit="product"):
            print(product)
    except LoginError as e:
        print(f"Login failed: {str(e)}")
    except ProductExtractionError as e:
        print(f"Failed to extract product data: {str(e)}")
    except NetworkError as e:
        print(f"Network error occurred: {str(e)}")
    except ScraperException as e:
        print(f"Scraping failed: {str(e)}")


if __name__ == "__main__":
    main()
