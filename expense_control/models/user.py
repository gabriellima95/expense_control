from expense_control.shared.repository import Repository


class User:
    id = None
    name = None
    password = None

    def __init__(self, **kwargs):
        for key in kwargs:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

    def create(self):
        Repository().create(self)
