from flask import jsonify, request
from flask_restplus import Namespace, Resource
from service.userService import List, create_user, login, token_required



api = Namespace('User API')

auth_header = {'token': {'name': 'token',
                           'in': 'header',
                           'type': 'string',
                           'description': 'Token JWT!'}}





@api.doc(params=auth_header)
@api.route('/list-user')
class ListCountryController(Resource):
    @staticmethod
    def get():
        token = None
        if 'token' in request.headers:
            token = request.headers['token']

        if not token:
            response = jsonify({'code': '-1', 'msg': 'Token is missing!'})
            response.status_code = 401
            return response

        current_user = token_required(token)

        if not current_user:
            response = jsonify({'code': '-1', 'msg': 'Token is invalid!'})
            response.status_code = 401
            return response
        data = List()

        if data:
            return jsonify(
                {'code': '1', 'msg': 'Get Data Successfull!', 'data':data})

        return jsonify(
            {'code': '0', 'msg': 'Data Not Found!', 'data': []})





@api.doc(params=auth_header)
@api.route('/create-user')
class createUserController(Resource):
    @staticmethod
    def post():
        param = request.json

        data = create_user(param, 1)
        return data



@api.doc(params=auth_header)
@api.route('/login')
class loginUserController(Resource):
    @staticmethod
    def post():
        param = request.json

        data = login(param)
        return data
 