# from entity.model import User
from entity import db
import jwt

secrets = 'secretindependent'

def token_required_jwt(token):
    try:
        payload = jwt.decode(token, secrets)
        if not payload['id']:
            return None
    except:
        payload = None
    return payload