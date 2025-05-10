from flask import request,jsonify
from service import agregar_jugador_service,buscar_jugador_service,modificar_jugador_service,eliminar_jugador_service

#Controllers
#Maneja la entrada (request) y salida (response). 
#Traduce lo que el usuario pide a una acción de dominio, y empaqueta la respuesta.

#agregar_jugador envia a service un body con los datos del usuario a crear
#RESPONDE A UNA LLAMADA POST
def agregar_jugador():
    data  = request.get_json()
    nombre:str = data.get('nombre')
    nombre = nombre.strip()

    if not nombre:
        return {
            'ok':False,
            'mensaje':'El nombre no puede estar vacio',
            'data':None
        },400
    
    respuesta = agregar_jugador_service(nombre)
  
    return (jsonify(respuesta),201) if respuesta['ok'] else (jsonify(respuesta),400) 
        

    

#obtener_jugador envia a service un id del usuario que desea buscar y service lo devuelve
def obtener_jugador(id:int ):
    if not isinstance(id,int):
        return {
            'ok':False,
            'mensaje':'El id debe ser un numero',
            'data':None
        }
    
    respuesta = buscar_jugador_service(id)

    return (jsonify(respuesta),200) if respuesta['ok'] else (jsonify(respuesta),400) 

#modificar_jugador envia a service un id del usuario que desea modificar y el body con los datos actualizados
def modificar_jugador():
    return modificar_jugador_service()

#remover_jugador envia a service un id del usuario que desea remover de la aplicacion
def remover_jugador(id:int):
    if not isinstance(id,int):
        return {
            'ok':False,
            'mensaje':'El id debe ser un numero',
        }
    
    return eliminar_jugador_service(id)