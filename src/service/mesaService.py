from service.jugadorService import buscar_jugador_service
from infra.estado_global import GestorDeMesas  
from domain.reglaMesa import ReglaMesa
#SERVICES
#Contiene la lógica de negocio: qué pasa si un jugador se une, 
# si una mesa se llena, si hay que crear algo.

def agregar_mesa_service(data):
    try:
        
        id:int = data.get('id_jugador')
        reglas = data.get('reglas')
       

        # Si el jugador no es encontrado responde la respuesta de buscar_jugador_service 
        respuesta = buscar_jugador_service(id)
        if not respuesta['ok']: return respuesta 
        
        
        

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
        jugador = respuesta['data']
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



def buscar_mesa_service(body):
    return ''


def modificar_mesa_service(body):
    return ''


def elimiar_mesa_service(body):
    return ''

    