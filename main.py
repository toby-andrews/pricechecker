from bs4 import BeautifulSoup
import requests
import smtplib

url = "https://shop.lululemon.com/p/mens-jackets-and-outerwear/Down-For-It-All-Hoodie/_/prod9200786?color=26083"

headers = {
    " Accept-Language": "en-US,en;q=0.9,en-GB;q=0.8,de;q=0.7",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.102 Safari/537.36",
}

response = requests.get(url=url, params=headers)

soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())



def send_email(price_only):

    my_email = "TESTTEST"
    password = "TESTTEST"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=my_email,
                            msg=f"Subject:Price Alert!\n\nThe price of the jacket has dropped to ${price_only}! Buy now.")


price = soup.find(class_="col-xs-12 price-wrapper OneLinkNoTx").text
price_without_currency = price.split("$")[1]
price_only = float(price_without_currency.split()[0])
#print(price_only)

if price_only < 230:
    send_email(price_only)