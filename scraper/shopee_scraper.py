from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from utils.webdriver_manager import get_chromium_driver
from config.settings import (
    SHOPEE_LOGIN_URL,
    SHOPEE_PRODUCT_URL,
    SHOPEE_USERNAME,
    SHOPEE_PASSWORD,
)
from models.product import Product
from exceptions import (
    ScraperException,
    LoginError,
    ProductExtractionError,
    NetworkError,
)

class ShopeeScraper:
    def __init__(self):
        self.driver = get_chromium_driver()
        self.wait = WebDriverWait(self.driver, 20)

    def login(self):
        try:
            self.driver.get(SHOPEE_LOGIN_URL)

            username_field = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        "input[placeholder='No. Handphone/Username/Email']",
                    )
                )
            )
            password_field = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "input[placeholder='Password']")
                )
            )

            username_field.send_keys(SHOPEE_USERNAME)
            password_field.send_keys(SHOPEE_PASSWORD)
            password_field.send_keys(Keys.RETURN)

            sleep(5)
        except Exception as e:
            raise LoginError(f"Failed to log in: {str(e)}")

    def scrape_products(self):
        try:
            self.driver.get(SHOPEE_PRODUCT_URL)
            self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[@class='product-list']")
                )
            )

            products = self.driver.find_elements(
                By.XPATH, "//div[@class='product-item']"
            )
            product_data = []

            for product in products:
                try:
                    product_data.append(Product.from_element(product))
                except Exception as e:
                    raise ProductExtractionError(
                        f"Error extracting product data: {str(e)}"
                    )

            return product_data
        except Exception as e:
            raise NetworkError(f"Failed to load product page: {str(e)}")

    def run(self):
        try:
            self.login()
            return self.scrape_products()
        except (LoginError, ProductExtractionError, NetworkError) as e:
            raise ScraperException(f"An error occurred during scraping: {str(e)}")
        finally:
            self.driver.quit()

