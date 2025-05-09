from flask import Blueprint
from controller import agregar_ronda,obtener_ronda,remover_ronda,modificar_ronda

ronda_bp = Blueprint("ronda_bp",__name__,url_prefix="/ronda")


ronda_bp.route('/:id',methods=['GET'])(obtener_ronda)

ronda_bp.route('/add',methods=['POST'])(agregar_ronda)

ronda_bp.route('/:id',methods=['PUT'])(modificar_ronda)

ronda_bp.route('/id',methods=['DELETE'])(remover_ronda)
