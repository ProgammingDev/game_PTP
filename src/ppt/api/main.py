from flask import Flask,jsonify,request
from ppt.state.globales import EstadoGlobal
from ppt.core.jugador import Jugador

app = Flask(__name__)

#Aplicar patron de arquitectura MODEL VIEW CONTROLLER

#Ruta para ingresar un jugador se necesita un body con nombre del usuario
@app.route('/game/usuario',methods=['POST'])
def crearUsuario():
    nombre= request.json['nombre']
    id = EstadoGlobal.agregar_usuario(nombre)
    return jsonify({"mensaje":"Jugador creado correctamente","id":id}),201



@app.route('/game/usuario/<id>',methods=['GET'])
def obtenerUsuario(id):
    id = int(id) 
    print(id)
    usuario:Jugador = EstadoGlobal.obtener_usuario(id)
    
    if(usuario): return jsonify({"mensaje":"Usuario encontrado correctamente","usuario":usuario.get_nombre()}),202
    
    return jsonify({"mensaje":"El usuario no fue encontrado con exito","usuario":None}),404




#-----------------SALAS------------------------
#MIDDLEWARE
#Ruta que inicializa el juego -Patron Singleton
@app.route('/game',methods=['POST'])
def crearSala():

    if EstadoGlobal.crear_juego(request.json):
        return jsonify({
            "mensaje":"Sala creada correctamente"
        }),201
    else:
        return jsonify({
            "mensaje":"Se ha generado un error en la creacion"
        }),404
    


#Ruta para obtener todas las salas creadas
@app.route('/game',methods=['GET'])
def obtenerSalas():
    juegos = EstadoGlobal.get_juegos()
    return jsonify(juegos)


















#Ruta para jugar una mano se necesita un body con respectiva jugada e id del jugador
@app.route('/game/jugar',methods=['POST'])
def jugar():

    body={
        "id":request.json['id'],
        "mano":request.json['mano']
    }

    return jsonify(body)

#Ruta que devuelve las estadisticas finales del juego
@app.route('/game/estadistica',methods=['GET'])
def obtenerEstadisticas():
    return jsonify({'estadisticas':'1'})







