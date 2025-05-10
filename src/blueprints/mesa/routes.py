from flask import Blueprint,jsonify
from controller import agregar_mesa,obtener_mesa,remover_mesa,modificar_mesa
mesa_bp =Blueprint('sala',__name__,url_prefix='/mesa')



mesa_bp.route('/:id',methods=['GET'])(obtener_mesa)

mesa_bp.route('/add',methods=['POST'])(agregar_mesa)

mesa_bp.route('/:id',methods=['PUT'])(modificar_mesa)

mesa_bp.route('/:id',methods=['DELETE'])(remover_mesa)
