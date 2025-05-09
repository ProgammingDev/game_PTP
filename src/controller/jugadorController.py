from flask import request
from service import agregar_jugador_service,buscar_jugador_service,modificar_jugador_service,elimiar_jugador_service

#En controller no ponemos logica de servicio solamente manejamos la peticion para darsela a service

#agregar_jugador envia a service un body con los datos del usuario a crear
def agregar_jugador():
    data  = request.get_json()
    return agregar_jugador_service()  

#obtener_jugador envia a service un id del usuario que desea buscar y service lo devuelve
def obtener_jugador():
    return buscar_jugador_service()

#modificar_jugador envia a service un id del usuario que desea modificar y el body con los datos actualizados
def modificar_jugador():
    return modificar_jugador_service()

#remover_jugador envia a service un id del usuario que desea remover de la aplicacion
def remover_jugador():
    return elimiar_jugador_service()