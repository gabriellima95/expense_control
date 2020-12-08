from expense_control.shared.repository import Repository
from expense_control.models.expense import Expense


class ExpenseRepository(Repository):

    _entity = Expense

    def get_by_id(self, id, user_id):
        return self.query(self._entity).filter_by(user_id=user_id).filter_by(id=id).first()

    def get_all(self, user_id):
        return self.query(self._entity).filter_by(user_id=user_id).order_by(Expense.due.desc()).all()

    def get_unpaid_expenses(self, user_id):
        return self.query(self._entity).filter_by(user_id=user_id).filter_by(paid=False).order_by(Expense.due.asc()).all()
