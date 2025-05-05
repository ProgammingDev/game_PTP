from ppt.core.jugador import JugadorHumano

class EstadoGlobal:
    juegos: dict[str, any]
    usuarios:dict[str,any]

    @classmethod
    def crear_juego(cls):
        ''    
    
    @classmethod
    def obtener_juego(cls,id_juego):
        return cls.juegos.get(id_juego)
    

    @classmethod
    def agregar_usuario(cls,nombre):
        nuevo_id = len(cls.usuarios) + 1
        cls.usuarios[nuevo_id] = JugadorHumano(nombre)
