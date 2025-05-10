from __future__ import annotations  # 👈 al principio del archivo
from domain.jugador import Jugador
from typing import TypedDict
from domain.reglaMesa import ReglaMesa

class SlotJugador(TypedDict):
    jugador:Jugador
    listo:bool


class Mesa():
    def __init__(self):
       self.id_mesa:int = 0
       self.jugadores:list[SlotJugador| None]= []
       self.juegoActual=None
       self.reglasMesa:ReglaMesa | None=None


    def agregar_jugador(self,regJugador:Jugador):
        asientos = self.jugadores
        for i in range(0,len(asientos)):
            # Por cada iteracion nos fijamos en el array Jugadores si hay un asiento vacio si hay un asiento nos colocamos ahi
            # si todos los asientos estan ocupados lanzamos un error que no se encontre asiento
           
            if not asientos[i]:
                asientos[i] = {
                    'jugador':regJugador,
                    'listo':False,
                }
                break
            elif i == len(asientos)-1:
                raise ValueError('No se encontro asiento')


    def establecer_reglas(self,reglas):
        self.reglasMesa= reglas

    def asignar_cantidad_maxima_de_jugadores(self,numero:int):
        if not numero > 1 : raise ValueError('Dato invalido')

        self.jugadores = [None] * numero

    def asignar_id(self,id):
        self.id_mesa = id

    
    def to_dict(self):
        return {
            'id_mesa':self.id_mesa,
            'jugadores':[
            j if j is None else {
                "jugador": j["jugador"],
                "listo": j["listo"]
            }
            for j in self.jugadores
        ],
            'juegoActual':self.juegoActual,
            'reglasMesa':self.reglasMesa.to_dict() if self.reglasMesa else None ,
        }
        

