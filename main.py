from typing import Dict, Union


def plus(a: Union[int, float], b: Union[int, float]) -> Dict[str, Union[int, float]]:
    return {"result": a + b}


def minus(a: Union[int, float], b: Union[int, float]) -> Dict[str, Union[int, float]]:
    return {"result": a - b}


def multiply(a: Union[int, float], b: Union[int, float]) -> Dict[str, Union[int, float]]:
    return {"result": a * b}


print(plus(5, 4))
print(minus(9, 8))
print(multiply(1, 4))

# __________________________________________

from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    name: str
    mail: str
    address: str


class Bank(BaseModel):
    name: str
    rating: int
    opened: bool


class Card(BaseModel):
    cardholder: User
    which_bank: Bank
    opened: bool


class Balance(BaseModel):
    card: Card
    amount: float
    currency: Optional[str] = 'USD'


#----------------------------------------------------------------

import requests
from bs4 import BeautifulSoup


url = "http://books.toscrape.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


books = soup.find_all("article", class_="product_pod")


for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text.strip("£")
    availability = book.find("p", class_="instock availability").text.strip()
    image_url = url + book.img["src"]

    print("Название книги:", title)
    print("Цена:", price)
    print("Наличие на складе:", availability)
    print("Ссылка на фото:", image_url)