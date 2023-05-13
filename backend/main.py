import uvicorn

import PostgresConnection as postgres_conn

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

from backend.auth.jwt_handler import signJWT
from data_request_model import Category, UserLogin, User
from backend.auth.jwt_bearer import jwtBearer

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def pong():
    return {
        'id': 0,
        'name': 'John',
        'surname': 'Doe'
    }


@app.post('/user/signup', tags=["user"])
def user_signup(user: User = Body(default=None)):
    postgres_conn.insert_user(user)
    return signJWT(user.email)


@app.post('/user/check', tags=["user"])
def check_user(data: UserLogin):
    pdata = postgres_conn.check(data)
    if len(pdata) > 0:
        return pdata[0][2] == data.password


@app.post('/user/login', tags=["user"])
def user_login(user: UserLogin = Body(default=None)):
    if check_user(user):
        return signJWT(user.email)
    else:
        return {
            "error": "Invalid login details!"
        }


@app.get('/user/test')
def test():
    data = postgres_conn \
        .add('''SELECT email, password FROM users WHERE email = 'ezzfvkoko@gmail.com';''')
    return {
        "ansa": data
    }


@app.get('/user/test2')
def test():
    data = postgres_conn \
        .add('''SELECT * FROM users;''')
    return {
        "ansa": data
    }


@app.get('/user/test3')
def test():
    data = postgres_conn \
        .add('''SELECT email, password FROM users WHERE email = 'ezzfvskoko@gmail.com';''')
    return {
        "ansa": data
    }


# @app.post("/add-test")
# async def add_test(parameters: Test):
#     print(parameters)
#     postgres_conn.add("INSERT INTO test VALUES ({}, '{}')".format(parameters.id, parameters.name))
#     return 'done'

if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8080)
