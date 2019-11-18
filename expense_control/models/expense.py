from expense_control.shared.repository import Repository


class Expense:
    id = None
    value = None
    description = None
    due = None
    paid = None
    user_id = None

    def __init__(self, **kwargs):
        for key in kwargs:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

    def create(self):
        Repository().create(self)

    def update(self):
        Repository().update(self)

    def get_all(self):
        return Repository().query(self.__class__).order_by(self.__class__.due.desc()).all()

    def get_unpaid_expenses(self):
        return Repository().query(self.__class__).filter_by(paid=False).order_by(self.__class__.due.asc()).all()

    def get_by_id(self, id):
        return Repository().query(self.__class__).filter_by(id=id).first()

    def pay(self):
        self.paid = True
