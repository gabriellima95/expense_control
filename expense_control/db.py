import uuid

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from expense_control.models.expense import Expense
from expense_control.models.user import User

db = SQLAlchemy()

expenses_mapping = db.Table(
    'expenses',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('value', db.Float),
    db.Column('description', db.String(255)),
    db.Column('due', db.DateTime()),
    db.Column('paid', db.Boolean(), default=False),
    db.Column(
        'user_id',
        UUID(as_uuid=True),
        db.ForeignKey('users.id'),
        nullable=False
    ),
)

db.mapper(Expense, expenses_mapping, properties={
    'user': relationship(User),
    'user_id': expenses_mapping.c.user_id
})

users_mapping = db.Table(
    'users',
    db.Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    db.Column('name', db.String(50)),
    db.Column('username', db.String(50)),
    db.Column('password', db.String(128))
)

db.mapper(User, users_mapping)
