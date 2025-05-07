from ppt.core.jugador import Jugador
from ppt.core.juego import Juego

class Sala():
    nro_sala:int= 0

    def __init__(self):
        self.__jugador1:Jugador= None
        self.__jugador2:Jugador = None
        self.__juegoActivo:Juego= None
        self.juegos:list[Juego] =None
        self.turnoActual:int=0


    def asignar_jugador(self,regJugador:Jugador):
        #Si existe lugar en alguno de los dos asientos osea Jugador1 o Jugador 2 lo inserta ahi si devuelve sala completa  
        if not self.__jugador1:
            self.__jugador1 = regJugador
            return {"ok": True, "mensaje": "Jugador asignado como jugador 1"}
        
        if self.__jugador2:
            self.__jugador2 = regJugador
            return {"ok": True, "mensaje": "Jugador asignado como jugador 1"}
         
        return {"ok": False, "mensaje": "Sala llena"}
    
    def crear_juego(self,reglas):
        #Valida que realmente existan ambos jugadores para iniciar un juego
        if not(self.__jugadoresExistentes) : return

        #En esta seccion se debera crear el juego para que los participantes puedan jugar
        juego = Juego().asingar_jugadores(self.__jugador1,self.__jugador2) 

        #


    def __jugadoresExistentes(self):
        if self.__jugador1 and self.__jugador2:
            return True