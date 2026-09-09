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
driver.get(
    "https://www.alibaba.com/trade/search?SearchText=wireless+headphones"
)

time.sleep(10)
soup = BeautifulSoup(driver.page_source, "html.parser")
links = soup.find_all("a", href=True)

data = []
seen = set()

for link in links:

    name = link.get_text(" ", strip=True)
    href = link.get("href")

    # Product-like links
    if (
        name
        and len(name) > 15
        and (
            "headphone" in name.lower()
            or "wireless" in name.lower()
        )
    ):

        if name not in seen:
            seen.add(name)

            if href.startswith("/"):
                href = "https://www.alibaba.com" + href

            data.append({
                "Product Name": name,
                "Product URL": href
            })

df = pd.DataFrame(data)

print("Product found:", len(df))
print(df.head(10))
filename = "alibaba_wireless_headphones.csv"

df.to_csv(
    filename,
    index=False,
    encoding="utf-8-sig"
)

print("CSV file created:", filename)

input("Press Enter to close...")
driver.quit()