from flask import request, jsonify
from flask_restplus import Namespace, Resource
from controller.support import token_required_jwt
from service.ahliService import list_ahli, Detail, Create, Edit, Delete


api = Namespace('Jurnal API')

auth_header = {'x-corpu': {'name': 'x-corpu',
                           'in': 'header',
                           'type': 'string',
                           'description': 'Token JWT!'}}



@api.route('/list')
@api.doc(params=auth_header)
class ListController(Resource):
    @staticmethod
    def get():
        token = None
        if 'x-corpu' in request.headers:
            token = request.headers['x-corpu']

        if not token:
            response = jsonify({'code': '-1', 'msg': 'Token is missing!'})
            response.status_code = 401
            return response

        check_token = token_required_jwt(token)
        if not check_token:
            response = jsonify({'code': '-1', 'msg': 'Token is invalid!'})
            response.status_code = 401
            return response

        user_id = check_token['id']
        jurnal_list = list_ahli()

        if len(jurnal_list) > 0:
            return jsonify(
                {'code': '1', 'msg': 'Get Data Successfull!', 'data': jurnal_list})
        return jsonify(
            {'code': '0', 'msg': 'Data Empty!', 'data': []})




@api.route('/detail/<int:id>')
@api.doc(params=auth_header)
class DetailController(Resource):
    @staticmethod
    def get(id):
        token = None
        if 'x-corpu' in request.headers:
            token = request.headers['x-corpu']

        if not token:
            response = jsonify({'code': '-1', 'msg': 'Token is missing!'})
            response.status_code = 401
            return response

        check_token = token_required_jwt(token)
        if not check_token:
            response = jsonify({'code': '-1', 'msg': 'Token is invalid!'})
            response.status_code = 401
            return response

        user_id = check_token['id']

        category_req = Detail(id)

        if category_req:
            return jsonify(
                {'code': '1', 'msg': 'Get Data Successfull!', 'data': category_req})

        return jsonify(
            {'code': '0', 'msg': 'Data Not Found!', 'data': []})


@api.route('/create')
@api.doc(params=auth_header)
class CreateController(Resource):
    def post(data):
        token = None
        if 'x-corpu' in request.headers:
            token = request.headers['x-corpu']

        if not token:
            response = jsonify({'code': '-1', 'msg': 'Token is missing!'})
            response.status_code = 401
            return response

        check_token = token_required_jwt(token)
        if not check_token:
            response = jsonify({'code': '-1', 'msg': 'Token is invalid!'})
            response.status_code = 401
            return response

        user_id = check_token['id']

        param = request.get_json()
        category_req = Create(param, user_id)

        if category_req:
            response = jsonify({'code': '1', 'msg': 'Data Created!'})
            response.status_code = 201
            return response

        response = jsonify({'code': '-1', 'msg': 'Data Fail to Create!'})
        response.status_code = 400
        return response
        


@api.route('/edit/<int:id>')
@api.doc(params=auth_header)
class EditController(Resource):
    @staticmethod
    def put(id):
        token = None
        if 'x-corpu' in request.headers:
            token = request.headers['x-corpu']

        if not token:
            response = jsonify({'code': '-1', 'msg': 'Token is missing!'})
            response.status_code = 401
            return response

        check_token = token_required_jwt(token)
        if not check_token:
            response = jsonify({'code': '-1', 'msg': 'Token is invalid!'})
            response.status_code = 401
            return response

        user_id = check_token['id']

        param = request.get_json()
        category_req = Edit(id, param, user_id)

        if category_req:
            response = jsonify({'code': '1', 'msg': 'Data Updated!'})
            response.status_code = 200
            return response

        if category_req is None:
            return jsonify(
            {'code': '0', 'msg': 'Data Not Found!'})

        response = jsonify({'code': '-1', 'msg': 'Data Fail to Update!'})
        response.status_code = 400
        return response


@api.route('/delete/<int:id>')
@api.doc(params=auth_header)
class DeleteController(Resource):
    @staticmethod
    def delete(id):
        token = None
        if 'x-corpu' in request.headers:
            token = request.headers['x-corpu']

        if not token:
            response = jsonify({'code': '-1', 'msg': 'Token is missing!'})
            response.status_code = 401
            return response

        check_token = token_required_jwt(token)
        if not check_token:
            response = jsonify({'code': '-1', 'msg': 'Token is invalid!'})
            response.status_code = 401
            return response

        user_id = check_token['id']

        category_req = Delete(id)

        if category_req:
            response = jsonify({'code': '1', 'msg': 'Data Deleted!'})
            response.status_code = 200
            return response

        if category_req is None:
            return jsonify(
            {'code': '0', 'msg': 'Data Not Found!'})

        response = jsonify({'code': '-1', 'msg': 'Data Fail to Delete!'})
        response.status_code = 400
        return response