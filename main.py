from fastapi import FastAPI
from views import price

app = FastAPI()

@app.get('/')
def home():
    return('hello! This is PRICENITOR, your price monitor')

app.include_router(price)