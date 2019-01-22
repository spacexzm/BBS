import time
from datetime import timedelta

from flask import Flask
# from flask_admin import Admin
# from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from admin import UserModelView, TopicModelView
import config

# web framework
# web application
# __main__
import secret
from models.base_model import db
from models.reply import Reply
from models.topic import Topic
from models.user import User
from models.board import Board
from routes import index
from utils import log

"""
在 flask 中，模块化路由的功能由 蓝图（Blueprints）提供
蓝图可以拥有自己的静态资源路径、模板路径（现在还没涉及）
用法如下
"""
# 注册蓝图
# 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀
# import routes.index as index_view
from routes.index import main as index_routes
from routes.topic import main as topic_routes
from routes.reply import main as reply_routes
from routes.user import main as user_routes
from routes.message import main as mail_routes, mail
from routes.index import not_found

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# db = SQLAlchemy(app)


# @app.template_filter()
def count(input):
    log('count using jinja filter')
    return len(input)


def format_time(unix_timestamp):
    # enum Year():
    #     2013
    #     13
    # f = Year.2013
    f = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(unix_timestamp)
    formatted = time.strftime(f, value)
    return formatted


def configured_app():
    app = Flask(__name__)
    # 设置 secret_key 来使用 flask 自带的 session
    # 这个字符串随便你设置什么内容都可以
    app.secret_key = config.secret_key

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{}@localhost/web19?charset=utf8mb4'.format(
        secret.database_password
    )
    db.init_app(app)
    migrate = Migrate(app, db)

    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=1)

    app.template_filter()(count)
    app.template_filter()(format_time)
    app.errorhandler(404)(not_found)

    # app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    # admin = Admin(app, name='web19', template_mode='bootstrap3')
    # user_mv = UserModelView(User, db.session)
    # topic_mv = TopicModelView(Topic, db.session)
    #
    # admin.add_view(user_mv)
    # admin.add_view(topic_mv)
    # admin.add_view(ModelView(Board, db.session))
    # admin.add_view(ModelView(Reply, db.session))
    # admin.add_view(ModelView(Topic, db.session))
    # admin.add_view(ModelView(Reply, db.session))
    # Add administrative views here
    app.config['MAIL_SERVER'] = 'smtp.exmail.qq.com'
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USERNAME'] = config.admin_mail
    app.config['MAIL_PASSWORD'] = secret.mail_password

    mail.init_app(app)

    register_routes(app)
    return app


def register_routes(app):
    """
        在 flask 中，模块化路由的功能由 蓝图（Blueprints）提供
        蓝图可以拥有自己的静态资源路径、模板路径（现在还没涉及）
        用法如下
        """
    # 注册蓝图
    # 有一个 url_prefix 可以用来给蓝图中的每个路由加一个前缀
    app.register_blueprint(index_routes)
    app.register_blueprint(topic_routes, url_prefix='/topic')
    app.register_blueprint(reply_routes, url_prefix='/reply')
    app.register_blueprint(user_routes, url_prefix='/user')
    app.register_blueprint(mail_routes, url_prefix='/mail')


# 运行代码
if __name__ == '__main__':
    # app.add_template_filter(count)
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    # 自动 reload jinja
    app = configured_app()
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    config = dict(
        debug=False,
        host='localhost',
        port=3000,
    )
    app.run(**config)
