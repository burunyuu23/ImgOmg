import uvicorn

import PostgresConnection as postgres_conn
from fastapi import Depends
from fastapi.responses import RedirectResponse
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from data_request_model import Test
from fastapi_keycloak import FastAPIKeycloak, OIDCUser

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
idp = FastAPIKeycloak(
    server_url="http://localhost:8080/",
    client_id="imgomg-client",
    client_secret="NWGsKxBAYnB2pP0kLPn8RVo5lk7d6emy",
    admin_client_secret="BIcczGsZ6I8W5zf0rZg5qSexlloQLPKB",
    realm="imgomg-realm",
    callback_uri="http://localhost:8081/callback"
)
idp.add_swagger_config(app)


@app.get("/")
async def pong():
    return {
        'id': 0,
        'name': 'John',
        'surname': 'Doe'
    }


@app.post("/add-test")
async def add_test(parameters: Test):
    print(parameters)
    postgres_conn.add("INSERT INTO test VALUES ({}, '{}')".format(parameters.id, parameters.name))
    return 'done'


@app.get("/user")  # Requires logged in
def current_users(user: OIDCUser = Depends(idp.get_current_user())):
    return user


@app.get("/admin")  # Requires the admin role
def company_admin(user: OIDCUser = Depends(idp.get_current_user(required_roles=["admin"]))):
    return f'Hi admin {user}'


@app.get("/login")
def login_redirect():
    return RedirectResponse(idp.login_uri)

@app.get("/api/user/current")
def current_user():
    return idp.get_current_user()

@app.get("/callback")
def callback(session_state: str, code: str):
    return idp.exchange_authorization_code(session_state=session_state, code=code)  # This will return an access token


if __name__ == '__main__':
    uvicorn.run('app:app', host="127.0.0.1", port=8081)
