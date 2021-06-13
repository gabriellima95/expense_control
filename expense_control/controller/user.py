import jwt
import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask import (
    Flask, request, render_template,
    redirect, url_for, make_response,
    Blueprint, jsonify
)
from expense_control.models.user import User
from expense_control.repositories.user_repository import UserRepository
from expense_control.config.config import SECRET_KEY

app = Blueprint('user', __name__)


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/user', methods=['POST'])
def create_user():
    name = request.form['name']
    username = request.form['username']
    hash_password = generate_password_hash(request.form['password'])

    user = User(
        name=name,
        username=username,
        password=hash_password
    )
    UserRepository().create(user)

    token = __generate_token(user.id)
    response = make_response(redirect('/'))
    response.set_cookie('X-Access-Token', token)

    return response


@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']

    user = UserRepository().get_by_username(username)

    if not user:
        return redirect('/login')

    if not check_password_hash(user.password, password):
        return redirect('/login')

    token = __generate_token(user.id)
    response = make_response(redirect('/'))
    response.set_cookie('X-Access-Token', token)

    return response


@app.route('/signout')
def signout():
    response = make_response(redirect('/login'))
    response.set_cookie('X-Access-Token', '', expires=0)

    return response


def __generate_token(user_id):
    token = jwt.encode(
        {
            'id': str(user_id),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        },
        SECRET_KEY,
        algorithm="HS256"
    )
    return token
