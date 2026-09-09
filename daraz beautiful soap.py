from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

keyword = "beautiful soap"
url = "https://www.daraz.pk/catalog/?q=" + keyword.replace(" ", "%20")

print("Opening Daraz...")
driver.get(url)

# Wait for page
time.sleep(7)

for i in range(4):
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )
    time.sleep(3)

products = driver.find_elements(
    By.CSS_SELECTOR,
    "div[data-qa-locator='product-item']"
)

print("Products found:", len(products))

data = []

for product in products:

    
    try:
        name = product.find_element(
            By.CSS_SELECTOR,
            "div.RfADt"
        ).text.strip()
    except:
        name = "N/A"


    try:
        price = product.find_element(
            By.CSS_SELECTOR,
            "span.ooOxS"
        ).text.strip()
    except:
        price = "N/A"


    try:
        link = product.find_element(
            By.TAG_NAME,
            "a"
        ).get_attribute("href")
    except:
        link = "N/A"

    data.append({
        "Product Name": name,
        "Price": price,
        "Link": link
    })

df = pd.DataFrame(data)

df.to_csv(
    "beautiful_soap.csv",
    index=False,
    encoding="utf-8-sig"
)

print("--------------------------------")
print("CSV CREATED SUCCESSFULLY!")
print("File: beautiful_soap.csv")
print("Total products:", len(df))
print("--------------------------------")

print(df)

driver.quit()