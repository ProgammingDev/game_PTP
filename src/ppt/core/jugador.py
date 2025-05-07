import random
from ppt.core.tipos import OpcionRespuesta
from ppt.core.sala import Sala
from abc import ABC, abstractmethod

class Jugador(ABC):
    cantidad = 0

    @abstractmethod
    def __init__(self, nombre):
        self.__nombre = nombre
        historial:list[Sala]= []
        self.__eleccionActual = {
            'opcion':'',
            'id':-1
        }

        self.sumar_cantidad()
        
        

    @abstractmethod
    def elegir(self):
        raise NotImplementedError("Este método debe ser implementado por la subclase")
    
    @classmethod
    def sumar_cantidad(cls):
        cls.cantidad += 1

    def sumar_punto(self):
       self.__puntaje = self.__puntaje +1 
     # Getters y setters

    def get_nombre(self):
        return self.__nombre

    def get_opciones(self):
        return self.__opciones
    
    def get_eleccion_actual_nombre(self):
        return self.__eleccionActual.get('opcion')

    def get_eleccion_actual_id(self):
        return self.__eleccionActual.get('id')
    
    def set_eleccion_actual(self, valor):
        self.__eleccionActual = valor
    
    def get_puntaje(self):
        return self.__puntaje

    def set_puntaje(self, valor):
        self.__puntaje = valor
    

    @classmethod
    def get_cantidad(cls):
        return  cls.cantidad

class JugadorCPU(Jugador):
    def __init__(self):
        super().__init__("CPU")

    def elegir(self):
        eleccionCPU = random.choice(list(self.get_opciones().items()))
        self.set_eleccion_actual({'opcion':eleccionCPU[0],'id':eleccionCPU[1]})



class JugadorHumano(Jugador):
    def __init__(self, nombre):
        super().__init__(nombre)

    def elegir(self):
        eleccion = None
        while eleccion not in self.get_opciones().keys():
            eleccion = input(f"{self.get_nombre()}, elige piedra, papel, o tijera: ").strip()

        self.set_eleccion_actual({'opcion':eleccion,'id':self.get_opciones()[eleccion]})
    

