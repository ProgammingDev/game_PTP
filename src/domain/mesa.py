from __future__ import annotations  # 👈 al principio del archivo
from domain.jugador import Jugador

class Mesa():
    nro_mesa:int= 0

    def __init__(self):
       id_mesa:int = 0
       jugadores:list[Jugador]= []
       juegoActual=None
       reglasMesa=None


    
    def asignar_id(self,id):
        self.id_mesa = id

    def obtener_numero_de_mesas(cls):
        return cls.nro_mesa
    

    def asignar_jugador(self,regJugador:Jugador):
        jugador_en_mesa = {
            'jugador':None,
            'listo':False
        }

        if(self.reglasMesa == None): return 'El campo reglas debe estar lleno'


        #Si existe lugar en alguno de los dos asientos osea Jugador1 o Jugador 2 lo inserta ahi si devuelve sala completa  
        if not self.__jugador1:
            self.__jugador1 = regJugador
            return self.__jugador1
        
        if self.__jugador2:
            self.__jugador2 = regJugador
            return 
         
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