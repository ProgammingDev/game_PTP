class ReglaMesa:
    def __init__(self):
        self.__permitir_espectadores:bool = False
        self.__tiempo_por_ronda = 30
        self.__modo = 'normal'
        self.__cantidad_max_de_jugadores=2

    @property
    def permitir_espectadores(self):
        return self.__permitir_espectadores
    
    @permitir_espectadores.setter
    def permitir_espectadores(self,nuevo_permitir_espectadores):
       self.__permitir_espectadores = nuevo_permitir_espectadores
       

    @property
    def tiempo_por_ronda(self):
        return self.__tiempo_por_ronda
    
    @tiempo_por_ronda.setter
    def tiempo_por_ronda(self,nuevo_tiempo_por_ronda):
        if not nuevo_tiempo_por_ronda >= 30 : raise ValueError('El tiempo no puede ser menor a 30')

        self.__tiempo_por_ronda = nuevo_tiempo_por_ronda

    @property
    def modo(self):
        return self.__modo
    
    @modo.setter
    def modo(self,nuevo_modo):
        self.__modo = nuevo_modo

    @property
    def cantidad_max_de_jugadores(self):
        return self.__cantidad_max_de_jugadores
    
    @cantidad_max_de_jugadores.setter
    def cantidad_max_de_jugadores(self,nueva_cantidad_max_de_jugadores):
        if not nueva_cantidad_max_de_jugadores > 0 : raise ValueError('La cantidad de jugadores no puede ser menor a 1')
        self.__cantidad_max_de_jugadores = nueva_cantidad_max_de_jugadores


    
    def to_dict(self):
        return {
            'espectadores':self.permitir_espectadores,
            'tiempoPorRonda':self.tiempo_por_ronda,
            'modo':self.modo,
            'cantidadJugadores':self.cantidad_max_de_jugadores
        }
