
class Config(object):
    SECRET_KEY = 'my_secret_key'
    SECURITY_PASSWORD_SALT = 'my_password_salt'
    MAIL_SERVER = 'smtp.gmail.com:587'

    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:feryganteng1234@localhost:5432/malesnugas'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_POOL_SIZE = 30
    SQLALCHEMY_POOL_TIMEOUT = 30  # 30 seconds
    SQLALCHEMY_POOL_RECYCLE = 10  # max connection idle
    SQLALCHEMY_MAX_OVERFLOW = 50  # max in queue
    JSON_SORT_KEYS = False

    forwarded_allow_ips = '*'
    secure_scheme_headers = {'X-Forwarded-Proto': 'https'}



account_sid = 'AC3eb0ddad4b5a815c8c463b2d52133133'
auth_token = '1936011218679298a9630dd69ea07aab'
twilio_number = '+19803242957'
my_phone_number = '081291522042'