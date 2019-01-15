from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from models.board import Board
from routes import *

from models.topic import Topic


main = Blueprint('bbs_topic', __name__)


@main.route("/")
def index():
    u = current_user()
    board_id = int(request.args.get('board_id', -1))
    if board_id == -1:
        ms = Topic.all()
    else:
        ms = Topic.all(board_id=board_id)
    boards = Board.all()
    return render_template("topic/index.html", ms=ms, user=u, boards=boards, bid=board_id)


@main.route('/<int:id>')
# /topic/1
# @main.route('/')
# /topic?id=1
# zhihu.com/question/1/answer/2/comment/3/xxx/y
def detail(id):
    # id = int(request.args['id'])
    # http://localhost:3000/topic/1
    # m = Topic.one(id=id)
    m = Topic.get(id)
    u = current_user()
    # 不应该放在路由里面
    # m.views += 1
    # m.save()

    # 传递 topic 的所有 reply 到 页面中
    return render_template("topic/detail.html", topic=m, user=u)


@main.route("/add", methods=["POST"])
def add():
    form = request.form.to_dict()
    u = current_user()
    m = Topic.add(form, user_id=u.id)
    return redirect(url_for('.detail', id=m.id))


@main.route("/new")
def new():
    board_id = int(request.args.get('board_id'))
    boards = Board.all()
    u = current_user()
    token = new_csrf_token()
    return render_template("topic/new.html", user=u, boards=boards, token=token, bid=board_id)

