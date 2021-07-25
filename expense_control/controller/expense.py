import datetime

from flask import request, render_template, redirect, url_for, Blueprint, g
from expense_control.repositories.expense_repository import ExpenseRepository
from expense_control.models.expense import Expense
from expense_control.shared.token_required import token_required

app = Blueprint('expense', __name__)


@app.route('/')
@token_required
def index():
    return render_template('index.html', user_name=g.current_user.name)


@app.route('/expense_history')
@token_required
def expense_history():
    expenses = ExpenseRepository().get_all(user_id=g.current_user.id)
    expenses_categories = {}
    for e in expenses:
        if expenses_categories.get(e.category.value):
            expenses_categories[e.category.value] += e.value
        else:
            expenses_categories[e.category.value] = e.value
    return render_template('expense_history.html', expenses=expenses, expenses_categories=expenses_categories,user_name=g.current_user.name)


@app.route('/unpaid_expenses')
@token_required
def unpaid_expenses():
    expenses = ExpenseRepository().get_unpaid_expenses(user_id=g.current_user.id)
    total_amount = 0
    for expense in expenses:
        total_amount += expense.value
    return render_template('unpaid_expenses.html', total_amount=total_amount ,expenses=expenses, date=datetime.datetime.now(), user_name=g.current_user.name)


@app.route('/expense', methods=['POST'])
@token_required
def save_expense():
    value = request.form['value']
    description = request.form['description']
    due = request.form['due']
    category = request.form['category']

    expense = Expense(value=value, description=description, due=due, category=category, user_id=g.current_user.id)
    ExpenseRepository().create(expense)
    return redirect(url_for('expense.index'))


@app.route('/expense/<expense_id>/pay', methods=['POST'])
@token_required
def pay_expense(expense_id):
    expense = ExpenseRepository().get_by_id(expense_id, g.current_user.id)
    expense.pay()
    ExpenseRepository().update(expense)

    return redirect(url_for('expense.unpaid_expenses'))
