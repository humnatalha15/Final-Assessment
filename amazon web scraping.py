import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.com/s?k=laptop"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/131.0.0.0 Safari/537.36", "Accept-Language": "en-US,en;q=0.9"}
response = requests.get(url, headers=headers)
print("Status Code:", response.status_code)
print("URL:", response.url)
soup = BeautifulSoup(response.text, "html.parser")
print("Page Title:", soup.title.get_text(strip=True) if soup.title else "No title")
products = soup.select('[data-component-type="s-search-result"]')
print("Number of products found:", len(products))
for product in products[:5]:
    title = product.select_one("h2")
    price = product.select_one(".a-price .a-offscreen")

    if price:
        print("Title:", title.get_text(strip=True) if title else "No title")
        print("Price:", price.get_text(strip=True))
        print("-" * 50)
data = []

for product in products:
    title = product.select_one("h2")
    price = product.select_one(".a-price .a-offscreen")
    link = product.select_one("a")

    data.append({
    "title": title.get_text(strip=True) if title else "No title",
    "price": price.get_text(strip=True) if price else "No price",
    "link": "https://www.amazon.com" + link.get("href")
            if link and link.get("href") else "No link"
})
print(data)
import pandas as pd

df = pd.DataFrame(data)
df.to_csv("amazon_products.csv", index=False)

print("CSV file created successfully!")
df["price"] = df["price"].str.replace(r"\xa0", " ", regex=True)
df.to_csv("amazon_products.csv", index=False)