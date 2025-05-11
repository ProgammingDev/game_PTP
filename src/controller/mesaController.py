from service import agregar_mesa_service,buscar_mesa_service,modificar_mesa_service,listado_de_mesas_service,agregar_jugador_a_mesa_service
from flask import request,jsonify
from domain.errores import JugadorNoEncontrado,MesaNoEncontrada,MesaLlenaError,JugadorYaExistente
from domain.mesa import Mesa
# Controllers
# Maneja la entrada (request) y salida (response). 
# Traduce lo que el usuario pide a una acción de dominio, y empaqueta la respuesta.

# Controlador para crear una mesa con respectivo usuario que decidio crearla
def agregar_mesa():
    # Si pasa try la peticion se realizo correctamente
    try:
        data = request.get_json()
        mesa = agregar_mesa_service(data)

        return jsonify({
            'ok':True,
            'mensaje':'La mesa fue creada con exito',
            'data':mesa.to_dict()
            }),201
        
    # Si salta este error es que el jugador pasado no se encontro en el server 
    except JugadorNoEncontrado as e:
        return jsonify({
            'ok':False,
            'mensaje':'Jugador no encontrado',
            'data':str(e)
        }),404
    
     # Si salta este error hubo un problema con la mesa  
    except MesaLlenaError as e:
        return jsonify({
            'ok':False,
            'mensaje':'Mesa completada',
            'data':str(e)
        }),400

    # Si salta este error hubo un problema con la codificacion 
    except (ValueError,TypeError) as e:
        return jsonify({
            'ok':False,
            'mensaje':'Problema en la codificacion',
            'data':str(e)
        }),500
    
# Controlador para agregar un jugador a la mesa 

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
    # Se devuelve este error si el jugador no es encontrado
    except  JugadorNoEncontrado as e:
        return jsonify({
            'ok':False,
            'mensaje':'Jugador no encontrado',
            'data':str(e)
        }),404
    # Se devuelve este error si el jugador ya existe en la mesa
    except JugadorYaExistente as e:
        return jsonify({
            'ok':False,
            'mensaje':'Jugador existente ya en la mesa',
            'data':str(e)
        }),409
    # Se devuelve este error si la mesa que intentar unirse el jugador esta llena
    except MesaLlenaError as e:
        return jsonify({
            'ok':False,
            'mensaje':'Mesa completa',
            'data':str(e)
        }),404
   #  Se devuelve este error si la mesa a la que intenta unirse el jugador no existe 
    except MesaNoEncontrada as e:
        return jsonify({
            'ok':False,
            'mensaje':'Mesa no encontrada',
            'data':str(e)
        }),404
    # Se devuelve este error cuando hubo un problema de codificiacion
    except (ValueError,TypeError) as e:
         return jsonify({
            'ok':False,
            'mensaje':'Ocurrio un error inesperado',
            'data':str(e)
        }),500

# Buscara una mesa por id
def obtener_mesa_por_id(id_mesa:int):
    try:
        mesa = buscar_mesa_service(id_mesa)
        
        return jsonify({
            'ok':False,
            'mensaje':'Mesa encontrada con exito',
            'data':mesa.to_dict()
        })
    
    # Se devuelve este error si la mesa buscada no es encontrada
    except MesaNoEncontrada as e:
        return jsonify({
            'ok':False,
            'mensaje':'Mesa no encontrada',
            'data': str(e)
        })
    
    # Se devuelve este error cuando hubo un problema de codificiacion
    except (ValueError,TypeError) as e:
         return jsonify({
            'ok':False,
            'mensaje':'Ocurrio un error inesperado',
            'data':str(e)
        }),500


def obtener_listado_de_mesas():
    try:
        limit = request.args.get('limit',default=10,type=int)
        mesas:dict[int,Mesa] = listado_de_mesas_service({'limit':limit})
       
        return jsonify({
            'ok':True,
            'mensaje':'Mesas extraidas',
            'data':[j.to_dict()  for _ , j in mesas.items()]
        })
    
    # Se devuelve este error cuando hubo un problema de codificiacion
    except (ValueError,TypeError) as e:
         return jsonify({
            'ok':False,
            'mensaje':'Ocurrio un error inesperado',
            'data':str(e)
        }),500


def remover_mesa():
   return ''

def modificar_mesa():
    return modificar_mesa_service()

