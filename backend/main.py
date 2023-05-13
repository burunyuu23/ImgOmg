import PostgresConnection as postgres_conn

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from data_request_model import Category

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


# @app.post("/add-test")
# async def add_test(parameters: Test):
#     print(parameters)
#     postgres_conn.add("INSERT INTO test VALUES ({}, '{}')".format(parameters.id, parameters.name))
#     return 'done'
