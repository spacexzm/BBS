import uuid
from functools import wraps

from flask import session, request, abort

from models.user import User

import redis


csrf_cache = redis.StrictRedis()

def current_user():
    uid = session.get('user_id', '')
    u = User.one(id=uid)
    return u


def csrf_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token = request.args['token']
        u = current_user()
        print(type(u.id))
        if csrf_cache.exists(token) and int(csrf_cache.get(token)) == u.id:
            csrf_cache.delete(token)
            return f(*args, **kwargs)
        else:
            abort(401)

    return wrapper


def new_csrf_token():
    u = current_user()
    token = str(uuid.uuid4())
    csrf_cache.set(token, u.id)
    return token