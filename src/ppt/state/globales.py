from ppt.core.jugador import JugadorHumano
from ppt.core.juego import Juego
from ppt.core.tipos import CrearJuegoRequest
class EstadoGlobal:
    juegos = {}
    usuarios={}



    @classmethod
    def crear_juego(cls,req:CrearJuegoRequest):
        empate,rondasTotales,creador_id=req.get('empate'),req.get('rondasTotales'),req.get('creador_id')
        
        #Esto es trabajo del middleware
        obj_usuario = cls.obtener_usuario(id)
        if not(obj_usuario) : return None
    

        juego = Juego()
        juego.asignar_empate = empate
        juego.asignar_rondasTotales= rondasTotales
        juego.asingar_jugador_1 = creador_id
        
        cantidad_juegos = len(cls.juegos)
        cls.juegos[cantidad_juegos] = juego

        return cantidad_juegos




        
    
    @classmethod
    def obtener_juego(cls,id_juego):
        return cls.juegos.get(id_juego)
    

    @classmethod
    def agregar_usuario(cls,nombre):
        #Obtenemos una instancia del jugador humano para poder guardarla en el diccionario global
        #Obtenemos la cantidad de Jugadores que se han inicializados 
        humano,cantidad_humano = JugadorHumano(nombre),JugadorHumano.get_cantidad()
          
        cls.usuarios[cantidad_humano] =humano
       
        return cantidad_humano


    @classmethod
    def obtener_usuario(cls,id):
        return cls.usuarios.get(id)


    


    @classmethod
    def get_juegos(cls):
        return cls.juegos




