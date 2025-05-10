from infra.estado_global import GestorDeJugadores
# SERVICES
# Contiene la lógica de negocio: qué pasa si un jugador se une, 
# si una mesa se llena, si hay que crear algo.

def agregar_jugador_service(nombre:str):    
    try:
       
        jugador = GestorDeJugadores.crear()
        jugador.nombre = nombre
    
        return {
            'ok':True,
            'mensaje':'Usario creado correctamente',
            'data':jugador.to_dict()
        }
        
    except:
        return {
            'ok':False,
            'mensaje':'Problema no especificado',
            'data':None
        }


    

def buscar_jugador_service(id):
    try:
        jugador = GestorDeJugadores.obtener(id)
        if not jugador:
            return {
                'ok':False,
                'mensaje':'Jugado no encontrado',
                'data':None
            }
            
        
        return {
                'ok':True,
                'mensaje':'Jugador encontrado',
                'data':jugador.to_dict()
            }
    except:
        return {
            'ok':False,
            'mensaje':'Problema no especificado',
            'data':None
        }

def modificar_jugador_service(body):
    return ''


def eliminar_jugador_service(id):
    try:
        return {'ok':True,'mensaje':'Jugador eliminado'} if GestorDeJugadores.eliminar(id) else {'ok':True,'mensaje':'Jugador inexistente'}

    except:
        return {
            'ok':False,
            'mensaje':'Problema no especificado',
        }
    

    