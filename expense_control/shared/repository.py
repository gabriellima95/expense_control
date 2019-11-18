from .storage import Storage


class Repository:

    def __init__(self):
        self.session = Storage().session

    def save(self, entity):
        self.session.add(entity)
        self.session.commit()

        return entity

    def create(self, entity):
        self.save(entity)

    def update(self, entity):
        self.save(entity)

    def query(self, entity):
        return self.session.query(entity)
