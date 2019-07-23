class Bank:
    def __init__(self, firstname, lastname, accountnumber, balance):
            self.firstname = firstname
            self.lastname = lastname
            self.accountnumber = accountnumber
            self.balance = balance
            self.transaction = []


    def deposit(self , addmoney):
        print(f"Adding money {addmoney} to  existing balance {self.balance}")
        self.balance +=  addmoney
        self.transaction.append(+addmoney)

    def withdraw(self, removemoney):
        print(f"Removing money {removemoney} from current balance {self.balance}")
        self.balance = self.balance - removemoney
        self.transaction.append(-removemoney)

    def recent_transaction(self):
        print(f"Current Balance is {self.balance}")
        print("Recent 2 transactions are ")
        self.transaction.reverse()
        for i in range(2):
          print(self.transaction[i])



if __name__ == "__main__":

    b = Bank("Poonam", "Yadav", "pooyadav1006885", 100000)
    b.deposit(100000)
    b.withdraw(500)
    b.recent_transaction()







