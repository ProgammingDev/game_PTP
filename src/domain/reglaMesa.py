class ReglaMesa:
    def __init__(self):
        self.espectadores = None
        self.tiempoPorRonda = None
        self.modo = None
        self.cantidadJugadores=None

    def asignar_espectadores(self,hay_espectadores):
        self.espectadores = hay_espectadores

    def asignar_tiempoPorRonda(self,tiempo):
        self.tiempoPorRonda = tiempo

    def asignar_modo(self,modo):
        self.modo = modo
    
    def asignar_cantidadJugadores(self,cantidadJugadores):
        self.cantidadJugadores = cantidadJugadores
    
    def to_dict(self):
        return {
            'espectadores':self.espectadores,
            'tiempoPorRonda':self.tiempoPorRonda,
            'modo':self.modo,
            'cantidadJugadores':self.cantidadJugadores
        }
