from entity.model import User
from entity import db
from flask import jsonify
import datetime
import codecs
import validators
import bcrypt
import jwt
import sqlalchemy
import json



def token_required(token):
    try:
        data = jwt.decode(token, secrets)
        current_user = User.query.filter_by(id=data['id']).first()
    except:
        current_user = None
    return current_user

secrets = 'secretindependent'





def List():
    data = []
    query = db.session.query(User).filter(
        User.deleted_date == None).all()

    for x in query:
        data.append({
            'id': x.id,
            'username': x.username,
            'fullName': x.full_name,
            'email': x.email,
            'notlp': x.notlp,
            'gender': x.gender,
        })

    return data



def create_user(param, current_user):
    password = param['password'].encode("utf-8")
    pw_hash = bcrypt.hashpw(password, bcrypt.gensalt())

    # Username
    if param['userName'] is None:
        return jsonify({'msg': 'Username cannot be empty', 'code': '-1'})
    if len(param['userName']) > 40:
        return jsonify({'error': "Max char username is 40"})

    # Fullname
    if param['fullName'] is None:
        return jsonify({'msg': 'Full name cannot be empty', 'code': '-1'})
    if len(param['fullName']) > 100:
        return jsonify({'error': "Max char full name is 100"})


    # email
    if param['email'] is None:
        return jsonify({'msg': 'Email cannot be empty', 'code': '-1'})
    if not validators.email(param['email']):
        return jsonify({'error': "Email is not valid"})



    username_validation = User.query.filter_by(username=param['userName']).first()
    if username_validation:
       return jsonify({'msg': 'Username already exist!', 'code': '-1'})

    email_validation = User.query.filter_by(email=param['email']).first()
    if email_validation:
        return jsonify({'msg': 'Email already exist!', 'code': '-1'})

    try:
        create = User(
            username=param['userName'].lower(),
            password=pw_hash.decode("utf-8"),
            full_name=param['fullName'],
            gender=param['gender'],
            notlp=param['notlp'],
            email=param['email'])
        
    
        db.session.add(create)
        db.session.commit()

        if create:
            user = db.session.query(User.id,User.username).filter(User.username == create.username)
            for x in user:
           
                token = jwt.encode(
                    {'id': x.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1440)},
                    secrets)

                a = codecs.decode(token, 'UTF-8')
                token_user = a.replace('b', '')
                token_user = a.replace("'", "")
    

        return jsonify({'code': '1', 'msg': 'Data Success Created!','token':f'{token_user}'})
    except sqlalchemy.exc.DataError:
        return jsonify({'msg': 'Data Failed Created!', 'code': '-1'})
    except sqlalchemy.exc.IntegrityError as err:
        return jsonify({'msg': str(err.__cause__), 'code': '-1'})

 
from bcrypt import hashpw

def login(param):
    try:
        username = param['userName']
        password = param['password']

        query = User.query.filter_by(username=username).first()

        if not query:
            return 'Username not found'
        
        if query.password == hashpw(password.encode('UTF_8'), query.password.encode('UTF_8')).decode():

            token = jwt.encode(
                    {'id': query.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=1440)},
                    secrets)

            a = codecs.decode(token, 'UTF-8')
            token_user = a.replace('b', '')
            token_user = a.replace("'", "")
            
            return jsonify({'code': '1', 'msg': 'Login success!', 'token': f'{token_user}'})
        else:
            return 'Wrong password'
        
    except sqlalchemy.exc.DataError:
        return jsonify({'msg': 'Failed to Login!', 'code': '-1'})
    except sqlalchemy.exc.IntegrityError as err:
        return jsonify({'msg': str(err.__cause__), 'code': '-1'})
    
        