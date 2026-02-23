from flask import Flask
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

pymysql.install_as_MySQLdb()


from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)
print("✓ Errors blueprint registered")


from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')
print("✓ Auth blueprint registered")


from app.main import bp as main_bp
app.register_blueprint(main_bp)
print("✓ Main blueprint registered")


def get_locale():
    # return request.accept_languages.best_match(app.config['LANGUAGES'])
    return 'zh_CN'


babel = Babel(app, locale_selector=get_locale)

login.login_view = 'auth.login'
login.login_message = _l('Please log in to access this page.')


# 导入一个新模块 models, 用来定义数据库的结构
from app import models
from app.main import routes
