import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import re

os.makedirs("app/export", exist_ok=True)

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(options=chrome_options)

with open("seed.json", "r", encoding="utf-8") as f:
    data = json.load(f)
product_url = data["product_url"]
driver.get(product_url)

wait = WebDriverWait(driver, 2)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))

soup = BeautifulSoup(driver.page_source, "lxml")

title_tag = soup.find("h1")
title = title_tag.text.strip() if title_tag else ""

price_tag = soup.find("div", class_="item__price-left-side")
if price_tag:
    price = price_tag.text.strip().replace("₸", "").replace(u'\xa0', '')
else:
    price = ""

rating_tag = soup.find("div", class_=re.compile("rating"))
rating = rating_tag.text.strip() if rating_tag else ""

images = []
for img in soup.find_all("img", class_=re.compile("item__slider-pic")):
    src = img.get("src")
    if src:
        images.append(src)

sellers = []

# Находим таблицу продавцов
table = soup.find("table", class_="sellers-table__self")
if table:
    rows = table.find("tbody").find_all("tr")
    for row in rows:
        # Название продавца
        seller_tag = row.find("td", class_="sellers-table__cell")
        seller_name = seller_tag.find("a").text.strip() if seller_tag else ""

        # Цена
        price_tag = row.find("div", class_="sellers-table__price-cell-text")
        price_value = price_tag.text.strip().replace(u'\xa0', '').replace("₸", "") if price_tag else ""

        # Доставка — собираем все опции через запятую
        delivery_cells = row.find_all("div", class_="sellers-table__delivery-cell-option")
        delivery_options = []
        for cell in delivery_cells:
            delivery_text = cell.get_text(separator=" ", strip=True)
            delivery_options.append(delivery_text)
        delivery = ", ".join(delivery_options)

        # Добавляем в список
        sellers.append({
            "Seller": seller_name,
            "SellerPrice": price_value,
            "Delivery": delivery
        })

# --- Вычисляем мин и макс цену ---
prices = []
for s in sellers:
    try:
        prices.append(int(s["SellerPrice"].replace(" ", "")))
    except:
        pass

min_price = min(prices) if prices else None
max_price = max(prices) if prices else None

# Пример вывода


product_data = {
    "title": title,
    "price": price,
    "rating": rating,
    "images": images,
    "sellers": sellers,
    "min_price": min_price,
    "max_price": max_price
}

with open("app/export/product.json", "w", encoding="utf-8") as f:
    json.dump(product_data, f, ensure_ascii=False, indent=4)

driver.quit()
