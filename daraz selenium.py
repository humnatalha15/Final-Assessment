from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)
driver.get("https://www.daraz.pk/")
time.sleep(5)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("beautiful soap")
search_box.submit()

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
        "Product Link": link
    })


df = pd.DataFrame(data)

df.to_csv(
    "beautiful_soap.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\n==============================")
print("SCRAPING COMPLETED")
print("==============================")
print("Products found:", len(df))
print("CSV file: beautiful_soap.csv")
print("\nFirst products:")
print(df.head())


driver.quit()