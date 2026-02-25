from app import db, create_app
from app.models import User, Post
from app.cli import register
from config import DevelopmentConfig


app = create_app(DevelopmentConfig)
register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    app.run()
