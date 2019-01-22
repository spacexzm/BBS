from flask import (
    render_template,
    request,
    redirect,
    session,
    url_for,
    Blueprint,
    abort,
    send_from_directory)
from flask.json import jsonify

from models.user import User

from utils import log

main = Blueprint('index', __name__)


def current_user():
    # 从 session 中找到 user_id 字段, 找不到就 -1
    # 然后用 id 找用户
    # 找不到就返回 None
    uid = session.get('user_id', -1)
    u = User.one(id=uid)
    return u


"""
用户在这里可以
    访问首页
    注册
    登录

用户登录后, 会写入 session, 并且定向到 /profile
"""


@main.route("/")
def index():
    u = current_user()
    return render_template("index.html", user=u)


@main.route("/register", methods=['POST'])
def register():
    # form = request.args
    form = request.json
    # 用类函数来判断
    u = User.register(form)
    if u is None:
        response = jsonify({'register': False, 'error': '注册失败，用户名已存在'})
        return response
    else:
        response = jsonify({'register': True, 'message': '注册成功，请点击登录'})
        return response


@main.route("/login", methods=['POST'])
def login():
    print('request in login')
    form = request.json
    u = User.validate_login(form)
    if u is None:
        response = jsonify({'login': False, 'error': '登录失败，请检查账号和密码'})
        response.status_code = 401
        return response
    else:
        # session 中写入 user_id
        session['user_id'] = u.id
        # 设置 cookie 有效期
        session.permanent = True
        response = jsonify({'login': True, 'path': 'topic'})
        response.status_code = 200
        return response


@main.route("/logout")
def logout():
    session.pop('user_id')
    return redirect(url_for('bbs_topic.index'))


@main.route('/profile')
def profile():
    u = current_user()
    if u is None:
        return redirect(url_for('bbs_topic.index'))
    else:
        return render_template('profile.html', user=u)


@main.route('/user/<int:id>')
def user_detail(id):
    u = User.find(id)
    if u is None:
        abort(404)
    else:
        return render_template('profile.html', user=u)


def not_found(e):
    return render_template('404.html')


@main.route('/images/<filename>')
def image(filename):

    return send_from_directory('images', filename)


