from flask import Blueprint, Flask
from flask_restplus import Api

from controller.jurnalController import api as jurnal
from controller.userController import api as user
from controller.BookController import api as book
from controller.ahliController import api as ahli
from controller.penerbitController import api as penerbit

app = Flask(__name__)
blueprint = Blueprint('api', __name__)
api = Api(blueprint, title='MALESNUGAS API Documentation',
          version='1.0',
          description='MALESNUGAS API')


api.add_namespace(jurnal,'/jurnal')
api.add_namespace(user,'/user')
api.add_namespace(book,'/book')
api.add_namespace(ahli,'/ahli')
api.add_namespace(penerbit,'/penerbit')


app.register_blueprint(blueprint)