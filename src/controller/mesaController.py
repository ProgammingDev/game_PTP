from service import agregar_mesa_service,buscar_mesa_service,modificar_mesa_service,elimiar_mesa_service,agregar_jugador_a_mesa_service
from flask import request,jsonify
from domain.errores import JugadorNoEncontrado,MesaNoEncontrada,MesaLlenaError,JugadorYaExistente
# Controllers
# Maneja la entrada (request) y salida (response). 
# Traduce lo que el usuario pide a una acción de dominio, y empaqueta la respuesta.

def agregar_mesa():
    #Si pasa try la peticion se realizo correctamente
    try:
        data = request.get_json()
        mesa = agregar_mesa_service(data)

        return jsonify({
            'ok':True,
            'mensaje':'La mesa fue creada con exito',
            'data':mesa.to_dict()
            }),201
        
    #Si salta este error es que el jugador pasado no se encontro en el server 
    except JugadorNoEncontrado as e:
        return jsonify({
            'ok':False,
            'mensaje':str(e),
            'data':None
        }),404
    
     #Si salta este error hubo un problema con la mesa  
    except MesaLlenaError as e:
        return jsonify({
            'ok':False,
            'mensaje':str(e),
            'data':404
        })

    #Si salta este error hubo un problema con la codificacion 
    except (ValueError,TypeError) as e:
        return jsonify({
            'ok':False,
            'mensaje':str(e),
            'data':None
        }),500
    
   
    
    

     


def agregar_jugador_a_mesa(id_mesa:int):
    try:
        data = request.get_json()
        id_jugador:int = data['id_jugador']
        mesa = agregar_jugador_a_mesa_service(id_mesa,id_jugador)

        return jsonify({
            'ok':True,
            'mensaje':'El jugador fue agregado correctamente a la mesa',
            'data':mesa.to_dict()
        }),201
    #Se devuelve este error si el jugador no es encontrado
    except JugadorNoEncontrado as e:
        return jsonify({
            'ok':False,
            'mensaje':'Jugador no encontrado',
            'data':str(e)
        }),404
    #Se devuelve este error si el jugador ya existe en la mesa
    except JugadorYaExistente as e:
        return jsonify({
            'ok':False,
            'mensaje':'Jugador existente ya en la mesa',
            'data':str(e)
        }),409
    #Se devuelve este error si la mesa que intentar unirse el jugador esta llena
    except MesaLlenaError as e:
        return jsonify({
            'ok':False,
            'mensaje':'Mesa completa',
            'data':str(e)
        }),404
   #Se devuelve este error si la mesa a la que intenta unirse el jugador no existe 
    except MesaNoEncontrada as e:
        return jsonify({
            'ok':False,
            'mensaje':'Mesa no encontrada',
            'data':str(e)
        }),404
    #Se devuelve este error cuando hubo un problema de codificiacion
    except (ValueError,TypeError) as e:
         return jsonify({
            'ok':False,
            'mensaje':'Ocurrio un error inesperado',
            'data':str(e)
        }),500


def remover_mesa():
    return buscar_mesa_service()

def modificar_mesa():
    return modificar_mesa_service()

def obtener_mesa():
    return elimiar_mesa_service()
