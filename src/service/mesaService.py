from service.jugadorService import buscar_jugador_service
from infra.estado_global import GestorDeMesas  
from infra.estado_global import GestorDeJugadores
from domain.reglaMesa import ReglaMesa
from domain.mesa import Mesa
from domain.mesa import Jugador
from domain.errores import JugadorNoEncontrado,MesaNoEncontrada
# SERVICES
# Contiene la lógica de negocio: qué pasa si un jugador se une, 
# si una mesa se llena, si hay que crear algo.

def agregar_mesa_service(data):        
        id:int = data.get('id_jugador')
        reglas = data.get('reglas')
       
        print('aaaaa')
        # Si el jugador no es encontrado responde la respuesta de buscar_jugador_service 
        jugador = GestorDeJugadores.obtener(id)

        if jugador is None: raise JugadorNoEncontrado(id)
            
        # e:espectadores,tpr:tiempoPorRonda,m:modo,cj:cantidadJugadores
        e,tpr,m,cj = reglas.get('espectadores'),reglas.get('tiempoPorRonda'),reglas.get('modo'),reglas.get('cantidadJugadores')
        print('a222aaaa')
        
        # Creamos reglas
        regla = ReglaMesa()

        # Asignamos las reglas que el usuario nos pide para la mesa ya que una mesa sin reglas no puede ser creada
        regla.permitir_espectadores = e
        regla.tiempo_por_ronda = tpr
        regla.modo = m
        regla.cantidad_max_de_jugadores = cj
        print('111aaaaa')
        
        # Creamos la mesa
        mesa = GestorDeMesas.crear()

        #Cambiamos la capacidad maxima de jugadores
        mesa.asignar_cantidad_maxima_de_jugadores(cj)

        # Asignamos las reglas a la mesa
        mesa.establecer_reglas(regla)
        
        #Agregamos el jugador principal osea el que creo la mesa
        mesa.agregar_jugador(jugador)

        return mesa
       
   

# Queda hacer esta parte hay que agregar jugadores a una mesa el jugador se pasa por el body asi no filtrar los datos
def agregar_jugador_a_mesa_service(id_mesa:int,id_jugador:int):
    jugador, mesa = GestorDeJugadores.obtener(id_jugador), GestorDeMesas.obtener(id_mesa)
    
    # Validamos que el jugador exista si el jugador no existe lanzamos un error de jugador no encontrado
    if (jugador is None) : raise JugadorNoEncontrado(id_jugador)

    # Validamos que mesa exista si mesa no existe lanzamos un error de mesa no encontrada
    if (mesa is None): raise MesaNoEncontrada(id_mesa)


    # Intentamos agregar un jugador a la mesa
    mesa.agregar_jugador(jugador)
    
    return mesa
    

       
    
    



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

    