from flask import Blueprint
from controller import obtener_juego,agregar_juego,modificar_juego,remover_juego

juego_bp = Blueprint('juego_bp',__name__,url_prefix='/juego')

juego_bp.route('/:id',methods=['GET'])(obtener_juego)

juego_bp.route('/add',methods=['POST'])(agregar_juego)

juego_bp.route('/:id',methods=['PUT'])(modificar_juego)

juego_bp.route('/:id',methods=['DELETE'])(remover_juego)