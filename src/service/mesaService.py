from service.jugadorService import buscar_jugador_service
from infra.estado_global import GestorDeMesas  
from infra.estado_global import GestorDeJugadores
from domain.reglaMesa import ReglaMesa
from domain.mesa import Mesa
from domain.mesa import Jugador
# SERVICES
# Contiene la lógica de negocio: qué pasa si un jugador se une, 
# si una mesa se llena, si hay que crear algo.

def agregar_mesa_service(data):
    try:
        
        id:int = data.get('id_jugador')
        reglas = data.get('reglas')
       

        # Si el jugador no es encontrado responde la respuesta de buscar_jugador_service 
        jugador = GestorDeJugadores.obtener(id)

        if jugador is None: return {'ok':False,'mensaje':'Jugador no encontrado','data':None} 
            
        # e:espectadores,tpr:tiempoPorRonda,m:modo,cj:cantidadJugadores
        e,tpr,m,cj = reglas.get('espectadores'),reglas.get('tiempoPorRonda'),reglas.get('modo'),reglas.get('cantidadJugadores')
        
        # Creamos reglas
        regla = ReglaMesa()
        # Asignamos las reglas que el usuario nos pide para la mesa ya que una mesa sin reglas no puede ser creada
        regla.asignar_espectadores(e)
        regla.asignar_tiempoPorRonda(tpr)
        regla.asignar_modo(m)
        regla.asignar_cantidadJugadores(cj)
        
        # Creamos la mesa
        mesa = GestorDeMesas.crear()

        #Cambiamos la capacidad maxima de jugadores
        mesa.asignar_cantidad_maxima_de_jugadores(cj)

        # Asignamos las reglas a la mesa
        mesa.establecer_reglas(regla)
        
        #Agregamos el jugador principal osea el que creo la mesa
        mesa.agregar_jugador(jugador)

        return {
            'ok':True,
            'mensaje':'La mesa fue creada con exito',
            'data':mesa.to_dict()
        }
    
    except (ValueError,TypeError) as e:
        return{
            'ok':False,
            'mensaje':'Error inesperado',
            'data': str(e)
        }

# Queda hacer esta parte hay que agregar jugadores a una mesa el jugador se pasa por el body asi no filtrar los datos
def agregar_jugador_a_mesa_service(id_mesa:int,id_jugador:int):
    try:
        jugador =GestorDeJugadores.obtener(id_jugador) 
        print(jugador,'Es objeto?')
        mesa = GestorDeMesas.obtener(id_mesa)
        
        # Validamos que el jugador y la mesa existan a la que se quiere unir si no existe devolvemos dicho mensaje
        if (jugador is None) or (mesa is None): return {
            'ok':False,
            'mensaje':'La mesa o el jugador no fueron encontrada',
            'data':None
        }

        # Una vez validado el jugador lo agregamos a la mesa
        mesa.agregar_jugador(jugador)
        
        return {
            'ok':True,
            'mensaje':'El jugador fue agregado correctamente a la mesa',
            'data':mesa.to_dict()
        }
    
    except(ValueError, TypeError) as e:
        return{
            'ok':False,
            'mensaje':'Ocurrio un error inesperado',
            'data':str(e)
        }
    
    



def buscar_mesa_service(id_mesa:int):
    respuesta:None | Mesa= GestorDeMesas.obtener(id_mesa)

    if not respuesta : return {
        'ok':False,
        'mensaje':'Mesa no encontrada',
        'data':None
    } 

    return {
        'ok':True,
        'mensaje':'Mesa encontrada',
        'data':respuesta.to_dict()
    }


def modificar_mesa_service(body):
    return ''


def elimiar_mesa_service(body):
    return ''

    