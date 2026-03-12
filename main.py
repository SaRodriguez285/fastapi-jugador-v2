from fastapi import FastAPI
from typing import List
from datetime import date
from enum import Enum, auto
from pydantic import BaseModel
from models.data import jugadores_data

app = FastAPI()

class PosicionFutbol(Enum):
    PORTERO = auto()
    DEFENSA = auto()
    MEDIOCAMPISTA = auto()
    DELANTERO = auto()
    EXTREMO = auto()

class Jugador(BaseModel):
    id: int
    name: str
    dorsal: int
    nacimiento: date
    altura: float
    posicion: PosicionFutbol
    equipo: str

jugadores: List[Jugador] = [
    Jugador(
        id=j["id"],
        name=j["name"],
        dorsal=j["dorsal"],
        nacimiento=j["nacimiento"],
        altura=j["altura"],
        posicion=PosicionFutbol[j["posicion"]],
        equipo=j["equipo"]
    )
    for j in jugadores_data
]

@app.get("/jugadores/")
def show_all_players():
    return jugadores

@app.get("/jugadores/{id}")
def show_one_player(id: int):
    return next((j for j in jugadores if j.id == id), {"error": "Jugador no encontrado"})

@app.get("/jugadores/compare/{id1}/{id2}")
def compare_two_players(id1: int, id2: int):
    j1 = next((j for j in jugadores if j.id == id1), None)
    j2 = next((j for j in jugadores if j.id == id2), None)
    if j1 and j2:
        return {"jugador_mas_alto": j1 if j1.altura > j2.altura else j2}
    return {"error": "Uno o ambos jugadores no encontrados"}

@app.get("/jugadores/equipo/{nombre}")
def show_equipo(nombre: str):
    j = next((j for j in jugadores if j.name.lower() == nombre.lower()), None)
    return {"equipo": j.equipo} if j else {"error": "Jugador no encontrado"}

@app.get("/jugadores/equipo/")
def show_players_by_team(equipo: str):
    return [j for j in jugadores if j.equipo == equipo]