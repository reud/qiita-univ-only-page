import traceback

import requests
from fastapi import FastAPI, HTTPException
from starlette.requests import Request
import os

app = FastAPI()



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
