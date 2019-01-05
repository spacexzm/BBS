import flask_mail
from flask import (
    render_template,
    request,
    redirect,
    url_for,
    Blueprint,
)

from routes import *
from config import admin_mail
from models.message import Messages
# from config import admin_mail

main = Blueprint('mail', __name__)
mail = flask_mail.Mail()


@main.route("/add", methods=["POST"])
def add():
    form = request.form.to_dict()
    form['receiver_id'] = int(form['receiver_id'])
    u = current_user()
    form['sender_id'] = u.id

    # # 发邮件
    r = User.one(id=form['receiver_id'])
    m = flask_mail.Message(
        subject=form['title'],
        body=form['content'],
        sender=admin_mail,
        recipients=[r.email]
    )
    mail.send(m)

    Messages.new(form)
    return redirect(url_for('.index'))


@main.route('/')
def index():
    u = current_user()

    send = Messages.all(sender_id=u.id)
    received = Messages.all(receiver_id=u.id)

    t = render_template(
        'mail/index.html',
        send=send,
        received=received,
    )
    return t


@main.route('/view/<int:id>')
def view(id):
    message = Messages.one(id=id)
    u = current_user()
    # if u.id == mail.receiver_id or u.id == mail.sender_id:
    if u.id in [message.receiver_id, message.sender_id]:
        return render_template('mail/detail.html', message=message)
    else:
        return redirect(url_for('.index'))
