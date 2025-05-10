from service import agregar_mesa_service,buscar_mesa_service,modificar_mesa_service,elimiar_mesa_service,agregar_jugador_a_mesa_service
from flask import request,jsonify
# Controllers
# Maneja la entrada (request) y salida (response). 
# Traduce lo que el usuario pide a una acción de dominio, y empaqueta la respuesta.

def agregar_mesa():
    data = request.get_json()
    respuesta = agregar_mesa_service(data)

    return (jsonify(respuesta),201) if respuesta['ok'] else (respuesta,400)


def agregar_jugador_a_mesa(id_mesa:int):
    data = request.get_json()
    id_jugador:int = data['id_jugador']
    respuesta = agregar_jugador_a_mesa_service(id_mesa,id_jugador)
    return (jsonify(respuesta),201) if respuesta['ok']  else (jsonify(respuesta),400)

def remover_mesa():
    return buscar_mesa_service()

def modificar_mesa():
    return modificar_mesa_service()

def obtener_mesa():
    return elimiar_mesa_service()
