from flask import Flask, request
from config import Config
from controller import blueprint
from entity import db
from flask_cors import CORS
import logging




application = Flask(__name__, static_url_path='/static')
application.config.from_object(Config)
db.init_app(application)
application.register_blueprint(blueprint)
CORS(application, resources={r"/*": {"origins": "*"}})




if __name__ == "__main__":
    # port = int(os.environ.get('PORT', 33507))
    application.run(debug=True)