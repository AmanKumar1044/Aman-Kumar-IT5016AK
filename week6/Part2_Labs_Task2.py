class Account():
    def _init_(self,owner,balance):
        self.owner=owner
        self._balance=balance
    def deposit(self,ammount):
        if ammount>0:
           self._balance += ammount
           print(F"{ammount} deposited")
        else:
            print("Deposit must be positive")


    def withdraw(self,ammount):
        if 0<ammount<self._balance:
            self._balance -= ammount
            print(F"{ammount} withdrawn")
        else:
            print("Insufficient Balance or Invalid Ammount")
    def getbalance(self):
        return self._balance
account1 = Account("Moiz",5000)
account1.deposit(50)
print(account1.getbalance)
account1.withdraw(75)    
print(account1.getbalance)