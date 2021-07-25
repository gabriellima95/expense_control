import enum

class Expense:
    id = None
    value = None
    description = None
    due = None
    paid = None
    category = None
    user_id = None

    def __init__(self, **kwargs):
        self.category = ExpenseCategory(kwargs.get('category')) if kwargs.get('category') else ExpenseCategory.OTHER
    
        for key in kwargs:
            if hasattr(self, key):
                setattr(self, key, kwargs[key])

    def pay(self):
        self.paid = True

class ExpenseCategory(enum.Enum):

    OTHER = 'Outros'
    FOOD = 'Alimentaçao'
    TRANSPORT = 'Transporte'
    ENTERTAINMENT = 'Entreterimento'