from fastapi import FastAPI
from utils.db import  create_db_and_tables
from category import router as categories_router
from Product import router as Products_router
from product_varients import router as product_varients_router 
from order import router as order_router
from user import router as user_router 
from cart import router as cart_router 


app=FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(categories_router.router)
app.include_router(Products_router.router)
app.include_router(product_varients_router.router)   
app.include_router(order_router.router)
app.include_router(user_router.router)
app.include_router(cart_router.router)  



