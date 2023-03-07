import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://www.ebay.com/itm/284966662977?_trkparms=amclksrc%3DITM%26aid%3D777008%26algo%3DPERSONAL.TOPIC%26ao%3D1%26asc%3D20220705100511%26meid%3De62b643806a2471993354600b3f20f89%26pid%3D101524%26rk%3D1%26rkt%3D1%26itm%3D284966662977%26pmt%3D0%26noa%3D1%26pg%3D2380057%26algv%3DRecentlyViewedItemsV2%26brand%3DKawasaki&_trksid=p2380057.c101524.m146925&_trkparms=pageci%3A3556b4f1-bd33-11ed-a6f8-0e749b2d058b%7Cparentrq%3Abe1558601860aa722465c118fffb3bce%7Ciid%3A1").content

soup = BeautifulSoup(data, "html.parser")

span = soup.find("h1",{"class":"x-item-title__mainTitle"})

item = span.text

span = soup.find("span",{"itemprop":"price"})

price = span.text

print("The item" + item + " has a price of " + price + " on ebay.com.")

