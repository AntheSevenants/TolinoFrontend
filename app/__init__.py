from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app(debug=False):
    """Create an application."""
    app = Flask(__name__)
    app.debug = debug
    app.config['SECRET_KEY'] = 'miep'

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/tolino')

    socketio.init_app(app)
    return app