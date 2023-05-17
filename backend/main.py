import uvicorn

import PostgresConnection as postgres_conn
import auth.pass_hash as ph

from fastapi import FastAPI, Body, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from backend.auth.jwt_handler import signJWT, decodeJWT
from data_request_model import Category, UserLogin, User
from backend.auth.jwt_bearer import jwtBearer

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", dependencies=[Depends(jwtBearer())])
async def pong():
    return {
        'id': 0,
        'name': 'John',
        'surname': 'Doe'
    }


@app.post('/user/signup', tags=["user"])
def user_signup(user: User = Body(default=None)):
    user.password = ph.hash(user.password)
    response = postgres_conn.insert_user(user)
    if response != 'done':
        raise HTTPException(status_code=403, detail=response)
    return signJWT(user.email)


@app.post('/user/check', tags=["user"])
def check_user(data: UserLogin):
    pdata = postgres_conn.check(data)
    if len(pdata) > 0:
        return ph.verify(data.password, pdata[0][2])


@app.post('/user/login', tags=["user"])
def user_login(user: UserLogin = Body(default=None)):
    if check_user(user):
        return signJWT(user.login + "/" + user.email)
    else:
        raise HTTPException(status_code=403, detail='Invalid login data!')


@app.get('/user/profile', dependencies=[Depends(jwtBearer())], tags=["user"])
def user_profile(token=Depends(jwtBearer())):
    decode_data = decodeJWT(token)
    pdata = postgres_conn.select_user(decode_data['userID'])
    return pdata


@app.get('/user/logout', tags=["user"])
def user_profile():
    data = {
        'login': '',
        'fullname': '',
        'email': '',
        'birthdate': '',
        'category': '',
    }
    return data


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8080)
