# 从 app 包中导入 app 对象 -> app = Flask(__name__)
from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'zhoudashuai'}
    posts = [  # 创建一个帖子列表,里面的元素是两个字典,每个字典里的元素还是字典: 作者,帖子内容
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
