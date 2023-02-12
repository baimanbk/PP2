class Account():
    def __init__(self, owner:str, balance = 0):
        self.owner = owner
        self.balance = balance
    def dep(self, add):
        self.add = add
        self.balance = self.balance + add
    def withdr(self, withdraw):
        self.withdraw = withdraw
        if(self.balance - withdraw >= 0):
            self.balance = self.balance - withdraw
            print("money withdrawn")
            print('осталось на карте: ' + str(self.balance))
        else:
            print('not enough money')
    def info(self):
        print('name: ' + self.owner)
        print('balance: ' + str(self.balance))

p = Account('Baisal', 300)
p.dep(200)
p.withdr(600)
p.info()     