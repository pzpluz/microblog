from flask import Flask
from flask import request
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import pymysql
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
babel = Babel(app)


def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'zh_CN'


babel.init_app(app, locale_selector=get_locale)

login.login_view = 'login'
login.login_message = _l('Please log in to access this page.')

pymysql.install_as_MySQLdb()

# 导入一个新模块 models, 用来定义数据库的结构
from app import routes, models, errors
