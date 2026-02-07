import os


class DevelopmentConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:199716128@localhost/microblog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTS_PER_PAGE = 3

    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'false').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    LANGUAGES = ['en', 'zh']


class TestingConfig(object):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SERVER_NAME = 'localhost.test'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
