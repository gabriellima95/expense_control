from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID

from expense_control.models.expense import Expense


def create_application(config={}):
    app = Flask(__name__)
    app.config.update(config)
    return app


app = create_application(
    config={
        'SECRET_KEY': 'chavesecreta',
        'SQLALCHEMY_DATABASE_URI': 'postgres://xazyzadt:5bBes4cKS89EEqRWgHTVYkC_CZY2Z9kA@salt.db.elephantsql.com:5432/xazyzadt'
    }
)

db = SQLAlchemy()


expenses_mapping = db.Table(
    'expenses',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('value', db.Float),
    db.Column('description', db.String(255)),
    db.Column('due', db.DateTime())
)

db.mapper(Expense, expenses_mapping)
