import os
import uuid

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
    abort)
from werkzeug.datastructures import FileStorage

from routes import current_user, csrf_required, new_csrf_token
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


@main.route('/setting')
def setting():
    u = current_user()
    token = new_csrf_token()
    return render_template('settings.html', user = u, token = token)


@main.route('/profile', methods=['POST'])
@csrf_required
def profile():
    form = request.form
    u = current_user()
    User.update(u.id, username = form['username'], signature = form['signature'])
    return redirect(url_for('.setting'))


@main.route('/change_password', methods=['POST'])
@csrf_required
def change_password():
    form = request.form
    u = current_user()
    if u.password == User.salted_password(form['old_pass']):
        new_pass = User.salted_password(form['new_pass'])
        User.update(u.id, password = new_pass)
        return redirect(url_for('.setting'))
    else:
        abort(401)


@main.route('/change_avatar', methods=['POST'])
@csrf_required
def change_avatar():
    file: FileStorage = request.files['avatar']

    suffix = file.filename.split('.')[-1]
    filename = '{}.{}'.format(str(uuid.uuid4()), suffix)
    path = os.path.join('images', filename)
    file.save(path)

    u = current_user()
    User.update(u.id, image='/images/{}'.format(filename))

    return redirect(url_for('.setting'))


