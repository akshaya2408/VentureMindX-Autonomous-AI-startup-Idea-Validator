from fastapi import FastAPI
from backend.api.routes import router
from fastapi.middleware.cors import CORSMiddleware
import logging

logging.basicConfig(level=logging.DEBUG)

app = FastAPI(
    title="VentureMind API"
)

origins = [
    "http://localhost:5175",
    "http://127.0.0.1:5175",
    "http://localhost:5174",
    "http://127.0.0.1:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def home():
    return {"message": "VentureMind Running"}