from service import agregar_ronda_service,buscar_ronda_service,modificar_ronda_service,elimiar_ronda_service

def agregar_ronda():
    return agregar_ronda_service()

def modificar_ronda():
    return modificar_ronda_service()
    
def remover_ronda():
    return elimiar_ronda_service()
    
def obtener_ronda():
    return buscar_ronda_service()