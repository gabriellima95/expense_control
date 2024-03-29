from expense_control import celery
from expense_control.models.expense import Expense
from expense_control.repositories.expense_repository import ExpenseRepository


@celery.task
def create_expense(value, description, due, user_id):
    expense = Expense(value=value, description=description, due=due, user_id=user_id)
    ExpenseRepository().create(expense)
