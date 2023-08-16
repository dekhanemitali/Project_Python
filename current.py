from Bank_acc import Bank_acc
class current(Bank_acc):
    _accno=None
    def __init__(self,accno,Initialbal):
        super().__init__(accno, Initialbal)
        print("Your "+str(accno)+" Current Account Created successfully with initial amount"+str(self._amount))

    def currentwithdraw(self, amount):
        amount +=200
        print("After every withdraw 200rs charges are applicable")
        self.withdraw(amount)
