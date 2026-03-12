from fastapi import FastAPI
from typing import List
from datetime import date
from enum import Enum, auto
from pydantic import BaseModel

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