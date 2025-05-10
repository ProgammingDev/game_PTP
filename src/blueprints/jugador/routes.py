from flask import request,Blueprint,jsonify,abort
from controller import agregar_jugador,modificar_jugador,obtener_jugador,remover_jugador
jugador_bp = Blueprint('Jugador',__name__,url_prefix='/jugador')


#Devuelve un jugador en especifico.
jugador_bp.route('/<int:id>',methods=['GET'])(obtener_jugador)

#Crea un jugador nuevo
jugador_bp.route('/add',methods=['POST'])(agregar_jugador)

#Modifica un jugador
jugador_bp.route('/<id>',methods=['PUT'])(modificar_jugador)

#Elimina un jugador
jugador_bp.route('/<int:id>',methods=['DELETE'])(remover_jugador)

