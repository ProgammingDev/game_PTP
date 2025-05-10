from flask import Blueprint,jsonify
from controller import agregar_mesa,obtener_mesa,remover_mesa,modificar_mesa,agregar_jugador_a_mesa
mesa_bp =Blueprint('sala',__name__,url_prefix='/mesa')


# METODOS GET
mesa_bp.route('/:id',methods=['GET'])(obtener_mesa)


# METODOS POST
mesa_bp.route('/add',methods=['POST'])(agregar_mesa)
mesa_bp.route('/<int:id_mesa>/jugador',methods=['POST'])(agregar_jugador_a_mesa)

# METODOS PUT
mesa_bp.route('/:id',methods=['PUT'])(modificar_mesa)


# METODOS DELETE
mesa_bp.route('/:id',methods=['DELETE'])(remover_mesa)
