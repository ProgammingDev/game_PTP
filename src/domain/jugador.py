
class Jugador:
    def __init__(self):
        self._nombre = None
        self.id = 0
        
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nuevo_nombre:str):
        if isinstance(nuevo_nombre,str) and nuevo_nombre:
            self.__nombre = nuevo_nombre
        else:
            raise('Nombre invalido')
        
    def to_dict(self) ->dict:
        return {
            'id':self.id,
            'nombre':self.__nombre
        }
    
