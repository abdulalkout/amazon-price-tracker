import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "https://www.amazon.com/Samsung-Electronics-Smartwatch-Detection-Bluetooth/dp/B096BKFG57/ref=nav_signin?c" \
      "rid=1KWQIS3CWJD5G&keywords=samsung%2Bwatch%2B4&qid=1649858914&sprefix=%2Caps%2C1042&sr=8-1&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36",
    "Accept-Language": "ar,en-US;q=0.9,en;q=0.8"
}

# ---URL get request -----#
response = requests.get(URL, headers=headers)
content = response.text

# --- Beautiful Soup -------#

soup = BeautifulSoup(content, "lxml")

all_price_data = soup.find(name="span", class_="a-price")
price = all_price_data.get_text().split("$")[1]
price_float = float(price)
print(price_float)

# ------send E-mail if the price got low ------#


ADD_to_send = "abdul.alkout@gmail.com"
my_email = "alkout.management@gmail.com"
password = "I'mA.A.M-1964"

# ---- Check the price -----#

if price_float >= 250:
    # ----------E-mail Connection --------------#
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=ADD_to_send,
                            msg="Subject: Watch price on AMAZON \n\n note that SAMSUNG"
                                " watch is avelable with the price you want")
