from Bank_acc import Bank_acc
class SavingAcc(Bank_acc):
    __acc=None

    def __init__(self,accno,Initialbal):
        super().__init__(accno,Initialbal)
        print("Your "+str(self._accno)+" Saving Account Created successfully with"+str(self._amount))

    def savedeposit(self, amount):
        intrest = amount * 3/100
        amount += intrest
        print(str(intrest)+"Interest added successfully in your account")
        self.deposit(amount)