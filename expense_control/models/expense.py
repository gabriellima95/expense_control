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

    def pay(self):
        self.paid = True
