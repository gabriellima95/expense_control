from expense_control.shared.repository import Repository
from expense_control.models.user import User


class UserRepository(Repository):

    _entity = User

    def get_by_id(self, id):
        return self.query(self._entity).filter_by(id=id).first()

    def get_by_username(self, username):
        return self.query(self._entity).filter_by(username=username).first()
