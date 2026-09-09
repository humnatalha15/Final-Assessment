from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.ebay.com")

wait = WebDriverWait(driver, 30)
search_box = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='_nkw']"))
)
search_box.clear()
search_box.send_keys("Beautiful Soap")
search_box.send_keys(Keys.ENTER)
time.sleep(8)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
time.sleep(5)
soup = BeautifulSoup(driver.page_source, "html.parser")
products = soup.select("li.s-card")

print("Product found:", len(products))

data = []

for product in products:

    title = product.select_one(".s-card__title")
    price = product.select_one(".s-card__price")
    link = product.select_one("a[href]")

    if title:

        product_name = title.get_text(" ", strip=True)

        if product_name:

            data.append({
                "Product Name": product_name,
                "Price": price.get_text(" ", strip=True)
                if price else "",
                "Product URL": link.get("href")
                if link else ""
            })

df = pd.DataFrame(data)

print(df.head(10))
print("Total products:", len(df))

filename = "ebay_beautiful_soap.csv"

df.to_csv(
    filename,
    index=False,
    encoding="utf-8-sig"
)

print("CSV file created:", filename)
driver.quit()