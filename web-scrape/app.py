from bs4 import BeautifulSoup
import pandas
import requests

r = requests.get(
    "https://www.century21.com/real-estate/colorado-spgs-co/LCCOCOLORADOSPGS/",
    headers={
        "User-agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
    },
)
c = r.content
soup = BeautifulSoup(c, "html.parser")
all = soup.find_all("div", {"class": "property-card-primary-info"})
lst = []
for item in all:
    prop = {}
    prop["Address"] = item.find("div", {"class", "property-address"}).text.strip()
    prop["Price"] = item.find("a", {"class", "listing-price"}).text.strip()
    prop["Beds"] = item.find("div", {"class", "property-beds"}).text.strip()
    prop["Bath"] = item.find("div", {"class", "property-baths"}).text.strip()
    prop["SQFT"] = item.find("div", {"class", "property-sqft"}).text.strip()

    lst.append(prop)

df = pandas.DataFrame(lst)
print(df)
df.to_csv("properties.csv")
