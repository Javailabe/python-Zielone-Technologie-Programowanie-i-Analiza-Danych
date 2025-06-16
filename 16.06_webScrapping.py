from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import openpyxl

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
# options.add_argument("--window-size=1920,1080")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--disable-extensions")
# options.add_argument("--incognito")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--lang=pl-PL")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get("https://www.onet.pl")

elements = driver.find_elements(
    by=By.TAG_NAME,
    value="article"
)

posts = []

for element in elements:
    try:
        image_element = element.find_element(by=By.TAG_NAME, value="img")
        post_title = element.find_element(by=By.TAG_NAME, value="h3")
        link_element = element.find_element(by=By.TAG_NAME, value="a")

        image = image_element.get_attribute("src")
        title = post_title.accessible_name
        link = link_element.get_attribute("href")

        new_post = {
            "title": title,
            "image": image,
            "link": link
        }
        posts.append(new_post)

    except Exception as e:
        print("Brak danych")