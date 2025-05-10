from flask import Flask
from blueprints.jugador.routes import jugador_bp
from blueprints.mesa.routes import mesa_bp 
from blueprints.juego.routes import juego_bp
from blueprints.ronda.routes import ronda_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(jugador_bp)
    app.register_blueprint(mesa_bp)
    app.register_blueprint(juego_bp)
    app.register_blueprint(ronda_bp)

    return app