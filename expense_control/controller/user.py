import jwt
import datetime

from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask, request, render_template, redirect, url_for, make_response, Blueprint
from expense_control.models.user import User

app = Blueprint('user', __name__)


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/user', methods=['POST'])
def create_user():
    name = request.form['name']
    username = request.form['usenname']
    hash_password = generate_password_hash(request.form['password'])

    user = User(
        name=name,
        username=username,
        password=hash_password
    )
    user.create()
    return render_template('signup.html')
