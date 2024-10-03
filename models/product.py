# models/product.py

from selenium.webdriver.common.by import By


class Product:
    def __init__(self, id, name, price, stock, image_url):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock
        self.image_url = image_url

    @classmethod
    def from_element(cls, element):
        id = element.find_element(
            By.XPATH, ".//input[@class='shopee-checkbox__input']"
        ).get_attribute("value")
        name = element.find_element(
            By.XPATH, ".//a[@class='product-name-wrap']/span"
        ).text
        price = element.find_element(
            By.XPATH, ".//span[contains(@class, 'price')]"
        ).text
        stock = element.find_element(By.XPATH, ".//span[@class='stock-text']").text
        image_url = element.find_element(By.XPATH, ".//img").get_attribute("src")

        return cls(id, name, price, stock, image_url)

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, stock={self.stock})"
