import jwt
import datetime

from flask import request, jsonify, redirect, url_for, g
from flask import current_app as app
from functools import wraps

from expense_control.repositories.user_repository import UserRepository


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try:
            cookie = request.headers.get('Cookie')
            token = cookie.split('=')[-1]
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = UserRepository().get_by_id(data['id'])
        except Exception:
            return redirect(url_for('user.login'))
        g.current_user = current_user

        return f(*args, **kwargs)

    return decorated
