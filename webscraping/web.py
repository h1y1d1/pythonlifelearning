import requests
import pandas
from bs4 import BeautifulSoup

response = requests.get("https://www.flipkart.com/search?q=samnsung%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
print(response)
soup = BeautifulSoup(response.content,"html.parser")
print(soup)
names = soup.find_all("div", class_="_4rR01T")
print(names)
name = []
for i in names[0:10]:
    d = i.get_text()
    name.append(d)
print(name)

prices = soup.find_all("div", class_="_30jeq3 _1_WHN1")
price = []
for i in prices[0:10]:
    d = i.get_text()
    price.append(d)
print(price)

ratings = soup.find_all("div", class_="_3LWZlK")
star = []
for i in ratings[0:10]:
    d = i.get_text()
    star.append(float(d))
print(star)

df = pandas.DataFrame()
df["Names"] = name
df["Prices"] = price
df["Ratings"] = star
df.to_csv("mobiles1.csv")

