from flask import Blueprint, Flask
from flask_restplus import Api

from controller.jurnalController import api as jurnal

app = Flask(__name__)
blueprint = Blueprint('api', __name__)
api = Api(blueprint, title='LMS-EXTERNAL-SERVICE API Documentation',
          version='1.0',
          description='LMS-EXTERNAL-SERVICE API for LMS')


api.add_namespace(jurnal,'/jurnal')


app.register_blueprint(blueprint)