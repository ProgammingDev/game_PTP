
class Jugador:
    def __init__(self):
        self.__nombre = None
        self.id = 0
        

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self,nombre:str):
        
        self.__nombre = nombre
        
    def to_dict(self) ->dict:
        return {
            'id':self.id,
            'nombre':self.__nombre
        }