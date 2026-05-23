from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_PATH = Path(__file__).resolve().parent / "data"

@app.get("/usuarios")
async def get_usuarios():
    with open(BASE_PATH / "usuarios.json", encoding="utf-8") as f:
        return json.load(f)

@app.get("/personas")
async def get_personas():
    with open(BASE_PATH / "personas.json", encoding="utf-8") as f:
        return json.load(f)