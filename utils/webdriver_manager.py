from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def get_chromium_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/usr/bin/chromium"
    # chrome_options.add_argument(f'--proxy-server={PROXY["http"]}')
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )

    driver.delete_all_cookies()
    return driver
