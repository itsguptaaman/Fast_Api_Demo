#  This is a Demo code of fast api

from fastapi import FastAPI
from enum import Enum

app = FastAPI()

# For Refrence use this commands
# Get :-To read data we use get method
# Post :- to create new order
# Put :- Udate data
# Delete :- delete data
# for inbuilt documentation :- http://127.0.0.1:8000/docs


@app.get("/hello/{name}")
async def hello(name):
    # url eg:- http://127.0.0.1:8000/hello/aman
    return f"Welcome to fast-api {name}"


class AvailableCuisines(str, Enum):
    indian = "indian"
    american = "american"
    italian = "italian"


food_items = {
    'indian': ["Samosa", "Dosa"],
    'american': ["Hot Dog", "Apple Pie"],
    'italian': ["Ravioli", "Pizza"]
}


@app.get("/get_items/{cuisine}")
async def get_items(cuisine: AvailableCuisines):
    # url eg:- http://127.0.0.1:8000/get_items/indian
    return food_items.get(cuisine)


coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}


@app.get("/get_coupon/{code}")
async def get_items(code: int):
    # url eg:-  http://127.0.0.1:8000/get_coupon/1
    return {'discount_amount': coupon_code.get(code)}
