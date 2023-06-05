import sys

import uvicorn

import PostgresConnection
import jwt_utils.pass_hash as ph

from fastapi import FastAPI, Body, Depends, HTTPException, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from jwt_utils.jwt_handler import signJWT, decodeJWT
from data_request_model import UserLogin, User
from jwt_utils.jwt_bearer import jwtBearer

app = FastAPI()
router = APIRouter(prefix="/api/auth")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost/"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

PC = PostgresConnection.PostgreConn(sys.argv[1:])


@router.get("/", dependencies=[Depends(jwtBearer())])
async def pong():
    return {
        'id': 0,
        'name': 'John',
        'surname': 'Doe'
    }


@router.post('/user/signup', tags=["user"])
def user_signup(user: User = Body(default=None)):
    user.password = ph.hash(user.password)
    response = PC.insert_user(user)
    if response != 'done':
        raise HTTPException(status_code=403, detail=response)
    return signJWT(user.email)


@router.post('/user/check', tags=["user"])
def check_user(data: UserLogin):
    pdata = PC.check(data)
    if len(pdata) > 0:
        return ph.verify(data.password, pdata[0][2])


@router.post('/user/login', tags=["user"])
def user_login(user: UserLogin = Body(default=None)):
    if check_user(user):
        return signJWT(user.login + "/" + user.email)
    else:
        raise HTTPException(status_code=403, detail='Invalid login data!')


@router.get('/user/profile', dependencies=[Depends(jwtBearer())], tags=["user"])
def user_profile(token=Depends(jwtBearer())):
    decode_data = decodeJWT(token)
    pdata = PC.select_user(decode_data['userID'])
    return pdata


@router.get('/user/logout', tags=["user"])
def user_profile():
    data = {
        'login': '',
        'fullname': '',
        'email': '',
        'birthdate': '',
        'category': '',
    }
    return data


app.include_router(router)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=int(sys.argv[4]))
