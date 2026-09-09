from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time


URL = "https://www.amazon.com/s?k=smart+home"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)
time.sleep(8)
print("Page opened")
print("Page title:", driver.title)
print("Current URL:", driver.current_url)
for i in range(6):
    driver.execute_script(
        "window.scrollBy(0, 600);"
    )
    time.sleep(2)

products = driver.find_elements(
    By.CSS_SELECTOR,
    "div[data-asin]"
)
products = [
    product
    for product in products
    if product.get_attribute("data-asin")
]

print("Products found:", len(products))

data = []

for product in products:

    asin = product.get_attribute("data-asin")

    
    try:
        title = product.find_element(
            By.CSS_SELECTOR,
            "h2 span"
        ).text.strip()
    except:
        title = "No title"

    
    try:
        price = product.find_element(
            By.CSS_SELECTOR,
            "span.a-offscreen"
        ).text.strip()
    except:
        price = "No price"


    try:
        rating = product.find_element(
            By.CSS_SELECTOR,
            "span.a-icon-alt"
        ).get_attribute("innerHTML")
    except:
        rating = "No rating"


    try:
        reviews = product.find_element(
            By.CSS_SELECTOR,
            "span.a-size-base.s-underline-text"
        ).text.strip()
    except:
        reviews = "No reviews"


    try:
        link = product.find_element(
            By.CSS_SELECTOR,
            "h2 a"
        ).get_attribute("href")
    except:
        link = "No link"

    data.append({
        "ASIN": asin,
        "Title": title,
        "Price": price,
        "Rating": rating,
        "Reviews": reviews,
        "Link": link
    })
df = pd.DataFrame(data)
print("\n==============================")
print("Data collected:", len(df))
print("==============================")
print(df.head(10))
df.to_csv(
    "amazon_selenium_products.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nCSV file created successfully!")

input("\nPress Enter to close browser...")

driver.quit()