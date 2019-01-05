from flask_admin.contrib.sqla import ModelView

from models.reply import Reply
from models.topic import Topic
from models.user import User
from models.board import Board

class UserModelView(ModelView):
    column_searchable_list = ('username', 'password')


class TopicModelView(ModelView):
    column_searchable_list = ('title', 'content', 'user_id', 'board_id')


