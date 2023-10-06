from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id:int
    username:str
    email:str

    class Config:
        orm_mode = True

class Product(BaseModel):
    id:int
    name:str
    price:float

    class Config:
        orm_mode = True

class Order(BaseModel):
    id:int
    user_id:int

    class Config:
        orm_mode = True


class OrderProduct(BaseModel):
    id:int
    order_id:int
    product_id:int
    quantity:int

    class Config:
        orm_mode = True
