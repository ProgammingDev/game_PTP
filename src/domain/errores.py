class JugadorYaExistente(Exception):
    def __init__(self,jugador_id):
        super().__init__(f'El jugador con ID {jugador_id} ya esta en la mesa')

class MesaLlenaError(Exception):
    def __init__(self):
        super().__init__("No hay asientos disponibles en la mesa.")