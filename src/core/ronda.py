from ppt.core.jugador import Jugador

class Ronda():
    def __init__(self,eleccion_j1:str,eleccion_j2:str,numero:int,ganador:Jugador,perdedor:Jugador):
        self.eleccion_j1 = eleccion_j1
        self.eleccion_j2 = eleccion_j2
        self.ganador = ganador
        self.perderdor = perdedor
        self.numero = numero
    
    