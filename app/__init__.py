from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import pymysql


app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)


login.login_view = 'login'


pymysql.install_as_MySQLdb()


# 导入一个新模块 models, 用来定义数据库的结构
from app import routes, models
