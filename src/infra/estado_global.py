from abc import ABC,abstractmethod
from domain.mesa import Mesa
from domain.jugador import Jugador

class SistemaDeJuego(ABC):
    

    @abstractmethod
    def crear():
        raise NotImplementedError('La funcion deberia ser implementada en una subclase')
    
    @abstractmethod
    def obtener():
        raise NotImplementedError('La funcion deberia ser implementada en una subclase')

    @abstractmethod
    def eliminar():
        raise NotImplementedError('La funcion deberia ser implementada en una subclase')



class GestorDeMesas(SistemaDeJuego):
    mesas={}
    siguiente_id_mesa:int=1
    
    @classmethod
    def crear(cls):
        #Obtenemos el id de la mesa siguiente
        siguiente_id = cls.siguiente_id_mesa

        #Creamos la mesa i le asignamos el id
        mesa = Mesa()   
        mesa.asignar_id(siguiente_id)

        #Guardamos la mesa en los Gestores
        cls.mesas[siguiente_id]= mesa

        #Aumentamos el siguiente_id_mesa
        cls.siguiente_id_mesa += 1

        return mesa
    
    @classmethod
    def obtener(cls,id):
        return cls.mesas.get(id)
    
    @classmethod
    def eliminar(cls,id):
        try:
            cls.mesas.pop(id)
            return True
        except:
            return False 
            

class GestorDeJugadores(SistemaDeJuego):
    personas={}
    siguiente_id_jugador:int=1

    @classmethod
    def crear(cls):
        #Obtenemos el id correspondiente para asignarselo al jugador nuevo
        id = cls.siguiente_id_jugador

        #Creamos una instancia del jugador y le asignamos el id
        usuario = Jugador()


        usuario.id = id
        
        #Guardamos el juegador en la coleccion de personas conectadas
        cls.personas[id] = usuario

        #Aumentamos el la variable de clase para el siguiente jugador a logear
        cls.siguiente_id_jugador+= 1
        

        return usuario
    
    @classmethod
    def obtener(cls,id) -> Jugador | None:
        return cls.personas.get(id)
    
    @classmethod
    def eliminar(cls,id):
        try:
            cls.personas.pop(id)
            return True
        except:
            return False
     