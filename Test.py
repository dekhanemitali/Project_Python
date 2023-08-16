from Bank_acc import Bank_acc
from Saving import SavingAcc
from current import current
bank1=Bank_acc(101,500)
bank1.showInitial()
bank1.withdraw(200)

print("----------------------------------------------------------------")
bank2=Bank_acc(102,200)
bank2.showInitial()
bank2.deposit(1000)
bank2.transfer(500,bank1)
print("Check balance")
bank1.check_bal()
bank2.check_bal()

print("__________________________________________")

s1=SavingAcc(1001,2000)
s1.savedeposit(500)
s1.check_bal()

print("-------------------------------------------------------------------")
c1=current(1002,2000)
c1.deposit(500)
c1.currentwithdraw(100)
c1.transfer(500,s1)
print("==================")
print("check saving and current account balance")
c1.check_bal()
s1.check_bal()



