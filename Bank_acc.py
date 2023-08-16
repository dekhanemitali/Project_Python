class Bank_acc:
    _accno = None
    _amount = None

    print("----Welcome to Bank----")
    def __init__(self,accno,Initialbal):
        self._accno=accno
        self._amount=Initialbal
    def showInitial(self):
        print("Your "+str(self._accno)+" Account is successfully created with " + str(self._amount) + "rs. amount")

    def deposit(self, amount):
        self._amount = self._amount + amount
        print(str(amount)+" rs is deposited to your Bank "+str(self._accno)+" Account")
        print("Your Account Balance is "+str(self._amount))

    def check_bal(self):
        print("Current balance "+str(self._amount)+"rs. is in your Account "+str(self._accno))

    def withdraw(self, amount):
        if amount <= self._amount:
            self._amount -= amount
            print(str(amount)+" rs. is withdraw from Bank Account "+str(self._accno))
           # print("after Withdraw Your balance is "+str(self._amount))
        else:
            print("Insufficient amount in your account")

    def transfer(self, amount, account):
        if amount <= self._amount:
            self.withdraw(amount)
            account.deposit(amount)
            print("The "+str(amount)+" is transfered from your Bank Account")
        else:
            print("Insufficient amount in your account")









            # print("Your total  amount is "+str(self.__balance))
    """    print("Your Account is created with "+str(self.__amount)+" amount")
    def __init__(self,balance,amount):
        self.__balance=balance
        self.__Total=amount+balance

    def showDepcash(self):
        print("The Account balance is "+str(self.__balance) +" And The amount is "+str(self.__amount))
        print("The total Account balance is "+str(self.__Total))
    """