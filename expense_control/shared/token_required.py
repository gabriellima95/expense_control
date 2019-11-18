import jwt
import datetime

from flask import request, jsonify
from flask import current_app as app
from functools import wraps

from .db import db
from .user import User
from .repository import Repository


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('X-Access-Token')

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = db.session.query(User).filter_by(public_id=data['public_id']).first()
        except:
            return jsonify({'error': 'Token is Invalid'}), 401

        return f(current_user, *args, **kwargs)

    return decorated
