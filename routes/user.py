from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import current_user
from models.topic import Topic
from models.reply import Reply
from models.user import User

main = Blueprint('gua_user', __name__)

@main.route('/<string:username>')
def user(username):
    u = User.one(username = username)
    t = Topic.all(user_id = u.id)
    r = Reply.all(user_id = u.id)
    rt = []
    for v in r:
        reply_topic = Topic.one(id = v.topic_id)
        if reply_topic not in rt:
            rt.append(reply_topic)
    t.reverse()
    rt.reverse()
    return render_template('user.html', user = u, topics = t, reply_topics = rt)