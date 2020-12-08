import jwt
import datetime

from flask import Flask, request, render_template, redirect, url_for, make_response, Blueprint, g
from expense_control.repositories.expense_repository import ExpenseRepository
from expense_control.shared.token_required import token_required
from expense_control.controller.tasks.create_expense import create_expense

app = Blueprint('expense', __name__)


@app.route('/')
@token_required
def index():
    return render_template('index.html', user_name=g.current_user.name)


@app.route('/expense_history')
@token_required
def expense_history():
    expenses = ExpenseRepository().get_all(user_id=g.current_user.id)
    return render_template('expense_history.html', expenses=expenses, user_name=g.current_user.name)


@app.route('/unpaid_expenses')
@token_required
def unpaid_expenses():
    expenses = ExpenseRepository().get_unpaid_expenses(user_id=g.current_user.id)
    return render_template('unpaid_expenses.html', expenses=expenses, date=datetime.datetime.now(), user_name=g.current_user.name)


@app.route('/expense', methods=['POST'])
@token_required
def save_expense():
    value = request.form['value']
    description = request.form['description']
    due = request.form['due']

    create_expense.delay(value, description, due, g.current_user.id)
    return redirect(url_for('expense.index'))


@app.route('/expense/<expense_id>/pay', methods=['POST'])
@token_required
def pay_expense(expense_id):
    expense = ExpenseRepository().get_by_id(expense_id, g.current_user.id)
    expense.pay()
    expense.update()

    return redirect(url_for('expense.unpaid_expenses'))
