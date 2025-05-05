from flask import Flask,jsonify,request
from src.ppt.state.globales import EstadoGlobal

app = Flask(__name__)


juegos_online = EstadoGlobal.crear_juego()


#Ruta para ingresar un jugador se necesita un body con nombre del usuario
@app.route('/game',methods=['POST'])
def ingresar():
    return jsonify()



#Ruta que inicializa el juego -Patron Singleton
@app.route('/game',methods=['GET'])
def logeo():
    return jsonify({'name':'12'})

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

if __name__ == '__main__':
    app.run(debug=True,port=4000)







