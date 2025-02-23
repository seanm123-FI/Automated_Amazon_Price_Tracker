import os
import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

#Add a header for the request
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "sec-fetch-site": "cross-site",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "priority": "u=0, i",
    "x-forwarded-proto": "https",
    "x-https":"on",
    "X-Forwarded-For": "51.182.3.210",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
}


# Scrape to get item price
URL = ("https://www.amazon.com/CeraVe-Moisturizing-Lotion-Hyaluronic-Fragrance/dp/B07RK4HST7/ref=sr_1_1?crid=6IHD8UNAB8OL&dib=eyJ2IjoiMSJ9.j7IYE0WXjFEUyEP4FpoxoEFFjRwUx9j3EkivcalZpUYyzR3vo6d0M-NiBcThR4Oi6xlw8-YExFHj5Lr5h6smurO0KeC1cIRaah2QmBfcojjMwKKhqvYX0oW3kyJ7oMKLoE7521EVZvX-J3T2FEolthC0QRKxIkj5zjuIAD_OwJdt4Mqm5EaGEdDWFHdNpQ6VQ-TkGzWsCLlBOhE12f_e-sui0X7WIFEkgZ_fBViz-QKX_RDSPOpJ_5PUqb44_DgkMwTYsWHZoFGYdii0E7X9RpVPaDdGXpVaU8PuusQicnNO9csArKdS1359grnfrp2sMSVvU0_tX9QNO55X-UIOAWukp4EvOxG9-W4fQYcmnEuFcrCo0HkdDpgmS8OTq38KpcwfEElxfuZYDae5yQI14zYEpIqAVG0wODJb2ta-s48VN5PmQBJ-77WTDWgsIuXt.DY83SYGZDnwKICjtDQEEL7miy4KOzWZXeC7h-ZKUFv8&dib_tag=se&keywords=cerave&qid=1740343824&sprefix=cerave%2Caps%2C162&sr=8-1&th=1")
response = requests.get(URL, headers=header)
pot_website_html = response.text

soup = BeautifulSoup(pot_website_html, 'html.parser')

whole_price = soup.find(class_="a-price-whole").get_text()
fraction_price = soup.find(class_="a-price-fraction").get_text()

total_price = float(whole_price + fraction_price)
print(total_price)

# Code to send email

product_desc = soup.find(class_="a-size-large product-title-word-break").get_text().strip()
print(product_desc)

BUY_PRICE = 20

if total_price < BUY_PRICE:
    message = f"{product_desc} is on sale for {total_price}!"

    #Use environment variables
    with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
        connection.starttls()
        result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
        connection.sendmail(
            from_addr=os.environ["EMAIL_ADDRESS"],
            to_addrs=os.environ["EMAIL_ADDRESS"],
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )

