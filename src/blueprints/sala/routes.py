from flask import Blueprint,jsonify
from controller import agregar_sala,obtener_sala,remover_sala,modificar_sala
sala_bp =Blueprint('sala',__name__,url_prefix='/sala')



sala_bp.route('/:id',methods=['GET'])(obtener_sala)

sala_bp.route('/add',methods=['POST'])(agregar_sala)

sala_bp.route('/:id',methods=['PUT'])(modificar_sala)

sala_bp.route('/:id',methods=['DELETE'])(remover_sala)
