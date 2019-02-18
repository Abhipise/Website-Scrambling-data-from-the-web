import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment,Residential-House,Villa&Locality=Warje&cityName=Pune")
c = r.content

soup =BeautifulSoup(c, "html.parser")

all = soup.find_all("div",{"class":"flex relative clearfix m-srp-card__container"})

l=[]
for item in all:
    d={}
    d["price"]=(item.find("div",{"class":"m-srp-card__price"}).text.replace(" ",""))
    d["Address"]=(item.find("div",{"class":"m-srp-card__heading clearfix"}).text.replace("What's near by","").replace("\n","").replace(",",""))
    #print(item.find("div",{"class":"m-srp-card__summary__item"}).text)
    for column_group in item.find_all("div",{"class":"m-srp-card__summary js-collapse__content"}):
       for feature_group , feature_name in zip(column_group.find_all("div",{"class":"m-srp-card__summary__title"}),column_group.find_all("div",{"class":"m-srp-card__summary__info"})):
         for LotSize in feature_group:
                d[LotSize]=(feature_name.text.replace("\n",""))
    l.append(d)



import pandas
df=pandas.DataFrame(l)
df.to_csv("MagicBricks.csv")
