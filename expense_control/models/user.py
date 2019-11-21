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

    def get_by_id(self, id):
        return Repository().query(self.__class__).filter_by(id=id).first()

    def get_by_username(self, username):
        return Repository().query(self.__class__).filter_by(username=username).first()
