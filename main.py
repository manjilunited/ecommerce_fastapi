from fastapi import FastAPI
from utils.db import  create_db_and_tables
from category import router as categories_router



app=FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(categories_router.router)



