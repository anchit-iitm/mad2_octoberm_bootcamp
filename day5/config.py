
class Config():
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = None

class LocalDev(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite3'

    SECRET_KEY = 'super-secret'
    SECURITY_TRACKABLE = True
    # SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authorization'


class ProdDev(Config):

    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.sqlite3'

    # SECRET_KEY = get.env