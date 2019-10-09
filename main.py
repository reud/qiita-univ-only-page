import traceback

import requests
from fastapi import FastAPI, HTTPException
from starlette.requests import Request
from starlette.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

@app.get("/")
def read_root():
    return {"200": "Welcome To Heroku"}


@app.get("/himitu/{user_id}")
def read_item(user_id: str, request: Request):
    k = request.headers.get('Authorization')
    if not k:
        raise HTTPException(status_code=403, detail="forbidden")
    headers = {'Authorization': k}
    # 適宜読み替えてください
    try:
        r = requests.get(f'https://{ os.getenv("TENANT") }.auth0.com/api/v2/users/{user_id}', headers=headers)
    except:
        raise HTTPException(status_code=403, detail=traceback.print_exc())
    j = r.json()
    try:
        # checker
        n = j['nickname']

        return {'himitsu': os.getenv('HIMITSU')}
    except:
        raise HTTPException(status_code=403, detail='forbidden')
