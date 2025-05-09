from typing import TypedDict

class OpcionRespuesta(TypedDict):
    opcion:str
    id:int

    
class CrearJuegoRequest(TypedDict):
    rondasTotales:int
    empate:bool
    creador_id:int