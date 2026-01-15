from flask import Flask
from config import Config


app = Flask(__name__)
app.config.from_object(Config)


print('等会谁(哪个包或模块)在使用我: ', __name__)


from app import routes
