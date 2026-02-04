from flask import Flask
from config import DevelopmentConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import pymysql
from flask_mail import Mail
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
mail = Mail(app)
bootstrap = Bootstrap(app)

login.login_view = 'login'

pymysql.install_as_MySQLdb()


# 导入一个新模块 models, 用来定义数据库的结构
from app import routes, models
