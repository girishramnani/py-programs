__author__ = 'Girish'

class Account:
    def __init__(self,name,account,pin,balance=0.0):
        self.name = name
        self.account = account
        self.pin = pin
        self.balance = balance
    def __lt__(self, other):
        if isinstance(other,Account):
            return self.name < other.name


t = Account("griihs","savig",3434)
t2 = Account("agriihs","savig",3434)




