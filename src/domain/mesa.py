from __future__ import annotations  # 👈 al principio del archivo
from domain.jugador import Jugador
from typing import TypedDict
from domain.reglaMesa import ReglaMesa
from domain.errores import MesaLlenaError,JugadorYaExistente

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
        try:
            if not self.__es_jugador_valido_para_agregar(regJugador):
                raise JugadorYaExistente(regJugador.id)

            index = next(i for i,j in enumerate(self.jugadores) if j is None)
            
            self.jugadores[index] = {
                    'jugador':regJugador,
                    'listo':False,
                }

        except StopIteration:
            raise MesaLlenaError()
            


    def establecer_reglas(self,reglas):
        self.reglasMesa= reglas

    def asignar_cantidad_maxima_de_jugadores(self,numero:int):
        if not numero > 1 : raise ValueError('Dato invalido')

        self.jugadores = [None] * numero

    def asignar_id(self,id):
        self.id_mesa = id

    
    def __es_jugador_valido_para_agregar(self,reg_jugador:Jugador):
        try:
            # Si el jugador ya existe con ese id, no se puede agreagar
            jugadores:list[Jugador] = [jugador['jugador'] for jugador in self.jugadores if jugador is not None]
          
                 
            _ = next(i for i,j in enumerate(jugadores) if j == reg_jugador)
           
            return False # Devuelve falso porque siginifica que ya existe
        
        except StopIteration:
            return True # Devuelve verdadero si no existe siginifica que se puede agregar

        except (ValueError,TypeError,KeyError) as e:
            # Por seguridad a algo no agregamos al participante
            print(f"[ERROR inesperado] {type(e).__name__}: {e}")
            return False # Devuelve falso si existe un error inesperado por las dudas no lo agregamos 



    def to_dict(self):
        return {
            'id_mesa':self.id_mesa,
            'jugadores':[
            j if j is None else {
                "jugador": j["jugador"].to_dict(),
                "listo": j["listo"]
            }
            for j in self.jugadores
        ],
            'juegoActual':self.juegoActual,
            'reglasMesa':self.reglasMesa.to_dict() if self.reglasMesa else None ,
        }
        


