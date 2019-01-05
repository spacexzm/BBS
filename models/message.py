import time

from sqlalchemy import Column, Unicode, UnicodeText, Integer

from models.base_model import SQLMixin, db


class Messages(SQLMixin, db.Model):
    title = Column(Unicode(50), nullable=False)
    content = Column(UnicodeText, nullable=False)
    sender_id = Column(Integer, nullable=False)
    receiver_id = Column(Integer, nullable=False)
