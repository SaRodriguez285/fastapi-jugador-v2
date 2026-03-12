from datetime import date
from main import Jugador, PosicionFutbol

jugadores = [
    Jugador(id=1, name="Lionel Messi", dorsal=10, nacimiento=date(1987,6,24), altura=1.70, posicion=PosicionFutbol.DELANTERO, equipo="Inter Miami"),
    Jugador(id=2, name="Cristiano Ronaldo", dorsal=7, nacimiento=date(1985,2,5), altura=1.87, posicion=PosicionFutbol.DELANTERO, equipo="Al Nassr"),
    Jugador(id=3, name="Manuel Neuer", dorsal=1, nacimiento=date(1986,3,27), altura=1.93, posicion=PosicionFutbol.PORTERO, equipo="Bayern Munich"),
    Jugador(id=4, name="Kevin De Bruyne", dorsal=17, nacimiento=date(1991,6,28), altura=1.81, posicion=PosicionFutbol.MEDIOCAMPISTA, equipo="Manchester City"),
]