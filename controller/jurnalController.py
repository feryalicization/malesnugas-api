from flask import request, jsonify
from flask_restplus import Namespace, Resource
from controller.support import token_required_jwt
from service.jurnalService import list_jurnal


api = Namespace('Jurnal API')

auth_header = {'x-corpu': {'name': 'x-corpu',
                           'in': 'header',
                           'type': 'string',
                           'description': 'Token JWT!'}}



@api.route('/jurnal/list')
@api.doc(params=auth_header)
class ListLogActivityExpertController(Resource):
    @staticmethod
    def get():
        # token = None
        # if 'x-corpu' in request.headers:
        #     token = request.headers['x-corpu']

        # if not token:
        #     response = jsonify({'code': '-1', 'msg': 'Token is missing!'})
        #     response.status_code = 401
        #     return response

        # check_token = token_required_jwt(token)
        # if not check_token:
        #     response = jsonify({'code': '-1', 'msg': 'Token is invalid!'})
        #     response.status_code = 401
        #     return response

        # user_id = check_token['id']
        # # 439 Ruwanto, 62 Manupakpane
        jurnal_list = list_jurnal()

        if len(jurnal_list) > 0:
            return jsonify(
                {'code': '1', 'msg': 'Get Data Successfull!', 'data': jurnal_list})
        return jsonify(
            {'code': '0', 'msg': 'Data Empty!', 'data': []})



