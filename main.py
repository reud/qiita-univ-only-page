from fastapi import FastAPI
from starlette.requests import Request

app = FastAPI()


@app.get("/")
def read_root():
    return {"200": "Welcome To Heroku"}


@app.get("/himitu")
def read_item(request: Request):
    k = request.headers.get('Authorization')
    return {"Authorization Header": k}