import jwt
import datetime

from flask import Flask, request, render_template, redirect, url_for, make_response, Blueprint
from expense_control.models.expense import Expense

app = Blueprint('expense', __name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/expense_history')
def expense_history():
    expenses = Expense().get_all()
    return render_template('expense_history.html', expenses=expenses)


@app.route('/unpaid_expenses')
def unpaid_expenses():
    expenses = Expense().get_unpaid_expenses()
    return render_template('unpaid_expenses.html', expenses=expenses, date=datetime.datetime.now())


@app.route('/expense', methods=['POST'])
def create_expense():
    value = request.form['value']
    description = request.form['description']
    due = request.form['due']

    expense = Expense(value=value, description=description, due=due)
    expense.create()
    return redirect(url_for('expense.index'))


@app.route('/expense/<expense_id>/pay', methods=['POST'])
def pay_expense(expense_id):
    expense = Expense().get_by_id(expense_id)
    expense.pay()
    expense.update()

    return redirect(url_for('expense.unpaid_expenses'))
