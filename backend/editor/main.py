import sys
import uvicorn
from fastapi import FastAPI, Body, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:5173"],
    allow_credentials=True,
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


if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", port=8081)